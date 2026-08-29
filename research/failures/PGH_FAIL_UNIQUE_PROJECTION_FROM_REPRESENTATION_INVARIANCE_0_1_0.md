# PGH-FAIL-0004 — Unique Projection from Representation Invariance Failure 0.1.0

## Identity

```text
DERIVATION_ID = PGH-FAIL-0004
OPERATION_ID = PGH0_REPRESENTATION_EQUIVALENCE_AND_COHERENCE_CHALLENGE
STATUS = FAILED
CLAIMED_RESULT = REPRESENTATION_INVARIANCE_UNIQUELY_SELECTS_THE_CORRECT_PRESENTATION_PROJECTION
FAILURE_CLASS = UNDERDETERMINED
```

## Failed idea

Once representation equivalence can be defined by a syntax-level projection, one might hope that the existing PGH requirement of representation invariance uniquely selects which presentation distinctions are irrelevant.

That hope fails at current scope.

## Counterfamily

The preregistered projections

```text
P0 = full tree identity
P1 = ordered leaf word
P2 = leaf multiset
P3 = leaf count
```

are all defined independently of the binary operation being tested and are covariant under bijective renaming of leaf labels.

Yet factorization through them imposes different coherence classes.

On a two-element carrier:

```text
P0 -> 16 binary operations
P1 -> 8 binary operations
P2 -> 6 binary operations
P3 -> 0 binary operations
```

Therefore outcome-independence and relabeling covariance do not uniquely choose one projection.

## Why choosing P1 would still be unearned

P1 is attractive because it forgets only bracketing while preserving leaf identities and order, and it yields associativity.

But selecting P1 *because* associativity is desirable would reintroduce result-directed selection.

Current PGH commitments do not yet prove that:

```text
BRACKETING = REPRESENTATIONAL_ONLY
ORDER = FUNDAMENTAL_OR_RETAINED
LABEL_IDENTITY = FUNDAMENTAL_OR_RETAINED
```

Nor do they prove the opposite.

## What remains valid

The failure does not invalidate:

- outcome-independent equivalence induced by a projection;
- factorization as the exact coherence criterion;
- the associativity result for P1;
- the associative-commutative result for P2;
- coherence monotonicity under increased forgetting.

It invalidates only the claim that current representation-invariance principles uniquely select the correct amount of forgetting.

## Result

```text
PGH-FAIL-0004 = FAILED_PRESERVED
UNIQUE_PRIVILEGED_PROJECTION = NOT_FOUND
NEXT_BURDEN = SELECT_INVARIANT_CONTENT_WITHOUT_RESULT_DIRECTED_CHOICE
```

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = PGH-GRAM-0002
RULE_DEPENDENCIES = PRESENTATION_PROJECTION; RELABELING_COVARIANCE
LEMMA_DEPENDENCIES = PGH-DER-0004; PGH-DER-0005
SEMANTIC_ASSUMPTIONS = NONE_PHYSICAL
PHYSICAL_ASSUMPTIONS = NONE
SOURCE_DEPENDENCIES = NONE
```
