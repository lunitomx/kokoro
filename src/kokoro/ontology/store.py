"""Persistence layer for coaching state.

Reads/writes `.kokoro/state.json` in the entrepreneur's project directory.
Uses atomic write (temp file + rename) to prevent corruption.
"""

from __future__ import annotations

import contextlib
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from kokoro.ontology.models import (
    CoachingNode,
    CoachingState,
    PhaseProgress,
    SkillCompletion,
)

KOKORO_DIR = ".kokoro"
STATE_FILE = "state.json"

# Which skills belong to which phase
PHASE_SKILLS: dict[int, list[str]] = {
    1: ["kokoro-diagnose", "kokoro-mountain", "kokoro-prune", "kokoro-finance"],
    2: ["kokoro-canvas", "kokoro-forces", "kokoro-interviews", "kokoro-validate"],
    3: ["kokoro-research", "kokoro-pescar", "kokoro-experiment", "kokoro-launch"],
    4: ["kokoro-factory", "kokoro-funnel", "kokoro-mafia", "kokoro-rhythm"],
}

# Skill dependency map: skill → list of source_skills whose nodes are relevant
SKILL_CONTEXT: dict[str, list[str]] = {
    "kokoro-diagnose": [],
    "kokoro-mountain": ["kokoro-diagnose"],
    "kokoro-prune": ["kokoro-diagnose", "kokoro-mountain"],
    "kokoro-finance": ["kokoro-prune"],
    "kokoro-canvas": [
        "kokoro-diagnose", "kokoro-mountain", "kokoro-prune", "kokoro-finance",
    ],
    "kokoro-forces": ["kokoro-canvas"],
    "kokoro-interviews": ["kokoro-canvas", "kokoro-forces"],
    "kokoro-validate": ["kokoro-canvas", "kokoro-forces", "kokoro-interviews"],
}

PHASE_NAMES: dict[int, str] = {
    1: "Preparar el Suelo",
    2: "Elegir la Semilla",
    3: "Germinar",
    4: "Cosechar",
}


def _state_path(project_dir: Path) -> Path:
    """Return the path to .kokoro/state.json."""
    return project_dir / KOKORO_DIR / STATE_FILE


def _skill_to_phase(skill: str) -> int:
    """Map a skill name to its phase number."""
    for phase_num, skills in PHASE_SKILLS.items():
        if skill in skills:
            return phase_num
    return 1  # Default to phase 1


def load_state(project_dir: Path) -> CoachingState | None:
    """Load coaching state from .kokoro/state.json.

    Returns None if the file doesn't exist.
    """
    path = _state_path(project_dir)
    if not path.is_file():
        return None
    content = path.read_text(encoding="utf-8")
    return CoachingState.model_validate_json(content)


def save_state(project_dir: Path, state: CoachingState) -> None:
    """Write coaching state to .kokoro/state.json atomically.

    Uses temp file + rename to prevent corruption on crash.
    """
    kokoro_dir = project_dir / KOKORO_DIR
    kokoro_dir.mkdir(parents=True, exist_ok=True)
    target = kokoro_dir / STATE_FILE
    json_str = state.model_dump_json(indent=2)

    # Atomic write: write to temp, then rename
    fd, tmp_path_str = tempfile.mkstemp(
        dir=str(kokoro_dir), suffix=".tmp", prefix="state_"
    )
    tmp_path = Path(tmp_path_str)
    try:
        tmp_path.write_text(json_str, encoding="utf-8")
        tmp_path.replace(target)
    except Exception:
        tmp_path.unlink(missing_ok=True)
        raise
    finally:
        with contextlib.suppress(OSError):
            os.close(fd)


def create_empty_state(negocio: str) -> CoachingState:
    """Create an empty coaching state with 4 phases initialized."""
    now = datetime.now(tz=timezone.utc)
    phases = [
        PhaseProgress(phase=num, name=name)
        for num, name in PHASE_NAMES.items()
    ]
    return CoachingState(
        negocio=negocio,
        phases=phases,
        created=now,
        updated=now,
    )


def mark_skill_complete(
    state: CoachingState,
    skill: str,
    summary: str,
    nodes: list[CoachingNode],
) -> CoachingState:
    """Mark a skill as completed and add its output nodes.

    Updates the appropriate phase progress. If all skills in a phase
    are done, marks the phase as done.
    """
    now = datetime.now(tz=timezone.utc)
    phase_num = _skill_to_phase(skill)
    phase_idx = phase_num - 1

    # Ensure phase exists
    if phase_idx >= len(state.phases):
        return state

    phase = state.phases[phase_idx]
    completion = SkillCompletion(
        skill=skill, completed=now, summary=summary
    )

    # Replace existing or append
    existing_idx: int | None = None
    for i, sc in enumerate(phase.skills_completed):
        if sc.skill == skill:
            existing_idx = i
            break
    if existing_idx is not None:
        phase.skills_completed[existing_idx] = completion
    else:
        phase.skills_completed.append(completion)

    # Update phase status
    phase_skill_names = PHASE_SKILLS.get(phase_num, [])
    completed_names = {sc.skill for sc in phase.skills_completed}
    if all(s in completed_names for s in phase_skill_names):
        phase.status = "done"
    else:
        phase.status = "in_progress"

    # Add nodes
    state.nodes.extend(nodes)
    state.updated = now

    return state


def get_skill_context(
    state: CoachingState, skill: str
) -> list[CoachingNode]:
    """Get relevant nodes for a skill based on methodology dependencies.

    Returns nodes produced by upstream skills that this skill needs as context.
    """
    source_skills = SKILL_CONTEXT.get(skill, [])
    if not source_skills:
        return []
    return [n for n in state.nodes if n.source_skill in source_skills]
