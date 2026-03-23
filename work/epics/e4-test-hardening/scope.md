# Epic E4: Test & Quality Hardening — Scope

> **Status:** DESIGNED
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
| S4.1 | Conftest Consolidation | S | Pending | Migrate 10 test files from EXTENSION_DIR to conftest fixtures |
| S4.2 | Anti-Vocabulary Gate | S | Pending | Add prohibited word tests to all 10 skill test files |
| S4.3 | Assertion Hardening | S | Pending | Backport strong assertions to E1 tests, fix content gaps |
| S4.4 | Output Testing Spike | S | Pending | Design + proof-of-concept for skill output smoke tests |

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

## Progress Tracking

| Story | Size | Status | Actual | Notes |
|-------|:----:|:------:|:------:|-------|
| S4.1 Conftest Consolidation | S | Pending | | |
| S4.2 Anti-Vocabulary Gate | S | Pending | | |
| S4.3 Assertion Hardening | S | Pending | | |
| S4.4 Output Testing Spike | S | Pending | | |
