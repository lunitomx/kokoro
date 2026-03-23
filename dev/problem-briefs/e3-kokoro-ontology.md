# Problem Brief: Kokoro Ontology + Neurosymbolic Memory

## Problem Statement

Kokoro currently operates as 10 standalone markdown skill files (8 Phase 1, 4 Phase 2, plus 2 meta-skills) connected only by text-based `/kokoro-X` cross-references. Each skill produces rich coaching output — Lean Canvas, Customer Forces, interview guides, validation plans — but none of this output persists between conversations. When an entrepreneur returns to Kokoro after completing `/kokoro-canvas`, the system has zero memory of what segments were identified, what PUV was articulated, or what forces were mapped. The entrepreneur must re-explain their entire context, and Kokoro cannot verify consistency between what `/kokoro-forces` produced and what `/kokoro-interviews` should validate.

Without a formal ontology, the methodology's domain concepts (Segmento, Problema, PUV, Fuerza, Hipotesis, Experimento) exist only as prose inside skill files. There is no structured representation that Kokoro can reason over, no graph that encodes the relationships Eduardo teaches (a Segmento alimenta a Problema, a Fuerza valida a PUV, an Experimento mide a Hipotesis). As Emilio observed in the SES-008 retrospective: without ontology and neurosymbolic memory, agents cannot be reliable. Skills remain isolated text generators instead of processes over a coherent coaching knowledge structure.

## Who Has This Problem

- **The entrepreneur using Kokoro** — loses all coaching context between sessions, must repeat themselves, gets inconsistent guidance because skills cannot see each other's outputs
- **Eduardo as methodology owner** — his 4-phase process has explicit dependencies (Forces validate Canvas, Interviews validate Forces, Experiments test Hypotheses) that the system cannot enforce
- **Rai as builder** — adding Phase 3/4 skills (8 more) will make the cross-reference problem exponential; the `/kokoro-session` routing logic is already a hardcoded conditional chain that does not scale

## Evidence

**From E1 (Phase 1 delivery):**
- `/kokoro-session` was built with hardcoded phase-tracking logic because there was no structured state to query
- `/kokoro` router uses a decision tree of "if no clarity -> diagnose, if no vision -> mountain" — pattern matching on human-described symptoms instead of querying actual coaching state

**From E2 (Phase 2 delivery):**
- S2.6 (Meta Skills Update) required manually updating `/kokoro-session` and `/kokoro` to route to 4 new skills — each new skill adds O(n) maintenance to meta-skills (PAT-L-013: meta-skills that reference other skills by name create maintenance coupling)
- Cross-references between skills are string literals: `/kokoro-forces` says "Usa `/kokoro-interviews` para validar estas fuerzas" and `/kokoro-validate` says "Usa `/kokoro-interviews` para ejecutar entrevistas de problema" — but nothing validates these references exist or are correct
- E2 retro identified skill cross-reference validation as P1 parking lot item precisely because broken links are silent
- The entrepreneur's coaching artifacts (canvas outputs, force maps, interview findings) vanish when the conversation ends — Phase 2 skills cannot build on Phase 1 outputs

**From E2 retrospective + Emilio retro (SES-008):**
- Parking lot item explicitly states: "Without ontology, skills are isolated text. With it, Kokoro becomes a coherent coaching system with memory."
- Rated P0 — highest priority, foundational for E3

## What This Is NOT

- **Not a general-purpose knowledge graph engine.** This is a domain-specific ontology for Eduardo's coaching methodology — 6-8 node types, 4-5 edge types, bounded and well-defined.
- **Not a vector/RAG system.** Neurosymbolic means structured symbolic nodes with typed edges, not embeddings. Deterministic retrieval, not probabilistic similarity.
- **Not a rewrite of existing skills.** Skills remain markdown files. The ontology sits underneath them as a queryable structure they can read from and write to.
- **Not Phase 3 skill implementation.** Phase 3 skills (research, pescar, experiment, launch) are a separate epic. This epic provides the foundation they will use.
- **Not full session replay or conversation logging.** Persistent memory means coaching state (decisions made, artifacts produced, phase progress), not conversation transcripts.

## Success Criteria

1. **Ontology schema exists and is testable** — node types (Segmento, Problema, PUV, Fuerza, Hipotesis, Experimento) and edge types (alimenta, valida, experimenta, mide) are defined as Pydantic models with validation
2. **Skills can write to the ontology** — at minimum, `/kokoro-canvas` output can be persisted as structured nodes (Segmento, Problema, PUV) connected by typed edges
3. **Skills can read from the ontology** — `/kokoro-forces` can retrieve the canvas output for the active segment without the entrepreneur re-explaining it
4. **Cross-reference validation passes** — all `/kokoro-X` references in skill files resolve to skills that actually exist, tested in CI
5. **Session continuity works** — an entrepreneur can close a conversation after `/kokoro-canvas`, return in a new conversation, and `/kokoro-session` correctly identifies their progress and pending next steps from persisted state
6. **Anti-vocabulary and voice integrity preserved** — ontology layer does not introduce any prohibited vocabulary (cliente, producto, precio, gratis, descuento) into skill outputs

## Risks & Unknowns

- **Storage mechanism undefined.** Where does the ontology persist between conversations? Options: local JSON/YAML file in the entrepreneur's project, SQLite, or the RaiSE symbolic memory adapter. Decision needed during epic design.
- **Skill output parsing.** Current skill outputs are free-form markdown generated by the LLM. Extracting structured nodes from unstructured output is non-trivial. May require output format conventions or post-processing.
- **Ontology granularity.** Too coarse (just phase completion flags) gives no real value. Too fine (every sentence becomes a node) creates noise. The right granularity for Eduardo's methodology needs discovery during design.
- **RaiSE adapter portability.** The parking lot mentions "RaiSE symbolic memory adapter can port to this ontology." Unclear how much of the RaiSE adapter is reusable vs. Kokoro-specific. Requires investigation.
- **Backward compatibility.** Existing Phase 1/2 skills must continue working without the ontology (graceful degradation). Cannot break the 263 existing tests.
- **Scope creep toward Phase 3.** This epic provides infrastructure. The temptation to also build Phase 3 skills "since the ontology is ready" must be resisted.

## Dependencies

- **E2 complete and merged** — Phase 2 skills must be stable (all 263 tests passing, pyright/ruff clean). Currently on `story/s2.2/kokoro-canvas` branch; E2 merge to main must complete first.
- **Eduardo's methodology domain validated** — the node types and edge types must be reviewed with Eduardo (or from his materials) to ensure they faithfully represent his coaching process, not our interpretation of it.
- **Storage decision** — local file vs. database vs. RaiSE adapter must be decided before implementation begins, as it affects the entire persistence layer.

## Estimated Complexity

**L (Large)** — Rationale:
- New architectural layer (ontology + persistence) that did not exist before
- Touches all existing skills (read/write integration) though can be done incrementally
- Requires domain modeling (methodology concepts, not just code)
- Cross-reference validation is S by itself but becomes part of the ontology story
- Persistent memory requires a storage mechanism decision and implementation
- Estimated 4-6 stories, likely spanning 2-3 sessions
- Comparable in scope to E1 (which delivered 8 skills + packaging) but more architecturally complex because it adds a layer under existing code rather than beside it
