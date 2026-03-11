# conversation-canonicalizer

## Purpose
`conversation-canonicalizer` is a Phase 1 tool for ingesting a conversation export, converting it into deterministic `CanonicalRecord` structures, and surfacing ambiguity/loss explicitly as flags.

## Phase 1 Scope
- Single supported export format.
- Deterministic canonical records.
- Explicit ambiguity/loss flags.
- Deterministic JSON + JSONL export.
- Minimal read-only viewer.

## Non-Goals (Phase 1)
- Multi-format parsing.
- Analytics/scoring.
- CLI tools.
- Cloud features.
- Dashboards.

## Pipeline
`source -> parse -> canonical -> export -> viewer`

- **source**: load local files into `SourceFile[]` with explicit read status.
- **parse**: convert source content into `RawRecord[]`.
- **canonical**: normalize to `CanonicalRecord[]` and attach warning/ambiguity/loss flags.
- **export**: write deterministic JSON/JSONL artifacts.
- **viewer**: render read-only list/detail views of canonical output.

## Determinism Guarantees
Phase 1 is designed around deterministic behavior:
- Canonical IDs are stable across runs for the same input.
- JSON export is byte-identical across runs for the same input.
- Ambiguity and loss are always surfaced as explicit flags.

## Repository Structure
- **`src/schemas`**: shared data contracts (`SourceFile`, `RawRecord`, `CanonicalRecord`, flags).
- **`src/engine`**: pipeline stages (`source`, `parse`, `canonical`, `export`).
- **`src/viewer`**: minimal read-only UI surface.
- **`fixtures`**: baseline, ambiguity, and loss-focused sample inputs.
- **`tests`**: stage-focused tests for determinism and contract behavior.

## Status
This repository is in **Phase 1 implementation**. The source layer and schema contracts are in progress; parse/canonical/export/viewer behavior is being implemented incrementally against the Phase 1 contract.
