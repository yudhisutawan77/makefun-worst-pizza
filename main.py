"""The Worst Pizza Topping - one funny line pitching a terrible topping."""

import os
from pathlib import Path

# The entry: one line, no trailing newline in the output file.
ENTRY_TEXT = (
    "Try our toothpaste pizza: minty-fresh, cavity-fighting, and the only "
    "slice that brushes your teeth while it ruins your dinner."
)


def resolve_output_path() -> Path:
    """Pick where entry.txt goes.

    ENTRY_OUT may name a file or a directory; then MAKEFUN_OUTPUT_DIR;
    then /output/entry.txt; cwd is the last resort.
    """
    entry_out = os.environ.get("ENTRY_OUT")
    if entry_out:
        candidate = Path(entry_out)
        if candidate.suffix == ".txt" or candidate.is_file():
            return candidate
        return candidate / "entry.txt"

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir:
        return Path(output_dir) / "entry.txt"

    return Path("/output/entry.txt")


def emit_entry(path: Path) -> Path:
    """Write the entry text with no trailing newline, creating parents."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY_TEXT, encoding="utf-8")
    return path


def main() -> None:
    target = resolve_output_path()
    try:
        emit_entry(target)
    except OSError:
        # /output may be missing or read-only in some sandboxes; fall back
        # to the current working directory as a last resort.
        emit_entry(Path.cwd() / "entry.txt")


if __name__ == "__main__":
    main()
