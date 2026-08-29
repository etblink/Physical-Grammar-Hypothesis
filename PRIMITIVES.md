# PRIMITIVES

## 1. Status

This file records candidate primitives for PGH-0.

Nothing in this file is yet a finalized axiom of a physical grammar.

```text
PRIMITIVE_SET_STATUS = PROVISIONAL_UNDER_REDUCTION
CURRENT_CANDIDATE_COUNT = 3
MINIMALITY_ESTABLISHED = NO
SUFFICIENCY_ESTABLISHED = NO
PHYSICAL_INTERPRETATION_ESTABLISHED = NO
```

## 2. Initial conceptual list

The first conceptual decomposition used five notions:

```text
DISTINCTION
BOUNDARY
COMPOSITION
TRANSFORMATION
EQUIVALENCE
```

These were chosen because a grammar plausibly needs some account of difference, admissible joining, change or derivation, and sameness under alternate description.

The list was not claimed to be minimal.

## 3. Current reduction hypothesis

The present conjecture is that a smaller candidate set may suffice:

\[
\{\text{DISTINGUISH},\text{COMPOSE},\text{IDENTIFY}\}.
\]

The working idea is:

- boundaries might arise from conditions on partial composability;
- transformations might be representable as structured compositions or relations;
- context may arise from compositional embedding;
- equivalence may be represented by `IDENTIFY`.

None of those reductions is yet proven.

## 4. Candidate primitive P1 — DISTINGUISH

### Informal role

`DISTINGUISH` supplies the possibility that two grammatical positions, states, terms, or structures are not interchangeable.

At minimum, a nontrivial grammar seems to require some notion of difference.

### Current danger

The word “distinguish” may secretly presuppose:

- a pre-existing set of objects;
- an observer;
- information;
- measurement;
- identity through time;
- binary logic.

None of these may be imported silently.

### PGH-1 burden

Define a notion of distinction weak enough that it does not presuppose the physical ontology the grammar is supposed to generate.

Possible directions for later examination include primitive inequality, discernibility by relation, or distinguishability by compositional behavior, but no option is currently selected.

```text
DISTINGUISH_FORMAL_DEFINITION = OPEN
DISTINGUISH_PRIMITIVE_STATUS = CANDIDATE
```

## 5. Candidate primitive P2 — COMPOSE

### Informal role

`COMPOSE` represents the possibility that some structures can combine to form another admissible structure.

Composition should probably be partial rather than universal: some things may compose and others may not.

### Current danger

Composition may secretly import:

- spatial adjacency;
- temporal succession;
- causal order;
- typed interfaces;
- boundaries;
- associativity;
- directionality;
- a category-theoretic formalism.

None is assumed merely from the word “compose.”

### PGH-1 burden

Define the weakest possible compositional operation or relation and determine which familiar properties, if any, must be assumed versus derived.

In particular:

```text
ASSOCIATIVITY = NOT_ASSUMED
COMMUTATIVITY = NOT_ASSUMED
IDENTITY_ELEMENT = NOT_ASSUMED
INVERSES = NOT_ASSUMED
DIRECTIONAL_COMPOSITION = NOT_ASSUMED
TYPED_BOUNDARIES = NOT_ASSUMED
CATEGORY_STRUCTURE = NOT_ASSUMED
```

```text
COMPOSE_FORMAL_DEFINITION = OPEN
COMPOSE_PRIMITIVE_STATUS = CANDIDATE
```

## 6. Candidate primitive P3 — IDENTIFY

### Informal role

`IDENTIFY` represents the possibility that two expressions or structures count as the same for the grammar despite not being literally identical descriptions.

This is the candidate ancestor of equivalence, synonymy, gauge-like redundancy, or representation independence.

### Current danger

`IDENTIFY` may simply stipulate the equivalence relation needed to recover known physics.

It may also be redundant if equivalence can instead be defined as indistinguishability under every admissible compositional context.

### PGH-1 burden

Test whether `IDENTIFY` can be derived from contextual substitutability.

A possible future criterion is:

\[
A \equiv B
\quad\text{iff}\quad
C[A] \text{ and } C[B] \text{ are indistinguishable for every admissible context } C.
\]

This expression is exploratory only. “Context,” “admissible,” and “indistinguishable” are not yet formally fixed.

```text
IDENTIFY_FORMAL_DEFINITION = OPEN
IDENTIFY_PRIMITIVE_STATUS = CANDIDATE
IDENTIFY_POSSIBLY_DERIVED = YES
```

