# Epic E1: Kokoro Phase 1 — Preparar el Suelo — Scope

> **Status:** IN PROGRESS
> **Branch:** `epic/e1/kokoro-phase1`
> **Created:** 2026-03-02

## Objective

Deliver an installable Kokoro package that clones Eduardo Muñoz Luna's voice and methodology into Claude Code, enabling guided Phase 1 strategic alignment sessions for entrepreneurs.

**Value:** Entrepreneurs get Eduardo's proven "Preparar el Suelo" process as an AI-guided experience. Validates the extension model before building Phases 2-4.

## Stories

| ID | Story | Size | Status | Description |
|----|-------|:----:|:------:|-------------|
| S1.1 | Package Skeleton | XS | Done | pyproject.toml, src layout, `kokoro init` CLI |
| S1.2 | CLAUDE.md Brain | L | Done | Eduardo's voice clone, methodology, anti-patterns |
| S1.3 | Knowledge Files | S | Done | Methodology references as package data |
| S1.4 | /kokoro-diagnose | M | Done | Speed Boat + Vision 20/20 guided session |
| S1.5 | /kokoro-mountain | M | Done | Montaña del Mañana + OKRs |
| S1.6 | /kokoro-prune | S | Done | Prune the Product Tree guided session |
| S1.7 | /kokoro-finance | S | Pending | Financial assessment guided session |
| S1.8 | Meta Skills | M | Pending | /kokoro router + /kokoro-session management |

**Total:** 8 stories

## Scope

