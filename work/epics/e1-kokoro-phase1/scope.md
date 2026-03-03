# E1 Scope: Kokoro Phase 1 — Preparar el Suelo

## Objective
Build the installable Kokoro package with Eduardo's cloned voice and Phase 1 strategic alignment skills.

## In Scope
- Python package structure (src layout, pyproject.toml)
- `kokoro init` CLI command that installs extension into user's project
- CLAUDE.md with Eduardo's personality, voice patterns, and methodology knowledge
- 4 Phase 1 skills as .md files in extension/commands/
- 2 meta skills (router + session)
- Knowledge reference files for methodology frameworks

## Out of Scope
- Phases 2-4 (Elegir la Semilla, Germinar, Cosechar)
- External API integrations
- Web interfaces
- Automated testing of skill outputs (manual QA)

## Planned Stories
1. S1.1 — Package Skeleton (pyproject.toml, src layout, kokoro init CLI)
2. S1.2 — CLAUDE.md Brain (Eduardo's voice clone, methodology, anti-patterns)
3. S1.3 — Knowledge Files (methodology references as package data)
4. S1.4 — /kokoro-diagnose skill (Speed Boat + Vision 20/20)
5. S1.5 — /kokoro-mountain skill (Montaña del Mañana + OKRs)
6. S1.6 — /kokoro-prune skill (Prune the Product Tree)
7. S1.7 — /kokoro-finance skill (Financial assessment)
8. S1.8 — Meta skills (/kokoro router + /kokoro-session)

## Done Criteria
- `pip install kokoro` from GitHub succeeds
- `kokoro init` creates .claude/ directory with all extension files
- Claude Code loads CLAUDE.md and responds in Eduardo's voice
- All 6 skills are discoverable and executable in Claude Code
