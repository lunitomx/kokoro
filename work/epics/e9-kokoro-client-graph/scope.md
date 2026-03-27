# Epic E9: Kokoro Client Graph — Scope

> **Status:** IN PROGRESS
> **Created:** 2026-03-26

## Objective

Dar a Kokoro una memoria neurosimbolica de clientes: un grafo central donde
cada cliente es un nodo conectado a sus artefactos (campanas, repos, canvas,
segmentos). Kokoro recupera contexto completo de cualquier cliente al instante.

**Value:** Eduardo trabaja con multiples clientes sin perder contexto entre
sesiones. Lo aprendido con un cliente puede informar el trabajo con otro.

## Stories (5 estimated)

| ID | Story | Size | Status | Description |
|----|-------|:----:|:------:|-------------|
| S9.1 | Modelo de datos | S | Pending | ClientProfile, ClientRegistry (Pydantic models) |
| S9.2 | Persistence layer | S | Pending | clients.json + load/save atomico |
| S9.3 | Skill /kokoro-client | M | Pending | Crear, listar, ver, buscar clientes |
| S9.4 | Integracion con skills | M | Pending | kokoro-ads y otros leen cliente automatico |
| S9.5 | Sync con Rai memory | S | Pending | Generar reference_*.md desde el grafo |

**Total:** 5 stories

## Scope

**In scope (MUST):**
- Modulo src/kokoro/clients/ con modelos Pydantic (separado de ontology)
- ClientProfile: nombre, grupo, repos, carpetas, segmentos, contexto paths
- ClientRegistry: coleccion de clientes con busqueda
- Persistence en clientes/.kokoro/clients.json (central en RaizAncestral)
- Skill /kokoro-client para gestionar clientes
- Skills existentes pueden resolver cliente por nombre antes de operar
- Sync bidireccional con reference_*.md en memory de Rai

**In scope (SHOULD):**
- Cross-client search por segmento o industria
- Timeline de campanas por cliente
- Deteccion automatica de cliente por carpeta de trabajo

**Out of scope:**
- CRM features (pipeline, deals) → no es CRM
- Vector/RAG → simbolico puro
- UI web → CLI + skills es la interfaz
- Sincronizacion automatica de repos → lookup manual

## Done Criteria

**Per story:**
- [ ] Type annotations (pyright strict)
- [ ] Tests passing
- [ ] Quality checks pass (ruff, pyright)

**Epic complete:**
- [ ] All stories complete (S9.1-S9.5)
- [ ] Al mencionar "Konecta Park", Kokoro recupera contexto completo
- [ ] Grafo persistido en clients.json
- [ ] /kokoro-client skill funcional
- [ ] reference_*.md se genera del grafo
- [ ] Tests existentes siguen pasando
- [ ] Epic retrospective done
- [ ] Merged to main

## Dependencies

```
S9.1 (modelos)
  |
S9.2 (persistence)
  |
S9.3 (skill /kokoro-client) ──┐
  |                            |
S9.4 (integracion skills)      |
                               |
S9.5 (sync memory) ◄──────────┘
```

**External:** Ninguna. E3 ontology es referencia pero no se modifica.

## Architecture

**Decision: Modulo separado (no extender ontology E3)**

El ontology de E3 modela conceptos de coaching POR emprendedor (segmento,
problema, PUV, fuerza). El grafo de clientes modela la relacion de Eduardo
CON sus clientes. Son dominios distintos.

```
src/kokoro/
  ontology/          ← E3: coaching concepts (per entrepreneur)
    models.py        ← NodeType, EdgeType, CoachingState
    store.py         ← .kokoro/state.json per project
  clients/           ← E9: client graph (Eduardo's brain)
    models.py        ← ClientProfile, ClientRegistry
    store.py         ← clients.json central
    __init__.py
```

El ClientProfile NO usa NodeType/EdgeType de ontology — tiene sus propios
campos tipados. Pero puede LEER el CoachingState de un cliente si existe
(.kokoro/state.json en su proyecto).

**Estructura del ClientProfile:**

