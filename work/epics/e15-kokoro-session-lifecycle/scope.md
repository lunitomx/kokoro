---
epic_id: "E15"
title: "Kokoro Session Lifecycle"
status: "designed"
---

# Scope: E15 — Kokoro Session Lifecycle

## Objective

Darle a Kokoro un ciclo de sesion propio para trabajo con invitados.
Al abrir: cargar contexto, historial y proponer foco. Al cerrar: persistir
hallazgos, actualizar perfil y proponer siguiente paso. Hoy todo se pierde
entre sesiones. Despues de esta epica, Kokoro recuerda.

## Architecture Decisions

### AD-1: Session log por invitado (no global)

Cada invitado tiene su historial en `ClientProfile.metadata["session_log"]`.
No un log global — el contexto es siempre relativo al invitado.

Rationale: Cuando Eduardo abre sesion con Crescer, necesita el contexto de
Crescer, no de Deyanira. El grafo global (clients.json) ya existe para la
vista panoramica.

### AD-2: Hallazgos en metadata (no archivos sueltos)

Los hallazgos se persisten en metadata["session_log"] — una lista de
entradas con fecha, tipo y contenido. No archivos markdown separados.

Rationale: El perfil ya es el punto de verdad. metadata es dict[str, Any],
disenado para extensibilidad. Agregar archivos fragmenta la informacion.

### AD-3: Skills independientes (no refactorizar kokoro-session)

/kokoro-open y /kokoro-close son skills transversales nuevos.
/kokoro-session se queda como esta — es el mapa de progreso por fases.

Rationale: Separar responsabilidades. kokoro-session tiene funcion clara
(roadmap). Meterle el ciclo de sesion lo haria complejo.

### AD-4: /kokoro-open resuelve invitado + carga contexto + propone foco

No es solo "abrir sesion" — carga todo lo que Kokoro sabe y propone que
hacer hoy basado en historial + pendientes.

### AD-5: /kokoro-close persiste + reflexiona + propone siguiente

Captura que se hizo, que se aprendio, que hacer la proxima vez. El "next
session prompt" de Kokoro para el invitado.

## Stories

- [ ] S15.1 — Session log model: estructura de datos para historial por invitado (S)
- [ ] S15.2 — /kokoro-open: resolver invitado, cargar historial, proponer foco (S)
- [ ] S15.3 — /kokoro-close: persistir hallazgos, actualizar perfil, proponer siguiente (S)
- [ ] S15.4 — Integracion con skills existentes: kokoro-ads y kokoro-creative registran actividad (M)

## Story Details

### S15.1 — Session log model (S)

Definir la estructura de datos para el historial de sesiones por invitado:

```
metadata["session_log"] = [
    {
        "date": "2026-03-27",
        "type": "creative",
        "summary": "6 creativos Baby Balance, 2 publicos",
        "hallazgos": ["publico mamas responde a dolor 'no se si va bien'"],
        "artifacts": ["campanas/meta-ads/creativo-01-mamas.txt"],
        "next_action": "Lanzar campana en Meta Ads"
    }
]
```

Sin cambios al modelo Pydantic — metadata ya es dict[str, Any].
Documentar schema en knowledge file.

**Dependencies:** None
**Size:** S

### S15.2 — /kokoro-open (S)

Skill que al iniciar trabajo con un invitado:
1. Resuelve invitado del grafo (find_by_name)
2. Lee session_log de metadata (ultimas 5 sesiones)
3. Presenta: quien es, que se hizo la ultima vez, que quedo pendiente
4. Propone foco basado en: pendientes > fase actual > oportunidades
5. Si primera vez: "Primera sesion con {name}" + proponer diagnostico

Extension mirrors + knowledge file.

**Dependencies:** S15.1
**Size:** S

### S15.3 — /kokoro-close (S)

Skill que al cerrar trabajo con un invitado:
1. Pregunta (o infiere): que se hizo hoy, que se aprendio
2. Crea entrada en session_log con schema de S15.1
3. Actualiza metadata si se aprendio algo nuevo
4. Propone siguiente paso: "La proxima vez con {name}, hacer X porque Y"
5. Persiste con save_registry()

Extension mirrors.

**Dependencies:** S15.1
**Size:** S

### S15.4 — Integracion con skills existentes (M)

Que /kokoro-ads y /kokoro-creative registren automaticamente en el
session_log lo que generaron. Al final de cada skill, agregar entrada
sin que el usuario lo pida.

Actualizar:
- kokoro-ads.md — seccion Persistencia
- kokoro-creative.md — seccion Persistencia
- Documentar patron para que futuros skills lo sigan

**Dependencies:** S15.1, S15.2, S15.3
**Size:** M

## Dependency Graph

```
S15.1 (model) ──┬──> S15.2 (open)
                ├──> S15.3 (close)
                └──> S15.4 (integracion, depende de S15.2+S15.3 tambien)
```

S15.1 primero. S15.2 y S15.3 en paralelo. S15.4 al final.

## Scope Boundaries

### In (MUST)
- /kokoro-open carga contexto y propone foco
- /kokoro-close persiste hallazgos y propone siguiente
- Session log en metadata por invitado
- Persistencia automatica con save_registry

### In (SHOULD)
- Integracion con kokoro-ads y kokoro-creative
- Resumen de ultimas 3-5 sesiones al abrir

### No-Gos
- No modificar ClientProfile model (usar metadata)
- No refactorizar /kokoro-session existente
- No crear base de datos separada
- No analytics sobre sesiones (prematuro)
- No dashboard visual

### Rabbit Holes
- Analytics de sesiones — primero acumular datos
- Dashboard visual — no es CLI
- Migrar kokoro-session — funciona bien

## Done Criteria

- [ ] /kokoro-open carga historial y propone foco
- [ ] /kokoro-close persiste hallazgos y propone siguiente
- [ ] Session log acumulativo por invitado en metadata
- [ ] Al menos kokoro-ads y kokoro-creative registran actividad
- [ ] Probado con Crescer y Deyanira (invitados existentes)
- [ ] Skills base de Kokoro intactos (no regresiones)

## Risks

1. **metadata crece indefinidamente**
   Mitigation: limitar session_log a ultimas 20 entradas, rotar antiguas
2. **Session log sin estructura**
   Mitigation: S15.1 define schema claro antes de implementar
3. **Skills existentes se rompen**
   Mitigation: S15.4 es aditivo, no modifica logica existente
