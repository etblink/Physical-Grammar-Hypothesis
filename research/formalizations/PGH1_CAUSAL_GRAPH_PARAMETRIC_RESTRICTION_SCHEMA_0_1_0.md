# PGH-OBJ-0033 — Causal Graph Parametric Restriction Schema 0.1.0

## Status

```text
OBJECT_ID = PGH-OBJ-0033
STATUS = QUALIFIED_FORMALIZATION
PHYSICAL_STATUS = NONE
```

## Purpose

This object records the minimal graph-parametric mechanism by which fixed directed wiring can restrict a finite joint-distribution model class while local conditional kernels remain free.

## Fixed comparison

```text
VARIABLES = A;B;C
ALPHABETS = BINARY
SPARSE_GRAPH = A->B->C
COMPLETE_GRAPH = A->B;A->C;B->C
```

The graphs are mathematical controls, not physical causal hypotheses.

## Sparse factorization

\[
p(a,b,c)=p(a)p(b\mid a)p(c\mid b)
\]

implies

\[
A\perp C\mid B.
\]

Thus sparse wiring yields a proper model subclass.

## Complete factorization

\[
p(a,b,c)=p(a)p(b\mid a)p(c\mid a,b)
\]

represents every finite joint distribution by the chain rule.

## Information accounting

```text
GRAPH_WIRING = SELECTIVE_STRUCTURAL_INPUT
LOCAL_KERNEL_VALUES = FREE_MODEL_DATA
EMPIRICAL_PARAMETER_VALUES = ABSENT
```

The schema therefore isolates a valid form of non-table-driven model-class exclusion.

## Candidate-family warning

A parameterized family containing every DAG must not inherit the exclusions of its sparse members at family scope.

If a complete DAG is admitted, arbitrary finite dependency structure is representable.

Therefore a later grammar candidate must bind its wiring structure explicitly.

## Representation discipline

Variable renaming transports both the graph and factorization conditions covariantly.

No full-automorphy requirement is imposed on a directed graph.

## Claim ceiling

```text
FORMAL_SELECTIVITY_FROM_FIXED_WIRING = YES
PHYSICAL_CAUSATION = NONE
PHYSICAL_GRAPH_SELECTION = NONE
R2B = UNSATISFIED
```
