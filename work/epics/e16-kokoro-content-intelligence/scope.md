---
epic_id: "E16"
title: "Kokoro Content Intelligence"
status: "complete"
---

# Scope: E16 — Kokoro Content Intelligence

## Objective

Darle a Eduardo un pipeline de inteligencia competitiva basado en video:
buscar videos top en YouTube por keyword, descargar, transcribir con Whisper,
analizar patrones, y encontrar oportunidades de contenido. Complementado con
AnswerThePublic para keywords. La salida es un calendario de contenido
accionable (horizontales + shorts) para la proxima semana.

## Value

- Eduardo deja de adivinar que contenido crear — los datos le dicen que falta
- Analizar 10 videos de 15 min cuesta ~$16 MXN total (Whisper)
- El calendario de contenido se genera desde evidencia, no intuicion
- Pipeline reutilizable para cualquier nicho / invitado

## Architecture Decisions

### AD-1: yt-dlp para descarga (no API de YouTube)

yt-dlp descarga audio directamente sin necesitar API key de YouTube.
Mas simple, sin limites de cuota, funciona con cualquier URL.

Rationale: La YouTube Data API tiene cuotas limitadas y requiere OAuth.
yt-dlp es standard de facto, ya disponible via pip/brew.

### AD-2: OpenAI Whisper API para transcripcion (no local)

Usar la API de OpenAI Whisper ($0.006 USD/min) en vez de correr Whisper
local. DeepTutor ya tiene el adapter funcionando.

Rationale: Whisper local requiere GPU o tarda mucho en CPU. La API es
rapida (~1x realtime), barata, y el adapter ya existe. Se puede migrar
a local despues si el volumen justifica.

### AD-3: Claude analiza patrones (no modelo separado)

Las transcripciones se analizan directamente en la conversacion de Claude.
No se necesita un modelo separado para el analisis — Claude es mejor
en sintesis y deteccion de patrones que cualquier alternativa.

Rationale: El valor esta en el analisis, no en la transcripcion. Claude
ya tiene el contexto del invitado y del mercado.

### AD-4: AnswerThePublic como input complementario (no dependencia)

El pipeline funciona sin AnswerThePublic. Si Eduardo tiene datos de ATP,
se usan como input adicional para priorizar keywords. Si no, se usan
las keywords de la busqueda original.

Rationale: No crear dependencia en un servicio de pago. ATP complementa,
no bloquea.

### AD-5: Video editor en parking lot (fase 2)

El pipeline de edicion automatica (OpenShorts, cortes, graficos) se
mantiene en parking lot hasta que E16 core este validado. Primero
inteligencia, despues produccion.

Rationale: El valor inmediato es saber QUE crear. La produccion viene
despues. No mezclar investigacion con produccion en la misma epica.

## Stories

- [x] S16.1 — /kokoro-listen: descargar y transcribir video/audio de cualquier URL (S)
- [x] S16.2 — /kokoro-intel: buscar top N en YouTube, descargar, transcribir, analizar patrones (M)
- [x] S16.3 — Analisis de oportunidades: detectar huecos, angulos no cubiertos, debilidades (S)
- [x] S16.4 — Calendario de contenido: generar plan semanal de videos horizontales + shorts (S)

## Story Details

### S16.1 — /kokoro-listen (S)

Skill que recibe una URL (YouTube, Instagram, TikTok) y:
1. Descarga el audio con yt-dlp
2. Transcribe con Whisper API (usando adapter de DeepTutor)
3. Guarda transcripcion en clientes/{grupo}/transcripciones/
4. Presenta resumen y ofrece analisis

Requiere: yt-dlp instalado, OPENAI_API_KEY en .env, ffmpeg.
Costo: ~$0.006 USD/min (~$1.60 MXN por video de 15 min).

**Dependencies:** None
**Size:** S

### S16.2 — /kokoro-intel (M)

Skill que recibe un keyword de busqueda y:
1. Busca en YouTube (yt-dlp search o scraping ligero)
2. Descarga audio de los top 5-10 resultados
3. Transcribe todos con Whisper
4. Analiza patrones: temas comunes, estructura, tono, duracion
5. Presenta reporte de inteligencia competitiva

Costo estimado: ~$8-16 MXN por busqueda (5-10 videos).

**Dependencies:** S16.1 (usa el mismo pipeline de descarga/transcripcion)
**Size:** M

### S16.3 — Analisis de oportunidades (S)

Extension de /kokoro-intel que despues del analisis de patrones:
1. Detecta huecos: que temas nadie cubre
2. Detecta debilidades: que esta mal explicado o desactualizado
3. Detecta angulos: que perspectiva falta (principiante, avanzado, caso real)
4. Presenta oportunidades rankeadas por impacto potencial

**Dependencies:** S16.2
**Size:** S

### S16.4 — Calendario de contenido (S)

Genera un plan semanal basado en las oportunidades detectadas:
1. N videos horizontales (8-15 min) con tema, angulo, estructura
2. N shorts (30-60 seg) derivados de cada horizontal
3. Titulos optimizados para YouTube
4. Thumbnails sugeridos (descripcion para /kokoro-creative)

Si hay datos de AnswerThePublic, los cruza con las oportunidades
para priorizar por volumen de busqueda.

**Dependencies:** S16.3
**Size:** S

## Dependency Graph

```
S16.1 (listen) ──> S16.2 (intel) ──> S16.3 (oportunidades) ──> S16.4 (calendario)
```

Lineal — cada paso alimenta al siguiente.

## Scope Boundaries

### In (MUST)
- /kokoro-listen descarga y transcribe cualquier URL
- /kokoro-intel analiza top N videos de una busqueda
- Deteccion de patrones y oportunidades
- Calendario de contenido semanal

### In (SHOULD)
- Integracion con AnswerThePublic (si Eduardo tiene cuenta)
- Sugerencias de thumbnails para /kokoro-creative

### No-Gos
- No editar video (parking lot — fase 2)
- No subir contenido a YouTube (manual)
- No crear shorts automaticamente (OpenShorts es parking lot)
- No scraping agresivo de YouTube (respetar rate limits)

### Rabbit Holes
- Construir editor de video completo (es otra epica)
- Automatizar subida a YouTube (prematuro)
- Analisis de sentimiento en comentarios (over-engineering)

## Done Criteria

- [ ] /kokoro-listen transcribe un video de YouTube correctamente
- [ ] /kokoro-intel analiza 5+ videos y detecta patrones
- [ ] Oportunidades rankeadas y accionables
- [ ] Calendario semanal generado con horizontales + shorts
- [ ] Costo por busqueda < $20 MXN

## Risks

1. **yt-dlp bloqueado por YouTube** — Mitigation: yt-dlp se actualiza frecuentemente, usar version mas reciente
2. **Whisper API rate limits** — Mitigation: procesar videos secuencialmente, no en paralelo
3. **Transcripciones largas saturan contexto** — Mitigation: resumir cada transcripcion antes de analisis cruzado
