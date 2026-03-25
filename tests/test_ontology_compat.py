"""Backward compatibility tests for ontology layer (S3.6).

Verifies that all existing functionality works correctly when
.kokoro/state.json does NOT exist (graceful degradation).
"""

from __future__ import annotations

from pathlib import Path

from kokoro.cli import init
from kokoro.ontology.store import (
    create_empty_state,
    get_skill_context,
    load_state,
    mark_skill_complete,
    save_state,
)


class TestInitCreatesKokoroDir:
    """kokoro init should create .kokoro/ directory."""

    def test_init_creates_kokoro_dir(self, tmp_path: Path) -> None:
        init(target=tmp_path)
        assert (tmp_path / ".kokoro").is_dir()

    def test_init_idempotent(self, tmp_path: Path) -> None:
        """Running init twice should not fail or lose state."""
        init(target=tmp_path)
        # Create state in .kokoro/
        state = create_empty_state("Test")
        save_state(tmp_path, state)
        # Run init again
        init(target=tmp_path)
        # State should survive
        loaded = load_state(tmp_path)
        assert loaded is not None
        assert loaded.negocio == "Test"


class TestGracefulDegradation:
    """All store operations degrade gracefully without state.json."""

    def test_load_state_returns_none(self, tmp_path: Path) -> None:
        """No state file → None, not an error."""
        assert load_state(tmp_path) is None

    def test_get_skill_context_empty_state(self) -> None:
        """Empty state → empty context, not an error."""
        state = create_empty_state("Empty")
        context = get_skill_context(state, "kokoro-forces")
        assert context == []

    def test_mark_skill_on_empty_state(self) -> None:
        """Marking a skill on empty state works."""
        state = create_empty_state("Test")
        updated = mark_skill_complete(
            state, "kokoro-diagnose", "Done", []
        )
        assert updated.phases[0].status == "in_progress"

    def test_save_and_load_empty_state(self, tmp_path: Path) -> None:
        """Empty state round-trips correctly."""
        state = create_empty_state("Round Trip")
        save_state(tmp_path, state)
        loaded = load_state(tmp_path)
        assert loaded is not None
        assert loaded.negocio == "Round Trip"
        assert len(loaded.phases) == 4
        assert loaded.nodes == []


class TestSkillFilesHavePersistencia:
    """All coaching skills must have a Persistencia section."""

    COACHING_SKILLS: list[str] = [
        "kokoro-diagnose",
        "kokoro-mountain",
        "kokoro-prune",
        "kokoro-finance",
        "kokoro-canvas",
        "kokoro-forces",
        "kokoro-interviews",
        "kokoro-validate",
        "kokoro-research",
        "kokoro-pescar",
        "kokoro-experiment",
        "kokoro-launch",
    ]

    def test_all_skills_have_persistencia(
        self, commands_path: Path
    ) -> None:
        for skill_name in self.COACHING_SKILLS:
            content = (commands_path / f"{skill_name}.md").read_text(
                encoding="utf-8"
            )
            assert "## Persistencia" in content, (
                f"{skill_name} missing '## Persistencia' section"
            )

    def test_all_skills_have_context_loading(
        self, commands_path: Path
    ) -> None:
        for skill_name in self.COACHING_SKILLS:
            content = (commands_path / f"{skill_name}.md").read_text(
                encoding="utf-8"
            )
            assert "state.json" in content, (
                f"{skill_name} missing state.json context loading"
            )


class TestMetaSkillsStateAware:
    """Meta-skills (session, router) reference state.json."""

    def test_session_references_state(self, commands_path: Path) -> None:
        content = (commands_path / "kokoro-session.md").read_text(
            encoding="utf-8"
        )
        assert "state.json" in content

    def test_router_references_state(self, commands_path: Path) -> None:
        content = (commands_path / "kokoro.md").read_text(
            encoding="utf-8"
        )
        assert "state.json" in content
