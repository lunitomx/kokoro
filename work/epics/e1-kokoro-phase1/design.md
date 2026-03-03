---
epic_id: "E1"
grounded_in: "Gemba of kokoro-project.md, libro-summary.md, luxelling-summary.md"
---

# Epic Design: Kokoro Phase 1

## Affected Surface (Gemba)

| Module/File | Current State | Changes |
|-------------|---------------|---------|
| src/kokoro/ | Does not exist | Create package with __init__.py, cli.py |
| pyproject.toml | Does not exist | Create with build config, entry points, package data |
| extension/.claude/ | Does not exist | Create CLAUDE.md, commands/, knowledge/ |
| tests/ | Does not exist | Create test suite for CLI and package |

## Target Components

| Component | Responsibility | Key Interface |
|-----------|---------------|---------------|
| kokoro.cli | Install extension into user's project | `kokoro init [--target PATH]` |
| extension/.claude/CLAUDE.md | Eduardo's personality, voice, methodology | Loaded by Claude Code at startup |
| extension/.claude/commands/*.md | Skill definitions (6 total) | Invoked as `/kokoro-*` in Claude Code |
| extension/.claude/knowledge/*.md | Methodology references | Referenced by CLAUDE.md and skills |
| extension/.claude/settings.json | Claude Code configuration | Auto-loaded by Claude Code |

## Key Contracts

```python
# src/kokoro/__init__.py
__version__: str = "0.1.0"

# src/kokoro/cli.py
def init(target: Path | None = None) -> None:
    """Copy extension files from package data to target .claude/ directory.

    - If target is None, uses current working directory
    - If .claude/CLAUDE.md exists, appends Kokoro section with markers
    - If .claude/CLAUDE.md doesn't exist, copies Kokoro CLAUDE.md as-is
    - Copies commands/ and knowledge/ directories
    - Writes settings.json (merge if exists)
    """
```

```
# Extension file layout (shipped as package data)
extension/
  .claude/
    CLAUDE.md              # Eduardo's brain
    settings.json          # Claude Code config
    commands/
      kokoro.md            # Router: identifies phase, routes to skill
      kokoro-session.md    # Session start/close
      kokoro-diagnose.md   # Speed Boat + Vision 20/20
      kokoro-mountain.md   # Montaña del Mañana + OKRs
      kokoro-prune.md      # Prune the Product Tree
      kokoro-finance.md    # Financial assessment
    knowledge/
      methodology.md       # Eduardo's 4-phase process overview
      frameworks.md        # Referenced frameworks with attribution
      voice-patterns.md    # Eduardo's speech patterns for CLAUDE.md reinforcement
```

## Migration Path

Greenfield — no migration needed.
