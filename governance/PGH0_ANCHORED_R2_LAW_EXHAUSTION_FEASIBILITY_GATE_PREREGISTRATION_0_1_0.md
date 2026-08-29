# PGH-0 Anchored R2 Law-Exhaustion Feasibility Gate — Preregistration 0.1.0

## Status

```text
OPERATION_ID = PGH0_ANCHORED_R2_LAW_EXHAUSTION_FEASIBILITY_GATE
REGISTRY_ID = PGH-OP-0030
OPERATION_CLASS = SOURCE_BOUND_FOUNDATIONAL_FEASIBILITY_GATE
STATUS = PREREGISTERED_IN_PROGRESS
CANONICAL_BASE = f3f9dcabcb5154a75dcb82b869f6fe867689929c
WORKING_BRANCH = research/pgh0-anchored-r2-law-exhaustion
FROZEN_SOURCE_COUNT = 37
NEW_SOURCE_SEARCH = FORBIDDEN_UNLESS_A_SPECIFIC_BLOCKING_GAP_IS_DEMONSTRATED
ANCHOR = HELD_FIXED
ACTIVE_GRAMMAR_BASELINE = PGH-GRAM-0002
NEW_GRAMMAR_SELECTION = FORBIDDEN
EMPIRICAL_PREDICTION = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

`PGH-OBJ-0012`, the anchored strong physical grammar hypothesis, permits a minimal law-free physical reference/contact anchor but still requires grammar to exhaust **substantive physical law**.

This gate asks whether the currently justified grammar architecture can meet even the first R2 feasibility burden:

> With the law-free anchor held fixed, does the grammar generate at least one substantive physical restriction that is neither already contained in the anchor nor supplied by an independent law-like selector?

The gate does not search for a new physical grammar. It audits the explanatory capacity of the current baseline and already-qualified grammar/coherence machinery.

## Fixed anchor firewall

Hold fixed the canonical law-free contact architecture:

\[
A_{ref}=(C,R,\iota_C,\rho).
\]

The anchor may identify probe/interface and record reference, but it contains no:

```text
ALLOWED_RESPONSE_RELATION
RESPONSE_FUNCTION
PROBABILITY_OR_AMPLITUDE_RULE
COMPLETE_POSSIBILITY_SET
TARGET_DISTINGUISHABILITY_PARTITION
```

No R2 credit may be assigned to a restriction already implicit in the anchor.

## Fixed grammar baseline

The active grammar baseline remains `PGH-GRAM-0002`, the extensional formation baseline.

Its already-canonical control is:

```text
PGH-FAIL-0001 = BARE_FORMATION_GRAMMAR_PHYSICAL_SUFFICIENCY
```

An unrestricted formation relation can encode an arbitrary admissibility table. Therefore a restriction receives no R2 credit merely because it is written into `F`.

## R2 credit standard

A candidate restriction `R` can count at this gate only if all of the following hold:

```text
R2A_ANCHOR_HELD_FIXED
R2B_R_IS_NOT_PRIMITIVE_IN_ANCHOR
R2C_R_IS_NOT_A_LOOKUP_TABLE_ENTRY_OR_ARBITRARY_FORMATION_MEMBERSHIP
R2D_R_FOLLOWS_FROM_A_COMPACT_GENERATIVE_OR_COHERENCE_PRINCIPLE_ALREADY_JUSTIFIED_INDEPENDENTLY_OF_TARGET_R
R2E_NO_INDEPENDENT_LAW_L_IS_NEEDED_TO_SELECT_R
R2F_R_HAS_A_PHYSICAL_INTERPRETATION_NOT_MERELY_FORMAL_WELL_FORMEDNESS
R2G_AT_LEAST_ONE_COUNTERMODEL_OR_ALTERNATIVE_ALLOWED_BY_WEAKER_STRUCTURE_VIOLATES_R
```

Formal exclusion without physical interpretation is not enough.

Physical interpretation without non-arbitrary derivation is not enough.

## Locked tests

### T1 — Bare formation universal-encoding control

Reapply the canonical result that any desired finite admissibility relation can be installed directly as the formation relation.

If the supposed physical restriction is merely membership/nonmembership in a freely chosen formation table, it fails R2C.

### T2 — Extensionality/quotient control

Test whether contextual extensional reduction by itself excludes any substantive physical possibility rather than merely canonicalizing descriptions.

### T3 — Coherence-law control

Test the strongest existing compact formal exclusion:

```text
PARSE_COHERENCE -> ASSOCIATIVITY
```

Determine whether this can receive R2 physical credit without separately justifying that parenthesization is physically representational and that the binary-operation realization is physically adequate.

### T4 — Grammar-generated empirical closure control

Test whether least empirical-interface closure produces a physical response/possibility restriction or only determines which formal contexts become available once grammar constructors are fixed.

### T5 — Physical-interpretation bridge control

No formal theorem may receive R2 credit unless a physical interpretation bridge is available that does not itself encode the target restriction.

If no such bridge currently exists, record that as a scientific failure at the present candidate scope rather than inventing one.

### T6 — Independent-law test

If recovering a substantive physical possibility set still requires an extra selector

\[
L:W(G)\to\{\text{physical},\text{nonphysical}\},
\]

or equivalent law-like input, R2 fails at current scope.

### T7 — Source-gap test

A source expansion is justified only if a specific missing literature question blocks the audit of the current baseline. The absence of a candidate physical grammar is not by itself permission for unbounded source search.

## Outcome space

```text
A = CURRENT_ANCHORED_GRAMMAR_ARCHITECTURE_GENERATES_AT_LEAST_ONE_SUBSTANTIVE_PHYSICAL_RESTRICTION_WITHOUT_INDEPENDENT_LAW

