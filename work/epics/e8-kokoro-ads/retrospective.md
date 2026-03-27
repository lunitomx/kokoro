---
epic_id: "E8"
title: "Kokoro Ads — Skill de campañas publicitarias"
status: "complete"
closed: "2026-03-26"
---

# Epic Retrospective: E8 — Kokoro Ads

## Delivered
- /kokoro-ads skill with 3-step process (describe creative → identify audience → generate copy)
- Knowledge file with Meta Ads specs (character limits, WhatsApp templates, Advantage+)
- Extension mirrors for Claude Desktop compatibility
- Registered in test suite with structural validation
- 521 tests passing

## Metrics

| Metric | Value |
|--------|-------|
| Stories | 2 (S8.1 M, S8.2 S) |
| Tests added | 3 parametrized |
| Tests total | 521 |
| Files created | 4 skill files + mirrors + story artifacts |
| AR verdict | PASS (S8.1) |
| QR verdict | PASS (S8.1) |

## What Went Well
- Emerged from real user session — the skill solves a validated pain point
- .txt output format was the right call — markdown breaks in Meta Ads Manager
- Following existing skill pattern made implementation fast
- Process validated: describe creative → identify audience → generate copy

## What Could Improve
- Should have saved campaign work from the FIRST session — lost progress because nothing was persisted
- Next time: when doing ad-hoc work with a client, save context.md immediately

## Patterns Learned
- PAT-L-016: Ad platform copy must be .txt plain text — markdown formatting breaks in Meta Ads Manager, Google Ads, WhatsApp templates. Always generate copy-paste-ready output.
- PAT-L-017: Client work generates reusable context — campaign context files (inventario, precios, ubicacion) should be created at first contact, not when a skill needs them.

## Process Notes
- E8 originated from retro of a real session (Konecta Park campaign)
- The epic was small (S appetite, 2 stories) and completed in one session
- Story run worked well for both stories
