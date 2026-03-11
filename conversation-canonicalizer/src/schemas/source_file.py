"""Purpose: SourceFile schema contract for ingest stage."""

from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class SourceFile:
    """Metadata and read result for a source file."""

    source_id: str
    path: str
    read_status: Literal["ok", "error"]
    raw_content: str | None
    read_error: str | None = None
