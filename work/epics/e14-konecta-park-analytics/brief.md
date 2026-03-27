---
epic_id: "E14"
title: "Konecta Park — Diagnóstico y optimización de campañas con Kokoro Analytics"
status: "draft"
created: "2026-03-26"
depends_on: "E11"
---

# Epic Brief: E14 — Konecta Park Analytics

## Hypothesis

For Eduardo who needs to understand why Konecta Park campaigns attract
spam messages (albañiles, servicios) instead of brokers and buyers,
the Kokoro Analytics system (E11) can connect to the actual campaign data
via MCP, diagnose targeting issues, and recommend fixes,
so that the ad spend produces qualified leads instead of noise.
Unlike manual campaign review in Meta Ads Manager,
our solution cross-references campaign data, creative content, audience
targeting, and performance metrics to find the root cause.

## Success Metrics
- **Leading:** Diagnóstico de campañas con data real de MCP (no manual)
- **Lagging:** Reducción de mensajes spam >50%, aumento de leads calificados

## Appetite
S — 3-4 stories

## Context (from SES-021)

### Campaña 1: "Konecta - Whatsapp"
- 6 anuncios, activa, $333/día
- Público: México (QRoo, BC, CDMX, Zapopan, MTY, Juriquilla, Mérida) +40km
- Edad: 40-64
- Intereses: Cadena de suministro, Logística, Negocios Y Emprendimientos,
  Comercio Exterior, Administración Empresas Turísticas, Encargado de almacén,
  Consultor inmobiliario, Logistics Manager
- Audiencia: 816K-960K (amplio)
- Advantage+ desactivado

### Campaña 2: "Konecta Park Brokers"
- 1 anuncio, activa con cambios sin publicar
- Público: México (Cancún +80km, CDMX +40km, EdoMex, Yucatán)
- Edad: 30-55
- Intereses: Ingeniería industrial, Negocios, Seguridad Industrial,
  Mantenimiento Industrial, Real Estate Agent/Broker, Representante Comercial,
  Agente de negocios
- Audiencia: 1.6M-1.9M (amplio)

### Problema
- Mensajes de gente ofreciendo servicios (albañilería, etc.)
- Eduardo apagó uno de los ads
- No está atrayendo al perfil correcto (brokers industriales, compradores de bodegas)

## Scope Boundaries

### In (MUST)
- Registrar Konecta Park como cliente en /kokoro-client con cuentas mapeadas
- Diagnóstico con data real de MCP (performance, demografía, creativos)
- Recomendaciones de targeting actionables para Meta Ads
- Nuevos copies si el creativo/texto es parte del problema

### In (SHOULD)
- A/B test plan para validar nuevas audiencias
- Audiencias de exclusión para filtrar spam
- Comparación antes/después con data

### No-Gos
- No modificar campañas automáticamente (Eduardo lo hace manual en Meta)
- No crear nuevas campañas desde Kokoro (solo recomendar)

### Rabbit Holes
- Rebuild completo de todas las campañas — empezar por diagnóstico puntual
- Scoring model de leads — demasiado complejo para el volumen actual
