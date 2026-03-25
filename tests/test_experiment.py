"""Tests for /kokoro-experiment skill file content."""

from pathlib import Path

from vocabulary_check import find_prohibited_words


class TestExperimentSkillExists:
    def test_skill_file_exists(self, commands_path: Path) -> None:
        assert (commands_path / "kokoro-experiment.md").is_file()


class TestExperimentContent:
    def _read(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-experiment.md").read_text(encoding="utf-8")

    def test_has_3x3x3_framework(self, commands_path: Path) -> None:
        assert "3x3x3" in self._read(commands_path)

    def test_has_hypothesis_format(self, commands_path: Path) -> None:
        assert "Creemos que" in self._read(commands_path)

    def test_has_build_measure_learn(self, commands_path: Path) -> None:
        content = self._read(commands_path)
        assert "Build" in content
        assert "Measure" in content
        assert "Learn" in content

    def test_has_three_verdicts(self, commands_path: Path) -> None:
        content = self._read(commands_path)
        assert "Perseverar" in content
        assert "Pivotar" in content
        assert "Pausar" in content


class TestExperimentEduardoVoice:
    def _read(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-experiment.md").read_text(encoding="utf-8")

    def test_has_proyector_strategy(self, commands_path: Path) -> None:
        assert "Proyector" in self._read(commands_path)

    def test_has_invitado(self, commands_path: Path) -> None:
        assert "invitado" in self._read(commands_path).lower()

    def test_has_creacion(self, commands_path: Path) -> None:
        assert "creacion" in self._read(commands_path).lower()


class TestExperimentAntiVocabulary:
    def test_no_prohibited_words(self, commands_path: Path) -> None:
        content = (commands_path / "kokoro-experiment.md").read_text(encoding="utf-8")
        violations = find_prohibited_words(content)
        assert violations == [], f"Prohibited words: {violations}"


class TestExperimentSummary:
    def _read(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-experiment.md").read_text(encoding="utf-8")

    def test_has_output_template(self, commands_path: Path) -> None:
        assert "Reporte de Experimento" in self._read(commands_path)

    def test_has_siguiente_paso(self, commands_path: Path) -> None:
        assert "Siguiente paso" in self._read(commands_path)

    def test_has_persistencia(self, commands_path: Path) -> None:
        assert "## Persistencia" in self._read(commands_path)
