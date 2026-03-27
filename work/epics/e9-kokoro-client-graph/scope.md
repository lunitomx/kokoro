---
epic_id: "E9"
title: "Kokoro Client Graph — Memoria neurosimbolica por cliente"
status: "planned"
---

# Scope: E9 — Kokoro Client Graph

## Objective
Crear una capa de memoria neurosimbolica que conecte todos los clientes de
Eduardo en un grafo central. Cada cliente es un nodo con aristas a sus
artefactos (campanas, canvas, repos, segmentos). Kokoro puede recuperar
el contexto de cualquier cliente al instante y detectar patrones cruzados.

## In Scope
- Modelo ClientNode + ClientEdge en ontologia existente
- Archivo central de clientes en RaizAncestral
- Integracion con skills existentes (leer contexto antes de empezar)
- Sincronizacion con memory system de Rai
- CRUD basico de clientes via skills o CLI

## Out of Scope
- UI web / dashboard
- Vector/RAG — esto es simbolico
- CRM features (pipeline, deals, invoicing)
- Sincronizacion automatica de repos

## Planned Stories
- [ ] S9.1 — Modelo de datos: ClientNode, ClientEdge, ClientRegistry
- [ ] S9.2 — Persistence layer: clients.json + load/save
- [ ] S9.3 — Skill /kokoro-client (crear, listar, ver, conectar clientes)
- [ ] S9.4 — Integracion con skills existentes (kokoro-ads, kokoro-canvas leen cliente)
- [ ] S9.5 — Sync con Rai memory (reference_*.md se genera del grafo)

## Done Criteria
- Kokoro recupera contexto completo de un cliente al mencionarlo
- Grafo de clientes persistido en RaizAncestral
- Skills existentes leen contexto del cliente antes de generar output
- Tests pasan