```python
class ClientProfile(BaseModel):
    id: str                          # "konecta-park"
    name: str                        # "Konecta Park"
    group: str                       # "invertikal"
    description: str                 # "Hub logistico Puerto Morelos"
    repos: list[str]                 # paths a repos
    campaign_folder: str             # path relativo en clientes/
    context_file: str | None         # path a contexto.md
    segments: list[str]              # ["brokers", "inversionistas"]
    industry: str                    # "real-estate-industrial"
    coaching_state_path: str | None  # path a .kokoro/state.json
    created: datetime
    updated: datetime
    metadata: dict[str, Any]         # datos clave (inventario, precios)

class ClientRegistry(BaseModel):
    version: int = 1
    clients: list[ClientProfile]
    created: datetime
    updated: datetime
```

No ADR formal — la decision es clara y sigue el patron existente.

## Risks

| Risk | L/I | Mitigation |
|------|:---:|------------|
| clients.json crece mucho con metadata de cada cliente | L/M | metadata es un dict libre — solo datos clave, no dumps completos |
| Skills no encuentran cliente si el nombre no matchea exacto | M/M | Fuzzy match simple: lowercase + contains |
| Sync con reference_*.md puede sobreescribir ediciones manuales | M/L | Generar solo si no existe o con flag --force |

## Implementation Plan

> Added by `/rai-epic-plan` — 2026-03-26

### Story Sequence

| Order | Story | Size | Dependencies | Milestone | Rationale |
|:-----:|-------|:----:|--------------|-----------|-----------|
| 1 | S9.1 — Modelo de datos | S | None | M1 | Foundation: sin modelos no hay nada |
| 2 | S9.2 — Persistence layer | S | S9.1 | M1 | Walking skeleton: modelos + persistence = grafo funcional |
| 3 | S9.3 — Skill /kokoro-client | M | S9.2 | M2 | Core MVP: Eduardo puede gestionar clientes |
| 4 | S9.4 — Integracion con skills | M | S9.3 | M2 | Valor real: skills leen cliente automatico |
| 5 | S9.5 — Sync con Rai memory | S | S9.2 | M3 | Cierre: reference_*.md se genera del grafo |

### Milestones

| Milestone | Stories | Success Criteria |
|-----------|---------|------------------|
| **M1: Walking Skeleton** | S9.1 + S9.2 | ClientProfile persiste en clients.json, load/save funciona |
| **M2: Core MVP** | + S9.3 + S9.4 | /kokoro-client crea clientes, /kokoro-ads lee contexto del cliente |
| **M3: Epic Complete** | + S9.5 | reference_*.md se genera del grafo, retro done |

### Parallel Work Streams

```
Time →
S9.1 ─► S9.2 ─► S9.3 ─► S9.4
              └──────► S9.5 (parallel with S9.3/S9.4)
```

S9.5 solo depende de S9.2 (persistence), asi que puede correr en paralelo
con S9.3/S9.4. Pero dado que es un solo developer, secuencial es mas simple.

### Progress Tracking

| Story | Size | Status | Actual | Notes |
|-------|:----:|:------:|:------:|-------|
| S9.1 — Modelo de datos | S | Pending | — | |
| S9.2 — Persistence layer | S | Pending | — | |
| S9.3 — Skill /kokoro-client | M | Pending | — | |
| S9.4 — Integracion con skills | M | Pending | — | |
| S9.5 — Sync con Rai memory | S | Pending | — | |

### Sequencing Risks

| Risk | L/I | Mitigation |
|------|:---:|------------|
| S9.4 requiere modificar skills existentes (kokoro-ads) que acaban de crearse | M/M | Cambio minimo: agregar lectura de cliente al inicio del skill |
| S9.5 puede conflictuar con reference_*.md editados manualmente | L/L | Solo genera si no existe, flag --force para sobreescribir |

## Parking Lot

- Cross-client ML patterns → futuro (Eduardo hace las conexiones con juicio)
- Auto-detect client from CWD → SHOULD, puede ir en S9.4 si es simple
- Migration tool para state.json existentes → manual primero
