"""Purpose: deterministic source registration and IDs."""

from collections.abc import Sequence
from pathlib import Path

from engine.source.file_loader import load_file
from schemas.source_file import SourceFile


def register_sources(paths: Sequence[str]) -> list[SourceFile]:
    """Register source files in input order with explicit read outcomes."""
    return [load_file(Path(path_str)) for path_str in paths]


def load_sources(paths: Sequence[str]) -> list[SourceFile]:
    """Contract alias for source registration."""
    return register_sources(paths)
