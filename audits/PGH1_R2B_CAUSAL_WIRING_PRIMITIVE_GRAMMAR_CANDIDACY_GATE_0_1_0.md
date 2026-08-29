# PGH-1 R2B Causal Wiring Primitive Grammar Candidacy Gate 0.1.0

## Identity

```text
OPERATION_ID = PGH1_R2B_CAUSAL_WIRING_PRIMITIVE_GRAMMAR_CANDIDACY_GATE
REGISTRY_ID = PGH-OP-0060
CANONICAL_BASE = b5107f219879c11f117ca1278a46a22fa150bf51
PREREGISTRATION_COMMIT = 03e20180a54ae13a0b1b9b4216dc815b7b35af6f
PRIMITIVE_GRAMMAR_STANDARD = PGH-OBJ-0020
FROZEN_SOURCE_CORPUS = 85_DISTINCT_ACCEPTED
NEW_SOURCE_SEARCH = NONE
EMPIRICAL_DATA = NONE
FCP_EFFECT = NONE
```

## Outcome

```text
OUTCOME = A__PGH_GRAM_0008_PASSES_FORMAL_PRIMITIVE_GRAMMAR_CANDIDACY_UNDER_PGH_OBJ_0020__ITS_FIXED_SPARSE_WIRING_GENERATES_NONTRIVIAL_MODEL_CLASS_EXCLUSION_WITH_FREE_LOCAL_KERNELS__NO_PHYSICAL_STATUS_OR_R2B_CREDIT_FOLLOWS
FORMAL_GRAMMAR_CANDIDATE = YES
PHYSICAL_GRAMMAR = NO
R2B = UNSATISFIED
PHYSICAL_LAW_DERIVED = NO
EMPIRICAL_PREDICTION = NONE
```

## Qualified candidate

```text
PGH-GRAM-0008 = THREE_NODE_SPARSE_MARKOV_CHAIN_PRIMITIVE_GRAMMAR_CANDIDATE
```

Its admissible models are finite normalized joint distributions over three formal variable roles satisfying

\[
p(a,b,c)=p(a)p(b\mid a)p(c\mid b).
\]

The local kernels remain free normalized model data.

No numerical response table is part of the candidate.

## P0 — formal definability

```text
PASS
```

The model class is exact and mathematically standard.

## P1 — declared primitives

```text
PASS
```

The candidate explicitly contains:

- three formal variable roles;
- fixed sparse directed wiring `A->B->C`;
- normalized finite probability models;
- the associated Markov factorization rule.

Nothing selective is hidden in a later model functor or semantic map at this gate.

## P2 — pre-target fixation

```text
PASS_AT_CURRENT_SCOPE
```

The sparse chain was frozen as the minimal graph-parametric witness before any empirical-fit operation and before any physical variable assignment.

Its current candidate admission uses no empirical response data.

This does not imply that a later physical application may choose the graph after inspecting target data.

## P3 — restricted hypothesis class / universal encoding

```text
PASS
```

`PGH-DER-0029` plus the preregistered counterdistribution proves that the candidate fails to represent at least one finite joint distribution.

Therefore it is not a universal finite response-table encoder at this scope.

The complete-DAG control `PGH-DER-0030` demonstrates what universality would look like in the same probabilistic language.

## P4 — no extensional target table

```text
PASS
```

The grammar does not enumerate allowed triples or specify numerical probabilities case by case.

One fixed graph/factorization rule defines the class.

## P5 — generative compression

```text
PASS_FORMAL
```

The candidate compactly specifies an infinite continuum of joint distributions through arbitrary normalized local kernels while excluding distributions that violate the chain Markov condition.

## P6 — nontrivial formal exclusion

```text
PASS
```

The derived theorem

\[
A\perp C\mid B
\]

excludes the locked distribution with independent fair `A,B` and `C=A`.

## P7 — representation discipline

```text
PASS_AT_FORMAL_SCOPE
```

Consistent relabeling of variables, alphabets, graph incidence, and probability arguments transports the candidate covariantly.

Full permutation automorphy of one directed graph is not required.

## P8 — semantic-load boundary

```text
PASS_PRE_PHYSICAL
```

No claim is made that the variables are empirical observables, that arrows are physical causes, or that numerical probabilities are physical frequencies/chances.

That hard stop is preserved as:

```text
PGH-FAIL-0032 = CAUSAL_WIRING_PHYSICAL_SEMANTICS_PREMATURE
```

## P9 — independent formal consequence

```text
PASS
```

The fixed wiring/factorization generates conditional-independence structure across every model of the candidate.

The result is standard probabilistic graphical-model mathematics; no novelty claim is authorized.

The relevant PGH fact is only that the candidate has a real model-class consequence not supplied by fitted local kernel values.

## P10 — counterexample exposure

```text
PASS
```

Two controls are explicit:

1. an excluded finite joint distribution;
2. the complete-DAG model class that restores universal finite-joint representability.

## P11 — physical bridge

```text
NOT_QUALIFIED
```

Formal candidacy does not assign any physical meaning to the graph or factorization.

## Why outcome D does not pass

The candidate's rule is highly compressive relative to an extensional support/probability table and leaves all local conditional values free.

It is not information-equivalent to specifying one target joint distribution.

However, the chain factorization and conditional-independence law are standard equivalent descriptions of the same graphical-model restriction. This gate claims formal grammar candidacy, not deeper explanatory reduction or mathematical novelty.

## Why the complete-DAG control is not promoted

The complete-DAG control is mathematically legitimate but has no response-selective power at finite joint-distribution scope because it represents every joint distribution.

This gate does not need to assign it a new `PGH-GRAM-*` identity.

## Scientific consequence

PGH now has at least one formal primitive grammar candidate whose fixed structural content directly removes response models while leaving local response parameters free.

That is stronger than the earlier monoidal/categorical doctrine candidates at the exact R2B model-class restriction task.

It is still entirely pre-physical.

## Next scientific operation

Recommended:

```text
PGH1_R2B_CAUSAL_WIRING_PHYSICAL_SEMANTIC_FIREWALL_GATE
```

Purpose:

- test possible physical/empirical semantic readings of `PGH-GRAM-0008` without selecting a graph from data;
- distinguish mere probabilistic factorization bookkeeping from a substantive dependency/causal interpretation;
- determine whether any semantic reading makes the graph's derived conditional independence a genuine candidate physical law without importing that law through the interpretation itself;
- stop before empirical fitting unless a noncircular semantic bridge survives.

## Hard-stop verification

```text
NEW_SOURCE_SEARCH = NO
EMPIRICAL_DATA_USED = NO
ARROWS_CALLED_PHYSICAL_CAUSES = NO
VARIABLES_CALLED_EMPIRICAL_OBSERVABLES = NO
LOCAL_KERNEL_VALUES_FIXED = NO
PRESENT_GRAMMARS_MODIFIED = NO
PHYSICAL_GRAMMAR_FOUND = NO
R2B_SATISFIED = NO
PHYSICAL_LAW_DERIVED = NO
EMPIRICAL_PREDICTION = NONE
FCP_CHANGED = NO
```
