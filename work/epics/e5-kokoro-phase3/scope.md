# Epic E5: Kokoro Phase 3 — Germinar — Scope

> **Status:** DONE
> **Created:** 2026-03-24
> **Problem Brief:** `dev/problem-briefs/e5-kokoro-phase3.md`

## Objective

Deliver Phase 3 ("Germinar") of Kokoro: 4 coaching skills that guide
entrepreneurs from validated model to market presence. Research, content
strategy (PESCAR), experimentation (3x3x3), and launch — completing 75%
of Eduardo's 4-phase journey.

**Value:** Entrepreneurs who completed Phases 1-2 can now execute. The
gap between "I validated my idea" and "people can find me" is closed.

## Stories

| ID | Story | Size | Status | Description |
|----|-------|:----:|:------:|-------------|
| S5.1 | Knowledge Files Phase 3 | S | Pending | 4 methodology references for Phase 3 skills |
| S5.2 | /kokoro-research | M | Pending | Multi-source market research guided session |
| S5.3 | /kokoro-pescar | M | Pending | PESCAR methodology complete guided session |
| S5.4 | /kokoro-experiment | M | Pending | 3x3x3 experiment sprint execution + reporting |
| S5.5 | /kokoro-launch | M | Pending | Copy frameworks + scripts + launch strategy |
| S5.6 | Meta Skills Update | S | Pending | Router + session + ontology for Phase 3 |

**Total:** 6 stories

## Scope

**In scope (MUST):**
- 4 Phase 3 skill files following PAT-L-001 pattern
- 4 knowledge files as package data
- Eduardo's voice: vocabulary, anti-patterns, Proyector strategy
- Persistence: Persistencia + context previo sections in all skills
- /kokoro-session and /kokoro router updated for Phase 3
- Anti-vocabulary tests for all new skills
- Output structure tests (template, table, siguiente paso)
- Cross-reference validation (no broken /kokoro-X links)
- Ontology store updated: Phase 3 skill mappings

**In scope (SHOULD):**
- Ontology node types for Phase 3 if needed
- Hardened assertions (Eduardo voice >= 3, anti-patterns >= 2)

