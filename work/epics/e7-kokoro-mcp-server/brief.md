---
epic_id: "E7"
title: "Kokoro MCP Server para Claude Desktop"
status: "draft"
created: "2026-03-24"
---

# Epic Brief: Kokoro MCP Server para Claude Desktop

## Hypothesis
For emprendedores y estudiantes de Eduardo who cannot install CLI tools,
the Kokoro MCP Server is a local MCP service
that exposes all coaching skills as tools accessible from Claude Desktop.
Unlike the current pip-install model, our solution requires only adding
3 lines to Claude Desktop config.

## Success Metrics
- **Leading:** Un estudiante conecta Kokoro en <5 minutos sin ayuda técnica
- **Lagging:** 10+ estudiantes usando Kokoro via MCP sin tickets de soporte

## Appetite
M — 5-6 stories estimated

## Scope Boundaries
### In (MUST)
- MCP server que expone 10 skills como tools
- State persistence via .kokoro/state.json (reusa E3 store)
- Knowledge files servidos como MCP resources
- Instalable via uvx (1 comando)
- Configuración de Claude Desktop documentada (3 pasos)

### In (SHOULD)
- Coaching state legible como MCP resource (progreso visual)
- Tool para inicializar estado (`kokoro_init`)
- Tool para ver progreso (`kokoro_progress`)

### No-Gos
- No SaaS / no cloud — local-first siempre
- No autenticación — es un proceso local
- No reescritura de skills — wrapping del contenido existente
- No requiere Claude Code instalado

### Rabbit Holes
- Crear un UI web para Kokoro — MCP + Claude Desktop ES el UI
- Multitenancy — un server por emprendedor, no compartido
- Streaming de respuestas — MCP tools retornan el prompt, Claude hace el coaching
