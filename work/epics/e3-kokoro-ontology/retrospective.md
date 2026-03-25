# Epic E3 Retrospective: Kokoro Ontology + Neurosymbolic Memory

> **Epic:** E3 | **Stories:** 6 | **Session:** SES-012
> **Started:** 2026-03-24 | **Completed:** 2026-03-24

## Deliverables

- `src/kokoro/ontology/models.py` — 10 node types, 5 edge types, CoachingState
- `src/kokoro/ontology/store.py` — JSON persistence with atomic writes
- All 8 coaching skills updated with Persistencia + context loading sections
- 2 meta-skills (session, router) read progress from state.json
- `kokoro init` creates `.kokoro/` directory
- 52 new tests (23 schema + 19 store + 10 compat)
- ADR-001: Coaching state persistence mechanism
- pydantic>=2.0 added as project dependency

## Metrics

| Metric | Planned | Actual |
|--------|---------|--------|
| Stories | 6 | 6 |
| Story sizes | 2M + 2M + 2S | All ≤S actual |
| Tests added | ~40 est | 52 |
| Test baseline | 355 | 365 |
| Node types | >= 6 | 10 |
| Edge types | >= 4 | 5 |
| Skills integrated | 8 MUST | 8 + 2 meta |

## Done Criteria Verification

- [x] All 6 stories complete
- [x] Ontology schema with 10 node types, 5 edge types
- [x] Canvas output persists as structured nodes (segmento, problema, puv)
- [x] Forces reads canvas state via get_skill_context
- [x] Session detects progress from state.json
- [x] All 365 existing tests pass (graceful degradation verified)
- [x] Zero prohibited vocabulary in new code
- [x] Epic retrospective done (this document)

## Milestones

| Milestone | Status |
|-----------|--------|
| M1: Walking Skeleton (schema + persistence) | ACHIEVED |
| M2: Skills Connected (8 skills integrated) | ACHIEVED |
| M3: Epic Complete (session + compat) | ACHIEVED |

## What Went Well

1. **RaiSE-inspired design paid off** — JSONL/Pydantic/atomic write patterns
   from RaiSE adapted cleanly to Kokoro's domain
2. **All stories came in under estimate** — M stories were S actual. Schema
   and persistence were simpler than expected with Pydantic
3. **Graceful degradation by design** — backwards compat was trivial because
   context loading is additive (if file exists, use it)
4. **10 compat tests as safety net** — verifies all 8 skills have persistence
   sections and state.json references

## What Could Improve

1. **No end-to-end integration test** — we test store + skill files separately
   but don't have a test that runs a full canvas→forces chain. This would
   require mocking Claude's output, which is out of scope
2. **Parking lot: MCP server** — Luna identified a key distribution gap:
   students/entrepreneurs should connect via Claude Desktop without installing
   packages. Added to parking lot as P1

## Patterns

- **Instruction-based persistence** — rather than parsing LLM output, skills
  instruct Claude to write structured data. The model follows formatting
  instructions reliably. No parsing needed.
- **Graceful degradation by absence** — "if file exists, use it; if not,
  ask the user" is simpler and more robust than migration logic
