# Kokoro — Lo que construimos

> Documento resumen del Epic E1: Kokoro Phase 1 — Preparar el Suelo
> Completado: 2026-03-09

---

## Qué es Kokoro

Kokoro es una **extensión para Claude Code** que transforma a Claude en Eduardo Muñoz Luna — un estratega de marketing con filosofía ancestral. No es un chatbot genérico: es un clon de la voz, la metodología y la personalidad de Eduardo, empaquetado como herramienta de trabajo para emprendedores.

**Una línea:** `pip install` → `kokoro init` → Claude habla como Eduardo y guía al emprendedor por la Fase 1 de estrategia de negocio.

---

## Qué logra

### Para el emprendedor
Un emprendedor instala Kokoro y obtiene acceso a **6 sesiones guiadas** de la Fase 1 "Preparar el Suelo":

| Skill | Qué hace | Metodología |
|-------|----------|-------------|
| `/kokoro` | Punto de entrada — diagnostica dónde estás y te dirige al skill correcto | Router inteligente |
| `/kokoro-session` | Gestiona tu progreso — inicia, continúa o revisa tu avance en Fase 1 | Gestión de sesiones |
| `/kokoro-diagnose` | Sesión guiada de diagnóstico empresarial | Speed Boat + Vision 20/20 |
| `/kokoro-mountain` | Define tu visión y objetivos estratégicos | Montaña del Mañana + OKRs |
| `/kokoro-prune` | Evalúa y prioriza tu portafolio de productos | Podar el Árbol de Productos |
| `/kokoro-finance` | Evaluación financiera real de tu negocio | Inventario Financiero + CPA/LTV/ROI |

### La experiencia
1. El emprendedor escribe `/kokoro` en Claude Code
2. Eduardo (via Claude) le pregunta con respeto si quiere ser guiado (estrategia del Proyector)
3. Con 3-4 preguntas diagnósticas, identifica en qué punto de la Fase 1 está
4. Lo dirige al skill correcto
5. El skill lo guía paso a paso con ejercicios concretos, preguntas y templates de resumen

### La voz de Eduardo
Claude no responde como asistente genérico. Responde como Eduardo:
- **Proyector 1/3** — espera invitación antes de guiar
- **Eneagrama 3w4** — logro con profundidad artística
- **Vocabulario propio** — "inversión" (no gasto), "creación" (no producto), "invitado" (no cliente)
- **Filosofía** — la riqueza es material, espiritual y ética
- **Anti-patrones** — nunca dice "deberías", nunca usa jargon corporativo vacío

---

## Qué construimos (técnicamente)

### Paquete Python
```
src/kokoro/
├── __init__.py          # Package metadata
└── cli.py               # kokoro init CLI (139 líneas)

extension/.claude/
├── CLAUDE.md            # Eduardo's brain (213 líneas)
├── commands/
│   ├── kokoro.md              # Router skill
│   ├── kokoro-session.md      # Session manager
│   ├── kokoro-diagnose.md     # Speed Boat + Vision 20/20
│   ├── kokoro-mountain.md     # Montaña del Mañana + OKRs
│   ├── kokoro-prune.md        # Podar el Árbol
│   └── kokoro-finance.md      # Evaluación Financiera
└── knowledge/
    ├── kokoro-metodologia.md          # 4-phase overview
    ├── kokoro-phase1-diagnostico.md   # Speed Boat + Vision 20/20
    ├── kokoro-phase1-vision.md        # Montaña del Mañana + OKRs
    ├── kokoro-phase1-poda.md          # Prune the Product Tree
    └── kokoro-phase1-finanzas.md      # Financial evaluation
```

### Cómo funciona
1. `pip install git+https://github.com/lunitomx/nitido.git` — instala el paquete
2. `kokoro init` — copia la extensión a `.claude/` del proyecto del usuario
3. Claude Code carga automáticamente `CLAUDE.md` (la personalidad) y los knowledge files
4. El usuario escribe `/kokoro-diagnose` (o cualquier skill) y Claude responde como Eduardo

### Mecanismo inteligente de copia
- Archivos que empiezan con `kokoro-` o `kokoro.` → propiedad de Kokoro, se actualizan en cada `kokoro init`
- Otros archivos del usuario → no se tocan, nunca se sobrescriben
- `CLAUDE.md` existente → se fusiona usando marcadores `<!-- KOKORO START/END -->`

---

## Números

| Métrica | Valor |
|---------|-------|
| Stories completadas | 8/8 |
| Tests | 159 |
| Errores pyright | 0 |
| Violaciones ruff | 0 |
| Defectos QR detectados | 2 (corregidos antes de merge) |
| Líneas de Python | ~300 (cli.py + tests) |
| Líneas de contenido | ~1,500 (skills + knowledge + CLAUDE.md) |
| Patrones descubiertos | 9 (PAT-L-001 a PAT-L-009) |
| Tiempo | ~1 semana (2026-03-02 a 2026-03-09) |

---

## Lo que falta (futuro)

| Epic | Fase | Skills |
|------|------|--------|
| E2 | Diseñar el Árbol | Canvas, fuerzas, entrevistas, validación |
| E3 | Plantar y Regar | Research, pescar, experimento, lanzamiento |
| E4 | Cosechar | Fábrica, funnel, mafia, ritmo |

---

## Instalación

```bash
# Instalar
pip install git+https://github.com/lunitomx/nitido.git

# Activar en tu proyecto
cd tu-proyecto
kokoro init

# Usar
# En Claude Code, escribe /kokoro para comenzar
```
