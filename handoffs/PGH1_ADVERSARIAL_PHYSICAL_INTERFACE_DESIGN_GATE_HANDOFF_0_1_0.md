# PGH-1 Adversarial Physical-Interface Design Gate — Handoff 0.1.0

## Exact result

```text
OPERATION_ID = PGH1_ADVERSARIAL_PHYSICAL_INTERFACE_DESIGN_GATE
PREREGISTRATION_COMMIT = 37d4c871666654c33ef5c9c26eb6a2de761aab46
OUTCOME = A__D1_MECHANICALLY_GANGED_THREE_POLE_SWITCH_QUALIFIES
SELECTED_DESIGN_ID = PGH-EXP-DESIGN-0001
TARGET_ID = NONE
NEXT_AVAILABLE_TARGET_ID = TGT-047
PHYSICAL_DATA_GENERATED = NO
TARGET_VALUES_ACCESSED = NO
PGH_OBJ_0052_TESTED = NO
```

## Controlling finding

A mechanically common two-position actuator controlling three physically distinct dry-contact poles is the weakest adequate adversarial interface class under unchanged frozen `I`.

It avoids the two main confounds of the alternatives:

- the common-armature relay adds unnecessary drive and timing machinery;
- the optical design cannot establish generic native-binary detector semantics at this closed-record scope without concrete hardware sourcing.

The switch design supplies three physically distinct `{OPEN,CLOSED}` channels without software duplication or analyst-selected thresholding.

## Frozen design

```text
COMMON_PHYSICAL_STATE = ONE_MECHANICALLY_SHARED_TWO_POSITION_ACTUATOR
PHYSICAL_CONTACT_POLES = 3
RAW_CHANNEL_ALPHABET = {OPEN,CLOSED}
PLANNED_TRIAL_COUNT = 512
ODD_TRIALS = POSITION_0
EVEN_TRIALS = POSITION_1
DEFAULT_SETTLE_INTERVAL = 1000 ms
ONE_JOINT_SAMPLE_PER_TRIAL = YES
```

A/B/C are assigned only after actual acquisition channel identifiers exist, using Unicode lexical order frozen before the first trial.

Disagreement among channels is response data and may never be converted into an invalidity rule merely because it weakens the expected common-bit pattern.

## Negative-only ceiling

```text
EXPECTED_COMMON_BIT_BEHAVIOR = ZERO_EMPIRICAL_EVIDENCE
QUALIFIED_REJECT_T_ind = MAY_REFUTE_PGH_OBJ_0052_AT_TARGET
DO_NOT_REJECT_T_ind = ADVERSARIAL_STRESS_TEST_SURVIVAL__ZERO_POSITIVE_EMPIRICAL_CREDIT
INCONCLUSIVE = NO_VERDICT
```

No support can be earned through this adversarial target-selection route.

## What remains before any physical trial

A separate apparatus-realization and target-freeze operation must bind a real apparatus and exact target metadata:

```text
APPARATUS_NAME_AND_VERSION
SWITCH_MANUFACTURER_MODEL_OR_UNIQUE_DESCRIPTION
SWITCH_SERIAL_OR_PHOTO_ID
ACQUISITION_DEVICE_IDENTITY
EXACT_THREE_CHANNEL_IDENTIFIERS
WIRING_MANIFEST
INTERFACE_SCHEMA_VERSION
SETTLE_INTERVAL
TRIAL_COUNT_AND_SCHEDULE
VALIDITY_RULE_VERSION
CUSTODY_PATH
PUBLIC_OR_AUDITABLE_ACCESS_PATH
```

Only then may a target identity such as the next available `TGT-047` be assigned.

After target freeze, a separate negative-only analysis preregistration must freeze the complete `T_ind` finite-sample decision functional before the first response datum is generated.

## Hard stop

```text
APPARATUS_REALIZATION = REQUIRES_EXTERNAL_PHYSICAL_ACTION
TARGET_FREEZE = NOT_YET_POSSIBLE
ANALYSIS_PREREGISTRATION = DEFER_UNTIL_EXACT_APPARATUS_AND_CHANNEL_IDENTITIES_EXIST
PHYSICAL_TRIAL_EXECUTION = FORBIDDEN
```

The repository-side scientific work has therefore reached the first genuine physical dependency: a real three-pole switch interface and acquisition hardware must exist before the next target-freeze operation can honestly proceed.

## Claim ceiling

```text
PGH_OBJ_0052_REFUTED = NO
PGH_OBJ_0052_SUPPORTED = NO
PGH_OBJ_0052_TESTED = NO
STRONG_PGH_CONFIRMED = NO
R2B = UNSATISFIED
```
