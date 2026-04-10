# Scope — E34 Kokoro Skill Diet

## Objective

Reducir el peso cognitivo de los 51 skills de Kokoro sin perder calidad,
extrayendo instrucciones repetidas a knowledge compartido y aplicando
patrones de atención óptima (BASE-055).

## In Scope

- Auditoría de los 51 skills: tamaño, instrucciones duplicadas, bloques repetidos
- Creación de `kokoro-skill-commons.md` con instrucciones compartidas
- Refactorización de los skills para referenciar el commons en vez de duplicar
- Reorganización interna de skills siguiendo BASE-055 (U-shaped attention)
- Validación de que ningún skill pierde capacidad post-poda

## Out of Scope

- Pipeline engine / orquestadores de fase (E35)
- MCP o infraestructura compartida (E36)
- Creación de skills nuevos
- Cambios de lógica o flujo en skills existentes
- Cambios al CLAUDE.md principal

## Planned Stories

| ID | Nombre | Tamaño | Descripción |
|----|--------|--------|-------------|
| S34.1 | Audit | S | Medir todos los skills, detectar bloques duplicados, generar reporte |
| S34.2 | Commons | M | Crear kokoro-skill-commons.md con instrucciones extraídas |
| S34.3 | Refactor | L | Podar los skills reemplazando bloques duplicados por referencia al commons |
| S34.4 | Attention | S | Reorganizar estructura interna de skills para BASE-055 |

## Done Criteria

- [ ] Todos los skills auditados con métricas antes/después
- [ ] kokoro-skill-commons.md creado y referenciado
- [ ] Tamaño promedio de skill reducido en >20%
- [ ] Ningún skill pierde instrucciones (solo cambian de ubicación)
- [ ] Commit por cada story completada
- [ ] Retrospectiva de la épica completada
