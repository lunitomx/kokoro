---
epic_id: "E11"
title: "Kokoro Analytics — MCP multi-cuenta"
status: "planned"
---

# Scope: E11 — Kokoro Analytics

## Objective
Conectar Meta Ads, GA4 y Google Ads via MCP con onboarding guiado para
usuarios no técnicos. Multi-cuenta, multi-cliente, integrado con client graph.

## Planned Stories
- [ ] S11.1 — Audit MétricaRadix: mapear MCP servers existentes y sus limitaciones
- [ ] S11.2 — Multi-account model: config por cliente con múltiples cuentas de ads/analytics
- [ ] S11.3 — Onboarding guiado: /kokoro-connect skill para conectar cuentas paso a paso
- [ ] S11.4 — /kokoro-analytics skill: consultar métricas en lenguaje natural
- [ ] S11.5 — Integración client graph: vincular cuentas a ClientProfile
- [ ] S11.6 — Meta Ads queries: campañas, ad sets, ads, métricas clave
- [ ] S11.7 — Google Ads queries: campañas, keywords, conversiones
- [ ] S11.8 — GA4 queries: tráfico, conversiones, fuentes

## Done Criteria
- Usuario no técnico conecta cuenta en <10 min
- Eduardo consulta métricas de múltiples clientes
- Integrado con client graph
- Tests pasan

## External Dependencies
- MétricaRadix MCP servers: /Users/soyahuehuetedigital/Documents/MétricaRadix
- MCP servers registrados en Claude Code: google-analytics, google-search-console (ya disponibles)