**Out of scope:**
- Web quality diagnostics
- Video/creative analysis pipeline
- Phase 4 skills (E6)
- Marketing automation / API integrations
- Actual copy generation (Kokoro GUIDES, doesn't write for them)

## Done Criteria

**Per story:**
- [ ] Tests pass (pyright, ruff, pytest)
- [ ] Commit after each task

**Epic complete:**
- [ ] All 6 stories complete
- [ ] 4 Phase 3 skill files in extension/.claude/commands/
- [ ] 4 knowledge files in extension/.claude/knowledge/
- [ ] All skills have Persistencia + context sections
- [ ] Anti-vocabulary passes on all new files
- [ ] Output structure tests pass (templates intact)
- [ ] Meta skills aware of Phase 3
- [ ] All 365+ tests pass
- [ ] Zero prohibited vocabulary in new code
- [ ] Epic retrospective done

## Phase 3 Skills Design

### /kokoro-research — Investigacion Multi-Fuente
**Purpose:** Guide systematic market research beyond the interview sample.
**Exercises:**
1. Desk research: industry reports, trends, competitors
2. Social listening: what does the segment say online?
3. Competitive mapping: who else serves this segment?
4. Synthesis: patterns across sources → research brief

**Output:** Research brief with validated insights, competitor map, opportunity gaps.
**Feeds:** /kokoro-pescar (content strategy needs research data)

### /kokoro-pescar — Metodologia PESCAR
**Purpose:** Guide complete content + marketing strategy using Eduardo's PESCAR.
**PESCAR framework:**
1. **P**roblema — anchor to the validated problem (from canvas/forces)
2. **E**strategia — define the approach (inbound, outbound, community, etc.)
3. **S**egmento — refine targeting with research data
4. **C**ontenido — design content pillars and editorial calendar
5. **A**ccion — define CTAs and conversion paths
6. **R**esultado — set metrics and measurement cadence

**Output:** PESCAR canvas with content pillars, editorial calendar skeleton, KPIs.
**Feeds:** /kokoro-launch (launch uses the strategy from PESCAR)

### /kokoro-experiment — Reporte de Experimento 3x3x3
**Purpose:** Execute and document validation sprints.
**Structure:**
1. Hypothesis from /kokoro-validate
2. 3-week sprint design: build → measure → learn
3. Experiment execution guidance
4. Results documentation: what worked, what didn't, what to pivot
5. Next sprint planning

**Output:** Experiment report with data, learnings, next actions.
**Feeds:** /kokoro-launch (launch strategy informed by experiment results)

### /kokoro-launch — Copies + Scripts + Landing
**Purpose:** Guide the creation of launch assets.
**Exercises:**
1. Value proposition copy (from PUV + forces)
2. Landing page structure (problem → solution → proof → CTA)
3. Launch script (email, social, outreach sequences)
4. Pre-launch checklist
5. Launch day playbook

**Output:** Copy frameworks, page structure, launch sequence, checklist.
**Note:** Kokoro GUIDES the creation. It does NOT generate generic copy.
Eduardo would say: "La forma de comunicar define tu categoría."

## Dependencies

```
S5.1 (knowledge) → S5.2 (research) → S5.3 (pescar)
                     S5.4 (experiment, parallel to S5.3)
                     S5.5 (launch, after S5.3)
S5.6 (meta update, after S5.2-S5.5)
```

- S5.1 first: knowledge files ground the skills
- S5.2 after S5.1: research needs methodology reference
- S5.3/S5.4 can be parallel (different exercises, same Phase 3)
- S5.5 after S5.3: launch builds on PESCAR strategy
- S5.6 last: meta skills update after all skills exist

**External:** None. E3 ontology complete, Phase 1-2 stable.

## Risks

| Risk | L/I | Mitigation |
|------|:---:|------------|
| PESCAR methodology source material thin | M/H | Design from Eduardo's curriculum + lean marketing principles |
| Skills become generic marketing advice | M/H | Enforce Eduardo's voice, metaphors, Proyector strategy |
| Launch skill drifts into copywriting | M/M | Clear boundary: guide frameworks, not generate copy |
| 4 M-sized skills may be larger than E2 | L/M | Follow E2 pattern exactly, timebox per skill |

## Architecture

Same as E1/E2: markdown skill files + knowledge files as package data.
No new code beyond test files and ontology store updates for Phase 3 mappings.

## Implementation Plan

### Story Sequence

| Order | Story | Size | Dependencies | Rationale |
|:-----:|-------|:----:|-------------|-----------|
| 1 | S5.1 Knowledge Files Phase 3 | S | None | Foundation: knowledge grounds the skills |
| 2 | S5.2 /kokoro-research | M | S5.1 | Risk-first: most novel skill, tests the Phase 3 pattern |
| 3 | S5.3 /kokoro-pescar | M | S5.1 | Core: PESCAR is the centerpiece of Phase 3 |
| 4 | S5.4 /kokoro-experiment | M | S5.1 | Parallel-capable: independent exercise from PESCAR |
| 5 | S5.5 /kokoro-launch | M | S5.3 | Dependency: launch uses PESCAR strategy |
| 6 | S5.6 Meta Skills Update | S | S5.2-S5.5 | Last: update router/session after all skills exist |

### Milestones

| Milestone | Stories | Success Criteria |
|-----------|---------|------------------|
| **M1: Foundation** | S5.1 | 4 knowledge files, methodology grounded |
| **M2: Core Skills** | +S5.2, S5.3, S5.4 | 3 skills working, research→pescar→experiment flow |
| **M3: Epic Complete** | +S5.5, S5.6 | Launch skill, meta update, retrospective |

### Progress Tracking

| Story | Size | Status | Actual | Notes |
|-------|:----:|:------:|:------:|-------|
| S5.1 Knowledge Files Phase 3 | S | Done | S | 4 files, 607 lines |
| S5.2 /kokoro-research | M | Done | S | 14 tests, 4 exercises |
| S5.3 /kokoro-pescar | M | Done | S | 11 tests, 6-step PESCAR |
| S5.4 /kokoro-experiment | M | Done | S | 12 tests, 3x3x3 framework |
| S5.5 /kokoro-launch | M | Done | S | 14 tests, 4 exercises |
| S5.6 Meta Skills Update | S | Done | XS | Router + session + ontology |
