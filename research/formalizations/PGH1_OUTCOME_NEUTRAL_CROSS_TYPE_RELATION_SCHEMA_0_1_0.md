# PGH-1 Outcome-Neutral Cross-Type Relation Schema 0.1.0

## Status

```text
OBJECT_ID = PGH-OBJ-0024
OBJECT_CLASS = CORRECTED_FORMAL_BRIDGE_SCHEMA
STATUS = PROVISIONAL_FORMAL_SCHEMA
PHYSICAL_STATUS = NONE
R2B = UNSATISFIED
```

## Purpose

Clarify what representation-neutral cross-type structure can mean after the outcome-neutral generativity gate exposed a covariance/automorphy confusion.

## Controlling distinction

Let a presentation contain context labels `C`, record labels `R`, and a cross-type relation

\[
T\subseteq C\times R.
\]

Under a relabeling

\[
\sigma:C\to C',\qquad \tau:R\to R',
\]

the representation-neutral requirement is **covariance**:

\[
T'=(\sigma\times\tau)[T].
\]

The renamed presentation may have a different labeled subset while representing the same abstract typed structure.

It is not generally required that

\[
(\sigma\times\tau)[T]=T
\]

on one fixed carrier for every permutation. That stronger condition is full permutation automorphy/homogeneity.

This is the cross-type analogue of canonical `PGH-FAIL-0002`.

## Conditional automorphy theorem

If one separately imposes full independent automorphy under

\[
S_C\times S_R,
\]

then `PGH-DER-0022` proves that the only invariant relations are

\[
\varnothing\quad\text{and}\quad C\times R.
\]

This is a legitimate theorem about a strong homogeneity axiom. It is not a theorem that label neutrality itself forces those extremes.

## Law-free cross-type structure

A future cross-type semantic/interface structure may be admissible without being a response law if it satisfies both:

1. **representation covariance** under faithful relabeling/translation;
2. **law-free multiplicity**: the same structure is compatible with at least two empirically incompatible response laws while held fixed.

A candidate example to test separately is a context-specific output typing relation

\[
T\subseteq C\times R,
\]

whose intended meaning is only that `r` is a well-typed record label for context `c`, not that the response `r` is possible, necessary, probable, or observed.

## Forbidden inference

```text
T(c,r) => PHYSICAL_RESPONSE_POSSIBLE
```

is not licensed merely by calling `T` a typing relation.

If `T` is chosen from observed response support, it fails the no-smuggling firewall.

## Physical ceiling

```text
FULL_PERMUTATION_AUTOMORPHY_AS_NEUTRALITY = REJECTED
RELABELING_COVARIANCE = REQUIRED
LAW_FREE_TYPED_CROSS_TYPE_STRUCTURE = POSSIBLE_IN_PRINCIPLE_NOT_YET_ADJUDICATED
PHYSICAL_BRIDGE = NONE
R2B = UNSATISFIED
```