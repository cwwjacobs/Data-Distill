
"""Purpose: export-stage tests for deterministic JSON/JSONL parity."""

from __future__ import annotations

from pathlib import Path
import json
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from engine.export.canonical_json_writer import write_json
from engine.export.canonical_jsonl_writer import write_jsonl
from schemas.canonical_record import CanonicalMessage, CanonicalRecord
from schemas.flags import WarningFlag


def _sample_canonical_records() -> list[CanonicalRecord]:
    return [
        CanonicalRecord(
            canonical_id="c1",
            source_file_id="s1",
            source_record_index=0,
            title="One",
            messages=[CanonicalMessage(message_index=0, role="user", content="hello", timestamp="2026-03-11T10:00:00Z")],
            flags=[WarningFlag(type="warning", code="W1", message="note", path=None, severity="info")],
        ),
        CanonicalRecord(
            canonical_id="c2",
            source_file_id="s1",
            source_record_index=1,
            title="Two",
            messages=[CanonicalMessage(message_index=0, role="assistant", content="hi", timestamp=None)],
            flags=[],
        ),
    ]


def test_repeated_json_export_is_byte_identical(tmp_path: Path) -> None:
    records = _sample_canonical_records()
    output = tmp_path / "canonical.json"

    write_json(records, output)
    first = output.read_bytes()
    write_json(records, output)
    second = output.read_bytes()

    assert first == second


def test_jsonl_has_one_line_per_canonical_record(tmp_path: Path) -> None:
    records = _sample_canonical_records()
    output = tmp_path / "canonical.jsonl"

    write_jsonl(records, output)

    lines = output.read_text(encoding="utf-8").splitlines()
    assert len(lines) == len(records)


def test_json_and_jsonl_contain_matching_canonical_content(tmp_path: Path) -> None:
    records = _sample_canonical_records()
    json_path = tmp_path / "canonical.json"
    jsonl_path = tmp_path / "canonical.jsonl"

    write_json(records, json_path)
    write_jsonl(records, jsonl_path)

    json_payload = json.loads(json_path.read_text(encoding="utf-8"))
    jsonl_payload = [json.loads(line) for line in jsonl_path.read_text(encoding="utf-8").splitlines()]

    assert json_payload == jsonl_payload


def test_exported_records_include_required_canonical_fields(tmp_path: Path) -> None:
    records = _sample_canonical_records()
    output = tmp_path / "canonical.json"

    write_json(records, output)
    payload = json.loads(output.read_text(encoding="utf-8"))

    for record in payload:
        assert "canonical_id" in record
        assert "messages" in record
        assert "flags" in record

