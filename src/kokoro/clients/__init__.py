"""Kokoro client graph — client knowledge models for Eduardo's brain."""

from kokoro.clients.models import ClientProfile, ClientRegistry
from kokoro.clients.store import create_empty_registry, load_registry, save_registry
from kokoro.clients.sync import generate_reference_md, sync_to_memory, update_memory_index

__all__ = [
    "ClientProfile",
    "ClientRegistry",
    "create_empty_registry",
    "load_registry",
    "generate_reference_md",
    "save_registry",
    "sync_to_memory",
    "update_memory_index",
]
