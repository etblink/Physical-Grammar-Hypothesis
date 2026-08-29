# PGH-0 Representation Equivalence and Coherence Challenge — Preregistration 0.1.0

## Status

```text
OPERATION_ID = PGH0_REPRESENTATION_EQUIVALENCE_AND_COHERENCE_CHALLENGE
REGISTRY_ID = PGH-OP-0007
OPERATION_CLASS = FOUNDATIONAL_FORMALIZATION
STATUS = PREREGISTERED_IN_PROGRESS
CANONICAL_BASE = b2c969f4708458e7007bec6d051cce3d0d9c7e75
SCIENTIFIC_INPUT_BASELINE = PGH-GRAM-0002
WORKING_BRANCH = research/pgh0-representation-equivalence-coherence
SOURCE_BOUND_STATUS = NOT_YET_SOURCE_BOUND
NEW_SOURCE_SEARCH = FORBIDDEN
PHYSICAL_BRIDGE = NOT_AUTHORIZED
FCP_EFFECT = NONE
```

## Purpose

The previous operation showed that a coherence premise can force a genuine formal exclusion, but that the premise itself was unearned. This operation targets that missing left-hand step:

\[
\text{representation equivalence}
\Longrightarrow
\text{coherence}
\Longrightarrow
\text{formal exclusion}.
\]

The question is not whether associativity is true or fundamental. It is:

> Can an equivalence between presentations be defined independently of the algebraic coherence equation that follows from it, and if so, does current PGH methodology uniquely privilege that equivalence?

## Preserved baseline

```text
PGH-GRAM-0002 = PROVISIONAL_FORMAL_BASELINE_NONPHYSICAL
PGH-DER-0002 = QUALIFIED
PGH-DER-0003 = QUALIFIED_CONDITIONAL_FORMAL
SUCCESSOR_GRAMMAR = NOT_ASSUMED
```

## Anti-circularity criterion

A candidate presentation-equivalence relation `~` may be called **outcome-independent** only if membership in `p ~ q` can be determined without evaluating the candidate formation operation whose coherence is later tested.

In particular, the operation may not define

```text
p ~ q  iff  eval(p) = eval(q)
```

and then count equality of evaluations as a derived result.

## Presentation space

For the primary finite test, let `X` be a formal alphabet and `T(X)` the set of finite nonempty ordered full binary trees whose leaves are labeled in `X`.

This is a presentation formalism only. Binary branching is not being promoted to fundamental ontology.

Define several syntax-level projections before testing any algebraic operation.

### P0 — Identity projection

```text
I(T) = T
```

No presentation differences are forgotten.

### P1 — Ordered-leaf projection

```text
W(T) = ordered leaf word of T
```

Tree bracketing is forgotten while leaf identities and left-to-right order are retained.

### P2 — Leaf-multiset projection

```text
M(T) = multiset of leaf labels
```

Both bracketing and left-to-right order are forgotten.

### P3 — Length projection

```text
L(T) = number of leaves
```

Bracketing, order, and label identity are forgotten.

Each projection induces an outcome-independent equivalence:

\[
T\sim_P T' \iff P(T)=P(T').
\]

No evaluation map appears in this definition.

## Evaluation family

For a total binary operation

\[
\star:A\times A\to A,
\]

and a leaf assignment into `A`, let `eval_star(T)` denote ordinary recursive evaluation of the tree.

A projection `P` is **evaluation-coherent** for `star` if evaluation factors through `P`:

\[
P(T)=P(T')\Longrightarrow eval_\star(T)=eval_\star(T').
\]

This factorization requirement is the coherence condition to be tested, not built into `~_P`.

## Frozen tests

The operation must proceed in this order.

### E1 — Noncircularity of projection-induced equivalence

For P0–P3 determine whether equivalence is definable without reference to `star` or its outputs.

Required result:

```text
OUTCOME_INDEPENDENT_EQUIVALENCE = YES/NO per projection
```

### E2 — Ordered-leaf factorization theorem

Test whether evaluation through `P1=W` is equivalent to associativity of `star`.

Required burdens:

- prove both directions at finite-tree scope;
- retain the explicit nonassociative two-element counterexample from PGH-DER-0003;
- do not call associativity fundamental.

### E3 — Multiset factorization theorem

