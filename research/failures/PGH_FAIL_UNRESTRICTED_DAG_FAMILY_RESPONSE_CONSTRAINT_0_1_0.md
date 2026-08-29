# PGH-FAIL-0031 — Unrestricted DAG Family Response Constraint

## Status

```text
FAILURE_ID = PGH-FAIL-0031
STATUS = FAILED_PRESERVED
FAILURE_CLASS = FAMILY_LEVEL_NONSELECTION
PHYSICAL_CLAIM = NONE
```

## Failed claim

> Because some DAGs impose nontrivial conditional-independence restrictions, the unrestricted family of DAG-based response models is itself response-selective.

## Why the claim fails

`PGH-DER-0029` shows that a fixed sparse chain can exclude distributions.

`PGH-DER-0030` shows that the complete ordered DAG on the same finite variables represents every joint distribution by the chain rule.

Therefore a family that leaves the graph unrestricted and includes the complete DAG recovers universal finite joint-distribution representability.

```text
SELECTIVITY_OF_SPARSE_MEMBER != SELECTIVITY_OF_UNRESTRICTED_FAMILY
```

The graph/wiring must be bound as candidate content if its restrictions are to receive explanatory credit.

## What this does not imply

The failure does not prohibit a fixed graph from entering primitive grammar candidacy.

A graph may be an explicit primitive hypothesis under `PGH-OBJ-0020` if it is preregistered, compact, non-extensional, exclusionary, representation-disciplined, and exposed to countermodels.

The failure prohibits only hiding graph choice behind a broad family label and then crediting the family with restrictions produced by selected members.

## Claim ceiling

```text
FIXED_SPARSE_DAG_CAN_CONSTRAIN = YES_FORMAL
UNRESTRICTED_DAG_FAMILY_CONSTRAINS_ALL_FINITE_JOINTS = NO
PHYSICAL_GRAPH_SELECTED = NO
R2B = UNSATISFIED
```
