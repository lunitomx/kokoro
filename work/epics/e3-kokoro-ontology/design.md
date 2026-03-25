---
epic_id: "E3"
grounded_in: "Gemba of src/kokoro/, extension/.claude/commands/, RaiSE memory/graph patterns"
---

# Epic Design: Kokoro Ontology + Neurosymbolic Memory

## Affected Surface (Gemba)

| Module/File | Current State | Changes |
|-------------|---------------|---------|
| `src/kokoro/` | `cli.py` + `__init__.py` only | Add `ontology/` package (models, store, hooks) |
| `extension/.claude/commands/kokoro-*.md` | 8 coaching skills, free-form output | Add structured output block + persist instructions |
| `extension/.claude/commands/kokoro-session.md` | Hardcoded progress detection (asks user) | Read from `.kokoro/state.json` for progress |
| `extension/.claude/commands/kokoro.md` | Router with diagnostic questions | Read progress from state, skip completed phases |
| `tests/` | 313 tests, content-based | Add ontology unit tests + integration tests |
| `.kokoro/` (new, in entrepreneur's project) | Does not exist | `state.json` — coaching state persistence |

## Target Components

| Component | Responsibility | Key Interface |
|-----------|---------------|---------------|
| `ontology.models` | Pydantic models for domain nodes + edges | `CoachingNode`, `CoachingEdge`, `CoachingState` |
| `ontology.store` | JSON persistence: read/write/query | `load_state()`, `save_state()`, `get_node()` |
| `ontology.hooks` | Skill integration: what to persist after each skill | `persist_skill_output()`, `get_skill_context()` |
| Skill files (*.md) | Updated prompts with persist instructions | Structured output block at end of each skill |

## Key Contracts

### Domain Node Types (inspired by RaiSE's GraphNode pattern)

```python
from pydantic import BaseModel
from enum import StrEnum
from datetime import datetime


class NodeType(StrEnum):
    SEGMENTO = "segmento"
    PROBLEMA = "problema"
    PUV = "puv"              # Propuesta Unica de Valor
    FUERZA = "fuerza"
    HIPOTESIS = "hipotesis"
    EXPERIMENTO = "experimento"
    VISION = "vision"        # Montana del Mañana
    OKR = "okr"
    CREACION = "creacion"    # Linea de negocio (from prune)
    METRICA = "metrica"      # Financial metrics


class EdgeType(StrEnum):
    ALIMENTA = "alimenta"       # Segmento → Problema
    VALIDA = "valida"           # Fuerza → PUV
    EXPERIMENTA = "experimenta" # Experimento → Hipotesis
    MIDE = "mide"               # Metrica → Creacion
    PERTENECE_A = "pertenece_a" # Node → Phase/Skill


class CoachingNode(BaseModel):
    id: str                     # e.g., "SEG-001"
    type: NodeType
    content: str                # Summary text
    source_skill: str           # Which /kokoro-X produced this
    created: datetime
    metadata: dict[str, Any] = {}


class CoachingEdge(BaseModel):
    source: str                 # Node ID
    target: str                 # Node ID
    type: EdgeType
    metadata: dict[str, Any] = {}
```

### Coaching State (top-level persistence, like RaiSE's SessionState)

```python
class SkillCompletion(BaseModel):
    skill: str                  # e.g., "kokoro-diagnose"
    completed: datetime
    summary: str                # 1-line what was decided/discovered


class PhaseProgress(BaseModel):
    phase: int                  # 1-4
    name: str                   # "Preparar el Suelo"
    skills_completed: list[SkillCompletion] = []
    status: str = "pending"     # pending | in_progress | done


class CoachingState(BaseModel):
    version: int = 1
    negocio: str = ""           # Business name
    phases: list[PhaseProgress] = []
    nodes: list[CoachingNode] = []
    edges: list[CoachingEdge] = []
    created: datetime
    updated: datetime
```

### Store Interface (like RaiSE's JSONL writer, but single JSON file)

```python
def load_state(project_dir: Path) -> CoachingState | None:
    """Load .kokoro/state.json. Returns None if doesn't exist."""

def save_state(project_dir: Path, state: CoachingState) -> None:
    """Write state to .kokoro/state.json. Atomic write."""

def get_skill_context(state: CoachingState, skill: str) -> dict[str, Any]:
    """Get relevant nodes for a skill (e.g., canvas nodes for forces)."""

def mark_skill_complete(
    state: CoachingState, skill: str, summary: str, nodes: list[CoachingNode]
) -> CoachingState:
    """Mark skill done, add nodes, update phase progress."""
```

## Design Decisions

### D1: Single JSON file, not JSONL

RaiSE uses JSONL for append-only patterns. Kokoro's coaching state is different:
- Small (8 skills max, ~50 nodes max for Phase 1-2)
- Read-modify-write pattern (update phase status, add nodes)
- Needs to be human-inspectable (entrepreneur might look at it)

**Decision:** Single `.kokoro/state.json`, atomic write (write to temp, rename).
JSONL would be overkill for this size and read pattern.

### D2: Skill output convention, not LLM output parsing

The problem brief warns about parsing free-form LLM output. Instead:
- Each skill file gets a "Persistencia" section at the end
- The section instructs Claude to produce a structured YAML block
- The Kokoro CLI provides a `kokoro persist` command that reads the YAML
  and writes to state.json
- Alternative: Claude writes directly to `.kokoro/state.json` via tool use

**Decision:** Instruction-based. Skills tell Claude to output a structured
block. The user copies it or Claude writes it via file tools. No parsing
of free-form output. Simple first.

### D3: Graceful degradation

All existing skills must work without the ontology. Integration is additive:
- If `.kokoro/state.json` exists: skills read context and auto-populate
- If not: skills work exactly as today (ask the user everything)
- New "Persistencia" section is instructions for Claude, not mandatory output

### D4: All 8 skills in one epic

Not a 2-skill PoC. All 8 coaching skills get persistence integration because:
- The value is in the connected chain, not individual persistence
- Each skill integration is S-sized once the schema and store exist
- Partial integration leaves broken chains

## Migration Path

No migration needed. `.kokoro/state.json` is created on first skill completion.
Existing users see no change until they run a skill that triggers persistence.

The `kokoro init` command will be updated to also create a `.kokoro/` directory
with an empty state template.

## Story Refinement

Based on design, stories are revised:

| ID | Story | Size | Description |
|----|-------|:----:|-------------|
| S3.1 | Ontology Schema | M | Pydantic models for 10 node types, 5 edge types, CoachingState |
| S3.2 | Persistence Layer | S | JSON read/write/query, atomic writes, load_state/save_state |
| S3.3 | Phase 1 Skill Integration | M | 4 Phase 1 skills: diagnose, mountain, prune, finance |
| S3.4 | Phase 2 Skill Integration | M | 4 Phase 2 skills: canvas, forces, interviews, validate |
| S3.5 | Session + Router Update | S | kokoro-session and kokoro read from state.json |
| S3.6 | Init Update + Compat Tests | S | kokoro init creates .kokoro/, backward compat verified |

6 stories, same count, refined scope per story.
