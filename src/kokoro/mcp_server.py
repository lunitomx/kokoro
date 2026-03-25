"""Kokoro MCP Server — Eduardo's coaching skills for Claude Desktop.

Exposes all Kokoro coaching skills as MCP tools and coaching state
as MCP resources. Students and entrepreneurs connect from Claude Desktop
without installing packages.

Usage (Claude Desktop config):
    {
        "mcpServers": {
            "kokoro": {
                "command": "uvx",
                "args": ["kokoro-mcp"],
                "env": {"KOKORO_PROJECT_DIR": "~/Documents/mi-negocio"}
            }
        }
    }
"""

from __future__ import annotations

import os
from pathlib import Path

from mcp.server.fastmcp import FastMCP

from kokoro.ontology.store import (
    create_empty_state,
    get_skill_context,
    load_state,
    save_state,
)

# Initialize MCP server
mcp = FastMCP(
    "kokoro",
    instructions=(
        "Kokoro es la extension digital de Eduardo Munoz Luna. "
        "Usa la voz de Eduardo: metaforas, profundidad, sprezzatura. "
        "Usa 'creacion' no 'producto', 'invitado' no 'cliente', "
        "'inversion' no 'precio'. Escucha 70%, habla 30%."
    ),
)

# Resolve paths
_PROJECT_DIR = Path(
    os.environ.get("KOKORO_PROJECT_DIR", "~/Documents/kokoro")
).expanduser()

_EXTENSION_DIR = Path(__file__).resolve().parent.parent.parent / "extension"
_COMMANDS_DIR = _EXTENSION_DIR / ".claude" / "commands"
_KNOWLEDGE_DIR = _EXTENSION_DIR / ".claude" / "knowledge"
_CLAUDE_MD = _EXTENSION_DIR / ".claude" / "CLAUDE.md"

# Skill definitions: name → (file, description)
SKILLS: dict[str, tuple[str, str]] = {
    "kokoro_diagnose": (
        "kokoro-diagnose.md",
        "Diagnostico estrategico: Speed Boat + Vision 20/20",
    ),
    "kokoro_mountain": (
        "kokoro-mountain.md",
        "Montana del Manana: vision a 3 anos + OKRs",
    ),
    "kokoro_prune": (
        "kokoro-prune.md",
        "Podar el Arbol de Creaciones: foco sobre dispersion",
    ),
    "kokoro_finance": (
        "kokoro-finance.md",
        "Evaluacion financiera real: margen, CPA, ROI",
    ),
    "kokoro_canvas": (
        "kokoro-canvas.md",
        "Lean Canvas guiado por segmento",
    ),
    "kokoro_forces": (
        "kokoro-forces.md",
        "Customer Forces Model: las 4 fuerzas del invitado",
    ),
    "kokoro_interviews": (
        "kokoro-interviews.md",
        "Guia de entrevistas de validacion",
    ),
    "kokoro_validate": (
        "kokoro-validate.md",
        "Plan de validacion y diseno de experimentos",
    ),
    "kokoro_research": (
        "kokoro-research.md",
        "Investigacion multi-fuente: desk, social, competencia",
    ),
    "kokoro_pescar": (
        "kokoro-pescar.md",
        "Metodologia PESCAR: estrategia de contenido",
    ),
    "kokoro_experiment": (
        "kokoro-experiment.md",
        "Reporte de experimento 3x3x3: build-measure-learn",
    ),
    "kokoro_launch": (
        "kokoro-launch.md",
        "Lanzamiento: copy, landing, secuencia, playbook",
    ),
    "kokoro_factory": (
        "kokoro-factory.md",
        "Customer Factory Blueprint: sistema de crecimiento predecible",
    ),
    "kokoro_funnel": (
        "kokoro-funnel.md",
        "Funnel Consciente: embudo alineado con valores",
    ),
    "kokoro_mafia": (
        "kokoro-mafia.md",
        "Oferta Mafia: propuesta irresistible basada en fuerzas",
    ),
    "kokoro_rhythm": (
        "kokoro-rhythm.md",
        "Ritmo Semanal: 90 minutos + scorecard",
    ),
}


def _load_skill(skill_file: str) -> str:
    """Load a skill markdown file."""
    path = _COMMANDS_DIR / skill_file
    if not path.is_file():
        return f"Error: skill file {skill_file} not found."
    return path.read_text(encoding="utf-8")


