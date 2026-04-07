---
epic_id: "E31"
title: "Kokoro Creative Review — Retroalimentacion de creativos bajo Meta AI"
status: "Planned"
created: "2026-04-07"
---

# Plan: E31 — Kokoro Creative Review

## Execution Order

```
S31.1 (knowledge files) → S31.2 (skill command) → S31.3 (mirror + tests + verify)
```

Linear dependency — knowledge must exist before the skill references it.

---

## S31.1 — Crear knowledge files (Meta AI ecosystem + Matriz Creativa)

**Objective:** Consolidar los 6 documentos fuente en 2 knowledge files optimizados
para consumo por el skill.

**Size:** S | **Depends on:** —

**Status:** DONE — archivos ya creados:
- `extension/.claude/knowledge/kokoro-meta-ai-ecosystem.md` (GEM + Andromeda + Lattice + Sequence Learning)
- `extension/.claude/knowledge/kokoro-creative-diversification.md` (16 Deseos x 5 Niveles + Matriz)
- Mirrors en `.claude/knowledge/`

### Tasks

1. ~~Crear `kokoro-meta-ai-ecosystem.md`~~ DONE
2. ~~Crear `kokoro-creative-diversification.md`~~ DONE
3. ~~Copiar mirrors a `.claude/knowledge/`~~ DONE
4. Commit: `feat(s31.1): knowledge files for Meta AI ecosystem and creative diversification`

### Verification

- Files exist in both `extension/.claude/knowledge/` and `.claude/knowledge/`
- Content covers los 4 sistemas (GEM, Andromeda, Lattice, Sequence)
- Matriz de 16 Deseos x 5 Niveles present

---

## S31.2 — Crear skill command /kokoro-creative-review

**Objective:** Crear el skill command que analiza creativos bajo los 4 lentes
de Meta AI con la voz de Eduardo.

**Size:** M | **Depends on:** S31.1

**Status:** DONE — skill ya creado:
- `extension/.claude/commands/kokoro-creative-review.md`
- Mirror en `.claude/commands/`

### Tasks

1. ~~Crear el skill command con 5 pasos~~ DONE
   - Paso 1: Recibir creativo (multimodal)
   - Paso 2: Analisis bajo 4 lentes (GEM, Andromeda, Lattice, Sequence)
   - Paso 3: Score global + Matriz de Diversificacion
   - Paso 4: Recomendaciones con voz de Eduardo
   - Paso 5: Siguiente paso (creative, ads, analytics)
2. ~~Copiar mirror a `.claude/commands/`~~ DONE
3. Commit: `feat(s31.2): /kokoro-creative-review skill command`

### Verification

- Skill references `kokoro-meta-ai-ecosystem.md` and `kokoro-creative-diversification.md`
- Follows Proyector strategy (esperar invitacion)
- Uses luxurizante vocabulary (inversion, creacion, invitado)
- Has anti-patterns section
- Has persistence section (save review to clientes/)

---

## S31.3 — Update docs, tests, verification end-to-end

**Objective:** Registrar el skill en README, CLAUDE.md, crear tests de vocabulario,
verificar que funciona end-to-end.

**Size:** S | **Depends on:** S31.2

### Tasks

1. Update `extension/README.md` — agregar `/kokoro-creative-review` a la lista
   de herramientas transversales con descripcion

2. Update `extension/.claude/CLAUDE.md` — agregar a la seccion de herramientas
   transversales:
   ```
   - `/kokoro-creative-review` — Analisis de creativos bajo Meta AI
   ```

3. Update `.claude/CLAUDE.md` (project) — agregar a herramientas transversales

4. Update root `CLAUDE.md` — agregar si tiene seccion de herramientas

5. Update `governance/backlog.md` — agregar E31

6. Create test `tests/test_creative_review.py`:
   - Test skill file exists
   - Test has Eduardo voice (Proyector strategy)
   - Test references knowledge files
   - Test no prohibited vocabulary
   - Test has 4 Meta AI lenses (GEM, Andromeda, Lattice, Sequence)
   - Test has scoring system
   - Test has Matriz de Diversificacion reference

7. Run tests: `uv run pytest`

8. Commit: `feat(s31.3): docs, tests, and verification for creative-review`

### Verification

- Skill appears in README and CLAUDE.md files
- All vocabulary tests pass
- `uv run pytest` passes
- Skill loads in Claude Code (manual verification)

---

## Milestones

| Milestone | Stories | Gate |
|-----------|---------|------|
| M1: Knowledge ready | S31.1 | Files exist, content complete |
| M2: Skill functional | S31.2 | Command created, references valid |
| M3: Integrated | S31.3 | Docs updated, tests pass, E2E verified |
