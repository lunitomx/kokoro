"""Tests for /kokoro-pulse skill file content and CLI integration."""

from pathlib import Path

import pytest
from vocabulary_check import find_prohibited_words

from kokoro.cli import init


class TestSkillFileExists:
    """Skill file exists at the correct path."""

    def test_skill_file_exists(self, commands_path: Path) -> None:
        skill = commands_path / "kokoro-pulse.md"
        msg = "kokoro-pulse.md must exist in extension/.claude/commands/"
        assert skill.is_file(), msg

    def test_knowledge_file_exists(self, knowledge_path: Path) -> None:
        knowledge = knowledge_path / "kokoro-pulse-guide.md"
        msg = "kokoro-pulse-guide.md must exist in extension/.claude/knowledge/"
        assert knowledge.is_file(), msg


class TestSkillContent:
    """Skill has required structural elements."""

    @pytest.fixture
    def content(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-pulse.md").read_text(
            encoding="utf-8",
        )

    def test_has_two_modes(self, content: str) -> None:
        """Skill supports prompt and recomendaciones modes."""
        lower = content.lower()
        assert "prompt" in lower
        assert "recomendaciones" in lower or "recomienda" in lower

    def test_uses_websearch(self, content: str) -> None:
        """Skill searches via WebSearch, no paid APIs."""
        assert "WebSearch" in content

    def test_searches_reddit(self, content: str) -> None:
        """Skill searches Reddit as a source."""
        lower = content.lower()
        assert "reddit" in lower

    def test_searches_youtube(self, content: str) -> None:
        """Skill searches YouTube as a source."""
        lower = content.lower()
        assert "youtube" in lower

    def test_output_in_spanish(self, content: str) -> None:
        """Skill specifies output in Spanish."""
        lower = content.lower()
        assert "español" in lower or "espanol" in lower

    def test_detects_prompt_intent(self, content: str) -> None:
        """Skill detects when user asks for a prompt."""
        lower = content.lower()
        has_detection = (
            "detecta" in lower
            or "identifica" in lower
            or "intento" in lower
            or "intent" in lower
        )
        assert has_detection

    def test_synthesizes_findings(self, content: str) -> None:
        """Skill synthesizes research into actionable output."""
        lower = content.lower()
        assert "sintetiza" in lower or "sintesis" in lower


class TestEduardoVoice:
    """Skill uses Eduardo's voice patterns."""

    @pytest.fixture
    def content(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-pulse.md").read_text(
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

    def test_no_prohibited_vocabulary(self, content: str) -> None:
        violations = find_prohibited_words(content)
        assert violations == [], (
            f"Prohibited words found: {violations}"
        )


class TestCLICopySkill:
    """kokoro init copies the pulse skill to .claude/commands/."""

    def test_init_copies_pulse_skill(self, tmp_path: Path) -> None:
        target = tmp_path / "project"
        target.mkdir()
        init(target=target)
        copied = target / ".claude" / "commands" / "kokoro-pulse.md"
        assert copied.is_file(), "kokoro init must copy kokoro-pulse.md"

    def test_init_copies_pulse_knowledge(self, tmp_path: Path) -> None:
        target = tmp_path / "project"
        target.mkdir()
        init(target=target)
        copied = target / ".claude" / "knowledge" / "kokoro-pulse-guide.md"
        assert copied.is_file(), "kokoro init must copy kokoro-pulse-guide.md"

    def test_copied_skill_matches_source(
        self,
        tmp_path: Path,
        commands_path: Path,
    ) -> None:
        target = tmp_path / "project"
        target.mkdir()
        init(target=target)
        copied = target / ".claude" / "commands" / "kokoro-pulse.md"
        source = commands_path / "kokoro-pulse.md"
        assert copied.read_text() == source.read_text()
