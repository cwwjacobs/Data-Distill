"""Purpose: normalize message role/content structure."""

from __future__ import annotations

from schemas.canonical_record import CanonicalMessage
from schemas.raw_record import RawRecord

_ALLOWED_ROLES = {"user", "assistant", "system"}


def _normalize_role(raw_role: object) -> str:
    if not isinstance(raw_role, str):
        return "unknown"
    lowered = raw_role.lower()
    return lowered if lowered in _ALLOWED_ROLES else "unknown"


def normalize_messages(raw_record: RawRecord) -> list[CanonicalMessage]:
    """Normalize message payloads into deterministic canonical message objects."""
    messages = raw_record.raw_payload.get("messages", [])
    normalized: list[CanonicalMessage] = []

    for message_index, message in enumerate(messages):
        role = _normalize_role(message.get("role")) if isinstance(message, dict) else "unknown"
        content = message.get("content", "") if isinstance(message, dict) else ""
        timestamp = message.get("timestamp") if isinstance(message, dict) else None

        normalized.append(
            CanonicalMessage(
                message_index=message_index,
                role=role,
                content=content if isinstance(content, str) else "",
                timestamp=timestamp if isinstance(timestamp, str) else None,
            )
        )

    return normalized
