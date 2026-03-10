---
epic_id: "E2"
title: "Kokoro Phase 2 — Elegir la Semilla"
status: "in_progress"
created: "2026-03-09"
---

# Epic Brief: Kokoro Phase 2 — Elegir la Semilla

## Hypothesis
For entrepreneurs who completed Phase 1 (strategic alignment) and need to validate their business model before building,
Kokoro Phase 2 extends the extension with 4 new skills
that guide them through Lean Canvas, Customer Forces, validation interviews, and experiment planning.
Unlike generic business planning tools, Phase 2 continues Eduardo's voice and methodology — "el modelo de negocio ES tu producto."

## Success Metrics
- **Leading:** 4 new Phase 2 skills discoverable and executable via Claude Code
- **Lagging:** Entrepreneur completes full Phase 2 cycle — from Lean Canvas to validation plan — with Eduardo's guided methodology

## Appetite
M — 6 stories (knowledge files + 4 skills + meta skills update)

## Scope Boundaries
### In (MUST)
- 4 Phase 2 skills: /kokoro-canvas, /kokoro-forces, /kokoro-interviews, /kokoro-validate
- Knowledge files for Phase 2 methodology (Lean Canvas, Customer Forces, entrevistas, validacion)
- Eduardo's voice maintained across all new skills
- Skills follow PAT-L-001 pattern established in E1

### In (SHOULD)
- Update /kokoro router to recognize Phase 2 position and route accordingly
- Update /kokoro-session to manage Phase 2 progress
- conftest.py with shared test fixtures (carry-forward from E1 retrospective)

### No-Gos
- Phases 3-4 skills (future epics E3, E4)
- External integrations (surveys, CRM, analytics)
- Persistent data storage or user databases
- Changes to CLI beyond what Phase 2 skills require

### Rabbit Holes
- Building actual survey/interview tools (skills guide the process, user executes manually)
- Over-engineering validation scoring (qualitative assessment, not quantitative engine)
- Trying to integrate real market data APIs (Eduardo's methodology is insight-driven, not data-driven)
