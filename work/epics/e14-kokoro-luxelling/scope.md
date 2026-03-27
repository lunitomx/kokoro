---
epic_id: "E14"
title: "Kokoro Luxelling — Conocimiento de lujo condicional"
status: "initialized"
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

## Architecture Decision

- `positioning_tier` field in ClientProfile: `"luxury" | "premium" | "standard"`
- Assessment via Triangulo F-S-E (5 preguntas) durante diagnostico o canvas
- Luxury skills son independientes — no modifican skills base de Kokoro
- Knowledge files en `conocimientoraiz/` (ya existen modulos 00-08, faltan 09 y Arquitectura)

## Stories

- [ ] S14.1 — Knowledge integration: copiar modulos faltantes + validar consistencia (XS)
- [ ] S14.2 — Positioning assessment: mini-examen Triangulo F-S-E + persistencia en perfil (S)
- [ ] S14.3 — /kokoro-luxury router: skill principal con navegacion a modulos (S)
- [ ] S14.4 — Mini-skills por modulo: escasez, calidad, experiencia, comunicacion, pricing, poder simbolico (M)
- [ ] S14.5 — Legacy client profile: onboarding completo + /kokoro-connect Meta Ads (S)
- [ ] S14.6 — Luxury layer en skills existentes: activar capas adicionales cuando luxury_tier (S)

## Scope Boundaries

### In (MUST)
- Positioning tier assessment integrado en flujo de cliente
- /kokoro-luxury como router de modulos de lujo
- Mini-skills para cada modulo de Luxelling
- Knowledge completo en conocimientoraiz/
- Legacy como primer cliente luxury con perfil y conexiones
- Luxury knowledge condicional — solo si califica

### In (SHOULD)
- ISDVEY como segundo cliente luxury
- Modulo 09 (Nuevo Lujo del Manana) integrado
- Sintesis Arquitectura Completa como referencia maestra

### No-Gos
- No modificar skills base de Kokoro
- No cambiar vocabulario universal (inversion, creacion, cortesia)
- No construir MCP servers nuevos
- No templates por industria (prematuro)

### Rabbit Holes
- Luxury CRM completo — el client graph con positioning_tier es suficiente
- Templates industria-especificos — demasiado pronto
- Automatizar auditorias de marca — mantener conversacional

## Done Criteria
- [ ] Modulos 00-09 + Arquitectura Completa en conocimientoraiz/
- [ ] Assessment de posicionamiento funcional (5 preguntas → tier)
- [ ] /kokoro-luxury router con navegacion a 6+ mini-skills
- [ ] Legacy onboarded: perfil + positioning_tier: luxury + Meta Ads conectado
- [ ] Skills base de Kokoro intactos (no regresiones)
- [ ] Tests pasan

## Risks
1. Knowledge duplicado entre notas-eduardo y workbook → S14.1 normaliza
2. Mini-skills demasiado granulares → consolidar si modulos son thin
3. Assessment demasiado largo → mantener en 5 preguntas max
