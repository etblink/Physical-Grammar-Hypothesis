# PGH-FAIL-0010 — Unique or Minimal Empirical Seed 0.1.0

## Identity

```text
DERIVATION_ID = PGH-FAIL-0010
OPERATION_ID = PGH0_EMPIRICAL_GENERATOR_INVARIANCE_AND_SEED_MINIMALITY_GATE
STATUS = FAILED_PRESERVED
FAILURE_CLASS = UNDERDETERMINED_AND_NONEXISTENT_MINIMAL_GENERATORS
```

## Failed idea

One might try to rescue empirical-seed privilege by declaring that the physically correct seed is the unique smallest, irredundant, or symmetry-canonical generator of the grammar-closed empirical interface.

The gate shows that no such general principle is available.

## Failure 1 — minimum generators can be nonunique

In the two-element constructor system

```text
f(a)=b
f(b)=b
g(a)=a
g(b)=a
```

both `{a}` and `{b}` are minimum-cardinality generators of `{a,b}`.

They are not related by an automorphism of the labeled constructor system.

Therefore:

```text
MINIMUM_CARDINALITY = NOT_A_UNIQUE_SELECTOR
GRAMMAR_AUTOMORPHISM = NOT_REQUIRED_FOR_EQUAL_CLOSURE
```

## Failure 2 — inclusion-irredundant generators need not exist

For `N` with predecessor constructor

```text
p(0)=0
p(n+1)=n
```

a seed generates all of `N` exactly when it is unbounded.

Deleting any single element from an unbounded subset leaves it unbounded, so every full generator remains generating after deletion of any one element.

Thus no inclusion-irredundant generator exists for the full closure.

```text
IRREDUNDANT_GENERATOR_EXISTENCE = NOT_GENERAL
```

## Failure 3 — target-defined optimization is circular as physical selection

The instruction

```text
choose a smallest A such that Cl(A)=T_phys
```

cannot explain the empirical interface when `T_phys` has already been supplied as the desired physical target.

It optimizes a presentation only after the physical closure is assumed.

Likewise, choosing a seed because it reproduces a desired distinguishability partition is result-directed.

## What survives

Equal-closure seeds may be quotient-identified **for closure-factoring structure**. That is the qualified result `PGH-DER-0010`.

The failure concerns only attempts to promote uniqueness, minimality, or irredundancy into a general physical-selection rule.

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = FIXED_GRAMMAR_GENERATED_CLOSURE
RULE_DEPENDENCIES = SEED_MINIMALITY_OR_UNIQUENESS_SELECTION
LEMMA_DEPENDENCIES = PGH-DER-0010
SEMANTIC_ASSUMPTIONS = NONE
PHYSICAL_ASSUMPTIONS = TARGET_DEFINED_SELECTION_CONTROL_EXPLICITLY_PRESUPPOSES_TARGET_INTERFACE
SOURCE_DEPENDENCIES = FROZEN_37_SOURCE_LANDSCAPE
```

## Result

```text
PGH-FAIL-0010 = FAILED_PRESERVED
UNIQUE_MINIMUM_EMPIRICAL_SEED = NOT_GENERAL
IRREDUNDANT_EMPIRICAL_SEED = NOT_GUARANTEED
MINIMUM_CARDINALITY_AS_PHYSICAL_PRIVILEGE = REJECTED
TARGET_DEFINED_SEED_OPTIMIZATION = REJECTED_AS_EXPLANATION
```
