---
epic_id: "E18"
title: "Kokoro Video Editor — De video crudo a contenido publicable"
status: "planned"
---

# Scope: E18 — Kokoro Video Editor

## Objective

Pipeline que toma video crudo (workshops, entrevistas, lives) y produce
contenido publicable: shorts de 30-60s, clips con overlays de texto,
y video final con intro/outro. El flujo completo:

```
video crudo --> transcribir --> identificar cortes --> generar graficos --> exportar video final + shorts
```

Reutiliza skills existentes (kokoro-listen para transcripcion, kokoro-creative
para graficos) y evalua OpenShorts como base para generacion automatizada
de shorts.

## Value

- Eduardo deja de pasar horas editando video manualmente
- Un video de 30 minutos produce 5+ shorts publicables en minutos
- El contenido de workshops y lives se reutiliza sistematicamente
- Pipeline reproducible: mismo proceso para cada video nuevo

## Architecture Decisions

### AD-1: OpenShorts como base para generacion de shorts (evaluar, no construir desde cero)

Evaluar github.com/mutonby/openshorts antes de implementar logica propia.
Si cubre >70% de las necesidades, integrarlo. Si no, tomar las ideas
utiles y construir lo minimo necesario con ffmpeg directo.

Rationale: No reinventar la rueda. Pero tampoco casarse con una
dependencia que no se mantenga.

### AD-2: ffmpeg para toda manipulacion de video (sin herramientas propietarias)

Toda operacion de video (cortar, overlay, render, reformat) usa ffmpeg.
No moviepy, no opencv para edicion, no herramientas de pago.

Rationale: ffmpeg es el estandar de la industria, corre en cualquier
maquina, y Eduardo ya lo tiene instalado. Sin licencias, sin sorpresas.

### AD-3: kokoro-listen para transcripcion (ya existe, reutilizar)

La transcripcion usa /kokoro-listen que ya integra yt-dlp + Whisper API.
No duplicar logica de descarga ni transcripcion.

Rationale: DRY. kokoro-listen ya maneja formatos de audio, timestamps,
y segmentacion. Solo necesitamos consumir su output.

### AD-4: kokoro-creative para graficos de overlay (Gemini API, ya existe)

Los graficos (thumbnails, lower-thirds, titulos) se generan con
/kokoro-creative que ya usa Gemini API. El pipeline le pasa contexto
del video y recibe imagenes listas para overlay.

Rationale: Reutilizar infraestructura existente. kokoro-creative ya
tiene el estilo visual de Eduardo calibrado.

### AD-5: Dos fases — Phase 1 = cortes + shorts, Phase 2 = graficos + polish

Phase 1 (S18.1-S18.3 + S18.6): Evaluar OpenShorts, identificar cortes,
extraer segmentos. Valor inmediato: shorts publicables.

Phase 2 (S18.4-S18.5): Overlays de texto, render final con intro/outro.
Valor incremental: contenido pulido.

Rationale: Phase 1 entrega valor en 3-4 stories. Phase 2 pule sin
bloquear el uso del pipeline.

## Stories

- [x] S18.1 — Evaluar OpenShorts: clonar, probar, documentar capacidades vs gaps (S) ✓
- [ ] S18.2 — /kokoro-cuts: identificar mejores momentos del transcript para shorts 30-60s (M)
- [x] S18.3 — /kokoro-shorts: extraer segmentos de video con ffmpeg segun cortes (M) ✓
- [x] S18.4 — /kokoro-overlay: generar overlays de texto/captions desde transcript con ffmpeg (M) ✓
- [x] S18.5 — /kokoro-render: ensamblar video final con overlays + intro/outro (M) ✓
- [ ] S18.6 — Test de integracion end-to-end con video real (S)

## Story Details

### S18.1 — Evaluar OpenShorts (S)

Clonar github.com/mutonby/openshorts, ejecutar con un video de prueba,
y documentar:
1. Que hace bien (deteccion de momentos, cortes, formato vertical)
2. Que le falta (integracion con transcript, estilo visual, calidad)
3. Decision: integrar, fork, o solo inspiracion

**Dependencies:** None
**Size:** S

### S18.2 — /kokoro-cuts (M)

Skill que recibe un transcript (output de kokoro-listen) y produce una
lista ordenada de los mejores momentos para shorts:

1. Analizar transcript por densidad de contenido, frases impactantes,
   cambios de tema, y momentos de alta energia
