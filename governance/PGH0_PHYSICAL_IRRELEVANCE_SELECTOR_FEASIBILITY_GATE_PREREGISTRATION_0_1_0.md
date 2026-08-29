# PGH-0 Physical Irrelevance Selector Feasibility Gate — Preregistration 0.1.0

## Status

```text
OPERATION_ID = PGH0_PHYSICAL_IRRELEVANCE_SELECTOR_FEASIBILITY_GATE
REGISTRY_ID = PGH-OP-0013
OPERATION_CLASS = SOURCE_BOUND_FOUNDATIONAL_FEASIBILITY_GATE
STATUS = PREREGISTERED_IN_PROGRESS
CANONICAL_BASE = a3b80ffab9f2d6a07ba11f1107e65f926104b893
WORKING_BRANCH = research/pgh0-physical-irrelevance-selector-feasibility
FROZEN_SOURCE_COUNT = 37
NEW_SOURCE_SEARCH = FORBIDDEN_UNLESS_GATE_EXPOSES_SPECIFIC_GAP
PHYSICAL_GRAMMAR_SELECTION = FORBIDDEN
EMPIRICAL_ADJUDICATION = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

This gate tests residual burden R1 from `PGH-OBJ-0008`:

> Can any currently available, frozen-corpus notion of equivalence or translation select which differences between mathematically adequate presentations are physically representational rather than physically real, without choosing the result by hand or importing the target physical law?

The gate is not allowed to rescue R1 by combining criteria ad hoc after seeing which physical laws they produce.

## Frozen inputs

Use the exact canonical prior-art and residual artifacts only:

```text
research/formalizations/PGH0_RESIDUAL_STRONG_PGH_SPECIFICATION_0_1_0.md
audits/PGH0_PRIOR_ART_OVERLAP_AND_RESIDUAL_NOVELTY_ADJUDICATION_0_1_0.md
sources/PGH0_REPRESENTATION_COHERENCE_SOURCE_REGISTER_0_1_0.md
sources/PGH0_REPRESENTATION_COHERENCE_SOURCE_LANDSCAPE_0_1_0.md
sources/PGH0_REPRESENTATION_COHERENCE_SOURCE_SELECTION_AUDIT_0_1_0.md
research/derivations/PGH_DERIVATION_PRESENTATION_PROJECTION_FACTORIZATION_0_1_0.md
research/derivations/PGH_DERIVATION_COHERENCE_MONOTONICITY_UNDER_FORGETTING_0_1_0.md
research/failures/PGH_FAIL_UNIQUE_PROJECTION_FROM_REPRESENTATION_INVARIANCE_0_1_0.md
```

## R1 acceptance criteria

A candidate selector family passes only if it satisfies all of:

```text
R1A_NON_RESULT_DIRECTED
R1B_REPRESENTATION_ROBUST
R1C_DISCRIMINATES_COMPETING_EQUIVALENCES
R1D_NOT_DEFINED_AS_WHATEVER_PRESERVES_TARGET_PHYSICS
R1E_NO_HIDDEN_PHYSICAL_LAW
R1F_APPLICABLE_BEFORE_A_FULL_PHYSICAL_THEORY_IS_ALREADY_FIXED
```

Partial satisfaction does not count as R1 success.

## Frozen candidate families

Test in this order.

### S1 — Definitional / syntactic equivalence

Question: Can interdefinability or syntactic translation determine physical irrelevance without privileging one formal language?

Primary frozen controls: `PGH-LS-SRC-017,018,019`.

### S2 — Categorical equivalence

Question: Does equivalence of appropriately constructed model categories identify physical sameness without moving the substantive choice into objects/morphisms/category construction?

Primary frozen controls: `PGH-LS-SRC-016,018,019` plus category/structural sources.

### S3 — Morita equivalence

Question: Does preservation under definitional extensions/sorts provide a physically privileged criterion rather than a stronger formal equivalence notion?

Primary frozen control: `PGH-LS-SRC-017`.

### S4 — Duality / common-core equivalence

Question: Can isomorphic common cores or dual formulations select physical irrelevance without presupposing which structure belongs in the common core?

Primary frozen control: `PGH-LS-SRC-020` and theory-equivalence sources.

### S5 — Structural / isomorphic / univalent equivalence

Question: Does identity up to isomorphism/equivalence decide physical irrelevance, or only once the physically relevant structure has already been chosen?

Primary frozen controls: `PGH-LS-SRC-021,022,023,030,031,032`.

### S6 — Operational / empirical equivalence

Question: Can agreement on observations/operations provide the physical selector without defining the relevant observables/operations using the very physics under explanation?

Primary frozen controls: `PGH-LS-SRC-024,025,026,027,036` together with `SRC-016,018,019`.

### S7 — Task / possibility equivalence

Question: Can agreement on possible/impossible transformations serve as the selector without simply importing the target possibility law as the equivalence criterion?

Primary frozen controls: `PGH-LS-SRC-033,034`.

## Formal underdetermination test

Independently of the seven literature families, test the following generic proposition.

Let `P` be a presentation space and `E` a nontrivial formal equivalence relation on `P`. Let a physical-realization or physical-significance map be any map

\[
\sigma:P\to S.
\]

Absent an independent restriction on admissible `sigma`, determine whether formal facts about `E` alone can entail

\[
p E p' \Longrightarrow \sigma(p)=\sigma(p').
\]

Required finite witness: for some `p E p'` with `p != p'`, exhibit both:

1. a `sigma_same` that assigns the pair the same physical-significance value;
2. a `sigma_split` that assigns the pair different values.

If both are admissible at purely formal scope, then `E` alone does not entail physical equivalence.

This theorem, if established, is formal only and carries no novelty claim.

## Semantic-anchor distinction

If no purely formal selector passes, distinguish:

```text
R1_IMPOSSIBLE
```

from

```text
R1_REQUIRES_MINIMAL_PHYSICAL_SEMANTIC_ANCHOR
```

The latter means some physical interpretation must enter to determine which formal differences matter, while PGH still has the burden of keeping that semantic anchor too weak to contain the substantive laws being explained.

Do not equate “semantics is needed” with “PGH is false.”

## Outcome space

```text
A = ONE_FROZEN_EQUIVALENCE_FAMILY_PASSES_R1
B = A_PREREGISTERED_NON_AD_HOC_COMBINATION_PASSES_R1
C = NO_FROZEN_FORMAL_SELECTOR_PASSES_AND_R1_REQUIRES_A_MINIMAL_PHYSICAL_SEMANTIC_ANCHOR
D = R1_IS_INCOMPATIBLE_WITH_PGH_NO_SMUGGLING_AT_CURRENT_SCOPE
E = FROZEN_CORPUS_INSUFFICIENT_AND_A_SPECIFIC_SOURCE_GAP_IS_IDENTIFIED
F = UNRESOLVED
```

No outcome is a ranking.

## Required outputs

Commit 2 may add only:

```text
audits/PGH0_PHYSICAL_IRRELEVANCE_SELECTOR_FEASIBILITY_GATE_0_1_0.md
research/derivations/PGH_DERIVATION_FORMAL_EQUIVALENCE_PHYSICAL_UNDERDETERMINATION_0_1_0.md   # if established
research/failures/PGH_FAIL_FROZEN_EQUIVALENCE_FAMILIES_AS_PHYSICAL_SELECTOR_0_1_0.md       # if warranted
handoffs/PGH0_PHYSICAL_IRRELEVANCE_SELECTOR_FEASIBILITY_GATE_HANDOFF_0_1_0.md
```

Do not update mutable registries/current state on the scientific branch.

## Commit boundary

```text
COMMIT_1_MESSAGE = Preregister PGH-0 physical irrelevance selector gate
COMMIT_2_MESSAGE = Adjudicate PGH-0 physical irrelevance selector gate
```

Exactly two commits are permitted for the scientific candidate.

## Hard stops

Stop before:

- inventing a new physical law;
- selecting a physical grammar;
- claiming an equivalence family is physically privileged because it reproduces known physics;
- carrying out empirical analysis;
- expanding the source corpus without first identifying a specific gate-blocking gap;
- beginning R2 law exhaustion;
- changing FCP;
- mutating canonical `main` before review.