## 7. Candidate derived notion — BOUNDARY

The initial idea that composable structures might have matched interfaces can be represented schematically as

\[
A:x\to y,\qquad B:y\to z,
\]

with composite

\[
B\circ A:x\to z.
\]

This notation is useful but potentially dangerous because it already imports typed directional boundaries.

Therefore:

```text
BOUNDARY = NOT_YET_DERIVED
TYPED_INTERFACE = NOT_ASSUMED
INPUT_OUTPUT_DIRECTION = NOT_ASSUMED
```

The PGH-1 question is whether boundary-like structure emerges necessarily from partial composition or must be inserted independently.

## 8. Candidate derived notion — TRANSFORMATION

A prior conceptual picture used derivations such as

\[
X_0 \Rightarrow X_1 \Rightarrow X_2.
\]

This was noted as potentially analogous to physical history.

It is not yet known whether transformation must be primitive or can be represented as a compositional relation within a static grammar.

Therefore:

```text
TRANSFORMATION = NOT_YET_DERIVED
DERIVATIONAL_ORDER = NOT_PHYSICAL_TIME
```

## 9. Candidate derived notion — CONTEXT

A context may eventually be represented as a larger compositional structure containing a replaceable position.

If so, contextual substitutability may help define equivalence.

But this is not yet established.

```text
CONTEXT = NOT_YET_DERIVED
CONTEXTUAL_EQUIVALENCE = CANDIDATE_TEST
```

## 10. Anti-import firewall

The following must not be smuggled into primitive definitions:

```text
OBSERVER = NOT_ASSUMED
MEASUREMENT = NOT_ASSUMED
INFORMATION = NOT_ASSUMED
SPACE = NOT_ASSUMED
TIME = NOT_ASSUMED
CAUSALITY = NOT_ASSUMED
LOCALITY = NOT_ASSUMED
PROBABILITY = NOT_ASSUMED
GEOMETRY = NOT_ASSUMED
DIMENSION = NOT_ASSUMED
QUANTUM_MECHANICS = NOT_ASSUMED
FIELD = NOT_ASSUMED
PARTICLE = NOT_ASSUMED
ENERGY = NOT_ASSUMED
MOMENTUM = NOT_ASSUMED
CONSERVATION = NOT_ASSUMED
SYMMETRY_GROUP = NOT_ASSUMED
CATEGORY_THEORY = NOT_ASSUMED_AS_FOUNDATIONAL
```

If a formal definition requires one of these, the project must record that dependency explicitly.

## 11. Tempting analogies currently quarantined

### 11.1 Boundary matching and conservation

Matched interfaces may resemble conservation-like bookkeeping.

Current status:

```text
CONSERVATION_ANALOGY = NOT_A_DERIVATION
```

No claim has been made that energy, momentum, charge, or any physical conserved quantity follows from grammatical composition.

### 11.2 Derivational order and time

A sequence of grammatical rewrites may resemble temporal evolution.

Current status:

```text
TIME_ANALOGY = NOT_A_DERIVATION
```

### 11.3 Contextual equivalence and gauge/representation invariance

Substitutability without external change may resemble gauge redundancy or representation independence.

Current status:

```text
GAUGE_ANALOGY = NOT_A_DERIVATION
```

### 11.4 Renaming invariance and symmetry

Physical irrelevance of arbitrary labels may resemble symmetry under relabeling.

Current status:

```text
SYMMETRY_ANALOGY = NOT_A_DERIVATION
```

## 12. Minimality tests

The candidate set should be challenged in this order:

### M1 — Remove IDENTIFY

Can equivalence be defined entirely through compositional indistinguishability?

If yes, reduce the primitive set.

### M2 — Remove DISTINGUISH

Can distinction itself be defined through nonidentical compositional behavior?

If yes, reduce further.

### M3 — Remove COMPOSE

Can any notion of grammar or generativity survive without composition or an equivalent relation?

If yes, clarify what is actually primitive.

### M4 — Dependency audit

For each surviving primitive, list every concept required to define it and test whether the definition is circular.

### M5 — Automorphism/renaming test

Determine what, if anything, remains invariant under arbitrary renaming of primitive symbols.

This may expose which features are structural and which depend only on notation.

## 13. Current next question

The immediate target is not to derive physics.

It is:

> Can `DISTINGUISH`, `COMPOSE`, and `IDENTIFY` be defined coherently without hidden physical content, and can one of them be eliminated?

Only after that should the project test whether the resulting structure implies a nontrivial exclusion.