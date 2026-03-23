# Problem Brief: Test & Quality Hardening

## Problem Statement

Kokoro has 263 tests across 12 test files, all passing. But the tests have
systematic weaknesses that allow regressions to slip through undetected:

1. **Anti-pattern assertions use OR logic.** A test like `has_generic or
   has_features or has_competing` (test_forces.py:105) passes if *any one*
   anti-pattern is present. An LLM regeneration that silently drops two of three
   anti-patterns still passes. The test claims to validate "anti-pattern
   warnings" but actually validates "at least one string exists."

2. **No anti-vocabulary coverage.** Tests verify Eduardo's voice is present
   (invitado, creacion, inversion) but never verify prohibited words are absent.
   A skill file containing "cliente", "producto", "precio", "gratis", or
   "descuento" would pass all tests. Eduardo's voice is defined by what it
   includes AND what it excludes — we only test half.

3. **Conftest fixtures are orphaned.** `conftest.py` defines `extension_path`,
   `knowledge_path`, and `commands_path` fixtures, but 10 of 12 test files
   ignore them and define their own `EXTENSION_DIR` module-level constant. Only
   `test_knowledge.py` and `test_knowledge_phase2.py` use the shared fixtures.
   This creates maintenance drift — a path change requires editing 10 files
   instead of 1.

4. **No automated skill output testing.** All tests validate file *content*
   (structural assertions on markdown). None test that a skill, when invoked by
   Claude Code, produces coherent output. Content correctness is necessary but
   not sufficient — a skill could have correct content but broken prompt
   structure that confuses the LLM at runtime.

## Who Has This Problem

- **Rai** (builder): Weak assertions create false confidence. QR catches issues
  that tests should catch automatically. As the skill count grows (Phase 3 adds
  4 more skills, Phase 4 adds 4 more), manual QR review does not scale.
- **Luna** (product owner): Regressions in Eduardo's voice or methodology
  accuracy would damage user trust. The test suite should be the first line of
  defense, not QR review.

## Evidence

- **S2.3 QR finding:** Caught weak assertions propagated from S2.2 — Eduardo
  voice threshold was `>= 2` when it should have been `>= 3`. Anti-pattern
  assertions used OR. Both were PAT-L-012 violations (weak assertions pass tests
  but fail semantic intent). Fixed before S2.3 close but the pattern exists in
  all E1 skill tests too.
- **S2.3 retrospective:** "QR caught 2 weak assertions (PAT-L-012) — fixed
  before close." Explicitly notes the OR problem should be addressed.
- **S2.5 retrospective:** "All QR learnings (PAT-L-008, PAT-L-012) applied from
  T1" — confirms the pattern was recognized but only applied forward, not
  backported to E1/early-E2 tests.
- **E2 retrospective:** PAT-L-012 reinforced 3 times across the epic. Parking
  lot items created for anti-vocabulary (P1), assertion hardening (P2), and
  conftest standardization (P3).
- **Parking lot:** 4 items explicitly queued — anti-vocabulary tests (P1),
  anti-pattern assertion hardening (P2), conftest fixture standardization (P3),
  automated skill output testing (P2).

## What This Is NOT

- **Not rewriting the test suite.** The structural content TDD pattern
  (PAT-L-001, PAT-L-006) is proven and stays. This epic strengthens assertions
  within that pattern.
- **Not changing TDD workflow.** RED-GREEN-REFACTOR remains the standard. This
  epic adds new RED tests for gaps, then makes them GREEN.
- **Not testing AI quality.** We are not evaluating whether Claude gives "good"
  coaching. We are testing that skill files have the structural properties that
  make good coaching possible.
- **Not a refactoring epic.** Conftest standardization is the only refactoring
  item. The rest is new test coverage.

## Success Criteria

1. **Anti-vocabulary gate:** Every skill test file has a `test_no_prohibited_vocabulary`
   that asserts none of [cliente, producto, precio, gratis, descuento] appear in
   the skill content. Failure on any one word fails the test.
2. **Anti-pattern threshold:** Anti-pattern assertions require `>= 2` of N
   candidates (not OR). Applied to all 8 skill test files (E1 + E2).
3. **Conftest consolidation:** Zero test files define their own `EXTENSION_DIR`.
   All use `extension_path` (or derived fixtures) from `conftest.py`. One path
   change propagates everywhere.
4. **Skill output smoke tests:** At least one test per skill that invokes the
   skill's prompt structure and validates the output contains expected sections.
   Mechanism TBD (may use a mock or snapshot approach).
5. **Zero regressions:** All 263 existing tests continue to pass after hardening.
6. **QR delta:** Post-E4 QR reviews should find zero assertion-weakness issues
   (PAT-L-012 should not trigger on hardened tests).

## Risks & Unknowns

1. **Automated output testing is the hardest item.** Skill files are markdown
   prompts — testing their "output" means either (a) invoking Claude and
   asserting on the response (expensive, non-deterministic, requires API key in
   CI), or (b) validating prompt structure heuristically (cheaper but less
   meaningful). The right approach needs a design spike.
2. **Anti-vocabulary may have false positives.** If a skill legitimately uses
   "cliente" in an anti-pattern warning context (e.g., "NO uses la palabra
   'cliente'"), the naive substring check would fail. Need context-aware
   exclusion or a different matching strategy.
3. **Backporting to E1 tests may surface latent failures.** Tightening
   assertions on E1 skill files (mountain, diagnose, prune, finance) could
   reveal that those files actually lack anti-patterns they should have. This is
   a feature, not a bug, but it means E4 may include content fixes alongside
   test fixes.
4. **Conftest migration is low-risk but tedious.** Changing 10 files from
   module constants to fixtures requires updating every test method signature.
   Mechanical but easy to introduce typos.

## Dependencies

- **No blocking dependencies.** E4 can run in parallel with E3 (Germinar) if
  needed. E4 touches test files; E3 creates new skill + test files. The only
  overlap would be if E3 creates tests with the old OR pattern — avoidable by
  landing E4 first or by applying E4 patterns in E3's T1 template.
- **Recommended sequencing:** E4 before E3. Hardened test patterns become the
  template for Phase 3 skills, preventing debt from accumulating again.
- **External dependency for output testing:** If approach (a) is chosen (live
  Claude invocation), requires API key configuration in CI. If approach (b)
  (heuristic validation), no external dependencies.

## Estimated Complexity

**Size: M** (Medium)

Rationale:
- 3 of 4 items are mechanical (anti-vocabulary, assertion hardening, conftest).
  Well-understood patterns, low design risk, high file count but repetitive.
- 1 item (automated output testing) requires a design spike to determine
  approach. This is the M-driver — without it, the epic would be S.
- Estimated 4 stories: one per item, or group the mechanical items into 2
  stories + 1 design spike + 1 implementation for output testing.
- Estimated effort: 3-4 hours total (based on E2 velocity of 1.24x on proven
  patterns, and the mechanical nature of most changes).
