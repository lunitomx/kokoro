# System Design: RaizAncestral (Kokoro)

> Internal component architecture (C4 Container level)

## Components

| Component | Path | Responsibility |
|-----------|------|----------------|
| CLI | `src/kokoro/cli.py` | Entry point `kokoro init` — copies extension skills/knowledge into target project |
| Client Registry | `src/kokoro/clients/` | Models (`ClientProfile`, `ClientRegistry`), persistent store, sync to memory index |
| MCP Server | `src/kokoro/mcp_server.py` | FastMCP server exposing skills as tools for Claude Desktop |
| Ontology | `src/kokoro/ontology/` | Coaching state graph — nodes, edges, phase progress, skill completions |
| Extension | `extension/.claude/` | Distributable package — 46 skill commands + 30 knowledge files + CLAUDE.md identity |
| Tests | `tests/` | Skill content validation — vocabulary, structure, Eduardo's voice, anti-patterns |

## Extension Structure

```
extension/
  .claude/
    CLAUDE.md            # Identidad completa de Kokoro
    commands/            # 46 skills (markdown prompts)
      kokoro-onboard.md
      kokoro-diagnose.md
      kokoro-canvas.md
      ...
    knowledge/           # 30 archivos de conocimiento
      kokoro-methodology.md
      kokoro-vocabulary.md
      kokoro-onboard-methodology.md
      ...
```

## Key Design Decisions

1. **Skills as prompts, not code**: Los skills son archivos markdown que Claude Code interpreta — zero runtime dependencies para el emprendedor
2. **Local-first state**: `.kokoro/` almacena todo el estado del invitado localmente — sin servidor, sin cuenta, sin dependencias externas
3. **MCP para plataformas**: Las integraciones con Meta Ads, GA4, etc. se conectan vía MCP servers registrados en `.raise/mcp/`
4. **Ontology as coaching memory**: El grafo de ontología persiste el progreso entre sesiones para dar continuidad
5. **CLI para distribución**: `kokoro init` copia la extensión al proyecto destino, mergeando CLAUDE.md sin sobreescribir
