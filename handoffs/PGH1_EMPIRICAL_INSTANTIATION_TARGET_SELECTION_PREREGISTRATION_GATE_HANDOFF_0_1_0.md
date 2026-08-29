# PGH-1 Empirical Instantiation Target Selection Preregistration Gate — Handoff 0.1.0

## Scientific result

```text
OPERATION_ID = PGH1_EMPIRICAL_INSTANTIATION_TARGET_SELECTION_PREREGISTRATION_GATE
REGISTRY_ID = PGH-OP-0062
STATUS = COMPLETE_CANDIDATE
PREREGISTRATION_COMMIT = 1a07bc4dd0090d5dd70646c71fae05230e890703
OUTCOME = A__A_NONLEAKING_TARGET_SELECTION_PROTOCOL_CAN_BE_FROZEN_WITH_OBJECTIVE_ROLE_ASSIGNMENT_ELIGIBILITY_RANKING_CONTAMINATION_AND_TIE_BREAK_RULES__A_SEPARATE_TARGET_DISCOVERY_OPERATION_IS_JUSTIFIED
```

## New records

```text
PGH-OBJ-0036 = EMPIRICAL_TARGET_SELECTION_PROTOCOL
PGH-FAIL-0034 = EMPIRICAL_TARGET_SELECTION_RESULT_LEAKAGE
```

## Core protocol

The first empirical target must be selected using only measurement/data architecture and accessibility metadata.

Role assignment is frozen from objective order:

```text
EARLIEST_OR_UPSTREAM = A
INTERMEDIATE = B
LATEST_OR_DOWNSTREAM = C
```

No candidate may be found, ranked, reordered, discretized, or retained because its observed dependence pattern is favorable to

\[
A\perp C\mid B.
\]

## Discovery information allowed

```text
DATASET_OR_EXPERIMENT_IDENTITY
PHYSICAL_PURPOSE
VARIABLE_DEFINITIONS
MEASUREMENT_OR_PROCESS_ORDER
DATA_TYPES_AND_ALPHABETS
EVENT_COUNT_METADATA
ACCESS_FORMAT
MISSINGNESS_SELECTION_DOCUMENTATION
INSTRUMENT_DESCRIPTION
```

## Discovery information forbidden for selection

```text
TARGET_CORRELATIONS
TARGET_CONDITIONAL_DEPENDENCE
MARKOV_OR_MEMORYLESSNESS_SUCCESS_CLAIMS
TARGET_CI_TESTS
CHAIN_MODEL_FIT
TARGET_P_VALUES_OR_EFFECT_SIZES
TARGET_DEPENDENCE_PLOTS
```

## Next recommended operation

```text
NEXT_RECOMMENDED_OPERATION = PGH1_EMPIRICAL_INSTANTIATION_TARGET_DISCOVERY_AND_FREEZE
NEXT_OPERATION_AUTHORIZED = NO
```

That operation may use external web/source search, but search terms must target physical-record architecture and public event-level data rather than the predicted result.

It must build a candidate ledger from metadata only, classify contamination, score the frozen rubric, and freeze one target if—and only if—an eligible uncontaminated candidate survives.

After target freeze, a separate statistical-analysis preregistration is mandatory before any target dependence is calculated.

## Result ceiling

```text
PHYSICALLY_TESTABLE_IN_PRINCIPLE = YES
TARGET_SELECTION_PROTOCOL = QUALIFIED
EMPIRICAL_TARGET = NONE
EMPIRICAL_DATA_ANALYSIS = NONE
EMPIRICAL_PREDICTION_TESTED = NO
R2B = UNSATISFIED
PHYSICAL_LAW_ESTABLISHED = NO
FCP_EFFECT = NONE
```

## Structured handoff capsule

<!-- PGH_HANDOFF_CAPSULE_BEGIN -->
```json
{
  "capsule_schema_version": "0.1.0",
  "operation_id": "PGH1_EMPIRICAL_INSTANTIATION_TARGET_SELECTION_PREREGISTRATION_GATE",
  "status": "COMPLETE_CANDIDATE",
  "indexed_research_baseline_commit": "d7f82ad8a7e5bb2b5a1a397002af42643ee50f65",
  "must_read": [
    "audits/PGH1_EMPIRICAL_INSTANTIATION_TARGET_SELECTION_PREREGISTRATION_GATE_0_1_0.md",
    "research/formalizations/PGH1_EMPIRICAL_TARGET_SELECTION_PROTOCOL_0_1_0.md",
    "research/failures/PGH_FAIL_EMPIRICAL_TARGET_SELECTION_RESULT_LEAKAGE_0_1_0.md",
    "research/formalizations/PGH1_CAUSAL_WIRING_MODEL_CLASS_PHYSICAL_BRIDGE_SCHEMA_0_1_0.md"
  ],
  "outputs": [
    "audits/PGH1_EMPIRICAL_INSTANTIATION_TARGET_SELECTION_PREREGISTRATION_GATE_0_1_0.md",
    "research/formalizations/PGH1_EMPIRICAL_TARGET_SELECTION_PROTOCOL_0_1_0.md",
    "research/failures/PGH_FAIL_EMPIRICAL_TARGET_SELECTION_RESULT_LEAKAGE_0_1_0.md",
    "handoffs/PGH1_EMPIRICAL_INSTANTIATION_TARGET_SELECTION_PREREGISTRATION_GATE_HANDOFF_0_1_0.md"
  ],
  "open_questions": ["PGH-Q-0017"],
  "next_recommended_operation": "PGH1_EMPIRICAL_INSTANTIATION_TARGET_DISCOVERY_AND_FREEZE",
  "next_operation_authorized": false,
  "do_not_assume": [
    "ANY_TARGET_HAS_BEEN_SELECTED",
    "ANY_TARGET_DEPENDENCE_HAS_BEEN_INSPECTED",
    "EMPIRICAL_PREDICTION_HAS_BEEN_TESTED",
    "R2B_HAS_PASSED"
  ]
}
```
<!-- PGH_HANDOFF_CAPSULE_END -->
