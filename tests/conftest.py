"""Shared test fixtures for kokoro tests."""

from pathlib import Path

import pytest


@pytest.fixture
def extension_path() -> Path:
    """Path to the extension/ directory."""
    return Path(__file__).resolve().parent.parent / "extension"


@pytest.fixture
def knowledge_path(extension_path: Path) -> Path:
    """Path to extension/.claude/knowledge/ directory."""
    return extension_path / ".claude" / "knowledge"


@pytest.fixture
def commands_path(extension_path: Path) -> Path:
    """Path to extension/.claude/commands/ directory."""
    return extension_path / ".claude" / "commands"
