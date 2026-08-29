# PGH-FAIL-0032 — Causal Wiring Physical Semantics Premature

## Status

```text
FAILURE_ID = PGH-FAIL-0032
STATUS = FAILED_PRESERVED
FAILURE_CLASS = PREMATURE_PHYSICAL_INTERPRETATION
```

## Failed inference

> Because `PGH-GRAM-0008` is a qualified formal grammar candidate and its graph factorization excludes some probability models, the graph arrows may already be called physical causes and the derived conditional independence may already be called a physical law.

## Why the inference fails

Formal grammar candidacy establishes only:

```text
EXACT_MODEL_CLASS
COMPACT_STRUCTURAL_RULE
NONTRIVIAL_FORMAL_EXCLUSION
FREE_LOCAL_KERNELS
COUNTERMODELS
```

It does not establish a physical interpretation of the variables, arrows, or probability values.

Calling the arrows physical causes by definition would cross the semantic boundary without a separate bridge test.

Likewise, assigning the formal variables to observed quantities after inspecting data could turn graph choice into empirical-model selection rather than grammar-derived law.

## What remains valid

A later physical-semantic operation may test a causal/dependency reading of the graph.

Such a reading is not forbidden merely because it is primitive. It must instead be:

- explicitly preregistered;
- kept distinct from empirical fit;
- tested against alternative semantic readings;
- shown not to import local response kernels or the target conditional-independence pattern through the interpretation map.

## Claim ceiling

```text
PGH_GRAM_0008_FORMAL_CANDIDATE = YES
PHYSICAL_CAUSAL_MEANING = NOT_YET_QUALIFIED
PHYSICAL_LAW_DERIVED = NO
R2B = UNSATISFIED
```
