"""Tests for client graph data models."""

from __future__ import annotations

from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from kokoro.clients.models import (
    ClientProfile,
    ClientRegistry,
)


class TestClientProfile:
    """ClientProfile model validation and behavior."""

    def test_create_minimal(self) -> None:
        """Minimal client with required fields only."""
        now = datetime.now(tz=timezone.utc)
        client = ClientProfile(
            id="konecta-park",
            name="Konecta Park",
            group="invertikal",
            created=now,
            updated=now,
        )
        assert client.id == "konecta-park"
        assert client.name == "Konecta Park"
        assert client.group == "invertikal"
        assert client.repos == []
        assert client.segments == []
        assert client.metadata == {}

    def test_create_full(self) -> None:
        """Full client with all optional fields."""
        now = datetime.now(tz=timezone.utc)
        client = ClientProfile(
            id="konecta-park",
            name="Konecta Park",
            group="invertikal",
            description="Hub logistico Puerto Morelos",
            repos=["/path/to/KonectaParkAhuehuete"],
            campaign_folder="clientes/invertikal/konecta-park/campanas",
            context_file="clientes/invertikal/konecta-park/campanas/meta-ads/contexto.md",
            segments=["brokers", "inversionistas"],
            industry="real-estate-industrial",
            coaching_state_path=None,
            created=now,
            updated=now,
            metadata={"avance": "58%", "entrega": "2026"},
        )
        assert client.description == "Hub logistico Puerto Morelos"
        assert len(client.repos) == 1
        assert "brokers" in client.segments
        assert client.industry == "real-estate-industrial"
        assert client.metadata["avance"] == "58%"

    def test_missing_required_field(self) -> None:
        """Missing required fields raise ValidationError."""
        with pytest.raises(ValidationError):
            ClientProfile(
                id="test",
                # missing name, group, created, updated
            )  # type: ignore[call-arg]


class TestClientRegistry:
    """ClientRegistry container and search."""

    @pytest.fixture
    def registry_with_clients(self) -> ClientRegistry:
        """Registry with two test clients."""
        now = datetime.now(tz=timezone.utc)
        konecta = ClientProfile(
            id="konecta-park",
            name="Konecta Park",
            group="invertikal",
            segments=["brokers", "inversionistas"],
            industry="real-estate-industrial",
            created=now,
            updated=now,
        )
        eln = ClientProfile(
            id="escuela-libre",
            name="Escuela Libre de Negocios",
            group="escuela-libre-de-negocios",
            segments=["emprendedores", "estudiantes"],
            industry="education",
            created=now,
            updated=now,
        )
        return ClientRegistry(
            clients=[konecta, eln],
            created=now,
            updated=now,
        )

    def test_find_by_id(self, registry_with_clients: ClientRegistry) -> None:
        """Find client by exact ID."""
        result = registry_with_clients.find_by_id("konecta-park")
        assert result is not None
        assert result.name == "Konecta Park"

    def test_find_by_id_not_found(self, registry_with_clients: ClientRegistry) -> None:
        """Returns None for unknown ID."""
        result = registry_with_clients.find_by_id("unknown")
        assert result is None

    def test_find_by_name(self, registry_with_clients: ClientRegistry) -> None:
        """Find client by partial name match (case-insensitive)."""
        result = registry_with_clients.find_by_name("konecta")
        assert result is not None
        assert result.id == "konecta-park"

    def test_find_by_name_case_insensitive(self, registry_with_clients: ClientRegistry) -> None:
        """Name search is case-insensitive."""
        result = registry_with_clients.find_by_name("ESCUELA")
        assert result is not None
        assert result.id == "escuela-libre"

    def test_find_by_name_not_found(self, registry_with_clients: ClientRegistry) -> None:
        """Returns None when no name matches."""
        result = registry_with_clients.find_by_name("xyz")
        assert result is None

    def test_find_by_segment(self, registry_with_clients: ClientRegistry) -> None:
        """Find all clients that serve a segment."""
        results = registry_with_clients.find_by_segment("brokers")
        assert len(results) == 1
        assert results[0].id == "konecta-park"

    def test_find_by_segment_none(self, registry_with_clients: ClientRegistry) -> None:
        """Empty list when no client has segment."""
        results = registry_with_clients.find_by_segment("astronauts")
        assert len(results) == 0

    def test_list_groups(self, registry_with_clients: ClientRegistry) -> None:
        """List unique groups."""
        groups = registry_with_clients.list_groups()
        assert set(groups) == {"invertikal", "escuela-libre-de-negocios"}

    def test_empty_registry(self) -> None:
        """Empty registry works."""
        now = datetime.now(tz=timezone.utc)
        reg = ClientRegistry(clients=[], created=now, updated=now)
        assert reg.find_by_id("x") is None
        assert reg.find_by_name("x") is None
        assert reg.find_by_segment("x") == []
        assert reg.list_groups() == []
