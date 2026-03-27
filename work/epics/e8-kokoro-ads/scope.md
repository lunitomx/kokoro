# Epic E8: Kokoro Ads — Scope

> **Status:** COMPLETE
> **Created:** 2026-03-26

## Objective

Crear el skill `/kokoro-ads` que automatice la generacion de contenido para
campanas de Meta Ads siguiendo el proceso validado: describir creativo → leer
contexto del cliente → identificar publico → generar entregables en .txt plano.

**Value:** Eduardo puede crear campanas completas sin re-explicar el proceso
cada sesion. Los entregables salen listos para copiar/pegar en Meta Ads Manager.

## Stories (2 estimated)

| ID | Story | Size | Status | Description |
|----|-------|:----:|:------:|-------------|
| S8.1 | Skill kokoro-ads | M | Complete | Command file + knowledge file + extension sync |
| S8.2 | Tests y validacion | S | Complete | Tests de estructura + validacion con caso real |

**Total:** 2 stories

## Scope

**In scope (MUST):**
- Command file `.claude/commands/kokoro-ads.md` con flujo completo
- Knowledge file `.claude/knowledge/kokoro-ads-meta.md` con specs de Meta Ads
- Extension sync (`extension/.claude/commands/` y `extension/.claude/knowledge/`)
- Proceso: imagen → descripcion del creativo → lectura contexto cliente → publico → copy
- Entregables: 5 titulos + 5 descripciones + plantilla WhatsApp + audiencia Advantage+
- Output en formato .txt plano (no markdown) — listo para copiar a Meta Ads Manager
- Guardado automatico en carpeta de campanas del cliente
- Vocabulario Kokoro (inversion, creacion, invitado — nunca precio, producto, cliente)

**In scope (SHOULD):**
- Nomenclatura automatica (creativo-01, creativo-02...)
- Lectura del repo del cliente para datos reales (inventario, precios)
- Soporte multiples creativos en una sesion

**Out of scope:**
- Integracion con Meta API → parking lot
- Google Ads → parking lot (kokoro-ads-google futuro)
- Analisis de rendimiento de campanas → parking lot (kokoro-ads-analytics futuro)
- Generacion de creativos visuales → fuera de Kokoro

## Done Criteria

**Per story:**
- [x] Code with proper structure
- [x] Tests passing
- [x] Quality checks pass (ruff, pyright)

**Epic complete:**
- [x] All stories complete (S8.1-S8.2)
- [x] /kokoro-ads genera entregables completos para 1 creativo
- [x] Output .txt copiable directo a Meta Ads Manager sin problemas de formato
- [x] Tests existentes siguen pasando (no romper skills existentes)
- [x] kokoro-ads registrado en VALID_COMMANDS y EXISTING_COMMANDS
- [x] Epic retrospective done
- [x] Merged to main

## Dependencies

```
S8.1 (skill + knowledge)
  |
S8.2 (tests + validacion)
```

**External:** Ninguna

## Architecture

No ADRs necesarios — sigue el patron exacto de los 16 skills existentes:
- Command file en `.claude/commands/kokoro-ads.md`
- Knowledge file en `.claude/knowledge/kokoro-ads-meta.md`
- Mirror en `extension/.claude/`
- Registro en `COACHING_SKILLS`, `VALID_COMMANDS`, `EXISTING_COMMANDS` en tests

**Diferencia clave vs skills existentes:**
- El output template NO es markdown con tablas — es un bloque .txt plano
- El skill genera archivos .txt en el filesystem (los otros skills generan output inline)
- Necesita leer imagen del usuario (creativo) como input

## Risks

| Risk | L/I | Mitigation |
|------|:---:|------------|
| Tests de estructura esperan markdown tables en output template — .txt no tiene tables | H/M | Adaptar test o crear output template hibrido (markdown wrapper + txt content) |
| Skill no puede "leer" imagen directamente — depende de Claude Code multimodal | L/H | El skill instruye al modelo a pedir la imagen y describirla, no la procesa el skill |

## Implementation Plan

> Added by `/rai-epic-plan` — 2026-03-26

### Story Sequence

| Order | Story | Size | Dependencies | Milestone | Rationale |
|:-----:|-------|:----:|--------------|-----------|-----------|
| 1 | S8.1 — Skill kokoro-ads | M | None | M1 | Quick win: el skill ES el producto. Sin skill no hay nada que testear |
| 2 | S8.2 — Tests y validacion | S | S8.1 | M2 | Valida estructura + caso real con Konecta Park brokers |

**Secuencia:** Lineal, sin oportunidades de paralelismo (2 stories con dependencia directa).

**Estrategia:** Quick win. S8.1 entrega valor inmediato — Eduardo puede usar `/kokoro-ads` desde que se complete. S8.2 asegura calidad y no-regresion.

### Milestones

| Milestone | Stories | Success Criteria |
|-----------|---------|------------------|
| **M1: Skill funcional** | S8.1 | `/kokoro-ads` genera entregables completos para 1 creativo. Output .txt copiable |
| **M2: Epic complete** | S8.1 + S8.2 | Tests pasan. kokoro-ads en VALID_COMMANDS. Tests existentes no rotos. Retro done |

### Progress Tracking

| Story | Size | Status | Actual | Notes |
|-------|:----:|:------:|:------:|-------|
| S8.1 — Skill kokoro-ads | M | Complete | M | |
| S8.2 — Tests y validacion | S | Complete | S | |

### Sequencing Risks

| Risk | L/I | Mitigation |
|------|:---:|------------|
| Output template hibrido (markdown wrapper + txt) puede confundir tests existentes | M/M | S8.2 actualiza COACHING_SKILLS y adapta assertions para el nuevo patron |
| Skill demasiado largo por cubrir todos los entregables (copy + whatsapp + audiencia) | M/L | Estructura modular en el command file — secciones claras por entregable |

## Parking Lot

- Integracion Meta API → futuro skill o MCP server
- Google Ads copy → kokoro-ads-google
- Analytics de campanas → kokoro-ads-analytics
- Dashboard de campanas → no necesario, carpetas .txt suficientes
