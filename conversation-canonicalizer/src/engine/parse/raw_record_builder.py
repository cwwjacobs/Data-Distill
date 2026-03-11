"""Purpose: build RawRecord entries from parsed objects."""

from __future__ import annotations

from typing import Any

from schemas.raw_record import RawRecord


def build_raw_records(parsed: object, source_file_id: str) -> list[RawRecord]:
    """Convert validated parsed payload into deterministic RawRecord entries."""
    if not isinstance(parsed, dict):
        raise ValueError("Parsed payload must be a dict for supported format")

    conversations = parsed.get("conversations")
    if not isinstance(conversations, list):
        raise ValueError("Parsed payload missing conversations list")

    records: list[RawRecord] = []
    for record_index, conversation in enumerate(conversations):
        parse_status = "ok" if isinstance(conversation, dict) else "error"
        payload = conversation if isinstance(conversation, dict) else {"invalid_conversation": conversation}
        records.append(
            RawRecord(
                source_file_id=source_file_id,
                record_index=record_index,
                raw_payload=payload,
                parse_status=parse_status,
            )
        )
    return records
