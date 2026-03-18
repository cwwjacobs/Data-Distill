"""Purpose: build CanonicalRecord objects with deterministic IDs."""

from __future__ import annotations

from hashlib import sha256

from engine.canonical.flag_emitter import emit_flags
from engine.canonical.message_normalizer import normalize_messages
from schemas.canonical_record import CanonicalRecord
from schemas.raw_record import RawRecord


def _build_canonical_id(source_file_id: str, source_record_index: int) -> str:
    """Derive a deterministic canonical ID from source linkage."""
    return sha256(f"{source_file_id}|{source_record_index}".encode("utf-8")).hexdigest()


def build_canonical(raw_records: list[RawRecord]) -> list[CanonicalRecord]:
    """Build canonical records from parse-stage raw records."""
    canonical_records: list[CanonicalRecord] = []

    for raw_record in raw_records:
        title_value = raw_record.raw_payload.get("title")
        title = title_value if isinstance(title_value, str) else None

        canonical_records.append(
            CanonicalRecord(
                canonical_id=_build_canonical_id(raw_record.source_file_id, raw_record.record_index),
                source_file_id=raw_record.source_file_id,
                source_record_index=raw_record.record_index,
                title=title,
                messages=normalize_messages(raw_record),
                flags=emit_flags(raw_record),
            )
        )

    return canonical_records
