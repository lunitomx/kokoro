"""Anti-vocabulary gate helper for skill content tests."""

import re


def _word_in_quotes(word: str, line: str) -> bool:
    """Check if word appears inside any quoted substring."""
    in_double = any(
        word in m.group(1)
        for m in re.finditer(r'"([^"]*)"', line)
    )
    in_single = any(
        word in m.group(1)
        for m in re.finditer(r"'([^']*)'", line)
    )
    return in_double or in_single


def find_prohibited_words(
    content: str,
) -> list[tuple[str, int, str]]:
    """Find prohibited vocabulary, excluding legitimate contexts.

    Returns list of (word, line_number, line_text) for each
    violation found outside of legitimate contexts.

    Excluded contexts:
    - Blockquote lines (starting with >)
    - Substitution instructions (no " / no ')
    - Word inside quotes (being referenced, not used)
    - Risk categories (riesgo de)
    - Methodology names (arbol de productos)
    - Financial categories (productos fisicos)
    """
    prohibited = [
        "cliente",
        "producto",
        "precio",
        "gratis",
        "descuento",
    ]
    violations: list[tuple[str, int, str]] = []
    for line_num, line in enumerate(content.splitlines(), 1):
        stripped = line.strip()
        lower = stripped.lower()
        # Skip blockquotes (opening quotes from sources)
        if stripped.startswith(">"):
            continue
        # Skip substitution instructions
        if 'no "' in lower or "no '" in lower:
            continue
        for word in prohibited:
            if word not in lower:
                continue
            # Skip if word appears inside quotes
            if _word_in_quotes(word, lower):
                continue
            # Skip risk category names
            if "riesgo de" in lower:
                continue
            # Skip methodology name
            if "arbol de productos" in lower:
                continue
            # Skip financial category
            if "productos fisicos" in lower:
                continue
            violations.append(
                (word, line_num, stripped)
            )
    return violations
