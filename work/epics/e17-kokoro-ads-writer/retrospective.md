# Epic Retrospective: E17 — Kokoro Ads Writer

**Completed:** 2026-03-30
**Resolution:** Partial — RaizAncestral scope complete, MCP backend deferred
**Stories:** 2 delivered (S17.3, S17.4), 2 deferred to MetricaRadix (S17.1, S17.2)

---

## Summary

E17 aimed to let Kokoro upload creatives directly to Meta Ads campaigns. The RaizAncestral side is complete: `/kokoro-publish` (S17.3) handles the publishing flow and the confirmation gate (S17.4) ensures double-check before any write. The backend MCP write tools (S17.1 permission verification + S17.2 write endpoints) live in MetricaRadix and are deferred — they require Facebook API `ads_management` scope and work in a different repository.

## Resolution: Partial

- **S17.3 done:** `/kokoro-publish` skill created — reads creative, shows preview, calls MCP write tools
- **S17.4 done:** Confirmation gate integrated — preview + explicit "si" before publish
- **S17.1 deferred:** Token permission verification — MetricaRadix repo, needs `ads_management` scope
- **S17.2 deferred:** MCP write tools (`create_ad_creative`, `update_ad_creative_text`, `upload_ad_image`) — MetricaRadix repo

## What Went Well

- AD-1 (never touch budget) is hardcoded in the skill — safety by design
- Separating skill (RaizAncestral) from backend (MetricaRadix) was the right call
- The confirmation gate pattern is reusable for any future write operation

## What Could Be Improved

- S17.1+S17.2 should have been tracked in MetricaRadix's backlog, not here

## Architecture Decisions Validated

- **AD-1: Solo creativos, NUNCA presupuesto** — correct and non-negotiable
- **AD-2: Confirmacion obligatoria** — implemented in S17.4
- **AD-3: Extender MCP existente** — validated, just needs execution in MetricaRadix

## Next Steps

- When Eduardo needs to publish creatives from Kokoro: execute S17.1+S17.2 in MetricaRadix
- `/kokoro-publish` is ready and waiting for the backend
