"""Tests for /kokoro-validate skill file content and CLI."""

from pathlib import Path

import pytest
from vocabulary_check import find_prohibited_words

from kokoro.cli import init


class TestValidateSkillExists:
    """AC1: Skill file exists at correct path."""

    def test_skill_file_exists(
        self, commands_path: Path,
    ) -> None:
        skill = commands_path / "kokoro-validate.md"
        msg = (
            "kokoro-validate.md must exist in"
            " extension/.claude/commands/"
        )
        assert skill.is_file(), msg


class TestValidateStructure:
    """AC2: Contains 3x3x3, risks, experiments, canvas."""

    @pytest.fixture
    def content(self, commands_path: Path) -> str:
        return (
            commands_path / "kokoro-validate.md"
        ).read_text(encoding="utf-8")

    def test_has_3x3x3_model(self, content: str) -> None:
        lower = content.lower()
        has_label = "3x3x3" in lower
        has_parts = (
            "3 anos" in lower
            and "3 meses" in lower
            and "3 semanas" in lower
        )
        assert has_label or has_parts, (
            "Must have 3x3x3 planning model"
        )

    def test_has_risk_categories(
        self, content: str
    ) -> None:
        lower = content.lower()
        assert "riesgo de producto" in lower, (
            "Missing: riesgo de producto"
        )
        has_consumer = (
            "riesgo de consumidor" in lower
            or "riesgo de invitado" in lower
        )
        assert has_consumer, (
            "Missing: riesgo de consumidor/invitado"
        )
        assert "riesgo de mercado" in lower, (
            "Missing: riesgo de mercado"
        )

    def test_has_experiment_design(
        self, content: str
    ) -> None:
        lower = content.lower()
        assert "hipotesis" in lower, "Missing: hipotesis"
        assert "experimento" in lower, (
            "Missing: experimento"
        )

    def test_has_validation_plan_canvas(
        self, content: str
    ) -> None:
        lower = content.lower()
        has_en = "validation plan" in lower
        has_es = "plan de validacion" in lower
        assert has_en or has_es, (
            "Must have Validation Plan Canvas"
        )


class TestValidateContent:
    """AC4: Eduardo's voice present."""

    @pytest.fixture
    def content(self, commands_path: Path) -> str:
        return (
            commands_path / "kokoro-validate.md"
        ).read_text(encoding="utf-8")

    def test_has_eduardo_voice(self, content: str) -> None:
        lower = content.lower()
        eduardo_terms = [
            "invitado",
            "creacion",
            "inversion",
        ]
        found = sum(
            1 for t in eduardo_terms if t in lower
        )
        assert found >= 3, (
            "Skill must use all Eduardo vocabulary"
        )

    def test_references_knowledge_file(
        self, content: str
    ) -> None:
        assert "kokoro-phase2-validation.md" in content

    def test_has_anti_pattern_warnings(
        self, content: str
    ) -> None:
        lower = content.lower()
        has_solution_love = (
            "enamorarse de la solucion" in lower
        )
        has_excel = (
            "proyecciones en excel" in lower
            or "excel" in lower
        )
        has_intentions = (
            "medir intenciones" in lower
            or "intenciones" in lower
        )
        assert (
            has_solution_love or has_excel or has_intentions
        ), "Must have anti-pattern warnings"

    def test_has_proyector_strategy(
        self, content: str
    ) -> None:
        lower = content.lower()
        assert (
            "permiso" in lower or "invitacion" in lower
        )

    def test_no_prohibited_vocabulary(
        self, content: str
    ) -> None:
        violations = find_prohibited_words(content)
        assert violations == [], (
            f"Prohibited words found: {violations}"
        )


class TestValidateSections:
    """AC5: Key sections present with guiding questions."""

    @pytest.fixture
    def content(self, commands_path: Path) -> str:
        return (
            commands_path / "kokoro-validate.md"
        ).read_text(encoding="utf-8")

    def test_has_traction_concept(
        self, content: str
    ) -> None:
        lower = content.lower()
        assert "traccion" in lower, (
            "Must have traction concept"
        )

    def test_has_mindset_principles(
        self, content: str
    ) -> None:
        lower = content.lower()
        assert (
            "principio" in lower or "mindset" in lower
        ), "Must have mindset principles"

    def test_experiment_section_has_guiding_questions(
        self, content: str
    ) -> None:
        """Experiment section must have >= 2 '?'."""
        lower = content.lower()
        marker = "## diseno de experimento"
        start = lower.index(marker)
        next_heading = content.find(
            "\n## ", start + len(marker)
        )
        section = (
            content[start:next_heading]
            if next_heading != -1
            else content[start:]
        )
        q_count = section.count("?")
        assert q_count >= 2, (
            f"Experiment section has {q_count}"
            f" questions, need >= 2"
        )


class TestValidateSummary:
    """AC6: Summary template covers validation plan."""

    @pytest.fixture
    def content(self, commands_path: Path) -> str:
        return (
            commands_path / "kokoro-validate.md"
        ).read_text(encoding="utf-8")

    def test_has_summary_template(
        self, content: str
    ) -> None:
        lower = content.lower()
        assert "resumen" in lower
        resumen_idx = lower.index("resumen")
        after_resumen = content[resumen_idx:]
        table_lines = [
            ln
            for ln in after_resumen.splitlines()
            if "|" in ln
        ]
        assert len(table_lines) >= 4, (
            "Summary table must have at least 4 rows"
        )


class TestValidateCLI:
    """AC7: kokoro init copies the file correctly."""

    def test_init_copies_validate_skill(
        self, tmp_path: Path
    ) -> None:
        target = tmp_path / "project"
        target.mkdir()
        init(target=target)
        copied = (
            target
            / ".claude"
            / "commands"
            / "kokoro-validate.md"
        )
        assert copied.is_file(), (
            "kokoro init must copy kokoro-validate.md"
        )

    def test_copied_skill_matches_source(
        self, tmp_path: Path, commands_path: Path,
    ) -> None:
        target = tmp_path / "project"
        target.mkdir()
        init(target=target)
        copied = (
            target
            / ".claude"
            / "commands"
            / "kokoro-validate.md"
        )
        source = commands_path / "kokoro-validate.md"
        assert copied.read_text() == source.read_text()
