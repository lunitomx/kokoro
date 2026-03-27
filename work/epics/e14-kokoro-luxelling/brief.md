---
epic_id: "E14"
title: "Kokoro Luxelling — Conocimiento de lujo condicional"
status: "draft"
created: "2026-03-27"
---

# Epic Brief: E14 — Kokoro Luxelling

## Hypothesis
For Eduardo's luxury-tier clients (Legacy by Invertikal, ISDVEY, future luxury brands)
who need luxury-specific strategic guidance beyond standard Kokoro methodology,
the Kokoro Luxelling system is a conditional knowledge layer with its own skill ecosystem
that activates luxury frameworks (Efecto Veblen, escasez estrategica, comunicacion que eleva,
value-based pricing) only when the client's positioning tier qualifies,
unlike the current Kokoro setup where luxury vocabulary is default but luxury strategy is absent.
Our solution gates luxury knowledge behind a positioning assessment (Triangulo F-S-E)
and provides `/kokoro-luxury` as router with module-specific mini-skills.

## Success Metrics
- **Leading:** Luxury assessment completes in <5 min, correctly classifying positioning tier
- **Lagging:** Legacy by Invertikal onboarded as luxury client with full platform connections

## Appetite
M-L — 5-7 stories

## Scope Boundaries
### In (MUST)
- Positioning tier assessment (luxury / premium / standard) integrated into client profile
- `/kokoro-luxury` router skill with module navigation
- Mini-skills per Luxelling module (escasez, calidad, experiencia, comunicacion, pricing, poder simbolico)
- Knowledge files from notas-eduardo + workbook integrated into conocimientoraiz/
- Legacy by Invertikal client profile with luxury tier + platform connections
- Luxury knowledge activates ONLY when positioning_tier = luxury or premium

### In (SHOULD)
- Workbook module 09 (Nuevo Lujo del Manana) integrated
- LUXELLING_Arquitectura_Completa synthesis as master reference
- ISDVEY client profile

### No-Gos
- No modify existing Kokoro skills — luxury is additive, not replacement
- No change Kokoro base vocabulary (inversion, creacion, cortesia remain universal)
- No luxury-specific MCP servers — use existing MétricaRadix
- No web UI — all conversational via skills

### Rabbit Holes
- Building a luxury CRM — just use client graph with positioning_tier
- Creating industry-specific luxury templates (hospitality, fashion, real estate) — too early
- Automating luxury brand audits — keep it guided/conversational