B = CURRENT_ARCHITECTURE_GENERATES_FORMAL_EXCLUSIONS_BUT_NO_R2_QUALIFYING_PHYSICAL_RESTRICTION__CURRENT_GRAMMAR_BASELINE_IS_INSUFFICIENT

C = LAW_FREE_ANCHOR_CANNOT_BE_HELD_FIXED__SUBSTANTIVE_PHYSICAL_LAW_MUST_ENTER_THROUGH_SEMANTICS_AND_THE_ANCHORED_SUCCESSOR_COLLAPSES

D = SPECIFIC_BLOCKING_SOURCE_GAP_IDENTIFIED

E = UNRESOLVED
```

No outcome is a ranking.

## Acceptance criteria

```text
B1_ANCHOR_IS_HELD_FIXED
B2_LOOKUP_TABLE_EXCLUSIONS_RECEIVE_NO_R2_CREDIT
B3_FORMAL_CANONICALIZATION_IS_NOT_CONFUSED_WITH_PHYSICAL_EXCLUSION
B4_COHERENCE_RESULTS_REQUIRE_AN_INDEPENDENT_PHYSICAL_INTERPRETATION_BRIDGE
B5_INTERFACE_CLOSURE_IS_NOT_MISCOUNTED_AS_RESPONSE_LAW
B6_NO_NEW_PHYSICAL_BRIDGE_IS_INVENTED
B7_NO_INDEPENDENT_LAW_SELECTOR_IS_HIDDEN_IN_GRAMMAR_OR_SEMANTICS
B8_CURRENT_GRAMMAR_IS_NOT_PROMOTED_TO_PHYSICAL_STATUS_WITHOUT_EVIDENCE
B9_SOURCE_GAP_DECISION_IS_EXPLICIT
B10_NO_EMPIRICAL_PREDICTION_OR_FCP_EFFECT_IS_CLAIMED
```

## Required outputs

Commit 1 may add only:

```text
governance/PGH0_ANCHORED_R2_LAW_EXHAUSTION_FEASIBILITY_GATE_PREREGISTRATION_0_1_0.md
```

Commit 2 may add only:

```text
audits/PGH0_ANCHORED_R2_LAW_EXHAUSTION_FEASIBILITY_GATE_0_1_0.md
research/failures/PGH_FAIL_CURRENT_GRAMMAR_R2_LAW_EXHAUSTION_0_1_0.md
handoffs/PGH0_ANCHORED_R2_LAW_EXHAUSTION_FEASIBILITY_GATE_HANDOFF_0_1_0.md
```

A new derivation artifact is permitted only for outcome `A` and must identify the exact physical restriction and assumption ancestry.

Do not mutate current-state/navigation files on the scientific branch.

## Commit boundary

```text
COMMIT_1_MESSAGE = Preregister PGH-0 anchored R2 law exhaustion feasibility gate
COMMIT_2_MESSAGE = Adjudicate PGH-0 anchored R2 law exhaustion feasibility gate
```

Exactly two commits are permitted.

## Hard stops

Stop before:

- inventing or selecting a new physical grammar;
- importing a known physical law as a grammatical axiom;
- searching for sources without a specific blocking gap;
- empirical prediction;
- claiming PGH truth or novelty;
- changing FCP;
- mutating canonical `main` before independent review.
