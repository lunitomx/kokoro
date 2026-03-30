---
epic_id: "E19"
title: "Kokoro Distribution — Proyecto limpio instalable"
status: "designed"
---

# Scope: E19 — Kokoro Distribution

## Objective

Crear una versión limpia y distribuible de Kokoro en `github.com/lunitomx/kokoro`
que cualquier usuario pueda instalar, configurar, y empezar a usar con Claude Code.
Proyecto en blanco: sin datos de clientes, sin epics, sin estado de sesión.

## Value

- Primera usuaria puede instalar Kokoro y arrancar con `/kokoro`
- Eduardo puede enviar actualizaciones con un simple push
- Base para crecer la comunidad de usuarios de Kokoro
- Separación limpia entre el framework (distribuible) y los datos (privados por usuario)

## Architecture Decisions

### AD-1: GitHub repo como canal de distribución (no PyPI)

El corazón de Kokoro son 43 skills `.md` + CLAUDE.md + knowledge docs. Esto no es
un paquete Python tradicional — es una extensión de Claude Code. GitHub es el canal
natural: clonas, configuras, usas.

Rationale: PyPI sirve para librerías Python. Kokoro es prompts + Python. El modelo
de distribución es más parecido a un dotfiles repo que a un pip package.

### AD-2: Script de instalación `kokoro install`

Un comando que:
1. Copia skills a `.claude/commands/` del usuario
2. Configura CLAUDE.md en el proyecto del usuario
3. Inicializa `.kokoro/clients.json` vacío
4. Verifica dependencias (Claude Code instalado, Python 3.10+)

Rationale: El usuario no debería tener que copiar archivos manualmente.
Un solo comando y listo.

### AD-3: Separar RaizAncestral (privado) de Kokoro (público)

RaizAncestral es el monorepo de Eduardo: clientes, epics, governance, transcripts.
Kokoro es el framework extraído. El repo público NO contiene:
- `clientes/` — datos de invitados
- `work/` — epics y stories de Eduardo
- `.raise/` — estado de RaiSE
- `dev/` — parking lot, problem briefs
- `governance/` — docs internos de Eduardo
- `conocimientoraiz/` — material de cursos (IP)
- `.env` — secrets

Rationale: Lo privado se queda en RaizAncestral. Lo público es el motor.

### AD-4: Actualizaciones via git pull + kokoro update

El usuario hace `git pull` para bajar cambios y `kokoro update` para re-copiar
skills actualizados a su `.claude/commands/`. Sin versioning complejo por ahora.

Rationale: Simplicidad. Versioning semántico puede venir después si hay demanda.

## Stories

- [ ] S19.1 — Definir estructura del repo limpio: qué archivos van, qué se excluye (S)
- [ ] S19.2 — Crear CLAUDE.md distribuible: sin referencias a RaizAncestral, Eduardo, ni clientes específicos (M)
- [ ] S19.3 — Crear `kokoro install` + `kokoro update`: script de instalación y actualización (M)
- [ ] S19.4 — Limpiar y copiar skills: 43 commands + knowledge docs al repo limpio (S)
- [ ] S19.5 — README + guía de inicio: instalación, primer uso, qué es cada fase (S)
- [ ] S19.6 — Push a lunitomx/kokoro + verificar instalación limpia (S)

## Story Details

### S19.1 — Estructura del repo limpio (S)

Definir el file tree exacto del repo distribuible:
```
kokoro/
├── .claude/
│   ├── CLAUDE.md          # Identidad + voz + metodología
│   └── commands/           # 43 skills kokoro-*.md
│       └── kokoro-*.md
├── knowledge/              # Knowledge docs por skill
├── src/kokoro/             # Python: CLI, ontología, clients, MCP
├── tests/                  # Test suite
├── .kokoro/
│   └── clients.json        # Vacío: {"clients": []}
├── pyproject.toml
├── .gitignore
└── README.md
```

**Dependencies:** None
**Size:** S

