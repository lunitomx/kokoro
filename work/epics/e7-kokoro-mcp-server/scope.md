# Epic E7: Kokoro MCP Server para Claude Desktop — Scope

> **Status:** PLANNED
> **Created:** 2026-03-24
> **Problem Brief:** `dev/problem-briefs/e7-kokoro-mcp-server.md`

## Objective

Hacer Kokoro accesible a cualquier emprendedor o estudiante desde Claude Desktop
sin instalación técnica. Exponer los 10 skills como MCP tools y el estado de
coaching como MCP resources, instalable con un solo comando.

**Value:** Multiplica el alcance de Kokoro de "developers que usan Claude Code"
a "cualquier persona con Claude Desktop". Eduardo puede distribuir a 100+
estudiantes con 3 líneas de configuración.

## Stories

| ID | Story | Size | Status | Description |
|----|-------|:----:|:------:|-------------|
| S7.1 | MCP Server Skeleton | M | Pending | Servidor MCP base con mcp Python SDK, registro de tools |
| S7.2 | Skill Tools | M | Pending | 10 tools que cargan y retornan skill markdown + contexto |
| S7.3 | State Resources | S | Pending | MCP resources para coaching state + progreso |
| S7.4 | Knowledge Resources | S | Pending | Archivos de conocimiento como MCP resources legibles |
| S7.5 | Distribution + Config | S | Pending | Empaquetado uvx, documentación de configuración |
| S7.6 | Integration Tests | S | Pending | Tests E2E del MCP server, backward compat |

**Total:** 6 stories

## Scope

**In scope (MUST):**
- MCP server en Python usando mcp SDK
- 10 tools: kokoro_diagnose, kokoro_mountain, kokoro_prune, kokoro_finance,
  kokoro_canvas, kokoro_forces, kokoro_interviews, kokoro_validate,
  kokoro_session, kokoro_router
- Cada tool retorna el contenido del skill .md + contexto de state.json
- State persistence: reusa kokoro.ontology.store (E3)
- 2 tools utilitarios: kokoro_init (crear estado), kokoro_progress (ver progreso)
- Instalable via `uvx kokoro-mcp` o `pip install kokoro[mcp]`
- Documentación: 3 pasos para configurar en Claude Desktop

**In scope (SHOULD):**
- MCP resources: state.json como recurso legible
- MCP resources: knowledge files como recursos
- Prompt caching: CLAUDE.md (identidad Eduardo) como system prompt persistente
- Configurable: path del proyecto del emprendedor

**Out of scope:**
- Web UI (Claude Desktop ES el UI)
- Cloud/SaaS/autenticación
- Reescritura de skills (wrapping solamente)
- Claude Code integration (ya funciona via extensión)
- Fase 3/4 skills (eso es E5/E6)

## Done Criteria

**Per story:**
- [ ] Tests pass (pyright, ruff, pytest)
- [ ] Commit after each task

**Epic complete:**
- [ ] MCP server arranca y registra 12 tools (10 skills + init + progress)
- [ ] Claude Desktop puede listar y llamar los tools
- [ ] Un tool retorna skill markdown + contexto previo del emprendedor
- [ ] State se persiste entre sesiones de Claude Desktop
- [ ] Instalable via uvx en <30 segundos
- [ ] Documentación de 3 pasos para estudiantes
- [ ] Todos los tests existentes (365+) siguen pasando
- [ ] Epic retrospective done

## Architecture

```
┌─────────────────────┐
│   Claude Desktop    │
│   (UI del usuario)  │
└──────────┬──────────┘
           │ MCP Protocol (stdio)
           ▼
┌─────────────────────┐
│  kokoro-mcp server  │
│                     │
│  Tools:             │
│  - kokoro_diagnose  │
│  - kokoro_mountain  │
│  - kokoro_canvas    │
│  - ... (10 skills)  │
│  - kokoro_init      │
│  - kokoro_progress  │
│                     │
│  Resources:         │
│  - state.json       │
│  - knowledge/*.md   │
└──────────┬──────────┘
           │ File I/O
           ▼
┌─────────────────────┐
│  ~/.kokoro/         │
│  ├── state.json     │
│  └── (entrepreneur  │
│       coaching data)│
└─────────────────────┘
```

