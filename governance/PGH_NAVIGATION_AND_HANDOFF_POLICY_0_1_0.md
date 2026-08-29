# PGH Navigation and Handoff Policy 0.1.0

## Status

```text
POLICY_ID = PGH_NAVIGATION_AND_HANDOFF_POLICY
VERSION = 0.1.0
STATUS = ACTIVE
```

## Purpose

This policy provides durable continuation across large repositories and finite chat context windows without allowing machine-readable navigation to become scientific authority.

## Authority hierarchy

```text
GIT = PROVENANCE_AUTHORITY
CANONICAL_MARKDOWN_ARTIFACTS = RESEARCH_AND_GOVERNANCE_AUTHORITY
STRUCTURED_NAVIGATION_LAYER = DERIVED_NAVIGATION_ONLY
```

Conflict rule:

```text
UNDERLYING_CANONICAL_ARTIFACT_WINS
```

## Core navigation surfaces

The navigation layer consists of:

```text
meta/PGH_CANONICAL_INDEX.json
meta/PGH_OPERATION_REGISTRY.jsonl
meta/PGH_RESEARCH_OBJECT_REGISTRY.jsonl
meta/PGH_OPEN_QUESTION_REGISTRY.jsonl
meta/PGH_NAVIGATION_SCHEMA_0_1_0.json
tools/pgh_navigation.py
```

The registries are structured historical/navigation records. Scientific meaning remains grounded in the canonical artifacts to which they point.

## Canonical index

`meta/PGH_CANONICAL_INDEX.json` is a compact orientation layer for a successor instance.

It should expose at minimum:

```text
schema_version
authority
indexed_research_baseline_commit
indexed_research_baseline_tree
current_phase
latest_completed_operation
current_handoff
canonical_state
canonical_hypothesis
active_candidate_grammar
counts
next_recommended_operation
next_operation_authorized
source_bound_status
fcp_relationship
```

The index may deliberately bind a logical research baseline rather than the enclosing navigation-maintenance commit. This avoids self-reference and preserves the distinction between research state and derived navigation state.

## Operation registry

The operation registry answers:

> What bounded operations exist, what is their status, and what artifacts did they produce?

Every record should have:

```text
registry_id
operation_id
operation_class
status
scientific_change
inputs
outputs
handoff
```

Recommended status values:

```text
RECOMMENDED_NOT_STARTED
AUTHORIZED_NOT_STARTED
IN_PROGRESS
QUALIFIED_LOCAL
CANONICALLY_COMPLETE
FAILED
SUPERSEDED
```

A recommendation is not authorization.

A completed record must not point to nonexistent outputs.

## Research-object registry

The research-object registry answers:

> What conceptual objects are currently or historically being studied?

Each record should have:

```text
object_id
object_type
name
status
canonical_artifact
dependencies
notes
```

Candidate grammar IDs are research objects, not proof that a grammar is physically privileged.

## Open-question registry

The open-question registry answers:

> Which unresolved questions remain live, deferred, or closed?

Each record should have:

```text
question_id
status
question
created_by_operation
related_objects
resolution_artifact
```

Questions should not disappear merely because later work stops mentioning them.

Recommended status values:

```text
OPEN
DEFERRED
RESOLVED
CLOSED_AS_ILL_POSED
SUPERSEDED
```

## Handoff capsules

Each major bounded operation should end with a human-readable handoff containing exactly one machine-readable capsule between:

```text
<!-- PGH_HANDOFF_CAPSULE_BEGIN -->
<!-- PGH_HANDOFF_CAPSULE_END -->
```

with exactly one fenced JSON object between the markers.

Required fields:

```text
capsule_schema_version
operation_id
status
indexed_research_baseline_commit
must_read
outputs
open_questions
next_recommended_operation
next_operation_authorized
do_not_assume
```

The `do_not_assume` field is mandatory because PGH is especially vulnerable to accidental promotion of analogy into derivation.

## Current-state capsule

`CURRENT_STATE.md` should contain exactly one bounded JSON state capsule:

```text
<!-- PGH_CURRENT_STATE_CAPSULE_BEGIN -->
<!-- PGH_CURRENT_STATE_CAPSULE_END -->
```

The capsule provides structured navigation fields only. The surrounding Markdown remains the authoritative human-readable state.

## Handoff continuation discipline

A successor research instance should:

1. verify the live Git baseline;
2. read `CURRENT_STATE.md`;
3. read the current handoff;
4. read every path in the handoff's `must_read`;
5. inspect relevant registries;
6. distinguish completed, recommended, authorized, and unstarted operations;
7. preserve every `do_not_assume` item until separately resolved.

Do not infer progress from phase labels alone.

## Navigation commands

The repository navigation utility supports:

```text
python -B tools/pgh_navigation.py check
python -B tools/pgh_navigation.py build --baseline-commit <commit>
```

`check` is nonmutating.

`build` regenerates only the derived canonical index. It requires an explicit logical research baseline commit so that the caller deliberately chooses what the navigation layer indexes.

## Validation scope

The checker should validate at least:

- JSON and JSONL syntax;
- unique stable IDs;
- recognized registry statuses;
- current-state capsule parsing;
- current-handoff capsule parsing;
- registry counts against the canonical index;
- existence of completed-operation outputs;
- existence of canonical artifacts referenced by active research objects;
- existence of the current handoff;
- validity of handoff open-question references;
- consistency of selected current-state/index fields;
- no missing required `do_not_assume` field.

## Portability

Machine-readable `.json`, `.jsonl`, and `.py` files are pinned to LF by `.gitattributes`.

Markdown is not globally pinned to LF.

Parsers must tolerate ordinary CRLF Markdown checkouts.

Use:

```text
python -B
```

to avoid qualification noise from `__pycache__`.

## Regeneration rule

Navigation regeneration may change derived metadata only.

If regeneration appears to require a scientific reinterpretation, stop and perform a separately bounded research or governance operation.

## Self-reference rule

Do not require a handoff or canonical index to contain the SHA of the commit that contains itself.

Git establishes the enclosing provenance.

Structured navigation should name a previously established logical research baseline where a commit identity is required.
