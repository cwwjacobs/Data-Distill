Free1.0 — Project Invariants

These apply to the entire repository.

Structural Invariants

Single Engine

One canonical engine produces all state.

ingest → canonical_state → viewer → exports

Viewer is Read-Only

Viewer never mutates engine state.

Canonical State Is the Truth

Everything derives from canonical state.

Not:

transcript → export

Always:

canonical_state → transcript/export

Determinism

Same input files must always produce:

same canonical ids

same warnings

same export output

No Silent Reduction

If information is lost:

mark loss_flag

attach warning

Explicit Ambiguity

Ambiguous structures must be flagged.

Engine First

Engine must work without the viewer.

Local Only

Free1.0 must not require:

internet

accounts

cloud services

No Training Assumptions

Free1.0 does not:

shape corpora

score conversations

interpret semantics

Exports Are Honest

Exports must reflect the canonical state exactly.