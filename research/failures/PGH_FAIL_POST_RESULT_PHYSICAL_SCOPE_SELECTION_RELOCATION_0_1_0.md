# PGH-FAIL-0036 — Post-Result Physical Scope Selection Relocation

## Status

```text
FAILURE_ID = PGH-FAIL-0036
STATUS = FAILED_PRESERVED
FAILURE_CLASS = POST_RESULT_SELECTOR_RELOCATION
PARENT_FAILURE_CONTEXT = PGH-FAIL-0035
TARGET = PGH-OBJ-0037
GRAMMAR = PGH-GRAM-0008
```

## Failed move

> After a prospectively selected empirical target refutes a candidate restriction, narrow or redefine the candidate's physical domain using information prompted by that failure, then treat the new domain restriction as though it had belonged to the original candidate before the test.

## Why the move fails

A physical scope predicate decides which real systems are allowed to count as instances of the grammar.

If that predicate is introduced only after seeing which target failed, it can absorb the unfavorable observation by changing instance membership rather than changing the grammar's formal equations.

The selective information has then moved from

```text
GRAMMAR_RULE
```

to

```text
PHYSICAL_DOMAIN_MEMBERSHIP
```

without eliminating result dependence.

This is scientifically equivalent in spirit to post-hoc target selection even when the formal grammar itself is left untouched.

## Canonical Kp application

Before Kp analysis:

- `PGH-GRAM-0008` had formal status but no physical-status assignment;
- `PGH-OBJ-0035` supplied a conditional full-model-class realization schema;
- `PGH-OBJ-0036` supplied a nonleaking first-target selection protocol;
- no physical domain predicate was frozen.

Kp was then validly selected and frozen under the protocol.

After Kp refuted the transferred restriction, a newly invented rule excluding geomagnetism, long-memory records, noncausal time series, or other failure-correlated classes cannot be backdated into the original candidate.

## Circular variants

The clearest invalid cases are:

```text
IN_SCOPE_IF_CONDITIONAL_INDEPENDENCE_HOLDS
IN_SCOPE_IF_MARKOV_FIT_IS_GOOD
IN_SCOPE_IF_TARGET_DOES_NOT_REJECT
```

More subtle variants can also fail when a post-result physical descriptor is chosen because it removes the observed counterexample.

## What remains allowed

Post-result learning is not forbidden.

A new physical scope hypothesis may be proposed if it has independent scientific motivation. But it must be represented as a **new or revised candidate** with explicit post-failure provenance and must be frozen before any new target outcome is examined.

Thus:

```text
POST_RESULT_SCOPE_HYPOTHESIS = PERMITTED_AS_NEW_HYPOTHESIS
RETROACTIVE_RESCUE = FORBIDDEN
OLD_KP_VERDICT = UNCHANGED
```

## Claim ceiling

This failure does not show that every possible physical scope rule is arbitrary.

It establishes only that the current PGH record contains no qualifying pre-Kp scope selector for `PGH-GRAM-0008`, and that a new post-Kp selector cannot receive retroactive predictive credit.
