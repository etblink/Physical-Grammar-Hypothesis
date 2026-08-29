# PGH-DER-0018 — Cartesian Copy/Discard Generation

## Status

```text
DERIVATION_ID = PGH-DER-0018
STATUS = QUALIFIED_FORMAL
PHYSICAL_CLAIM = NONE
```

## Claim

Finite-product structure canonically generates diagonal, deletion-to-terminal, and exchange maps without listing those maps object by object.

## Diagonal

Let `A x A` be a product with projections `pi_1, pi_2`.

By the product universal property there is a unique morphism

\[
\Delta_A=\langle 1_A,1_A\rangle:A\to A\times A
\]

such that

\[
\pi_1\Delta_A=1_A=\pi_2\Delta_A.
\]

## Discard-like map

If `1` is terminal, there is a unique morphism

\[
!_A:A\to 1.
\]

## Exchange

The product universal property gives

\[
\sigma_{A,B}=\langle \pi_2,\pi_1\rangle:A\times B\to B\times A,
\]

with inverse `sigma_{B,A}`.

## Naturality

For `f:A->B`, uniqueness gives

\[
(f\times f)\Delta_A=\Delta_B f,
\]

and terminality gives

\[
!_B f=!_A.
\]

Thus the construction is uniform and structural rather than an extensional permission table.

## Qualification

The derivation is conditional on finite-product structure.

```text
GENERATED_NOT_LISTED = YES
CANONICAL_RELATIVE_TO_CARTESIAN_DOCTRINE = YES
CARTESIAN_DOCTRINE_GENERATED_BY_ACCEPTED_PGH = NO
PHYSICAL_PRIVILEGE = NONE
```

## Dual control

Finite coproduct structure generates the different canonical package

\[
\nabla_A=[1_A,1_A]:A+A\to A,
\qquad
0\to A.
\]

Therefore universal-property generation does not itself uniquely select the product doctrine.

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = [CATEGORY]
RULE_DEPENDENCIES = [FINITE_PRODUCTS, TERMINAL_OBJECT]
SEMANTIC_ASSUMPTIONS = NONE
PHYSICAL_ASSUMPTIONS = NONE
```
