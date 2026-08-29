# PGH-0 Representation Equivalence and Coherence — Adjudication 0.1.0

## Identity

```text
OPERATION_ID = PGH0_REPRESENTATION_EQUIVALENCE_AND_COHERENCE_CHALLENGE
REGISTRY_ID = PGH-OP-0007
CANONICAL_BASE = b2c969f4708458e7007bec6d051cce3d0d9c7e75
PREREGISTRATION_COMMIT = f1853b509535d73fba6b523eb0162b324eed1d40
SOURCE_BOUND_STATUS = NOT_YET_SOURCE_BOUND
NEW_SOURCE_COUNT = 0
```

## Outcome

```text
OUTCOME = B__OUTCOME_INDEPENDENT_EQUIVALENCE_IS_DEFINED_BUT_PROJECTION_SELECTION_REMAINS_UNDERDETERMINED
SUCCESSOR_GRAMMAR_QUALIFIED = NO
ACTIVE_BASELINE_REMAINS = PGH-GRAM-0002
PHYSICAL_BRIDGE = NOT_PERFORMED
```

The experiment resolves one uncertainty and exposes another.

A presentation-equivalence relation can be defined **without** evaluating the candidate operation by choosing a syntax-level projection

\[
q:P\to I
\]

from detailed presentations `P` to retained invariant content `I`, and defining

\[
p\sim_q p' \iff q(p)=q(p').
\]

Coherence of an evaluation `e:P→A` is then the independent requirement that `e` factor through `q`.

Thus representation equivalence need not be defined circularly by equality of evaluated outputs.

However, current PGH commitments do not uniquely determine which projection `q` is privileged. Different outcome-independent, relabeling-covariant projections erase different presentation distinctions and therefore impose different coherence laws.

## E1 — Outcome-independent equivalence

For the preregistered binary-tree presentation space, all four projections are defined without reference to the binary operation being tested:

```text
P0_IDENTITY = OUTCOME_INDEPENDENT
P1_ORDERED_LEAF_WORD = OUTCOME_INDEPENDENT
P2_LEAF_MULTISET = OUTCOME_INDEPENDENT
P3_LENGTH = OUTCOME_INDEPENDENT
```

Therefore:

```text
ONLY_OPERATION_DEPENDENT_EQUIVALENCE_CAN_BE_DEFINED = FALSE
```

## E2 — Ordered-leaf factorization

Let `W(T)` be the ordered leaf word of a binary tree.

Evaluation under a total binary operation `star` factors through `W` for all finite trees iff `star` is associative.

Forward direction: the two three-leaf trees

\[
((a b)c),\qquad (a(b c))
\]

have the same ordered leaf word, so coherence forces

\[
(a\star b)\star c=a\star(b\star c).
\]

Reverse direction: associativity makes every parenthesization of a fixed ordered word evaluate to the same iterated product, by induction on tree size.

Finite two-element validation:

```text
TOTAL_BINARY_OPERATIONS = 16
P1_COHERENT = 8
```

## E3 — Multiset factorization

Let `M(T)` be the multiset of leaf labels.

Evaluation factors through `M` for all finite trees iff `star` is associative and commutative.

Forward direction:

- two-leaf trees `(a b)` and `(b a)` have the same multiset, forcing commutativity;
- alternative three-leaf parenthesizations have the same multiset, forcing associativity.

Reverse direction: an associative commutative product depends only on the finite multiset of factors.

Finite two-element validation:

```text
P2_COHERENT = 6
```

An associative but noncommutative separator is the left-projection operation

\[
a\star b=a.
\]

It passes P1 and fails P2 when `a != b`.

## E4 — Length-only control

Let `L(T)` be the number of leaves.

For nonempty presentation trees, factorization through length requires all one-leaf presentations to evaluate equally.

On a carrier with at least two distinct elements and the ordinary leaf assignment, this is impossible because a one-leaf tree evaluates to its leaf label.

Therefore on a two-element carrier:

```text
P3_COHERENT = 0
```

This is the over-forgetting control.

## E5 — Identity control

The identity projection equates only literally identical presentations. Factorization therefore imposes no equality between distinct presentations.

On a two-element carrier:

```text
P0_COHERENT = 16
```

This is the under-forgetting control.

## Coherence ladder

The four projections form an information-forgetting ladder:

\[
P0 \succeq P1 \succeq P2 \succeq P3,
\]

where moving right forgets more presentation structure.

The compatible two-element operation classes shrink accordingly:

\[
16 \supset 8 \supset 6 \supset 0.
\]

The general monotonicity is exact: if equivalence `E2` is coarser than `E1` (so `E2` identifies every pair identified by `E1` and possibly more), any evaluation coherent with `E2` is coherent with `E1`.

Therefore:

