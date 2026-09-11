# PGH-1 Adversarial Common-State Interface Specification 0.1.0

## Status

```text
DESIGN_ID = PGH-EXP-DESIGN-0001
DECLARING_OPERATION = PGH1_ADVERSARIAL_PHYSICAL_INTERFACE_DESIGN_GATE
STATUS = QUALIFIED_DESIGN_CLASS__NOT_YET_REALIZED_TARGET
CANDIDATE_PACKAGE = PGH-OBJ-0052
NEGATIVE_ONLY_ROUTE = YES
TARGET_ID = NONE
```

## Physical concept

Use one mechanically ganged three-pole, two-position dry-contact switch. One common actuator position is the shared physical state. The three poles are three distinct physical contact channels.

Each channel is recorded independently as:

```text
OPEN
CLOSED
```

No channel may be synthesized from another channel's software value.

## Required apparatus architecture

```text
COMMON_ACTUATOR = 1
PHYSICAL_CONTACT_POLES = 3
ACQUISITION_CHANNELS = 3 DISTINCT INPUTS
JOINT_CLOCK = ALLOWED
COMMON_STORAGE = ALLOWED
SOFTWARE_DUPLICATION = FORBIDDEN
```

The three poles should be wired as electrically distinguishable paths. Shared acquisition hardware is acceptable if the three inputs are separately addressable and each receives its signal from a different physical contact pole.

## Prospective event schema

```text
TRIAL_ID               integer, unique, monotone
ACQUISITION_TIMESTAMP  timestamp
INTERFACE_VERSION      immutable string
CHANNEL_1_STATE        {OPEN,CLOSED} or missing
CHANNEL_2_STATE        {OPEN,CLOSED} or missing
CHANNEL_3_STATE        {OPEN,CLOSED} or missing
VALIDITY_CODE           frozen categorical code
```

The channel identifiers `CHANNEL_1`, `CHANNEL_2`, `CHANNEL_3` are placeholders only. At apparatus realization they must be replaced by exact acquisition-channel identifiers before the first trial.

## Role assignment

At realization:

1. freeze exact three channel identifiers;
2. sort them by Unicode code-point order;
3. assign the first to A, second to B, third to C;
4. never permute after data exist.

## Planned trial protocol

```text
TRIAL_COUNT = 512
TRIAL_001 = ACTUATOR_POSITION_0
TRIAL_002 = ACTUATOR_POSITION_1
TRIAL_003 = ACTUATOR_POSITION_0
TRIAL_004 = ACTUATOR_POSITION_1
...
ODD_TRIALS = POSITION_0
EVEN_TRIALS = POSITION_1
DEFAULT_SETTLE_INTERVAL = 1000 ms
ONE_JOINT_SAMPLE_PER_TRIAL = YES
```

The actuator command is control metadata and is not A, B or C.

The alternating schedule is frozen to guarantee both physical states are exercised equally. It is not used to exclude records and does not itself establish any empirical distribution.

## Validity rule

Top-level codes:

```text
VALID
MISSING_CHANNEL_1
MISSING_CHANNEL_2
MISSING_CHANNEL_3
ACQUISITION_FAILURE
TIMING_FAILURE
```

A/B/C disagreement is never itself an invalidity condition.

A channel disagreeing with the commanded actuator position is never itself an invalidity condition.

No trial may be removed because it weakens agreement.

## Required realization manifest

Before any trial, bind:

```text
APPARATUS_NAME
APPARATUS_VERSION
SWITCH_MANUFACTURER_IF_AVAILABLE
SWITCH_MODEL_OR_UNIQUE_DESCRIPTION
SWITCH_SERIAL_OR_PHOTO_ID
LOGGER_OR_ACQUISITION_DEVICE
EXACT_CHANNEL_IDENTIFIERS
WIRING_MANIFEST
INTERFACE_SCHEMA_VERSION
SETTLE_INTERVAL
TRIAL_COUNT
TRIAL_SCHEDULE
VALIDITY_RULE_VERSION
RAW_FILE_PATH
CUSTODY_PATH
HASH_ALGORITHM = SHA-256
PUBLIC_OR_AUDITABLE_ACCESS_PATH
```

If a switch has no serial number, a stable photo identifier plus physical markings/description must be bound before data.

## Pre-data custody sequence

```text
FREEZE_APPARATUS_MANIFEST
-> FREEZE_CHANNEL_IDS_AND_ROLES
-> FREEZE_NEGATIVE_ONLY_ANALYSIS
-> ONLY_THEN_BEGIN_TRIAL_001
-> COMPLETE_FIXED_512_TRIAL_RANGE
-> CLOSE_RAW_FILE
-> HASH_RAW_FILE
-> COMMIT_OR_OTHERWISE_AUDITABLY_FREEZE_RAW_FILE_AND_HASH
```

No response rows may be inspected for model behavior before the analysis preregistration is frozen.

## Scientific interpretation

The design intentionally creates a physical common-state architecture expected to stress the `T_ind` common-bit exclusion.

```text
DESIGN_EXPECTATION = NOT_EVIDENCE
QUALIFIED_REJECT_T_ind = MAY_REFUTE_PGH_OBJ_0052_AT_TARGET
DO_NOT_REJECT_T_ind = ZERO_POSITIVE_EMPIRICAL_CREDIT
INCONCLUSIVE = NO_VERDICT
```

## Not yet authorized

```text
BUY_OR_SELECT_SPECIFIC_HARDWARE = NOT_DONE
ASSEMBLY = NOT_DONE
TARGET_FREEZE = NOT_DONE
ANALYSIS_PREREGISTRATION = NOT_DONE
PHYSICAL_DATA_GENERATION = FORBIDDEN
```
