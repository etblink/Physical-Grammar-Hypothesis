# PGH-DER-0006 — Formal Equivalence Does Not Entail Physical Equivalence 0.1.0

## Identity

```text
DERIVATION_ID = PGH-DER-0006
OPERATION_ID = PGH0_PHYSICAL_IRRELEVANCE_SELECTOR_FEASIBILITY_GATE
STATUS = QUALIFIED_FORMAL
CLAIM_SCOPE = FORMAL_PRESENTATION_EQUIVALENCE_WITH_UNRESTRICTED_PHYSICAL_SIGNIFICANCE_MAP
PHYSICAL_CLAIM = NONE
NOVELTY_CLAIM = NONE
```

## Claim

Let `P` be a presentation space and `E` a nontrivial equivalence relation on `P`.

If no independent constraint is imposed on admissible physical-significance maps

\[
\sigma:P\to S,
\]

then `E` alone does not entail that `E`-equivalent presentations have the same physical significance.

Formally, from

\[
p E p'
\]

one cannot derive

\[
\sigma(p)=\sigma(p')
\]

for arbitrary admissible `sigma` unless constancy on `E`-classes is itself imposed as an additional condition.

## Proof

Choose distinct `p,p' in P` such that `p E p'`. Let `S={0,1}`.

Define

\[
\sigma_{same}(x)=0
\]

for all `x in P`.

Then

\[
\sigma_{same}(p)=\sigma_{same}(p').
\]

Now define a second map with

\[
\sigma_{split}(p)=0,\qquad \sigma_{split}(p')=1,
\]

and assign arbitrary values to all remaining elements of `P`.

Then

\[
\sigma_{split}(p)\neq\sigma_{split}(p').
\]

The same formal pair `(P,E)` therefore admits both a significance assignment that identifies the `E`-equivalent pair and one that distinguishes it.

Hence formal facts about `E` alone do not entail physical-significance constancy on `E`-classes. QED.

## Corollary — Extra condition required

To infer physical irrelevance from formal equivalence, one must add a restriction such as:

\[
\sigma = \bar\sigma\circ q_E,
\]

where `q_E:P→P/E` is the quotient map, or an equivalent condition that all admissible physical-significance maps are constant on `E`-classes.

But the requirement that physical significance factor through `E` is precisely an additional semantic/physical condition. It is not supplied by the formal equivalence relation itself.

## Relationship to PGH-DER-0004

`PGH-DER-0004` showed:

> once a projection/equivalence is declared, coherence is factorization through the retained invariant content.

`PGH-DER-0006` adds the converse warning relevant to R1:

> formal factorization is not physically mandatory unless admissible physical significance is independently constrained to respect that quotient.

Thus:

\[
\text{formal quotient}
\not\Rightarrow
\text{physical quotient}
\]

without a semantic anchor.

## Scope boundary

The theorem does **not** say:

```text
PHYSICAL_EQUIVALENCE_IS_IMPOSSIBLE = NO
SEMANTICS_MUST_CONTAIN_FULL_PHYSICS = NO
PGH_IS_FALSE = NO
```

It says only that some restriction on the physical interpretation/significance relation is logically necessary if a formal equivalence is to have physical force.

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = PRESENTATION_SPACE; FORMAL_EQUIVALENCE; SIGNIFICANCE_CODOMAIN
RULE_DEPENDENCIES = NONE
LEMMA_DEPENDENCIES = EXISTENCE_OF_DISTINCT_EQUIVALENT_PRESENTATIONS
SEMANTIC_ASSUMPTIONS = PHYSICAL_SIGNIFICANCE_MAP_UNRESTRICTED_AT_FORMAL_SCOPE
PHYSICAL_ASSUMPTIONS = NONE
SOURCE_DEPENDENCIES = FROZEN_EQUIVALENCE_LANDSCAPE_AS_CONTEXT_ONLY
METALANGUAGE_DEPENDENCIES = SETS_OR_CLASSES; FUNCTIONS; EQUALITY; EQUIVALENCE_RELATIONS
```

## Result

```text
FORMAL_EQUIVALENCE_ALONE_ENTAILS_PHYSICAL_EQUIVALENCE = NO
ADDITIONAL_SEMANTIC_OR_PHYSICAL_RESTRICTION_REQUIRED = YES
R1_PURELY_FORMAL_ROUTE = BLOCKED_AT_CURRENT_SCOPE
```
