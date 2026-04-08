---
epic_id: "E32"
title: "Kokoro Landing — Auditoria estrategica de landing pages"
status: "Scoped"
---

# Scope: E32 — Kokoro Landing

## Objective

Crear `/kokoro-landing` — un skill que audita landing pages contra la metodologia
Lean Landing Page de Eduardo Munoz Luna, evaluando estructura de decision, calidad
de copy y adherencia a los 5 principios fundamentales.

## In Scope

### S32.1 — Knowledge file: Lean Landing Page
- Extraer y estructurar la metodologia completa del PDF + transcripcion
- Los 5 principios fundamentales con criterios verificables
- Los 9 bloques del esqueleto con reglas de oro por bloque
- Anti-patrones (lo que NO es una Lean Landing Page)
- Metricas de referencia
- Instalar en ambos mirrors (extension/ y .claude/knowledge/)

### S32.2 — Skill command: /kokoro-landing
- Recibir URL (via WebFetch) o HTML pegado
- Detectar y mapear secciones contra los 9 bloques
- Evaluar copy bloque por bloque contra reglas de oro
- Scorecard de los 5 principios (presente/ausente/parcial + diagnostico)
- Rewrite suggestions en voz Eduardo
- Integracion opcional con /kokoro-audit para diagnostico tecnico
- Output estructurado: mapa de bloques, scorecard, recomendaciones priorizadas

### S32.3 — Tests y verificacion
- Tests del skill con landing pages de ejemplo
- Verificacion de vocabulario Kokoro en outputs
- Validacion de integracion con kokoro-audit

## Out of Scope

- Generacion de landing pages (es /kokoro-launch)
- Evaluacion de diseno visual o UX
- Scraping de SPAs con JavaScript rendering
- Medicion de conversion real o integracion con analytics
- Modificacion de /kokoro-audit existente

## Planned Stories

| ID | Name | Size | Dependencies |
|----|------|------|-------------|
| S32.1 | Knowledge: Lean Landing Page | S | None |
| S32.2 | Skill: /kokoro-landing | M | S32.1 |
| S32.3 | Tests + verificacion | S | S32.2 |

## Done Criteria

- [ ] `/kokoro-landing` disponible como skill en ambos mirrors
- [ ] Knowledge file con metodologia completa instalado
- [ ] Skill produce analisis estructurado de landing pages reales
- [ ] Scorecard cubre los 5 principios con diagnostico accionable
- [ ] Voz Eduardo presente en rewrites y sugerencias
- [ ] Tests pasan
