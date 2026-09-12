# PGH-1 D1 Experiment Readiness Preparation — Preregistration 0.1.0

## Identity

```text
OPERATION = PGH1_D1_EXPERIMENT_READINESS_PREPARATION
CANONICAL_BASE = d8a16161f33d3bb8f97c15f095ca651c169f5896
CANONICAL_BASE_TREE = 772b0946912aeae73cfec6b1676e71911fb89cb5
CONTROLLING_DESIGN_ARTIFACT = audits/PGH1_ADVERSARIAL_PHYSICAL_INTERFACE_DESIGN_GATE_0_1_0.md
CANDIDATE_PACKAGE = PGH-OBJ-0052
SELECTED_INTERFACE_CLASS = D1__MECHANICALLY_GANGED_THREE_POLE_SWITCH_INTERFACE
ACTUAL_APPARATUS = NONE_BOUND
ACTUAL_CHANNEL_IDS = NONE_BOUND
TARGET_ID = NONE
TARGET_VALUES_ACCESSED = NO
PHYSICAL_RESPONSE_DATA_GENERATED = NO
```

## Purpose

Prepare non-scientific experiment-execution infrastructure so that, once the required physical hardware exists, the separately governed operation `APPARATUS_REALIZATION_AND_TARGET_FREEZE` can bind an actual D1 apparatus without improvising custody, schema, validity, or operator procedure under time pressure.

This operation improves readiness only. It is not apparatus realization, target selection, target freeze, analysis preregistration, trial execution, or empirical adjudication.

## Frozen source boundary

The controlling D1 design gate already establishes:

```text
INTERFACE_CLASS = THREE_POLE_TWO_POSITION_MECHANICALLY_GANGED_DRY_CONTACT_INTERFACE
CHANNEL_COUNT = 3
RAW_ALPHABET_PER_CHANNEL = {OPEN,CLOSED}
DEFAULT_SETTLE_INTERVAL = 1000 milliseconds
PLANNED_TRIAL_COUNT = 512
TRIAL_SCHEDULE = ODD_POSITION_0__EVEN_POSITION_1
SAMPLE_COUNT_PER_TRIAL = 1 joint sample
NEXT_AVAILABLE_TARGET_ID = TGT-047__NOT_ASSIGNED
```

It also requires the future scientific sequence:

```text
APPARATUS_REALIZATION_AND_TARGET_FREEZE
-> NEGATIVE_ONLY_ANALYSIS_PREREGISTRATION
-> ONLY_THEN_PHYSICAL_TRIAL_EXECUTION_AND_RESPONSE_DATA
```

This preparation may not collapse or reorder that sequence.

## Authorized outputs

The operation may create only execution-readiness materials of the following classes:

1. an operator checklist for apparatus realization and target freeze;
2. apparatus and protocol manifest templates containing placeholders rather than hardware facts;
3. a machine-readable raw-record schema;
4. a schema/custody validator that performs structural checks only;
5. clearly marked synthetic fixtures for dry-run validation of file/schema handling;
6. a capture-directory README and custody procedure;
7. a readiness handoff and bounded current-state navigation reconciliation.

## Explicitly forbidden

```text
BIND_REAL_APPARATUS = NO
ASSIGN_TGT_047 = NO
BIND_REAL_CHANNEL_IDENTIFIERS = NO
ACCESS_OR_RECORD_REAL_RESPONSE_VALUES = NO
GENERATE_PHYSICAL_TRIALS = NO
CHOOSE_T_IND_FINITE_SAMPLE_DECISION_FUNCTIONAL = NO
COMPUTE_P_VALUE_OR_OTHER_EMPIRICAL_VERDICT = NO
SELECT_RESULT_DIRECTED_VALIDITY_RULE = NO
CHANGE_G_J_S_I = NO
REVISE_PGH_OBJ_0052 = NO
AWARD_POSITIVE_EMPIRICAL_CREDIT = NO
CLAIM_REFUTATION_OR_SUPPORT = NO
```

No synthetic fixture may be represented as a prediction about the real apparatus. Synthetic rows exist only to test parsing, validity-code handling, trial scheduling, and custody tooling.

## Synthetic-data firewall

Every synthetic fixture must satisfy all of the following:

```text
INTERFACE_VERSION starts with SYNTHETIC_
ACQUISITION_TIMESTAMP uses a non-real reserved synthetic date domain
fixture path contains /synthetic/
README labels rows NON-EMPIRICAL
validator output never assigns a scientific verdict
```

Synthetic channel patterns should intentionally include agreement, disagreement, and missing/invalid cases so no single physical-response direction is encoded as the expected observed result.

## Validation requirements

Before publication/integration, all of the following must hold:

1. branch is a strict descendant of exact base `d8a16161...`;
2. changed paths are limited to readiness infrastructure plus bounded navigation reconciliation;
3. no real target ID is assigned and `TGT-047` remains available/unassigned;
4. no actual hardware identity, serial, photo ID, logger ID, or channel ID is fabricated;
5. no physical-response record exists;
6. schema preserves exact substantive channel alphabet `{OPEN,CLOSED}` and separates validity from channel values;
7. validator rejects derived/copied-column declarations when represented in manifests and rejects malformed/missing required fields;
8. schedule validation requires 512 rows only for a final real capture, while synthetic fixtures may use an explicitly declared smaller dry-run count;
9. disagreement among channels is never treated as invalid by itself;
10. analysis/statistical logic is absent except for verifying that no such verdict is produced;
11. current-state navigation, if updated, must say design qualified / apparatus not yet bound / data absent;
12. final handoff stops at the apparatus-realization boundary.

## Publication rule

The preparation package may be integrated into `main` only if all validation requirements pass. Integration grants no authority to execute physical trials. The later apparatus-realization operation remains separately prospective and must bind actual identities before target freeze.

Truth over PGH.