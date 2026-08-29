# PGH-FAIL-0030 — Structural Process Constraint Input Relocation

## Status

```text
FAILURE_ID = PGH-FAIL-0030
STATUS = FAILED_PRESERVED
FAILURE_CLASS = SELECTIVE_INPUT_RELOCATION
PHYSICAL_CLAIM = NONE
```

## Failed claim

> A compositional stochastic or causal framework constrains response models purely by virtue of being structural, so its graph, wiring, topology, source-independence assumptions, or generating signature may be treated as neutral background.

## Why the claim fails

The frozen SG4 corpus separates at least four information layers:

```text
D = doctrine/process calculus
W = graph/wiring/topology/signature
K = local channels/kernels/boxes
E = empirical response parameters
```

Nontrivial model-class restrictions can depend materially on `W` even when `K` remains free.

For example, sparse causal graphs can entail conditional-independence consequences that a more connected graph does not entail. Network/source-independence results likewise depend on topology and independence structure.

Therefore moving the target-selective information from a response table into an unexamined graph or topology does not constitute PGH law derivation.

## What remains valid

The failure does **not** say that graph/wiring inputs are forbidden primitives.

Under `PGH-OBJ-0020`, a primitive structural package may enter formal candidacy if it is explicitly declared, fixed before target evaluation, non-extensional, counterexample-exposing, and subjected to the anti-smuggling suite.

The required correction is provenance and explanatory accounting:

```text
IF_W_DOES_SELECTIVE_WORK
THEN_W_MUST_BE_PART_OF_THE_CANDIDATE_IDENTITY
```

not silently treated as semantics.

## Positive consequence

A graph-parametric formal gate is scientifically useful because it can isolate exactly how much exclusion comes from `W` while keeping local kernels free.

## Claim ceiling

```text
CAUSAL_OR_NETWORK_STRUCTURE_CAN_CONSTRAIN_MODELS = YES_SOURCE_BOUND
SELECTIVE_STRUCTURE_IS_NEUTRAL_BACKGROUND = NO
PHYSICAL_CAUSAL_STRUCTURE_SELECTED = NO
R2B = UNSATISFIED
```
