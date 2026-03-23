# Parking Lot

Items deferred from active work. Review during epic planning.

| Item | Origin | Priority | Promote When |
|------|--------|----------|-------------|
| Phase 2 skills (canvas, forces, interviews, validate) | E1 scope | P1 | E1 complete |
| Phase 3 skills (research, pescar, experiment, launch) | E1 scope | P2 | E2 complete |
| Phase 4 skills (factory, funnel, mafia, rhythm) | E1 scope | P3 | E3 complete |
| Automated skill output testing | E1 scope | P2 | After E1 manual QA validates approach |
| Kokoro persistent memory — track decisions, copy changes, art changes, pending work, session continuity (Rai-like model) | SES-007 user request | P1 | After E2 — core coaching flow must exist first |
| Web quality skills (Addy Osmani web-quality-skills) — site health diagnostics for entrepreneurs | SES-007 user request | P2 | E3 (Germinar) — fits with /kokoro-research and /kokoro-launch |
| Video/creative analysis pipeline — ffmpeg frames + Whisper transcription + Andromeda 4-signal framework | SES-007 Konecta case study | P2 | E3 (Germinar) — fits with /kokoro-pescar and /kokoro-launch |
| Skill cross-reference validation — test that `/kokoro-X` references in skill files point to skills that actually exist. Prevents silent broken links on rename. | E2 retro (kaizen) | P1 | E3 planning — cheap to add, high value |
| Anti-vocabulary tests — verify prohibited words (cliente, producto, precio, gratis, descuento) do NOT appear in skill files. Protects Eduardo's voice by both sides: what must be AND what must not be. | E2 retro (kaizen) | P1 | E3 T1 of each skill — add to test template |
| Anti-pattern assertion hardening — require >= 2 of N anti-patterns present, not just 1 (OR is too permissive). QR detected in S2.3/S2.5 but deferred as LOW. | E2 retro (kaizen) | P2 | E3 planning — apply to new skills, backport to E2 if time |
| Conftest fixture standardization — either all test files use shared fixtures from conftest.py or remove orphaned fixtures. Currently mixed. | E2 retro (kaizen) | P3 | E3 or refactoring sprint |
| Skill dependency graph — formal graph connecting skills by methodology flow (canvas→forces→interviews→validate), enabling: validation of cross-refs, session continuity, progress visualization, pedagogical coherence checks | E2 retro (Luna question) | P1 | Before E3 — foundational for persistent memory and skill interconnection |
