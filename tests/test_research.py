"""Tests for /kokoro-research skill file content."""

from pathlib import Path

from vocabulary_check import find_prohibited_words


class TestResearchSkillExists:
    """AC1: Skill file exists at correct path."""

    def test_skill_file_exists(self, commands_path: Path) -> None:
        skill = commands_path / "kokoro-research.md"
        msg = "kokoro-research.md must exist in extension/.claude/commands/"
        assert skill.is_file(), msg


class TestResearchContent:
    """AC2: Contains all 4 research exercises."""

    def _read(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-research.md").read_text(encoding="utf-8")

    def test_has_desk_research(self, commands_path: Path) -> None:
        assert "Investigacion de Escritorio" in self._read(commands_path)

    def test_has_social_listening(self, commands_path: Path) -> None:
        assert "Escucha Social" in self._read(commands_path)

    def test_has_competitive_mapping(self, commands_path: Path) -> None:
        assert "Mapeo Competitivo" in self._read(commands_path)

    def test_has_synthesis(self, commands_path: Path) -> None:
        content = self._read(commands_path)
        assert "Sintesis" in content or "Triangul" in content

    def test_has_triangulation_concept(self, commands_path: Path) -> None:
        assert "triangul" in self._read(commands_path).lower()


class TestResearchEduardoVoice:
    """AC3: Eduardo's voice is present."""

    def _read(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-research.md").read_text(encoding="utf-8")

    def test_has_proyector_strategy(self, commands_path: Path) -> None:
        assert "Proyector" in self._read(commands_path)

    def test_has_invitado_vocabulary(self, commands_path: Path) -> None:
        assert "invitado" in self._read(commands_path).lower()

    def test_has_creacion_vocabulary(self, commands_path: Path) -> None:
        assert "creacion" in self._read(commands_path).lower()


class TestResearchAntiVocabulary:
    """AC4: No prohibited words in skill content."""

    def test_no_prohibited_words(self, commands_path: Path) -> None:
        content = (commands_path / "kokoro-research.md").read_text(encoding="utf-8")
        violations = find_prohibited_words(content)
        assert violations == [], (
            f"Prohibited words found: {violations}"
        )


class TestResearchSummary:
    """AC5: Output template has required structure."""

    def _read(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-research.md").read_text(encoding="utf-8")

    def test_has_output_template(self, commands_path: Path) -> None:
        assert "Research Brief" in self._read(commands_path)

    def test_has_siguiente_paso(self, commands_path: Path) -> None:
        assert "Siguiente paso" in self._read(commands_path)

    def test_references_pescar(self, commands_path: Path) -> None:
        assert "/kokoro-pescar" in self._read(commands_path)

    def test_has_persistencia(self, commands_path: Path) -> None:
        assert "## Persistencia" in self._read(commands_path)
