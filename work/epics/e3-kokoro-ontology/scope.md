# Epic E3: Kokoro Ontology + Neurosymbolic Memory — Scope

> **Status:** IN PROGRESS
> **Created:** 2026-03-24
> **Problem Brief:** `dev/problem-briefs/e3-kokoro-ontology.md`

## Objective

Give Kokoro a structured memory layer that persists coaching state across
conversations. Domain concepts become queryable nodes with typed relationships,
enabling skills to read prior outputs and enforce Eduardo's methodology
dependencies. Skills remain markdown — the ontology sits underneath.

**Value:** Entrepreneurs stop losing context. Skills become connected processes
over a coherent coaching structure instead of isolated text generators.
Foundation for E5/E6 skill additions.

## Stories

| ID | Story | Size | Status | Description |
|----|-------|:----:|:------:|-------------|
| S3.1 | Ontology Schema | M | Pending | Pydantic models: 10 node types, 5 edge types, CoachingState |
| S3.2 | Persistence Layer | S | Pending | JSON read/write/query, atomic writes, load/save |
| S3.3 | Phase 1 Skill Integration | M | Pending | diagnose, mountain, prune, finance — persist + context |
| S3.4 | Phase 2 Skill Integration | M | Pending | canvas, forces, interviews, validate — persist + context |
| S3.5 | Session + Router Update | S | Pending | kokoro-session and kokoro read progress from state.json |
| S3.6 | Init Update + Compat Tests | S | Pending | kokoro init creates .kokoro/, backward compat verified |

**Total:** 6 stories

## Scope

**In scope (MUST):**
- Pydantic domain models: Segmento, Problema, PUV, Fuerza, Hipotesis, Experimento,
  Vision, OKR, Creacion, Metrica (10 node types)
