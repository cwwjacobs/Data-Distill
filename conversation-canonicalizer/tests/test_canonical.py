"""Purpose: canonical-stage tests for stable IDs and flags."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from engine.canonical.canonical_builder import build_canonical
from engine.parse.json_export_parser import parse_export_json
from engine.parse.raw_record_builder import build_raw_records


FIXTURES_DIR = PROJECT_ROOT / "fixtures"


def _canonical_from_fixture(name: str, source_id: str = "src-1"):
    raw_text = (FIXTURES_DIR / name).read_text(encoding="utf-8")
    parsed = parse_export_json(raw_text)
    raw_records = build_raw_records(parsed, source_file_id=source_id)
    return build_canonical(raw_records)


def test_canonical_ids_stable_across_repeated_runs() -> None:
    first = _canonical_from_fixture("sample_supported_export.json", source_id="same-source")
    second = _canonical_from_fixture("sample_supported_export.json", source_id="same-source")

    assert [r.canonical_id for r in first] == [r.canonical_id for r in second]


def test_ambiguous_fixture_emits_ambiguity_flag() -> None:
    records = _canonical_from_fixture("sample_ambiguous_export.json")
    all_flags = [flag for record in records for flag in record.flags]

    assert any(flag.type == "ambiguity" for flag in all_flags)


def test_lossy_fixture_emits_loss_flag() -> None:
    records = _canonical_from_fixture("sample_lossy_export.json")
    all_flags = [flag for record in records for flag in record.flags]

    assert any(flag.type == "loss" for flag in all_flags)


def test_message_order_is_preserved() -> None:
    records = _canonical_from_fixture("sample_supported_export.json")
    assert [m.message_index for m in records[0].messages] == [0, 1]
    assert [m.content for m in records[0].messages] == ["Hello", "Hi there!"]


def test_ambiguous_role_normalizes_to_unknown() -> None:
    records = _canonical_from_fixture("sample_ambiguous_export.json")
    assert records[0].messages[0].role == "unknown"


def test_canonical_id_is_hash_shaped_and_stable() -> None:
    records_one = _canonical_from_fixture("sample_supported_export.json", source_id="hash-source")
    records_two = _canonical_from_fixture("sample_supported_export.json", source_id="hash-source")

    canonical_id = records_one[0].canonical_id
    assert canonical_id == records_two[0].canonical_id
    assert len(canonical_id) == 64
    assert all(ch in "0123456789abcdef" for ch in canonical_id)


def test_non_string_content_normalizes_to_empty_string() -> None:
    parsed = {
        "conversations": [
            {
                "id": "conv-nonstr-content",
                "title": "Non-string content",
                "messages": [
                    {"role": "user", "content": {"nested": "value"}, "timestamp": "2026-03-11T13:00:00Z"}
                ],
            }
        ]
    }
    raw_records = build_raw_records(parsed, source_file_id="source-content")
    canonical = build_canonical(raw_records)

    assert canonical[0].messages[0].content == ""
