"""Tests for /kokoro-forces skill file content and CLI integration."""

from pathlib import Path

import pytest
from vocabulary_check import find_prohibited_words

from kokoro.cli import init


class TestForcesSkillExists:
    """AC1: Skill file exists at correct path."""

    def test_skill_file_exists(
        self, commands_path: Path,
    ) -> None:
        skill = commands_path / "kokoro-forces.md"
        msg = (
            "kokoro-forces.md must exist in"
            " extension/.claude/commands/"
        )
        assert skill.is_file(), msg


class TestForcesStructure:
    """AC2: Contains all 4 Customer Forces."""

    @pytest.fixture
    def content(self, commands_path: Path) -> str:
        return (
            commands_path / "kokoro-forces.md"
        ).read_text(encoding="utf-8")

    def test_has_four_forces(self, content: str) -> None:
        forces = [
            "Trigger Event",
            "Push",
            "Inercia",
            "Pull y Friccion",
        ]
        lower = content.lower()
        for force in forces:
            assert force.lower() in lower, (
                f"Missing force: {force}"
            )

    def test_trigger_event_is_first_force(
        self, content: str
    ) -> None:
        """Trigger Event must be Fuerza 1."""
        assert "## Fuerza 1" in content
        idx1 = content.index("## Fuerza 1")
        assert "trigger" in content[idx1 : idx1 + 80].lower()

    def test_inercia_present(self, content: str) -> None:
        lower = content.lower()
        assert "inercia" in lower, (
            "Inercia must be present as force/enemy"
        )

    def test_forces_in_order(self, content: str) -> None:
        """Forces appear in prescribed order 1-4."""
        order = [
            "## Fuerza 1",
            "## Fuerza 2",
            "## Fuerza 3",
            "## Fuerza 4",
        ]
        for heading in order:
            assert heading in content, f"Missing: {heading}"
        positions = [content.index(h) for h in order]
        assert positions == sorted(positions), (
            "Forces must be in order 1-4"
        )


class TestForcesContent:
    """AC4: Eduardo's voice present."""

    @pytest.fixture
    def content(self, commands_path: Path) -> str:
        return (
            commands_path / "kokoro-forces.md"
        ).read_text(encoding="utf-8")

    def test_has_eduardo_voice(self, content: str) -> None:
        lower = content.lower()
        eduardo_terms = ["invitado", "creacion", "inversion"]
        found = sum(
            1 for t in eduardo_terms if t in lower
        )
        assert found >= 3, (
            "Skill must use all Eduardo vocabulary"
        )

    def test_references_knowledge_file(
        self, content: str
    ) -> None:
        assert "kokoro-phase2-forces.md" in content

    def test_has_anti_pattern_warnings(
        self, content: str
    ) -> None:
        lower = content.lower()
        has_generic = "deseos genericos" in lower
        has_features = "competir en features" in lower
        has_competing = "competir en caracteristicas" in lower
        assert has_generic or has_features or has_competing, (
            "Must have anti-pattern warnings"
        )

    def test_has_proyector_strategy(
        self, content: str
    ) -> None:
        lower = content.lower()
        assert "permiso" in lower or "invitacion" in lower

    def test_no_prohibited_vocabulary(
        self, content: str
    ) -> None:
        violations = find_prohibited_words(content)
        assert violations == [], (
            f"Prohibited words found: {violations}"
        )


class TestForcesSections:
    """AC5: Each force has guiding questions + key sections."""

    @pytest.fixture
    def content(self, commands_path: Path) -> str:
        return (
            commands_path / "kokoro-forces.md"
        ).read_text(encoding="utf-8")

    def test_each_force_has_guiding_questions(
        self, content: str
    ) -> None:
        """Each of 4 forces must have at least 2 question marks."""
        for i in range(1, 5):
            heading = f"## Fuerza {i}"
            assert heading in content, f"Missing {heading}"
            start = content.index(heading)
            next_heading = content.find(
                "\n## ", start + len(heading)
            )
            if next_heading != -1:
                block_text = content[start:next_heading]
            else:
                block_text = content[start:]
            q_count = block_text.count("?")
            assert q_count >= 2, (
                f"Force {i} has {q_count} questions,"
                f" need >= 2"
            )

    def test_has_customer_criteria(
        self, content: str
    ) -> None:
        lower = content.lower()
        assert "customer criteria" in lower

    def test_has_momento_aja(self, content: str) -> None:
        lower = content.lower()
        assert "momento aja" in lower

    def test_has_oferta_mafia(self, content: str) -> None:
        lower = content.lower()
        assert "oferta mafia" in lower


class TestForcesSummary:
    """AC6: Summary template covers all forces."""

    @pytest.fixture
    def content(self, commands_path: Path) -> str:
        return (
            commands_path / "kokoro-forces.md"
        ).read_text(encoding="utf-8")

    def test_has_summary_template(self, content: str) -> None:
        lower = content.lower()
        assert "resumen" in lower
        resumen_idx = lower.index("resumen")
        after_resumen = content[resumen_idx:]
        table_lines = [
            ln for ln in after_resumen.splitlines() if "|" in ln
        ]
        assert len(table_lines) >= 4, (
            "Summary table must have at least 4 rows"
        )


class TestForcesCLI:
    """AC7: kokoro init copies the file correctly."""

    def test_init_copies_forces_skill(
        self, tmp_path: Path
    ) -> None:
        target = tmp_path / "project"
        target.mkdir()
        init(target=target)
        copied = (
            target
            / ".claude"
            / "commands"
            / "kokoro-forces.md"
        )
        assert copied.is_file(), (
            "kokoro init must copy kokoro-forces.md"
        )

    def test_copied_skill_matches_source(
        self, tmp_path: Path, commands_path: Path,
    ) -> None:
        target = tmp_path / "project"
        target.mkdir()
        init(target=target)
        copied = (
            target
            / ".claude"
            / "commands"
            / "kokoro-forces.md"
        )
        source = commands_path / "kokoro-forces.md"
        assert copied.read_text() == source.read_text()
