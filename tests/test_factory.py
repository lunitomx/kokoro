"""Tests for /kokoro-factory skill file content."""

from pathlib import Path

from vocabulary_check import find_prohibited_words


class TestFactorySkillExists:
    def test_skill_file_exists(self, commands_path: Path) -> None:
        assert (commands_path / "kokoro-factory.md").is_file()


class TestFactoryContent:
    def _read(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-factory.md").read_text(encoding="utf-8")

    def test_has_five_factory_steps(self, commands_path: Path) -> None:
        content = self._read(commands_path)
        for step in ["Adquirir", "Activar", "Retener"]:
            assert step in content, f"Missing step: {step}"

    def test_has_ltv_cpa(self, commands_path: Path) -> None:
        content = self._read(commands_path)
        assert "LTV" in content
        assert "CPA" in content


class TestFactoryEduardoVoice:
    def _read(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-factory.md").read_text(encoding="utf-8")

    def test_has_proyector(self, commands_path: Path) -> None:
        assert "Proyector" in self._read(commands_path)

    def test_has_invitado(self, commands_path: Path) -> None:
        assert "invitado" in self._read(commands_path).lower()

    def test_has_creacion(self, commands_path: Path) -> None:
        assert "creacion" in self._read(commands_path).lower()


class TestFactoryAntiVocabulary:
    def test_no_prohibited_words(self, commands_path: Path) -> None:
        content = (commands_path / "kokoro-factory.md").read_text(encoding="utf-8")
        violations = find_prohibited_words(content)
        assert violations == [], f"Prohibited: {violations}"


class TestFactorySummary:
    def _read(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-factory.md").read_text(encoding="utf-8")

    def test_has_siguiente_paso(self, commands_path: Path) -> None:
        assert "Siguiente paso" in self._read(commands_path)

    def test_has_persistencia(self, commands_path: Path) -> None:
        assert "## Persistencia" in self._read(commands_path)
