"""Sync client registry to Rai memory system.

Generates reference_*.md files from ClientProfile data,
maintaining compatibility with the Rai memory format.
"""

from __future__ import annotations

from pathlib import Path

from kokoro.clients.models import ClientProfile, ClientRegistry


def _slugify(name: str) -> str:
    """Convert client name to file slug."""
    return name.lower().replace(" ", "_").replace("-", "_")


def generate_reference_md(client: ClientProfile) -> str:
    """Generate reference markdown content from a ClientProfile."""
    segments_str = ", ".join(client.segments) if client.segments else "none"
    repos_str = "\n".join(f"- {r}" for r in client.repos) if client.repos else "- none"

    metadata_lines: list[str] = []
    for key, value in client.metadata.items():
        metadata_lines.append(f"- {key}: {value}")
    metadata_str = "\n".join(metadata_lines) if metadata_lines else "- none"

    return f"""---
name: {client.name}
description: {client.description or f'Cliente {client.group}'}
type: reference
---

{client.name} ({client.group}) — {client.description}

**Grupo:** {client.group}
**Industria:** {client.industry or 'no especificada'}
**Segmentos:** {segments_str}
**Carpeta campanas:** {client.campaign_folder or 'no configurada'}
**Contexto:** {client.context_file or 'no configurado'}

**Repos:**
{repos_str}

**Datos clave:**
{metadata_str}

**How to apply:** Leer contexto del cliente antes de generar contenido. Verificar datos actuales en el repo.
"""


def sync_to_memory(
    registry: ClientRegistry,
    memory_dir: Path,
    *,
    force: bool = False,
) -> list[Path]:
    """Sync client registry to Rai memory directory.

    Generates reference_*.md for each client. Does not overwrite
    existing files unless force=True.

    Returns list of created/updated file paths.
    """
    memory_dir.mkdir(parents=True, exist_ok=True)
    created: list[Path] = []

    for client in registry.clients:
        slug = _slugify(client.name)
        ref_file = memory_dir / f"reference_{slug}.md"

        if ref_file.exists() and not force:
            continue

        content = generate_reference_md(client)
        ref_file.write_text(content, encoding="utf-8")
        created.append(ref_file)

    return created
