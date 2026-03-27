---
epic_id: "E14"
title: "Konecta Park — Diagnóstico y optimización de campañas"
status: "planned"
depends_on: "E11"
---

# Scope: E14 — Konecta Park Analytics

## Objective

Usar Kokoro Analytics (E11) para diagnosticar por qué las campañas de
Konecta Park atraen mensajes spam y recomendar optimizaciones de targeting
basadas en data real de los MCP servers.

## Dependency

Requiere E11 completo — necesita /kokoro-connect y /kokoro-analytics
para acceder a data de Meta Ads.

## Planned Stories

- [ ] S14.1 — Registrar Konecta Park como cliente: /kokoro-client + /kokoro-connect con cuentas Meta Ads
- [ ] S14.2 — Diagnóstico de campañas: análisis de performance, demografía y creativos via MCP
- [ ] S14.3 — Recomendaciones de targeting: audiencias optimizadas + exclusiones + nuevos copies
- [ ] S14.4 — Validación post-cambio: comparar métricas antes/después con data real

## Done Criteria

- [ ] Konecta Park registrado en client graph con cuentas mapeadas
- [ ] Diagnóstico documentado con data real (no manual)
- [ ] Recomendaciones aplicadas por Eduardo en Meta Ads Manager
- [ ] Reducción medible de mensajes spam
