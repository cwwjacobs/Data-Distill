from __future__ import annotations

import json
from pathlib import Path

from engine.export.canonical_json_writer import _canonical_payload


def write_jsonl(canonical_records: list[object], output_path: Path) -> None:
    """Write deterministic UTF-8 JSONL, one canonical record per line."""
    payload = _canonical_payload(canonical_records)
    lines = [json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":")) for record in payload]
    output_path.write_text(("\n".join(lines) + ("\n" if lines else "")), encoding="utf-8")