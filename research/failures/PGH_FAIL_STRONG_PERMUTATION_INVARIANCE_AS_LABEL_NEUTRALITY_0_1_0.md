# PGH-FAIL-0002 — Strong Permutation Invariance as Label Neutrality 0.1.0

## Identity

```text
DERIVATION_ID = PGH-FAIL-0002
OPERATION_ID = PGH0_NONARBITRARY_FORMATION_CONSTRAINT_CHALLENGE
STATUS = FAILED
CLAIMED_RESULT = LABEL_NEUTRALITY_REQUIRES_EVERY_CARRIER_PERMUTATION_TO_BE_AN_AUTOMORPHISM
FAILURE_CLASS = OVERSTRENGTHENED_PREMISE; REPRESENTATION_CONFUSION
```

## Proposed idea

Because primitive labels should carry no physical or grammatical significance, one might demand that a formation relation satisfy

\[
F(a,b,c)\iff F(\pi a,\pi b,\pi c)
\]

for every permutation `pi` of the carrier.

This produces a compact and strongly restrictive class of formation relations.

The inference from label neutrality to this condition is invalid.

## Covariance versus automorphism

Label neutrality requires that a renamed presentation represent the same structure up to isomorphism.

It does not require the renamed relation to be literally identical on the same labeled carrier.

For example:

```text
A = {0,1,2}
F = {(0,0,0)}
```

Swapping labels `0` and `1` gives the isomorphic presentation

```text
F' = {(1,1,1)}
```

The two presentations differ as labeled tables but are structurally isomorphic.

Requiring `F'=F` would forbid this relational individuation and impose homogeneity.

## Strength of the failed condition

On a three-label carrier, full permutation invariance groups ordered triples into five equality-pattern orbits. Therefore only

\[
2^5=32
\]

ternary relations satisfy the condition, out of

\[
2^{27}=134{,}217{,}728.
\]

So the proposed rule is genuinely selective.

That selectivity is precisely why its justification matters.

## Failure diagnosis

```text
RELABELING_COVARIANCE = REPRESENTATION_NEUTRALITY
FULL_PERMUTATION_AUTOMORPHY = STRUCTURAL_HOMOGENEITY
```

The second does not follow from the first.

Adopting it would insert a substantive structural law under the name of a representational convention.

## What remains valid

- scientific claims should be invariant under isomorphism/relabeling;
- full permutation invariance can be studied as a candidate homogeneity axiom if separately motivated;
- it does produce nontrivial formal exclusions.

What fails is the claim that it is already required by label neutrality.

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = FORMATION_RELATION
RULE_DEPENDENCIES = FULL_PERMUTATION_AUTOMORPHY
LEMMA_DEPENDENCIES = ORBIT_DECOMPOSITION_BY_EQUALITY_PATTERN
SEMANTIC_ASSUMPTIONS = NONE
PHYSICAL_ASSUMPTIONS = NONE
SOURCE_DEPENDENCIES = NONE
METALANGUAGE_DEPENDENCIES = PERMUTATION_GROUPS; RELATIONS; EQUALITY
```

## Result

```text
PGH-FAIL-0002 = FAILED_PRESERVED
STRONG_PERMUTATION_INVARIANCE_IS_LABEL_NEUTRALITY = REJECTED
STRONG_PERMUTATION_INVARIANCE_AS_SEPARATE_AXIOM = NOT_ADJUDICATED_AS_PHYSICAL
WHAT_REMAINS = ISOMORPHISM_COVARIANCE_ONLY
```
