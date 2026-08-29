# PGH-0 Prior-Art Overlap and Residual Novelty Adjudication — Preregistration 0.1.0

## Status

```text
OPERATION_ID = PGH0_PRIOR_ART_OVERLAP_AND_RESIDUAL_NOVELTY_ADJUDICATION
REGISTRY_ID = PGH-OP-0011
OPERATION_CLASS = SOURCE_BOUND_PRIOR_ART_ADJUDICATION
STATUS = PREREGISTERED_IN_PROGRESS
CANONICAL_BASE = afea41f9a68f923533747493bcec853887bc4abc
WORKING_BRANCH = research/pgh0-prior-art-residual-novelty-adjudication
FROZEN_SOURCE_COUNT = 37
NEW_SOURCE_SEARCH = FORBIDDEN
PGH_GRAMMAR_CHANGE = FORBIDDEN
PHYSICAL_BRIDGE = FORBIDDEN
EMPIRICAL_ADJUDICATION = FORBIDDEN
FCP_EFFECT = NONE
NOVELTY_CLAIM_AUTHORIZED = NO
```

## Purpose

The source landscape established extensive prior-art neighborhoods for the mathematical machinery and foundational ideas used by PGH. This operation performs explicit prior-art subtraction.

The controlling question is:

> After removing claims already supplied, substantially anticipated, or rendered mathematically routine by the frozen 37-source landscape, what scientifically meaningful PGH research burden, if any, remains?

This is not a patent-style novelty determination and not a claim of historical priority. It is an internal scientific sequencing adjudication.

## Frozen inputs

Use only:

```text
sources/PGH0_REPRESENTATION_COHERENCE_SOURCE_REGISTER_0_1_0.md
sources/PGH0_REPRESENTATION_COHERENCE_SOURCE_LANDSCAPE_0_1_0.md
sources/PGH0_REPRESENTATION_COHERENCE_SOURCE_SELECTION_AUDIT_0_1_0.md
HYPOTHESIS.md
research/formalizations/PGH0_REPRESENTATION_EQUIVALENCE_COHERENCE_ADJUDICATION_0_1_0.md
research/derivations/PGH_DERIVATION_CONTEXTUAL_EXTENSIONAL_REDUCTION_0_1_0.md
research/derivations/PGH_DERIVATION_ISOMORPHISM_COVARIANCE_UNDERDETERMINATION_0_1_0.md
research/derivations/PGH_DERIVATION_PARSE_COHERENCE_ASSOCIATIVITY_0_1_0.md
research/derivations/PGH_DERIVATION_PRESENTATION_PROJECTION_FACTORIZATION_0_1_0.md
research/derivations/PGH_DERIVATION_COHERENCE_MONOTONICITY_UNDER_FORGETTING_0_1_0.md
research/failures/PGH_FAIL_BARE_FORMATION_GRAMMAR_PHYSICAL_SUFFICIENCY_0_1_0.md
research/failures/PGH_FAIL_STRONG_PERMUTATION_INVARIANCE_AS_LABEL_NEUTRALITY_0_1_0.md
research/failures/PGH_FAIL_UNPRIVILEGED_SIMPLICITY_SELECTION_0_1_0.md
research/failures/PGH_FAIL_UNIQUE_PROJECTION_FROM_REPRESENTATION_INVARIANCE_0_1_0.md
```

No source expansion is permitted in this operation.

## Subtraction rule

An apparent PGH contribution does not survive merely because the exact phrase “Physical Grammar Hypothesis” or the exact current conjunction was not found.

For each object, classify the strongest supported status:

```text
ESTABLISHED_PRIOR_ART_FAMILY
LOCAL_REFORMULATION_OR_SPECIALIZATION
PROJECT_SPECIFIC_CONTROL_WITHOUT_NOVELTY_WEIGHT
KNOWN_FOUNDATIONAL_NEIGHBORHOOD
RESIDUAL_RESEARCH_BURDEN
UNRESOLVED_AGAINST_FROZEN_SCOPE
```

The adjudication must choose the **strongest subtraction justified by the frozen corpus**.

## Objects requiring explicit adjudication

At minimum:

```text
PGH-W
PGH-S
PGH-I
PGH-DER-0001
PGH-DER-0002
PGH-DER-0003
PGH-DER-0004
PGH-DER-0005
PGH-FAIL-0001
PGH-FAIL-0002
PGH-FAIL-0003
PGH-FAIL-0004
PGH-Q-0008
PGH-Q-0014
PGH-Q-0015
PGH-Q-0016
```

