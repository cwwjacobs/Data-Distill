

cli_v3 = """# Index Conversations — CLI 3.0 Freeze
## CLI / Power Surface Edition
### Frozen concept file for later dedicated 3-phase loop

Date frozen: 2026-03-11
Status: Frozen after Free 1.0 and Paid 2.0 separation

---

## Purpose

CLI 3.0 is the later command-line surface for the same engine that powers Free 1.0 and later Paid 2.0.

It is not a separate parser.
It is not a second implementation path.
It is not allowed to drift from the UI/engine result.

Its purpose is:
- parity
- automation
- credibility
- power-user workflows
- inspectable deterministic operation

CLI 3.0 receives its own complete 3-phase loop after Free 1.0 and Paid 2.0 are properly established.

---

## Relationship to Free 1.0 and Paid 2.0

### Free 1.0
Primary UI-first product surface.
No CLI required for core value.

### Paid 2.0
Trace curation and analytics branch built on canonical serialized state.

### CLI 3.0
Optional but real power surface built last, after the engine math and serialization basis are already stable.

CLI 3.0 must consume the same engine and same canonical state model as the UI surfaces.

---

## Core Thesis

The CLI exists because:
- some users want automation
- some users want batch workflows
- some users want terminal surfaces
- it strengthens technical credibility
- it is useful for internal workflows and future advanced users

But it is built **last** so that its logic cannot distort the primary UI-first product.

---

## Non-Negotiable Invariants

- One engine only.
- No second parser.
- No second canonicalization logic.
- Same input + same options = same canonical result across UI and CLI.
- No CLI-only math.
- No CLI-only export truth.
- No CLI-only hidden power that changes determinism.
- CLI must read and write the same canonical state contracts.
- CLI should help audit determinism, not undermine it.
- Surface parity matters more than terminal cleverness.

---

## What CLI 3.0 Is

CLI 3.0 is an alternate surface for:
- ingest
- canonical state generation
- inspection summaries
- export actions
- batch operations
- deterministic reporting

It should be elegant and credible, but not separate in logic.

---

## What CLI 3.0 Is Not

- not the primary v1 customer path
- not a replacement for the viewer
- not an excuse to duplicate logic
- not a place for experimental parser features
- not a place to hide extra export behavior
- not a shortcut around UI truthfulness rules

---

## Why It Is Last

CLI is deliberately last because:
- the engine must be stable first
- Free 1.0 UI math must already be correct
- Paid 2.0 data/analysis expectations must already be known
- parity is easier when the engine contracts are frozen
- earlier CLI work previously created determinism drift

So CLI receives its own later 3-phase loop:
1. define CLI scope and contracts
2. build CLI against frozen engine
3. test parity and polish CLI surface

---

## CLI 3.0 Responsibilities

- expose engine operations clearly
- support canonical ingest generation
- support export commands
- support summary/report outputs
- support repeatable scripted use
- respect same validations as UI
- provide human-readable and machine-readable output modes

---

## Strong Candidate CLI Commands / Actions

These are frozen as concepts only, not final syntax.

- ingest files
- emit canonical state
- emit normalized export
- emit target-specific exports
- show ingest summary
- show file/record status counts
- validate export readiness
- print warnings / ambiguity / loss counts
- inspect a record by id
- list files / list conversations / list statuses

No syntax is locked yet.

---

## Output Modes

CLI should eventually support:
- human-readable terminal summaries
- machine-readable JSON output
- saved artifact output files

But all of them must derive from the same engine state.

---

## Parity Requirements

CLI and UI must align on:
- canonical ids
- file/session accounting
- warnings
- ambiguity flags
- loss flags
- export inclusion/exclusion
- normalized timestamps
- detection outcomes
- summary counts

If parity breaks, the engine is wrong or the surface is wrong. No silent divergence allowed.

---

## Aesthetic / Product Requirements

Even though CLI is not the primary surface, it should still be:
- beautiful
- restrained
- branded enough to feel intentional
- readable
- credible
- useful

This is not throwaway tooling.

---

## Things Explicitly Deferred Until CLI 3.0 Phase 1

- exact command syntax
- exact flag structure
- exact TUI vs plain CLI decisions
- packaging/distribution decisions
- shell completion
- advanced batch orchestration
- any remote/server modes

These are intentionally deferred.

---

## What Must Not Be Forgotten Later

- CLI is not optional in the long run.
- CLI is last because parity matters.
- CLI must respect the same contracts as UI and Paid 2.0.
- CLI should strengthen determinism trust, not weaken it.
- CLI can be beautiful and credible without becoming a separate product.

---

## Frozen Summary

CLI 3.0 is the later power-user and automation surface for the same engine that drives Free 1.0 and Paid 2.0.

It must:
- be real
- be elegant
- be deterministic
- be engine-parity strict
- never introduce separate math or parsing paths

This file freezes the concept only.
CLI implementation planning happens later, after Free 1.0 and Paid 2.0 are properly established.
"""

