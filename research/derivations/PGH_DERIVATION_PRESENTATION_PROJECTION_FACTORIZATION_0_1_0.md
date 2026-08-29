# PGH-DER-0004 — Presentation Projection Factorization 0.1.0

## Identity

```text
DERIVATION_ID = PGH-DER-0004
OPERATION_ID = PGH0_REPRESENTATION_EQUIVALENCE_AND_COHERENCE_CHALLENGE
STATUS = QUALIFIED_FORMAL
PHYSICAL_CLAIM = NONE
```

## Claim

Let `P` be any collection of formal presentations and let

\[
q:P\to I
\]

be a map defined independently of the candidate evaluation being tested.

Define

\[
p\sim_q p' \iff q(p)=q(p').
\]

Then `~_q` is an outcome-independent equivalence relation.

For any evaluation or interpretation map

\[
e:P\to A,
\]

the following are equivalent:

1. `e(p)=e(p')` whenever `p~_q p'`;
2. `e` is constant on every fiber of `q`;
3. there exists a unique map

\[
\bar e:\operatorname{im}(q)\to A
\]

such that

\[
e=\bar e\circ q.
\]

Thus coherence relative to a declared representation equivalence is exactly factorization through the retained invariant content.

## Proof

`~_q` is equality of `q`-images, so it is reflexive, symmetric, and transitive.

If `e` is constant on fibers, define `ebar(q(p))=e(p)`. Fiber constancy makes this well defined, and construction gives `e=ebar∘q`. Uniqueness follows because every element of `im(q)` is `q(p)` for some `p`.

Conversely, if `e=ebar∘q` and `q(p)=q(p')`, then `e(p)=ebar(q(p))=ebar(q(p'))=e(p')`. QED.

## Binary-tree specializations

For ordered binary-tree presentations:

```text
P0 = full tree identity
P1 = ordered leaf word
P2 = leaf multiset
P3 = leaf count
```

All four maps are definable without evaluating a binary operation.

Therefore the representation-equivalence relation need not be defined by the coherence result itself.

## Scope

The theorem is arity-neutral and algebra-neutral. It does not identify which `q` is fundamental or physically meaningful.

```text
OUTCOME_INDEPENDENT_EQUIVALENCE_EXISTS = YES
CANONICAL_PROJECTION_SELECTED = NO
PHYSICAL_EQUIVALENCE_DERIVED = NO
```

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = NONE_BEYOND_PRESENTATION_SPACE_AND_PROJECTION
RULE_DEPENDENCIES = EQUALITY_OF_PROJECTION_IMAGES
LEMMA_DEPENDENCIES = FIBER_FACTORIZATION
SEMANTIC_ASSUMPTIONS = NONE_PHYSICAL
PHYSICAL_ASSUMPTIONS = NONE
SOURCE_DEPENDENCIES = NONE
METALANGUAGE_DEPENDENCIES = SETS_OR_CLASSES; FUNCTIONS; EQUALITY; QUOTIENTS
```
