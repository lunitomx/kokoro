---
epic_id: "E33"
title: "Meta Delivery Gates — Thresholds para decisiones de ads"
status: "Planned"
---

# Scope: E33 — Meta Delivery Gates

## Objective

Cerrar el knowledge gap que permite a Kokoro recomendar apagar ads en fase de
exploracion. Crear knowledge file de delivery system, actualizar knowledge de
ads, y agregar gate de learning phase al skill /kokoro-ads.

## In Scope

### S33.1 — Knowledge: Meta Delivery System (M)
- Nuevo knowledge file: `kokoro-meta-delivery-system.md`
- Fases del ad delivery (exploration → learning → optimization)
- Thresholds oficiales de Meta (50 conv/7d standard, 10 conv/3d Purchase)
- Thresholds de media buyers (hard kill 3x CPA, soft pause 72h, min 5 dias)
- Como Andromeda/GEM/Lattice interactuan con diversidad de creativos
- Resets que reinician learning phase
- Budget minimo por ad set (5x CPA target/dia)
- Instalar en ambos mirrors

### S33.2 — Update: kokoro-ads-meta.md (S)
- Agregar seccion "Thresholds de Decision" al knowledge file existente
- Tabla de cuando apagar/pausar/esperar basada en fase + metricas
- Regla explicita: nunca recomendar apagar sin verificar fase de learning
- Instalar en ambos mirrors

### S33.3 — Gate: /kokoro-ads learning phase check (S)
- Agregar gate al skill /kokoro-ads: antes de recomendar on/off, verificar
  impresiones, spend, tiempo activo, y conversiones vs thresholds
- Si el ad esta en learning → recomendar esperar, no apagar
- Referenciar kokoro-meta-delivery-system.md como knowledge source
- Instalar en ambos mirrors

## Out of Scope

- Modificar /kokoro-creative-review (no hace recomendaciones de on/off)
- Crear herramienta automatizada de monitoreo de ads
- Integrar con API de Meta para leer fase de learning en tiempo real
- Modificar /kokoro-analytics (consulta metricas, no recomienda acciones)

## Planned Stories

| ID | Name | Size | Dependencies |
|----|------|------|-------------|
| S33.1 | Knowledge: Meta Delivery System | M | None |
| S33.2 | Update: kokoro-ads-meta.md thresholds | S | S33.1 |
| S33.3 | Gate: /kokoro-ads learning phase check | S | S33.2 |

## Done Criteria

- [x] Knowledge file con delivery system completo instalado
- [ ] kokoro-ads-meta.md tiene seccion de thresholds
- [ ] /kokoro-ads tiene gate de learning phase antes de recomendar on/off
- [ ] El escenario del issue #1 no se repite (ad con 283 impresiones NO se recomienda apagar)
- [ ] Verificacion completa

---

## Implementation Plan

### Sequencing Strategy: Knowledge → Update → Gate

Lineal. El gate necesita el knowledge file para referenciar, y el update
establece los thresholds que el gate aplica.

### Story Sequence

| # | ID | Name | Size | Depends On | Rationale | Status |
|---|-----|------|------|------------|-----------|--------|
| 1 | S33.1 | Knowledge: Meta Delivery System | M | — | Fundacion. Sin knowledge file no hay thresholds que referenciar. | complete |
| 2 | S33.2 | Update: kokoro-ads-meta.md | S | S33.1 | Agrega thresholds al knowledge existente. | pending |
| 3 | S33.3 | Gate: /kokoro-ads learning check | S | S33.2 | Core fix. Agrega el gate que previene el bug. | pending |

### Critical Path

```
S33.1 (knowledge) → S33.2 (update) → S33.3 (gate)
```

### Milestones

#### M1: Delivery System Documentado (after S33.1)
- [x] Knowledge file con fases, thresholds, y mecanica de los 4 sistemas
- **Demo:** Leer el knowledge file y verificar que un humano puede evaluar
  si un ad esta en learning phase solo con esa referencia.

#### M2: Thresholds Integrados (after S33.2)
- [ ] kokoro-ads-meta.md tiene tabla de decision on/off
- **Demo:** Consultar thresholds para el caso del issue (283 imp, $79, 0 conv)
  y confirmar que la respuesta es "esperar".

#### M3: Epic Complete (after S33.3)
- [ ] /kokoro-ads tiene gate funcional
- **Demo:** Simular el escenario del issue y confirmar que Kokoro recomienda
  esperar en vez de apagar.
