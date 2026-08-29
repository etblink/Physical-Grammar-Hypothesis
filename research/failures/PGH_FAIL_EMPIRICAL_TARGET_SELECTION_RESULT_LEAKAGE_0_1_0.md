# PGH-FAIL-0034 — Empirical Target Selection Result Leakage

## Status

```text
FAILURE_ID = PGH-FAIL-0034
STATUS = FAILED_PRESERVED
FAILURE_CLASS = TARGET_SELECTION_LEAKAGE
```

## Failed procedure

> Use the predicted relation `A independent C given B`, or statistics strongly revealing it, to find, rank, reorder, discretize, or retain the empirical target later claimed as the first prediction test.

## Why the procedure fails

The target result would participate in selecting the target that is later used to test that same result.

This invalidates prospective predictive credit even if the later statistical computation is technically correct.

Examples include:

- searching for datasets advertised as Markov or memoryless;
- preferring triples with weak conditional association after exploratory analysis;
- permuting roles until the chain relation is strongest;
- choosing discretization bins that improve conditional independence;
- dropping candidate datasets after inspecting unfavorable target dependence.

## Required correction

Target discovery and selection must use only the metadata/architecture rubric frozen in `PGH-OBJ-0036`.

The target, role assignment, data identity, and any discretization must be frozen before the target-dependence analysis begins.

## Contamination rule

A candidate whose documentation already discloses the exact target conditional-independence result is not eligible for first-test predictive credit, even if the project itself did not compute the result.

## Claim ceiling

```text
POSTHOC_TARGET_SELECTION = INVALID
PROSPECTIVE_METADATA_ONLY_SELECTION = REQUIRED
EMPIRICAL_TEST_CREDIT = NONE_UNTIL_PROTOCOL_SEQUENCE_IS_FOLLOWED
```
