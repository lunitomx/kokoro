---
epic_id: "E11"
title: "Kokoro Analytics — MCP multi-cuenta para Meta Ads, GA4, Google Ads"
status: "draft"
created: "2026-03-26"
---

# Epic Brief: E11 — Kokoro Analytics

## Hypothesis
For Eduardo and his non-technical clients who need to see campaign performance,
the Kokoro Analytics system is a guided setup + skills layer
that connects Meta Ads, Google Analytics, and Google Ads via MCP servers,
supporting multiple accounts/clients with a zero-code onboarding flow.
Unlike the current MétricaRadix setup (one client, one account, requires technical knowledge),
our solution guides any user to connect their accounts step by step
and provides /kokoro-analytics skill to query performance in natural language.

## Success Metrics
- **Leading:** Un usuario no técnico conecta su cuenta de Meta Ads en <10 min
- **Lagging:** Eduardo consulta métricas de 3+ clientes desde Kokoro

## Appetite
L — 6-8 stories

## Scope Boundaries
### In (MUST)
- Onboarding guiado para conectar cuentas (Meta Ads, GA4, Google Ads)
- Soporte multi-cuenta/multi-cliente
- /kokoro-analytics skill para consultar métricas en lenguaje natural
- Integración con client graph (cada cuenta se conecta a un ClientProfile)
- Basado en MCP servers existentes de MétricaRadix

### In (SHOULD)
- Dashboard simple en terminal (tablas con métricas clave)
- Comparación entre períodos
- Alertas cuando métricas bajan

### No-Gos
- No construir MCP servers desde cero — usar los de MétricaRadix como base
- No UI web — todo via skills y terminal
- No almacenar credenciales en el repo — usar env vars o config local

### Rabbit Holes
- Construir un Google Data Studio killer — solo consultas puntuales
- Real-time streaming de métricas — batch queries son suficientes
- Automatic campaign optimization — eso es otro nivel
