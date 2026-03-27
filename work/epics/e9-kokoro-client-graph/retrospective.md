---
epic_id: "E9"
title: "Kokoro Client Graph — Memoria neurosimbolica por cliente"
status: "complete"
closed: "2026-03-26"
---

# Epic Retrospective: E9 — Kokoro Client Graph

## Delivered
- src/kokoro/clients/ module with ClientProfile, ClientRegistry (Pydantic models)
- Atomic persistence to .kokoro/clients.json
- /kokoro-client skill with 4 operations (crear, listar, ver, buscar)
- Client resolution integrated in /kokoro-ads
- Memory sync: generate reference_*.md from client graph
- 551 tests passing

## Metrics

| Metric | Value |
|--------|-------|
| Stories | 5 (S9.1 S, S9.2 S, S9.3 M, S9.4 M, S9.5 S) |
| Tests added | 25+ new |
| Tests total | 551 |
| Python files | 4 created (models, store, sync, __init__) |
| Skill files | 2 created (kokoro-client + mirror) |
| Skills modified | 2 (kokoro-ads + mirror — client resolution) |
| Test files modified | 1 (test_output_structure.py — kokoro-client registration) |

## What Went Well
- Walking skeleton strategy worked — models + persistence first enabled all other stories
- Separate module from ontology was the right call — different domains, clean separation
- TDD across all stories caught issues early
- Client resolution in kokoro-ads is backward compatible

## What Could Improve
- Only integrated client resolution in kokoro-ads — other skills still need it
- MEMORY.md index update not automated
- No cross-client pattern detection yet (parking lot)

## Patterns Learned
- PAT-L-018: Client resolution as standard skill preamble — add before exercises, not inside
- PAT-L-019: Separate domain modules for separate concerns — coaching ontology (per-entrepreneur) vs client graph (Eduardo's brain) are different domains even though both use Pydantic

## Process Notes
- E9 originated from user question about connecting client knowledge neurosymbolically
- All 5 stories completed in one session using /rai-story-run
- The client graph connects to E3 ontology conceptually but not in code — by design
