## 1. KERNEL
A local tool that ingests one supported conversation export format, converts it into deterministic canonical records with explicit ambiguity/loss flags, and lets users inspect and export that canonical state.

## 2. REQUIRED SPINES

### source
- purpose: read user-provided local files and attach stable source metadata.
- why it is required: no pipeline exists without reliable ingest boundaries.
- what inputs it accepts: list of local file paths.
- what outputs it produces: `SourceFile[]` (id, path, read status, raw content).

### parse
- purpose: parse raw file content into uniform intermediate records.
- why it is required: canonicalization cannot run on raw blobs.
- what inputs it accepts: `SourceFile[]`.
- what outputs it produces: `RawRecord[]` (source link, record index, parse status, raw fields).

### canonical
- purpose: normalize records into canonical records/messages and attach warnings/ambiguity/loss flags.
- why it is required: canonical state is the MVP truth artifact.
- what inputs it accepts: `RawRecord[]`.
- what outputs it produces: `CanonicalRecord[]`.

### export
- purpose: write deterministic machine-readable output from canonical state.
- why it is required: MVP must produce reusable artifacts outside the viewer.
- what inputs it accepts: `CanonicalRecord[]`.
- what outputs it produces: canonical JSON (required) and JSONL (optional, same canonical content).

### viewer
- purpose: provide a basic local read-only inspection surface for canonical output.
- why it is required: Free 1.0 is UI-first in the spec.
- what inputs it accepts: in-memory canonical objects or exported canonical JSON.
- what outputs it produces: list/detail display with visible warning/loss/ambiguity flags.

## 3. MINIMAL BRANCHES

### source
- name: `file_loader`
  - responsibility: read file bytes/text from disk.
  - why it exists: isolate file IO and read errors.
  - type: core.
- name: `source_registry`
  - responsibility: assign deterministic source IDs and preserve input order.
  - why it exists: stable traceability across pipeline stages.
  - type: core.

### parse
- name: `json_export_parser`
  - responsibility: parse one supported export schema into raw objects.
  - why it exists: minimum viable parser for one real format.
  - type: core.
- name: `raw_record_builder`
  - responsibility: emit normalized `RawRecord` structures.
  - why it exists: canonical stage needs a uniform input contract.
  - type: core.

### canonical
- name: `message_normalizer`
  - responsibility: normalize role/content/message sequence.
  - why it exists: create consistent canonical message blocks.
  - type: core.
- name: `flag_emitter`
  - responsibility: emit warnings, ambiguity flags, and loss flags.
  - why it exists: enforce no-silent-loss/no-hidden-ambiguity rule.
  - type: core.
- name: `canonical_builder`
  - responsibility: build final canonical records with deterministic IDs.
  - why it exists: produce the truth artifact used by viewer/export.
  - type: core.

### export
- name: `canonical_json_writer`
  - responsibility: write canonical JSON in deterministic order.
  - why it exists: required MVP export target.
  - type: core.
- name: `canonical_jsonl_writer`
  - responsibility: write one canonical record per JSONL line.
  - why it exists: thin interoperability output.
  - type: thin-supporting logic.

### viewer
- name: `conversation_list`
  - responsibility: show conversation index and flag counts.
  - why it exists: navigation and quick status visibility.
  - type: core.
- name: `conversation_detail`
  - responsibility: show normalized messages plus warnings/loss/ambiguity.
  - why it exists: inspection of canonical truth.
  - type: core.

## 4. DEFERRED SPINES / BRANCHES
- advanced detection layers not needed for the first supported format.
- session analytics and summary intelligence.
- premium metrics and any paid 2.0-style analysis.
- scoring/ranking/classification systems.
- CLI parity and command surface.
- batch orchestration and large-job pipelines.
- non-essential filters beyond basic list/detail browsing.
- speculative UX features (dashboards, customization, collaboration).

## 5. NEW REPOSITORY RECOMMENDATION
- candidate names:
  1. `conversation-canonicalizer`
  2. `free1-canonical-mvp`
  3. `chat-export-canonical`
- best name: `conversation-canonicalizer`.
- reason: plain technical meaning, credible on GitHub, and clear in a portfolio without internal project context.

## 6. DIRECTORY TREE
```text
conversation-canonicalizer/
  README.md
  pyproject.toml
  src/
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
    schemas/
      source_file.py
      raw_record.py
      canonical_record.py
      flags.py
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
    PHASE1_SCOPE.md
    SUPPORTED_FORMAT.md
```

