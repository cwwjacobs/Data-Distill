"""Purpose: viewer smoke tests using real fixture->parse->canonical->export->viewer flow."""

from __future__ import annotations

from pathlib import Path
import sys

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from engine.parse.json_export_parser import parse_export_json
from engine.parse.raw_record_builder import build_raw_records
from engine.canonical.canonical_builder import build_canonical
from engine.export.canonical_json_writer import write_json
from viewer.app import run_viewer


def test_viewer_smoke_pipeline_to_json_artifact(tmp_path: Path) -> None:
    fixture_path = PROJECT_ROOT / "fixtures" / "sample_supported_export.json"
    raw_text = fixture_path.read_text(encoding="utf-8")

    parsed = parse_export_json(raw_text)
    raw_records = build_raw_records(parsed, source_file_id="viewer-smoke-source")
    canonical_records = build_canonical(raw_records)

    output_path = tmp_path / "canonical.json"
    write_json(canonical_records, output_path)

    with pytest.raises(NotImplementedError):
        run_viewer(output_path)
