"""Tests for /kokoro-mafia skill file content."""

from pathlib import Path

from vocabulary_check import find_prohibited_words


class TestMafiaSkillExists:
    def test_skill_file_exists(self, commands_path: Path) -> None:
        assert (commands_path / "kokoro-mafia.md").is_file()


class TestMafiaContent:
    def _read(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-mafia.md").read_text(encoding="utf-8")

    def test_has_customer_forces(self, commands_path: Path) -> None:
        content = self._read(commands_path)
        assert "Trigger" in content
        assert "Inercia" in content or "Friccion" in content

    def test_has_offer_formula(self, commands_path: Path) -> None:
        content = self._read(commands_path)
        assert "Resultado" in content and "Garantia" in content


class TestMafiaEduardoVoice:
    def _read(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-mafia.md").read_text(encoding="utf-8")

    def test_has_proyector(self, commands_path: Path) -> None:
        assert "Proyector" in self._read(commands_path)

    def test_has_invitado(self, commands_path: Path) -> None:
        assert "invitado" in self._read(commands_path).lower()


class TestMafiaAntiVocabulary:
    def test_no_prohibited_words(self, commands_path: Path) -> None:
        content = (commands_path / "kokoro-mafia.md").read_text(encoding="utf-8")
        violations = find_prohibited_words(content)
        assert violations == [], f"Prohibited: {violations}"


class TestMafiaSummary:
    def _read(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-mafia.md").read_text(encoding="utf-8")

    def test_has_siguiente_paso(self, commands_path: Path) -> None:
        assert "Siguiente paso" in self._read(commands_path)

    def test_has_persistencia(self, commands_path: Path) -> None:
        assert "## Persistencia" in self._read(commands_path)
