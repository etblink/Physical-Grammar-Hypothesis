# PGH-DER-0002 — Isomorphism Covariance Underdetermination 0.1.0

## Identity

```text
DERIVATION_ID = PGH-DER-0002
OPERATION_ID = PGH0_NONARBITRARY_FORMATION_CONSTRAINT_CHALLENGE
STATUS = QUALIFIED_FORMAL
CLAIM_SCOPE = FORMATION_STRUCTURE_SELECTION_UNDER_BIJECTIVE_RELABELING
PHYSICAL_CLAIM = NONE
```

## Claim

Requiring a formation-law selector to be invariant under bijective relabeling does not by itself determine or nontrivially privilege any collection of formation structures.

More precisely, if formation structures are partitioned into isomorphism classes, every arbitrary subset of those classes defines an isomorphism-invariant selector.

Therefore representation covariance under renaming removes label dependence but does not remove structural selection arbitrariness.

## Setup

Let `S` be any collection of formation structures `G=(A,F)` at a declared scope, and let `~=` denote structure isomorphism induced by bijections of carriers preserving `F`.

Let

\[
S/{\cong}
\]

be the set of isomorphism classes.

A selector is a predicate

\[
C:S\to\{0,1\}.
\]

Relabeling covariance requires

\[
G\cong H\Longrightarrow C(G)=C(H).
\]

## Theorem

For every subset

\[
U\subseteq S/{\cong},
\]

define

\[
C_U(G)=1
\quad\Longleftrightarrow\quad
[G]\in U.
\]

Then `C_U` is isomorphism-invariant.

### Proof

If `G ≅ H`, then `[G]=[H]`. Therefore `[G] in U` iff `[H] in U`, so `C_U(G)=C_U(H)`. QED.

Because `U` is arbitrary, covariance alone does not determine which structural classes are selected.

## Finite witness — two-label ternary relations

Let `A={0,1}` and `F subset A^3`.

There are

\[
2^8=256
\]

ternary relations.

The permutation group has two elements: identity and the swap `0<->1`.

The identity fixes all 256 relations.

Under the nontrivial swap, the eight ordered triples form four two-element orbits. A relation fixed by the swap must include or exclude each orbit as a whole, so exactly

\[
2^4=16
\]

relations are fixed.

By Burnside averaging, the number of isomorphism classes is

\[
(256+16)/2=136.
\]

Therefore there are

\[
2^{136}
\]

distinct selectors on these classes that all satisfy relabeling covariance.

This finite example makes the underdetermination explicit.

## Important distinction

The theorem does not say that relabeling covariance is unimportant.

It says:

```text
RELABELING_COVARIANCE = NECESSARY_FOR_LABEL_NEUTRALITY
RELABELING_COVARIANCE = INSUFFICIENT_FOR_STRUCTURAL_SELECTION
```

A stronger requirement may exclude structures, but its extra content must be justified separately.

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = FORMATION_STRUCTURES_AS_OBJECTS_OF_ANALYSIS
RULE_DEPENDENCIES = SELECTOR_IS_CONSTANT_ON_ISOMORPHISM_CLASSES
LEMMA_DEPENDENCIES = ISOMORPHIC_STRUCTURES_HAVE_THE_SAME_CLASS
SEMANTIC_ASSUMPTIONS = NONE_BEYOND_FORMAL_STRUCTURE_SELECTION
PHYSICAL_ASSUMPTIONS = NONE
SOURCE_DEPENDENCIES = NONE
METALANGUAGE_DEPENDENCIES = SETS_OR_CLASSES; EQUIVALENCE_CLASSES; BIJECTIONS; FINITE_GROUP_ACTION_FOR_EXAMPLE
```

## Result

```text
PGH-DER-0002 = QUALIFIED_FORMAL
REPRESENTATION_COVARIANCE_ALONE_SELECTS_FORMATION = NO
NONARBITRARY_FORMATION_CONSTRAINT_DERIVED = NO
PHYSICAL_CONSEQUENCE = NONE
```
