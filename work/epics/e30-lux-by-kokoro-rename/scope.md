---
epic_id: "E30"
title: "Lux by Kokoro — Rename from Luxelling"
status: "In Progress"
created: "2026-04-07"
---

# Scope: E30 — Lux by Kokoro Rename

## Objective

Replace all references to "Luxelling" (third-party registered trademark) with
"Lux by Kokoro" across the entire codebase to eliminate legal risk and establish
Eduardo's own luxury methodology brand.

## Value

Legal compliance + brand ownership. "Luxelling" is a registered trademark that
inspired the module but is not ours to use. "Lux by Kokoro" positions the luxury
methodology as Eduardo's own creation within the Kokoro ecosystem.

## In Scope (MUST)

- Rename knowledge directories: `luxelling/` → `lux/` (both `.claude/knowledge/` and `extension/.claude/knowledge/`)
- Rename knowledge files: `luxelling-*.md` → `lux-*.md` (16 files total, 8 per mirror)
- Update content: "Luxelling" → "Lux by Kokoro" in all skill commands (16 files)
- Update content in `kokoro-luxury-layers.md` (2 files)
- Update `extension/README.md`
- Final verification: zero `luxelling` matches in tracked files

## In Scope (SHOULD)

- Update governance/backlog.md E14 label for clarity

## Out of Scope

- Skill command slugs (`kokoro-luxury-*`) — "luxury" is generic, no trademark issue
- Epic directory `work/epics/e14-kokoro-luxelling/` — historical record, preserved as-is
- Epic directory `work/epics/e1-kokoro-phase1/` — historical references, preserved
- Any logic or structure changes to the luxury module

## Stories

| ID | Story | Size | Depends on |
|----|-------|------|------------|
| S30.1 | Rename knowledge files and directories | S | — |
| S30.2 | Update skill command content | S | S30.1 |
| S30.3 | Update docs, governance, and final verification | XS | S30.2 |

## Done Criteria

1. `grep -ri luxelling --include="*.md" | grep -v "work/epics/e14\|work/epics/e30\|work/epics/e1"` returns 0 results
2. `uv run pytest` passes
3. Knowledge file references in skills resolve correctly (no broken links)

## Risks

| Risk | L | I | Mitigation |
|------|---|---|------------|
| Broken knowledge refs in skills | M | M | S30.2 depends on S30.1; verify refs |
| Mirror drift | L | L | Process both mirrors in same story |
| Missed occurrence | L | M | Final grep in S30.3 |