2. Proponer 5-10 cortes con timestamps inicio/fin (30-60s cada uno)
3. Incluir titulo sugerido y hook para cada corte
4. Permitir que Eduardo seleccione/descarte/ajuste antes de continuar

**Dependencies:** kokoro-listen (existente)
**Size:** M

### S18.3 — /kokoro-shorts (M)

Skill que toma la lista de cortes aprobados y extrae los segmentos:

1. Usar ffmpeg para cortar video en los timestamps especificados
2. Opcionalmente reformatear a 9:16 (vertical) para shorts/reels
3. Aplicar fade in/out basico
4. Exportar cada segmento como archivo independiente

**Dependencies:** S18.2
**Size:** M

### S18.4 — /kokoro-overlay (M)

Skill que genera overlays de texto sobre los shorts:

1. Tomar segmento de transcript correspondiente al corte
2. Generar captions sincronizados (subtitulos con timestamps)
3. Aplicar estilo visual consistente (fuente, color, posicion)
4. Renderizar con ffmpeg drawtext o ASS subtitles

**Dependencies:** S18.3
**Size:** M

### S18.5 — /kokoro-render (M)

Skill que ensambla el video final:

1. Agregar intro/outro (templates predefinidos)
2. Componer overlays + video base
3. Normalizar audio (volumen consistente)
4. Exportar en formatos apropiados (MP4 H.264 para compatibilidad)

**Dependencies:** S18.4
**Size:** M

### S18.6 — Test de integracion end-to-end (S)

Pipeline completo con video real:

1. Video crudo de Eduardo (workshop o live)
2. kokoro-listen transcribe
3. kokoro-cuts identifica mejores momentos
4. kokoro-shorts extrae segmentos
5. kokoro-overlay agrega captions
6. kokoro-render produce video final
7. Verificar calidad del output manualmente

**Dependencies:** S18.5
**Size:** S

## Dependency Graph

```
S18.1 (evaluar OpenShorts) ──────────────────────────────────────┐
                                                                  │
kokoro-listen (existente) ──> S18.2 (cuts) ──> S18.3 (shorts) ──> S18.4 (overlay) ──> S18.5 (render) ──> S18.6 (e2e test)
```

S18.1 es independiente y puede ejecutarse en paralelo con S18.2.
Sus hallazgos pueden influir en la implementacion de S18.3+.

## Scope Boundaries

### In (MUST)
- Identificacion de cortes desde transcript con timestamps
- Extraccion de segmentos de video via ffmpeg
- Captions/subtitulos sincronizados sobre video
- Render final con intro/outro
- Pipeline end-to-end funcional

### In (SHOULD)
- Reformateo vertical (9:16) para shorts/reels
- Batch processing de multiples cortes
- Seleccion interactiva de cortes por Eduardo

### No-Gos
- No edicion manual frame-by-frame (esto no es un NLE)
- No generacion de video con IA (solo edicion de footage existente)
- No upload a plataformas (YouTube, TikTok, Instagram)
- No mezcla de audio ni musica de fondo
- No herramientas propietarias de video

### Rabbit Holes
- Construir un editor de video completo — ffmpeg commands son suficientes
- Speaker diarization — prematuro para Phase 1
- B-roll automatico — demasiado complejo
- Deteccion de escenas por computer vision — el transcript es suficiente
- Streaming/live editing — fuera de scope completamente

## Done Criteria

- [x] OpenShorts evaluado con decision documentada (integrar/fork/inspiracion)
- [ ] /kokoro-cuts produce lista de cortes rankeados desde un transcript
- [x] /kokoro-shorts extrae segmentos de video correctamente con ffmpeg
- [x] /kokoro-overlay genera captions sincronizados sobre video
- [x] /kokoro-render produce video final con intro/outro
- [ ] Pipeline end-to-end probado con video real de Eduardo
- [ ] Todos los tests pasan

## Risks

1. **OpenShorts no sirve** — Mitigation: evaluacion temprana (S18.1), plan B es ffmpeg puro
2. **Calidad de cortes automaticos** — Mitigation: HITL en S18.2 (Eduardo aprueba cortes antes de extraer)
3. **ffmpeg complejidad** — Mitigation: comandos simples, un paso a la vez, no pipelines complejos
4. **Tiempos de procesamiento largos** — Mitigation: Phase 1 procesa shorts (30-60s), no video completo
5. **Sincronizacion de captions** — Mitigation: kokoro-listen ya produce timestamps precisos con Whisper

