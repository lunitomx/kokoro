---
epic_id: "E3"
title: "Kokoro Ontology + Neurosymbolic Memory"
status: "draft"
created: "2026-03-24"
---

# Epic Brief: Kokoro Ontology + Neurosymbolic Memory

## Hypothesis
For entrepreneurs using Kokoro who lose all coaching context between sessions,
the coaching ontology is a domain-specific knowledge structure
that persists decisions, artifacts, and phase progress across conversations.
Unlike the current stateless skill files, our solution enables skills to
read prior outputs and enforce methodology dependencies.

## Success Metrics
- **Leading:** `/kokoro-canvas` output persists as structured nodes retrievable
  by `/kokoro-forces` in a new conversation
- **Lagging:** Entrepreneur can complete Phase 1-2 across multiple sessions
  without re-explaining context

## Appetite
M — 5-7 stories estimated

## Scope Boundaries
### In (MUST)
- Ontology schema: Pydantic models for domain nodes (Segmento, Problema, PUV,
  Fuerza, Hipotesis, Experimento) and typed edges
- Persistence layer: local file storage (JSON/YAML) for coaching state
- Read/write integration for at least 2 skills (canvas + forces)
- `/kokoro-session` reads from persisted state for progress tracking
- Graceful degradation: skills work without ontology (backward compat)

### In (SHOULD)
- Integration with all Phase 1/2 skills (not just canvas/forces)
- Schema validation on read/write
- Migration path for existing entrepreneurs (no state → with state)

### No-Gos
- Phase 3/4 skill implementation (separate epics E5/E6)
- Vector/RAG system — this is symbolic, not probabilistic
- Conversation logging — persist state, not transcripts
- External database dependency — must be local-first

### Rabbit Holes
- Over-engineering the graph: 6-8 node types, 4-5 edge types is sufficient.
  Don't build a general-purpose knowledge graph engine
- Trying to parse existing free-form LLM output: better to define output
  format conventions than to parse arbitrary markdown
- Building full CRUD UI for the ontology: CLI queries are enough for E3
