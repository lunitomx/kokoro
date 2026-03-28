---
epic_id: "E12"
title: "Kokoro Video Analysis"
status: "partially-covered"
updated: "2026-03-27"
---

# Scope: E12 — Video Analysis Pipeline

## Objective
Analizar creativos en video: extraer frames, transcribir audio, aplicar
Andromeda 4-signal framework, generar descripción para /kokoro-ads.

## Stories

- [ ] S12.1 — Frame extraction: ffmpeg key frames de video
- [x] S12.2 — Audio transcription: Whisper o similar
- [ ] S12.3 — Andromeda 4-signal analysis: aplicar framework a VISUAL frames
- [ ] S12.4 — /kokoro-ads integration: video como input
- [ ] S12.5 — Tests + validación con caso real

## Absorption Notes (2026-03-27)

### S12.2 — DONE via E16 S16.1 (`/kokoro-listen`)
Audio transcription is fully covered by `/kokoro-listen` (E16 S16.1).
The skill downloads video/audio, extracts audio via ffmpeg, and transcribes
using Whisper. No remaining work here.

### S12.4 — Partially covered
`/kokoro-ads` already accepts creative descriptions as input. The missing
piece is automated video-to-description (which requires S12.1 + S12.3).

## Remaining Value

The unique value E12 still delivers is **visual analysis**, not audio:

1. **S12.1 — Frame extraction:** Extract key frames from video using ffmpeg
   scene detection. This is the visual counterpart to `/kokoro-listen`.
2. **S12.3 — Andromeda 4-signal on VISUAL frames:** Apply the framework
   (personaje, ambiente, emoción, acción) to extracted frames, not audio.
   Combined with `/kokoro-listen` transcript, produces a complete video
   analysis.
3. **S12.4 — Integration:** Wire frame analysis + transcript into a unified
   video creative description for `/kokoro-ads`.
4. **S12.5 — Validation:** End-to-end test with a real Konecta Park or
   Legacy video ad.

## Done Criteria
- Video de 30s analizado en <2 min
- Descripción generada comparable a análisis manual
- Integrado con /kokoro-ads
- Visual frame analysis + audio transcript produce descripción unificada
