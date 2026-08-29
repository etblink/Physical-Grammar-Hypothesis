# PGH-DER-0034 — Triangle / Minimal-Path CI Incomparability Witness 0.1.0

## Purpose

Show that the independent-source triangle model class is not merely another presentation of one of the six retired three-role/two-edge path conditional-independence model classes.

Two exact finite witnesses are used:

1. `q`, which belongs to the independent-source triangle but violates all six retired path restrictions;
2. `p_*`, which belongs to the retired noncollider path-family union but is excluded by the independent-source triangle by `PGH-DER-0033`.

## Witness q is generated inside the triangle

Let `U,V,W` be mutually independent fair bits and define deterministic local outputs

```text
A = 1 iff U=0 and W=0
B = 1 iff U=0 and V=0
C = 1 iff V=0 and W=0
```

Enumerating the eight equiprobable source triples gives

| U | V | W | A | B | C |
|---:|---:|---:|---:|---:|---:|
|0|0|0|1|1|1|
|0|0|1|0|1|0|
|0|1|0|1|0|0|
|0|1|1|0|0|0|
|1|0|0|0|0|1|
|1|0|1|0|0|0|
|1|1|0|0|0|0|
|1|1|1|0|0|0|

Hence

```text
q(000)=1/2
q(001)=1/8
q(010)=1/8
q(100)=1/8
q(111)=1/8
```

and all other outcomes have zero probability.

Therefore

\[
\boxed{q\in T_{\mathrm{ind}}}.
\]

## q violates all three marginal-independence restrictions

By symmetry,

\[
P_q(A=1)=P_q(B=1)=P_q(C=1)=\tfrac14.
\]

For every pair,

\[
P_q(A=1,B=1)=P_q(A=1,C=1)=P_q(B=1,C=1)=\tfrac18.
\]

Independence would require

\[
\tfrac14\cdot\tfrac14=\tfrac1{16},
\]

which differs from `1/8`.

Thus

```text
A independent C = FALSE
A independent B = FALSE
B independent C = FALSE
```

so `q` violates the three collider-center restrictions represented by PGH-OBJ-0041, PGH-OBJ-0043 and PGH-OBJ-0045.

## q violates all three separator conditional-independence restrictions

Consider `A independent B given C`. Since

\[
P(C=0)=\tfrac34,
\]

we have

\[
P(A=1\mid C=0)=P(B=1\mid C=0)=\frac{1/8}{3/4}=\tfrac16,
\]

while

\[
P(A=1,B=1\mid C=0)=0.
\]

Conditional independence would require `1/36`, not zero. Hence

\[
A\not\!\perp B\mid C.
\]

By cyclic symmetry of `q`, the same exact calculation gives

\[
B\not\!\perp C\mid A
\]

and

\[
A\not\!\perp C\mid B.
\]

Therefore `q` also violates the three noncollider separator restrictions, including the historical separator-B restriction of PGH-GRAM-0008.

Thus

\[
\boxed{q\notin \bigcup_{j=1}^{6}\mathcal P_j}
\]

where `P_j` denotes the six role-conditioned minimal path model classes, while `q in T_ind`.

## p_* lies in the retired noncollider path-family union

Recall

\[
p_*(000)=p_*(111)=\tfrac12.
\]

Condition on any one of `A`, `B`, or `C`. The remaining two variables are then both deterministic copies of the conditioning value. Their conditional joint law factors as the product of two point masses.

Therefore all three separator conditional independences hold:

\[
A\perp C\mid B,
\qquad
A\perp B\mid C,
\qquad
B\perp C\mid A.
\]

Equivalently, `p_*` admits each corresponding noncollider path factorization with deterministic transition kernels.

Hence

\[
\boxed{p_*\in \bigcup_{j=1}^{6}\mathcal P_j}.
\]

But `PGH-DER-0033` proves

\[
\boxed{p_*\notin T_{\mathrm{ind}}}.
\]

## Incomparability conclusion

We have exact witnesses in both directions:

```text
q IN T_ind AND q NOT_IN union(minimal-path classes)
p_* IN union(minimal-path classes) AND p_* NOT_IN T_ind
```

Therefore

\[
\boxed{
T_{\mathrm{ind}}
\text{ and }
\bigcup_j\mathcal P_j
\text{ are incomparable at this finite observed scope.}
}
\]

The M3 source-independence mechanism is thus structurally different from merely selecting another member of the retired minimal path-CI family.

## Claim ceiling

```text
STRUCTURAL_DIFFERENCE_FROM_RETIRED_PATH_CI = QUALIFIED
PHYSICAL_SUPERIORITY = NOT_CLAIMED
NETWORK_PHYSICAL_PRIVILEGE = NONE
R2B = UNSATISFIED
FCP_EFFECT = NONE
```
