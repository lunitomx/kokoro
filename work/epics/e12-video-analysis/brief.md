---
epic_id: "E12"
title: "Kokoro Video Analysis — Pipeline de análisis de creativos en video"
status: "draft"
created: "2026-03-26"
---

# Epic Brief: E12 — Video/Creative Analysis Pipeline

## Hypothesis
For Eduardo who receives video creatives from clients and needs to generate ad copy,
the video analysis pipeline is a skill that extracts frames + transcription
from video files and applies the Andromeda 4-signal framework,
so that Kokoro can describe video creatives with the same depth as images.
Unlike the current manual process (watch video, describe manually),
our solution automates extraction and analysis.

## Success Metrics
- **Leading:** Kokoro describe un video creativo de 30s en <2 min
- **Lagging:** Eduardo genera copy para campañas de video sin ver el video completo

## Appetite
M — 4-5 stories

## Scope Boundaries
### In (MUST)
- Extraer frames clave de video (ffmpeg)
- Transcribir audio (Whisper o similar)
- Aplicar framework Andromeda (4 señales) al contenido
- Integración con /kokoro-ads (video como input además de imagen)

### In (SHOULD)
- Detección de escenas/cortes automática
- Análisis de paleta de colores del video
- Thumbnail selection automático

### No-Gos
- No edición de video — solo análisis
- No generación de video — solo describe lo que existe
- No hosting de video — archivos locales

### Rabbit Holes
- Computer vision avanzado — los frames + multimodal de Claude son suficientes
- Lip sync analysis — overkill para ads