## Implementation Plan

### Sequencing Strategy

Risk-first + walking skeleton: resolver incertidumbre (OpenShorts) en paralelo
con el corazon del pipeline (cuts), llegar a shorts publicables lo antes posible.

```
Stream A:  S18.1 (evaluar OpenShorts) ─────────────┐
                                                     ├─→ hallazgos informan S18.3+
Stream B:  S18.2 (cuts) ──→ S18.3 (shorts) ──→ S18.4 (overlay) ──→ S18.5 (render) ──→ S18.6 (e2e)
```

### Story Sequence

| # | Story | Size | Strategy | Rationale | Status |
|---|-------|------|----------|-----------|--------|
| 1a | S18.1 — Evaluar OpenShorts | S | Risk-first | Resolver incertidumbre antes de implementar | done |
| 1b | S18.2 — /kokoro-cuts | M | Walking skeleton | Corazon del pipeline, paralelo con S18.1 | done |
| 2 | S18.3 — /kokoro-shorts | M | Dependency-driven | Necesita S18.2 + hallazgos S18.1. Completa Phase 1 | done |
| 3 | S18.4 — /kokoro-overlay | M | Incremental value | Captions sobre shorts. Inicia Phase 2 | done |
| 4 | S18.5 — /kokoro-render | M | Dependency-driven | Video final con intro/outro | done |
| 5 | S18.6 — Test e2e | S | Integration | Pipeline completo con video real | pending |

### Milestones

#### M1: Shorts Publicables (Phase 1) — S18.1 + S18.2 + S18.3
- Eduardo va de video crudo a shorts cortados y listos para publicar
- **Criterio:** dado un video de prueba, produce al menos 3 shorts de 30-60s
- **Demo:** Eduardo ve lista de cortes sugeridos, aprueba, y recibe archivos de video
- **Status:** DONE (2026-03-28). Pipeline probado con video real. 3 shorts extraidos.
- **Hallazgo critico:** Los shorts salen en horizontal — NO son publicables en
  Reels/Shorts/TikTok sin reformat vertical (9:16). El reformat esta implementado
  en /kokoro-shorts como opcion pero no es el default. Debe ser default o al menos
  ofrecido activamente despues de cada extraccion.

#### M2: Contenido Pulido (Phase 2) — S18.4 + S18.5
- Shorts con captions estilizados + video final con intro/outro
- **Criterio:** short con subtitulos sincronizados renderizado correctamente
- **Demo:** short con captions + video final con branding de Eduardo
- **Nota:** S18.4 (overlay/captions) es el paso mas valioso de Phase 2.
  Los captions hacen que los shorts funcionen en modo silencio (80%+ de
  usuarios ven sin audio). Considerar hacer reformat vertical parte de S18.4.

#### M3: Epic Complete — S18.6
- Pipeline probado end-to-end con video real de Eduardo
- **Criterio:** done criteria del scope cumplidos al 100%
- **Nota:** El e2e DEBE producir shorts verticales con captions, no horizontales sin texto.

### Sequencing Risks

1. ~~S18.1 invalida approach de S18.3~~ — RESOLVED: verdict INSPIRATION-ONLY
2. **Captions word-level vs phrase-level** — Decision diferida a S18.4 design.
   Whisper verbose_json ya da segmentos, pero word-level requiere otro response_format.
3. ~~Video de prueba necesario desde S18.2~~ — RESOLVED: video de Eduardo usado
4. **Vertical reformat debe ser default** — Los shorts horizontales no son publicables
   en ninguna plataforma de formato corto. S18.4 o un patch a S18.3 debe resolver esto.

### Progress Log (2026-03-28)

- S18.1 DONE: OpenShorts evaluado, verdict INSPIRATION-ONLY
- S18.2 DONE: /kokoro-cuts live, probado con video real (3 cortes identificados)
- S18.3 DONE: /kokoro-shorts live, probado con video real (3 shorts extraidos con fades)
- Pipeline completo funcional: /kokoro-listen → /kokoro-cuts → /kokoro-shorts
- Costo total del pipeline test: ~$0.04 USD (2x Whisper transcription)
- S18.4 DONE: /kokoro-overlay live — captions + vertical reformat with ffmpeg drawtext
- S18.5 DONE: /kokoro-render live — concat intro+main+outro, two-pass loudnorm -16 LUFS
- **Next:** S18.6 — Test de integracion end-to-end con video real
