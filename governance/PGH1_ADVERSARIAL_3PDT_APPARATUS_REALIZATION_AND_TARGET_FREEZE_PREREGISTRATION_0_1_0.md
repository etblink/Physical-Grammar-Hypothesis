# PGH-1 Adversarial 3PDT Apparatus Realization and Target Freeze — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_ADVERSARIAL_3PDT_APPARATUS_REALIZATION_AND_TARGET_FREEZE
OPERATION_CLASS = PHYSICAL_APPARATUS_REALIZATION__PRE_DATA_TARGET_FREEZE
CANONICAL_BASE = d8a16161f33d3bb8f97c15f095ca651c169f5896
QUALIFIED_DESIGN_ID = PGH-EXP-DESIGN-0001
CANDIDATE_PACKAGE = PGH-OBJ-0052
NEXT_AVAILABLE_TARGET_ID = TGT-047
TARGET_ID_AT_OPEN = NONE
PHYSICAL_TRIAL_DATA_GENERATION = FORBIDDEN
T_IND_ANALYSIS = FORBIDDEN
RESPONSE_DATA_INSPECTION = FORBIDDEN
```

## 1. Purpose

Realize the already-qualified mechanically ganged three-pole, two-position dry-contact interface as one exact physical apparatus, bind its acquisition/custody identity, verify only non-scientific engineering readiness, and freeze a new target **before any scientific trial is generated**.

This operation may assign `TGT-047` only if every frozen `I` eligibility burden is satisfied prospectively.

It may not execute the 512-trial scientific protocol.

## 2. Required physical components

The realized apparatus must contain at least:

```text
ONE_MECHANICALLY_GANGED_THREE_POLE_TWO_POSITION_DRY_CONTACT_SWITCH
THREE_DISTINCT_PHYSICAL_CONTACT_POLES
THREE_SEPARATELY_ADDRESSABLE_ACQUISITION_INPUTS
ONE_LOGGING_OR_ACQUISITION_DEVICE
ONE_HOST_OR_STORAGE_PATH_CAPABLE_OF_APPEND_ONLY_RAW_CAPTURE
```

The acquisition device may be a microcontroller, DAQ, data logger, or equivalent instrument, provided it exposes three separately addressable digital/dry-contact inputs whose semantics can be frozen before data.

The apparatus may share power, clocking and storage, but the three channel values must originate from three different physical switch poles.

## 3. Hardware identity evidence required

Before target freeze, record:

```text
SWITCH_MANUFACTURER_IF_AVAILABLE
SWITCH_MODEL_OR_PART_NUMBER_IF_AVAILABLE
SWITCH_SERIAL_IF_AVAILABLE
SWITCH_PHOTO_ID
SWITCH_PHYSICAL_MARKINGS
ACQUISITION_DEVICE_MANUFACTURER_IF_AVAILABLE
ACQUISITION_DEVICE_MODEL
ACQUISITION_DEVICE_SERIAL_OR_UNIQUE_HOST_ID
EXACT_INPUT_CHANNEL_IDENTIFIERS
WIRING_MANIFEST
APPARATUS_PHOTO_OR_DIAGRAM
```

If the switch has no serial number, `SWITCH_PHOTO_ID` plus physical markings and the committed wiring manifest become part of target identity.

No hardware may be silently substituted after target freeze.

## 4. Permitted commissioning before target freeze

Engineering commissioning is allowed only to establish that the three acquisition channels and three physical poles are separately wired and recordable.

Permitted checks:

```text
CHANNEL_EXISTENCE_CHECK
CONTINUITY_CHECK_PER_POLE
OPEN_CIRCUIT_CHECK_PER_POLE
LOGGER_TIMESTAMP_CHECK
MISSING_CHANNEL_DETECTION_CHECK
FILE_WRITE_CHECK
```

Commissioning must not execute the scientific alternating 512-trial schedule.

Commissioning observations:

- are engineering metadata, not empirical PGH evidence;
- receive zero positive or negative scientific credit;
- may be used to repair wiring before target freeze;
- must not be used to modify `G`, `J`, `S`, `I`, the qualified design class, field-selection rule, role rule, planned trial count, or verdict mapping.

A commissioning log must be retained with date, action, and any hardware change.

## 5. Commissioning boundary against leakage

The following are forbidden before analysis preregistration:

```text
RUNNING_THE_512_TRIAL_PROTOCOL
COMPUTING_A_B_C_AGREEMENT_RATE
COMPUTING_JOINT_COUNTS
COMPUTING_CORRELATION_OR_DEPENDENCE
COMPUTING_T_IND_COMPATIBILITY
SELECTING_CHANNELS_BY_OBSERVED_BEHAVIOR
DISCARDING_A_WORKING_CHANNEL_FOR_POOR_AGREEMENT
```

If commissioning reveals that a component is defective, it may be replaced **before target freeze** and the replacement identity must be bound. After target freeze, replacement creates a new target identity and requires a new freeze.

## 6. Exact channel and field freeze

Before target assignment, bind the three exact acquisition identifiers, for example only as a structural pattern:

```text
INPUT_D2
INPUT_D3
INPUT_D4
```

Actual identifiers come from the realized device.

Each field's substantive alphabet must be prospectively frozen as exactly:

```text
OPEN
CLOSED
```

Missing/invalid states are not substantive values.

Exact identifiers are Unicode-sorted and assigned:

```text
A = first
B = second
C = third
```

No later permutation is allowed.

## 7. Wiring requirement

The wiring manifest must establish:

```text
POLE_1 -> EXACT_INPUT_1
POLE_2 -> EXACT_INPUT_2
POLE_3 -> EXACT_INPUT_3
```

There must be no software duplication path from one physical pole into multiple scientific fields.

If pull-ups, pull-downs, isolation, interface resistors, or optocouplers are used, they must be documented before target freeze.

## 8. Frozen scientific protocol inherited without change

The realized target inherits:

```text
PLANNED_TRIAL_COUNT = 512
ODD_TRIALS = ACTUATOR_POSITION_0
EVEN_TRIALS = ACTUATOR_POSITION_1
DEFAULT_SETTLE_INTERVAL = 1000 ms
ONE_JOINT_SAMPLE_PER_TRIAL = YES
```

A different settle interval may be frozen during this operation only if:

1. it is chosen before target freeze;
2. the reason is engineering/authority based and not derived from the scientific A/B/C distribution;
3. the value is recorded in the target-freeze artifact.

Trial count and alternating schedule may not change.

## 9. Validity and missingness freeze

Before target assignment, freeze exactly these top-level validity classes unless a one-to-one refinement is required by the acquisition system:

```text
VALID
MISSING_CHANNEL_1
MISSING_CHANNEL_2
MISSING_CHANNEL_3
ACQUISITION_FAILURE
TIMING_FAILURE
```

A/B/C disagreement is never itself invalid.

A channel state that disagrees with the commanded actuator position is never itself invalid.

## 10. Required target-freeze fields

A successful target freeze must record:

```text
TARGET_ID = TGT-047
TARGET_CLASS = ADVERSARIAL_NEGATIVE_ONLY_PHYSICAL_INTERFACE
APPARATUS_NAME
APPARATUS_VERSION
SWITCH_IDENTITY
ACQUISITION_DEVICE_IDENTITY
CHANNEL_A_IDENTIFIER
CHANNEL_B_IDENTIFIER
CHANNEL_C_IDENTIFIER
RAW_ALPHABETS
WIRING_MANIFEST_HASH
APPARATUS_PHOTO_OR_DIAGRAM_LOCATOR
INTERFACE_SCHEMA_VERSION
SETTLE_INTERVAL
TRIAL_COUNT = 512
TRIAL_SCHEDULE = ODD_POSITION_0__EVEN_POSITION_1
VALIDITY_RULE_VERSION
RAW_DATA_FILENAME_RULE
CUSTODY_PATH
PUBLIC_OR_AUDITABLE_ACCESS_PATH
HASH_ALGORITHM = SHA-256
```

If any field is absent, target freeze fails rather than being inferred.

## 11. Public or auditable event-level access

Before target assignment, define the exact future event-level custody surface.

The target may qualify with either:

```text
PUBLIC_REPOSITORY_COMMIT_PATH
OR
AUDITABLE_IMMUTABLE_LOCAL_CUSTODY_PATH_WITH_HASH_AND_LATER_PUBLICATION_RULE
```

Preferred route for this project:

```text
RAW_DATA_AND_MANIFESTS_COMMITTED_TO_PGH_REPOSITORY_AFTER_CAPTURE
OR
AN_IMMUTABLE_ARCHIVE_LINKED_FROM_THE_REPOSITORY
```

The raw scientific data do not yet exist during this operation.

## 12. Acquisition software boundary

If custom acquisition software is required, its exact source must be frozen before target assignment.

The software may:

```text
READ_THREE_INPUTS
READ_TIMESTAMP
WRITE_ONE_RAW_ROW_PER_TRIAL
WRITE_VALIDITY_CODE
WRITE_INTERFACE_VERSION
```

It may not:

```text
DERIVE_ONE_CHANNEL_FROM_ANOTHER
COMPUTE_AGREEMENT
COMPUTE_CORRELATION
COMPUTE_MODEL_STATISTICS
FILTER_ROWS_BY_A_B_C_PATTERN
```

Any scientific analysis code must be separately frozen in the later negative-only analysis preregistration.

## 13. Operation outcome space

Exactly one outcome:

```text
A = APPARATUS_REALIZED__I_ELIGIBLE__TGT_047_FROZEN
B = APPARATUS_REALIZED__I_INELIGIBLE__NO_TARGET_FREEZE
C = APPARATUS_NOT_YET_REALIZED__PHYSICAL_DEPENDENCY_REMAINS
D = APPARATUS_REALIZATION_PROVENANCE_INSUFFICIENT__NO_TARGET_FREEZE
```

## 14. Required outputs on completion

If the apparatus is physically realized, the completion commit may create:

```text
empirical/PGH1_ADVERSARIAL_3PDT_APPARATUS_MANIFEST_0_1_0.md
empirical/PGH1_ADVERSARIAL_3PDT_COMMISSIONING_LOG_0_1_0.md
empirical/PGH1_ADVERSARIAL_3PDT_TARGET_FREEZE_0_1_0.md
handoffs/PGH1_ADVERSARIAL_3PDT_APPARATUS_REALIZATION_HANDOFF_0_1_0.md
```

If the apparatus is not physically realized, do not fabricate these artifacts.

## 15. Hard stop after successful target freeze

If Outcome A occurs:

```text
TARGET_VALUES_ACCESSED = NO
SCIENTIFIC_TRIALS_GENERATED = NO
NEXT_OPERATION = PGH1_ADVERSARIAL_3PDT_NEGATIVE_ONLY_ANALYSIS_PREREGISTRATION
```

Only after that analysis preregistration is canonical may physical scientific trials begin.

## 16. Claim ceiling

```text
PGH_OBJ_0052_TESTED = NO
PGH_OBJ_0052_REFUTED = NO
PGH_OBJ_0052_SUPPORTED = NO
STRONG_PGH_CONFIRMED = NO
R2B = UNSATISFIED
```

Truth over PGH requires binding the real apparatus before treating a design as an empirical target.
