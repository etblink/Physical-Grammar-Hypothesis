# PGH-1 R2 Primitive Grammar Candidate Family Screen 0.1.0

## Identity

```text
OPERATION_ID = PGH1_R2_PRIMITIVE_GRAMMAR_CANDIDATE_FAMILY_SCREEN
REGISTRY_ID = PGH-OP-0048
CANONICAL_BASE = 86c97f110b8b1b8d85e7d0c08d4e5352cd857aff
PREREGISTRATION_COMMIT = 65dd9975cabc70f29267fb3c971be254dd97051c
CANDIDATE_STANDARD = PGH-OBJ-0020
R2_TARGET = PGH-OBJ-0021
NEW_SOURCE_SEARCH = NONE
PHYSICAL_FIT = NONE
FCP_EFFECT = NONE
```

## Outcome

```text
OUTCOME = A__THE_FROZEN_DOCTRINE_FAMILY_CONTAINS_MULTIPLE_NONTRIVIAL_FORMAL_PRIMITIVE_GRAMMAR_CANDIDATES_UNDER_PGH_OBJ_0020__NO_PHYSICAL_RANKING_OR_R2B_CREDIT_FOLLOWS
FORMAL_CANDIDATE_GRAMMARS = 5
R2C_FORMAL_CANDIDACY = PASS_FOR_FROZEN_FAMILY
R2B = UNSATISFIED
PHYSICAL_GRAMMAR_FOUND = NO
```

## Independent-review correction

An initial unintegrated candidate classified a doctrine without a fixed generator seed as an incomplete grammar shell.

That was too strong.

For formal candidacy a grammar may be an axiom/doctrine system whose well-formed structures are its models:

\[
W(G)=\{X:X\models G\}.
\]

A finite generator seed is **not** required by `PGH-OBJ-0020`.

The relevant distinction is instead:

```text
BROAD_FIXED_MODEL_CLASS != CHANGING_GRAMMAR_RULES
```

and later:

```text
SEMANTIC_OR_MODEL_SELECTION_MAY_NOT_SMUGGLE_THE_TARGET_PHYSICS.
```

Thus seedlessness is not a candidacy blocker. The rejected unintegrated result is preserved conceptually as `PGH-FAIL-0022`.

## Frozen candidate family

The five candidates are now assigned stable candidate identities:

```text
PGH-GRAM-0003 = BARE_MONOIDAL_PRIMITIVE_GRAMMAR_CANDIDATE
PGH-GRAM-0004 = SYMMETRIC_MONOIDAL_PRIMITIVE_GRAMMAR_CANDIDATE
PGH-GRAM-0005 = CARTESIAN_PRIMITIVE_GRAMMAR_CANDIDATE
PGH-GRAM-0006 = COCARTESIAN_PRIMITIVE_GRAMMAR_CANDIDATE
PGH-GRAM-0007 = BICARTESIAN_PRIMITIVE_GRAMMAR_CANDIDATE
```

These are candidate **formal grammars**, not candidate physical theories.

## PGH-OBJ-0020 matrix

### P0 formal definability

```text
PGH-GRAM-0003..0007 = PASS
```

Each candidate has exact doctrine axioms/universal properties defining its model class.

### P1 declared primitives

```text
PASS
```

The doctrine-level primitive structural assumptions are explicit.

### P2 pre-target fixation

```text
PASS
```

The family was frozen from completed PGH formal work before any physical-fit evaluation.

### P3 restricted hypothesis class / universal encoding

```text
PASS_AT_FIXED_GRAMMAR_SCOPE
```

Each grammar is frozen as the doctrine itself. Target-specific generators, relations, equations, response tables, or theory presentations are **not part of the candidate** unless separately preregistered as a different grammar.

The fact that a doctrine has many models does not by itself mean its grammar rules have been changed to encode a target.

However, later selecting a model/interpretation because it reproduces known physics is a semantic-load/physical-bridge issue and earns no current credit.

### P4 no extensional target table

```text
PASS
```

No candidate contains a target response or admissibility table.

### P5 generative compression

```text
PASS_FORMAL
```

Compact doctrine-level assumptions govern entire model classes and generate uniform structural consequences without object-by-object permission lists.

### P6 nontrivial formal exclusion

```text
PASS_FORMAL
```

Each candidate excludes mathematically specifiable structures that fail its doctrine conditions. Stronger candidates additionally force structural consequences such as symmetry, diagonals, terminal maps, codiagonals, or initial maps.

No physical exclusion is claimed.

### P7 representation discipline

```text
PASS_AT_FORMAL_SCOPE
```

The doctrine properties are structural rather than tied to coordinates or naming. Physical representation invariance remains untested.

### P8 law-free semantic boundary

```text
PASS_AT_PRE_BRIDGE_SCOPE
```

The candidates add no response law to `A_ref`.

### P9 independent formal consequence

```text
PASS
```

The completed structural-package gates provide explicit consequences not listed object by object. In particular `PGH-GRAM-0005` and `PGH-GRAM-0006` generate dual universal-property packages.

### P10 counterexample exposure

```text
PASS
```

We have explicit weaker or dual structures that fail each stronger doctrine and therefore function as mathematical countermodels.

### P11 physical bridge

```text
NOT_APPLICABLE_YET
```

No candidate receives physical status.

## Candidate roles without ranking

| Candidate | Formal role | Physical status |
|---|---|---|
| `PGH-GRAM-0003` | weak composition control | none |
| `PGH-GRAM-0004` | exchange/symmetry candidate | none |
| `PGH-GRAM-0005` | product-structural candidate | none |
| `PGH-GRAM-0006` | coproduct-dual candidate | none |
| `PGH-GRAM-0007` | product+coproduct rich control | none |

The roles are experimental bookkeeping, not likelihood judgments.

## Universal-encoding safeguard

The screen does **not** authorize later arbitrary extensions while retaining the same grammar identity.

If target-specific generator/equation data are added, then either:

1. they define a new candidate grammar and must be independently preregistered; or
2. if hidden in semantics/model selection, they receive no grammar-derived explanatory credit.

This prevents doctrine candidacy from becoming a loophole for unrestricted theory encoding.

## Why outcome C does not pass

A doctrine can be a complete abstract formal grammar without a finite generator seed because its model class is well-defined by its axioms.

Seeded free constructions remain useful **test models**, but they are not required for candidate identity.

## Why outcome B does not pass

The candidates have real formal compression, exclusion, consequence structure, and countermodels. They are not empty metalanguage labels.

## What candidacy means

The result is deliberately weak in physical terms:

```text
FORMAL_CANDIDACY = YES
PHYSICAL_PRIVILEGE = NO
PHYSICAL_BRIDGE = NONE
LAW_EXHAUSTION = UNTESTED
```

The next discriminator must therefore be semantic/physical, not another attempt to prove one doctrine uniquely fundamental from pure form.

## Recommended next operation

```text
PGH1_R2B_PHYSICAL_BRIDGE_FEASIBILITY_DESIGN_GATE
```

That gate must define the weakest noncircular bridge from the law-free empirical anchor to the frozen grammar family and explicitly test whether model/interpretation choice merely reintroduces the independent law selector.

## Claim ceiling

```text
FORMAL_PRIMITIVE_GRAMMAR_CANDIDATES = 5
PHYSICALLY_TESTABLE_CANDIDATES = 0
R2B = UNSATISFIED
PHYSICAL_LAW_DERIVED = NO
EMPIRICAL_PREDICTION = NONE
FCP_EFFECT = NONE
```
