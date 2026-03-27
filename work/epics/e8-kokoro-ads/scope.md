---
epic_id: "E8"
title: "Kokoro Ads — Skill de campañas publicitarias"
status: "in-progress"
---

# Scope: E8 — Kokoro Ads

## Objective
Crear el skill /kokoro-ads que automatice el flujo de generación de contenido
para campañas de Meta Ads, siguiendo el proceso validado con Eduardo:
describir creativo → leer contexto del cliente → identificar público → generar
entregables en .txt plano.

## In Scope
- Skill /kokoro-ads con flujo completo
- Proceso de 3 pasos validado (describir → público → copy)
- Entregables en .txt plano (no markdown)
- Lectura de contexto del cliente
- Guardado automático en carpeta de campañas
- Tests del skill

## Out of Scope
- Integración con Meta API
- Google Ads
- Análisis de rendimiento
- Generación de creativos visuales

## Planned Stories
- [ ] S8.1 — Diseño e implementación del skill /kokoro-ads
- [ ] S8.2 — Tests y validación con caso real (Konecta Park brokers)

## Done Criteria
- /kokoro-ads genera entregables completos para un creativo
- Output es .txt plano copiable directo a Meta Ads Manager
- Proceso sigue: describir imagen → leer contexto → público → copy
- Tests pasan
