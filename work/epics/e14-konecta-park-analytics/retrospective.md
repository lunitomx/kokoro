# Epic Retrospective: E14 — Konecta Park Analytics

**Updated:** 2026-03-30
**Resolution:** Near-complete — S14b.2+S14b.3 done via reporte MetricaRadix, S14b.4 pendiente validación
**Stories:** 3 delivered (S14b.1-S14b.3), 1 pending (S14b.4 — post-cambio)

---

## Summary

E14 aimed to diagnose why Konecta Park's Meta Ads campaigns attracted spam instead of brokers/investors. The diagnosis was executed via a comprehensive MetricaRadix weekly report (27-30 Mar 2026) that crossed data from Meta Business API, GA4, Microsoft Clarity, and Pipedrive — revealing that the root cause was NOT targeting keywords ("albañilería") as originally suspected, but Audience Network delivering 96.6% junk traffic (bots + zero-engagement sessions). Corrective actions were applied immediately.

## Key Findings

1. **Audience Network was the primary problem** — 96.6% of Meta traffic to the website had zero engagement (Clarity recordings). 42% were flagged as bots.
2. **Pixel was inflating conversions** — 9 CompleteRegistration reported by pixel, but only 2 confirmed in Pipedrive. 7 were view-through (saw ad, arrived at /gracias by another path). Real CPR: $379, not $84.
3. **Brokers campaign is healthy** — $16.37 per WA conversation, 39 conversations, healthy depth funnel (55% depth 2, 15% depth 5).
4. **125 hidden conversions** — GA4 tracked 125 click_to_chat on the website from Meta traffic, not counted as Meta conversions. 99 on March 28 were from Audience Network (now excluded).
5. **UTM bug in Brokers form** — Leads arrive to Pipedrive without UTMs, breaking attribution.

## Actions Taken

- Audience Network excluded from CompleteRegistration campaign (March 30)
- "Avance de Obra" creative reactivated with traffic filtered through profiling form
- Pixel fix E15 in progress: move firing to Pipedrive API callback (eliminates view-through ghost conversions)

## What Went Well

- Cross-platform analysis (Meta + GA4 + Clarity + Pipedrive) revealed truth that single-platform data hid
- Original hypothesis ("targeting includes albañilería fields") was wrong — the real cause was placement, not audience
- The reporte format (HTML with charts, funnels, creative cards) makes findings actionable for the client

## What Could Be Improved

- Diagnosis was done manually via MetricaRadix reporte, not via /kokoro-analytics as E14 originally planned
- The infrastructure (/kokoro-analytics + MCP) exists but the manual cross-platform analysis was more thorough for this case

## Next Steps

- **S14b.4 validation:** Compare next week's data (post Audience Network exclusion) ~2026-04-07
- Verify click_to_chat volume drops (99 on March 28 were Audience Network)
- Monitor if real CPR improves with cleaner traffic
- Fix UTMs in Brokers form for proper Pipedrive attribution