phase1_v1 = """# Index Conversations — Free 1.0 Phase 1 Formalization
## 1 / 3 phased build: Phase 1
### Goal freeze, kernel, boundary, spine, and today's build logic

Date formalized: 2026-03-11

---

## Phase 1 Purpose

Define Free 1.0 correctly before Phase 2 build begins.

This phase is not implementation.
This phase is not polish.
This phase is the structural freeze that prevents drift.

---

## Kernel

Free 1.0 is a **UI-first local canonical conversation ingestion tool**.

Its job is to:
- ingest conversation/archive files locally
- produce the clearest honest canonical parse state possible
- show what happened at ingest
- make that state inspectable
- export that canonical state and a small set of useful downstream outputs

---

## One-Line Product Promise

Load conversation exports, get the clearest honest canonical view we can produce, see what happened at ingest, and export the result in useful plain forms.

---

## Artifact Boundary for Free 1.0

Free 1.0 is complete when a user can:

1. open the UI
2. load one or more files without CLI
3. see per-file and per-session ingest results
4. inspect canonicalized conversations clearly
5. understand what was preserved, reduced, unsupported, ambiguous, or failed
6. filter the resulting session sanely
7. export the canonical ingest state
8. export a small set of useful validated outputs

---

## What Free 1.0 Is

- UI-first
- local-only
- engine-backed
- canonicalization-first
- transparent about ingest behavior
- honest about limits
- useful even without training/corpus goals

---

## What Free 1.0 Is Not

- not the full provenance product
- not the training corpus product
- not the semantic labeling product
- not the CLI-first product
- not the Golden Trace analytics layer
- not the deep metadata/provenance registry
- not the place for interpretive scoring

---

## Necessary Core Outcome

The primary artifact of Free 1.0 is the **canonical ingest state**.

The viewer is a surface for inspecting that state.
Downstream exports are derived from that state.

This means the pretty transcript is not the source truth.
It is a derived view.

---

## Non-Negotiable Invariants

- UI is the primary customer path.
- No CLI required for core value.
- One engine only.
- No silent destructive ingest.
- No single-path GPT reduction as preserved truth.
- No fake-clean success language.
- No misleading summary labels.
- No hidden ambiguity.
- No hidden loss.
- No hidden unsupported structures.
- Canonical ingest state must be exportable.
- Same input must lead to the same canonical result.
- Free 1.0 must remain free-tier useful on its own, not crippled for Paid 2.0.

---

## Preserve vs Defer

### Preserve in Free 1.0
- UI language and visual identity
- local-only workflow
- multi-file import direction
- compact filters near search
- transcript readability
- performance-aware list behavior
- accessibility hardening
- per-file provenance-lite carry-through
- result/accounting feedback
- export validation logic where useful and simple

### Defer to Paid 2.0
- deep provenance system
- training corpus shaping
- semantic labels
- emotive language identification
- density beyond token count
- teacher/student analytics
- trace scoring
- Golden Trace curation logic

### Defer to CLI 3.0
- terminal surface
- batch automation surface
- command design
- CLI UX/polish

---

## Free 1.0 Minimum Spine

1. Source intake
2. Raw parse
3. Per-record detection
4. Canonical ingest shaping / preservation
5. Normalized inspectable session state
6. Viewer/accounting surface
7. Filtering/review
8. Export validation/output

---

## Necessary Data Artifacts

### SourceFile
- file id
- filename
- file status
- file error/warning counts

### RawRecord
- source file id
- record index
- raw payload
- raw parse status

### CanonicalConversation
- canonical id
- source record id if available
- source type
- file origin
- title raw + canonical
- created raw + normalized
- updated raw + normalized
- canonical messages/blocks
- warnings
- loss flags
- ambiguity flags
- ingest notes

### SessionState
- files loaded
- records seen
- records canonicalized
- partials
- failures
- source summary
- export availability summary

---

## Required Free 1.0 Exports

### Primary
- canonical ingest state
- normalized conversations JSON

### Secondary
- useful plain transcript / plain JSON exports if simple and honest

### Conditional
- target-specific exports only when validation is simple and clear enough not to mislead

---

## Viewer Rules

The viewer remains HTML/UI-first and should:
- clearly show ingest outcomes
- clearly show active filters
- clearly show total vs shown counts
- remain compact
- remain visually strong
- not become dashboard sprawl

---

## Today's Build Logic (Phase 2 entry rule)

Phase 2 should build **Free 1.0 only**.

Paid 2.0 is frozen.
CLI 3.0 is frozen.

Implementation lead preference:
- Codex as primary builder
- structured against this Phase 1 freeze
- with us holding kernel, invariants, branch review, and red-team judgment

---

## Build Order for Free 1.0 Phase 2

1. engine contracts and canonical state model
2. ingest + raw parse + detection
3. canonical ingest shaping
4. viewer/session/accounting integration
5. filters and feedback clarity
6. export layer
7. integration pass
8. full Phase 3 test/red-team/polish

This is branch order, not per-branch polish.

---

## Phase 3 Entry Rule

Do not open full Free 1.0 Phase 3 until the Free 1.0 spine is complete enough to test as a coherent artifact.

Branch-level checks are allowed during build.
True polish happens after the 1.0 artifact boundary is reached.

---

## Frozen Summary

Free 1.0 is a UI-first local canonical conversation ingestion tool.

Its core value is:
- honest ingest
- canonicalized output
- clear viewer feedback
- useful exports

This Phase 1 file freezes what Free 1.0 must be before build proceeds.
"""

base = Path("/mnt/data")
paths = {
    "v2_updated": base / "index_conversations_paid_2_0_freeze_updated.md",
    "v3_cli": base / "index_conversations_cli_3_0_freeze.md",
    "v1_phase1": base / "index_conversations_free_1_0_phase1_formalization.md",
}
paths["v2_updated"].write_text(paid_v2, encoding="utf-8")
paths["v3_cli"].write_text(cli_v3, encoding="utf-8")
paths["v1_phase1"].write_text(phase1_v1, encoding="utf-8")

print(str(paths["v2_updated"]))
print(str(paths["v3_cli"]))
print(str(paths["v1_phase1"]))
