---
epic_id: "E31"
title: "Kokoro Creative Review — Retroalimentacion de creativos bajo Meta AI"
status: "In Progress"
created: "2026-04-07"
---

# Scope: E31 — Kokoro Creative Review

## Objective

Crear `/kokoro-creative-review`, un skill que recibe una imagen o creativo del
emprendedor y lo analiza bajo los criterios del ecosistema de IA de Meta Ads
(GEM, Andromeda, Lattice, Sequence Learning), dando retroalimentacion accionable
con la voz de Eduardo.

## Value

Hoy el emprendedor crea un creativo y lo sube a Meta sin saber como lo evaluara
el algoritmo. Este skill cierra esa brecha: antes de invertir un peso en pauta,
el emprendedor recibe un analisis que le dice como ve Meta su creativo, que
audiencias lo veran, y que ajustar para maximizar rendimiento.

Completa el ciclo: `/kokoro-creative` genera → `/kokoro-creative-review` evalua
→ `/kokoro-ads` pauta.

## In Scope (MUST)

- Skill command `/kokoro-creative-review` que recibe imagen via Read tool (multimodal)
- Knowledge file consolidado con los 4 sistemas de Meta AI (GEM, Andromeda, Lattice, Sequence Learning)
- Knowledge file con la Matriz de Diversificacion Creativa (16 deseos x 5 niveles)
- Analisis estructurado: composicion visual, hook clarity, cluster prediction, diversification score
- Sugerencias de mejora con voz de Eduardo
- Mirror en extension/.claude/ para distribucion

## In Scope (SHOULD)

- Referencia cruzada con kokoro-ads (targeting suggestions basadas en analisis)
- Scoring visual (1-10) por dimension

## Out of Scope

- Integracion con Meta Ads API para validar predicciones en tiempo real
- Generacion de creativos (eso es kokoro-creative)
- Analisis de video en movimiento (solo frames/thumbnails)
- Modelo predictivo real — la prediccion es heuristica informada por documentacion de Meta

## Stories

| ID | Story | Size | Depends on |
|----|-------|------|------------|
| S31.1 | Crear knowledge files (Meta AI ecosystem + Matriz Creativa) | S | — |
| S31.2 | Crear skill command /kokoro-creative-review | M | S31.1 |
| S31.3 | Mirror a extension/, tests de vocabulario, verificacion end-to-end | S | S31.2 |

## Done Criteria

1. `/kokoro-creative-review` existe en ambos mirrors (.claude/ y extension/.claude/)
2. Knowledge files cubren GEM, Andromeda, Lattice, Sequence Learning, Diversificacion
3. El skill puede recibir una imagen y generar analisis estructurado
4. Tests de vocabulario pasan (invitado, inversion, creacion — no precio, producto, cliente)
5. `uv run pytest` pasa

## Risks

| Risk | L | I | Mitigation |
|------|---|---|------------|
| Analisis superficial sin datos reales | M | M | Knowledge files densos + heuristicas bien documentadas |
| Creativo no legible por Claude | L | M | Guia al usuario sobre formatos soportados |
| Overlap con kokoro-creative | L | L | Scope claro: review ANALIZA, creative GENERA |
