---
epic_id: "E14"
title: "Kokoro Luxelling — Conocimiento de lujo condicional"
status: "designed"
---

# Scope: E14 — Kokoro Luxelling

## Objective

Integrar el conocimiento de lujo de Luxelling como capacidad condicional en Kokoro.
El lujo no es default — se activa cuando el invitado califica via assessment de
posicionamiento (Triangulo Funcional-Simbolico-Emocional). Cada modulo de Luxelling
tiene su propio mini-skill. Legacy by Invertikal se onboardea como primer cliente luxury.

## Source Material

- `notas-eduardo/` — 9 modulos + Arquitectura Completa (~3,000 lineas)
- `workbook/` — 10 modulos incluyendo Mod 09 Nuevo Lujo (~1,300 lineas)
- Legacy by Invertikal — ficha, plan maestro, evaluacion Luxelling
- ISDVEY — extraccion editorial (menor prioridad)

Ubicacion: `/Users/soyahuehuetedigital/Downloads/Alquimia Digital Final/Luxelling/`

## Architecture Decisions

### AD-1: Positioning tier via metadata (no model change)

`ClientProfile.metadata["positioning_tier"]` = `"luxury" | "premium" | "standard"`

Rationale: metadata is `dict[str, Any]`, designed for extensible fields.
No schema migration needed. Consistent with how `platform_accounts` was added in E11.

### AD-2: Assessment as standalone skill (not embedded in diagnose/canvas)

Create `/kokoro-luxury-assess` as independent skill that can be called from
`/kokoro-client` during creation OR standalone for existing clients.

Rationale: Embedding in diagnose/canvas would modify base skills (violates No-Go).
Independent skill can be invoked from any context. Assessment result persists in
client profile for all future skill invocations.

### AD-3: Luxury knowledge as .claude/knowledge files (not conocimientoraiz/)

Luxury module knowledge files live in `.claude/knowledge/luxelling/` — NOT in
`conocimientoraiz/`. The knowledge files in conocimientoraiz/ are raw source material.
The .claude/knowledge/ files are curated, structured references that skills consume.

Rationale: conocimientoraiz/ has raw transcripts and notes at varying quality.
Skills need structured, prompt-optimized knowledge files (like kokoro-connect-platforms.md).
Pattern from PAT-L-012: knowledge files separate from skill prompts.

### AD-4: One router + module skills (not monolithic)

`/kokoro-luxury` routes to module-specific skills. Each module skill is independent
and can be invoked directly if the user knows what they want.

Module mapping:
- `/kokoro-luxury` — Router: assessment check + module navigation
- `/kokoro-luxury-assess` — Triangulo F-S-E positioning assessment
- `/kokoro-luxury-scarcity` — Mod 03: Escasez estrategica
- `/kokoro-luxury-quality` — Mod 03: Calidad extrema + Mod 04: Poder simbolico
- `/kokoro-luxury-experience` — Mod 03: Experiencias memorables
- `/kokoro-luxury-communication` — Mod 05: Comunicacion que eleva
- `/kokoro-luxury-pricing` — Mod 08: Estrategia de precios en lujo
- `/kokoro-luxury-growth` — Mod 07: Crecer sin perder brillo

Rationale: 6 module skills (not 9) because some modules merge naturally.
Mods 01-02 (intro, mass vs premium vs luxury) are assessment material, not standalone skills.
Mod 06 (ser lujo para vender lujo) is a mindset module — it informs voice, not actions.

### AD-5: Luxury layer in base skills via knowledge file (not code change)

Base skills like /kokoro-pescar, /kokoro-launch, /kokoro-finance don't get code changes.
Instead, a single knowledge file `.claude/knowledge/kokoro-luxury-layers.md` documents
what luxury-specific guidance to add when `positioning_tier = luxury`.

Each base skill already reads client context. The knowledge file tells the skill:
"If this client is luxury-tier, also consider: [specific luxury principles]."

Rationale: Zero changes to existing skills. Knowledge file is additive context.
Follows the same pattern as kokoro-connect-platforms.md (reference, not code).

## Stories

