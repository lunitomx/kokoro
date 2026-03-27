---
epic_id: "E13"
title: "Kokoro Web Quality — Skills de Addy Osmani integrados"
status: "draft"
created: "2026-03-26"
---

# Epic Brief: E13 — Web Quality Skills (Addy Osmani)

## Hypothesis
For Eduardo's clients who need site health diagnostics,
the Kokoro Web Quality integration wraps Addy Osmani's web-quality-skills
into the Kokoro ecosystem with proper credit and Kokoro voice,
so that entrepreneurs can audit their sites without technical knowledge.
Unlike running the skills directly (requires understanding of SEO/performance terminology),
our solution translates results into actionable recommendations in Eduardo's voice.

## Success Metrics
- **Leading:** Un emprendedor corre auditoría de su sitio sin ayuda técnica
- **Lagging:** 3+ sitios de clientes auditados con recomendaciones accionables

## Appetite
S — 2-3 stories

## Scope Boundaries
### In (MUST)
- /kokoro-audit skill que wrappea los web-quality-skills existentes
- Crédito explícito a Addy Osmani y web-quality-skills
- Resultados traducidos a lenguaje de emprendedor (no técnico)
- Integración con client graph (auditar sitio del cliente)

### In (SHOULD)
- Priorización de hallazgos por impacto en negocio
- Comparación con competidores del cliente

### No-Gos
- No reescribir los skills de Addy Osmani — wrapping con crédito
- No reemplazar herramientas especializadas (Lighthouse, PageSpeed)
- No implementar fixes automáticos — solo diagnosticar y recomendar

### Rabbit Holes
- Construir un Lighthouse propio — usar el existente
- Dashboard de métricas históricas — auditoría puntual es suficiente
