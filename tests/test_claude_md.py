"""Structural tests for Kokoro CLAUDE.md — Eduardo's voice clone.

Tests validate that the CLAUDE.md contains required sections, vocabulary,
interaction patterns, and anti-patterns. Not testing prose quality.
"""

from pathlib import Path

import pytest

CLAUDE_MD = Path(__file__).parent.parent / "extension" / ".claude" / "CLAUDE.md"


@pytest.fixture
def content() -> str:
    """Load CLAUDE.md content."""
    return CLAUDE_MD.read_text(encoding="utf-8")


def _has_section(text: str, heading: str) -> bool:
    """Check if markdown contains a heading (## or ###)."""
    return f"## {heading}" in text or f"### {heading}" in text


# --- Identity ---


class TestIdentity:
    """CLAUDE.md must establish Eduardo's identity and philosophy."""

    def test_has_identity_section(self, content: str) -> None:
        assert _has_section(content, "Identidad") or _has_section(
            content, "Identity"
        )

    def test_mentions_eduardo(self, content: str) -> None:
        assert "Eduardo" in content

    def test_mentions_kokoro(self, content: str) -> None:
        assert "Kokoro" in content

    def test_mentions_projector(self, content: str) -> None:
        """Eduardo is a Human Design Projector — wait for invitation."""
        lower = content.lower()
        assert "proyector" in lower or "projector" in lower

    def test_mentions_invitation_strategy(self, content: str) -> None:
        """Projectors wait for invitation before guiding."""
        lower = content.lower()
        assert "invitación" in lower or "invitation" in lower

    def test_mentions_guardian(self, content: str) -> None:
        """Eduardo's core archetype: Guardian of Wealth."""
        lower = content.lower()
        assert "guardián" in lower or "guardian" in lower


# --- Voice Patterns ---


class TestVoicePatterns:
    """CLAUDE.md must define Eduardo's voice and interaction style."""

    def test_has_voice_section(self, content: str) -> None:
        assert _has_section(content, "Voz") or _has_section(
            content, "Voice"
        ) or _has_section(content, "Patrones")

    def test_mentions_espejo(self, content: str) -> None:
        """Mirror before advise — espejo antes que consejo."""
        lower = content.lower()
        assert "espejo" in lower or "mirror" in lower

    def test_mentions_70_30(self, content: str) -> None:
        """Listen 70%, speak 30%."""
        assert "70" in content and "30" in content

    def test_mentions_sprezzatura(self, content: str) -> None:
        """Studied naturalness."""
        lower = content.lower()
        assert "sprezzatura" in lower

    def test_mentions_amortiguar(self, content: str) -> None:
        """Cushion-pivot-offer technique."""
        lower = content.lower()
        assert "amortiguar" in lower or "cushion" in lower


# --- Vocabulary ---


class TestVocabulary:
    """CLAUDE.md must include the luxurizante vocabulary guide."""

    def test_has_vocabulary_section(self, content: str) -> None:
        assert _has_section(content, "Vocabulario") or _has_section(
            content, "Vocabulary"
        ) or "vocabulario" in content.lower()

    def test_mentions_inversion_not_precio(self, content: str) -> None:
        """Eduardo says 'inversión' not 'precio'."""
        lower = content.lower()
        assert "inversión" in lower

    def test_mentions_creacion_not_producto(self, content: str) -> None:
        """Eduardo says 'creación' not 'producto'."""
        lower = content.lower()
        assert "creación" in lower


# --- Methodology ---


class TestMethodology:
    """CLAUDE.md must outline Eduardo's 4-phase process."""

    def test_has_methodology_section(self, content: str) -> None:
        assert _has_section(content, "Metodología") or _has_section(
            content, "Methodology"
        ) or _has_section(content, "Proceso") or _has_section(
            content, "Fases"
        )

    def test_mentions_preparar(self, content: str) -> None:
        lower = content.lower()
        assert "preparar" in lower

    def test_mentions_germinar(self, content: str) -> None:
        lower = content.lower()
        assert "germinar" in lower

    def test_mentions_cosechar(self, content: str) -> None:
        lower = content.lower()
        assert "cosechar" in lower

    def test_mentions_skills(self, content: str) -> None:
        """Must reference at least one /kokoro-* skill."""
        assert "/kokoro-" in content


# --- Anti-patterns ---


class TestAntiPatterns:
    """CLAUDE.md must define what Eduardo would NEVER do."""

    def test_has_antipattern_section(self, content: str) -> None:
        lower = content.lower()
        assert (
            "anti-patr" in lower
            or "nunca" in lower
            or "never" in lower
            or "prohibid" in lower
        )

    def test_forbids_generic_ai_language(self, content: str) -> None:
        """Must warn against generic AI marketing speak."""
        lower = content.lower()
        assert "genéric" in lower or "generic" in lower

    def test_vocabulary_prohibitions(self, content: str) -> None:
        """Must list forbidden words."""
        lower = content.lower()
        assert "gratis" in lower or "free" in lower


# --- Bilingual ---


class TestBilingual:
    """CLAUDE.md must include bilingual response instructions."""

    def test_has_bilingual_section(self, content: str) -> None:
        lower = content.lower()
        assert (
            "bilingüe" in lower
            or "bilingual" in lower
            or "idioma" in lower
            or "language" in lower
        )

    def test_spanish_soul_instruction(self, content: str) -> None:
        """Spanish is the soul language."""
        lower = content.lower()
        assert "español" in lower or "spanish" in lower
