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

## In Scope

- Rename content: "Luxelling" → "Lux by Kokoro" in all skill prompts and knowledge files
- Rename directories: `luxelling/` → `lux/` in `.claude/knowledge/` and `extension/.claude/knowledge/`
- Rename files: `luxelling-*.md` → `lux-*.md`
- Update references in CLAUDE.md files (global, project, extension)
- Update governance docs that reference Luxelling
- Update backlog entry for E14

## Out of Scope

- Skill command slugs (`kokoro-luxury-*`) — "luxury" is generic, no issue
- Epic directory `work/epics/e14-kokoro-luxelling/` — historical record, leave as-is
- Logic or structure changes to the luxury module itself

## Stories

| ID | Story | Size |
|----|-------|------|
| S30.1 | Rename knowledge files and directories (luxelling/ → lux/) | S |
| S30.2 | Update skill content (Luxelling → Lux by Kokoro) in all commands | S |
| S30.3 | Update CLAUDE.md files and governance docs | XS |

## Done Criteria

- `grep -ri luxelling` returns zero results in tracked files
- All tests pass
- Skills load correctly in Claude Code
