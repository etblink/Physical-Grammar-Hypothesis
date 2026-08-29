# PGH-0 Minimal Grammar Challenge — Preregistration 0.1.0

## Status

```text
OPERATION_ID = PGH0_MINIMAL_GRAMMAR_CHALLENGE
REGISTRY_ID = PGH-OP-0003
OPERATION_CLASS = FOUNDATIONAL_FORMALIZATION
STATUS = PREREGISTERED_IN_PROGRESS
CANONICAL_BASE = ac6baff2596eedbe3902b07dfe5e5ee2e69ac918
WORKING_BRANCH = research/pgh0-minimal-grammar-challenge
SOURCE_BOUND_STATUS = NOT_YET_SOURCE_BOUND
NEW_SOURCE_SEARCH = FORBIDDEN
PHYSICAL_INTERPRETATION = NOT_AUTHORIZED_AS_A_RESULT
```

## Purpose

This operation tests the opening candidate primitive shell

```text
PGH-GRAM-0001 = {DISTINGUISH, COMPOSE, IDENTIFY}
```

without assuming that any member is primitive, independent, minimal, sufficient, or physical.

The target is the weakest coherent formal structure that preserves a genuinely generative notion of grammar while exposing every meta-mathematical assumption used to define it.

The operation may establish a negative result. Failure of the three-primitive proposal is an acceptable and scientifically informative outcome.

## Hard scientific boundary

This operation may:

- define minimal formal objects and relations;
- test removal of `IDENTIFY`;
- test removal of `DISTINGUISH`;
- test whether binary `COMPOSE` is fundamental or merely one representation of a more general formation relation;
- derive purely formal consequences;
- construct explicit mathematical countermodels;
- apply N0–N9 from `NONTRIVIALITY_TESTS.md` where possible;
- record failed derivations and unresolved burdens;
- propose a successor candidate grammar identity if scientifically required.

It may not:

- search for or admit external sources;
- claim a physical law from formal analogy;
- identify derivational order with time;
- identify compositional locality with physical locality;
- identify contextual equivalence with gauge symmetry;
- identify matched interfaces with conservation;
- identify relabeling invariance with a physical symmetry group;
- import probability, geometry, causal order, spacetime, quantum theory, fields, particles, energy, momentum, charge, measurement, observers, or information as physical primitives;
- claim empirical support;
- change FCP;
- treat category theory or any other mathematical formalism as privileged ontology merely because it conveniently represents the result.

## Meta-mathematical versus object-level structure

This operation explicitly distinguishes the metalanguage used to reason from the candidate grammar being studied.

Permitted metalanguage includes ordinary mathematical logic, finite sets or classes of formal symbols, equality of mathematical expressions, quantification, finite trees, relations, and proof by counterexample.

These are bookkeeping resources of the analysis and are not thereby promoted to physical primitives.

Any result that depends essentially on a metalanguage choice must disclose that dependence.

## Ordered minimality tests

The result may not skip this order.

### M1 — Remove IDENTIFY

Question:

> Can grammar-internal equivalence be defined from compositional or contextual behavior alone, without an independent object-level `IDENTIFY` primitive?

Required burden:

- define the relevant class of contexts;
- define contextual profile or substitutability without physical observables;
- determine whether the induced relation is an equivalence relation;
- determine whether it is compatible with the formation relation;
- state exactly what is lost if only contextually visible distinctions are retained.

No result may claim gauge invariance or physical equivalence from this test.

### M2 — Remove DISTINGUISH

Question:

> Once contextual equivalence is available, can grammatical distinction be defined as non-equivalence or differential contextual behavior, rather than as an independent primitive?

Required burden:

- separate literal metalanguage inequality from grammar-internal discernibility;
- identify whether purely haecceitic label differences survive;
- disclose any extensionality principle used to discard contextually invisible labels.

### M3 — Remove COMPOSE

Question:

> Can a generative grammar survive without an object-level formation/composition relation or an equivalent generative mechanism?

Required burden:

- distinguish the necessity of *some* generative relation from the stronger claim that binary composition is fundamental;
- test whether arity, directionality, determinism, associativity, commutativity, identities, inverses, typing, boundaries, or category structure have been smuggled in;
- permit the conclusion that `COMPOSE` is only a placeholder for a weaker `FORMATION` or `GENERATIVE_RELATION` primitive.

### M4 — Dependency audit

For each surviving object-level primitive or rule report:

```text
PRIMITIVE_DEPENDENCIES
RULE_DEPENDENCIES
LEMMA_DEPENDENCIES
SEMANTIC_ASSUMPTIONS
PHYSICAL_ASSUMPTIONS
SOURCE_DEPENDENCIES
METALANGUAGE_DEPENDENCIES
```

