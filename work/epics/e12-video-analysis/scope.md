---
epic_id: "E12"
title: "Kokoro Video Analysis"
status: "planned"
---

# Scope: E12 — Video Analysis Pipeline

## Objective
Analizar creativos en video: extraer frames, transcribir audio, aplicar
Andromeda 4-signal framework, generar descripción para /kokoro-ads.

## Planned Stories
- [ ] S12.1 — Frame extraction: ffmpeg key frames de video
- [ ] S12.2 — Audio transcription: Whisper o similar
- [ ] S12.3 — Andromeda 4-signal analysis: aplicar framework a frames + transcript
- [ ] S12.4 — /kokoro-ads integration: video como input
- [ ] S12.5 — Tests + validación con caso real

## Done Criteria
- Video de 30s analizado en <2 min
- Descripción generada comparable a análisis manual
- Integrado con /kokoro-ads
