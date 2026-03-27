"""Client graph data models.

Defines ClientProfile (individual client node) and ClientRegistry
(collection with search). Separate from coaching ontology — this models
Eduardo's relationship WITH clients, not coaching concepts.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel


class ClientProfile(BaseModel):
    """A client node in Eduardo's knowledge graph.

    Each client has identity, location info, and connections to
    their artifacts (repos, campaigns, coaching state).
    """

    id: str
    name: str
    group: str
    description: str = ""
    repos: list[str] = []
    campaign_folder: str = ""
    context_file: str | None = None
    segments: list[str] = []
    industry: str = ""
    coaching_state_path: str | None = None
    created: datetime
    updated: datetime
    metadata: dict[str, Any] = {}


class ClientRegistry(BaseModel):
    """Container for all client profiles.

    Persisted as clients.json in RaizAncestral.
    Provides search methods for quick client lookup.
    """

    version: int = 1
    clients: list[ClientProfile] = []
    created: datetime
    updated: datetime

    def find_by_id(self, client_id: str) -> ClientProfile | None:
        """Find client by exact ID."""
        return next((c for c in self.clients if c.id == client_id), None)

    def find_by_name(self, query: str) -> ClientProfile | None:
        """Find first client whose name contains query (case-insensitive)."""
        q = query.lower()
        return next((c for c in self.clients if q in c.name.lower()), None)

    def find_by_segment(self, segment: str) -> list[ClientProfile]:
        """Find all clients that serve a segment."""
        s = segment.lower()
        return [c for c in self.clients if s in [seg.lower() for seg in c.segments]]

    def list_groups(self) -> list[str]:
        """List unique client groups."""
        return sorted({c.group for c in self.clients})
