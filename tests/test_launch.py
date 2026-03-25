"""Tests for /kokoro-launch skill file content."""

from pathlib import Path

from vocabulary_check import find_prohibited_words


class TestLaunchSkillExists:
    def test_skill_file_exists(self, commands_path: Path) -> None:
        assert (commands_path / "kokoro-launch.md").is_file()


class TestLaunchContent:
    def _read(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-launch.md").read_text(encoding="utf-8")

    def test_has_copy_exercise(self, commands_path: Path) -> None:
        assert "Copy de Propuesta de Valor" in self._read(commands_path)

    def test_has_landing_structure(self, commands_path: Path) -> None:
        assert "Landing Page" in self._read(commands_path)

    def test_has_launch_sequence(self, commands_path: Path) -> None:
        assert "Secuencia de Lanzamiento" in self._read(commands_path)

    def test_has_checklist(self, commands_path: Path) -> None:
        assert "Checklist" in self._read(commands_path)

    def test_has_pre_launch(self, commands_path: Path) -> None:
        assert "Pre-launch" in self._read(commands_path) or "pre-lanzamiento" in self._read(commands_path).lower()


class TestLaunchEduardoVoice:
    def _read(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-launch.md").read_text(encoding="utf-8")

    def test_has_proyector_strategy(self, commands_path: Path) -> None:
        assert "Proyector" in self._read(commands_path)

    def test_has_invitado(self, commands_path: Path) -> None:
        assert "invitado" in self._read(commands_path).lower()

    def test_has_creacion(self, commands_path: Path) -> None:
        assert "creacion" in self._read(commands_path).lower()

    def test_guides_not_generates(self, commands_path: Path) -> None:
        """Launch must guide copy creation, not generate generic copy."""
        content = self._read(commands_path)
        assert "GUIA" in content.upper() or "guia" in content.lower()


class TestLaunchAntiVocabulary:
    def test_no_prohibited_words(self, commands_path: Path) -> None:
        content = (commands_path / "kokoro-launch.md").read_text(encoding="utf-8")
        violations = find_prohibited_words(content)
        assert violations == [], f"Prohibited words: {violations}"


class TestLaunchSummary:
    def _read(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-launch.md").read_text(encoding="utf-8")

    def test_has_output_template(self, commands_path: Path) -> None:
        assert "Plan de Lanzamiento" in self._read(commands_path)

    def test_has_siguiente_paso(self, commands_path: Path) -> None:
        assert "Siguiente paso" in self._read(commands_path)

    def test_has_persistencia(self, commands_path: Path) -> None:
        assert "## Persistencia" in self._read(commands_path)
