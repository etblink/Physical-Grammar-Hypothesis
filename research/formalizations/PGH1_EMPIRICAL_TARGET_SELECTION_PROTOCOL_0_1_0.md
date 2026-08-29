# PGH-OBJ-0036 — Empirical Target Selection Protocol 0.1.0

## Status

```text
OBJECT_ID = PGH-OBJ-0036
STATUS = QUALIFIED_PROTOCOL
EMPIRICAL_TARGET = NONE
```

## Purpose

Define a nonleaking rule for discovering and selecting the first empirical instantiation of `PGH-GRAM-0008` before inspecting the predicted conditional-independence result.

## Required target form

A candidate target must provide repeated jointly indexable records for three finite variables, or a target-specific discretization rule fixed before value inspection.

Role assignment must be objective from measurement/process/spatial architecture:

```text
EARLIEST_OR_UPSTREAM = A
INTERMEDIATE = B
LATEST_OR_DOWNSTREAM = C
```

No post-hoc role permutation is allowed.

## Eligibility

A candidate is eligible only if it satisfies all:

```text
PHYSICAL_RECORD_SCOPE
OBJECTIVE_ORDERED_THREE_ROLE_ARCHITECTURE
JOINT_EVENT_IDENTITY
FINITE_ALPHABET_OR_PRECOMMITTED_DISCRETIZATION
PUBLIC_OR_AUDITABLE_EVENT_LEVEL_ACCESS
ADEQUATE_SAMPLE_SUPPORT
DOCUMENTED_SELECTION_MISSINGNESS_AND_MEASUREMENT_RULES
NO_USE_OF_TARGET_DEPENDENCE_FOR_DISCOVERY_OR_RANKING
NO_SELECTION_BECAUSE_MARKOV_OR_MEMORYLESS_BEHAVIOR_IS_ALREADY_KNOWN
```

## Ranking rubric

Score eligible candidates using only:

1. measurement-role clarity;
2. native finite records;
3. event-level joint access;
4. sample size/cell support;
5. preprocessing burden;
6. selection/missingness clarity;
7. reproducibility;
8. physical-record interpretation clarity;
9. discretization rigidity;
10. archival stability.

No correlation, independence, model-fit, or target-effect statistic may enter ranking.

## Contamination policy

```text
C0_NO_EXPOSURE = ELIGIBLE
C1_GENERAL_DOMAIN_KNOWLEDGE = ELIGIBLE
C2_HINTS_AT_TARGET_DEPENDENCE = REVIEW
C3_EXACT_TARGET_RESULT_DISCLOSED = FIRST_TEST_INELIGIBLE
```

## Tie break

```text
NATIVE_FINITE
> LARGER_EVENT_COUNT
> FEWER_PREPROCESSING_STEPS
> EARLIER_ARCHIVAL_DATE
> LEXICOGRAPHIC_IDENTIFIER
```

## Search discipline

Discovery queries must seek physical datasets by record architecture, public event-level access, and measurement metadata.

They may not seek datasets by the success/failure of the predicted conditional independence.

## Freeze sequence

```text
DISCOVER_METADATA_ONLY
-> BUILD_CANDIDATE_LEDGER
-> CLASSIFY_CONTAMINATION
-> SCORE_ELIGIBILITY_AND_RANKING
-> FREEZE_ONE_TARGET_AND_ROLE_ASSIGNMENT
-> FREEZE_RAW_DATA_IDENTITY
-> PREREGISTER_STATISTICAL_TEST
-> ONLY_THEN_INSPECT_TARGET_DEPENDENCE
```

## Failure condition

If no candidate survives the frozen rubric, the empirical test remains uninstantiated. The criteria may not be relaxed after seeing candidate dependence patterns.

## Claim ceiling

```text
TARGET_SELECTION_PROTOCOL = QUALIFIED
TARGET = NONE
EMPIRICAL_TEST = NOT_STARTED
```
