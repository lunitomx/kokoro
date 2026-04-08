---
epic_id: "E32"
title: "Design: Kokoro Landing"
status: "Designed"
---

# Design: E32 — Kokoro Landing

## Gemba (Current State)

### What exists

- `/kokoro-audit` — audita salud **tecnica** (SEO, performance, a11y, best
  practices). Traduce metricas tecnicas a lenguaje de negocio. NO lee copy,
  NO evalua estructura de decision, NO conoce la metodologia Lean Landing Page.
- `/kokoro-launch` — **genera** copies, scripts y landing pages. No audita
  landing existentes.
- PDF "Guia Lean Landing Page 2026 v2.0" — la metodologia completa pero como
  documento estatico, no como herramienta ejecutable.
- Transcripcion de clase (sesion 56) — contexto de aplicacion real con
  emprendedores B2B.

### Gap

No existe una herramienta que lea una landing page y la evalue como **secuencia
de decision** — que bloques tiene, cuales faltan, si el copy califica o
convence, si el flujo sigue el orden correcto.

### Pattern established

Kokoro skills siguen un patron consolidado:
- **Command file**: `extension/.claude/commands/kokoro-{name}.md`
- **Knowledge file(s)**: `extension/.claude/knowledge/kokoro-{name}.md`
- **Mirror**: copiado identico a `.claude/commands/` y `.claude/knowledge/`
- **Estructura del command**: titulo > tagline > cita Eduardo > contexto >
  diferencia con otros skills > resolucion de invitado > instrucciones paso
  a paso > output estructurado

No se necesitan ADRs — el patron esta establecido desde E31.

## Target Components

### 1. Knowledge file: `kokoro-lean-landing.md`

Referencia completa de la metodologia. Estructura:

```
# Lean Landing Page — Referencia para /kokoro-landing
> Cita de Eduardo

## Filosofia Base
- No es plantilla estetica, es secuencia de decision
- No busca convencer, busca calificar
- Anti-patrones (NO brochure, NO blog, NO institucional)

## Los 5 Principios Fundamentales
1. Claridad en 10-20 segundos — criterios verificables
2. Riesgo invertido — criterios verificables
3. Filtro de prospectos (Quality > Volume) — criterios verificables
4. Proceso visible — criterios verificables
5. CTA unico y persistente — criterios verificables

## Los 9 Bloques (Esqueleto de Decision)
Por bloque: objetivo, regla de oro, que evaluar, anti-patron, ejemplo

01. HERO (Trigger + PUV + CTA)
02. PAINS (Dolor actual)
03. INERCIAS (Bloqueos)
04. ASI FUNCIONA (Proceso visible)
05. MAFIA OFFER (Riesgo invertido)
06. NO ES PARA TI SI... (Filtro)
07. FRICTIONS (Prueba social)
08. QUID PRO QUO (Intercambio)
09. CTA PERSISTENTE

## Metricas de Referencia
- Tasa de conversion a cita: 25%
- Calidad del lead (ICP Match): 90% High Fit
- Show-up rate: 80%
- Tiempo a decision: 7 dias

## Uso Recomendado
Consultoria B2B, SaaS Enterprise, Real Estate Premium, Educacion Ejecutiva
```

**Fuentes**: PDF v2.0 (estructura y principios) + transcripcion sesion 56
(contexto de aplicacion, ejemplos reales, matices que Eduardo explica en vivo).

### 2. Skill command: `kokoro-landing.md`

