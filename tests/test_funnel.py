"""Tests for /kokoro-funnel skill file content."""

from pathlib import Path

from vocabulary_check import find_prohibited_words


class TestFunnelSkillExists:
    def test_skill_file_exists(self, commands_path: Path) -> None:
        assert (commands_path / "kokoro-funnel.md").is_file()


class TestFunnelContent:
    def _read(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-funnel.md").read_text(encoding="utf-8")

    def test_has_five_stages(self, commands_path: Path) -> None:
        content = self._read(commands_path)
        for stage in ["Conciencia", "Consideracion", "Decision"]:
            assert stage in content, f"Missing: {stage}"

    def test_has_consciente_concept(self, commands_path: Path) -> None:
        assert "Consciente" in self._read(commands_path)


class TestFunnelEduardoVoice:
    def _read(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-funnel.md").read_text(encoding="utf-8")

    def test_has_proyector(self, commands_path: Path) -> None:
        assert "Proyector" in self._read(commands_path)

    def test_has_invitado(self, commands_path: Path) -> None:
        assert "invitado" in self._read(commands_path).lower()


class TestFunnelAntiVocabulary:
    def test_no_prohibited_words(self, commands_path: Path) -> None:
        content = (commands_path / "kokoro-funnel.md").read_text(encoding="utf-8")
        violations = find_prohibited_words(content)
        assert violations == [], f"Prohibited: {violations}"


class TestFunnelSummary:
    def _read(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-funnel.md").read_text(encoding="utf-8")

    def test_has_siguiente_paso(self, commands_path: Path) -> None:
        assert "Siguiente paso" in self._read(commands_path)

    def test_has_persistencia(self, commands_path: Path) -> None:
        assert "## Persistencia" in self._read(commands_path)