> **The more presentation distinctions declared irrelevant, the stronger the resulting coherence constraints.**

This is a formal theorem, not a physical law.

## E6 — Projection-selection underdetermination

The four projections are all specified syntactically and are covariant under bijective renaming of leaf labels. Yet they induce different coherence classes.

Current PGH methodology does not uniquely justify:

- retaining the full parse tree;
- forgetting bracketing but retaining order;
- forgetting both bracketing and order;
- forgetting labels as well.

Selecting P1 because it yields associativity would be circular at the level of project motivation even though the equivalence relation itself is outcome-independent.

Thus:

```text
OUTCOME_INDEPENDENT_EQUIVALENCE_DEFINED = YES
UNIQUE_PRIVILEGED_PROJECTION_FOUND = NO
PROJECTION_SELECTION_UNDERDETERMINATION = YES
```

## E7 — Arity-neutral formulation

The projection/factorization framework itself is not fundamentally binary.

For any presentation collection `P`, any syntax- or structure-defined map

\[
q:P\to I
\]

induces presentation equivalence by equality of `q`-images. An evaluation or admissibility map is coherent exactly when it is constant on the fibers of `q`, equivalently when it factors through the quotient image.

This abstract statement applies to binary trees, flat n-ary presentations, relational encodings, and auxiliary-node presentations.

However, bare `PGH-GRAM-0002` does not supply a canonical `q` connecting those different presentation families.

Therefore:

```text
PROJECTION_METHOD_BINARY_ONLY = NO
ARITY_NEUTRAL_FACTORIZATION_FRAMEWORK = YES
CANONICAL_CROSS_PRESENTATION_PROJECTION = NOT_ESTABLISHED
```

## Qualified derivations

```text
PGH-DER-0004 = PRESENTATION_PROJECTION_FACTORIZATION
STATUS = QUALIFIED_FORMAL

PGH-DER-0005 = COHERENCE_MONOTONICITY_UNDER_FORGETTING
STATUS = QUALIFIED_FORMAL
```

## Preserved failure

```text
PGH-FAIL-0004 = UNIQUE_PROJECTION_FROM_REPRESENTATION_INVARIANCE
STATUS = FAILED_PRESERVED
```

Representation invariance by itself does not choose which structural distinctions should be forgotten.

## Nontriviality assessment

```text
N0_FORMAL_DEFINABILITY = PASS
N1_UNIVERSAL_ENCODING = PARTIAL
N2_NO_SMUGGLING = PASS_FOR_FORMAL_PROJECTION_RESULTS
N3_NONUNIVERSAL_EXCLUSION = PASS_CONDITIONALLY_ON_CHOSEN_PROJECTION
N4_REPRESENTATION_INVARIANCE = PARTIAL
N5_SEMANTIC_LOAD = NOT_APPLICABLE
N6_GENERATIVE_COMPRESSION = NOT_ESTABLISHED
N7_INDEPENDENT_CONSEQUENCE = PASS_FORMALLY_CONDITIONAL
N8_COUNTEREXAMPLE_EXPOSURE = PASS
N9_RELABELING_INVARIANCE = PASS
N10_PHYSICAL_BRIDGE = NOT_APPLICABLE
```

The operation does not pass the opening PGH physical bridge gate because the projection-selection problem remains unresolved.

## Main conceptual result

The previous project question was:

\[
\text{What makes two presentations the same?}
\]

The answer is now split into two layers:

1. **Formal mechanism:** a projection or quotient can define their equivalence without consulting the algebraic outcome.
2. **Foundational selection:** current PGH does not yet explain which projection represents physically or fundamentally irrelevant structure.

The deep bottleneck is therefore no longer the existence of noncircular equivalence. It is **selection of invariant content**.

## Hard non-effects

```text
ASSOCIATIVITY_IS_FUNDAMENTAL = NO
COMMUTATIVITY_IS_FUNDAMENTAL = NO
PROJECTION_P1_IS_FUNDAMENTAL = NO
PHYSICAL_GRAMMAR_FOUND = NO
PHYSICAL_LAW_DERIVED = NO
EMPIRICAL_SUPPORT = NONE
FCP_EFFECT = NONE
```

## Next scientific recommendation

Further purely internal formalization now risks choosing a preferred invariant by intuition. Before another foundational-selection axiom is proposed, the Project Lead recommends a bounded external source-intake and prior-art landscape audit focused on representation equivalence, quotient/coherence methods, formal grammar, universal algebra/rewriting, operadic or categorical coherence, and neighboring foundational-physics programs.

Proposed next operation:

```text
PGH0_REPRESENTATION_COHERENCE_SOURCE_LANDSCAPE_INTAKE
```

This recommendation does not itself admit any external source or alter PGH.
