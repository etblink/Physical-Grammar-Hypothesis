# PGH Artifact and Provenance Policy 0.1.0

## Status

```text
POLICY_ID = PGH_ARTIFACT_AND_PROVENANCE_POLICY
VERSION = 0.1.0
STATUS = ACTIVE
PROJECT = Physical Grammar Hypothesis
```

## Purpose

This policy establishes a scalable but deliberately lightweight provenance model for the Physical Grammar Hypothesis (PGH) repository.

It does not change the scientific content of PGH.

The governing authority order is:

```text
GIT = PROVENANCE_AUTHORITY
CANONICAL_MARKDOWN_ARTIFACTS = RESEARCH_AND_GOVERNANCE_AUTHORITY
STRUCTURED_METADATA = DERIVED_NAVIGATION_ONLY
```

If derived metadata conflicts with a canonical research or governance artifact, the underlying canonical artifact wins.

## Artifact classes

### Mutable canonical surfaces

These summarize current state and may be updated by later bounded operations:

```text
README.md
CURRENT_STATE.md
```

They must not silently erase historical results.

### Append-oriented historical surfaces

These accumulate chronology or registry entries:

```text
RESEARCH_LOG.md
meta/PGH_OPERATION_REGISTRY.jsonl
meta/PGH_RESEARCH_OBJECT_REGISTRY.jsonl
meta/PGH_OPEN_QUESTION_REGISTRY.jsonl
```

Existing historical entries should not be rewritten merely to make the project trajectory cleaner. Corrections should be explicit and attributable.

### Versioned canonical artifacts

Accepted bounded artifacts should ordinarily be versioned rather than overwritten:

```text
governance/*_0_1_0.md
research/derivations/*_0_1_0.md
research/failures/*_0_1_0.md
research/formalizations/*_0_1_0.md
research/models/*_0_1_0.md
research/representation_tests/*_0_1_0.md
handoffs/*_0_1_0.md
```

A scientifically material change should create a new version or an explicit superseding artifact.

### Derived navigation

The following are navigation aids, not scientific authority:

```text
meta/PGH_CANONICAL_INDEX.json
```

Derived navigation may be regenerated from canonical state and registries.

## Stable identifiers

Stable IDs are used to prevent filenames or prose labels from becoming the only identity system.

Preferred namespaces:

```text
PGH-OP-####    bounded operation record
PGH-Q-####     open question
PGH-OBJ-####   general research object
PGH-DER-####   derivation
PGH-FAIL-####  failed derivation
PGH-GRAM-####  candidate grammar
```

IDs are permanent once assigned.

Deletion of an object does not free its ID for reuse.

Numeric order is an identity convenience, not a scientific score, ranking, or phase number.

## Research-object status vocabulary

Permitted core statuses include:

```text
ACTIVE_HYPOTHESIS
CANDIDATE
CANDIDATE_NOT_FORMALLY_FIXED
PROVISIONAL
QUALIFIED
FAILED
SUPERSEDED
DEFERRED
REJECTED
HISTORICAL
```

A record may use a more specific status when necessary, but it must not imply scientific acceptance that the associated artifact does not support.

## Derivation status

Every formal derivation should eventually resolve to one of:

```text
PROVISIONAL
QUALIFIED
FAILED
```

A failed derivation remains a first-class research result.

Recommended failure classes are:

```text
CIRCULAR
PHYSICS_SMUGGLED
DEFINITIONAL_TAUTOLOGY
REPRESENTATION_DEPENDENT
NONEXCLUSIVE
SEMANTIC_MAP_SMUGGLING
UNDERDETERMINED
COUNTEREXAMPLE_FOUND
FORMAL_INCONSISTENCY
OTHER_EXPLICIT
```

Failure classes identify what went wrong; they are not severity scores.

## Assumption ancestry

Every substantive derivation artifact should expose its dependency ancestry explicitly.

At minimum:

```text
PRIMITIVE_DEPENDENCIES
RULE_DEPENDENCIES
LEMMA_DEPENDENCIES
SEMANTIC_ASSUMPTIONS
PHYSICAL_ASSUMPTIONS
SOURCE_DEPENDENCIES
```

A claimed grammar-derived physical result is especially significant only if its physical-assumption ancestry is transparent.

The target form for a genuinely grammar-internal derivation is:

```text
PHYSICAL_ASSUMPTIONS = NONE
```

That status must be earned by audit, not asserted from intent.

## No-smuggling provenance

If a later audit shows that a physical assumption entered upstream, the affected derivation must be downgraded or failed explicitly. The original record remains preserved.

Do not repair ancestry by deleting the upstream assumption from history.

## Supersession

Supersession means:

- the old artifact remains historically valid as a record of what was concluded then;
- the new artifact becomes the current authority for the superseded question;
- navigation should point to the new artifact while retaining ancestry.

Supersession does not authorize rewriting old commits or versioned files.

## Source boundary

At repository-opening scope:

```text
SOURCE_BOUND_STATUS = NOT_YET_SOURCE_BOUND
```

The project may discuss broad conceptual background conversationally, but canonical source-bound claims require a separately opened source-intake process.

When source work begins, it should establish explicit source identity, selection, provenance, and admission rules before treating literature as a frozen scientific corpus.

Do not retroactively treat casual citations as a selected source set.

## Scientific non-effects

Repository maintenance, indexing, registry normalization, path reorganization, or navigation regeneration does not by itself:

```text
CHANGE_PGH
ESTABLISH_A_PRIMITIVE
QUALIFY_A_GRAMMAR
QUALIFY_A_DERIVATION
FAIL_A_DERIVATION
CREATE_AN_EMPIRICAL_RESULT
CHANGE_FCP
```

Any such scientific effect requires an explicit research artifact.

## Preservation rule

The repository should preserve:

```text
RESULTS
FAILURES
ASSUMPTIONS
BOUNDARIES
UNCERTAINTIES
```

rather than protecting PGH from adverse results.
