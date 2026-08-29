# PGH-FAIL-0026 — Typed Anchor Internalization as Bridge Selector

## Status

```text
FAILURE_ID = PGH-FAIL-0026
STATUS = FAILED_PRESERVED
PHYSICAL_CLAIM = NONE
```

## Failure 1 — edge internalization

Given a typed relation

\[
T\subseteq C\times R,
\]

suppose every pair `(c,r) in T` is internalized by a primitive generating morphism

\[
e_{c,r}:X_c\to Y_r.
\]

Then the formal hom-existence relation contains `T` by construction.

If one later reads hom existence as the derived cross-type bridge, the alleged result was entered in the generating signature.

```text
TYPED_PAIR_SET = INPUT
CROSS_TYPE_EDGE_SET = SAME_INFORMATION_AS_INPUT
EXPLANATORY_CREDIT_FOR_REPRODUCING_T = FAIL
```

## Failure 2 — product packaging is edge data in disguise

For a two-label typed fiber, adding

\[
m:X\to Y0\times Y1
\]

may look syntactically more compact than adding two component arrows.

But the product universal property gives a natural bijection

\[
Hom(X,Y0\times Y1)
\cong
Hom(X,Y0)\times Hom(X,Y1).
\]

Therefore specifying `m` is equivalent formal information to specifying the two component arrows.

```text
ONE_PRODUCT_CODOMAIN_GENERATOR =/=> EXPLANATORY_COMPRESSION
PRODUCT_PACKAGING_OF_EDGE_PAIR = EDGE_INFORMATION_IN_EQUIVALENT_FORM
```

This is a direct anti-smuggling/control lesson: surface symbol count is not explanatory compression.

## Failure 3 — post-hoc internalization choice

The same typed interface and same bicartesian doctrine admit internalizations with different component-arrow consequences (`PGH-DER-0025`).

Therefore choosing the internalization because its consequences resemble the desired response pattern relocates bridge selectivity into the embedding map.

Examples of prohibited reasoning include:

```text
CHOOSE_PRODUCT_OUTPUT_BECAUSE_COMPONENT_ARROWS_ARE_DESIRED
CHOOSE_COPRODUCT_OUTPUT_BECAUSE_COMPONENT_ARROWS_SHOULD_BE_ABSENT
CHOOSE_CONTEXT_AS_PROCESS_BECAUSE_THAT_MAKES_A_BRIDGE_EXIST
```

when the choice follows the target consequence.

## Failure 4 — representation-role smuggling

A context label from the semantic anchor does not canonically determine whether it should be represented as an object, process, process source, typed codomain, or some other categorical/interface role.

Using whichever role makes a bridge work and then attributing that bridge to the grammar fails the no-smuggling standard.

## What remains valid

The coproduct-output control shows that not every nontrivial internalization is equivalent to an extensional component-edge list.

A generic process

\[
n:X\to Y0+Y1
\]

can be introduced without thereby determining either component arrow.

Such a generic typed process remains additional primitive bridge structure and does not yet have physical response meaning, but it is formally weaker than a component response-edge specification.

## Failure classification

```text
FAILURE_CLASS = BRIDGE_INTERNALIZATION_RELOCATION; EQUIVALENT_EDGE_PACKAGING; TARGET_DIRECTED_EMBEDDING_SELECTION
HIDDEN_IMPORT = COMPONENT_EDGE_INFORMATION_OR_UNJUSTIFIED_CONTEXT_OUTPUT_EMBEDDING
WHAT_REMAINS_VALID = GENERIC_AGGREGATE_OUTPUT_PROCESS_INTERNALIZATIONS_CAN_BE_FORMALLY_WEAKER_THAN_COMPONENT_RESPONSE_EDGES
```