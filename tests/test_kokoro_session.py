"""Tests for /kokoro-session skill file content and CLI integration."""

from pathlib import Path

import pytest

from kokoro.cli import init

EXTENSION_DIR = Path(__file__).resolve().parent.parent / "extension"
SKILL_PATH = EXTENSION_DIR / ".claude" / "commands" / "kokoro-session.md"


class TestSkillFileExists:
    """Skill file exists at the correct path."""

    def test_skill_file_exists(self) -> None:
        msg = "kokoro-session.md must exist in extension/.claude/commands/"
        assert SKILL_PATH.is_file(), msg


class TestSessionStartContent:
    """Session start mode initializes the Phase 1 journey."""

    @pytest.fixture
    def content(self) -> str:
        return SKILL_PATH.read_text(encoding="utf-8")

    def test_mentions_roadmap(self, content: str) -> None:
        lower = content.lower()
        assert "roadmap" in lower or "hoja de ruta" in lower or "mapa" in lower

    def test_mentions_four_phases(self, content: str) -> None:
        lower = content.lower()
        has_phases = (
            "4 fases" in lower
            or "cuatro fases" in lower
            or "4 estaciones" in lower
            or "cuatro estaciones" in lower
        )
        assert has_phases

    def test_guides_to_diagnose(self, content: str) -> None:
        assert "/kokoro-diagnose" in content


class TestSessionContinueContent:
    """Session continue mode reviews completed skills and identifies next."""

    @pytest.fixture
    def content(self) -> str:
        return SKILL_PATH.read_text(encoding="utf-8")

    def test_mentions_completed(self, content: str) -> None:
        assert "completado" in content.lower()

    def test_mentions_next_step(self, content: str) -> None:
        assert "siguiente" in content.lower()


class TestSessionReviewContent:
    """Session review mode provides structured progress report."""

    @pytest.fixture
    def content(self) -> str:
        return SKILL_PATH.read_text(encoding="utf-8")

    def test_mentions_progreso(self, content: str) -> None:
        assert "progreso" in content.lower()

    def test_mentions_resumen(self, content: str) -> None:
        assert "resumen" in content.lower()

    def test_structured_report(self, content: str) -> None:
        lower = content.lower()
        assert "reporte" in lower or "informe" in lower


class TestEduardoVoice:
    """Skill uses Eduardo's voice patterns."""

    @pytest.fixture
    def content(self) -> str:
        return SKILL_PATH.read_text(encoding="utf-8")

    def test_projector_strategy(self, content: str) -> None:
        """Eduardo's Projector strategy: ask before guiding."""
        lower = content.lower()
        assert "invitación" in lower or "invitacion" in lower or "permiso" in lower

    def test_uses_eduardo_vocabulary(self, content: str) -> None:
        """Eduardo uses inversion, creacion, invitado."""
        eduardo_terms = [
            "inversión", "inversion", "creación", "creacion",
            "invitado",
        ]
        found = any(term in content.lower() for term in eduardo_terms)
        assert found, "Skill should use Eduardo's vocabulary"


class TestCLICopySkill:
    """kokoro init copies the session skill to .claude/commands/."""

    def test_init_copies_session_skill(self, tmp_path: Path) -> None:
        target = tmp_path / "project"
        target.mkdir()
        init(target=target)
        copied = target / ".claude" / "commands" / "kokoro-session.md"
        assert copied.is_file(), "kokoro init must copy kokoro-session.md"

    def test_copied_skill_matches_source(self, tmp_path: Path) -> None:
        target = tmp_path / "project"
        target.mkdir()
        init(target=target)
        copied = target / ".claude" / "commands" / "kokoro-session.md"
        source = SKILL_PATH
        assert copied.read_text() == source.read_text()

    def test_overwrites_kokoro_skill_on_rerun(self, tmp_path: Path) -> None:
        target = tmp_path / "project"
        target.mkdir()
        commands_dir = target / ".claude" / "commands"
        commands_dir.mkdir(parents=True)
        (commands_dir / "kokoro-session.md").write_text("old version")

        init(target=target)

        content = (commands_dir / "kokoro-session.md").read_text()
        assert content != "old version"
