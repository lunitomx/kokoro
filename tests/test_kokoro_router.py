"""Tests for /kokoro router skill file content and CLI integration."""

from pathlib import Path

import pytest

from kokoro.cli import init

EXTENSION_DIR = Path(__file__).resolve().parent.parent / "extension"
SKILL_PATH = EXTENSION_DIR / ".claude" / "commands" / "kokoro.md"


class TestSkillFileExists:
    """Skill file exists at the correct path."""

    def test_skill_file_exists(self) -> None:
        msg = "kokoro.md must exist in extension/.claude/commands/"
        assert SKILL_PATH.is_file(), msg


class TestDiagnosticQuestionsContent:
    """Router asks diagnostic questions to identify where entrepreneur is."""

    @pytest.fixture
    def content(self) -> str:
        return SKILL_PATH.read_text(encoding="utf-8")

    def test_asks_permission(self, content: str) -> None:
        """Projector strategy: ask permission before guiding."""
        lower = content.lower()
        assert "permiso" in lower or "invitación" in lower or "invitacion" in lower

    def test_asks_questions(self, content: str) -> None:
        """Router includes diagnostic question markers."""
        assert "?" in content


class TestSkillAwareness:
    """Router is aware of all 4 Phase 1 skills."""

    @pytest.fixture
    def content(self) -> str:
        return SKILL_PATH.read_text(encoding="utf-8")

    def test_mentions_diagnose(self, content: str) -> None:
        assert "/kokoro-diagnose" in content

    def test_mentions_mountain(self, content: str) -> None:
        assert "/kokoro-mountain" in content

    def test_mentions_prune(self, content: str) -> None:
        assert "/kokoro-prune" in content

    def test_mentions_finance(self, content: str) -> None:
        assert "/kokoro-finance" in content


class TestMethodologyOrder:
    """Router references methodology phases in correct order."""

    @pytest.fixture
    def content(self) -> str:
        return SKILL_PATH.read_text(encoding="utf-8")

    def test_mentions_diagnostico(self, content: str) -> None:
        lower = content.lower()
        assert "diagnóstico" in lower or "diagnostico" in lower

    def test_mentions_vision(self, content: str) -> None:
        lower = content.lower()
        assert "visión" in lower or "vision" in lower

    def test_mentions_poda(self, content: str) -> None:
        assert "poda" in content.lower()

    def test_mentions_finanzas(self, content: str) -> None:
        lower = content.lower()
        assert "finanzas" in lower or "financier" in lower


class TestRouterRecommendation:
    """Router explains why it recommends a specific skill."""

    @pytest.fixture
    def content(self) -> str:
        return SKILL_PATH.read_text(encoding="utf-8")

    def test_explains_why(self, content: str) -> None:
        lower = content.lower()
        assert "porque" in lower or "por qué" in lower or "razón" in lower or "razon" in lower


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
    """kokoro init copies the router skill to .claude/commands/."""

    def test_init_copies_router_skill(self, tmp_path: Path) -> None:
        target = tmp_path / "project"
        target.mkdir()
        init(target=target)
        copied = target / ".claude" / "commands" / "kokoro.md"
        assert copied.is_file(), "kokoro init must copy kokoro.md"

    def test_copied_skill_matches_source(self, tmp_path: Path) -> None:
        target = tmp_path / "project"
        target.mkdir()
        init(target=target)
        copied = target / ".claude" / "commands" / "kokoro.md"
        source = SKILL_PATH
        assert copied.read_text() == source.read_text()

    def test_overwrites_kokoro_skill_on_rerun(self, tmp_path: Path) -> None:
        target = tmp_path / "project"
        target.mkdir()
        commands_dir = target / ".claude" / "commands"
        commands_dir.mkdir(parents=True)
        (commands_dir / "kokoro.md").write_text("old version")

        init(target=target)

        content = (commands_dir / "kokoro.md").read_text()
        assert content != "old version"
