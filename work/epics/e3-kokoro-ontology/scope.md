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
| S3.1 | Ontology Schema | M | Pending | Pydantic models for domain nodes + typed edges |
| S3.2 | Persistence Layer | S | Pending | Local JSON file read/write with schema validation |
| S3.3 | Canvas Integration | M | Pending | /kokoro-canvas writes structured output to ontology |
| S3.4 | Forces Integration | S | Pending | /kokoro-forces reads canvas state, writes force map |
| S3.5 | Session State | M | Pending | /kokoro-session reads ontology for progress tracking |
| S3.6 | Backward Compatibility | S | Pending | Graceful degradation tests, migration from no-state |

**Total:** 6 stories

## Scope

**In scope (MUST):**
- Pydantic domain models: Segmento, Problema, PUV, Fuerza, Hipotesis, Experimento
- Typed edges: alimenta, valida, experimenta, mide
- Local JSON persistence (entrepreneur's project directory)
- Read/write integration for /kokoro-canvas and /kokoro-forces
- /kokoro-session progress from persisted state
- Graceful degradation: all 313 tests pass without ontology present
- Zero prohibited vocabulary in ontology layer

**In scope (SHOULD):**
- Integration with remaining Phase 1/2 skills
- Schema versioning for future migrations
- CLI query interface for ontology state

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
S3.1 (schema) ──→ S3.2 (persistence) ──→ S3.3 (canvas)
                                          S3.4 (forces, needs S3.3)
                                          S3.5 (session, needs S3.2)
S3.6 (compat, independent but runs last)
```

- S3.1 first: models must exist before persistence
- S3.2 after S3.1: file I/O needs schema
- S3.3/S3.4 sequential: forces depends on canvas writing first
- S3.5 after S3.2: session reads from persistence
- S3.6 last: validates everything works without ontology

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
