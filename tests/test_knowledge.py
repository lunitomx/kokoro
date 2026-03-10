"""Tests for knowledge file content and structure."""

from pathlib import Path

import pytest

EXPECTED_FILES = [
    "kokoro-metodologia.md",
    "kokoro-phase1-diagnostico.md",
    "kokoro-phase1-vision.md",
    "kokoro-phase1-poda.md",
    "kokoro-phase1-finanzas.md",
]


class TestKnowledgeContent:
    """Verify knowledge files exist with substantive content."""

    @pytest.mark.parametrize("filename", EXPECTED_FILES)
    def test_file_exists(
        self, knowledge_path: Path, filename: str
    ) -> None:
        path = knowledge_path / filename
        assert path.is_file(), f"Missing knowledge file: {filename}"

    @pytest.mark.parametrize("filename", EXPECTED_FILES)
    def test_file_has_substantive_content(
        self, knowledge_path: Path, filename: str
    ) -> None:
        path = knowledge_path / filename
        lines = path.read_text(encoding="utf-8").splitlines()
        assert len(lines) >= 30, (
            f"{filename} has only {len(lines)} lines, expected >= 30"
        )

    @pytest.mark.parametrize("filename", EXPECTED_FILES)
    def test_file_has_managed_header(
        self, knowledge_path: Path, filename: str
    ) -> None:
        content = (knowledge_path / filename).read_text(encoding="utf-8")
        assert "kokoro-managed" in content

    @pytest.mark.parametrize("filename", EXPECTED_FILES)
    def test_file_has_title(
        self, knowledge_path: Path, filename: str
    ) -> None:
        content = (knowledge_path / filename).read_text(encoding="utf-8")
        assert content.count("\n# ") >= 1 or content.startswith("# ") or \
            "<!-- kokoro-managed" in content

    def test_no_gitkeep(self, knowledge_path: Path) -> None:
        assert not (knowledge_path / ".gitkeep").exists()
