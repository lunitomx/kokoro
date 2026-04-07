---
epic_id: "E30"
title: "Lux by Kokoro — Rename from Luxelling"
status: "Planned"
created: "2026-04-07"
---

# Plan: E30 — Lux by Kokoro Rename

## Execution Order

```
S30.1 (knowledge dirs/files) → S30.2 (skill commands) → S30.3 (docs + verify)
```

Linear dependency — each story depends on the previous.

---

## S30.1 — Rename knowledge files and directories

**Objective:** Rename all `luxelling/` dirs to `lux/` and all `luxelling-*.md`
files to `lux-*.md` in both mirrors. Update content inside files.

**Size:** S | **Depends on:** —

### Tasks

1. Rename `extension/.claude/knowledge/luxelling/` → `extension/.claude/knowledge/lux/`
   - `luxelling-master.md` → `lux-master.md`
   - `luxelling-assessment.md` → `lux-assessment.md`
   - `luxelling-scarcity.md` → `lux-scarcity.md`
   - `luxelling-quality-symbolism.md` → `lux-quality-symbolism.md`
   - `luxelling-experience.md` → `lux-experience.md`
   - `luxelling-communication.md` → `lux-communication.md`
   - `luxelling-pricing.md` → `lux-pricing.md`
   - `luxelling-growth.md` → `lux-growth.md`

2. Replace "Luxelling" → "Lux by Kokoro" inside each renamed file

3. Update `extension/.claude/knowledge/kokoro-luxury-layers.md` — replace all
   "Luxelling" references with "Lux by Kokoro"

4. Mirror to `.claude/knowledge/`:
   - Rename `.claude/knowledge/luxelling/` → `.claude/knowledge/lux/`
   - Same 8 file renames
   - Same content updates
   - Update `.claude/knowledge/kokoro-luxury-layers.md`

5. Commit: `feat(s30.1): rename knowledge files luxelling → lux`

### Verification

- `ls extension/.claude/knowledge/lux/` shows 8 files with `lux-` prefix
- `ls .claude/knowledge/lux/` shows 8 files with `lux-` prefix
- `ls extension/.claude/knowledge/luxelling/` → does not exist
- `grep -ri luxelling extension/.claude/knowledge/` → 0 results
- `grep -ri luxelling .claude/knowledge/` → 0 results

---

## S30.2 — Update skill command content

**Objective:** Replace "Luxelling" → "Lux by Kokoro" in all luxury skill commands
and update knowledge file references from `luxelling/luxelling-*.md` to `lux/lux-*.md`.

**Size:** S | **Depends on:** S30.1

### Tasks

1. Update these 8 commands in `extension/.claude/commands/`:
   - `kokoro-luxury.md` — router principal
   - `kokoro-luxury-assess.md`
   - `kokoro-luxury-scarcity.md`
   - `kokoro-luxury-quality.md`
   - `kokoro-luxury-experience.md`
   - `kokoro-luxury-communication.md`
   - `kokoro-luxury-pricing.md`
   - `kokoro-luxury-growth.md`

   In each file:
   - Replace "Luxelling" → "Lux by Kokoro" in content
   - Replace `luxelling/luxelling-` → `lux/lux-` in knowledge file references

2. Mirror: apply same changes to `.claude/commands/` (8 files)

3. Commit: `feat(s30.2): update skill commands luxelling → lux by kokoro`

### Verification

- `grep -ri luxelling extension/.claude/commands/` → 0 results
- `grep -ri luxelling .claude/commands/` → 0 results
- `grep -r "lux/lux-" extension/.claude/commands/kokoro-luxury*.md` → references found (correct)

---

## S30.3 — Update docs, governance, and final verification

**Objective:** Update remaining references in README, CLAUDE.md files, governance.
Run full verification that zero `luxelling` references remain.

**Size:** XS | **Depends on:** S30.2

### Tasks

1. Update `extension/README.md` — replace any "Luxelling" references

2. Check and update CLAUDE.md files if needed:
   - `.claude/CLAUDE.md`
   - `extension/.claude/CLAUDE.md`
   - Root `CLAUDE.md`

3. Update `governance/backlog.md` — E14 label if desired (optional, historical)

4. Run final verification:
   ```bash
   grep -ri luxelling --include="*.md" | grep -v "work/epics/e14\|work/epics/e1-\|work/epics/e30"
   ```
   Must return 0 results.

5. Run tests: `uv run pytest`

6. Commit: `feat(s30.3): final docs update + zero-luxelling verification`

### Verification

- Final grep returns 0 non-historical references
- All tests pass
- `extension/README.md` references "Lux by Kokoro"

---

## Milestones

| Milestone | Stories | Gate |
|-----------|---------|------|
| M1: Knowledge renamed | S30.1 | Dirs exist, content updated |
| M2: Skills updated | S30.2 | References resolve to new paths |
| M3: Clean repo | S30.3 | Zero luxelling + tests pass |
