"""Purpose: CanonicalRecord schema contract for canonical stage."""

from dataclasses import dataclass, field
from typing import Literal

from schemas.flags import WarningFlag


@dataclass(frozen=True)
class CanonicalMessage:
    """Minimal normalized message structure for Phase 1."""

    message_index: int
    role: Literal["user", "assistant", "system", "unknown"]
    content: str
    timestamp: str | None


@dataclass(frozen=True)
class CanonicalRecord:
    """Minimal canonical record structure for Phase 1."""

    canonical_id: str
    source_file_id: str
    source_record_index: int
    title: str | None
    messages: list[CanonicalMessage] = field(default_factory=list)
    flags: list[WarningFlag] = field(default_factory=list)