### M5 — Relabeling / automorphism audit

Determine which claims survive arbitrary bijective renaming of formal labels.

A representation-dependent feature may not be promoted to deep grammatical structure.

## Weakest permitted formalization family

The operation should begin weaker than a partial binary function.

A permitted initial shell is a nonempty formal carrier `A` together with a formation relation such as

\[
R \subseteq A \times A \times A,
\]

where `R(a,b,c)` means only that `a` and `b` may participate in a formal formation yielding `c`.

This notation does NOT assume:

```text
PHYSICAL_OBJECTS = NO
INPUT_OUTPUT_CAUSALITY = NO
TEMPORAL_ORDER = NO
UNIQUE_OUTPUT = NO
ASSOCIATIVITY = NO
COMMUTATIVITY = NO
IDENTITY_ELEMENTS = NO
INVERSES = NO
BOUNDARIES = NO
TYPES = NO
CATEGORY_STRUCTURE = NO
```

The operation may weaken this shell further if binary arity or ordered inputs prove representational rather than structural.

## Contextual-equivalence candidate

A context may be represented formally as a finite formation pattern with exactly one replaceable occurrence and otherwise fixed formal labels.

For candidate element `a`, define its grammatical context profile only through whether substitution yields a well-formed pattern.

A candidate equivalence may then take the schematic form

\[
a \equiv_G b
\quad\Longleftrightarrow\quad
\forall C[-],\; \mathrm{WF}(C[a]) \leftrightarrow \mathrm{WF}(C[b]).
\]

This is a preregistered candidate definition, not a result.

The operation must test whether it is sufficiently strong to make the quotient formation relation well defined.

## Nontriviality suite

Apply N0–N9 from `NONTRIVIALITY_TESTS.md` where meaningful.

Special attention is required for:

```text
N0_FORMAL_DEFINABILITY
N1_UNIVERSAL_ENCODING
N2_NO_SMUGGLING
N3_NONUNIVERSAL_EXCLUSION
N5_SEMANTIC_LOAD
N6_GENERATIVE_COMPRESSION
N7_INDEPENDENT_CONSEQUENCE
N8_COUNTEREXAMPLE_EXPOSURE
N9_RELABELING_INVARIANCE
```

N10 remains not applicable unless a nontrivial formal consequence survives and a separate physical bridge is later authorized.

## Outcome space

The operation may conclude any of the following:

```text
A = THREE_PRIMITIVES_REMAIN_INDEPENDENT
B = IDENTIFY_DERIVED_BUT_DISTINGUISH_AND_COMPOSE_REMAIN
C = IDENTIFY_AND_DISTINGUISH_DERIVED__GENERATIVE_RELATION_REMAINS
D = ALL_THREE_REFORMULATED_INTO_A_DIFFERENT_WEAKER_CORE
E = CANDIDATE_CORE_FORMALLY_INCOHERENT
F = CANDIDATE_CORE_FORMALLY_COHERENT_BUT_TRIVIAL_ENCODING
G = UNRESOLVED
```

These outcome labels are not rankings.

A minimality result is distinct from a physical-success result.

## Counterexample requirement

At least one explicit finite countermodel or witness structure must be constructed for every material claim that a rule is necessary, sufficient, or independent whenever such a countermodel is feasible.

The project should prefer a small finite witness over verbal intuition.

## Scientific stop rule

The operation must stop before claiming that any formal result is a law of nature.

Even a successful formal reduction leaves:

```text
PHYSICAL_BRIDGE = UNESTABLISHED
EMPIRICAL_SUPPORT = NONE
```

unless separately authorized later.

## Required outputs

The operation should create at minimum:

```text
research/formalizations/PGH0_MINIMAL_GRAMMAR_FORMALIZATION_0_1_0.md
research/derivations/PGH_DERIVATION_CONTEXTUAL_EXTensional_REDUCTION_0_1_0.md
handoffs/PGH0_MINIMAL_GRAMMAR_CHALLENGE_HANDOFF_0_1_0.md
```

If a proposed derivation fails, create a versioned record under `research/failures/` rather than silently dropping it.

The operation may update mutable current-state surfaces and structured registries as required by the result, but it must not rewrite the opening charter or historical versioned artifacts.

## Integration boundary

Substantive scientific work is performed on the research branch.

Canonical `main` is not to be advanced merely because a local or remote research candidate exists.

The final candidate must first be internally qualified and its exact result reported for Project Lead/user review.
