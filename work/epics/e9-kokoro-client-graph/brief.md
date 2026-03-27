---
epic_id: "E9"
title: "Kokoro Client Graph — Memoria neurosimbolica por cliente"
status: "draft"
created: "2026-03-26"
---

# Epic Brief: Kokoro Client Graph — Memoria neurosimbolica por cliente

## Hypothesis
For Eduardo who coaches multiple clients and creates campaigns across projects,
the Kokoro Client Graph is a layer above the per-project ontology
that creates a node per client with edges to their artifacts (campaigns, canvas,
forces, repos), enabling Kokoro to recall any client's context instantly and
cross-pollinate patterns between clients.
Unlike the current system (flat memory references + isolated .kokoro/state.json
per project), our solution gives Eduardo a connected "brain" where each client
is a neuron linked to its knowledge and to patterns from other clients.

## Success Metrics
- **Leading:** Al mencionar "Konecta Park", Kokoro recupera contexto completo
  (inventario, campanas, repo, segmentos) sin que Eduardo re-explique
- **Lagging:** Eduardo trabaja con 5+ clientes y Kokoro mantiene contexto
  de todos sin perdida entre sesiones

## Appetite
M — 4-6 stories estimated

## Scope Boundaries
### In (MUST)
- Modelo ClientNode en la ontologia existente (nuevo NodeType)
- Persistence layer: archivo central de clientes (.kokoro/clients.json o similar)
  que vive en RaizAncestral (el proyecto "cerebro"), no en cada proyecto individual
- Cada cliente tiene: nombre, grupo (invertikal, escuela-libre), repo(s),
  carpeta de campanas, contexto.md path, segmentos, estado del coaching
- Skills existentes (/kokoro-ads, /kokoro-canvas, etc.) pueden leer el
  contexto del cliente antes de iniciar
- Integrar con el memory system de Rai (reference_*.md) — el grafo alimenta
  los archivos de referencia automaticamente

### In (SHOULD)
- Cross-client patterns: lo aprendido en un cliente informa a otro
  (ej: "esta audiencia funciono para Konecta → probala para Invertikal")
- Busqueda por segmento: "dame todos los clientes que venden a brokers"
- Timeline de campanas por cliente

### No-Gos
- No SaaS / no cloud — local-first siempre
- No reemplazar .kokoro/state.json por proyecto — el grafo de clientes
  ES un nivel arriba, no un reemplazo
- No UI web — los skills y el CLI son la interfaz
- No vector/RAG — esto es simbolico, grafos con nodos y aristas tipados

### Rabbit Holes
- Construir un CRM completo — esto es un grafo de conocimiento, no un CRM
- Sincronizacion automatica con repos de clientes — es lookup manual por ahora
- Machine learning sobre patrones entre clientes — las conexiones las hace
  Eduardo con juicio, no un algoritmo
- Migracion automatica de state.json existentes — hazlo manual primero
