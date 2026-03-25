"""Domain models for Eduardo's coaching methodology ontology.

Defines the node types (coaching concepts), edge types (relationships),
and the top-level CoachingState container for persistence.
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any

from pydantic import BaseModel

if sys.version_info >= (3, 11):
    from enum import StrEnum
else:
    from enum import Enum

    class StrEnum(str, Enum):  # type: ignore[no-redef]
        """Backport of StrEnum for Python 3.10."""


class NodeType(StrEnum):
    """Domain concept types in Eduardo's coaching methodology.

    Each type represents a concept that coaching skills produce or consume.
    """

    SEGMENTO = "segmento"
    """Segmento de invitados — who the entrepreneur serves."""

    PROBLEMA = "problema"
    """Reto u oportunidad identified for a segment."""

    PUV = "puv"
    """Propuesta Unica de Valor — unique value proposition."""

    FUERZA = "fuerza"
    """Customer Force — push, pull, inertia, or friction."""

    HIPOTESIS = "hipotesis"
    """Hypothesis to validate through experiments."""

    EXPERIMENTO = "experimento"
    """Validation experiment designed to test a hypothesis."""

    VISION = "vision"
    """Montana del Manana — 3-year strategic vision."""

    OKR = "okr"
    """Objective and Key Results from mountain exercise."""

    CREACION = "creacion"
    """Linea de negocio — a product/service line (from prune)."""

    METRICA = "metrica"
    """Financial or performance metric for a creacion."""


class EdgeType(StrEnum):
    """Typed relationships between coaching concepts.

    Encodes Eduardo's methodology dependencies.
    """

    ALIMENTA = "alimenta"
    """Segmento alimenta Problema — a segment feeds a problem."""

    VALIDA = "valida"
    """Fuerza valida PUV — a customer force validates the value prop."""

    EXPERIMENTA = "experimenta"
    """Experimento experimenta Hipotesis — an experiment tests a hypothesis."""

    MIDE = "mide"
    """Metrica mide Creacion — a metric measures a business line."""

    PERTENECE_A = "pertenece_a"
    """Node pertenece_a Phase/Skill — attribution to origin."""


class CoachingNode(BaseModel):
    """A domain concept node in the coaching ontology."""

    id: str
    type: NodeType
    content: str
    source_skill: str
    created: datetime
    metadata: dict[str, Any] = {}


class CoachingEdge(BaseModel):
    """A typed relationship between two coaching nodes."""

    source: str
    target: str
    type: EdgeType
    metadata: dict[str, Any] = {}


class SkillCompletion(BaseModel):
    """Record of a completed coaching skill session."""

    skill: str
    completed: datetime
    summary: str


class PhaseProgress(BaseModel):
    """Phase-level progress tracking."""

    phase: int
    name: str
    skills_completed: list[SkillCompletion] = []
    status: str = "pending"


class CoachingState(BaseModel):
    """Top-level container for all coaching state.

    Persisted as `.kokoro/state.json` in the entrepreneur's project.
    """

    version: int = 1
    negocio: str = ""
    phases: list[PhaseProgress] = []
    nodes: list[CoachingNode] = []
    edges: list[CoachingEdge] = []
    created: datetime
    updated: datetime
