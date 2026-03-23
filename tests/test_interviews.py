"""Tests for /kokoro-interviews skill file content and CLI integration."""

from pathlib import Path

import pytest

from kokoro.cli import init

EXTENSION_DIR = Path(__file__).resolve().parent.parent / "extension"
SKILL_PATH = (
    EXTENSION_DIR / ".claude" / "commands" / "kokoro-interviews.md"
)


class TestInterviewsSkillExists:
    """AC1: Skill file exists at correct path."""

    def test_skill_file_exists(self) -> None:
        msg = (
            "kokoro-interviews.md must exist in"
            " extension/.claude/commands/"
        )
        assert SKILL_PATH.is_file(), msg


class TestInterviewsStructure:
    """AC2: Contains Problem and Solution Interview sections."""

    @pytest.fixture
    def content(self) -> str:
        return SKILL_PATH.read_text(encoding="utf-8")

    def test_has_problem_interview_section(
        self, content: str
    ) -> None:
        lower = content.lower()
        assert "entrevista de problema" in lower, (
            "Must have Entrevista de Problema section"
        )

    def test_has_solution_interview_section(
        self, content: str
    ) -> None:
        lower = content.lower()
        assert "entrevista de solucion" in lower, (
            "Must have Entrevista de Solucion section"
        )

    def test_problem_before_solution(
        self, content: str
    ) -> None:
        """Problem Interview must appear before Solution Interview."""
        lower = content.lower()
        problem_idx = lower.index("entrevista de problema")
        solution_idx = lower.index("entrevista de solucion")
        assert problem_idx < solution_idx, (
            "Problem Interview must come before Solution Interview"
        )

    def test_has_coaching_methodology(
        self, content: str
    ) -> None:
        lower = content.lower()
        assert "coach" in lower, (
            "Must have coaching methodology section"
        )


class TestInterviewsContent:
    """AC4: Eduardo's voice present."""

    @pytest.fixture
    def content(self) -> str:
        return SKILL_PATH.read_text(encoding="utf-8")

    def test_has_eduardo_voice(self, content: str) -> None:
        lower = content.lower()
        eduardo_terms = ["invitado", "creacion", "inversion"]
        found = sum(
            1 for t in eduardo_terms if t in lower
        )
        assert found >= 3, (
            "Skill must use all Eduardo vocabulary"
        )

    def test_references_knowledge_file(
        self, content: str
    ) -> None:
        assert "kokoro-phase2-interviews.md" in content

    def test_has_anti_pattern_warnings(
        self, content: str
    ) -> None:
        lower = content.lower()
        has_nunca = "nunca" in lower
        has_no_vender = "no vender" in lower
        has_no_vendas = "no vendas" in lower
        assert has_nunca or has_no_vender or has_no_vendas, (
            "Must have anti-pattern warnings"
        )

    def test_has_proyector_strategy(
        self, content: str
    ) -> None:
        lower = content.lower()
        assert "permiso" in lower or "invitacion" in lower


class TestInterviewsSections:
    """AC5: Interview sections have guiding questions and key content."""

    @pytest.fixture
    def content(self) -> str:
        return SKILL_PATH.read_text(encoding="utf-8")

    def test_problem_interview_has_guiding_questions(
        self, content: str
    ) -> None:
        """Problem Interview section must have >= 2 question marks."""
        lower = content.lower()
        start = lower.index("entrevista de problema")
        next_heading = content.find("\n## ", start + 1)
        section = (
            content[start:next_heading]
            if next_heading != -1
            else content[start:]
        )
        q_count = section.count("?")
        assert q_count >= 2, (
            f"Problem Interview has {q_count} questions,"
            f" need >= 2"
        )

    def test_solution_interview_has_guiding_questions(
        self, content: str
    ) -> None:
        """Solution Interview section must have >= 2 question marks."""
        lower = content.lower()
        start = lower.index("entrevista de solucion")
        next_heading = content.find("\n## ", start + 1)
        section = (
            content[start:next_heading]
            if next_heading != -1
            else content[start:]
        )
        q_count = section.count("?")
        assert q_count >= 2, (
            f"Solution Interview has {q_count} questions,"
            f" need >= 2"
        )

    def test_has_bias_awareness(self, content: str) -> None:
        lower = content.lower()
        biases = [
            "confirmacion",
            "deseabilidad social",
            "recencia",
            "disponibilidad",
        ]
        for bias in biases:
            assert bias in lower, (
                f"Missing bias: {bias}"
            )

    def test_has_quality_metrics(
        self, content: str
    ) -> None:
        lower = content.lower()
        assert "calidad" in lower, (
            "Must have quality metrics section"
        )

    def test_has_coaching_not_consultant(
        self, content: str
    ) -> None:
        lower = content.lower()
        assert "coach" in lower, "Must mention coach"
        assert "consultor" in lower, (
            "Must mention consultor for contrast"
        )


class TestInterviewsSummary:
    """AC6: Summary template covers interview preparation."""

    @pytest.fixture
    def content(self) -> str:
        return SKILL_PATH.read_text(encoding="utf-8")

    def test_has_summary_template(self, content: str) -> None:
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


class TestInterviewsCLI:
    """AC7: kokoro init copies the file correctly."""

    def test_init_copies_interviews_skill(
        self, tmp_path: Path
    ) -> None:
        target = tmp_path / "project"
        target.mkdir()
        init(target=target)
        copied = (
            target
            / ".claude"
            / "commands"
            / "kokoro-interviews.md"
        )
        assert copied.is_file(), (
            "kokoro init must copy kokoro-interviews.md"
        )

    def test_copied_skill_matches_source(
        self, tmp_path: Path
    ) -> None:
        target = tmp_path / "project"
        target.mkdir()
        init(target=target)
        copied = (
            target
            / ".claude"
            / "commands"
            / "kokoro-interviews.md"
        )
        assert copied.read_text() == SKILL_PATH.read_text()
