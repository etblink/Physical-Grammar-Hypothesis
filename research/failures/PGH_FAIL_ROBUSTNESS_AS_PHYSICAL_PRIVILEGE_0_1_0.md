# PGH-FAIL-0007 — Representation Robustness as Physical Privilege 0.1.0

## Identity

```text
DERIVATION_ID = PGH-FAIL-0007
OPERATION_ID = PGH0_CONTEXT_RECORD_ANCHOR_ROBUSTNESS_GATE
STATUS = FAILED_PRESERVED
CLAIMED_RESULT = REPRESENTATION_ROBUSTNESS_SELECTS_THE_UNIQUE_PHYSICALLY_CORRECT_CONTEXT_RECORD_ANCHOR
FAILURE_CLASS = UNDERDETERMINED
```

## Failed idea

One might hope that once a semantic anchor survives faithful translation between formal presentations, representation robustness itself identifies the physically correct anchor.

That inference fails.

## Counterexample family

Use one presentation with identity translation and two terminal labels `u,v`.

Define a fine record map

```text
rho_fine(u) = 0
rho_fine(v) = 1
```

and a coarse record map

```text
rho_coarse(u) = 0
rho_coarse(v) = 0
```

Both maps are perfectly robust under identity translation:

\[
\rho(\operatorname{id}(t))=\rho(t).
\]

Yet whenever the evaluator can produce both `u` and `v`, the fine anchor distinguishes responses that the coarse anchor identifies.

Thus two representation-robust anchors can induce different equivalence partitions.

## Why the failure matters

Representation robustness is a consistency constraint on a chosen interface. It does not determine which distinctions are physically meaningful.

```text
ROBUSTNESS = NECESSARY_CANDIDATE_CONSISTENCY_PROPERTY
ROBUSTNESS = SUFFICIENT_FOR_PHYSICAL_PRIVILEGE = NO
```

The same problem persists for more elaborate faithful translations: if multiple record/interface maps commute with the translation structure, robustness alone does not select among them.

## What remains valid

This failure does not invalidate:

- the context/record semantic-anchor schema;
- anchor/response-law separation;
- commuting translation of record profiles;
- anchor-relative equivalence on a declared shared interface.

It invalidates only the promotion from representation robustness to physical privilege.

## Result

```text
PGH-FAIL-0007 = FAILED_PRESERVED
UNIQUE_PHYSICAL_ANCHOR_FROM_ROBUSTNESS = NO
R1_SOLVED = NO
NEXT_BURDEN = EMPIRICAL_INTERFACE_PRIMITIVE_ADMISSIBILITY
```

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = CONTEXT_RECORD_ANCHOR_SCHEMA
RULE_DEPENDENCIES = REPRESENTATION_ROBUSTNESS
LEMMA_DEPENDENCIES = PGH-DER-0008
SEMANTIC_ASSUMPTIONS = RECORD_MAPS_MAY_DIFFER_IN_COARSENESS
PHYSICAL_ASSUMPTIONS = NONE
SOURCE_DEPENDENCIES = FROZEN_37_SOURCE_LANDSCAPE_AS_CONTROL_ONLY
```
