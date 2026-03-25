# ADR-001: Coaching State Persistence Mechanism

## Status
Accepted

## Context
Kokoro needs to persist coaching state between conversations. The entrepreneur's
progress, decisions, and artifacts must survive conversation boundaries so that
skills can read prior outputs and enforce methodology dependencies.

## Decision
Use a single `.kokoro/state.json` file in the entrepreneur's project directory.

**Format:** JSON (not JSONL, not SQLite, not YAML)
**Location:** `.kokoro/state.json` relative to project root
**Write pattern:** Read-modify-write with atomic rename (write to `.tmp`, rename)
**Schema:** Pydantic `CoachingState` model with embedded nodes and edges

## Rationale

### Why JSON over JSONL
- Coaching state is small (~50 nodes max for Phase 1-2)
- Access pattern is read-modify-write, not append-only
- Must be human-inspectable (entrepreneur might look at it)
- RaiSE uses JSONL for patterns because they're append-only and high-volume;
  coaching state is neither

### Why not SQLite
- Adds dependency for small dataset
- Not human-inspectable
- Overkill for 8-skill, 50-node graph

### Why not RaiSE's memory adapter
- Kokoro state is entrepreneur-facing, not developer-facing
- Different lifecycle (persists across Kokoro usage, not RaiSE sessions)
- Coupling to RaiSE internals would break Kokoro's portability as standalone package

## Consequences
- Simple implementation, no new dependencies
- Human-readable state file aids debugging
- Concurrent writes are not safe (acceptable: one conversation at a time)
- File size is bounded by methodology scope (~50 nodes max)
