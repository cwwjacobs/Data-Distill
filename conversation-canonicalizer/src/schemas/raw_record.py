"""Purpose: RawRecord schema contract for parse stage."""

from dataclasses import dataclass
from typing import Any, Literal


@dataclass(frozen=True)
class RawRecord:
    """Uniform parse-stage record linked to a source file."""

    source_file_id: str
    record_index: int
    raw_payload: dict[str, Any]
    parse_status: Literal["ok", "error"]