Test whether evaluation through `P2=M` requires both associativity and commutativity.

Required burdens:

- derive commutativity from two-leaf presentations;
- derive associativity from three-leaf presentations;
- prove the converse by finite-tree rearrangement;
- supply finite examples.

### E4 — Length-only factorization control

Determine how strong `P3=L` is.

Test whether evaluation independence from labels and parse forces severe collapse, and characterize the constraint at least on finite two-element carriers.

This is a control for over-forgetting.

### E5 — Identity-projection control

Confirm that P0 imposes no cross-presentation coherence and therefore excludes no operation merely from factorization.

This is a control for under-forgetting.

### E6 — Projection-selection underdetermination

Ask whether current PGH commitments uniquely select P1 rather than P0, P2, P3, or another relabeling-covariant projection.

A projection is not privileged merely because it yields an attractive algebraic law.

Required questions:

- Is the projection invariant under renaming of leaf labels?
- Does it preserve generativity?
- Which distinctions does it deliberately erase?
- Can current PGH rules justify erasing exactly those distinctions?
- Could a different syntax-only projection remain equally representation-neutral while inducing different coherence laws?

### E7 — Variable-arity / relational translation test

Test whether the projection idea can be stated without privileging total binary operations.

At minimum, compare:

- binary-tree presentations;
- flat ordered `n`-ary presentations;
- relational formation presentations with auxiliary nodes.

The operation must record whether a common invariant can be defined without an additional arbitrary translation map.

## Finite-model requirements

At minimum:

1. enumerate all 16 binary operations on a two-element carrier;
2. verify the exact count coherent with P1;
3. verify the exact count coherent with P2;
4. verify the exact count coherent with P3 for the declared finite presentation scope;
5. provide at least one operation separating each non-equivalent coherence class where feasible.

Computational enumeration is validation, not the proof itself.

## Outcome space

```text
A = OUTCOME_INDEPENDENT_EQUIVALENCE_IS_DEFINED_AND_CURRENT_PGH_UNIQUELY_PRIVILEGES_ONE_NONTRIVIAL_PROJECTION
B = OUTCOME_INDEPENDENT_EQUIVALENCE_IS_DEFINED_BUT_PROJECTION_SELECTION_REMAINS_UNDERDETERMINED
C = ONLY_OPERATION_DEPENDENT_EQUIVALENCE_CAN_BE_DEFINED
D = PROJECTION_METHOD_FAILS_OUTSIDE_BINARY_PRESENTATIONS
E = CURRENT_BASELINE_REQUIRES_REPAIR
F = UNRESOLVED
```

Outcome labels are descriptive, not rankings.

## Nontriviality audit

Apply N0–N9 where meaningful.

Special attention:

```text
N1_UNIVERSAL_ENCODING
N2_NO_SMUGGLING
N3_NONUNIVERSAL_EXCLUSION
N4_REPRESENTATION_INVARIANCE
N6_GENERATIVE_COMPRESSION
N7_INDEPENDENT_CONSEQUENCE
N8_COUNTEREXAMPLE_EXPOSURE
N9_RELABELING_INVARIANCE
```

N10 remains out of scope.

## Required outputs

Create at minimum:

```text
research/formalizations/PGH0_REPRESENTATION_EQUIVALENCE_COHERENCE_ADJUDICATION_0_1_0.md
handoffs/PGH0_REPRESENTATION_EQUIVALENCE_AND_COHERENCE_CHALLENGE_HANDOFF_0_1_0.md
```

Create versioned derivation and failure artifacts for material results.

Do not update canonical registries or `CURRENT_STATE.md` on the scientific branch.

## Hard stop

Stop before:

- declaring a projection physically fundamental;
- declaring associativity or commutativity physical;
- source intake;
- empirical interpretation;
- physical bridge work;
- FCP mutation;
- beginning a successor scientific operation;
- mutating canonical `main` before independent review.

## Review boundary

The scientific candidate should use exactly two commits:

```text
COMMIT_1_MESSAGE = Preregister PGH-0 representation equivalence challenge
COMMIT_2_MESSAGE = Adjudicate PGH-0 representation equivalence challenge
```

Commit 1 contains only this preregistration. Commit 2 contains only the adjudication, required derivation/failure artifacts, and the handoff.