def _load_identity() -> str:
    """Load Eduardo's identity from CLAUDE.md."""
    if _CLAUDE_MD.is_file():
        return _CLAUDE_MD.read_text(encoding="utf-8")
    return ""


def _build_context(skill_name: str) -> str:
    """Build context from coaching state for a skill."""
    state = load_state(_PROJECT_DIR)
    if state is None:
        return ""

    # Get relevant nodes from upstream skills
    dash_name = skill_name.replace("_", "-")
    nodes = get_skill_context(state, dash_name)
    if not nodes:
        return ""

    lines = ["\n---\n## Contexto del emprendedor (de sesiones anteriores)\n"]
    for node in nodes:
        lines.append(
            f"- **{node.type.value}** ({node.id}, via {node.source_skill}): "
            f"{node.content}"
        )
    return "\n".join(lines)


def _run_skill(skill_name: str) -> str:
    """Load skill content + identity + context."""
    skill_file = SKILLS[skill_name][0]
    identity = _load_identity()
    skill_content = _load_skill(skill_file)
    context = _build_context(skill_name)

    parts = []
    if identity:
        parts.append(identity)
    parts.append(skill_content)
    if context:
        parts.append(context)

    return "\n\n".join(parts)


# Register all skill tools dynamically
def _make_tool(name: str, description: str) -> None:
    """Register a skill as an MCP tool."""

    @mcp.tool(name=name, description=description)
    def skill_tool() -> str:  # type: ignore[reportUnusedFunction]
        return _run_skill(name)


for _name, (_file, _desc) in SKILLS.items():
    _make_tool(_name, _desc)


# Utility tools
@mcp.tool(
    name="kokoro_init",
    description="Inicializar el estado de coaching para un nuevo emprendedor",
)
def kokoro_init(negocio: str) -> str:
    """Create a new coaching state for an entrepreneur."""
    existing = load_state(_PROJECT_DIR)
    if existing is not None:
        return (
            f"Estado ya existe para '{existing.negocio}'. "
            f"Fase 1: {existing.phases[0].status}, "
            f"Fase 2: {existing.phases[1].status}, "
            f"Fase 3: {existing.phases[2].status}."
        )
    state = create_empty_state(negocio)
    save_state(_PROJECT_DIR, state)
    return (
        f"Estado de coaching creado para '{negocio}' en "
        f"{_PROJECT_DIR / '.kokoro' / 'state.json'}. "
        f"4 fases inicializadas. Usa kokoro_diagnose para comenzar."
    )


@mcp.tool(
    name="kokoro_progress",
    description="Ver el progreso del emprendedor en las 4 fases",
)
def kokoro_progress() -> str:
    """Show coaching progress across all phases."""
    state = load_state(_PROJECT_DIR)
    if state is None:
        return (
            "No hay estado de coaching. Usa kokoro_init para comenzar."
        )

    lines = [f"## Progreso de {state.negocio}\n"]
    for phase in state.phases:
        completed = [sc.skill for sc in phase.skills_completed]
        status_icon = (
            "Done" if phase.status == "done"
            else "En progreso" if phase.status == "in_progress"
            else "Pendiente"
        )
        lines.append(f"### Fase {phase.phase}: {phase.name} — {status_icon}")
        if completed:
            for sc in phase.skills_completed:
                lines.append(f"- {sc.skill}: {sc.summary}")
        else:
            lines.append("- (sin skills completados)")
        lines.append("")

    lines.append(f"**Nodos totales:** {len(state.nodes)}")
    lines.append(f"**Edges totales:** {len(state.edges)}")

    return "\n".join(lines)


# Resources
@mcp.resource("kokoro://state")
def coaching_state() -> str:
    """The current coaching state as JSON."""
    state = load_state(_PROJECT_DIR)
    if state is None:
        return '{"status": "no_state", "message": "Usa kokoro_init para comenzar"}'
    return state.model_dump_json(indent=2)


@mcp.resource("kokoro://methodology")
def methodology() -> str:
    """Eduardo's complete methodology overview."""
    path = _KNOWLEDGE_DIR / "kokoro-metodologia.md"
    if path.is_file():
        return path.read_text(encoding="utf-8")
    return "Methodology file not found."


def main() -> None:
    """Entry point for kokoro-mcp command."""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
