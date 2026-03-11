Free1.0 — Builder Invariants (Codex Rules)

These apply to every Codex build exchange.

Build Scope Discipline

Codex must:

modify only requested modules

avoid speculative files

avoid architectural redesign

No Feature Drift

Codex must not introduce:

semantic scoring

ML labeling

corpus scoring

training pipeline logic

Those belong to 2.0.

Module Isolation

Each module must:

expose a clear interface

not reach across layers

not mutate unrelated state

Deterministic Logic Only

No:

randomness

timestamp-based IDs

order instability

IDs must derive from:

source_file
record_index
message_index
Engine → Viewer Boundary

Viewer can call:

engine.getSessionState()
engine.getConversation()
engine.getFilteredState()

Viewer must never modify canonical data.

Builder Summary Requirement

At the end of every Codex response, Codex must append:

Builder Summary
---------------
Files created:
Files modified:
Modules touched:
Why:
What remains unchanged:

This replaces the need for an internal auditor.

You will provide diff review externally.

Free1.0 Kernel → Spine (Branch Map)

Now we map the actual build sequence.

ROOT
Free1.0ui+backend
Spine
ENGINE
VIEWER
EXPORT
Engine Branch
engine/
Branch 1 — Source Intake
engine/source/

modules

file_loader
file_registry
fingerprint

produces

SourceFile[]
Branch 2 — Raw Parse
engine/parse/

modules

json_reader
text_reader
raw_record_builder

produces

RawRecord[]
Branch 3 — Record Detection
engine/detect/

modules

conversation_detector
message_detector
role_detector
timestamp_detector
structure_validator

produces

DetectedRecord[]
Branch 4 — Canonicalization
engine/canonical/

modules

role_normalizer
timestamp_normalizer
message_block_builder
warning_system
loss_system
ambiguity_system
canonical_conversation_builder

produces

CanonicalConversation[]
Branch 5 — Session State
engine/session/

modules

session_builder
session_counters
file_status
record_status

produces

SessionState
Branch 6 — Filter Engine
engine/filter/

modules

search_filter
file_filter
status_filter
date_filter
length_filter

produces

FilteredSessionState
Branch 7 — Export Validation
engine/export_validation/

modules

canonical_validator
export_readiness
ambiguity_checker
loss_checker

produces

ExportReport
Branch 8 — Export Output
engine/export/

modules

canonical_exporter
normalized_exporter
transcript_exporter

produces

exports/*
Viewer Branch
viewer/

modules

session_summary
conversation_list
conversation_view
message_block
filter_controls
status_indicators
export_controls

Consumes

ViewerState
FilteredSessionState
ExportReport
Kernel Path

End-to-end flow:

FILES
 ↓
SOURCE_INTAKE
 ↓
RAW_PARSE
 ↓
RECORD_DETECTION
 ↓
CANONICALIZATION
 ↓
SESSION_STATE
 ↓
VIEW_MODEL
 ↓
FILTER_ENGINE
 ↓
EXPORT_VALIDATION
 ↓
EXPORT_OUTPUT
Phase 2 Build Order (for Codex)

Strict order:

1 engine/source
2 engine/parse
3 engine/detect
4 engine/canonical
5 engine/session
6 engine/filter
7 engine/export_validation
8 engine/export
9 viewer