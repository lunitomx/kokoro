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
| S1.1 | Package Skeleton | XS | Pending | pyproject.toml, src layout, `kokoro init` CLI |
| S1.2 | CLAUDE.md Brain | L | Pending | Eduardo's voice clone, methodology, anti-patterns |
| S1.3 | Knowledge Files | S | Pending | Methodology references as package data |
| S1.4 | /kokoro-diagnose | M | Pending | Speed Boat + Vision 20/20 guided session |
| S1.5 | /kokoro-mountain | M | Pending | Montaña del Mañana + OKRs |
| S1.6 | /kokoro-prune | S | Pending | Prune the Product Tree guided session |
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
- [ ] `pip install git+https://github.com/lunitomx/kokoro.git` succeeds
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

## Parking Lot

- Phase 2 skills (canvas, forces, interviews, validate) → E2
- Phase 3 skills (research, pescar, experiment, launch) → E3
- Phase 4 skills (factory, funnel, mafia, rhythm) → E4
- Automated skill output testing → future epic
