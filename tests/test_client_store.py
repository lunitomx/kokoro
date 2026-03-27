"""Tests for client registry persistence."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import pytest

from kokoro.clients.models import ClientProfile, ClientRegistry
from kokoro.clients.store import (
    create_empty_registry,
    load_registry,
    save_registry,
)


class TestLoadRegistry:
    """Loading registry from disk."""

    def test_returns_none_when_no_file(self, tmp_path: Path) -> None:
        """No file → None."""
        result = load_registry(tmp_path)
        assert result is None

    def test_loads_saved_registry(self, tmp_path: Path) -> None:
        """Round-trip: save then load."""
        now = datetime.now(tz=timezone.utc)
        registry = ClientRegistry(
            clients=[
                ClientProfile(
                    id="test-client",
                    name="Test Client",
                    group="test-group",
                    created=now,
                    updated=now,
                ),
            ],
            created=now,
            updated=now,
        )
        save_registry(tmp_path, registry)
        loaded = load_registry(tmp_path)
        assert loaded is not None
        assert len(loaded.clients) == 1
        assert loaded.clients[0].id == "test-client"
        assert loaded.clients[0].name == "Test Client"


class TestSaveRegistry:
    """Saving registry to disk."""

    def test_creates_kokoro_dir(self, tmp_path: Path) -> None:
        """Creates .kokoro/ directory if missing."""
        registry = create_empty_registry()
        save_registry(tmp_path, registry)
        assert (tmp_path / ".kokoro" / "clients.json").is_file()

    def test_overwrites_existing(self, tmp_path: Path) -> None:
        """Saving twice overwrites cleanly."""
        now = datetime.now(tz=timezone.utc)
        reg1 = create_empty_registry()
        save_registry(tmp_path, reg1)

        reg2 = ClientRegistry(
            clients=[
                ClientProfile(
                    id="new",
                    name="New Client",
                    group="g",
                    created=now,
                    updated=now,
                ),
            ],
            created=now,
            updated=now,
        )
        save_registry(tmp_path, reg2)
        loaded = load_registry(tmp_path)
        assert loaded is not None
        assert len(loaded.clients) == 1
        assert loaded.clients[0].id == "new"


class TestCreateEmptyRegistry:
    """Creating empty registry."""

    def test_empty_has_no_clients(self) -> None:
        """New registry starts empty."""
        reg = create_empty_registry()
        assert len(reg.clients) == 0
        assert reg.version == 1

    def test_has_timestamps(self) -> None:
        """New registry has created/updated timestamps."""
        reg = create_empty_registry()
        assert reg.created is not None
        assert reg.updated is not None
