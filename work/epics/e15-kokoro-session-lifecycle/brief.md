---
epic_id: "E15"
title: "Kokoro Session Lifecycle"
status: "proposed"
---

# Brief: E15 — Kokoro Session Lifecycle

## Hypothesis

Si Kokoro tiene un ciclo de sesion propio (abrir + cerrar) para el trabajo
con invitados, Eduardo dejara de repetir contexto entre sesiones y los
hallazgos se acumularan automaticamente — mejorando la calidad de cada
interaccion con el tiempo.

## Success Metrics

- /kokoro-open carga historial del invitado y propone foco en <30 segundos
- /kokoro-close persiste hallazgos sin que Eduardo tenga que dictar un resumen
- Session log acumulativo visible al abrir siguiente sesion
- Skills existentes (ads, creative) registran actividad automaticamente

## Appetite

4 stories (S, S, S, M). Estimado: 2-3 sesiones.

## Rabbit Holes

- Construir analytics sobre sesiones (premature — primero acumular datos)
- Dashboard visual de progreso por invitado (no es CLI, fuera de scope)
- Migrar kokoro-session existente (funciona bien, dejarlo)
