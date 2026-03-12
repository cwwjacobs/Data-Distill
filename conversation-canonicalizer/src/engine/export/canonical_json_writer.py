from __future__ import annotations

from dataclasses import asdict, is_dataclass
import json
from pathlib import Path
from typing import Any


def _to_builtin(value: Any) -> Any:
    """Convert dataclass-rich canonical records to JSON-serializable builtins."""
    if is_dataclass(value):
        return asdict(value)
    if isinstance(value, list):
        return [_to_builtin(item) for item in value]
    if isinstance(value, dict):
        return {key: _to_builtin(val) for key, val in value.items()}
    return value


def _canonical_payload(canonical_records: list[object]) -> list[dict[str, Any]]:
    """Build deterministic payload preserving input record order."""
    return [_to_builtin(record) for record in canonical_records]


def write_json(canonical_records: list[object], output_path: Path) -> None:
    """Write deterministic UTF-8 JSON array of canonical records."""
    payload = _canonical_payload(canonical_records)
    output_path.write_text(
        json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")),
        encoding="utf-8",
    )