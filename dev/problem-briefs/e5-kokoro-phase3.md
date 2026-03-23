# Problem Brief: Kokoro Phase 3 — Germinar

## Problem Statement

After Phase 2, the entrepreneur has a validated Lean Canvas, understood their Customer Forces, conducted validation interviews, and built an experiment plan. They know WHAT to build and for WHOM. But they are staring at a gap: how do they go from validated model to market presence? Research, content, landing pages, launch strategy — the transition from "I know this could work" to "people can find and choose this" is where most validated ideas die quietly.

Phase 2 ends with `/kokoro-validate` producing an experiment plan. Phase 3 picks up exactly there: execute the research, create the content, run the experiments, and launch. Without Phase 3, the entrepreneur has a beautiful map and no vehicle.

## Who Has This Problem

Entrepreneurs who have completed Phases 1-2 with Kokoro. They have:
- Strategic alignment (Phase 1: pruned products, clear vision, financial reality)
- Validated model (Phase 2: canvas, forces, interviews, validation plan)

They do NOT have:
- Market research beyond their interview sample
- Content that communicates their value proposition
- A launch strategy connecting their validated model to real channels
- A systematic experimentation framework (3x3x3) to test what works

These are people who know their "semilla" is viable but don't know how to make it germinate in real soil.

## Evidence

1. **Phase 2 ends at planning, not execution.** `/kokoro-validate` produces a validation plan and experiment design — but no tool guides the actual research, content creation, or launch execution.
2. **The methodology defines 4 phases explicitly.** Eduardo's curriculum (02_Modulo_Semilla through the full arc) treats Germinar as the critical bridge between validation and growth. Skipping it leaves the coaching arc incomplete.
3. **Parking lot accumulation.** Three P2 items from SES-007 and E2 retro converge on Phase 3: the core skills, web quality diagnostics, and video/creative analysis. The demand signal is clear.
4. **E2 velocity data supports continuation.** All 6 E2 stories delivered at or above estimated velocity (1.13x-1.38x), with the PAT-L-001 skill pattern proven across 9 skills total. The pattern is mature enough to scale to Phase 3.

## What This Is NOT

- **Not execution-for-hire.** Kokoro coaches the process of researching, creating content, and launching. It does NOT write the entrepreneur's copy, build their landing page, or run their ads. Eduardo guides — the entrepreneur does the work.
- **Not a marketing automation tool.** No API integrations, no scheduled posts, no analytics dashboards. Kokoro produces markdown guidance that the entrepreneur applies.
- **Not a replacement for domain expertise.** `/kokoro-research` guides multi-source research methodology, not AI-generated market reports. `/kokoro-launch` produces copy frameworks and scripts, not finished campaigns.
- **Not a web development tool.** Even with potential web quality diagnostics, the output is a coaching report ("here's what to improve"), not automated fixes.

## Success Criteria

1. **4 Phase 3 skills delivered:** `/kokoro-research`, `/kokoro-pescar`, `/kokoro-experiment`, `/kokoro-launch` — all following PAT-L-001, with Eduardo's voice, tested via structural content validation (PAT-L-006).
2. **Complete coaching arc from validate to launch:** An entrepreneur can flow from `/kokoro-validate` output through Phase 3 skills sequentially, each skill building on the previous.
3. **Anti-vocabulary enforcement:** No prohibited words (cliente, producto, precio, gratis, descuento) in any skill file. Test coverage from T1 of each skill (parking lot item, P1).
4. **Skill cross-reference integrity:** All `/kokoro-X` references in skill files resolve to existing skills. No broken links (parking lot item, P1).
5. **Meta skills updated:** `/kokoro` router and `/kokoro-session` aware of Phase 3 position and progress.
6. **Tests passing:** All quality gates (pyright strict, ruff, pytest) green before every commit.

## Risks & Unknowns