- [ ] S14.1 — Knowledge curation: create structured .claude/knowledge/luxelling/ files from source material (S)
- [ ] S14.2 — /kokoro-luxury-assess: positioning assessment skill + persist tier in client profile (S)
- [ ] S14.3 — /kokoro-luxury router: module navigation with tier gate (S, dep: S14.2)
- [ ] S14.4 — Module skills batch 1: scarcity + quality + experience (M, dep: S14.1)
- [ ] S14.5 — Module skills batch 2: communication + pricing + growth (M, dep: S14.1)
- [ ] S14.6 — Legacy onboarding: client profile + luxury tier + /kokoro-connect (S, dep: S14.2)
- [ ] S14.7 — Luxury layers: knowledge file for base skill augmentation (S, dep: S14.1)

## Story Details

### S14.1 — Knowledge curation (S)
Create 6 structured knowledge files in `.claude/knowledge/luxelling/` from source material:
- `luxelling-scarcity.md` — From notas-eduardo/03 + workbook/03
- `luxelling-quality-symbolism.md` — From notas-eduardo/03+04 + workbook/03+04
- `luxelling-experience.md` — From notas-eduardo/03 (experiencias section) + workbook
- `luxelling-communication.md` — From notas-eduardo/05 + workbook/05
- `luxelling-pricing.md` — From notas-eduardo/08 + workbook/08
- `luxelling-growth.md` — From notas-eduardo/07 + workbook/07
- `luxelling-assessment.md` — From notas-eduardo/01+02 (positioning framework)
- `luxelling-master.md` — From LUXELLING_Arquitectura_Completa (synthesis)

Also copy workbook/09-nuevo-lujo-del-manana.md to conocimientoraiz/ as raw source.
Extension mirrors for all knowledge files.

**Dependencies:** None
**Size:** S (content curation, no code)

### S14.2 — /kokoro-luxury-assess (S)
Skill that runs the Triangulo F-S-E assessment:
1. 5 questions (value type, distribution, price point, production control, buyer motivation)
2. Score: 4-5/5 = luxury, 2-3/5 = premium, 0-1/5 = standard
3. Persist result in ClientProfile.metadata["positioning_tier"]
4. If no client selected, prompt for client resolution first

Reads: `luxelling-assessment.md`
Extension mirrors + test_output_structure.py update.

**Dependencies:** None (can run before S14.1 — assessment knowledge is simple enough)
**Size:** S

### S14.3 — /kokoro-luxury router (S)
Router skill that:
1. Checks client's positioning_tier — if not set, redirects to /kokoro-luxury-assess
2. If tier = standard, explains luxury is not applicable, suggests /kokoro-diagnose
3. If tier = luxury or premium, presents module menu with brief descriptions
4. Routes to appropriate module skill

Extension mirrors + test_output_structure.py update.

**Dependencies:** S14.2 (needs assessment to exist)
**Size:** S

### S14.4 — Module skills batch 1: scarcity, quality, experience (M)
Three skill files:
- `/kokoro-luxury-scarcity` — Demand Gap Index, ediciones limitadas, distribucion selectiva
- `/kokoro-luxury-quality` — Piramide de calidad, 5A Framework, poder simbolico
- `/kokoro-luxury-experience` — Experiencias multisensoriales, rituales de acceso

Each follows Kokoro patterns: Proyector strategy, luxurizante vocabulary,
references its knowledge file, includes client resolution.
Extension mirrors + test_output_structure.py updates.

**Dependencies:** S14.1 (needs knowledge files)
**Size:** M (3 skills, but they follow established pattern)

### S14.5 — Module skills batch 2: communication, pricing, growth (M)
Three skill files:
- `/kokoro-luxury-communication` — Codigos visuales, paleta 60/30/10, silencio visual
- `/kokoro-luxury-pricing` — Value-based pricing, Efecto Veblen, discontinuidad estrategica
- `/kokoro-luxury-growth` — Brand stretching, crecer sin diluir, halo effect

Same patterns as S14.4.
Extension mirrors + test_output_structure.py updates.

