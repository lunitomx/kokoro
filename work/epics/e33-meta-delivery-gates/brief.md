---
epic_id: "E33"
title: "Meta Delivery Gates — Thresholds para decisiones de ads"
status: "Scoped"
origin: "lunitomx/kokoro#1"
---

# Brief: E33 — Meta Delivery Gates

## Problem

Kokoro recomendo apagar un ad con $79 MXN de gasto y 283 impresiones porque
tenia 0 conversiones. El ad estaba en fase de exploracion — Andromeda/GEM no
habian tenido oportunidad de optimizar. Recomendar apagar durante exploration
es un error de timing, no de diagnostico.

Causa raiz: knowledge gap. Kokoro analiza datos de ads como tabla estatica
("cero conversiones = malo") sin modelar las fases de delivery de Meta
(exploration → learning → optimization).

## Origin

GitHub issue: lunitomx/kokoro#1

## Desired Outcome

Kokoro nunca recomienda apagar un ad que no ha salido de learning phase.
Cuando analiza performance de ads, aplica thresholds basados en evidencia
antes de hacer recomendaciones tacticas.
