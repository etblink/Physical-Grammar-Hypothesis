# PGH-FAIL-0033 — Post-Hoc Causal Wiring Empirical Instantiation

## Status

```text
FAILURE_ID = PGH-FAIL-0033
STATUS = FAILED_PRESERVED
FAILURE_CLASS = TARGET_SELECTION_LEAKAGE
```

## Failed procedure

> Search observed data for triples of variables that approximately satisfy `A independent C given B`, then map those variables to the formal roles of `PGH-GRAM-0008` and count the agreement as a grammar prediction.

## Why the procedure fails

The target conditional-independence result would have been used to choose the empirical instantiation that is later claimed to predict it.

This reverses the explanatory direction:

```text
OBSERVED_PATTERN -> ROLE_ASSIGNMENT -> CLAIMED_PREDICTION
```

rather than the admissible order:

```text
PRE_REGISTERED_ROLE_ASSIGNMENT -> GRAMMAR_RESTRICTION -> EMPIRICAL_TEST
```

The former is target leakage / model fitting and receives no PGH predictive credit.

## Required correction

Before any empirical data relevant to the target conditional independence are inspected, a separate operation must freeze:

- target-selection criteria;
- the physical system/domain;
- the three variable roles and alphabets or discretization rules;
- sampling/measurement assumptions;
- the later statistical test protocol or the rule for designing it without inspecting the target result.

Target discovery may use metadata, feasibility, accessibility, and measurement-definition information, but may not use the target conditional-independence outcome to select the system.

## Claim ceiling

```text
POSTHOC_TARGET_MAPPING = INVALID
PROSPECTIVE_TARGET_MAPPING = REQUIRED
PGH_GRAM_0008_TESTABILITY_IN_PRINCIPLE = PRESERVED
EMPIRICAL_PREDICTION_CREDIT = NONE_YET
```
