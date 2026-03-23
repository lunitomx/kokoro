"""Tests for /kokoro-canvas skill file content and CLI integration."""

from pathlib import Path

import pytest

from kokoro.cli import init


class TestCanvasSkillExists:
    """AC1: Skill file exists at correct path."""

    def test_skill_file_exists(self, commands_path: Path) -> None:
        skill = commands_path / "kokoro-canvas.md"
        msg = "kokoro-canvas.md must exist in extension/.claude/commands/"
        assert skill.is_file(), msg


class TestCanvasStructure:
    """AC2: Contains all 9 Lean Canvas blocks."""

    @pytest.fixture
    def content(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-canvas.md").read_text(
            encoding="utf-8",
        )

    def test_has_nine_blocks(self, content: str) -> None:
        blocks = [
            "Segmento de Invitados",
            "Problema",
            "Propuesta Unica de Valor",
            "Ventaja Injusta",
            "Canales",
            "Flujo de Ingresos",
            "Estructura de Costos",
            "Metricas Clave",
            "Solucion",
        ]
        lower = content.lower()
        for block in blocks:
            assert block.lower() in lower, f"Missing block: {block}"

    def test_segment_is_first_block(self, content: str) -> None:
        """Segmento must be Bloque 1."""
        assert "## Bloque 1" in content
        idx1 = content.index("## Bloque 1")
        assert "segmento" in content[idx1:idx1 + 80].lower()

    def test_solution_is_last_block(self, content: str) -> None:
        """Solucion must be Bloque 9 (LAST)."""
        assert "## Bloque 9" in content
        idx9 = content.index("## Bloque 9")
        assert "solucion" in content[idx9:idx9 + 80].lower()

    def test_fill_order_enforced(self, content: str) -> None:
        """Blocks appear in Eduardo's prescribed segment-first order."""
        order = [
            "## Bloque 1", "## Bloque 2", "## Bloque 3",
            "## Bloque 4", "## Bloque 5", "## Bloque 6",
            "## Bloque 7", "## Bloque 8", "## Bloque 9",
        ]
        for heading in order:
            assert heading in content, f"Missing: {heading}"
        positions = [content.index(h) for h in order]
        assert positions == sorted(positions), "Blocks must be in order 1-9"


class TestCanvasContent:
    """AC4: Eduardo's voice present."""

    @pytest.fixture
    def content(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-canvas.md").read_text(
            encoding="utf-8",
        )

    def test_has_eduardo_voice(self, content: str) -> None:
        lower = content.lower()
        eduardo_terms = ["invitado", "creacion", "inversion"]
        found = sum(1 for t in eduardo_terms if t in lower)
        assert found >= 2, "Skill must use Eduardo's vocabulary"

    def test_references_knowledge_file(self, content: str) -> None:
        assert "kokoro-phase2-canvas.md" in content

    def test_has_anti_pattern_warnings(self, content: str) -> None:
        lower = content.lower()
        has_ballenas = "inciensos de ballenas" in lower
        has_nunca = "nunca iniciar por la solucion" in lower
        has_nunca2 = "nunca empezar por la solucion" in lower
        assert has_ballenas or has_nunca or has_nunca2

    def test_has_proyector_strategy(self, content: str) -> None:
        lower = content.lower()
        assert "permiso" in lower or "invitacion" in lower


class TestCanvasBlocks:
    """AC2b: Each block has guiding questions."""

    @pytest.fixture
    def content(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-canvas.md").read_text(
            encoding="utf-8",
        )

    def test_each_block_has_guiding_questions(self, content: str) -> None:
        """Each of 9 blocks must have at least 2 question marks."""
        for i in range(1, 10):
            heading = f"## Bloque {i}"
            assert heading in content, f"Missing {heading}"
            start = content.index(heading)
            # Find next ## heading or end of file
            next_heading = content.find("\n## ", start + len(heading))
            if next_heading != -1:
                block_text = content[start:next_heading]
            else:
                block_text = content[start:]
            q_count = block_text.count("?")
            assert q_count >= 2, f"Block {i} has {q_count} questions, need >= 2"


class TestCanvasSummary:
    """AC6: Summary template covers all 9 blocks."""

    @pytest.fixture
    def content(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-canvas.md").read_text(
            encoding="utf-8",
        )

    def test_has_summary_template(self, content: str) -> None:
        lower = content.lower()
        assert "resumen" in lower
        # Check the summary section has a table
        resumen_idx = lower.index("resumen")
        after_resumen = content[resumen_idx:]
        assert "|" in after_resumen, "Summary must include a table template"


class TestCanvasCLI:
    """AC7: kokoro init copies the file correctly."""

    def test_init_copies_canvas_skill(self, tmp_path: Path) -> None:
        target = tmp_path / "project"
        target.mkdir()
        init(target=target)
        copied = target / ".claude" / "commands" / "kokoro-canvas.md"
        assert copied.is_file(), "kokoro init must copy kokoro-canvas.md"

    def test_copied_skill_matches_source(
        self, tmp_path: Path, commands_path: Path,
    ) -> None:
        target = tmp_path / "project"
        target.mkdir()
        init(target=target)
        copied = target / ".claude" / "commands" / "kokoro-canvas.md"
        source = commands_path / "kokoro-canvas.md"
        assert copied.read_text() == source.read_text()