**Dependencies:** S14.1 (needs knowledge files)
**Size:** M (3 skills)

### S14.6 — Legacy onboarding (S)
1. Create Legacy by Invertikal client profile via /kokoro-client flow
2. Set positioning_tier: luxury (or run /kokoro-luxury-assess to demonstrate)
3. Run /kokoro-connect to map Meta Ads account
4. Copy Legacy materials (ficha, plan maestro) to clientes/invertikal/legacy/

**Dependencies:** S14.2 (needs assessment skill)
**Size:** S (operational, not code)

### S14.7 — Luxury layers knowledge file (S)
Create `.claude/knowledge/kokoro-luxury-layers.md` documenting:

For each base Kokoro skill, what additional luxury considerations apply:
- /kokoro-pescar: comunicacion que seduce, no que vende; codigos visuales de lujo
- /kokoro-launch: escasez estrategica, lanzamiento a fuego lento, apnea comercial
- /kokoro-finance: value-based pricing, Efecto Veblen, pricing power
- /kokoro-factory: distribucion hiper-selectiva, customer curation
- /kokoro-mafia: exclusividad real, rituales de acceso, poder simbolico

Extension mirrors.

**Dependencies:** S14.1 (needs curated knowledge as source)
**Size:** S

## Dependency Graph

```
S14.1 (knowledge) ──┬──→ S14.4 (batch 1: scarcity/quality/experience)
                     ├──→ S14.5 (batch 2: communication/pricing/growth)
                     └──→ S14.7 (luxury layers)

S14.2 (assess) ─────┬──→ S14.3 (router)
                     └──→ S14.6 (Legacy onboarding)

No cycles. S14.1 and S14.2 can run in parallel.
S14.4 and S14.5 can run in parallel after S14.1.
S14.3 and S14.6 can run in parallel after S14.2.
```

## Scope Boundaries

### In (MUST)
- Positioning tier assessment integrado en flujo de cliente
- /kokoro-luxury como router de modulos de lujo
- 6 mini-skills para modulos de Luxelling
- Knowledge curado en .claude/knowledge/luxelling/
- Legacy como primer cliente luxury con perfil y conexiones
- Luxury knowledge condicional — solo si califica

### In (SHOULD)
- ISDVEY como segundo cliente luxury
- Modulo 09 (Nuevo Lujo del Manana) en conocimientoraiz/
- Sintesis Arquitectura Completa como referencia maestra

### No-Gos
- No modificar skills base de Kokoro (pescar, launch, finance, etc.)
- No cambiar vocabulario universal (inversion, creacion, cortesia)
- No construir MCP servers nuevos
- No templates por industria (prematuro)

### Rabbit Holes
- Luxury CRM completo — el client graph con positioning_tier es suficiente
- Templates industria-especificos — demasiado pronto
- Automatizar auditorias de marca — mantener conversacional

## Done Criteria
- [ ] 8 knowledge files en .claude/knowledge/luxelling/ (curated from source)
- [ ] /kokoro-luxury-assess funcional (5 preguntas → tier en perfil)
- [ ] /kokoro-luxury router con tier gate + navegacion a 6 modulos
- [ ] 6 module skills creados con mirrors y tests
- [ ] Legacy onboarded: perfil + positioning_tier: luxury + Meta Ads
- [ ] kokoro-luxury-layers.md documenta capas para skills base
- [ ] Skills base de Kokoro intactos (no regresiones)
- [ ] Tests pasan (100%)

## Risks
1. **Knowledge duplicado** — notas-eduardo y workbook cubren mismo contenido
   - Mitigation: S14.1 curates, doesn't copy — structured extraction, not duplication
2. **Mini-skills demasiado thin** — algunos modulos son cortos
   - Mitigation: Merged modules (03 split into 3, 03+04 into quality)
3. **Assessment gaming** — usuario podria responder "luxury" a todo
   - Mitigation: Assessment es guia, no gate hard — el skill funciona igual, la guia cambia
4. **PAT-L-013 coupling** — router references module skills by name
   - Mitigation: Accepted trade-off — luxury is a closed set, not extensible
