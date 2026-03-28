---
epic_id: "E14"
title: "Konecta Park — Diagnóstico y optimización de campañas"
status: "in-progress"
depends_on: "E11"
updated: "2026-03-27"
---

# Scope: E14 — Konecta Park Analytics

## Objective

Usar Kokoro Analytics (E11) para diagnosticar por qué las campañas de
Konecta Park atraen mensajes spam y recomendar optimizaciones de targeting
basadas en data real de los MCP servers.

## Dependency

Requiere E11 completo — necesita /kokoro-connect y /kokoro-analytics
para acceder a data de Meta Ads. **E11 is DONE.**

## Stories

- [x] S14b.1 — Registrar Konecta Park como cliente (done 2026-03-27)
  - Registered in `.kokoro/clients.json` with id `konecta-park`, group `invertikal`
  - Segments: brokers, inversionistas, fondos, desarrolladores
  - Industry: real-estate-industrial
  - Meta Ads account: act_860134896091761
  - Context file: `clientes/invertikal/konecta-park/campañas/meta-ads/contexto.md`
  - Repo: `Documents/GitHub/KonectaParkAhuehuete`
- [ ] S14b.2 — Diagnóstico de campañas: análisis de performance, demografía y creativos via MCP
- [ ] S14b.3 — Recomendaciones de targeting: audiencias optimizadas + exclusiones + nuevos copies
- [ ] S14b.4 — Validación post-cambio: comparar métricas antes/después con data real

## Done Criteria

- [x] Konecta Park registrado en client graph con cuentas mapeadas
- [ ] Diagnóstico documentado con data real (no manual)
- [ ] Recomendaciones aplicadas por Eduardo en Meta Ads Manager
- [ ] Reducción medible de mensajes spam