| Risk | L/I | Notes |
|------|:---:|-------|
| **Ontology dependency (P0 blocker)** | H/H | Parking lot item marks ontology + neurosymbolic memory as P0, "Before E3 — foundational." Without it, Phase 3 skills remain isolated text like Phases 1-2. Decision needed: does E3 (ontology) gate E5, or do we proceed and retrofit? |
| **PESCAR methodology complexity** | M/M | PESCAR is a multi-step framework (Problema-Estrategia-Segmento-Contenido-Acción-Resultado). Richest skill in Phase 3, similar risk profile to S2.2 (Lean Canvas). Source material quality unknown — needs assessment. |
| **Web quality skills add technical surface area** | M/H | Addy Osmani's web-quality-skills means Kokoro would need to parse Lighthouse/PageSpeed data or guide manual checks. This is a different kind of skill — diagnostic rather than coaching. May not fit PAT-L-001. |
| **Video/creative pipeline is infrastructure, not coaching** | M/H | ffmpeg + Whisper + Andromeda framework requires binary dependencies, processing pipelines, and media handling. This is a significant departure from markdown skill files. |
| **Content creation guidance vs. content generation** | L/M | `/kokoro-launch` must guide copy/script creation without becoming a generic copywriting tool. Eduardo's voice must permeate the framework, not just the instructions. |
| **Phase 3 source material depth unknown** | L/M | E1 and E2 had rich source material (01_Modulo_Suelo, 02_Modulo_Semilla). Need to verify equivalent depth exists for Phase 3 methodology. |

## Dependencies

### Hard Dependencies
- **E2 complete and merged to main** — Phase 3 skills reference Phase 2 outputs (canvas, forces, validation plan). E2 is nearly complete (all stories done, pending close/merge).

### Decision Required: Ontology (E3/E4)
The parking lot marks "Kokoro ontology + neurosymbolic memory" as **P0, before E3**. This creates a sequencing question:

- **Option A: Ontology first (E3), then Germinar (E5).** Skills become processes over a knowledge graph. Cross-references are structural, not string-based. Memory persists across sessions. Higher ceiling, higher upfront cost.
- **Option B: Germinar first (E5), retrofit ontology later.** Delivers coaching value sooner. Follows the same proven pattern from E1/E2. Risk: rework when ontology lands.
- **Option C: Interleave.** Lightweight ontology schema (E3) first, then Germinar skills reference it. Full neurosymbolic memory deferred.

This decision should be made during `/rai-epic-design` for E5, informed by the ontology problem brief (if one exists for E3/E4).

### Parking Lot Items Absorbed (P1, mandatory)
- Skill cross-reference validation — add to test infrastructure in first story
- Anti-vocabulary tests — add to test template, apply from T1 of each skill

### Parking Lot Items Absorbed (P2, should-have)
- Anti-pattern assertion hardening (>= 2 of N) — apply to new skills, backport if time

## Optional Additions (May Be Separate Stories or Deferred)

Two parking lot items fit thematically with Phase 3 but add significant technical complexity beyond the established markdown skill pattern:

### Web Quality Skills (P2)
- **What:** Site health diagnostics based on Addy Osmani's web-quality-skills. Coaching the entrepreneur to assess their web presence.
- **Fit:** Complements `/kokoro-research` (research includes web presence assessment) and `/kokoro-launch` (launch readiness includes site quality).
- **Risk:** Requires either MCP tool integration or structured manual-check guidance. Different skill shape than PAT-L-001.
- **Recommendation:** Scope as 1-2 optional stories within E5, or defer to a separate mini-epic. Decision during `/rai-epic-design`.

### Video/Creative Analysis Pipeline (P2)
- **What:** ffmpeg frame extraction + Whisper transcription + Andromeda 4-signal framework for analyzing creative content.
- **Fit:** Complements `/kokoro-pescar` (analyzing existing content for PESCAR methodology) and `/kokoro-launch` (evaluating launch creative).
- **Risk:** Binary dependencies (ffmpeg, Whisper), media file handling, processing pipelines. This is infrastructure, not coaching content. Highest technical complexity of any Kokoro work to date.
- **Recommendation:** Defer to a separate technical epic or spike. The coaching skills should not be gated on pipeline infrastructure.

## Estimated Complexity

**L (Large)** — 4 core skills + test infrastructure improvements + meta skills update.

Rationale:
- E2 was 6 stories (S-M sized), delivered in ~2 weeks with proven patterns. E5 core is similar: 4 skills + knowledge files + meta update = ~6 stories.
- However, PESCAR and launch skills are likely M-L individually (richer methodology, more output structure).
- Adding P1 test infrastructure items (cross-ref validation, anti-vocabulary) increases first-story scope.
- If web quality or video pipeline are included, complexity jumps to **XL**. Recommend keeping them optional/deferred to maintain L sizing.

**Without optional additions:** L (6-8 stories, ~2-3 weeks at E2 velocity)
**With optional additions:** XL (10-12 stories, ~4-5 weeks, mixed technical complexity)