**Key decisions:**
- **stdio transport** — estándar para Claude Desktop MCP
- **Skills como tools** — cada tool carga el .md y lo retorna como prompt
  con contexto previo del state.json pre-inyectado
- **State en ~/.kokoro/** — sin "proyecto", el estado vive en home del usuario
  (configurable via env var KOKORO_PROJECT_DIR)
- **CLAUDE.md como system context** — la identidad de Eduardo se inyecta como
  prefijo en cada tool response para mantener la voz

## Dependencies

```
S7.1 (skeleton) → S7.2 (skill tools) → S7.3 (state resources)
                                         S7.4 (knowledge resources)
                   S7.5 (distribution, needs S7.2)
S7.6 (integration tests, runs last)
```

- S7.1 first: MCP server base must exist
- S7.2 after S7.1: tools need the server framework
- S7.3/S7.4 after S7.2: resources augment tools
- S7.5 after S7.2: packaging needs working tools
- S7.6 last: E2E validates everything

**External:** mcp Python SDK (pip install mcp)

## Risks

| Risk | L/I | Mitigation |
|------|:---:|------------|
| MCP SDK API changes | M/M | Pin version, test against specific Claude Desktop version |
| Tool response too large (skill .md + context) | M/M | Truncate context to most relevant nodes |
| State path confusion (no "project" concept) | M/L | Default to ~/.kokoro/, configurable via env var |
| Eduardo voice diluted in MCP tool format | L/H | Inject CLAUDE.md identity as prefix in every response |
| Claude Desktop limits on tool count | L/M | 12 tools is well within typical MCP limits |

## Implementation Plan

### Story Sequence

| Order | Story | Size | Dependencies | Rationale |
|:-----:|-------|:----:|-------------|-----------|
| 1 | S7.1 MCP Server Skeleton | M | None | Walking skeleton: server must exist first |
| 2 | S7.2 Skill Tools | M | S7.1 | Core value: skills accessible via MCP |
| 3 | S7.3 State Resources | S | S7.2 | Augments tools with coaching state visibility |
| 4 | S7.4 Knowledge Resources | S | S7.2 | Augments tools with methodology depth |
| 5 | S7.5 Distribution + Config | S | S7.2 | Packaging for end-user deployment |
| 6 | S7.6 Integration Tests | S | S7.3, S7.4, S7.5 | E2E validation |

### Milestones

| Milestone | Stories | Success Criteria |
|-----------|---------|------------------|
| **M1: Server Runs** | S7.1 | MCP server starts, registers tools, responds to list_tools |
| **M2: Skills Work** | +S7.2 | All 10 skills callable, return markdown + context |
| **M3: Full Package** | +S7.3-S7.5 | Resources, uvx install, 3-step docs |
| **M4: Epic Complete** | +S7.6 | E2E tests, retrospective |

### Progress Tracking

| Story | Size | Status | Actual | Notes |
|-------|:----:|:------:|:------:|-------|
| S7.1 MCP Server Skeleton | M | Pending | | |
| S7.2 Skill Tools | M | Pending | | |
| S7.3 State Resources | S | Pending | | |
| S7.4 Knowledge Resources | S | Pending | | |
| S7.5 Distribution + Config | S | Pending | | |
| S7.6 Integration Tests | S | Pending | | |

### Claude Desktop Config (end state)

```json
{
  "mcpServers": {
    "kokoro": {
      "command": "uvx",
      "args": ["kokoro-mcp"],
      "env": {
        "KOKORO_PROJECT_DIR": "~/Documents/mi-negocio"
      }
    }
  }
}
```

3 pasos para el estudiante:
1. Instalar uv: `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. Agregar config arriba a Claude Desktop settings
3. Reiniciar Claude Desktop → Kokoro aparece como herramienta disponible
