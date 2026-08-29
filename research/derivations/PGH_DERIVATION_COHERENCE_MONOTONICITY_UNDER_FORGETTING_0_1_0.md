# PGH-DER-0005 — Coherence Monotonicity Under Forgetting 0.1.0

## Identity

```text
DERIVATION_ID = PGH-DER-0005
OPERATION_ID = PGH0_REPRESENTATION_EQUIVALENCE_AND_COHERENCE_CHALLENGE
STATUS = QUALIFIED_FORMAL
PHYSICAL_CLAIM = NONE
```

## General theorem

Let `E1` and `E2` be equivalence relations on a presentation space `P` such that

\[
E1\subseteq E2,
\]

meaning that `E2` identifies every pair identified by `E1` and possibly more.

If an evaluation `e:P→A` is coherent with `E2`, then it is coherent with `E1`.

### Proof

If `p E1 p'`, then `p E2 p'` by inclusion. `E2`-coherence gives `e(p)=e(p')`. Therefore `e` is `E1`-coherent. QED.

So increasing the amount of presentation structure declared irrelevant can only maintain or strengthen the resulting coherence constraints.

## Binary-tree coherence ladder

For finite nonempty ordered binary trees with leaves evaluated in a total binary operation:

```text
P0 = full tree identity
P1 = ordered leaf word
P2 = leaf multiset
P3 = leaf count
```

Their induced equivalences become successively coarser:

\[
E_{P0}\subseteq E_{P1}\subseteq E_{P2}\subseteq E_{P3}.
\]

### P0

Identity coherence imposes no equation between different presentations.

Two-element count:

```text
P0_COHERENT_OPERATIONS = 16
```

### P1

Coherence under forgetting bracketing but retaining ordered leaves is equivalent to associativity.

Two-element count:

```text
P1_COHERENT_OPERATIONS = 8
```

### P2

Coherence under forgetting bracketing and order while retaining the multiset is equivalent to associativity plus commutativity.

Two-element count:

```text
P2_COHERENT_OPERATIONS = 6
```

### P3

Coherence under retaining only leaf count identifies all one-leaf presentations. On a carrier with at least two distinct elements this conflicts with ordinary leaf evaluation, so no two-element operation is coherent with P3 over the full nonempty presentation space.

```text
P3_COHERENT_OPERATIONS = 0
```

Therefore the finite coherence ladder is:

\[
16\supset 8\supset 6\supset 0.
\]

## Separating examples

The operation

\[
a\star b=a
\]

is associative but not commutative on a carrier with at least two elements. It therefore passes P1 and fails P2.

A preregistered nonassociative two-element operation fails P1.

Any nontrivial two-element carrier fails P3 already at one-leaf presentations.

## Interpretation boundary

The theorem establishes a structural relation between **how much representation information is forgotten** and **how restrictive coherence becomes**.

It does not establish which information should be forgotten.

```text
COHERENCE_STRENGTH_MONOTONIC_WITH_FORGETTING = YES
PRIVILEGED_FORGETTING_LEVEL = NOT_ESTABLISHED
ASSOCIATIVITY_IS_PHYSICAL = NO
COMMUTATIVITY_IS_PHYSICAL = NO
```

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = PRESENTATION_EQUIVALENCE
RULE_DEPENDENCIES = COHERENCE_AS_CONSTANCY_ON_EQUIVALENCE_CLASSES
LEMMA_DEPENDENCIES = PGH-DER-0004
SEMANTIC_ASSUMPTIONS = ORDINARY_RECURSIVE_TREE_EVALUATION_FOR_BINARY_SPECIALIZATION
PHYSICAL_ASSUMPTIONS = NONE
SOURCE_DEPENDENCIES = NONE
METALANGUAGE_DEPENDENCIES = EQUIVALENCE_RELATIONS; FUNCTIONS; FINITE_TREES
```
