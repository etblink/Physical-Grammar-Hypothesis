# PGH-FAIL-0018 — Meta-Framework Neutrality as Rule Selection 0.1.0

## Status

```text
FAILURE_ID = PGH-FAIL-0018
DERIVATION_STATUS = FAILED_PRESERVED
FAILURE_CLASS = UNDERDETERMINED
PHYSICAL_CLAIM = NONE
```

## Failed claim

> A sufficiently abstract, invariant, categorical, or logic-independent meta-framework thereby selects the structural rule package that should govern admissibility.

This claim fails at current source-bound scope.

## Source-bound reason

The frozen SG3 corpus contains mature frameworks with strong abstraction and translation properties that are deliberately compatible with multiple object logics.

Examples include:

```text
INSTITUTIONS / GENERAL_LOGICS -> multiple concrete logics under one abstract architecture
LOGICAL_FRAMEWORKS -> multiple object logics encoded in one metalanguage
CATEGORICAL_LOGIC -> logical structure relative to categorical assumptions
DISPLAY_LOGIC -> multiple logics inside one structural proof architecture
SUBSTRUCTURAL_LOGIC -> multiple logics from distinct structural-rule packages
```

Therefore:

\[
\boxed{\text{meta-framework organization} \not\Rightarrow \text{unique rule-package selection}}
\]

## Control 1 — institution neutrality

Institution theory abstracts over signatures, sentences, models, and satisfaction while supporting many concrete logics.

Its representation discipline does not make one concrete logic the unique inhabitant of the framework.

## Control 2 — logical-framework neutrality

LF fixes a powerful dependent-type metalanguage, but object-logical constants, judgments, rules, and axioms remain encoded data.

Thus:

```text
ONE_META_LANGUAGE = YES
ONE_OBJECT_LOGIC_SELECTED = NO
```

## Control 3 — categorical conditionality

Categorical structure can generate or interpret logical operations.

But the structure required—cartesian, closed, fibred, contextual, topos-like, monoidal, etc.—is itself substantive input.

Calling the induced logic structural does not explain why that base structure is privileged.

## Control 4 — structural-rule plurality

Substructural proof theory supplies coherent systems with differing exchange, weakening, contraction, order, and resource behavior.

Their existence blocks any inference from “structural rules matter” to “one structural package is automatically forced.”

## What the failure does not establish

```text
UNIQUE_META_GRAMMAR_IMPOSSIBLE = NO
PHYSICAL_SELECTOR_IMPOSSIBLE = NO
CATEGORICAL_ROUTE_USELESS = NO
LOGICAL_FRAMEWORKS_USELESS = NO
INSTITUTION_THEORY_USELESS = NO
PGH_FALSE = NO
```

It establishes only:

```text
NEUTRAL_OR_INVARIANT_META_FRAMEWORK_ALONE_IS_NOT_RULE_SELECTION = YES
```

## Relation to PGH-FAIL-0017

`PGH-FAIL-0017` established internally that canonical/free/invariant meta-language constructions relocate the origin problem into signatures, projections, symmetries, or primitives.

This source-bound failure strengthens that result by showing the same distinction is endemic in established meta-logic:

```text
FRAMEWORK_LEVEL_INVARIANCE_AND_REUSE = MATURE
OBJECT_LOGIC_OR_STRUCTURAL_PACKAGE_VARIABILITY = ALSO_MATURE
```

## Preservation reason

This failure prevents future PGH work from claiming that adoption of an institution, logical framework, categorical semantics, or general proof architecture has solved the selective-rule-origin burden merely because the framework is elegant, universal, or representation independent.

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = [PGH-OBJ-0016]
RULE_DEPENDENCIES = [PGH-FAIL-0017]
LEMMA_DEPENDENCIES = []
SEMANTIC_ASSUMPTIONS = NONE
PHYSICAL_ASSUMPTIONS = NONE
SOURCE_DEPENDENCIES = [SG3-001..SG3-019]
```
