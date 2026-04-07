# PRD: RaizAncestral (Kokoro)

> Product Requirements Document

---

## Problem

Los emprendedores reciben consejos genéricos de marketing digital — listas de tips,
plantillas sin contexto, promesas de resultados rápidos. Eduardo Muñoz Luna tiene
una metodología profunda de 4 fases, pero su capacidad de atención es limitada a
sesiones individuales. No existe una forma de escalar la profundidad de su consultoría
sin perder la voz, la filosofía y el rigor que la distinguen.

## Goals

Un sistema que preserve la identidad completa de Eduardo (voz, arquetipos, vocabulario
luxurizante, estrategia Proyector) mientras guía emprendedores a través de procesos
estructurados con datos reales de sus plataformas digitales.

---

## Requirements

### RF-01: Skill Distribution

El sistema se distribuye como carpeta `extension/` con skills de Claude Code (`.claude/commands/`)
y archivos de conocimiento (`.claude/knowledge/`). Un emprendedor clona el repo, entra a
`extension/` y ejecuta Claude Code para iniciar.

### RF-02: Metodología de 4 Fases

Cada fase tiene skills dedicados que no se pueden saltar. Fase 1 (diagnóstico, visión, poda,
finanzas), Fase 2 (canvas, fuerzas, entrevistas, validación), Fase 3 (investigación, PESCAR,
experimentos, lanzamiento), Fase 4 (factory, funnel, oferta mafia, ritmo semanal).

### RF-03: Voz y Vocabulario de Eduardo

Todas las interacciones usan el vocabulario luxurizante (inversión, creación, invitado,
condiciones especiales) y siguen los patrones de interacción (espejo antes que consejo,
escucha 70/30, sprezzatura, amortiguar-pivotar-ofrecer).

### RF-04: Grafo de Invitados

El sistema mantiene un registro local (`.kokoro/clients.json`) con perfiles de invitados,
segmentos, fases activas y cuentas conectadas. Nunca se sube a git.

### RF-05: Integración con Plataformas

Conexión vía MCP servers a Meta Ads, Google Ads, GA4, Google Search Console, Pipedrive
para consultar métricas reales y ejecutar campañas desde los skills transversales.

### RF-06: Ontología de Coaching

Grafo interno que rastrea el progreso del emprendedor por fases, skills completados,
y estado de coaching para dar contexto entre sesiones.

### RF-07: MCP Server

Servidor MCP que expone los skills de Kokoro como herramientas para Claude Desktop,
permitiendo uso fuera de Claude Code CLI.

### RF-08: Onboarding

Primera consulta profunda (`/kokoro-onboard`) que explora 7 dimensiones del emprendedor
antes de diagnosticar la fase correcta y registrar al invitado.