## 7. MODULE CONTRACTS

### `schemas`
- purpose: shared typed contracts for pipeline data.
- public interface: `SourceFile`, `RawRecord`, `CanonicalRecord`, `WarningFlag`.
- key functions/classes: data models only.
- invariants: explicit required/optional fields; stable identifiers.
- dependencies allowed: typing/dataclasses (or pydantic only).
- dependencies forbidden: IO, parser, canonical logic, viewer framework.

### `engine.source`
- purpose: deterministic local ingest and source registration.
- public interface: `load_sources(paths) -> list[SourceFile]`.
- key functions/classes: `load_file`, `register_sources`.
- invariants: stable source ID generation; explicit read failures.
- dependencies allowed: stdlib IO/pathlib/hashlib + `schemas`.
- dependencies forbidden: parse/canonical/export/viewer modules.

### `engine.parse`
- purpose: transform source content into raw records for one supported format.
- public interface: `parse_sources(source_files) -> list[RawRecord]`.
- key functions/classes: `parse_export_json`, `build_raw_record`.
- invariants: source linkage retained; deterministic record indexing; parse errors preserved.
- dependencies allowed: stdlib json + `schemas`.
- dependencies forbidden: canonical/viewer/export writers.

### `engine.canonical`
- purpose: deterministic normalization and truth-flag emission.
- public interface: `canonicalize(raw_records) -> list[CanonicalRecord]`.
- key functions/classes: `normalize_messages`, `emit_flags`, `build_canonical`.
- invariants: deterministic canonical IDs; no silent loss; ambiguity/loss must be explicit.
- dependencies allowed: `schemas` + parse outputs.
- dependencies forbidden: viewer UI and file export code.

### `engine.export`
- purpose: deterministic serialization of canonical state.
- public interface: `write_json(canonical, path)`, `write_jsonl(canonical, path)`.
- key functions/classes: JSON writer, JSONL writer.
- invariants: stable ordering; same input -> byte-identical output.
- dependencies allowed: stdlib json/pathlib + `schemas`.
- dependencies forbidden: parser/source internals and viewer components.

### `viewer`
- purpose: local read-only inspection UI for canonical output.
- public interface: `run_viewer(canonical_path_or_data)`.
- key functions/classes: app entrypoint, list component, detail component.
- invariants: never mutates canonical data; always renders flags clearly.
- dependencies allowed: minimal local UI framework + `schemas`.
- dependencies forbidden: canonical transformation and exporter write logic.

## 8. ACCEPTANCE CRITERIA
MVP is working only if all conditions pass:
1. ingest: loads at least one documented export fixture (`sample_supported_export.json`).
2. parse: emits `RawRecord[]` with deterministic source/record indexes.
3. canonical: emits `CanonicalRecord[]` with stable IDs across repeated runs.
4. truth flags: ambiguous/lossy fixtures emit explicit warning/ambiguity/loss flags.
5. export: JSON export is deterministic (same input run twice -> identical bytes).
6. export format: JSONL export (if enabled) matches canonical JSON content record-for-record.
7. viewer: local viewer renders conversation list and detail with visible flags.
8. tests: automated tests cover source, parse, canonical, export determinism, viewer smoke.

## 9. BUILD ORDER
1. define `schemas` models and invariants.
2. implement `engine.source` (load + deterministic source registration).
3. add one supported export fixture and schema note in `docs/SUPPORTED_FORMAT.md`.
4. implement `engine.parse` for that single format.
5. implement `engine.canonical` (normalization + flag emission + deterministic IDs).
6. implement deterministic JSON export.
7. implement JSONL writer.
8. implement minimal read-only viewer (list + detail).
9. implement tests and lock deterministic output fixtures.
10. finalize README with exact supported format and explicit non-goals.

## 10. OUT-OF-SCOPE
- paid 2.0 features of any kind.
- CLI 3.0 features of any kind.
- semantic scoring, ranking, or conversation quality grading.
- multi-format parser expansion beyond the first supported format.
- advanced filters, analytics dashboards, or trend views.
- cloud features, auth, accounts, sync, or collaboration.
- workflow automation/batch scheduling.
- plugin systems and extension APIs.

## 11. FINAL RECOMMENDATION
A. build new repo immediately from Free 1.0 spec.

Reason: this repo is a spec container; mixing implementation here will keep scope muddy. Start a separate small implementation repo with strict MVP boundaries and treat this repo as upstream contract documentation.
