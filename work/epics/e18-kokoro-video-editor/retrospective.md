# Epic Retrospective: E18 — Kokoro Video Editor

**Completed:** 2026-03-30
**Duration:** 3 days (started 2026-03-28)
**Stories:** 5 delivered, 1 descoped (S18.6 — e2e validated incrementally)

---

## Summary

Delivered a complete video editing pipeline for Eduardo: from raw video to publishable shorts with captions and final renders. The pipeline chains 5 skills (`kokoro-listen` -> `kokoro-cuts` -> `kokoro-shorts` -> `kokoro-overlay` -> `kokoro-render`) using ffmpeg exclusively — no proprietary tools. S18.6 (formal e2e test) was descoped because each story was validated with real video during implementation.

## Metrics

| Metric | Value | Notes |
|--------|-------|-------|
| Stories Delivered | 5 | S18.1-S18.5 |
| Stories Descoped | 1 | S18.6 — e2e validated incrementally |
| Commits | 21 | feat/fix/test commits |
| Tests at Close | 586 | All passing |
| Calendar Days | 3 | 2026-03-28 to 2026-03-30 |
| Pipeline Cost | ~$0.04 USD | Per video (Whisper transcription) |

### Story Breakdown

| Story | Size | Est. min | Actual min | Velocity | Key Learning |
|-------|:----:|:--------:|:----------:|:--------:|--------------|
| S18.1 — Evaluar OpenShorts | S | 12 | ~10 | 1.2x | Eval-first saved us from a bad dependency |
| S18.2 — /kokoro-cuts | M | 120 | 75 | 1.6x | LLM-native skills don't need code, just good prompts |
| S18.3 — /kokoro-shorts | M | — | — | — | ffmpeg timestamp math is tricky (HH:MM:SS vs seconds) |
| S18.4 — /kokoro-overlay | M | 60 | 45 | 1.3x | drawtext filter + knowledge doc pattern works well |
| S18.5 — /kokoro-render | M | 60 | 40 | 1.5x | loudnorm two-pass is essential for audio consistency |

## What Went Well

- **Risk-first sequencing worked.** Evaluating OpenShorts first (S18.1) confirmed the INSPIRATION-ONLY verdict in 10 minutes, avoiding a potentially wasted integration effort.
- **Real video validation from S18.3 onward.** Every story was tested with Eduardo's actual footage, making S18.6 redundant.
- **ffmpeg-only architecture decision (AD-2) was correct.** Zero external dependencies beyond ffmpeg. Portable, predictable, no licensing issues.
- **Knowledge docs pattern.** Pairing each skill with a `knowledge/` doc (ffmpeg commands, drawtext syntax) made implementation faster and the skills self-documenting.
- **Phase 1/Phase 2 split (AD-5) delivered value early.** Shorts were extractable after S18.3, captions added polish in Phase 2.

## What Could Be Improved

- **S18.2 checkbox sync.** The scope doc had S18.2 unchecked despite being complete — caught only at epic close. Scope doc updates should happen atomically in story-close.
- **Vertical format not default.** M1 milestone noted that shorts came out horizontal. Reformat to 9:16 should have been the default from the start, not an option.
- **No story retrospectives as separate files for S18.1.** S18.1 retro had a different format than S18.2-S18.5. Minor inconsistency.

## Patterns Discovered

| ID | Pattern | Context |
|----|---------|---------|
| PAT-L-012 | QR catches assertion weakness that GREEN phase misses | Applied in S18.4, S18.5 |
| PAT-L-015 | List comprehensions avoid pyright reportUnknownMemberType | Applied in S18.3 |
| NEW | Knowledge doc per skill: pair `.md` skill with `knowledge/*.md` for domain-specific commands | ffmpeg skills |
| NEW | LLM-native skills (no code, just prompt) are viable for analysis tasks | S18.2 /kokoro-cuts |
| NEW | Two-pass loudnorm (-16 LUFS) is the correct approach for audio normalization | S18.5 /kokoro-render |

## Process Insights

- **Descoping is healthy.** S18.6 was descoped without loss because incremental validation covered its intent. Formal e2e is valuable when stories are tested in isolation — not when each builds on real output from the previous.
- **Skill-per-story works for pipeline epics.** Each story = one skill = one pipeline stage. Clean boundaries, clear done criteria.
- **Phase splits reduce risk.** Delivering Phase 1 (cuts + shorts) before Phase 2 (overlay + render) meant Eduardo had usable output midway through the epic.

## Artifacts

- **Scope:** `work/epics/e18-kokoro-video-editor/scope.md`
- **Stories:** `work/epics/e18-kokoro-video-editor/stories/`
- **Skills delivered:** `/kokoro-cuts`, `/kokoro-shorts`, `/kokoro-overlay`, `/kokoro-render`
- **Knowledge docs:** `knowledge/ffmpeg-overlay-captions.md`, `knowledge/ffmpeg-render.md`
- **Evaluation:** `work/epics/e18-kokoro-video-editor/stories/s18.1-openshorts-evaluation.md`
- **Tests:** 586 total (all passing)

## Next Steps

- Pipeline is ready for production use with Eduardo's workshop videos
- Consider a future epic for: batch processing, auto-upload to platforms, B-roll integration
- Vertical reformat should be revisited as default behavior in `/kokoro-shorts`
