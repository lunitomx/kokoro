---
epic_id: "E32"
title: "Kokoro Landing — Auditoria estrategica de landing pages"
status: "Planned"
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

---

## Implementation Plan

### Sequencing Strategy: Quick Wins → Build → Verify

Epic lineal de 3 stories con dependencia en cadena. No hay paralelismo posible
— el skill necesita el knowledge file, y los tests necesitan el skill.

Estrategia: quick wins primero. S32.1 es autocontenido, de bajo riesgo y
entrega valor inmediato (la metodologia queda documentada como referencia
reutilizable por otros skills como /kokoro-launch).

### Story Sequence

| # | ID | Name | Size | Depends On | Rationale | Status |
|---|-----|------|------|------------|-----------|--------|
| 1 | S32.1 | Knowledge: Lean Landing Page | S | — | Fundacion. Sin knowledge file el skill no tiene contra que evaluar. Ademas, es reutilizable por /kokoro-launch. | complete |
| 2 | S32.2 | Skill: /kokoro-landing | M | S32.1 | Core delivery. Consume el knowledge file. Patron ya establecido en E31. | complete |
| 3 | S32.3 | Tests + verificacion | S | S32.2 | Validacion. Verifica vocabulario, estructura de output, e integracion con /kokoro-audit. | pending |

### Critical Path

```
S32.1 (knowledge) → S32.2 (skill) → S32.3 (tests)
```

Lineal. No hay caminos alternativos ni work streams paralelos.
El riesgo principal es S32.1 — si la extraccion del PDF + transcripcion
no captura bien la metodologia, todo lo demas hereda ese error.

### Milestones

#### M1: Metodologia Documentada (after S32.1)
- [ ] Knowledge file instalado en ambos mirrors
- [ ] 5 principios con criterios verificables
- [ ] 9 bloques con reglas de oro
- [ ] Anti-patrones documentados
- **Demo:** Leer el knowledge file y verificar que un humano puede auditar
  una landing manualmente solo con esa referencia.

#### M2: Skill Funcional (after S32.2)
- [ ] Skill recibe URL y produce analisis estructurado
- [ ] Mapa de bloques + Scorecard + Rewrites generados
- [ ] Voz Eduardo presente en output
- **Demo:** Auditar una landing page real (ej: la de Luvexi del transcript)
  y producir diagnostico accionable.

#### M3: Epic Complete (after S32.3)
- [ ] Tests pasan
- [ ] Vocabulario Kokoro verificado en outputs
- [ ] Integracion con /kokoro-audit validada
- **Demo:** Ciclo completo: `/kokoro-landing` + `/kokoro-audit` sobre la
  misma URL, diagnostico estrategico + tecnico complementarios.

### Sequencing Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| PDF no se parsea limpio (es generado por NotebookLM) | M1 delayed | Ya lo leimos — las slides son claras. Transcripcion como complemento, no dependencia. |
| Skill demasiado largo (9 bloques x evaluacion detallada) | M2 scope creep | Mantener output conciso: tabla + top 3 acciones. Detalle solo si el usuario pide profundizar. |
| WebFetch no captura contenido de algunas landings | M2 friction | Fallback documentado: pedir HTML o screenshot. No invertir en scraping. |
