"""Kokoro CLI — install the extension into a project."""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from importlib import resources
from pathlib import Path

KOKORO_START = "<!-- KOKORO START -->"
KOKORO_END = "<!-- KOKORO END -->"


def _get_extension_path() -> Path:
    """Return the path to the bundled extension directory."""
    ref = resources.files("kokoro").joinpath("..").joinpath("..").joinpath("extension")
    return Path(str(ref))


def _find_extension_dir() -> Path:
    """Locate the extension directory.

    Tries package-relative first, then importlib.resources.
    """
    # Try relative to this source file (works in editable installs and direct runs)
    source_relative = Path(__file__).resolve().parent.parent.parent / "extension"
    if source_relative.is_dir():
        return source_relative

    # Try importlib.resources (works in installed packages)
    try:
        pkg_path = _get_extension_path()
        if pkg_path.is_dir():
            return pkg_path
    except (TypeError, FileNotFoundError):
        pass

    msg = "Could not locate Kokoro extension files."
    raise FileNotFoundError(msg)


def _merge_claude_md(existing: str, kokoro_content: str) -> str:
    """Merge Kokoro content into an existing CLAUDE.md using markers."""
    marker_pattern = re.compile(
        rf"{re.escape(KOKORO_START)}.*?{re.escape(KOKORO_END)}",
        re.DOTALL,
    )
    kokoro_section = f"{KOKORO_START}\n{kokoro_content}\n{KOKORO_END}\n"

    if KOKORO_START in existing:
        return marker_pattern.sub(kokoro_section.rstrip(), existing)

    if existing.endswith("\n\n"):
        separator = ""
    elif existing.endswith("\n"):
        separator = "\n"
    else:
        separator = "\n\n"
    return existing + separator + kokoro_section


def _copy_dir_no_overwrite(src: Path, dst: Path) -> None:
    """Copy directory contents, preserving user files.

    Files prefixed with ``kokoro-`` are owned by Kokoro and will be
    overwritten on every run so that updates propagate.  All other
    existing files are left untouched.  ``.gitkeep`` placeholders are
    never copied.
    """
    dst.mkdir(parents=True, exist_ok=True)
    for item in src.iterdir():
        if item.name == ".gitkeep":
            continue
        target = dst / item.name
        if item.is_dir():
            _copy_dir_no_overwrite(item, target)
        elif not target.exists() or item.name.startswith("kokoro"):
            shutil.copy2(item, target)


def init(target: Path | None = None) -> None:
    """Install Kokoro extension files into the target project directory.

    Args:
        target: Project directory. Defaults to current working directory.
    """
    target = target or Path.cwd()
    extension_dir = _find_extension_dir()
    claude_dir = target / ".claude"

    # Handle CLAUDE.md
    source_claude_md = extension_dir / ".claude" / "CLAUDE.md"
    target_claude_md = claude_dir / "CLAUDE.md"
    kokoro_content = source_claude_md.read_text(encoding="utf-8")

    if target_claude_md.exists():
        existing = target_claude_md.read_text(encoding="utf-8")
        merged = _merge_claude_md(existing, kokoro_content)
        target_claude_md.write_text(merged, encoding="utf-8")
    else:
        claude_dir.mkdir(parents=True, exist_ok=True)
        wrapped = f"{KOKORO_START}\n{kokoro_content}\n{KOKORO_END}\n"
        target_claude_md.write_text(wrapped, encoding="utf-8")

    # Copy commands/ and knowledge/ without overwriting
    for subdir in ("commands", "knowledge"):
        src = extension_dir / ".claude" / subdir
        if src.is_dir():
            _copy_dir_no_overwrite(src, claude_dir / subdir)

    print(f"Kokoro installed in {claude_dir}")


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        prog="kokoro",
        description="Kokoro — AI marketing strategist extension for Claude Code",
    )
    subparsers = parser.add_subparsers(dest="command")

    init_parser = subparsers.add_parser("init", help="Install Kokoro into your project")
    init_parser.add_argument(
        "--target",
        type=Path,
        default=None,
        help="Target project directory (default: current directory)",
    )

    args = parser.parse_args()

    if args.command == "init":
        init(target=args.target)
    else:
        parser.print_help()
        sys.exit(1)
