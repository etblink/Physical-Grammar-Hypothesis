# PGH-1 R2 Primitive Grammar Candidate Family Screen — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_R2_PRIMITIVE_GRAMMAR_CANDIDATE_FAMILY_SCREEN
REGISTRY_ID = PGH-OP-0048
CANONICAL_BASE = 86c97f110b8b1b8d85e7d0c08d4e5352cd857aff
CANDIDATE_STANDARD = PGH-OBJ-0020
R2_TARGET = PGH-OBJ-0021
FROZEN_ACCEPTED_SOURCE_COUNT = 70
NEW_SOURCE_SEARCH = FORBIDDEN
PHYSICAL_FIT = FORBIDDEN
PHYSICAL_BRIDGE = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Freeze and screen a small doctrine family before any physical-fit evaluation.

The screen asks two separate questions:

1. does the doctrine pass the structural/nontriviality controls of `PGH-OBJ-0020` as a fixed formal shell?
2. is the doctrine alone a sufficiently complete **candidate grammar**, or does it remain parameterized by an unearned generator/signature/theory seed?

## Frozen doctrine family

The family is selected only because each member arose in the completed structural-package/doctrine-origin sequence.

```text
D0 = BARE_MONOIDAL
D1 = SYMMETRIC_MONOIDAL
D2 = CARTESIAN_FINITE_PRODUCT
D3 = COCARTESIAN_FINITE_COPRODUCT
D4 = BICARTESIAN_PRODUCT_AND_COPRODUCT
```

No physical interpretation or ranking is attached to these labels.

## Fixed comparison rule

For each doctrine test:

```text
P0 FORMAL_DEFINABILITY
P1 DECLARED_PRIMITIVES
P2 PRE_TARGET_FIXATION
P3 RESTRICTED_HYPOTHESIS_CLASS / UNIVERSAL_ENCODING
P4 NO_EXTENTIONAL_TARGET_TABLE
P5 GENERATIVE_COMPRESSION
P6 NONTRIVIAL_FORMAL_EXCLUSION
P7 REPRESENTATION_DISCIPLINE
P8 LAW_FREE_SEMANTIC_BOUNDARY
P9 INDEPENDENT_FORMAL_CONSEQUENCE
P10 COUNTEREXAMPLE_EXPOSURE
P11 PHYSICAL_BRIDGE = NOT_APPLICABLE_IN_THIS_SCREEN
```

No scalar score is allowed.

## Doctrine-shell completeness test

A doctrine shell is not yet a complete PGH candidate grammar if substantive content remains freely parameterized by:

```text
ARBITRARY_OBJECT_GENERATORS
ARBITRARY_MORPHISM_GENERATORS
ARBITRARY_RELATIONS_OR_EQUATIONS
ARBITRARY_TYPES
ARBITRARY_RESPONSE_OR_EMPIRICAL_RULES
```

Two controls must both be tested:

### U1 — unrestricted presentation control

If arbitrary theory-specific generators or relations may be added, can the shell host arbitrary target-directed content while retaining the same doctrine?

If yes, doctrine alone does not solve the universal-encoding problem.

### U2 — empty/nonstructural-generator-free control

If all nonstructural generators are forbidden, does the doctrine still contain enough fixed structure to define a nontrivial grammar connected to the law-free anchor, or is it merely an abstract structural shell?

## Anchor-seed possibility

The screen may recommend—but not execute—a future construction in which the same law-free `A_ref` tokens provide a fixed neutral seed and multiple doctrines freely generate structure from that identical seed.

Such a future operation must use the **same seed across competing doctrines** and may not add target-specific response laws.

## Outcome space

```text
A = AT_LEAST_ONE_DOCTRINE_ALONE_PASSES_PGH_OBJ_0020_AS_A_COMPLETE_NONTRIVIAL_PRIMITIVE_GRAMMAR_CANDIDATE_WITHOUT_UNEARNED_SEED_OR_PRESENTATION_DATA
B = ALL_TESTED_DOCTRINES_FAIL_THE_FORMAL_ADMISSIBILITY_STANDARD_EVEN_AS_STRUCTURAL_SHELLS
C = ONE_OR_MORE_DOCTRINES_PASS_AS_NONTRIVIAL_STRUCTURAL_GRAMMAR_SHELLS_BUT_NONE_IS_A_COMPLETE_PGH_CANDIDATE_GRAMMAR_WITHOUT_A_FIXED_NON_TARGET_DIRECTED_SEED__ANCHOR_SEEDED_FREE_DOCTRINE_CONSTRUCTION_IS_JUSTIFIED
D = CURRENT_FORMAL_BASELINE_IS_INSUFFICIENT_TO_CLASSIFY_THE_FAMILY
```

Outcome C creates no `PGH-GRAM-*` successor IDs.

## Required outputs

Commit 2 may add only:

```text
audits/PGH1_R2_PRIMITIVE_GRAMMAR_CANDIDATE_FAMILY_SCREEN_0_1_0.md
research/formalizations/PGH1_PRIMITIVE_GRAMMAR_DOCTRINE_FAMILY_SCREEN_0_1_0.md
research/failures/PGH_FAIL_DOCTRINE_ONLY_GRAMMAR_SHELL_COMPLETENESS_0_1_0.md
handoffs/PGH1_R2_PRIMITIVE_GRAMMAR_CANDIDATE_FAMILY_SCREEN_HANDOFF_0_1_0.md
```

## Commit topology

```text
COMMIT_1_MESSAGE = Preregister PGH-1 R2 primitive grammar candidate family screen
COMMIT_2_MESSAGE = Screen PGH-1 R2 primitive grammar candidate family
EXACT_COMMITS = 2
```

## Hard stops

```text
DO_NOT_ASSIGN_PGH_GRAM_IDS_UNLESS_OUTCOME_A
DO_NOT_USE_KNOWN_PHYSICS_TO_RANK_DOCTRINES
DO_NOT_ADD_TARGET_SPECIFIC_GENERATORS
DO_NOT_BEGIN_PHYSICAL_BRIDGE
DO_NOT_SEARCH_NEW_SOURCES
DO_NOT_CHANGE_FCP
```
