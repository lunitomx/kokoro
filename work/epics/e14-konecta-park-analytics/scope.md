---
epic_id: "E14"
title: "Konecta Park — Diagnóstico y optimización de campañas"
status: "near-complete"
depends_on: "E11"
updated: "2026-03-30"
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
- [x] S14b.2 — Diagnóstico de campañas: análisis de performance, demografía y creativos (done 2026-03-30)
  - Ejecutado via reporte semanal MetricaRadix (27-30 Mar 2026), no via /kokoro-analytics
  - Fuentes: Meta Business API + GA4 + Microsoft Clarity + Pipedrive (cruce manual)
  - Hallazgo principal: 96.6% del tráfico al sitio era basura (Audience Network + bots)
  - Auditoría de conversiones: 9 pixel → 2 leads reales (7 view-through)
  - Reporte: `Documents/MétricaRadix/Entregables Marzo 2026/Semana 27Mar-30Mar/Konecta/`
- [x] S14b.3 — Recomendaciones aplicadas (done 2026-03-30)
  - Audience Network excluido de campaña CompleteRegistration (30 Mar)
  - Pixel fix E15 en progreso: mover disparo a callback Pipedrive API
  - Creativo "Avance de Obra" reactivado con tráfico filtrado por formulario
  - UTMs de campaña Brokers pendiente de fix (bug detectado)
- [ ] S14b.4 — Validación post-cambio: comparar métricas antes/después con data real
  - Pendiente: esperar ~1 semana post-exclusión Audience Network (~2026-04-07)
  - Verificar: reducción de tráfico basura, mejora en CPR real, click_to_chat legítimos

## Done Criteria

- [x] Konecta Park registrado en client graph con cuentas mapeadas
- [x] Diagnóstico documentado con data real (reporte MetricaRadix 27-30 Mar)
- [x] Recomendaciones aplicadas: Audience Network excluido, pixel fix en progreso
- [ ] Reducción medible de tráfico basura (pendiente validación post-cambio ~2026-04-07)
