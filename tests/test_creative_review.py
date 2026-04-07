"""Tests for /kokoro-creative-review skill file content."""

from pathlib import Path

from vocabulary_check import find_prohibited_words


class TestCreativeReviewSkillExists:
    """AC1: Skill file exists at correct path."""

    def test_skill_file_exists(self, commands_path: Path) -> None:
        skill = commands_path / "kokoro-creative-review.md"
        msg = "kokoro-creative-review.md must exist in extension/.claude/commands/"
        assert skill.is_file(), msg


class TestCreativeReviewContent:
    """AC2: Contains all 4 Meta AI analysis lenses."""

    def _read(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-creative-review.md").read_text(encoding="utf-8")

    def test_has_gem_lens(self, commands_path: Path) -> None:
        assert "GEM" in self._read(commands_path)

    def test_has_andromeda_lens(self, commands_path: Path) -> None:
        assert "Andromeda" in self._read(commands_path)

    def test_has_lattice_lens(self, commands_path: Path) -> None:
        assert "Lattice" in self._read(commands_path)

    def test_has_sequence_learning_lens(self, commands_path: Path) -> None:
        assert "Sequence" in self._read(commands_path)

    def test_has_scoring_system(self, commands_path: Path) -> None:
        content = self._read(commands_path)
        assert "/10" in content

    def test_has_diversification_matrix(self, commands_path: Path) -> None:
        content = self._read(commands_path)
        assert "Matriz" in content or "Diversificacion" in content


class TestCreativeReviewEduardoVoice:
    """AC3: Uses Eduardo's voice patterns."""

    def _read(self, commands_path: Path) -> str:
        return (commands_path / "kokoro-creative-review.md").read_text(encoding="utf-8")

    def test_has_proyector_strategy(self, commands_path: Path) -> None:
        content = self._read(commands_path).lower()
        assert "proyector" in content or "invitacion" in content

    def test_has_invitado_vocabulary(self, commands_path: Path) -> None:
        assert "invitado" in self._read(commands_path).lower()

    def test_has_espejo_pattern(self, commands_path: Path) -> None:
        content = self._read(commands_path).lower()
        assert "espejo" in content or "amortiguar" in content


class TestCreativeReviewAntiVocabulary:
    """AC4: No prohibited words."""

    def test_no_prohibited_words(self, commands_path: Path) -> None:
        content = (commands_path / "kokoro-creative-review.md").read_text(encoding="utf-8")
        found = find_prohibited_words(content)
        assert not found, f"Prohibited words found: {found}"


class TestCreativeReviewKnowledge:
    """AC5: Knowledge files exist."""

    def test_meta_ai_ecosystem_exists(self, knowledge_path: Path) -> None:
        f = knowledge_path / "kokoro-meta-ai-ecosystem.md"
        assert f.is_file(), "kokoro-meta-ai-ecosystem.md must exist"

    def test_creative_diversification_exists(self, knowledge_path: Path) -> None:
        f = knowledge_path / "kokoro-creative-diversification.md"
        assert f.is_file(), "kokoro-creative-diversification.md must exist"

    def test_references_knowledge_files(self, commands_path: Path) -> None:
        content = (commands_path / "kokoro-creative-review.md").read_text(encoding="utf-8")
        assert "kokoro-meta-ai-ecosystem.md" in content
        assert "kokoro-creative-diversification.md" in content
