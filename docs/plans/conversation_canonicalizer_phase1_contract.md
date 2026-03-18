## 1. FINAL REPO NAME
`conversation-canonicalizer`

## 2. FINAL DIRECTORY TREE
```text
conversation-canonicalizer/
  README.md
  pyproject.toml
  src/
    schemas/
      source_file.py
      raw_record.py
      canonical_record.py
      flags.py
    engine/
      source/
        file_loader.py
        source_registry.py
      parse/
        json_export_parser.py
        raw_record_builder.py
      canonical/
        message_normalizer.py
        flag_emitter.py
        canonical_builder.py
      export/
        canonical_json_writer.py
        canonical_jsonl_writer.py
    viewer/
      app.py
      conversation_list.py
      conversation_detail.py
  fixtures/
    sample_supported_export.json
    sample_ambiguous_export.json
    sample_lossy_export.json
  tests/
    test_source.py
    test_parse.py
    test_canonical.py
    test_export.py
    test_viewer_smoke.py
  docs/
    SUPPORTED_FORMAT.md
    PHASE1_SCOPE.md
```

## 3. FILE-BY-FILE CREATION ORDER
1. `README.md`
2. `pyproject.toml`
3. `docs/PHASE1_SCOPE.md`
4. `docs/SUPPORTED_FORMAT.md`
5. `src/schemas/source_file.py`
6. `src/schemas/raw_record.py`
7. `src/schemas/flags.py`
8. `src/schemas/canonical_record.py`
9. `fixtures/sample_supported_export.json`
10. `fixtures/sample_ambiguous_export.json`
11. `fixtures/sample_lossy_export.json`
12. `src/engine/source/file_loader.py`
13. `src/engine/source/source_registry.py`
14. `src/engine/parse/json_export_parser.py`
15. `src/engine/parse/raw_record_builder.py`
16. `src/engine/canonical/message_normalizer.py`
17. `src/engine/canonical/flag_emitter.py`
18. `src/engine/canonical/canonical_builder.py`
19. `src/engine/export/canonical_json_writer.py`
20. `src/engine/export/canonical_jsonl_writer.py`
21. `src/viewer/conversation_list.py`
22. `src/viewer/conversation_detail.py`
23. `src/viewer/app.py`
24. `tests/test_source.py`
25. `tests/test_parse.py`
26. `tests/test_canonical.py`
27. `tests/test_export.py`
28. `tests/test_viewer_smoke.py`

## 4. FOR EACH FILE

### `README.md`
- purpose: state exactly what Phase 1 does and does not do.
- what it must contain: one-format support statement, deterministic-output statement, run/test commands.
- what it must NOT contain: Paid 2.0/CLI claims, unsupported feature promises.

### `pyproject.toml`
- purpose: lock runtime/test dependencies and entrypoints.
- what it must contain: minimal dependencies for parser, viewer, and test runner.
- what it must NOT contain: optional plugin ecosystems, unused tooling stacks.

### `docs/PHASE1_SCOPE.md`
- purpose: strict scope guard.
- what it must contain: in-scope list, out-of-scope list, stop conditions reference.
- what it must NOT contain: roadmap beyond Phase 1.

### `docs/SUPPORTED_FORMAT.md`
- purpose: define the single supported export schema.
- what it must contain: required keys, optional keys, parse assumptions.
- what it must NOT contain: multi-format commitments.

### `src/schemas/source_file.py`
- purpose: source file contract.
- what it must contain: source id, path, read status, raw content fields.
- what it must NOT contain: parsing/canonical logic.

### `src/schemas/raw_record.py`
- purpose: parse-stage contract.
- what it must contain: source link, record index, raw payload, parse status.
- what it must NOT contain: viewer/export behavior.

### `src/schemas/flags.py`
- purpose: warning/ambiguity/loss flag contract.
- what it must contain: flag type, code, message, path pointer, severity.
- what it must NOT contain: scoring/ranking fields.

### `src/schemas/canonical_record.py`
- purpose: canonical record contract.
- what it must contain: deterministic canonical id, normalized messages, flags.
- what it must NOT contain: analytics metrics.

### `fixtures/sample_supported_export.json`
- purpose: baseline happy-path input.
- what it must contain: at least one complete conversation parseable by format contract.
- what it must NOT contain: ambiguous/lossy edge cases.

### `fixtures/sample_ambiguous_export.json`
- purpose: ambiguity trigger fixture.
- what it must contain: data shape that forces explicit ambiguity flag emission.
- what it must NOT contain: malformed JSON that only tests parser crash behavior.

### `fixtures/sample_lossy_export.json`
- purpose: loss trigger fixture.
- what it must contain: representable input where reduction is required and loss must be flagged.
- what it must NOT contain: unparseable garbage.

### `src/engine/source/file_loader.py`
- purpose: deterministic local file reading.
- what it must contain: path read logic and explicit read error handling.
- what it must NOT contain: parse or canonical transforms.

### `src/engine/source/source_registry.py`
- purpose: stable source registration.
- what it must contain: deterministic source id derivation and ordering.
- what it must NOT contain: schema inference logic.

### `src/engine/parse/json_export_parser.py`
- purpose: parse one export format to raw objects.
- what it must contain: schema-constrained parsing for the supported format.
- what it must NOT contain: format auto-detection across many vendors.

### `src/engine/parse/raw_record_builder.py`
- purpose: convert parsed objects into `RawRecord` entries.
- what it must contain: deterministic record indexing and source linkage.
- what it must NOT contain: canonical normalization.

