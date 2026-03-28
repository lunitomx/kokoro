---
epic_id: "E18"
title: "Kokoro Video Editor — De video crudo a contenido publicable"
status: "draft"
created: "2026-03-27"
---

# Epic Brief: E18 — Kokoro Video Editor

## Hypothesis
For Eduardo who produces long-form video content (workshops, interviews, lives)
and needs to extract publishable shorts and polished clips,
the Kokoro Video Editor pipeline takes raw video, transcribes it,
identifies the best moments, generates graphics/overlays,
and exports final video + shorts ready for publication,
unlike the current manual process (watch full video, cut in editor, add text by hand).
Our solution leverages OpenShorts as base for shorts generation,
ffmpeg for video manipulation, and existing Kokoro skills (listen, creative)
for transcription and graphics.

## Success Metrics
- **Leading:** Pipeline identifies top 5 shorts-worthy moments from a 30-min video in <5 min
- **Lagging:** Eduardo publishes 3+ shorts per week from a single raw video session

## Appetite
M-L — 6 stories (Phase 1: cuts + shorts, Phase 2: graphics + polish)

## Scope Boundaries
### In (MUST)
- Transcription-based cut identification (best moments for 30-60s shorts)
- Video segment extraction via ffmpeg
- Text overlay/caption generation from transcript
- Final render with overlays + intro/outro
- End-to-end pipeline test with real video

### In (SHOULD)
- OpenShorts integration for automated shorts generation
- Vertical (9:16) reformatting for shorts/reels
- Batch processing (multiple shorts from one video)

### No-Gos
- No live streaming — only post-production
- No proprietary video tools — ffmpeg only
- No AI video generation — only editing existing footage
- No hosting/upload to platforms — output is local files
- No audio mixing/music addition — keep it simple

### Rabbit Holes
- Building a full NLE (non-linear editor) — ffmpeg commands are enough
- Speaker diarization for multi-person videos — Phase 2+ at best
- Automatic B-roll insertion — too complex, too early
- YouTube/TikTok direct upload — separate concern (/kokoro-publish scope)
