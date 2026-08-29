# PGH-GRAM-0008 — Three-Node Sparse Markov Chain Primitive Grammar Candidate 0.1.0

## Status

```text
GRAMMAR_ID = PGH-GRAM-0008
STATUS = FORMAL_PRIMITIVE_GRAMMAR_CANDIDATE
PHYSICAL_STATUS = NONE
R2B_STATUS = UNSATISFIED
```

## Primitive structure

The grammar has three formal variable roles

\[
A,B,C
\]

with arbitrary nonempty finite alphabets and fixed directed wiring

\[
A\to B\to C.
\]

Its admissible models are normalized finite joint distributions satisfying

\[
\boxed{p(a,b,c)=p(a)p(b\mid a)p(c\mid b)}.
\]

The local kernels

\[
p(a),\qquad p(b\mid a),\qquad p(c\mid b)
\]

remain arbitrary normalized model data.

## Well-formed model class

\[
W(PGH\text{-}GRAM\text{-}0008)
=
\{p:\ p\text{ is a finite normalized joint model factorizing over }A\to B\to C\}.
\]

No empirical variable assignment is part of `W(G)`.

## Derived formal consequence

Every model satisfies

\[
A\perp C\mid B
\]

by `PGH-DER-0029`.

Thus the grammar excludes some finite joint distributions without specifying local numerical kernels.

## Exclusion witness

The preregistered distribution with independent fair `A,B` and `C=A` is not a model of the grammar.

The witness is a countermodel, not grammar content.

## Universal-control comparison

`PGH-DER-0030` establishes that the complete ordered DAG on the same node set represents all finite joint distributions.

Thus selectivity is attributable to the fixed sparse wiring.

## Representation discipline

Isomorphic renaming of variable roles and alphabets transports the candidate and its model class.

A directed graph is not required to be invariant under every permutation of its node set.

## Semantic boundary

```text
A_B_C_AS_PHYSICAL_VARIABLES = NOT_ASSIGNED
ARROWS_AS_PHYSICAL_CAUSES = NOT_ASSIGNED
PROBABILITY_AS_PHYSICAL_CHANCE = NOT_ASSIGNED
EMPIRICAL_FIT = NONE
```

A later semantic gate must create separate provenance for any physical interpretation.

## Novelty discipline

The Markov-chain factorization and conditional-independence consequence are established probabilistic graphical-model machinery.

```text
MATHEMATICAL_NOVELTY_CLAIM = NONE
```

The PGH-specific use is experimental: this is a compact primitive grammar candidate that passes the project's anti-table candidacy standard and possesses direct response-model exclusion power.

## Claim ceiling

```text
FORMAL_GRAMMAR_CANDIDATE = YES
PHYSICAL_GRAMMAR = NO
PHYSICAL_LAW_DERIVED = NO
R2B = UNSATISFIED
EMPIRICAL_PREDICTION = NONE
```