## Neighbor subtraction tests for strong PGH

Strong PGH must be compared conjunct-by-conjunct against the frozen nearby families:

1. formal generative grammar;
2. universal algebra / quotient and algebraic-theory machinery;
3. rewriting and coherence;
4. structural realism / mathematical structuralism;
5. categorical/process physics;
6. operational/informational reconstruction;
7. constructor theory;
8. laws as constraints;
9. theoretical equivalence / duality;
10. Mathematical Universe Hypothesis.

The adjudication must distinguish:

```text
COMPONENT_ALREADY_KNOWN
COMBINATION_ONLY
RESEARCH_BURDEN_NOT_DISCHARGED
```

A combination not found verbatim is not thereby novel.

## Residual-burden test

A residual burden may survive only if:

1. it is needed for strong PGH to differ substantively from the live null;
2. the frozen literature supplies multiple candidate mechanisms or neighboring theses but does not discharge the burden itself;
3. it can be stated more precisely than “find the right grammar”;
4. success and failure conditions can be specified;
5. it is not simply a renamed standard theorem or mathematical formalism.

## Candidate residual axes

The operation must test, without preaccepting, at least these two candidate burdens:

### R1 — Physical irrelevance selector

Can a non-result-directed physical criterion determine which distinctions between mathematically adequate presentations are physically representational rather than physically real?

### R2 — Law exhaustion

Can all substantive physical selection be carried by grammatical well-formedness/coherence after the representation quotient, leaving no independent physical law set `L` to perform residual selection?

These are candidate burdens, not established PGH contributions.

## Required downgrade tests

### Weak PGH

Determine whether `PGH-W` is too broad to retain as a scientifically discriminating hypothesis after categorical/process, formal-language, and reconstruction prior art.

### Linguistic–Physical Identity Hypothesis

Determine whether `PGH-I` is sufficiently operationalized to remain an active research target at this stage, or should remain quarantined as a speculative extension.

### Strong PGH

Determine whether the broad current wording should remain live unchanged, be narrowed to a residual conjecture, or be downgraded because its substantive content is already absorbed by neighbors.

## Outcome space

```text
A = NO_MEANINGFUL_RESIDUAL_PGH_BURDEN_SURVIVES_SUBTRACTION
B = A_NARROW_RESIDUAL_RESEARCH_BURDEN_SURVIVES_WITHOUT_NOVELTY_CLAIM
C = MULTIPLE_INDEPENDENT_RESIDUAL_BURDENS_SURVIVE_AND_REQUIRE_EXPLICIT_SPLIT
D = STRONG_PGH_IS_SUBSTANTIALLY_ABSORBED_BUT_AN_UNRESOLVED_COMBINATION_REMAINS_TOO_VAGUE_TO_ADVANCE
E = FROZEN_LANDSCAPE_INSUFFICIENT_FOR_RESIDUAL_ADJUDICATION
```

No outcome is a ranking.

## Required outputs

Commit 2 may add only:

```text
audits/PGH0_PRIOR_ART_OVERLAP_AND_RESIDUAL_NOVELTY_ADJUDICATION_0_1_0.md
research/formalizations/PGH0_RESIDUAL_STRONG_PGH_SPECIFICATION_0_1_0.md   # only if a precise residual survives
handoffs/PGH0_PRIOR_ART_OVERLAP_AND_RESIDUAL_NOVELTY_ADJUDICATION_HANDOFF_0_1_0.md
```

Do not update mutable current state or registries on the scientific branch. That is a later reconciliation operation after acceptance/integration.

## Commit boundary

Use exactly two commits:

```text
COMMIT_1_MESSAGE = Preregister PGH-0 prior-art residual adjudication
COMMIT_2_MESSAGE = Adjudicate PGH-0 prior-art residual
```

Commit 1 contains only this preregistration.

## Hard stops

Stop before:

- claiming PGH is historically or mathematically novel;
- beginning new source search;
- selecting a physical grammar;
- choosing category theory, operads, constructor theory, or any other formalism as PGH ontology;
- deriving physical law;
- empirical work;
- changing FCP;
- beginning the next scientific operation;
- mutating canonical `main` before independent review.