**In scope (MUST):**
- pip-installable Python package from GitHub
- `kokoro init` CLI command installs extension into user's .claude/
- CLAUDE.md that makes Claude respond as Eduardo (voice, philosophy, methodology)
- 4 Phase 1 skills as .claude/commands/*.md
- 2 meta skills: /kokoro (router), /kokoro-session
- Bilingual: Spanish soul, responds in user's language
- Extension files as package data (no network download)

**In scope (SHOULD):**
- Knowledge files embedded (framework references, attribution)
- settings.json for Claude Code configuration

**Out of scope:**
- Phases 2-4 skills → future epics (E2, E3, E4)
- Web UI / dashboard → not planned
- External API integrations (Meta, Google Ads) → Phase 3+
- User data persistence → Claude Code native sessions suffice

## Done Criteria

**Per story:**
- [ ] Code with type annotations (pyright strict)
- [ ] Tests passing
- [ ] Quality checks pass (ruff, pyright)

**Epic complete:**
- [ ] All stories complete (S1.1–S1.8)
- [ ] `pip install git+https://github.com/lunitomx/nitido.git` succeeds
- [ ] `kokoro init` creates .claude/ with all extension files
- [ ] Claude Code loads CLAUDE.md and responds in Eduardo's voice
- [ ] All 6 skills discoverable and executable
- [ ] Epic retrospective done
- [ ] Merged to `main`

## Dependencies

```
S1.1 (skeleton) ──┐
                   ├──→ S1.3 (knowledge) ──→ S1.4 (diagnose) ─┐
S1.2 (brain)    ──┘                     ──→ S1.5 (mountain) ─┤
                                        ──→ S1.6 (prune)    ─┤
                                        ──→ S1.7 (finance)  ─┤
                                                              ↓
                                                   S1.8 (meta skills)
```

- S1.1 and S1.2 are **parallel** (no dependency between them)
- S1.3 depends on S1.1 (needs package structure for data files)
- S1.4–S1.7 depend on S1.2 (voice) and S1.3 (knowledge) — **parallel** with each other
- S1.8 depends on S1.4–S1.7 (router needs skills to exist)

**External:** None

## Architecture

| Decision | Source | Summary |
|----------|--------|---------|
| src layout | SES-001 | `src/kokoro/` for proper packaging |
| Package data | SES-001 | Extension files shipped as package_data, no downloads |
| CLAUDE.md merge | SES-001 | Append with `<!-- KOKORO START/END -->` markers |
| Skill format | SES-001 | `.claude/commands/{name}.md` per Claude Code convention |
| Namespace | SES-001 | `kokoro-*` for skills, `kokoro.*` for metadata |

> Problem Brief: N/A (originated from knowledge synthesis in SES-001)

## Risks

| Risk | L/I | Mitigation |
|------|:---:|------------|
| Eduardo's voice too generic in CLAUDE.md | M/H | Use libro-summary.md patterns, test with known Eduardo phrases |
| Claude Code skill format changes | L/M | Pin to current convention, minimal coupling |
| Knowledge files too large for context | L/L | Already confirmed: platform limits are file count, not size |

## Implementation Plan

> Added by `/rai-epic-plan` — 2026-03-02

### Story Sequence

| Order | Story | Size | Dependencies | Milestone | Rationale |
|:-----:|-------|:----:|--------------|-----------|-----------|
| 1 | S1.1 Package Skeleton | XS | None | M1 | Quick win: establishes structure, unblocks S1.3 |
| 2 | S1.2 CLAUDE.md Brain | L | None | M1 | Risk-first: hardest story, star of the project. If voice fails, everything pivots |
| 3 | S1.3 Knowledge Files | S | S1.1 | M1 | Bridges package to skills, quick after skeleton exists |
| 4 | S1.4 /kokoro-diagnose | M | S1.2, S1.3 | M2 | First skill — proves the skill pattern works |
| 5 | S1.5 /kokoro-mountain | M | S1.2, S1.3 | M2 | Follows Phase 1 methodology order |
| 6 | S1.6 /kokoro-prune | S | S1.2, S1.3 | M3 | Methodology order, smaller scope |
| 7 | S1.7 /kokoro-finance | S | S1.2, S1.3 | M3 | Methodology order, smaller scope |
| 8 | S1.8 Meta Skills | M | S1.4–S1.7 | M3 | Router needs all skills to exist |

### Critical Path

```
S1.1 → S1.3 ─┐
              ├──→ S1.4 → S1.5 → S1.6 → S1.7 → S1.8
S1.2 ─────────┘
```

S1.2 is the longest story (L) and gates all skills. It IS the critical path.

### Milestones

| Milestone | Stories | Success Criteria |
|-----------|---------|------------------|
| **M1: Walking Skeleton** | S1.1, S1.2, S1.3 | `kokoro init` installs, CLAUDE.md loads, Claude responds as Eduardo |
| **M2: Core MVP** | +S1.4, S1.5 | 2 skills functional, full Phase 1 diagnostic + vision flow |
| **M3: Feature Complete** | +S1.6, S1.7, S1.8 | All 6 skills work, /kokoro routes correctly |
| **M4: Epic Complete** | — | Done criteria met, retrospective done, merged to main |

### Progress Tracking

| Story | Size | Status | Actual | Notes |
|-------|:----:|:------:|:------:|-------|
| S1.1 Package Skeleton | XS | Done | XS | SES-002 |
| S1.2 CLAUDE.md Brain | L | Done | M | SES-002/003, 2x velocity |
| S1.3 Knowledge Files | S | Done | 20 min | 1.75x velocity |
| S1.4 /kokoro-diagnose | M | Done | S | |
| S1.5 /kokoro-mountain | M | Done | S | PAT-L-001, 2x velocity |
| S1.6 /kokoro-prune | S | Done | S | PAT-L-001 |
| S1.7 /kokoro-finance | S | Pending | — | |
| S1.8 Meta Skills | M | Pending | — | |

### Sequencing Risks

| Risk | L/I | Mitigation |
|------|:---:|------------|
| S1.2 takes longer than expected (voice tuning) | M/H | Timebox voice iterations; "good enough" first, refine in later stories |
| Skill pattern established in S1.4 needs revision | M/M | Build S1.4 as the template, validate before batch-building S1.5-S1.7 |
| S1.8 router logic unclear until all skills exist | L/M | Define routing contract early in S1.2 CLAUDE.md, implement last |

## Parking Lot

- Phase 2 skills (canvas, forces, interviews, validate) → E2
- Phase 3 skills (research, pescar, experiment, launch) → E3
- Phase 4 skills (factory, funnel, mafia, rhythm) → E4
- Automated skill output testing → future epic
