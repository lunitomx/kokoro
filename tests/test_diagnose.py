"""Tests for /kokoro-diagnose skill file content and CLI integration."""

from pathlib import Path

import pytest

from kokoro.cli import init


class TestSkillFileExists:
    """AC1: Skill file exists at the correct path."""

    def test_skill_file_exists(self, commands_path: Path) -> None:
        skill = commands_path / "kokoro-diagnose.md"
        msg = "kokoro-diagnose.md must exist in extension/.claude/commands/"
        assert skill.is_file(), msg


class TestSpeedBoatContent:
    """AC2: Skill guides through Speed Boat exercise."""

    @pytest.fixture
    def content(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-diagnose.md").read_text(
            encoding="utf-8",
        )

    def test_mentions_speed_boat(self, content: str) -> None:
        assert "Speed Boat" in content

    def test_mentions_anchors(self, content: str) -> None:
        assert "ancla" in content.lower() or "anchor" in content.lower()

    def test_mentions_wind(self, content: str) -> None:
        assert "viento" in content.lower() or "wind" in content.lower()

    def test_mentions_rocks(self, content: str) -> None:
        # rocks = risks in the Speed Boat metaphor
        lower = content.lower()
        assert "roca" in lower or "riesgo" in lower or "rock" in lower


class TestVision2020Content:
    """AC3: Skill guides through Vision 20/20 exercise."""

    @pytest.fixture
    def content(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-diagnose.md").read_text(
            encoding="utf-8",
        )

    def test_mentions_vision_2020(self, content: str) -> None:
        assert "20/20" in content or "Visión" in content or "Vision" in content

    def test_mentions_clear_vision(self, content: str) -> None:
        assert "clara" in content.lower() or "clear" in content.lower()

    def test_mentions_blurry_vision(self, content: str) -> None:
        assert "borrosa" in content.lower() or "blurry" in content.lower()

    def test_mentions_blind_spots(self, content: str) -> None:
        lower = content.lower()
        has_punto_ciego = "punto" in lower and "ciego" in lower
        assert has_punto_ciego or "blind" in lower


class TestDiagnosticSummary:
    """AC4: Skill produces structured diagnostic summary."""

    @pytest.fixture
    def content(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-diagnose.md").read_text(
            encoding="utf-8",
        )

    def test_has_summary_section(self, content: str) -> None:
        assert "resumen" in content.lower() or "summary" in content.lower()

    def test_has_action_plan(self, content: str) -> None:
        lower = content.lower()
        assert "accion" in lower or "action" in lower or "plan" in lower


class TestEduardoVoice:
    """Skill uses Eduardo's voice patterns."""

    @pytest.fixture
    def content(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-diagnose.md").read_text(
            encoding="utf-8",
        )

    def test_projector_strategy(self, content: str) -> None:
        """Eduardo's Projector strategy: ask before guiding."""
        lower = content.lower()
        assert "invitación" in lower or "invitacion" in lower or "permiso" in lower

    def test_uses_eduardo_vocabulary(self, content: str) -> None:
        """Eduardo never says 'problema', says 'oportunidad' or 'reto'."""
        # Check for at least one Eduardo vocabulary term
        eduardo_terms = [
            "inversión", "inversion", "creación", "creacion",
            "invitado", "montaña", "montana",
        ]
        found = any(term in content.lower() for term in eduardo_terms)
        assert found, "Skill should use Eduardo's vocabulary"


class TestCLICopySkill:
    """AC5: kokoro init copies the skill to .claude/commands/."""

    def test_init_copies_diagnose_skill(self, tmp_path: Path) -> None:
        target = tmp_path / "project"
        target.mkdir()
        init(target=target)
        copied = target / ".claude" / "commands" / "kokoro-diagnose.md"
        assert copied.is_file(), "kokoro init must copy kokoro-diagnose.md"

    def test_copied_skill_matches_source(
        self, tmp_path: Path, commands_path: Path,
    ) -> None:
        target = tmp_path / "project"
        target.mkdir()
        init(target=target)
        copied = target / ".claude" / "commands" / "kokoro-diagnose.md"
        source = commands_path / "kokoro-diagnose.md"
        assert copied.read_text() == source.read_text()

    def test_overwrites_kokoro_skill_on_rerun(self, tmp_path: Path) -> None:
        target = tmp_path / "project"
        target.mkdir()
        commands_dir = target / ".claude" / "commands"
        commands_dir.mkdir(parents=True)
        (commands_dir / "kokoro-diagnose.md").write_text("old version")

        init(target=target)

        content = (commands_dir / "kokoro-diagnose.md").read_text()
        assert content != "old version"
