"""Persistence layer for client registry.

Reads/writes `.kokoro/clients.json` in the project directory.
Uses atomic write (temp file + rename) to prevent corruption.
"""

from __future__ import annotations

import contextlib
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from kokoro.clients.models import ClientRegistry

KOKORO_DIR = ".kokoro"
CLIENTS_FILE = "clients.json"


def _registry_path(project_dir: Path) -> Path:
    """Return the path to .kokoro/clients.json."""
    return project_dir / KOKORO_DIR / CLIENTS_FILE


def load_registry(project_dir: Path) -> ClientRegistry | None:
    """Load client registry from .kokoro/clients.json.

    Returns None if the file doesn't exist.
    """
    path = _registry_path(project_dir)
    if not path.is_file():
        return None
    content = path.read_text(encoding="utf-8")
    return ClientRegistry.model_validate_json(content)


def save_registry(project_dir: Path, registry: ClientRegistry) -> None:
    """Write client registry to .kokoro/clients.json atomically.

    Uses temp file + rename to prevent corruption on crash.
    """
    kokoro_dir = project_dir / KOKORO_DIR
    kokoro_dir.mkdir(parents=True, exist_ok=True)
    target = kokoro_dir / CLIENTS_FILE
    json_str = registry.model_dump_json(indent=2)

    fd, tmp_path_str = tempfile.mkstemp(
        dir=str(kokoro_dir), suffix=".tmp", prefix="clients_"
    )
    tmp_path = Path(tmp_path_str)
    try:
        tmp_path.write_text(json_str, encoding="utf-8")
        tmp_path.replace(target)
    except Exception:
        tmp_path.unlink(missing_ok=True)
        raise
    finally:
        with contextlib.suppress(OSError):
            os.close(fd)


def create_empty_registry() -> ClientRegistry:
    """Create an empty client registry."""
    now = datetime.now(tz=timezone.utc)
    return ClientRegistry(
        clients=[],
        created=now,
        updated=now,
    )
