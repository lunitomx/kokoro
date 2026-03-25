# Epic E4: Test & Quality Hardening — Scope

> **Status:** DONE
> **Created:** 2026-03-22
> **Problem Brief:** `dev/problem-briefs/e4-test-hardening.md`

## Objective

Harden the Kokoro test suite to catch regressions that currently slip through:
prohibited vocabulary, weak assertions, inconsistent fixtures, and untested
prompt structure. After E4, the test suite is the first line of defense — not
QR review.

**Value:** Hardened patterns become the template for E5 (Phase 3) and E6
(Phase 4), preventing debt from accumulating as the skill count grows from
10 to 16+.

## Stories

| ID | Story | Size | Status | Description |
|----|-------|:----:|:------:|-------------|
| S4.1 | Conftest Consolidation | S | Done | Migrate 10 test files from EXTENSION_DIR to conftest fixtures |
| S4.2 | Anti-Vocabulary Gate | S | Done | Add prohibited word tests to all 10 skill test files |
| S4.3 | Assertion Hardening | S | Done | Backport strong assertions to E1 tests, fix content gaps |
| S4.4 | Output Testing Spike | S | Done | Design + proof-of-concept for skill output smoke tests |

**Total:** 4 stories

## Scope

**In scope (MUST):**
- Conftest fixture consolidation: zero EXTENSION_DIR in test files
- Anti-vocabulary tests: [cliente, producto, precio, gratis, descuento] absent
- Assertion hardening: Eduardo voice >= 3, anti-patterns >= 2 of N, summary >= 4 rows
- Backport to ALL skill test files (E1 + E2)
- Zero regressions in existing 263 tests

**In scope (SHOULD):**
- Output testing proof-of-concept (1 skill minimum)
- Content fixes in E1 skill files if assertions reveal gaps

**Out of scope:**
- Live Claude invocation in CI (too expensive, non-deterministic)
- Rewriting test structure (PAT-L-001/PAT-L-006 stays)
- New skill files (that's E5/E6)
- Ontology work (that's E3)

## Done Criteria

**Per story:**
- [ ] Tests pass (pyright, ruff, pytest)
- [ ] Commit after each task

**Epic complete:**
- [ ] All 4 stories complete
- [ ] Zero test files with EXTENSION_DIR module constant
- [ ] All 10 skill test files have anti-vocabulary test
- [ ] All assertion weaknesses from E2 QR backported to E1
- [ ] Output testing approach documented + 1 PoC test
- [ ] >= 263 tests pass (count will grow)
- [ ] Epic retrospective done

## Dependencies

```
S4.1 (conftest) ──→ S4.2 (anti-vocab) ──→ S4.3 (hardening)
                                            S4.4 (spike, independent)
```

- S4.1 first: fixture changes must be stable before adding new assertions
- S4.2/S4.3 after S4.1, can be parallel but sequential is safer (10 files)
- S4.4 independent: design spike doesn't touch existing test files

**External:** None. Can run in parallel with E3 if needed.

## Risks

| Risk | L/I | Mitigation |
|------|:---:|------------|
| Anti-vocabulary false positives in anti-pattern text | M/M | Context-aware check: skip lines containing "no uses" or "nunca digas" |
| E1 skill files may lack content that hardened tests require | M/L | Fix content in same story — this is a feature, not a bug |
| Conftest migration introduces typos across 10 files | L/M | Run full suite after each file migration, commit incrementally |
| Output testing PoC may be inconclusive | L/L | Timeboxed spike — if inconclusive, document learnings and defer |

## Architecture

No new architecture. All changes are within the existing test infrastructure.

**Key decision:** Anti-vocabulary check will use line-level exclusion — skip
lines that contain anti-pattern markers (e.g., "nunca digas", "no uses") to
avoid false positives when skills legitimately quote prohibited words in
warnings.

## Implementation Plan

> Added by `/rai-epic-plan` — 2026-03-23

### Story Sequence

| Order | Story | Size | Dependencies | Rationale |
|:-----:|-------|:----:|-------------|-----------|
| 1 | S4.1 Conftest Consolidation | S | None | Dependency-driven: fixture changes must be stable before other stories touch test files |
| 2 | S4.2 Anti-Vocabulary Gate | S | S4.1 | Quick win: new test per file, catches voice violations immediately |
| 3 | S4.3 Assertion Hardening | S | S4.1 | Risk-first: backporting to E1 may surface content gaps in skill files |
| 4 | S4.4 Output Testing Spike | S | None (soft: S4.1-S4.3) | Spike last: benefits from all hardening being complete for comparison |

### Critical Path

```
S4.1 → S4.2 → S4.3 → S4.4
```

Strictly sequential — all stories touch the same 10 test files.

### Milestones

| Milestone | Stories | Success Criteria |
|-----------|---------|------------------|
| **M1: Foundation** | S4.1 | Zero EXTENSION_DIR in test files, all 263 tests pass via conftest fixtures |
| **M2: Voice Protection** | +S4.2, S4.3 | Anti-vocabulary + hardened assertions on all 10 skill test files, E1 content gaps fixed |
| **M3: Epic Complete** | +S4.4 | Output testing PoC documented, retrospective done |

### Progress Tracking

| Story | Size | Status | Actual | Notes |
|-------|:----:|:------:|:------:|-------|
| S4.1 Conftest Consolidation | S | Done | S | 10 files migrated, 1.33x velocity |
| S4.2 Anti-Vocabulary Gate | S | Done | S | 10 tests, 9 content fixes, 1.12x |
| S4.3 Assertion Hardening | S | Done | S | 12 assertions hardened, 3 skill fixes, 1.33x |
| S4.4 Output Testing Spike | S | Done | S | 40 tests, 1 content fix, viable |

### Sequencing Risks

| Risk | L/I | Mitigation |
|------|:---:|------------|
| Conftest migration breaks test discovery | L/M | Migrate one file at a time, run suite after each |
| S4.3 backport reveals many E1 content gaps | M/L | Fix in-story — content fixes are a feature, scope is flexible |
| S4.4 spike inconclusive | L/L | Timebox to 1 hour, document learnings regardless of outcome |
