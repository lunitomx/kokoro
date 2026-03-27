---
epic_id: "E8"
title: "Kokoro Ads — Skill de campañas publicitarias"
status: "draft"
created: "2026-03-26"
---

# Epic Brief: Kokoro Ads — Skill de campañas publicitarias

## Hypothesis
For Eduardo y su equipo who crean campañas de Meta Ads para clientes como Konecta Park,
the /kokoro-ads skill is a flujo guiado
that recibe una imagen de creativo, lee el contexto del cliente, y genera todos los
entregables de una campaña (copy, WhatsApp, audiencias) en formato .txt listo para
copiar y pegar en Meta Ads Manager.
Unlike el proceso actual (improvisar en cada sesión y perder avances), nuestro skill
sigue el proceso validado: describir creativo → identificar público → generar copy.

## Success Metrics
- **Leading:** Generar entregables completos para 1 creativo en una sola invocación
- **Lagging:** Eduardo puede crear campañas sin re-explicar el proceso cada sesión

## Appetite
S — 2-3 stories

## Scope Boundaries
### In (MUST)
- Skill /kokoro-ads que siga el proceso: imagen → descripción → público → copy
- Lectura automática del contexto del cliente (contexto.md)
- 5 títulos + 5 descripciones en .txt plano (no markdown)
- Plantilla WhatsApp según tipo de campaña
- Descripción de audiencia para Advantage+ (Meta AI targeting)
- Guardado automático en carpeta de campañas del cliente

### In (SHOULD)
- Soporte para múltiples creativos en una sesión
- Nomenclatura automática de archivos (creativo-01, creativo-02...)
- Lectura del repo del cliente para datos reales (inventario, precios)

### No-Gos
- No gestionar la campaña en Meta Ads Manager — solo generar el contenido
- No crear imágenes ni creativos visuales — el input es la imagen que trae el usuario
- No Google Ads — por ahora solo Meta Ads
- No generar copy genérico sin leer contexto del cliente primero

### Rabbit Holes
- Integración directa con Meta API — overkill, copiar/pegar es suficiente
- Análisis de rendimiento de campañas anteriores — eso es otro skill
- Crear un dashboard de campañas — archivos .txt en carpetas es suficiente
