# System Context: RaizAncestral (Kokoro)

> External actors and system interfaces (C4 Context level)

## Actors

| Actor | Type | Description |
|-------|------|-------------|
| Emprendedor | Human | Invitado que recorre las 4 fases de la metodología |
| Eduardo Muñoz Luna | Human | Operador y guardián de la metodología — configura skills, atiende invitados |
| Claude Code | System | Runtime que ejecuta los skills de Kokoro |
| Claude Desktop | System | Cliente alternativo que consume el MCP server |

## External Systems

| System | Interface | Direction | Purpose |
|--------|-----------|-----------|---------|
| Meta Ads API | MCP (facebook-ads) | Bidirectional | Consultar métricas de campañas, crear audiencias, gestionar ads |
| Google Ads API | MCP (google-ads) | Bidirectional | Campañas de búsqueda, keywords, performance |
| Google Analytics 4 | MCP (google-analytics) | Read | Métricas de sitio web, comportamiento de usuarios |
| Google Search Console | MCP (google-search-console) | Read | Indexación, queries de búsqueda, rendimiento SEO |
| Pipedrive CRM | MCP (pipedrive) | Bidirectional | Gestión de deals, contactos, pipeline de ventas |
| GitHub | Git remote | Push/Pull | Distribución del repositorio público |
| Local filesystem | `.kokoro/` | Read/Write | Grafo de invitados, estado de coaching, configuración local |

## Data Flow

```
Emprendedor → Claude Code → Kokoro Skills → Plataformas (vía MCP)
                                ↓
                         .kokoro/ (estado local)
                                ↓
                         Ontología de coaching
```
