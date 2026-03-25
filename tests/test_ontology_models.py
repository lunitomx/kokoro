"""Tests for kokoro ontology domain models (S3.1)."""

from __future__ import annotations

from datetime import datetime, timezone

import pytest

from kokoro.ontology.models import (
    CoachingEdge,
    CoachingNode,
    CoachingState,
    EdgeType,
    NodeType,
    PhaseProgress,
    SkillCompletion,
)


class TestNodeType:
    """NodeType enum must define all 10 domain concept types."""

    REQUIRED_TYPES: list[str] = [
        "segmento",
        "problema",
        "puv",
        "fuerza",
        "hipotesis",
        "experimento",
        "vision",
        "okr",
        "creacion",
        "metrica",
    ]

    def test_has_all_required_types(self) -> None:
        values = [t.value for t in NodeType]
        for required in self.REQUIRED_TYPES:
            assert required in values, f"NodeType missing: {required}"

    def test_has_at_least_10_types(self) -> None:
        assert len(NodeType) >= 10


class TestEdgeType:
    """EdgeType enum must define all 5 relationship types."""

    REQUIRED_TYPES: list[str] = [
        "alimenta",
        "valida",
        "experimenta",
        "mide",
        "pertenece_a",
    ]

    def test_has_all_required_types(self) -> None:
        values = [t.value for t in EdgeType]
        for required in self.REQUIRED_TYPES:
            assert required in values, f"EdgeType missing: {required}"

    def test_has_at_least_5_types(self) -> None:
        assert len(EdgeType) >= 5


class TestCoachingNode:
    """CoachingNode must serialize and validate correctly."""

    @pytest.fixture
    def sample_node(self) -> CoachingNode:
        return CoachingNode(
            id="SEG-001",
            type=NodeType.SEGMENTO,
            content="Emprendedores digitales en LATAM",
            source_skill="kokoro-canvas",
            created=datetime(2026, 3, 24, tzinfo=timezone.utc),
        )

    def test_node_creation(self, sample_node: CoachingNode) -> None:
        assert sample_node.id == "SEG-001"
        assert sample_node.type == NodeType.SEGMENTO
        assert sample_node.source_skill == "kokoro-canvas"

    def test_node_serialization(self, sample_node: CoachingNode) -> None:
        json_str = sample_node.model_dump_json()
        restored = CoachingNode.model_validate_json(json_str)
        assert restored == sample_node

    def test_node_requires_id(self) -> None:
        with pytest.raises(Exception):  # noqa: B017
            CoachingNode(
                type=NodeType.SEGMENTO,
                content="test",
                source_skill="test",
                created=datetime.now(tz=timezone.utc),
            )  # type: ignore[call-arg]

    def test_node_metadata_default_empty(self, sample_node: CoachingNode) -> None:
        assert sample_node.metadata == {}

    def test_node_metadata_accepts_dict(self) -> None:
        node = CoachingNode(
            id="PRO-001",
            type=NodeType.PROBLEMA,
            content="No tiene claridad financiera",
            source_skill="kokoro-diagnose",
            created=datetime(2026, 3, 24, tzinfo=timezone.utc),
            metadata={"severity": "high", "validated": False},
        )
        assert node.metadata["severity"] == "high"


class TestCoachingEdge:
    """CoachingEdge must define typed relationships between nodes."""

    @pytest.fixture
    def sample_edge(self) -> CoachingEdge:
        return CoachingEdge(
            source="SEG-001",
            target="PRO-001",
            type=EdgeType.ALIMENTA,
        )

    def test_edge_creation(self, sample_edge: CoachingEdge) -> None:
        assert sample_edge.source == "SEG-001"
        assert sample_edge.target == "PRO-001"
        assert sample_edge.type == EdgeType.ALIMENTA

    def test_edge_serialization(self, sample_edge: CoachingEdge) -> None:
        json_str = sample_edge.model_dump_json()
        restored = CoachingEdge.model_validate_json(json_str)
        assert restored == sample_edge

    def test_edge_metadata_default_empty(self, sample_edge: CoachingEdge) -> None:
        assert sample_edge.metadata == {}


