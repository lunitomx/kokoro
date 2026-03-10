---
epic_id: "E1"
title: "Kokoro Phase 1 — Preparar el Suelo"
status: "in_progress"
created: "2026-03-02"
---

# Epic Brief: Kokoro Phase 1 — Preparar el Suelo

## Hypothesis
For entrepreneurs and small business owners who need strategic clarity before marketing,
Kokoro is a Claude Code extension (pip-installable)
that guides them through Eduardo Muñoz Luna's methodology to align their business foundations.
Unlike generic AI marketing tools, Kokoro clones Eduardo's voice, philosophy, and proven frameworks.

## Success Metrics
- **Leading:** `kokoro init` installs cleanly and CLAUDE.md loads Eduardo's voice into Claude Code
- **Lagging:** Phase 1 skills (diagnose, mountain, prune, finance) deliver guided strategic sessions

## Appetite
L — 8 stories (package skeleton + CLAUDE.md brain + 4 skills + 2 meta skills)

## Scope Boundaries
### In (MUST)
- pip-installable Python package with `kokoro init` CLI command
- CLAUDE.md that clones Eduardo's voice and methodology (the star of the project)
- 4 Phase 1 skills: /kokoro-diagnose, /kokoro-mountain, /kokoro-prune, /kokoro-finance
- 2 meta skills: /kokoro (router), /kokoro-session (session management)
- Extension files as package data (no network download)
- Bilingual: Spanish soul, responds in user's language

### In (SHOULD)
- Knowledge files embedded in extension (methodology references, frameworks)
- settings.json for Claude Code configuration

### No-Gos
- Phases 2-4 skills (future epics)
- Web UI or dashboard
- Integration with external APIs (Meta, Google Ads, etc.)
- User data persistence beyond Claude Code's native session

### Rabbit Holes
- Over-engineering the CLI beyond `kokoro init`
- Building a skill registry system (Claude Code auto-discovers)
- Trying to compress knowledge files for token limits (platform limits are on file count, not size)
