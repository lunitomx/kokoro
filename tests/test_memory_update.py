"""Tests for MEMORY.md auto-update from client sync."""

from __future__ import annotations

from pathlib import Path

from kokoro.clients.sync import update_memory_index


class TestUpdateMemoryIndex:
    """Update MEMORY.md with new reference entries."""

    def test_adds_new_entry(self, tmp_path: Path) -> None:
        """Adds entry for new reference file."""
        memory_md = tmp_path / "MEMORY.md"
        memory_md.write_text(
            "# Memory\n\n## References\n\n## Feedback\n",
            encoding="utf-8",
        )
        ref_file = tmp_path / "reference_test_client.md"
        ref_file.write_text("content", encoding="utf-8")

        updated = update_memory_index(memory_md, [ref_file])
        assert updated
        content = memory_md.read_text(encoding="utf-8")
        assert "reference_test_client.md" in content

    def test_skips_existing_entry(self, tmp_path: Path) -> None:
        """Does not duplicate existing entries."""
        memory_md = tmp_path / "MEMORY.md"
        memory_md.write_text(
            "# Memory\n\n## References\n\n"
            "- [Test](reference_test_client.md) — exists\n\n"
            "## Feedback\n",
            encoding="utf-8",
        )
        ref_file = tmp_path / "reference_test_client.md"
        ref_file.write_text("content", encoding="utf-8")

        updated = update_memory_index(memory_md, [ref_file])
        assert not updated
        content = memory_md.read_text(encoding="utf-8")
        assert content.count("reference_test_client.md") == 1

    def test_no_memory_file(self, tmp_path: Path) -> None:
        """Returns False when MEMORY.md doesn't exist."""
        memory_md = tmp_path / "MEMORY.md"
        ref_file = tmp_path / "reference_test.md"
        ref_file.write_text("content", encoding="utf-8")

        updated = update_memory_index(memory_md, [ref_file])
        assert not updated

    def test_empty_file_list(self, tmp_path: Path) -> None:
        """Returns False for empty file list."""
        memory_md = tmp_path / "MEMORY.md"
        memory_md.write_text("# Memory\n", encoding="utf-8")

        updated = update_memory_index(memory_md, [])
        assert not updated

    def test_multiple_new_entries(self, tmp_path: Path) -> None:
        """Adds multiple new entries at once."""
        memory_md = tmp_path / "MEMORY.md"
        memory_md.write_text(
            "# Memory\n\n## References\n\n## Feedback\n",
            encoding="utf-8",
        )
        files: list[Path] = []
        for name in ["alpha", "beta"]:
            f = tmp_path / f"reference_{name}.md"
            f.write_text("content", encoding="utf-8")
            files.append(f)

        updated = update_memory_index(memory_md, files)
        assert updated
        content = memory_md.read_text(encoding="utf-8")
        assert "reference_alpha.md" in content
        assert "reference_beta.md" in content
