"""Tests for Phase 2 knowledge file content and structure."""

from pathlib import Path

import pytest

PHASE2_FILES = [
    "kokoro-phase2-canvas.md",
    "kokoro-phase2-forces.md",
    "kokoro-phase2-interviews.md",
    "kokoro-phase2-validation.md",
]


class TestPhase2FilesExist:
    """AC1: All 4 Phase 2 knowledge files exist."""

    @pytest.mark.parametrize("filename", PHASE2_FILES)
    def test_file_exists(self, knowledge_path: Path, filename: str) -> None:
        path = knowledge_path / filename
        assert path.is_file(), f"Missing knowledge file: {filename}"


class TestPhase2Structure:
    """AC2: Each file follows PAT-L-008 structure."""

    @pytest.mark.parametrize("filename", PHASE2_FILES)
    def test_file_has_kokoro_managed_header(
        self, knowledge_path: Path, filename: str
    ) -> None:
        content = (knowledge_path / filename).read_text(encoding="utf-8")
        assert "kokoro-managed" in content

    @pytest.mark.parametrize("filename", PHASE2_FILES)
    def test_file_has_proposito_section(
        self, knowledge_path: Path, filename: str
    ) -> None:
        content = (knowledge_path / filename).read_text(encoding="utf-8")
        assert "## Proposito" in content

    @pytest.mark.parametrize("filename", PHASE2_FILES)
    def test_file_has_conexion_section(
        self, knowledge_path: Path, filename: str
    ) -> None:
        content = (knowledge_path / filename).read_text(encoding="utf-8")
        assert "## Conexion con Otros Skills" in content

    @pytest.mark.parametrize("filename", PHASE2_FILES)
    def test_file_has_substantive_content(
        self, knowledge_path: Path, filename: str
    ) -> None:
        path = knowledge_path / filename
        lines = path.read_text(encoding="utf-8").splitlines()
        assert len(lines) >= 30, (
            f"{filename} has only {len(lines)} lines, expected >= 30"
        )


class TestCanvasContent:
    """AC3: Canvas file has Lean Canvas methodology content."""

    @pytest.fixture
    def content(self, knowledge_path: Path) -> str:
        return (knowledge_path / "kokoro-phase2-canvas.md").read_text(
            encoding="utf-8"
        )

    def test_has_segmento(self, content: str) -> None:
        assert "segmento" in content.lower()

    def test_has_propuesta_unica_de_valor(self, content: str) -> None:
        assert "propuesta unica de valor" in content.lower()

    def test_has_ventaja_injusta(self, content: str) -> None:
        assert "ventaja injusta" in content.lower()

    def test_has_nine_blocks(self, content: str) -> None:
        lower = content.lower()
        assert "9 bloques" in lower or "nueve bloques" in lower

    def test_has_segment_first_order(self, content: str) -> None:
        lower = content.lower()
        assert "nunca iniciar por la solucion" in lower or "nunca empezar por la solucion" in lower


class TestForcesContent:
    """AC3: Forces file has Customer Forces methodology content."""

    @pytest.fixture
    def content(self, knowledge_path: Path) -> str:
        return (knowledge_path / "kokoro-phase2-forces.md").read_text(
            encoding="utf-8"
        )

    def test_has_trigger(self, content: str) -> None:
        assert "trigger" in content.lower()

    def test_has_inercia(self, content: str) -> None:
        assert "inercia" in content.lower()

    def test_has_friccion(self, content: str) -> None:
        assert "friccion" in content.lower()

    def test_has_oferta_mafia(self, content: str) -> None:
        assert "oferta mafia" in content.lower()


class TestInterviewsContent:
    """AC3: Interviews file has interview methodology content."""

    @pytest.fixture
    def content(self, knowledge_path: Path) -> str:
        return (knowledge_path / "kokoro-phase2-interviews.md").read_text(
            encoding="utf-8"
        )

    def test_has_escuchar(self, content: str) -> None:
        assert "escucha" in content.lower()

    def test_has_15_minutos(self, content: str) -> None:
        assert "15 minutos" in content

    def test_has_problema_interview(self, content: str) -> None:
        lower = content.lower()
        assert "entrevista" in lower and "problema" in lower


class TestValidationContent:
    """AC3: Validation file has experiment design content."""

    @pytest.fixture
    def content(self, knowledge_path: Path) -> str:
        return (knowledge_path / "kokoro-phase2-validation.md").read_text(
            encoding="utf-8"
        )

    def test_has_3x3x3(self, content: str) -> None:
        assert "3x3x3" in content

    def test_has_hipotesis(self, content: str) -> None:
        assert "hipotesis" in content.lower()

    def test_has_construir_medir_aprender(self, content: str) -> None:
        lower = content.lower()
        assert "construir" in lower and "medir" in lower and "aprender" in lower
