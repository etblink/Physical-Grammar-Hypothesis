# PGH-FAIL-0011 — Generic Empirical Substructure Privilege Selectors 0.1.0

## Identity

```text
DERIVATION_ID = PGH-FAIL-0011
OPERATION_ID = PGH0_EMPIRICAL_SUBSTRUCTURE_PRIVILEGE_GATE
STATUS = FAILED_PRESERVED
FAILURE_CLASS = UNDERDETERMINED_TRIVIAL_OR_EXTRA_SELECTOR_INPUT
```

## Failed idea

The gate tested whether standard intrinsic properties of a grammar-generated closure system can generally identify one physically privileged empirical substructure without empirical-result input.

No tested generic criterion succeeds.

## Smallest nontrivial

In the symmetric witness both `{a,b}` and `{c,d}` are smallest nonempty proper closed substructures.

```text
SMALLEST_NONTRIVIAL = NONUNIQUE
```

## Largest

The unique largest closed substructure is the entire formal context universe `P`.

```text
LARGEST = FORMALLY_UNIQUE_BUT_EMPIRICALLY_NONSELECTIVE
```

Uniqueness of the whole universe does not establish that every formal context is physically empirical.

## Automorphism invariant

Only `empty` and `P` are fixed by every automorphism in the symmetric witness.

```text
FULL_AUTOMORPHISM_INVARIANCE = TRIVIAL_EXTREMES
```

## Closure fixed point

Every closed substructure satisfies `Cl(T)=T`, so this criterion selects every candidate.

```text
CLOSURE_FIXED_POINT = UNDERDETERMINED
```

## Free canonical endomap

A freely introduced endomap `F` on the closed-substructure space can encode any target `T0` as a unique fixed point by taking `F(S)=T0` for all `S`.

```text
FREE_CANONICAL_OPERATOR = UNIVERSAL_TARGET_ENCODER
```

## Intersection and union

For the two proper blocks `A` and `B`:

\[
A\cap B=\varnothing,
\qquad
A\cup B=P.
\]

Thus natural meet/join aggregation produces the trivial extremes.

## Simplicity

The symmetric blocks are exchanged by automorphism, so any representation-respecting intrinsic complexity measure cannot privilege one over the other. An external coding language merely reintroduces the unprivileged simplicity failure already preserved in PGH.

## Empirical success

Selecting a substructure because it matches known records, experimental success, or desired physical distinguishability is legitimate empirical model selection but is not an **intrinsic grammar-derived privilege criterion**. It is result-directed relative to R1.

## Important limitation

The failure is general-principle failure, not impossibility.

An asymmetric grammar can contain a unique smallest proper closed substructure. Therefore this artifact does not claim that no grammar can ever internally distinguish a candidate empirical substructure.

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = FIXED_GRAMMAR_CLOSURE_SYSTEM
RULE_DEPENDENCIES = GENERIC_INTRINSIC_SELECTOR_FAMILIES
LEMMA_DEPENDENCIES = PGH-DER-0011
SEMANTIC_ASSUMPTIONS = NONE
PHYSICAL_ASSUMPTIONS = EMPIRICAL_SUCCESS_CONTROL_EXPLICITLY_USES_TARGET_DATA
SOURCE_DEPENDENCIES = FROZEN_37_SOURCE_LANDSCAPE
```

## Result

```text
PGH-FAIL-0011 = FAILED_PRESERVED
GENERAL_INTRINSIC_EMPIRICAL_SUBSTRUCTURE_PRIVILEGE_SELECTOR = NOT_FOUND
SPECIAL_GRAMMAR_INTRINSIC_UNIQUENESS = POSSIBLE
PHYSICAL_PRIVILEGE = UNESTABLISHED
```
