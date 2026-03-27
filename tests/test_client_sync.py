"""Tests for client graph to Rai memory sync."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from kokoro.clients.models import ClientProfile, ClientRegistry
from kokoro.clients.sync import generate_reference_md, sync_to_memory


def _make_registry() -> ClientRegistry:
    """Create a test registry with one client."""
    now = datetime.now(tz=timezone.utc)
    return ClientRegistry(
        clients=[
            ClientProfile(
                id="konecta-park",
                name="Konecta Park",
                group="invertikal",
                description="Hub logistico Puerto Morelos",
                repos=["/path/to/KonectaParkAhuehuete"],
                campaign_folder="clientes/invertikal/konecta-park/campanas",
                segments=["brokers", "inversionistas"],
                industry="real-estate-industrial",
                created=now,
                updated=now,
                metadata={"avance": "58%"},
            ),
        ],
        created=now,
        updated=now,
    )


class TestGenerateReferenceMd:
    """Generate reference markdown content from ClientProfile."""

    def test_has_frontmatter(self) -> None:
        """Generated content has YAML frontmatter."""
        registry = _make_registry()
        content = generate_reference_md(registry.clients[0])
        assert content.startswith("---\n")
        assert "type: reference" in content

    def test_has_name_and_description(self) -> None:
        """Frontmatter includes name and description."""
        registry = _make_registry()
        content = generate_reference_md(registry.clients[0])
        assert "name: Konecta Park" in content
        assert "description:" in content

    def test_has_client_data(self) -> None:
        """Body includes repos, segments, metadata."""
        registry = _make_registry()
        content = generate_reference_md(registry.clients[0])
        assert "invertikal" in content
        assert "brokers" in content
        assert "KonectaParkAhuehuete" in content


class TestSyncToMemory:
    """Sync registry to memory directory."""

    def test_creates_reference_file(self, tmp_path: Path) -> None:
        """Creates reference_*.md for each client."""
        registry = _make_registry()
        created = sync_to_memory(registry, tmp_path)
        assert len(created) == 1
        ref_file = tmp_path / "reference_konecta_park.md"
        assert ref_file.is_file()

    def test_does_not_overwrite_existing(self, tmp_path: Path) -> None:
        """Existing files are not overwritten without force."""
        registry = _make_registry()
        ref_file = tmp_path / "reference_konecta_park.md"
        ref_file.write_text("manual content", encoding="utf-8")
        created = sync_to_memory(registry, tmp_path)
        assert len(created) == 0
        assert ref_file.read_text(encoding="utf-8") == "manual content"

    def test_overwrites_with_force(self, tmp_path: Path) -> None:
        """Force flag overwrites existing files."""
        registry = _make_registry()
        ref_file = tmp_path / "reference_konecta_park.md"
        ref_file.write_text("old content", encoding="utf-8")
        created = sync_to_memory(registry, tmp_path, force=True)
        assert len(created) == 1
        assert "old content" not in ref_file.read_text(encoding="utf-8")

    def test_empty_registry(self, tmp_path: Path) -> None:
        """Empty registry creates no files."""
        now = datetime.now(tz=timezone.utc)
        registry = ClientRegistry(clients=[], created=now, updated=now)
        created = sync_to_memory(registry, tmp_path)
        assert len(created) == 0
