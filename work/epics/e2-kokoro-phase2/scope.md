# Epic E2: Kokoro Phase 2 — Elegir la Semilla — Scope

> **Status:** IN PROGRESS
> **Created:** 2026-03-09

## Objective

Extend Kokoro with Phase 2 skills that guide entrepreneurs through business model validation — Lean Canvas, Customer Forces analysis, validation interviews, and experiment planning — maintaining Eduardo's voice and the proven PAT-L-001 skill pattern.

**Value:** Entrepreneurs who completed Phase 1 (strategic alignment) can now validate their business model before building. Validates that the skill pattern scales to multi-phase delivery.

## Stories

| ID | Story | Size | Status | Description |
|----|-------|:----:|:------:|-------------|
| S2.1 | Knowledge Files Phase 2 | S | Done | Methodology references for Lean Canvas, Customer Forces, interviews, validation |
| S2.2 | /kokoro-canvas | M | Done | Lean Canvas guided session — segment-first, problem-driven |
| S2.3 | /kokoro-forces | S | Done | Customer Forces Model guided session |
| S2.4 | /kokoro-interviews | M | Done | Validation interview guide + processing methodology |
| S2.5 | /kokoro-validate | S | Done | Validation plan and experiment design |
| S2.6 | Meta Skills Update | S | Pending | Update /kokoro router + /kokoro-session for Phase 2 awareness |

**Total:** 6 stories

## Scope

**In scope (MUST):**
- 4 Phase 2 skills as .claude/commands/*.md following PAT-L-001
- Knowledge files for Phase 2 methodology embedded as package data
- Eduardo's voice (vocabulary, anti-patterns, Proyector strategy) in all skills
- TDD with structural content validation (PAT-L-006)
- Bilingual support (Spanish soul, responds in user's language)

**In scope (SHOULD):**
- conftest.py with shared test fixtures (E1 carry-forward)
- /kokoro router update for Phase 2 routing
- /kokoro-session update for Phase 2 progress tracking

**Out of scope:**
- Phases 3-4 skills (E3, E4)
- External API integrations
- Automated survey/interview tools
- Persistent user data beyond Claude Code sessions

## Done Criteria

**Per story:**
- [ ] Code with type annotations (pyright strict)
- [ ] Tests passing
- [ ] Quality checks pass (ruff, pyright)

**Epic complete:**
- [ ] All stories complete (S2.1-S2.6)
- [ ] `kokoro init` installs all Phase 2 files
- [ ] All 4 new skills discoverable and executable
- [ ] /kokoro router correctly identifies Phase 2 position
- [ ] Epic retrospective done
- [ ] Merged to `main`

## Dependencies

```
S2.1 (knowledge) ──→ S2.2 (canvas)    ─┐
                 ──→ S2.3 (forces)     ─┤
                 ──→ S2.4 (interviews) ─┤
                 ──→ S2.5 (validate)   ─┤
                                        ↓
                             S2.6 (meta update)
```

- S2.1 creates knowledge files that skills reference
- S2.2-S2.5 depend on S2.1 — **parallel** with each other
- S2.6 depends on S2.2-S2.5 (router needs skills to exist)

**External:** E1 complete (merged to main) ✓

## Architecture

| Decision | Source | Summary |
|----------|--------|---------|
| PAT-L-001 reuse | E1 | Skill file TDD pattern — proven across 5 stories |
| PAT-L-006 reuse | E1 | Structural TDD for content — tests define markers |
| PAT-L-009 reuse | E1 | kokoro- prefix convention for managed files |
| conftest.py | E1 retro | Shared test fixtures to reduce duplication |

## Risks

| Risk | L/I | Mitigation |
|------|:---:|------------|
| Phase 2 content less structured than Phase 1 | M/M | Source material (02_Modulo_Semilla) is rich and detailed |
| Interview skill too prescriptive | L/M | Guide the process, don't execute it — Eduardo coaches, doesn't interview |
| Meta skills coupling increases | L/L | PAT-L-004 established pattern, PAT-L-005 for precise string matching |

## Implementation Plan

> Added by `/rai-epic-plan` — 2026-03-09

### Story Sequence

| Order | Story | Size | Dependencies | Milestone | Rationale |
|:-----:|-------|:----:|--------------|-----------|-----------:|
| 1 | S2.1 Knowledge Files Phase 2 | S | None | M1 | Quick win: creates methodology references, unblocks all skills. Also introduces conftest.py |
| 2 | S2.2 /kokoro-canvas | M | S2.1 | M2 | Risk-first: Lean Canvas is the richest skill (9 blocks), proves Phase 2 pattern works |
| 3 | S2.3 /kokoro-forces | S | S2.1 | M2 | Methodology order: forces complement canvas, simpler structure |
| 4 | S2.4 /kokoro-interviews | M | S2.1 | M2 | Methodology order: interviews validate canvas/forces hypotheses |
| 5 | S2.5 /kokoro-validate | S | S2.1 | M3 | Methodology order: validation plan synthesizes all Phase 2 work |
| 6 | S2.6 Meta Skills Update | S | S2.2-S2.5 | M3 | Router needs all Phase 2 skills to exist |

### Critical Path

```
S2.1 → S2.2 → S2.3 → S2.4 → S2.5 → S2.6
```

S2.2-S2.5 are theoretically parallel but executed sequentially (single developer). S2.2 is risk-first: if Lean Canvas pattern works, S2.3-S2.5 follow predictably (PAT-L-002).

### Milestones

| Milestone | Stories | Success Criteria |
|-----------|---------|------------------|
| **M1: Knowledge Base** | S2.1 | Knowledge files installed, conftest.py shared fixtures, tests passing |
| **M2: Core Skills** | +S2.2, S2.3, S2.4 | 3 skills functional — Lean Canvas + Forces + Interviews flow |
| **M3: Feature Complete** | +S2.5, S2.6 | All 4 Phase 2 skills work, /kokoro routes Phase 2 correctly |
| **M4: Epic Complete** | — | Done criteria met, retrospective done, merged to main |

### Progress Tracking

| Story | Size | Status | Actual | Notes |
|-------|:----:|:------:|:------:|-------|
| S2.1 Knowledge Files Phase 2 | S | Done | S | PAT-L-008, conftest.py, QR fix |
| S2.2 /kokoro-canvas | M | Done | M | 13 tests, PAT-L-007, 1.13x velocity |
| S2.3 /kokoro-forces | S | Done | S | 16 tests, PAT-L-008, 1.22x velocity |
| S2.4 /kokoro-interviews | M | Done | M | 17 tests, PAT-L-009, 1.19x velocity |
| S2.5 /kokoro-validate | S | Done | S | 15 tests, 1.38x velocity |
| S2.6 Meta Skills Update | S | Pending | | |

### Sequencing Risks

| Risk | L/I | Mitigation |
|------|:---:|------------|
| S2.2 Lean Canvas harder than E1 skills (9 blocks vs simple flow) | M/M | Rich source material (02_Modulo_Semilla), PAT-L-001 proven pattern |
| S2.4 Interview skill scope creep (too many question types) | L/M | Eduardo coaches the process, doesn't execute interviews — keep skill focused on guide + template |
| E1 velocity calibration may not hold for Phase 2 content | L/L | Source material is equally detailed; pattern maturity offsets content complexity |
