"""Tests for /kokoro-finance skill file content and CLI integration."""

from pathlib import Path

import pytest
from vocabulary_check import find_prohibited_words

from kokoro.cli import init


class TestSkillFileExists:
    """AC1: Skill file exists at the correct path."""

    def test_skill_file_exists(self, commands_path: Path) -> None:
        skill = commands_path / "kokoro-finance.md"
        msg = "kokoro-finance.md must exist in extension/.claude/commands/"
        assert skill.is_file(), msg


class TestFinancialInventoryContent:
    """AC2: Skill guides through financial inventory per product."""

    @pytest.fixture
    def content(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-finance.md").read_text(
            encoding="utf-8",
        )

    def test_mentions_inversion(self, content: str) -> None:
        lower = content.lower()
        assert "inversión" in lower or "inversion" in lower

    def test_mentions_costos(self, content: str) -> None:
        assert "costo" in content.lower()

    def test_mentions_margen(self, content: str) -> None:
        assert "margen" in content.lower()

    def test_mentions_facturacion(self, content: str) -> None:
        lower = content.lower()
        assert "facturación" in lower or "facturacion" in lower


class TestAcquisitionContent:
    """AC3: Skill covers acquisition analysis."""

    @pytest.fixture
    def content(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-finance.md").read_text(
            encoding="utf-8",
        )

    def test_mentions_cpa(self, content: str) -> None:
        assert "cpa" in content.lower()

    def test_mentions_conversion(self, content: str) -> None:
        lower = content.lower()
        assert "conversión" in lower or "conversion" in lower

    def test_mentions_canal(self, content: str) -> None:
        assert "canal" in content.lower()


class TestKeyMetricsContent:
    """AC4: Skill includes key financial metrics."""

    @pytest.fixture
    def content(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-finance.md").read_text(
            encoding="utf-8",
        )

    def test_mentions_roi(self, content: str) -> None:
        assert "roi" in content.lower()

    def test_mentions_ltv(self, content: str) -> None:
        assert "ltv" in content.lower()

    def test_mentions_cliente_definition(self, content: str) -> None:
        """Cliente = alguien que compra 2 veces."""
        lower = content.lower()
        assert "2 veces" in lower or "dos veces" in lower


class TestBudgetContent:
    """AC5: Skill includes budget benchmarks."""

    @pytest.fixture
    def content(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-finance.md").read_text(
            encoding="utf-8",
        )

    def test_mentions_presupuesto(self, content: str) -> None:
        assert "presupuesto" in content.lower()

    def test_mentions_sector_benchmarks(self, content: str) -> None:
        lower = content.lower()
        assert "sector" in lower


class TestValidationPlanContent:
    """AC5b: Skill includes 90-day validation plan."""

    @pytest.fixture
    def content(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-finance.md").read_text(
            encoding="utf-8",
        )

    def test_mentions_90_dias(self, content: str) -> None:
        lower = content.lower()
        assert "90 días" in lower or "90 dias" in lower

    def test_mentions_metricas(self, content: str) -> None:
        lower = content.lower()
        assert "métricas" in lower or "metricas" in lower


class TestEduardoVoice:
    """Skill uses Eduardo's voice patterns."""

    @pytest.fixture
    def content(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-finance.md").read_text(
            encoding="utf-8",
        )

    def test_projector_strategy(self, content: str) -> None:
        """Eduardo's Projector strategy: ask before guiding."""
        lower = content.lower()
        assert "invitación" in lower or "invitacion" in lower or "permiso" in lower

    def test_uses_eduardo_vocabulary(self, content: str) -> None:
        """Eduardo uses inversion, creacion, invitado."""
        lower = content.lower()
        eduardo_terms = ["invitado", "creacion", "inversion"]
        found = sum(1 for t in eduardo_terms if t in lower)
        assert found >= 3, "Skill must use all Eduardo vocabulary"

    def test_no_prohibited_vocabulary(
        self, content: str
    ) -> None:
        violations = find_prohibited_words(content)
        assert violations == [], (
            f"Prohibited words found: {violations}"
        )


class TestCLICopySkill:
    """AC6: kokoro init copies the skill to .claude/commands/."""

    def test_init_copies_finance_skill(self, tmp_path: Path) -> None:
        target = tmp_path / "project"
        target.mkdir()
        init(target=target)
        copied = target / ".claude" / "commands" / "kokoro-finance.md"
        assert copied.is_file(), "kokoro init must copy kokoro-finance.md"

    def test_copied_skill_matches_source(
        self, tmp_path: Path, commands_path: Path,
    ) -> None:
        target = tmp_path / "project"
        target.mkdir()
        init(target=target)
        copied = target / ".claude" / "commands" / "kokoro-finance.md"
        source = commands_path / "kokoro-finance.md"
        assert copied.read_text() == source.read_text()

    def test_overwrites_kokoro_skill_on_rerun(self, tmp_path: Path) -> None:
        target = tmp_path / "project"
        target.mkdir()
        commands_dir = target / ".claude" / "commands"
        commands_dir.mkdir(parents=True)
        (commands_dir / "kokoro-finance.md").write_text("old version")

        init(target=target)

        content = (commands_dir / "kokoro-finance.md").read_text()
        assert content != "old version"