- Typed edges: alimenta, valida, experimenta, mide, pertenece_a (5 edge types)
- Local JSON persistence (`.kokoro/state.json` in entrepreneur's project)
- Read/write integration for ALL 8 coaching skills (not just 2)
- /kokoro-session and /kokoro router read from state.json for progress
- Graceful degradation: all 313 tests pass without ontology present
- Zero prohibited vocabulary in ontology layer

**In scope (SHOULD):**
- Schema versioning (version field in CoachingState)
- `kokoro init` creates `.kokoro/` with empty state template
- CLI query for state (`kokoro state` or similar)

**Out of scope:**
- Phase 3/4 skill implementation (E5/E6)
- Vector/RAG/embeddings (symbolic only)
- External database (local-first)
- Conversation logging
- General-purpose knowledge graph

## Done Criteria

**Per story:**
- [ ] Tests pass (pyright, ruff, pytest)
- [ ] Commit after each task

**Epic complete:**
- [ ] All 6 stories complete
- [ ] Ontology schema with >= 6 node types, >= 4 edge types
- [ ] Canvas output persists as structured nodes
- [ ] Forces reads canvas state in a fresh context
- [ ] Session detects progress from persisted state
- [ ] All 313+ existing tests pass (graceful degradation)
- [ ] Zero prohibited vocabulary in new code
- [ ] Epic retrospective done

## Dependencies

```
S3.1 (schema) ──→ S3.2 (persistence) ──→ S3.3 (Phase 1 skills)
                                          S3.4 (Phase 2 skills, after S3.3)
                                          S3.5 (session+router, needs S3.2)
S3.6 (init+compat, runs last)
```

- S3.1 first: models must exist before persistence layer
- S3.2 after S3.1: file I/O needs schema to serialize/deserialize
- S3.3 after S3.2: Phase 1 skills need store to persist/read
- S3.4 after S3.3: Phase 2 skills reference Phase 1 outputs
- S3.5 after S3.2: session/router read from persistence
- S3.6 last: validates full backward compat with ontology absent

**External:** None. E1/E2/E4 all done and merged.

## Risks

| Risk | L/I | Mitigation |
|------|:---:|------------|
| Output parsing from LLM is unreliable | M/H | Define output format conventions, not parse free-form |
| Ontology too granular (noise) | M/M | Start with 6 node types, expand only if needed |
| Storage path conflicts between projects | L/M | Use `.kokoro/` in entrepreneur's project root |
| Backward compat breaks | L/H | S3.6 dedicated to this, run full suite |
| Scope creep toward Phase 3 | M/M | Explicit out-of-scope, parking lot for Phase 3 ideas |

## Architecture

**New layer:** `src/kokoro/ontology/` package
- `models.py` — Pydantic node/edge models
- `store.py` — JSON persistence (read/write/query)
- `integration.py` — skill hooks for reading/writing state

**Storage:** `.kokoro/state.json` in the entrepreneur's project directory.
Loaded on session start, written on skill completion.

**Key decision:** Skills write structured output alongside their free-form
markdown output. The structured part goes to the ontology; the markdown
goes to the user. Skills don't need to parse their own output.

## Implementation Plan

> Added by `/rai-epic-plan` — 2026-03-24

### Story Sequence

| Order | Story | Size | Dependencies | Rationale |
|:-----:|-------|:----:|-------------|-----------|
| 1 | S3.1 Ontology Schema | M | None | Walking skeleton: models must exist before anything else can be built or tested |
| 2 | S3.2 Persistence Layer | S | S3.1 | Walking skeleton: completes the minimal E2E path (model → file → model) |
| 3 | S3.3 Phase 1 Skill Integration | M | S3.2 | Risk-first: Phase 1 skills are simpler (fewer cross-refs), proves the integration pattern |
| 4 | S3.4 Phase 2 Skill Integration | M | S3.3 | Dependency-driven: Phase 2 skills read Phase 1 outputs (forces reads canvas) |
| 5 | S3.5 Session + Router Update | S | S3.2 (soft: S3.3-S3.4) | Quick win: session/router only need to read state, not write complex nodes |
| 6 | S3.6 Init Update + Compat Tests | S | S3.3, S3.4, S3.5 | Last: validates full backward compat with and without ontology present |

### Critical Path

```
S3.1 → S3.2 → S3.3 → S3.4 → S3.6
                 ↘ S3.5 ───────↗
```

S3.5 can run in parallel with S3.3/S3.4 (only needs S3.2), but sequential
is safer since all touch skill files. S3.6 waits for everything.

### Milestones

| Milestone | Stories | Success Criteria |
|-----------|---------|------------------|
| **M1: Walking Skeleton** | S3.1, S3.2 | Schema models pass pyright strict, state.json round-trips (write → read → identical), atomic writes tested |
| **M2: Skills Connected** | +S3.3, S3.4 | All 8 coaching skills have persist instructions, at least canvas→forces chain verified (forces reads canvas state) |
| **M3: Epic Complete** | +S3.5, S3.6 | Session reads progress from state, router skips completed phases, `kokoro init` creates .kokoro/, 313+ tests pass, retrospective done |

### Progress Tracking

| Story | Size | Status | Actual | Notes |
|-------|:----:|:------:|:------:|-------|
| S3.1 Ontology Schema | M | Done | S | 23 tests, 7 models, pydantic added |
| S3.2 Persistence Layer | S | Done | S | 19 tests, atomic writes, skill context |
| S3.3 Phase 1 Skill Integration | M | Done | S | 4 skills, persistence + context |
| S3.4 Phase 2 Skill Integration | M | Done | S | 4 skills, persistence + context |
| S3.5 Session + Router Update | S | Done | XS | State-aware routing |
| S3.6 Init Update + Compat Tests | S | Pending | | |

### Sequencing Risks

| Risk | L/I | Mitigation |
|------|:---:|------------|
| Schema churn during skill integration | M/M | S3.1 scope includes all 10 node types upfront, not incremental |
| Persist instructions break Eduardo's voice flow | M/M | Keep persist block at end, after Claude's natural closing |
| S3.3/S3.4 touch all 8 skill files + 8 test files | L/M | Commit after each skill integration, run full suite per file |