### `src/engine/canonical/message_normalizer.py`
- purpose: normalize roles/content/message sequence.
- what it must contain: deterministic message normalization rules.
- what it must NOT contain: quality scoring or semantic classification.

### `src/engine/canonical/flag_emitter.py`
- purpose: emit warning/ambiguity/loss flags.
- what it must contain: explicit rule checks and deterministic flag output.
- what it must NOT contain: silent suppression of edge cases.

### `src/engine/canonical/canonical_builder.py`
- purpose: construct canonical records.
- what it must contain: canonical id generation, normalized message assembly, attached flags.
- what it must NOT contain: exporter or UI rendering code.

### `src/engine/export/canonical_json_writer.py`
- purpose: deterministic JSON export.
- what it must contain: stable key ordering and stable record ordering.
- what it must NOT contain: non-deterministic metadata (timestamps/random ids).

### `src/engine/export/canonical_jsonl_writer.py`
- purpose: deterministic JSONL export.
- what it must contain: one canonical record per line, same canonical content as JSON export.
- what it must NOT contain: alternate transformation logic.

### `src/viewer/conversation_list.py`
- purpose: read-only list view.
- what it must contain: conversation index with flag visibility.
- what it must NOT contain: edit/mutate controls.

### `src/viewer/conversation_detail.py`
- purpose: read-only detail view.
- what it must contain: normalized messages and explicit flags display.
- what it must NOT contain: hidden flag collapsing by default.

### `src/viewer/app.py`
- purpose: minimal local viewer entrypoint.
- what it must contain: load canonical output and wire list/detail views.
- what it must NOT contain: ingest/canonical business logic.

### `tests/test_source.py`
- purpose: validate source ingest determinism and error handling.
- what it must contain: fixed-path read tests and deterministic source id assertions.
- what it must NOT contain: parser/canonical assertions.

### `tests/test_parse.py`
- purpose: validate supported-format parsing.
- what it must contain: `RawRecord` shape and stable indexing checks.
- what it must NOT contain: viewer assertions.

### `tests/test_canonical.py`
- purpose: validate normalization and flag emission.
- what it must contain: stable canonical id tests; ambiguity/loss flag tests.
- what it must NOT contain: export byte-equality checks.

### `tests/test_export.py`
- purpose: validate deterministic JSON/JSONL outputs.
- what it must contain: repeat-run byte equality (JSON) and content parity (JSON vs JSONL).
- what it must NOT contain: viewer rendering checks.

### `tests/test_viewer_smoke.py`
- purpose: validate viewer launch and basic read-only rendering.
- what it must contain: list/detail load smoke tests using fixture-derived canonical data.
- what it must NOT contain: browser automation beyond smoke-level checks.

## 5. DATA FLOW
`source -> parse -> canonical -> export -> viewer`

- source: local files become `SourceFile[]`.
- parse: `SourceFile[]` becomes `RawRecord[]`.
- canonical: `RawRecord[]` becomes `CanonicalRecord[]` plus flags.
- export: `CanonicalRecord[]` becomes deterministic JSON/JSONL artifacts.
- viewer: reads canonical artifacts and renders read-only list/detail views.

## 6. MVP SCHEMAS

### minimal canonical record structure
```json
{
  "canonical_id": "string",
  "source_file_id": "string",
  "source_record_index": 0,
  "title": "string|null",
  "messages": [
    {
      "message_index": 0,
      "role": "user|assistant|system|unknown",
      "content": "string",
      "timestamp": "string|null"
    }
  ],
  "flags": [
    {
      "type": "warning|ambiguity|loss",
      "code": "string",
      "message": "string",
      "path": "string|null",
      "severity": "info|warn|error"
    }
  ]
}
```

### warning/ambiguity/loss flag fields
- `type`: one of `warning`, `ambiguity`, `loss`.
- `code`: stable machine-readable identifier.
- `message`: human-readable explanation.
- `path`: optional pointer to affected field.
- `severity`: `info`, `warn`, or `error`.

## 7. FIRST PASS FIXTURES
- `sample_supported_export.json`: valid baseline with at least one full conversation and two roles.
- `sample_ambiguous_export.json`: structurally valid input where role or message structure is ambiguous and must trigger ambiguity flag.
- `sample_lossy_export.json`: structurally valid input containing unsupported block that forces reduction and must trigger loss flag.

## 8. TEST PLAN
- source tests:
  - deterministic source ID from same input across repeated runs.
  - explicit read failure status for missing/unreadable file.
- parse tests:
  - supported fixture parses into expected `RawRecord` count.
  - raw record ordering/indexes stable.
- canonical tests:
  - canonical IDs stable across repeated runs.
  - ambiguity fixture emits at least one `ambiguity` flag.
  - lossy fixture emits at least one `loss` flag.
- export tests:
  - JSON output byte-identical across repeated runs.
  - JSONL lines map one-to-one with canonical records in JSON.
- viewer smoke tests:
  - viewer loads canonical artifact.
  - list view shows records.
  - detail view shows messages and flags.

## 9. STOP CONDITIONS
Phase 1 stops only when all are true:
1. one export format is documented and parsed end-to-end.
2. canonical records are produced with deterministic IDs.
3. ambiguity/loss are always explicit via flags.
4. deterministic JSON export passes repeat-run byte equality.
5. JSONL output (if enabled) matches canonical JSON content.
6. local viewer renders read-only list/detail with visible flags.
7. all Phase 1 tests pass.

Phase 1 must also stop if any scope creep appears in implementation PRs:
- paid analytics/scoring
- CLI features
- multi-format parser expansion
- non-essential UX/dashboard additions