### S19.2 — CLAUDE.md distribuible (M)

Adaptar `.claude/CLAUDE.md` para que funcione sin contexto de RaizAncestral:
- Mantener identidad de Eduardo, voz, arquetipos, metodología
- Remover referencias a clientes específicos (Invertikal, Konecta, Legacy)
- Remover referencias a RaiSE (epics, stories, gates)
- Agregar sección de onboarding para nuevos usuarios
- Mantener anti-patrones y vocabulario luxurizante intactos

**Dependencies:** S19.1
**Size:** M

### S19.3 — `kokoro install` + `kokoro update` (M)

CLI commands que:
- `kokoro install`: copia skills + CLAUDE.md + knowledge al proyecto del usuario
- `kokoro update`: re-copia skills actualizados (preservando clients.json del usuario)
- Verificación: Claude Code disponible, Python 3.10+
- Idempotente: correr install dos veces no rompe nada

**Dependencies:** S19.1
**Size:** M

### S19.4 — Limpiar y copiar skills + knowledge (S)

Copiar los 43 skills y knowledge docs al repo limpio. Verificar que:
- Ningún skill referencia paths de RaizAncestral
- Ningún skill menciona clientes específicos por nombre
- Cross-references entre skills funcionan (`/kokoro-X` apunta a skills que existen)

**Dependencies:** S19.1
**Size:** S

### S19.5 — README + guía de inicio (S)

README.md con:
- Qué es Kokoro (1 párrafo, voz de Eduardo)
- Instalación (3 pasos)
- Primer uso: `/kokoro` para diagnóstico de fase
- Las 4 fases con sus skills
- Requisitos: Claude Code, Python 3.10+

**Dependencies:** S19.2, S19.4
**Size:** S

### S19.6 — Push + verificar instalación limpia (S)

Push a `github.com/lunitomx/kokoro`. Verificar:
1. Clone en directorio limpio
2. `pip install -e .`
3. `kokoro install`
4. Abrir Claude Code, correr `/kokoro`
5. Confirmar que funciona sin RaizAncestral

**Dependencies:** S19.3, S19.5
**Size:** S

## Dependency Graph

```
S19.1 (estructura) ──┬──> S19.2 (CLAUDE.md) ──┬──> S19.5 (README)──> S19.6 (push+verify)
                      ├──> S19.3 (install CLI) ─┘                         ↑
                      └──> S19.4 (skills)  ────────────────────────────────┘
```

## Scope Boundaries

### In (MUST)
- Repo limpio sin datos privados
- Script de instalación funcional
- 43 skills + knowledge docs
- CLAUDE.md con identidad completa
- README con guía de inicio

### In (SHOULD)
- Tests que pasen en el repo limpio
- `kokoro update` para actualizaciones

### No-Gos
- No PyPI por ahora (complejidad innecesaria)
- No versioning semántico (premature)
- No CI/CD (se agrega si hay demanda)
- No modificar RaizAncestral — el repo público es una extracción, no un refactor
- No incluir material de cursos (conocimientoraiz/ es IP)

### Rabbit Holes
- Sistema de plugins/extensiones — prematuro
- Marketplace de skills — mucho después
- Auto-update daemon — innecesario, git pull basta

## Done Criteria

- [ ] Repo `lunitomx/kokoro` público con estructura limpia
- [ ] `kokoro install` funciona en un directorio vacío
- [ ] `/kokoro` responde correctamente sin datos previos
- [ ] Ningún dato privado en el repo (clientes, .env, transcripts, epics)
- [ ] README permite a un nuevo usuario arrancar en <5 minutos

## Risks

1. **Skills referencian contexto privado** — Mitigation: grep por nombres de clientes y paths de RaizAncestral antes de copiar
2. **Tests dependen de fixtures con datos privados** — Mitigation: S19.4 verifica que tests pasen sin clientes/
3. **CLAUDE.md pierde personalidad al limpiar** — Mitigation: S19.2 preserva voz y arquetipos, solo limpia referencias específicas