```
# /kokoro-landing — Auditoria Estrategica de Landing Pages

> Herramienta transversal: Evaluacion de landing pages
> Aplica en Fase 3 (Germinar) y Fase 4 (Cosechar)

> "Tu pagina no tiene que convencer a nadie. Tiene que calificar
> a quien merece estar en tu mesa."

## Contexto
Lee: kokoro-lean-landing.md
Complementa: /kokoro-audit (tecnico), /kokoro-launch (genera)

## Diferencia con otros skills
- /kokoro-audit evalua salud TECNICA → este evalua ESTRATEGIA de conversion
- /kokoro-launch GENERA landing pages → este AUDITA las existentes
- /kokoro-ads genera copy para Meta → este evalua copy EN la landing

## Resolucion de invitado (patron estandar)

## Instrucciones para la sesion

### Paso 1 — Obtener la landing
- URL → WebFetch para obtener HTML
- HTML pegado directamente
- Si el fetch falla (SPA): pedir HTML o screenshot

### Paso 2 — Mapeo de bloques (9 bloques)
Leer el HTML/texto y mapear cada seccion contra los 9 bloques.
Output: tabla de bloques (presente/ausente/parcial + ubicacion)

### Paso 3 — Evaluacion bloque por bloque
Para cada bloque presente, evaluar contra reglas de oro:
- Score (fuerte/parcial/debil)
- Que dice el copy actual
- Que deberia decir (rewrite en voz Eduardo)
- Diagnostico especifico

### Paso 4 — Scorecard de 5 principios
Cada principio: cumple/parcial/no cumple + evidencia + recomendacion

### Paso 5 — Diagnostico integrado
- Bloques faltantes priorizados
- Bloques en desorden (vs flujo recomendado)
- Top 3 mejoras de mayor impacto
- Oferta de complementar con /kokoro-audit si quieren el lado tecnico

## Output estructurado
Mapa de bloques → Scorecard → Recomendaciones priorizadas → Rewrites
```

## Key Contracts

### Input

El skill acepta 3 formas de input:
1. **URL** → se usa WebFetch para obtener el HTML
2. **HTML pegado** → el usuario copia el source
3. **Sin pagina** → modo consultivo: evalua un copy/estructura descrita

### Output

Siempre estructurado en 4 secciones:

```
## Mapa de Bloques
| # | Bloque | Estado | Ubicacion/Nota |
|---|--------|--------|----------------|

## Scorecard de Principios
| Principio | Estado | Evidencia |
|-----------|--------|-----------|

## Diagnostico por Bloque
### 01. HERO
Score: fuerte/parcial/debil
Copy actual: "..."
Rewrite sugerido: "..."
Nota: ...

## Top 3 Acciones Inmediatas
1. ...
2. ...
3. ...
```

### Integration with /kokoro-audit

No dependency — /kokoro-landing funciona independiente. Al final del analisis,
ofrece: "Si quieres que tambien revisemos la salud tecnica de tu pagina
(velocidad, SEO, accesibilidad), podemos complementar con /kokoro-audit."

## Stories (Refined)

### S32.1 — Knowledge: Lean Landing Page (S)

**Input**: PDF v2.0 + transcripcion sesion 56
**Output**: `extension/.claude/knowledge/kokoro-lean-landing.md` + mirror
**Criterio**: Los 5 principios con criterios verificables, los 9 bloques con
reglas de oro, anti-patrones, metricas. Formato consistente con knowledge
files existentes (kokoro-meta-ai-ecosystem.md como referencia).

### S32.2 — Skill: /kokoro-landing (M)

**Input**: Knowledge file de S32.1 + patron de kokoro-creative-review.md
**Output**: `extension/.claude/commands/kokoro-landing.md` + mirror
**Criterio**: Recibe URL o HTML, produce mapa de bloques + scorecard +
rewrites. Voz Eduardo. Resolucion de invitado. Integracion sugerida con
/kokoro-audit.

### S32.3 — Tests + verificacion (S)

**Input**: Skill + knowledge completados
**Output**: Tests en `tests/skills/` + verificacion manual
**Criterio**: Vocabulario Kokoro verificado. Output estructurado. Integracion
con /kokoro-audit funcional. Landing de ejemplo analizada correctamente.

## Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| WebFetch no captura SPAs (JS-rendered) | Medium | Low | Fallback a HTML pegado o screenshot. Documentar limitacion. |
| Transcripcion tiene ruido (es clase en vivo) | Low | Low | Usar PDF como fuente primaria, transcripcion solo para matices y ejemplos. |
| Overlap con /kokoro-audit confunde al usuario | Low | Medium | Diferencia explicita en contexto del skill + sugerencia al final, no al inicio. |

## Dependencies

- Ninguna externa. PDF y transcripcion ya estan en el repo.
- Patron de skills Kokoro ya establecido (E31).
