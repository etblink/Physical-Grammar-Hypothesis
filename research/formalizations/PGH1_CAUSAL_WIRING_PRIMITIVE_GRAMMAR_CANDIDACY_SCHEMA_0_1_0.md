# PGH-OBJ-0034 — Causal Wiring Primitive Grammar Candidacy Schema 0.1.0

## Status

```text
OBJECT_ID = PGH-OBJ-0034
STATUS = QUALIFIED_FORMALIZATION
PHYSICAL_STATUS = NONE
```

## Purpose

This object records how fixed probabilistic wiring may enter PGH formal grammar candidacy without treating graph choice, local kernel values, or physical interpretation as invisible background.

## Candidate-content rule

If graph/wiring structure does selective work, then it belongs to the candidate grammar identity.

```text
SELECTIVE_WIRING -> CANDIDATE_CONTENT
LOCAL_NUMERICAL_KERNELS -> MODEL_DATA
EMPIRICAL_PARAMETER_VALUES -> NOT_CANDIDATE_CONTENT
```

## Candidacy example

`PGH-GRAM-0008` fixes the chain

\[
A\to B\to C
\]

and the corresponding finite Markov factorization while leaving local kernels free.

The model class is proper because `PGH-DER-0029` gives a conditional-independence theorem and an explicit excluded counterdistribution.

## Null-control principle

The complete ordered DAG on the same variables is universal at finite joint-distribution scope by `PGH-DER-0030`.

Therefore one may not attribute the sparse candidate's exclusion merely to:

```text
PROBABILITY
DAG_NOTATION
FACTORISATION_IN_GENERAL
```

The fixed sparse wiring is the selective part.

## Stopping rule

No meta-derivation of the graph is required for **formal candidacy**.

The graph may be a primitive hypothesis under `PGH-OBJ-0020` if it is:

- explicit;
- pre-target;
- compact/non-extensional;
- exclusionary;
- representation-disciplined;
- counterexample-exposing.

This does not grant physical status.

## Physical firewall

A later operation must separately justify any reading of:

```text
VARIABLE = EMPIRICAL_QUANTITY
ARROW = PHYSICAL_CAUSAL_OR_DEPENDENCY_RELATION
PROBABILITY = PHYSICAL_CHANCE_OR_FREQUENCY
```

and may not select the graph because observed data already fit its conditional independences.

## Claim ceiling

```text
FORMAL_CAUSAL_WIRING_GRAMMAR_CANDIDACY = COHERENT
PHYSICAL_CAUSATION = UNESTABLISHED
PHYSICAL_LAW = UNESTABLISHED
R2B = UNSATISFIED
```
