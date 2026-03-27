"""Kokoro client graph — client knowledge models for Eduardo's brain."""

from kokoro.clients.models import ClientProfile, ClientRegistry
from kokoro.clients.store import create_empty_registry, load_registry, save_registry

__all__ = [
    "ClientProfile",
    "ClientRegistry",
    "create_empty_registry",
    "load_registry",
    "save_registry",
]
