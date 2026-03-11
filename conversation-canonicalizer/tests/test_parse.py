"""Purpose: parse-stage tests for supported format and stable indexing."""

from pathlib import Path
import sys

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from engine.parse.json_export_parser import parse_export_json
from engine.parse.raw_record_builder import build_raw_records


FIXTURES_DIR = PROJECT_ROOT / "fixtures"


def _read_fixture(name: str) -> str:
    return (FIXTURES_DIR / name).read_text(encoding="utf-8")


def test_supported_fixture_parses_successfully() -> None:
    parsed = parse_export_json(_read_fixture("sample_supported_export.json"))
    assert isinstance(parsed, dict)
    assert isinstance(parsed["conversations"], list)


def test_ambiguous_fixture_parses_successfully() -> None:
    parsed = parse_export_json(_read_fixture("sample_ambiguous_export.json"))
    assert isinstance(parsed, dict)
    assert len(parsed["conversations"]) == 1


def test_lossy_fixture_parses_successfully() -> None:
    parsed = parse_export_json(_read_fixture("sample_lossy_export.json"))
    assert isinstance(parsed, dict)
    assert len(parsed["conversations"]) == 1


def test_raw_record_ordering_and_indexes_are_stable() -> None:
    parsed = parse_export_json(_read_fixture("sample_supported_export.json"))

    first = build_raw_records(parsed, source_file_id="source-1")
    second = build_raw_records(parsed, source_file_id="source-1")

    assert [r.record_index for r in first] == [0]
    assert [r.record_index for r in first] == [r.record_index for r in second]
    assert [r.source_file_id for r in first] == ["source-1"]
    assert [r.parse_status for r in first] == ["ok"]


def test_invalid_top_level_structure_raises_value_error() -> None:
    with pytest.raises(ValueError, match="top-level 'conversations' must be a list"):
        parse_export_json('{"conversations": {"not": "a list"}}')
