---
epic_id: "E10"
title: "Client Resolution en todos los skills + MEMORY.md auto-update"
status: "draft"
created: "2026-03-26"
---

# Epic Brief: E10 — Client Resolution universal + Memory auto-update

## Hypothesis
For Eduardo who uses Kokoro skills across multiple clients,
the universal client resolution is a standard preamble in every skill
that reads the client graph before starting any exercise,
so that every skill knows quién es el cliente sin que Eduardo lo re-explique.
Unlike the current state (solo kokoro-ads tiene client resolution),
our solution integra la resolución en los 16 skills restantes y
automatiza el update de MEMORY.md cuando Kokoro detecta cambios.

## Success Metrics
- **Leading:** Cualquier skill de Kokoro reconoce al cliente al invocarse
- **Lagging:** Eduardo nunca tiene que re-explicar quién es un cliente

## Appetite
M — 3-4 stories

## Scope Boundaries
### In (MUST)
- Agregar sección "Resolución de cliente" a los 16 skills que no la tienen
- Mirrors en extension/ sincronizados
- MEMORY.md auto-update: cuando se crea/modifica un cliente, actualizar el índice
- Tests existentes siguen pasando

### In (SHOULD)
- Template reutilizable para la sección (no copy-paste 16 veces)
- Auto-detect client from working directory

### No-Gos
- No reescribir los skills — solo agregar la sección de resolución
- No modificar la lógica de los ejercicios

### Rabbit Holes
- Personalizar la resolución por tipo de skill — la misma sección funciona para todos
