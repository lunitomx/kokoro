"""Tests for /kokoro-prune skill file content and CLI integration."""

from pathlib import Path

import pytest

from kokoro.cli import init

EXTENSION_DIR = Path(__file__).resolve().parent.parent / "extension"
SKILL_PATH = EXTENSION_DIR / ".claude" / "commands" / "kokoro-prune.md"


class TestSkillFileExists:
    """AC1: Skill file exists at the correct path."""

    def test_skill_file_exists(self) -> None:
        msg = "kokoro-prune.md must exist in extension/.claude/commands/"
        assert SKILL_PATH.is_file(), msg


class TestProductTreeContent:
    """AC2: Skill guides through Product Tree exercise."""

    @pytest.fixture
    def content(self) -> str:
        return SKILL_PATH.read_text(encoding="utf-8")

    def test_mentions_arbol(self, content: str) -> None:
        lower = content.lower()
        assert "árbol" in lower or "arbol" in lower

    def test_mentions_rama(self, content: str) -> None:
        assert "rama" in content.lower()

    def test_mentions_frutos(self, content: str) -> None:
        assert "fruto" in content.lower()


class TestEvaluationMatrixContent:
    """AC3: Skill includes 4-criteria evaluation matrix."""

    @pytest.fixture
    def content(self) -> str:
        return SKILL_PATH.read_text(encoding="utf-8")

    def test_mentions_ingresos(self, content: str) -> None:
        assert "ingresos" in content.lower()

    def test_mentions_rentabilidad(self, content: str) -> None:
        assert "rentabilidad" in content.lower()

    def test_mentions_coherencia(self, content: str) -> None:
        assert "coherencia" in content.lower()

    def test_mentions_energia(self, content: str) -> None:
        lower = content.lower()
        assert "energía" in lower or "energia" in lower


class TestClassificationContent:
    """AC4: Skill classifies branches into 4 categories."""

    @pytest.fixture
    def content(self) -> str:
        return SKILL_PATH.read_text(encoding="utf-8")

    def test_mentions_crecer(self, content: str) -> None:
        assert "crecer" in content.lower()

    def test_mentions_mantener(self, content: str) -> None:
        assert "mantener" in content.lower()

    def test_mentions_transformar(self, content: str) -> None:
        assert "transformar" in content.lower()

    def test_mentions_podar(self, content: str) -> None:
        assert "podar" in content.lower()


class TestPruningSummary:
    """AC5: Skill produces structured pruning summary."""

    @pytest.fixture
    def content(self) -> str:
        return SKILL_PATH.read_text(encoding="utf-8")

    def test_has_summary_section(self, content: str) -> None:
        assert "resumen" in content.lower()

    def test_has_decision_markers(self, content: str) -> None:
        lower = content.lower()
        assert "decisión" in lower or "decision" in lower or "fecha" in lower


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
        """Eduardo never says 'problema', says 'oportunidad' or 'reto'."""
        eduardo_terms = [
            "inversión", "inversion", "creación", "creacion",
            "invitado", "montaña", "montana",
        ]
        found = any(term in content.lower() for term in eduardo_terms)
        assert found, "Skill should use Eduardo's vocabulary"


class TestCLICopySkill:
    """AC6: kokoro init copies the skill to .claude/commands/."""

    def test_init_copies_prune_skill(self, tmp_path: Path) -> None:
        target = tmp_path / "project"
        target.mkdir()
        init(target=target)
        copied = target / ".claude" / "commands" / "kokoro-prune.md"
        assert copied.is_file(), "kokoro init must copy kokoro-prune.md"

    def test_copied_skill_matches_source(self, tmp_path: Path) -> None:
        target = tmp_path / "project"
        target.mkdir()
        init(target=target)
        copied = target / ".claude" / "commands" / "kokoro-prune.md"
        source = SKILL_PATH
        assert copied.read_text() == source.read_text()

    def test_overwrites_kokoro_skill_on_rerun(self, tmp_path: Path) -> None:
        target = tmp_path / "project"
        target.mkdir()
        commands_dir = target / ".claude" / "commands"
        commands_dir.mkdir(parents=True)
        (commands_dir / "kokoro-prune.md").write_text("old version")

        init(target=target)

        content = (commands_dir / "kokoro-prune.md").read_text()
        assert content != "old version"
