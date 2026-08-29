# NONTRIVIALITY TESTS

## 1. Purpose

This file defines the tests a candidate Physical Grammar Hypothesis must survive before the project treats it as more than a redescription of known physics or a universal formal encoding.

At PGH-0 these are research tests, not completed results.

```text
NONTRIVIALITY_TEST_SUITE_VERSION = 0.1.0
COMPLETE_PASS = NO
```

## 2. N0 — Formal definability

### Question

Can the candidate grammar be stated precisely enough that independent readers could determine whether a proposed structure is grammatical or ungrammatical?

### Failure modes

- key terms remain metaphorical;
- admissibility is decided case by case;
- physical intuition is required to interpret the production rules;
- the grammar cannot be separated from its examples.

### Current status

```text
N0_FORMAL_DEFINABILITY = NOT_TESTED
```

## 3. N1 — Universal-encoding test

### Question

Could essentially any desired physical theory be reproduced merely by changing the grammar rules to encode that theory?

If yes, the existence of a grammar is trivial.

### Pass burden

A candidate should reveal why one restricted family of structures is privileged by the grammar rather than merely demonstrating that formal systems can encode arbitrary laws.

### Current status

```text
N1_UNIVERSAL_ENCODING = NOT_TESTED
```

## 4. N2 — No-smuggling audit

### Question

Does substantive physical content enter through any of the following?

- primitive definitions;
- typing conditions;
- composition rules;
- boundary rules;
- rewrite rules;
- semantic interpretation;
- initial conditions;
- choice of allowed objects;
- equivalence relation;
- background mathematical structure.

### Pass burden

Any substantive imported content must be declared. A claimed derivation fails if its conclusion is already present in equivalent form among its assumptions.

### Current status

```text
N2_NO_SMUGGLING = NOT_TESTED
```

## 5. N3 — Nonuniversal exclusion test

### Question

Does the candidate grammar exclude at least one mathematically describable structure that is not excluded merely by a definition equivalent to the desired physical conclusion?

### Pass burden

There must exist at least one `X` such that:

\[
X \text{ is mathematically specifiable}
\]

but

\[
G \nvdash X \text{ as well formed}.
\]

The exclusion must follow from the grammar rather than from an independently inserted physical prohibition.

### Current status

```text
N3_NONUNIVERSAL_EXCLUSION = NOT_TESTED
```

## 6. N4 — Representation-invariance test

### Question

Does the candidate deep grammatical structure survive faithful reformulation into genuinely different mathematical surface languages?

### Failure modes

- a “fundamental” feature exists only in one notation;
- equivalent formulations induce incompatible deep grammars;
- the invariant can be recovered only by privileging one representation.

### Open burden

A precise definition of faithful translation is still required.

### Current status

```text
N4_REPRESENTATION_INVARIANCE = NOT_TESTED
```

## 7. N5 — Semantic-load audit

### Question

How much physical selection is performed by the grammar itself, and how much is deferred to the interpretation map from grammar to physics?

### Failure condition

If the semantics map must encode the substantive equations, dynamical laws, allowed histories, or empirical structure, then the grammar has not explained them.

### Current status

```text
N5_SEMANTIC_LOAD = NOT_TESTED
```

## 8. N6 — Generative-compression test

### Question

Is the candidate grammar materially simpler than the space of structures it accounts for?

### Pass burden

The grammar should produce broad structured consequences from a comparatively compact rule system.

At PGH-0 no exact complexity measure is mandated.

Possible later measures may include description length or related formal complexity notions, but those are not yet adopted.

### Current status

```text
N6_GENERATIVE_COMPRESSION = NOT_TESTED
```

## 9. N7 — Independent-consequence test

### Question

Does at least one nontrivial restriction follow that was not inserted as a known physical law or equivalent assumption?

This is the key transition from architecture to explanatory content.

### Pass burden

A derivation must show:

1. exact assumptions;
2. exact grammatical rules;
3. exact derived restriction;
4. why the restriction was not contained in the assumptions by definition;
5. what mathematical structures are thereby excluded;
6. what, if anything, would make the result physically meaningful.

### Current status

```text
N7_INDEPENDENT_CONSEQUENCE = NOT_TESTED
```

## 10. N8 — Counterexample exposure test

### Question

Can the candidate grammar fail in a definite way?

### Pass burden

The candidate should expose at least one of:

- a mathematical countermodel;
- an equivalent representation in which the alleged invariant disappears;
- a structure the grammar wrongly excludes;
- an observation the grammar declares impossible;
- an internal inconsistency;
- dependence on an undeclared assumption.

A proposal insulated from all counterexamples by reinterpretation fails this test.

### Current status

```text
N8_COUNTEREXAMPLE_EXPOSURE = NOT_TESTED
```

## 11. N9 — Relabeling / automorphism test

### Question

Which features survive arbitrary renaming of primitive symbols or structurally irrelevant labels?

### Purpose

This test separates possible structural content from features created by notation or naming conventions.

### Warning

Invariance under renaming is not by itself a physical symmetry law.

### Current status

```text
N9_RELABELING_INVARIANCE = NOT_TESTED
```

## 12. N10 — Physical bridge test

This test applies only after a nontrivial formal consequence has survived N0–N9.

### Question

Is there a noncircular bridge from the grammatical result to physical possibility?

### Pass burden

The project must explain why the derived grammatical exclusion corresponds to a physical exclusion rather than merely a feature of the chosen formal system.

If the bridge requires importing the physical conclusion independently, the test fails.

### Current status

```text
N10_PHYSICAL_BRIDGE = NOT_APPLICABLE_YET
```

## 13. Result classes

For future candidate grammars, each test should receive one of:

```text
PASS
PARTIAL
FAIL
NOT_TESTED
NOT_APPLICABLE
```

No scalar score should be used.

## 14. Candidate-level outcome

A candidate grammar may be classified as:

```text
TRIVIAL_ENCODING
FORMALLY_INTERESTING_NONPHYSICAL
NONTRIVIAL_FORMAL_CANDIDATE
PHYSICAL_BRIDGE_UNESTABLISHED
PHYSICALLY_TESTABLE_CANDIDATE
REFUTED_CANDIDATE
UNRESOLVED
```

These labels are descriptive and may be revised as the project matures.

## 15. Opening PGH-0 gate

Before PGH should advance from conceptual formulation toward a claimed nontrivial derivation, require at minimum:

```text
N0_FORMAL_DEFINABILITY = PASS
N1_UNIVERSAL_ENCODING != FAIL
N2_NO_SMUGGLING = PASS
N3_NONUNIVERSAL_EXCLUSION = PASS
N5_SEMANTIC_LOAD != FAIL
N7_INDEPENDENT_CONSEQUENCE = PASS
N8_COUNTEREXAMPLE_EXPOSURE = PASS
```

Representation-invariance testing may require later formal examples, but any known representation dependence must be disclosed immediately.

## 16. Failed-derivation record template

When a derivation fails, record:

```text
DERIVATION_ID =
DATE =
CLAIMED_RESULT =
ASSUMPTIONS =
FAILURE_TEST =
FAILURE_CLASS =
HIDDEN_IMPORT_IF_ANY =
WHAT_REMAINS_VALID =
SUPERSESSION_STATUS =
```

Do not delete the failed argument merely because a better one is later found.