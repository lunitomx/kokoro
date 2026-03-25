"""Tests for skill output template structure (S4.4 spike).

Validates that coaching skill files contain well-formed output templates
with required structural elements. Tests the PROMPT structure, not live
Claude output.

Approach: parse skill markdown, extract fenced code blocks, verify
structural elements (headers, tables, cross-references).
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

# Coaching skills that must have output templates (excludes meta-skills)
COACHING_SKILLS: list[str] = [
    "kokoro-diagnose",
    "kokoro-mountain",
    "kokoro-prune",
    "kokoro-finance",
    "kokoro-canvas",
    "kokoro-forces",
    "kokoro-interviews",
    "kokoro-validate",
    "kokoro-research",
]

# All valid /kokoro-X command files (existing + planned Phase 3/4)
VALID_COMMANDS: set[str] = {
    "kokoro",
    "kokoro-diagnose",
    "kokoro-mountain",
    "kokoro-prune",
    "kokoro-finance",
    "kokoro-canvas",
    "kokoro-forces",
    "kokoro-interviews",
    "kokoro-validate",
    "kokoro-session",
    # Phase 3 (planned — referenced in existing skills)
    "kokoro-experiment",
    "kokoro-research",
    "kokoro-pescar",
    "kokoro-launch",
    # Phase 4 (planned)
    "kokoro-factory",
    "kokoro-funnel",
    "kokoro-mafia",
    "kokoro-rhythm",
}

# Commands that must exist as files today
EXISTING_COMMANDS: set[str] = {
    "kokoro",
    "kokoro-diagnose",
    "kokoro-mountain",
    "kokoro-prune",
    "kokoro-finance",
    "kokoro-canvas",
    "kokoro-forces",
    "kokoro-interviews",
    "kokoro-validate",
    "kokoro-session",
    "kokoro-research",
}


def _extract_code_blocks(content: str) -> list[str]:
    """Extract fenced code block contents from markdown."""
    return re.findall(r"```\n(.*?)```", content, re.DOTALL)


def _get_output_template(content: str) -> str:
    """Get the primary output template (longest code block)."""
    blocks = _extract_code_blocks(content)
    if not blocks:
        return ""
    return max(blocks, key=len)


def _extract_cross_refs(content: str) -> list[str]:
    """Extract /kokoro-X references from text."""
    return re.findall(r"`(/kokoro(?:-\w+)?)`", content)


def _read_skill(commands_path: Path, skill_name: str) -> str:
    """Read a skill file and return its content."""
    return (commands_path / f"{skill_name}.md").read_text(encoding="utf-8")


class TestOutputTemplateExists:
    """Every coaching skill must have at least one output template."""

    @pytest.mark.parametrize("skill_name", COACHING_SKILLS)
    def test_has_output_template(
        self, commands_path: Path, skill_name: str
    ) -> None:
        content = _read_skill(commands_path, skill_name)
        blocks = _extract_code_blocks(content)
        assert len(blocks) >= 1, (
            f"{skill_name} must have at least one output template code block"
        )


class TestOutputTemplateStructure:
    """Output templates must have required structural elements."""

    @pytest.fixture(params=COACHING_SKILLS)
    def template_with_name(
        self, commands_path: Path, request: pytest.FixtureRequest
    ) -> tuple[str, str]:
        skill_name: str = request.param
        content = _read_skill(commands_path, skill_name)
        template = _get_output_template(content)
        assert template, f"No code block in {skill_name}"
        return skill_name, template

    def test_has_title_header(
        self, template_with_name: tuple[str, str]
    ) -> None:
        """Output template must have a ## level heading."""
        skill_name, template = template_with_name
        assert re.search(r"^## .+", template, re.MULTILINE), (
            f"{skill_name}: output template must have a ## title header"
        )

    def test_has_table(self, template_with_name: tuple[str, str]) -> None:
        """Output template must include a markdown table."""
        skill_name, template = template_with_name
        assert "|" in template and "---" in template, (
            f"{skill_name}: output template must include a markdown table"
        )

    def test_has_siguiente_paso(
        self, template_with_name: tuple[str, str]
    ) -> None:
        """Output template must have a next-step section."""
        skill_name, template = template_with_name
        assert "siguiente paso" in template.lower(), (
            f"{skill_name}: output template must have 'Siguiente paso'"
        )


class TestCrossReferences:
    """Cross-skill references must point to existing command files."""

    @pytest.mark.parametrize("skill_name", COACHING_SKILLS)
    def test_cross_refs_resolve(
        self, commands_path: Path, skill_name: str
    ) -> None:
        """All /kokoro-X references must point to existing files."""
        content = _read_skill(commands_path, skill_name)
        refs = _extract_cross_refs(content)
        for ref in refs:
            command_name = ref.lstrip("/")
            assert command_name in VALID_COMMANDS, (
                f"{skill_name} references {ref} — not a valid command"
            )
            # Only check file existence for current-phase commands
            if command_name in EXISTING_COMMANDS:
                target = commands_path / f"{command_name}.md"
                assert target.is_file(), (
                    f"{skill_name} references {ref} but {target.name} missing"
                )
