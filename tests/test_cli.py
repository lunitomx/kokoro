"""Tests for kokoro init CLI."""

from pathlib import Path

import pytest

from kokoro.cli import init


@pytest.fixture
def tmp_target(tmp_path: Path) -> Path:
    """Return a clean temporary directory as init target."""
    return tmp_path / "project"


class TestInitFreshDirectory:
    """Scenario: Fresh install into empty project."""

    def test_creates_claude_directory(self, tmp_target: Path) -> None:
        tmp_target.mkdir()
        init(target=tmp_target)
        assert (tmp_target / ".claude").is_dir()

    def test_creates_claude_md(self, tmp_target: Path) -> None:
        tmp_target.mkdir()
        init(target=tmp_target)
        claude_md = tmp_target / ".claude" / "CLAUDE.md"
        assert claude_md.is_file()
        assert claude_md.read_text().strip() != ""

    def test_creates_commands_directory(self, tmp_target: Path) -> None:
        tmp_target.mkdir()
        init(target=tmp_target)
        assert (tmp_target / ".claude" / "commands").is_dir()

    def test_creates_knowledge_directory(self, tmp_target: Path) -> None:
        tmp_target.mkdir()
        init(target=tmp_target)
        assert (tmp_target / ".claude" / "knowledge").is_dir()


class TestInitExistingClaude:
    """Scenario: Install into project with existing .claude/."""

    def test_appends_with_markers(self, tmp_target: Path) -> None:
        tmp_target.mkdir()
        claude_dir = tmp_target / ".claude"
        claude_dir.mkdir()
        existing_content = "# My Project\n\nExisting instructions.\n"
        (claude_dir / "CLAUDE.md").write_text(existing_content)

        init(target=tmp_target)

        result = (claude_dir / "CLAUDE.md").read_text()
        assert result.startswith(existing_content)
        assert "<!-- KOKORO START -->" in result
        assert "<!-- KOKORO END -->" in result

    def test_preserves_existing_content(self, tmp_target: Path) -> None:
        tmp_target.mkdir()
        claude_dir = tmp_target / ".claude"
        claude_dir.mkdir()
        existing_content = "# My Project\n\nDo not delete this.\n"
        (claude_dir / "CLAUDE.md").write_text(existing_content)

        init(target=tmp_target)

        result = (claude_dir / "CLAUDE.md").read_text()
        assert "Do not delete this." in result

    def test_replaces_existing_kokoro_section(self, tmp_target: Path) -> None:
        tmp_target.mkdir()
        claude_dir = tmp_target / ".claude"
        claude_dir.mkdir()
        old_content = (
            "# My Project\n\n"
            "<!-- KOKORO START -->\nold kokoro content\n<!-- KOKORO END -->\n"
        )
        (claude_dir / "CLAUDE.md").write_text(old_content)

        init(target=tmp_target)

        result = (claude_dir / "CLAUDE.md").read_text()
        assert "old kokoro content" not in result
        assert result.count("<!-- KOKORO START -->") == 1

    def test_does_not_overwrite_existing_commands(self, tmp_target: Path) -> None:
        tmp_target.mkdir()
        claude_dir = tmp_target / ".claude"
        commands_dir = claude_dir / "commands"
        commands_dir.mkdir(parents=True)
        (commands_dir / "my-skill.md").write_text("user skill")

        init(target=tmp_target)

        assert (commands_dir / "my-skill.md").read_text() == "user skill"


class TestInitDefaultTarget:
    """Scenario: kokoro init with no target uses cwd."""

    def test_uses_cwd_when_no_target(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        monkeypatch.chdir(tmp_path)
        init()
        assert (tmp_path / ".claude").is_dir()