class TestSkillCompletion:
    """SkillCompletion tracks when a skill session was completed."""

    def test_creation(self) -> None:
        sc = SkillCompletion(
            skill="kokoro-diagnose",
            completed=datetime(2026, 3, 24, tzinfo=timezone.utc),
            summary="Identified 3 anchors, 2 blind spots",
        )
        assert sc.skill == "kokoro-diagnose"
        assert sc.summary == "Identified 3 anchors, 2 blind spots"

    def test_serialization(self) -> None:
        sc = SkillCompletion(
            skill="kokoro-canvas",
            completed=datetime(2026, 3, 24, tzinfo=timezone.utc),
            summary="Lean Canvas for segment: digital entrepreneurs",
        )
        json_str = sc.model_dump_json()
        restored = SkillCompletion.model_validate_json(json_str)
        assert restored == sc


class TestPhaseProgress:
    """PhaseProgress tracks phase-level completion."""

    def test_default_pending(self) -> None:
        phase = PhaseProgress(phase=1, name="Preparar el Suelo")
        assert phase.status == "pending"
        assert phase.skills_completed == []

    def test_with_completed_skills(self) -> None:
        phase = PhaseProgress(
            phase=1,
            name="Preparar el Suelo",
            status="in_progress",
            skills_completed=[
                SkillCompletion(
                    skill="kokoro-diagnose",
                    completed=datetime(2026, 3, 24, tzinfo=timezone.utc),
                    summary="Diagnóstico completado",
                ),
            ],
        )
        assert len(phase.skills_completed) == 1
        assert phase.status == "in_progress"


class TestCoachingState:
    """CoachingState is the top-level container for all coaching data."""

    @pytest.fixture
    def empty_state(self) -> CoachingState:
        now = datetime(2026, 3, 24, tzinfo=timezone.utc)
        return CoachingState(
            negocio="Tienda Artesanal",
            created=now,
            updated=now,
        )

    @pytest.fixture
    def populated_state(self) -> CoachingState:
        now = datetime(2026, 3, 24, tzinfo=timezone.utc)
        node = CoachingNode(
            id="SEG-001",
            type=NodeType.SEGMENTO,
            content="Artesanos locales",
            source_skill="kokoro-canvas",
            created=now,
        )
        edge = CoachingEdge(
            source="SEG-001",
            target="PRO-001",
            type=EdgeType.ALIMENTA,
        )
        phase = PhaseProgress(
            phase=1,
            name="Preparar el Suelo",
            status="done",
            skills_completed=[
                SkillCompletion(
                    skill="kokoro-diagnose",
                    completed=now,
                    summary="Done",
                ),
            ],
        )
        return CoachingState(
            negocio="Tienda Artesanal",
            phases=[phase],
            nodes=[node],
            edges=[edge],
            created=now,
            updated=now,
        )

    def test_empty_state_defaults(self, empty_state: CoachingState) -> None:
        assert empty_state.version == 1
        assert empty_state.nodes == []
        assert empty_state.edges == []
        assert empty_state.phases == []

    def test_state_round_trip_json(self, populated_state: CoachingState) -> None:
        """Critical: serialize → deserialize must produce identical state."""
        json_str = populated_state.model_dump_json(indent=2)
        restored = CoachingState.model_validate_json(json_str)
        assert restored == populated_state

    def test_state_has_version(self, empty_state: CoachingState) -> None:
        assert empty_state.version == 1

    def test_state_has_negocio(self, populated_state: CoachingState) -> None:
        assert populated_state.negocio == "Tienda Artesanal"

    def test_state_contains_nodes(self, populated_state: CoachingState) -> None:
        assert len(populated_state.nodes) == 1
        assert populated_state.nodes[0].type == NodeType.SEGMENTO

    def test_state_contains_edges(self, populated_state: CoachingState) -> None:
        assert len(populated_state.edges) == 1
        assert populated_state.edges[0].type == EdgeType.ALIMENTA

    def test_state_contains_phases(self, populated_state: CoachingState) -> None:
        assert len(populated_state.phases) == 1
        assert populated_state.phases[0].status == "done"
