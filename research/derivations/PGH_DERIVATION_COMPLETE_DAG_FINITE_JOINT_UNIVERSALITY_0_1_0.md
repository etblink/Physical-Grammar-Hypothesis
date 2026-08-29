# PGH-DER-0030 — Complete DAG Finite Joint Universality

## Status

```text
DERIVATION_ID = PGH-DER-0030
STATUS = QUALIFIED_FORMAL
PHYSICAL_CLAIM = NONE
```

## Setup

Let finite random variables `A,B,C` have arbitrary joint distribution `p(a,b,c)`.

Consider the complete ordered DAG

\[
A\to B,\qquad A\to C,\qquad B\to C.
\]

Its factorization class is

\[
p(a,b,c)=p(a)p(b\mid a)p(c\mid a,b).
\]

## Claim

Every finite joint distribution admits such a factorization.

## Construction

Define the marginal

\[
p(a)=\sum_{b,c}p(a,b,c).
\]

For `p(a)>0`, define

\[
p(b\mid a)=\frac{p(a,b)}{p(a)}.
\]

For `p(a,b)>0`, define

\[
p(c\mid a,b)=\frac{p(a,b,c)}{p(a,b)}.
\]

On any zero-probability parent configuration, choose arbitrary normalized conditional values. Those terms are multiplied by zero and do not alter the joint distribution.

Then in every case,

\[
p(a)p(b\mid a)p(c\mid a,b)=p(a,b,c).
\]

Therefore the complete ordered DAG represents every finite joint distribution on the fixed alphabets.

## Consequence

At finite joint-distribution scope,

```text
COMPLETE_DAG_MODEL_CLASS = ALL_FINITE_JOINT_DISTRIBUTIONS
```

so complete wiring supplies no proper response restriction at this scope.

Combined with `PGH-DER-0029`, this localizes the selectivity of sparse causal-factorization models in the graph/wiring structure rather than the mere use of DAG factorization.

## Scope

No physical interpretation of the graph is asserted.
