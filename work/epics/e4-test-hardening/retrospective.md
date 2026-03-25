# Epic E4 Retrospective: Test & Quality Hardening

> **Epic:** E4 | **Stories:** 4 | **Sessions:** SES-011, SES-012
> **Started:** 2026-03-22 | **Completed:** 2026-03-24

## Deliverables

- Conftest fixtures replacing EXTENSION_DIR across all 10 test files
- Anti-vocabulary gate (vocabulary_check.py) with context-aware exclusions
- Hardened assertions across E1+E2 test files (Eduardo voice, anti-patterns, summaries)
- Output template structure tests (40 parametrized tests)
- 1 content fix in kokoro-mountain (missing Siguiente paso)
- 313 total tests (up from 263 at E4 start — +50 tests)

## Metrics

| Metric | Planned | Actual |
|--------|---------|--------|
| Stories | 4 | 4 |
| Story sizes | 4S | 4S |
| Tests added | ~30 est | 50 |
| Content fixes | ~5 est | 13 (9 vocab + 3 assertions + 1 output) |
| Test baseline | 263 | 313 |
| Velocity | 1.0x | ~1.25x avg |

## Done Criteria Verification

- [x] All 4 stories complete
- [x] Zero test files with EXTENSION_DIR module constant
- [x] All 10 skill test files have anti-vocabulary test
- [x] All assertion weaknesses from E2 QR backported to E1
- [x] Output testing approach documented + 40 PoC tests (target was 1)
- [x] >= 263 tests pass → 313 pass
- [x] Epic retrospective done (this document)

## Milestones

| Milestone | Status | Achieved |
|-----------|--------|----------|
| M1: Foundation | ACHIEVED | S4.1 — zero EXTENSION_DIR |
| M2: Voice Protection | ACHIEVED | S4.2 + S4.3 — vocab gate + hardened assertions |
| M3: Epic Complete | ACHIEVED | S4.4 — output testing viable |

## What Went Well

1. **All 4S stories delivered at or above estimate** — the S sizing was
   accurate, and the sequential dependency chain worked cleanly
2. **13 content fixes surfaced by tests** — the hardened test suite found
   real gaps in skill files. Tests are now the first line of defense
3. **Output testing spike was conclusive** — viable approach, easy to scale,
   caught a real gap in kokoro-mountain
4. **vocabulary_check.py is reusable** — context-aware exclusion pattern
   works for any new skill file

## What Could Improve

1. **E1/E2 scope files weren't updated to DONE** — had to fix as housekeeping
   in SES-012. Epic close should update scope status automatically
2. **Backlog was stale** — only tracked E1/E2, not E3-E6. Now fixed

## Patterns Discovered

- **Output template as contract (BASE-050 extension)** — code blocks in
  skill files are the output specification. Testing them tests the contract
- **Longest-block heuristic** — when skills have multiple code blocks, the
  longest is the output template. Works for 8/8 skills but fragile

## Impact on E5/E6

The test infrastructure is now templated for new skills:
1. Copy any existing test file as starter
2. Conftest provides extension_path, knowledge_path, commands_path
3. vocabulary_check.py provides anti-vocab gate
4. test_output_structure.py auto-covers new skills added to COACHING_SKILLS list

This reduces per-skill test setup from ~30 min to ~5 min.
