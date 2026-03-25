"""Tests for /kokoro-pescar skill file content."""

from pathlib import Path

from vocabulary_check import find_prohibited_words


class TestPescarSkillExists:
    def test_skill_file_exists(self, commands_path: Path) -> None:
        assert (commands_path / "kokoro-pescar.md").is_file()


class TestPescarContent:
    def _read(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-pescar.md").read_text(encoding="utf-8")

    def test_has_all_pescar_steps(self, commands_path: Path) -> None:
        content = self._read(commands_path)
        for step in ["P —", "E —", "S —", "C —", "A —", "R —"]:
            assert step in content, f"Missing PESCAR step: {step}"

    def test_has_80_20_rule(self, commands_path: Path) -> None:
        assert "80" in self._read(commands_path) and "20" in self._read(commands_path)

    def test_has_calendario_editorial(self, commands_path: Path) -> None:
        assert "Calendario" in self._read(commands_path)


class TestPescarEduardoVoice:
    def _read(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-pescar.md").read_text(encoding="utf-8")

    def test_has_proyector_strategy(self, commands_path: Path) -> None:
        assert "Proyector" in self._read(commands_path)

    def test_has_invitado(self, commands_path: Path) -> None:
        assert "invitado" in self._read(commands_path).lower()

    def test_has_creacion(self, commands_path: Path) -> None:
        assert "creacion" in self._read(commands_path).lower()


class TestPescarAntiVocabulary:
    def test_no_prohibited_words(self, commands_path: Path) -> None:
        content = (commands_path / "kokoro-pescar.md").read_text(encoding="utf-8")
        violations = find_prohibited_words(content)
        assert violations == [], f"Prohibited words: {violations}"


class TestPescarSummary:
    def _read(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-pescar.md").read_text(encoding="utf-8")

    def test_has_output_template(self, commands_path: Path) -> None:
        assert "PESCAR" in self._read(commands_path)

    def test_has_siguiente_paso(self, commands_path: Path) -> None:
        assert "Siguiente paso" in self._read(commands_path)

    def test_has_persistencia(self, commands_path: Path) -> None:
        assert "## Persistencia" in self._read(commands_path)
