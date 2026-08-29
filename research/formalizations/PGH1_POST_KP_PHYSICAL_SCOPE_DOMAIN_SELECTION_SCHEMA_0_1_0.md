# PGH-OBJ-0038 — Post-Kp Physical Scope / Domain-Selection Schema 0.1.0

## Status

```text
OBJECT_ID = PGH-OBJ-0038
OBJECT_CLASS = PHYSICAL_SCOPE_ACCOUNTING_SCHEMA
STATUS = QUALIFIED_POST_RESULT_METHOD_SCHEMA
PARENT_GRAMMAR = PGH-GRAM-0008
PARENT_BRIDGE = PGH-OBJ-0035
PARENT_TARGET_PROTOCOL = PGH-OBJ-0036
FIRST_EMPIRICAL_FAILURE = PGH-FAIL-0035
PHYSICAL_LAW_CLAIM = NONE
```

## Purpose

Keep four logically distinct layers separate when a formal grammar is exposed to multiple physical targets:

```text
G = FORMAL_GRAMMAR_MODEL_CLASS
J = SEMANTIC_REALIZATION_SCHEMA
T = EMPIRICAL_TARGET_SELECTION_PROTOCOL
S = PHYSICAL_SCOPE_PREDICATE
```

The Kp result exposed that the first three do not automatically determine the fourth.

## Layer G — grammar

`G` defines the formal model class and its consequences.

For `PGH-GRAM-0008`, `G` contains the sparse chain factorization and implies conditional independence.

`G` alone does not say which physical systems instantiate it.

## Layer J — semantic realization

`J` states how the formal model class is realized as a candidate empirical model class while preserving the grammar's restriction and avoiding semantic model-subset selection.

A conditional statement of the form

```text
IF_X_IS_A_VALID_REALIZATION_OF_G_THROUGH_J
THEN_X_MUST_SATISFY_THE_TRANSPORTED_RESTRICTION
```

does not itself specify which physical `X` satisfy the antecedent.

## Layer T — target selection

`T` is a procedure for selecting an empirical confrontation without using the predicted result.

It may use measurement architecture, access, support, ordering, contamination, and other preregistered metadata.

`T` can make a test prospective and nonleaking while still leaving physical-scope membership conceptually open.

Therefore:

```text
NONLEAKING_TARGET_SELECTION != PHYSICAL_SCOPE_THEORY
```

## Layer S — physical scope

A physical scope predicate `S(X)` answers:

> Is physical system/record architecture `X` claimed to be governed by this candidate grammar?

For scope-sensitive cross-target claims, `S` is scientifically substantive auxiliary structure.

A scope rule can be broad, narrow, or universal, but its provenance must remain visible.

## Pre-result scope rule

A pre-result scope rule qualifies for prospective credit only if it can classify candidate systems without using the empirical behavior later predicted by the grammar.

Schematically:

```text
CANDIDATE_IDENTITY = (G, J, S)
TARGET_SELECTION = T conditioned on S
OUTCOME_OBSERVED_ONLY_AFTER_G_J_S_T_ARE_FIXED
```

`S` may not be secretly equivalent to the target restriction.

## Post-result scope revision

Suppose a target `X` was validly frozen and the candidate restriction fails on `X`.

A new predicate `S'` introduced afterward may define a scientifically legitimate revised hypothesis, but:

```text
S_PRIME_CANNOT_CHANGE_THE_OLD_VERDICT
S_PRIME_CANNOT_MAKE_X_RETROACTIVELY_INVALID
S_PRIME_CANNOT_RECEIVE_PRE_RESULT_PREDICTIVE_CREDIT
```

The revised candidate must carry explicit post-result provenance, for example:

```text
NEW_CANDIDATE_IDENTITY = (G, J, S_PRIME)
```

or a correspondingly revised grammar/bridge identity if the change is deeper.

## Circular scope rules

The following are disallowed as explanatory scope selectors when they merely restate the tested consequence:

```text
S(X) := X_SATISFIES_A_INDEPENDENT_OF_C_GIVEN_B
S(X) := X_IS_FIRST_ORDER_MARKOV
S(X) := X_IS_WELL_FIT_BY_THE_TESTED_SPARSE_CHAIN
```

Such predicates can define mathematical subclasses, but they do not explain why those subclasses are the intended physical domain of the grammar.

## Scope and target failure

A failed target can have different meanings depending on what was frozen before the test:

### Case 1 — pre-result scope includes target

The failure is adverse within the declared physical scope.

### Case 2 — pre-result scope excludes target but target was nevertheless frozen

A provenance/protocol inconsistency must be resolved; the target cannot simply be erased.

### Case 3 — no pre-result physical scope exists

The target failure remains valid for the frozen instantiation, while generalization to other domains is underdetermined. Any later scope narrowing is a new hypothesis revision.

### Case 4 — candidate was explicitly universal

The failure counts against the universal candidate at the declared scope, subject to its auxiliary assumptions.

## PGH-GRAM-0008 classification

The post-Kp audit places the existing candidate in Case 3:

```text
FORMAL_SCOPE = EXACT
PHYSICAL_SCOPE = NOT_PRE_KP_QUALIFIED
FIRST_EMPIRICAL_INSTANTIATION = VALIDLY_FROZEN_AND_REFUTED
```

## Claim ceiling

```text
SCOPE_ACCOUNTING_SCHEMA = QUALIFIED
PHYSICAL_SCOPE_FOR_PGH_GRAM_0008 = NOT_RETROACTIVELY_SUPPLIED
NEW_SCOPE_BEARING_CANDIDATE = NOT_CREATED
SECOND_TARGET = NOT_SELECTED
PHYSICAL_LAW_DERIVED = NO
R2B = UNSATISFIED
FCP_EFFECT = NONE
```
