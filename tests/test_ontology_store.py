"""Tests for kokoro ontology persistence layer (S3.2)."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from kokoro.ontology.models import (
    CoachingEdge,
    CoachingNode,
    EdgeType,
    NodeType,
)
from kokoro.ontology.store import (
    create_empty_state,
    get_skill_context,
    load_state,
    mark_skill_complete,
    save_state,
)

NOW = datetime(2026, 3, 24, tzinfo=timezone.utc)


class TestLoadState:
    """load_state returns None when no file, CoachingState when exists."""

    def test_returns_none_when_no_file(self, tmp_path: Path) -> None:
        result = load_state(tmp_path)
        assert result is None

    def test_returns_state_when_file_exists(self, tmp_path: Path) -> None:
        state = create_empty_state("Test Negocio")
        save_state(tmp_path, state)
        loaded = load_state(tmp_path)
        assert loaded is not None
        assert loaded.negocio == "Test Negocio"


class TestSaveState:
    """save_state writes .kokoro/state.json atomically."""

    def test_creates_kokoro_directory(self, tmp_path: Path) -> None:
        state = create_empty_state("Mi Negocio")
        save_state(tmp_path, state)
        assert (tmp_path / ".kokoro").is_dir()
        assert (tmp_path / ".kokoro" / "state.json").is_file()

    def test_round_trip_preserves_data(self, tmp_path: Path) -> None:
        state = create_empty_state("Mi Negocio")
        node = CoachingNode(
            id="SEG-001",
            type=NodeType.SEGMENTO,
            content="Artesanos digitales",
            source_skill="kokoro-canvas",
            created=NOW,
        )
        state.nodes.append(node)
        state.edges.append(
            CoachingEdge(
                source="SEG-001",
                target="PRO-001",
                type=EdgeType.ALIMENTA,
            )
        )
        save_state(tmp_path, state)
        loaded = load_state(tmp_path)
        assert loaded is not None
        assert len(loaded.nodes) == 1
        assert loaded.nodes[0].id == "SEG-001"
        assert len(loaded.edges) == 1

    def test_overwrites_existing_state(self, tmp_path: Path) -> None:
        state1 = create_empty_state("Version 1")
        save_state(tmp_path, state1)
        state2 = create_empty_state("Version 2")
        save_state(tmp_path, state2)
        loaded = load_state(tmp_path)
        assert loaded is not None
        assert loaded.negocio == "Version 2"

    def test_no_temp_file_left_behind(self, tmp_path: Path) -> None:
        state = create_empty_state("Clean")
        save_state(tmp_path, state)
        kokoro_dir = tmp_path / ".kokoro"
        files = list(kokoro_dir.iterdir())
        assert len(files) == 1
        assert files[0].name == "state.json"


class TestCreateEmptyState:
    """create_empty_state produces a valid starting state."""

    def test_has_version_1(self) -> None:
        state = create_empty_state("Test")
        assert state.version == 1

    def test_has_negocio(self) -> None:
        state = create_empty_state("Mi Tienda")
        assert state.negocio == "Mi Tienda"

    def test_has_four_phases(self) -> None:
        state = create_empty_state("Test")
        assert len(state.phases) == 4
        assert state.phases[0].name == "Preparar el Suelo"
        assert state.phases[1].name == "Elegir la Semilla"
        assert state.phases[2].name == "Germinar"
        assert state.phases[3].name == "Cosechar"

    def test_all_phases_pending(self) -> None:
        state = create_empty_state("Test")
        for phase in state.phases:
            assert phase.status == "pending"

    def test_empty_nodes_and_edges(self) -> None:
        state = create_empty_state("Test")
        assert state.nodes == []
        assert state.edges == []


class TestMarkSkillComplete:
    """mark_skill_complete updates phase progress and adds nodes."""

    def test_marks_skill_and_updates_phase(self) -> None:
        state = create_empty_state("Test")
        nodes = [
            CoachingNode(
                id="VIS-001",
                type=NodeType.VISION,
                content="Cima en 3 años",
                source_skill="kokoro-mountain",
                created=NOW,
            ),
        ]
        updated = mark_skill_complete(
            state, "kokoro-mountain", "Montaña definida", nodes
        )
        # Phase 1 should be in_progress
        assert updated.phases[0].status == "in_progress"
        # Skill should be recorded
        completions = updated.phases[0].skills_completed
        assert len(completions) == 1
        assert completions[0].skill == "kokoro-mountain"
        # Nodes added
        assert len(updated.nodes) == 1

    def test_phase_done_when_all_skills_complete(self) -> None:
        state = create_empty_state("Test")
        phase1_skills = [
            "kokoro-diagnose",
            "kokoro-mountain",
            "kokoro-prune",
            "kokoro-finance",
        ]
        for skill in phase1_skills:
            state = mark_skill_complete(state, skill, f"{skill} done", [])
        assert state.phases[0].status == "done"

    def test_phase2_skill_updates_phase2(self) -> None:
        state = create_empty_state("Test")
        state = mark_skill_complete(
            state, "kokoro-canvas", "Canvas listo", []
        )
        assert state.phases[1].status == "in_progress"

    def test_does_not_duplicate_skill(self) -> None:
        state = create_empty_state("Test")
        state = mark_skill_complete(state, "kokoro-diagnose", "v1", [])
        state = mark_skill_complete(state, "kokoro-diagnose", "v2", [])
        completions = state.phases[0].skills_completed
        assert len(completions) == 1
        assert completions[0].summary == "v2"


class TestGetSkillContext:
    """get_skill_context returns relevant nodes for a skill."""

    def test_forces_gets_canvas_nodes(self) -> None:
        state = create_empty_state("Test")
        canvas_node = CoachingNode(
            id="SEG-001",
            type=NodeType.SEGMENTO,
            content="Emprendedores digitales",
            source_skill="kokoro-canvas",
            created=NOW,
        )
        state.nodes.append(canvas_node)
        context = get_skill_context(state, "kokoro-forces")
        assert len(context) >= 1
        assert any(n.source_skill == "kokoro-canvas" for n in context)

    def test_interviews_gets_forces_and_canvas_nodes(self) -> None:
        state = create_empty_state("Test")
        state.nodes.extend([
            CoachingNode(
                id="SEG-001",
                type=NodeType.SEGMENTO,
                content="Segment",
                source_skill="kokoro-canvas",
                created=NOW,
            ),
            CoachingNode(
                id="FUE-001",
                type=NodeType.FUERZA,
                content="Trigger event",
                source_skill="kokoro-forces",
                created=NOW,
            ),
        ])
        context = get_skill_context(state, "kokoro-interviews")
        assert len(context) == 2

    def test_returns_empty_when_no_relevant_nodes(self) -> None:
        state = create_empty_state("Test")
        context = get_skill_context(state, "kokoro-diagnose")
        assert context == []

    def test_validate_gets_all_phase2_nodes(self) -> None:
        state = create_empty_state("Test")
        state.nodes.extend([
            CoachingNode(
                id="SEG-001",
                type=NodeType.SEGMENTO,
                content="Segment",
                source_skill="kokoro-canvas",
                created=NOW,
            ),
            CoachingNode(
                id="FUE-001",
                type=NodeType.FUERZA,
                content="Force",
                source_skill="kokoro-forces",
                created=NOW,
            ),
            CoachingNode(
                id="HIP-001",
                type=NodeType.HIPOTESIS,
                content="Hypothesis",
                source_skill="kokoro-interviews",
                created=NOW,
            ),
        ])
        context = get_skill_context(state, "kokoro-validate")
        assert len(context) == 3
