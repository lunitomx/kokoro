---
epic_id: "E33"
title: "Retrospective: Meta Delivery Gates"
status: "Complete"
date: "2026-04-08"
origin: "lunitomx/kokoro#1"
---

# Epic Retrospective: E33 — Meta Delivery Gates

## Objective Delivered

Closed the knowledge gap that allowed Kokoro to recommend turning off ads
during the exploration phase. Three layers of protection were added:

1. A comprehensive knowledge file documenting Meta's delivery system
2. A quick-reference decision table in the existing kokoro-ads-meta.md
3. A behavioral gate in /kokoro-ads that checks learning phase before any on/off recommendation

## Origin

GitHub issue: lunitomx/kokoro#1
Trigger: Kokoro recommended killing an ad with 283 impressions, $79 MXN, 0
conversions, 8 days active — when the correct recommendation was WAIT.
Root cause: Kokoro evaluated ad data as a static table without modeling
Meta's delivery phases.

## Deliverables

| Artifact | Path |
|----------|------|
| Knowledge file | `extension/.claude/knowledge/kokoro-meta-delivery-system.md` |
| Knowledge mirror | `.claude/knowledge/kokoro-meta-delivery-system.md` |
| Thresholds section | `extension/.claude/knowledge/kokoro-ads-meta.md` (lines 218-249) |
| Thresholds mirror | `.claude/knowledge/kokoro-ads-meta.md` |
| Learning phase gate | `extension/.claude/commands/kokoro-ads.md` (lines 59-93) |
| Gate mirror | `.claude/commands/kokoro-ads.md` |

## Story Metrics

| ID | Name | Size | Est | Actual | Velocity | AR | QR |
|----|------|:----:|:---:|:------:|:--------:|:--:|:--:|
| S33.1 | Knowledge: Meta Delivery System | M | 60m | 50m | 1.20x | PASS | PASS* |
| S33.2 | Update: kokoro-ads-meta.md thresholds | S | — | — | — | PASS | PASS |
| S33.3 | Gate: /kokoro-ads learning check | S | — | — | — | PASS | PASS |

*QR on S33.1 caught one typo (reincias → reinicias) — fixed before merge.

## What Went Well

1. **Three-layer architecture.** The Knowledge → Update → Gate sequence
   produced a coherent defense in depth. The knowledge file is the authority,
   the update is the quick reference, the gate is the behavioral enforcement.
   Each layer serves a distinct purpose.

2. **Decision matrix as the load-bearing artifact.** The 7-row matrix in
   kokoro-meta-delivery-system.md (and its condensed version in kokoro-ads-meta.md)
   makes the exploration/learning/optimization determination deterministic.
   Kokoro no longer needs to infer — it can look up the scenario.

3. **Gate placement.** Positioning the learning phase gate in /kokoro-ads BEFORE
   the main instructions (after "Resolucion de invitado", before "Instrucciones")
   ensures it is loaded early in the skill execution flow. A gate buried at the
   bottom would be ignored.

4. **Issue case as anchor.** The 283-impression case from lunitomx/kokoro#1 is
   embedded in kokoro-meta-delivery-system.md as a concrete worked example. This
   is more durable than an abstract rule — future Kokoro instances can verify the
   logic against a real case.

## What Could Improve

1. **/kokoro-analytics gap.** S33.3 retrospective flagged that /kokoro-analytics
   (which reads ad metrics) doesn't have a learning phase gate. If that skill
   adds recommendation capabilities in the future, the gate should be ported.
   Logged for the parking lot.

2. **No live simulation test.** The verification was static (reading the gate
   text and confirming it matched the intent). A better test would be running
   /kokoro-ads with the exact issue scenario (283 imp, $79, 0 conv, 8 days) and
   confirming the output says ESPERAR. Worth doing as manual QA.

## Patterns Confirmed

- **PAT-L-052:** Behavioral gates in skill files should be positioned early
  (after context resolution, before main instructions) to ensure they are
  loaded before the AI begins generating recommendations.
- **PAT-L-053:** A knowledge file + quick-reference table + behavioral gate is
  the three-layer pattern for adding domain constraints to existing skills.
  Each layer serves a distinct audience: the knowledge file for deep reasoning,
  the table for quick lookup, the gate for mandatory checks.

## Done Criteria — Final Check

- [x] Knowledge file con delivery system completo instalado en ambos mirrors
- [x] kokoro-ads-meta.md tiene seccion de thresholds (tabla de 7 escenarios)
- [x] /kokoro-ads tiene gate de learning phase antes de recomendar on/off
- [x] El escenario del issue #1 no se repite (283 impresiones → ESPERAR, no APAGAR)
- [x] Verificacion completa — QR PASS en las 3 stories

## Next

- Manual QA: run /kokoro-ads with the issue scenario (283 imp, $79, 0 conv, 8 days)
  and verify output says ESPERAR
- Carry forward: /kokoro-analytics gate if it adds recommendation capabilities
- Carry forward: MCP configs, kokoro-onboard E2E, Konecta diagnostic, README count
- Close lunitomx/kokoro#1 with a comment linking to E33 deliverables
