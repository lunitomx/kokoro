"""Tests for /kokoro-rhythm skill file content."""

from pathlib import Path

from vocabulary_check import find_prohibited_words


class TestRhythmSkillExists:
    def test_skill_file_exists(self, commands_path: Path) -> None:
        assert (commands_path / "kokoro-rhythm.md").is_file()


class TestRhythmContent:
    def _read(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-rhythm.md").read_text(encoding="utf-8")

    def test_has_90_minutes(self, commands_path: Path) -> None:
        assert "90" in self._read(commands_path)

    def test_has_scorecard(self, commands_path: Path) -> None:
        assert "Scorecard" in self._read(commands_path) or "scorecard" in self._read(commands_path)

    def test_has_ritual_concept(self, commands_path: Path) -> None:
        content = self._read(commands_path)
        assert "Ritual" in content or "ritual" in content or "Ritmo" in content


class TestRhythmEduardoVoice:
    def _read(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-rhythm.md").read_text(encoding="utf-8")

    def test_has_proyector(self, commands_path: Path) -> None:
        assert "Proyector" in self._read(commands_path)

    def test_has_invitado(self, commands_path: Path) -> None:
        assert "invitado" in self._read(commands_path).lower()


class TestRhythmAntiVocabulary:
    def test_no_prohibited_words(self, commands_path: Path) -> None:
        content = (commands_path / "kokoro-rhythm.md").read_text(encoding="utf-8")
        violations = find_prohibited_words(content)
        assert violations == [], f"Prohibited: {violations}"


class TestRhythmSummary:
    def _read(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-rhythm.md").read_text(encoding="utf-8")

    def test_has_siguiente_paso(self, commands_path: Path) -> None:
        content = self._read(commands_path)
        assert "Siguiente paso" in content or "Completaste" in content

    def test_has_persistencia(self, commands_path: Path) -> None:
        assert "## Persistencia" in self._read(commands_path)
