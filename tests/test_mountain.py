"""Tests for /kokoro-mountain skill file content and CLI integration."""

from pathlib import Path

import pytest

from kokoro.cli import init

EXTENSION_DIR = Path(__file__).resolve().parent.parent / "extension"
SKILL_PATH = EXTENSION_DIR / ".claude" / "commands" / "kokoro-mountain.md"


class TestSkillFileExists:
    """AC1: Skill file exists at the correct path."""

    def test_skill_file_exists(self) -> None:
        msg = "kokoro-mountain.md must exist in extension/.claude/commands/"
        assert SKILL_PATH.is_file(), msg


class TestMontanaContent:
    """AC2: Skill guides through Montana del Manana exercise."""

    @pytest.fixture
    def content(self) -> str:
        return SKILL_PATH.read_text(encoding="utf-8")

    def test_mentions_montana(self, content: str) -> None:
        assert "montaña" in content.lower() or "montana" in content.lower()

    def test_mentions_summit(self, content: str) -> None:
        assert "cima" in content.lower() or "summit" in content.lower()

    def test_mentions_base_camps(self, content: str) -> None:
        lower = content.lower()
        assert "campamento" in lower or "hito" in lower

    def test_mentions_three_year_vision(self, content: str) -> None:
        lower = content.lower()
        has_vision = (
            "3 año" in lower
            or "3 ano" in lower
            or "tres año" in lower
            or "3-year" in lower
            or "3 años" in lower
        )
        assert has_vision


class TestOKRContent:
    """AC3: Skill guides OKR definition."""

    @pytest.fixture
    def content(self) -> str:
        return SKILL_PATH.read_text(encoding="utf-8")

    def test_mentions_okr(self, content: str) -> None:
        assert "OKR" in content or "okr" in content.lower()

    def test_mentions_key_results(self, content: str) -> None:
        lower = content.lower()
        assert "resultado" in lower or "key result" in lower

    def test_mentions_objectives(self, content: str) -> None:
        lower = content.lower()
        assert "objetivo" in lower or "objective" in lower


class TestVisionSummary:
    """AC4: Skill produces structured vision summary."""

    @pytest.fixture
    def content(self) -> str:
        return SKILL_PATH.read_text(encoding="utf-8")

    def test_has_summary_section(self, content: str) -> None:
        lower = content.lower()
        assert "resumen" in lower or "summary" in lower

    def test_has_action_elements(self, content: str) -> None:
        lower = content.lower()
        assert "acción" in lower or "accion" in lower or "plan" in lower


class TestEduardoVoice:
    """Skill uses Eduardo's voice patterns."""

    @pytest.fixture
    def content(self) -> str:
        return SKILL_PATH.read_text(encoding="utf-8")

    def test_projector_strategy(self, content: str) -> None:
        """Eduardo's Projector strategy: ask before guiding."""
        lower = content.lower()
        assert (
            "invitación" in lower
            or "invitacion" in lower
            or "permiso" in lower
        )

    def test_uses_eduardo_vocabulary(self, content: str) -> None:
        """Eduardo never says 'problema', says 'oportunidad' or 'reto'."""
        eduardo_terms = [
            "inversión",
            "inversion",
            "creación",
            "creacion",
            "invitado",
            "montaña",
            "montana",
        ]
        found = any(term in content.lower() for term in eduardo_terms)
        assert found, "Skill should use Eduardo's vocabulary"


class TestCLICopySkill:
    """AC5: kokoro init copies the skill to .claude/commands/."""

    def test_init_copies_mountain_skill(self, tmp_path: Path) -> None:
        target = tmp_path / "project"
        target.mkdir()
        init(target=target)
        copied = target / ".claude" / "commands" / "kokoro-mountain.md"
        assert copied.is_file(), "kokoro init must copy kokoro-mountain.md"

    def test_copied_skill_matches_source(self, tmp_path: Path) -> None:
        target = tmp_path / "project"
        target.mkdir()
        init(target=target)
        copied = target / ".claude" / "commands" / "kokoro-mountain.md"
        assert copied.read_text() == SKILL_PATH.read_text()

    def test_overwrites_kokoro_skill_on_rerun(self, tmp_path: Path) -> None:
        target = tmp_path / "project"
        target.mkdir()
        commands_dir = target / ".claude" / "commands"
        commands_dir.mkdir(parents=True)
        (commands_dir / "kokoro-mountain.md").write_text("old version")
        init(target=target)
        content = (commands_dir / "kokoro-mountain.md").read_text()
        assert content != "old version"
