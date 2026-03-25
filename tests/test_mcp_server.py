"""Tests for Kokoro MCP server (E7)."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import pytest

from kokoro.mcp_server import (
    SKILLS,
    _build_context,
    _load_identity,
    _load_skill,
    _run_skill,
)
from kokoro.ontology.models import CoachingNode, NodeType
from kokoro.ontology.store import create_empty_state, save_state


class TestSkillRegistry:
    """All 12 coaching skills must be registered."""

    def test_has_12_skills(self) -> None:
        assert len(SKILLS) == 12

    def test_phase1_skills_present(self) -> None:
        phase1 = [
            "kokoro_diagnose", "kokoro_mountain",
            "kokoro_prune", "kokoro_finance",
        ]
        for skill in phase1:
            assert skill in SKILLS, f"Missing: {skill}"

    def test_phase2_skills_present(self) -> None:
        phase2 = [
            "kokoro_canvas", "kokoro_forces",
            "kokoro_interviews", "kokoro_validate",
        ]
        for skill in phase2:
            assert skill in SKILLS, f"Missing: {skill}"

    def test_phase3_skills_present(self) -> None:
        phase3 = [
            "kokoro_research", "kokoro_pescar",
            "kokoro_experiment", "kokoro_launch",
        ]
        for skill in phase3:
            assert skill in SKILLS, f"Missing: {skill}"


class TestLoadSkill:
    """Skill loader returns markdown content."""

    def test_loads_existing_skill(self) -> None:
        content = _load_skill("kokoro-diagnose.md")
        assert "Speed Boat" in content

    def test_error_on_missing_skill(self) -> None:
        content = _load_skill("nonexistent.md")
        assert "Error" in content


class TestLoadIdentity:
    """Identity loader returns Eduardo's CLAUDE.md."""

    def test_loads_identity(self) -> None:
        identity = _load_identity()
        assert "Eduardo" in identity or "Kokoro" in identity


class TestRunSkill:
    """Skill execution combines identity + content + context."""

    def test_returns_skill_content(self) -> None:
        result = _run_skill("kokoro_diagnose")
        assert "Speed Boat" in result

    def test_includes_identity(self) -> None:
        result = _run_skill("kokoro_canvas")
        assert "Eduardo" in result or "Kokoro" in result


class TestBuildContext:
    """Context builder returns relevant nodes from state."""

    def test_empty_when_no_state(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        import kokoro.mcp_server as mod

        monkeypatch.setattr(mod, "_PROJECT_DIR", tmp_path)
        context = _build_context("kokoro_forces")
        assert context == ""

    def test_returns_upstream_nodes(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        import kokoro.mcp_server as mod

        monkeypatch.setattr(mod, "_PROJECT_DIR", tmp_path)
        state = create_empty_state("Test")
        state.nodes.append(
            CoachingNode(
                id="SEG-001",
                type=NodeType.SEGMENTO,
                content="Digital entrepreneurs",
                source_skill="kokoro-canvas",
                created=datetime(2026, 3, 24, tzinfo=timezone.utc),
            )
        )
        save_state(tmp_path, state)
        context = _build_context("kokoro_forces")
        assert "SEG-001" in context
        assert "Digital entrepreneurs" in context
