# PGH-1 Adversarial Physical-Interface Design Gate — Adjudication 0.1.0

## Identity

```text
OPERATION_ID = PGH1_ADVERSARIAL_PHYSICAL_INTERFACE_DESIGN_GATE
PREREGISTRATION_COMMIT = 37d4c871666654c33ef5c9c26eb6a2de761aab46
CANONICAL_BASE = 56ce58c3b13ba1188e096ed187c2a96c205e9b40
CANDIDATE_PACKAGE = PGH-OBJ-0052
NEW_EXTERNAL_SOURCE_SEARCH = NO
PHYSICAL_DATA_GENERATED = NO
TARGET_SELECTED = NO
TARGET_VALUES_ACCESSED = NO
```

## 1. Controlling result

```text
OUTCOME = A__D1_MECHANICALLY_GANGED_THREE_POLE_SWITCH_QUALIFIES
SELECTED_DESIGN = D1__MECHANICALLY_GANGED_THREE_POLE_SWITCH_INTERFACE
D2_COMMON_ARMATURE_RELAY = QUALIFIES_IN_PRINCIPLE_BUT_NOT_WEAKEST_ADEQUATE
D3_COMMON_OPTICAL_SOURCE = NOT_ESTABLISHED_AT_CLOSED_RECORD_SCOPE

ACTUAL_TARGET = NONE
NEXT_AVAILABLE_TARGET_ID = TGT-047__NOT_ASSIGNED
PGH_OBJ_0052_TESTED = NO
```

A mechanically common two-position actuator controlling three physically distinct contact poles is the weakest adequate adversarial physical-interface class under frozen `I`.

It is deliberately hostile because its common physical state is expected to drive the three observed binary contact channels toward a nondegenerate common-bit distribution, a formally known outside-model direction for `T_ind`. That expectation is **zero empirical evidence** and gives no positive-credit route.

## 2. C1-C14 adjudication

| Criterion | D1 switch | D2 relay | D3 optical |
|---|---|---|---|
| C1 common physical state | PASS | PASS | PASS |
| C2 three physically distinct binary channels | PASS | PASS | PASS_IN_PRINCIPLE |
| C3 native binary/no analyst threshold | PASS | PASS | NOT_ESTABLISHED |
| C4 repeated joint records feasible | PASS | PASS | PASS |
| C5 pre-data field/role determinism | PASS | PASS | PASS |
| C6 missing/invalid handling freeze | PASS | PASS | PASS_IN_PRINCIPLE |
| C7 stable identity bindable | PASS | PASS | PASS_IN_PRINCIPLE |
| C8 auditable custody feasible | PASS | PASS | PASS |
| C9 minimal auxiliary processing | PASS | PARTIAL | FAIL_RELATIVE_TO_D1 |
| C10 low software-copy risk | PASS | PASS | PASS_IN_PRINCIPLE |
| C11 direct common-bit stress | PASS | PASS | PASS |
| C12 unchanged G/J/S/I | PASS | PASS | NOT_ESTABLISHED_WITHOUT_CONCRETE_NATIVE_DIGITAL_DETECTORS |
| C13 pre-data analysis freeze feasible | PASS | PASS | PASS_IN_PRINCIPLE |
| C14 negative-only interpretation | PASS | PASS | PASS |

## 3. Why D1 passes

D1 supplies exactly the structural ingredients required for a severe but legitimate test:

```text
ONE_COMMON_MECHANICAL_ACTUATOR_STATE
THREE_SEPARATE_CONTACT_POLES
THREE_SEPARATE_ELECTRICAL_RECORD_CHANNELS
TWO_NATIVE_CONTACT_STATES_PER_CHANNEL = {OPEN,CLOSED}
ONE_JOINT_TRIAL_INDEX
NO_SOFTWARE_DUPLICATION
NO_POST_DATA_THRESHOLD
```

The common actuator is physical. Each contact pole is separately physical. The three records therefore do not arise by copying one recorded software value into three columns.

The interface does not require the target to contain three independent physical sources because frozen `I` does not impose that requirement and `S` is universal across `I`-eligible interfaces.

## 4. Why D2 is not selected

A common-armature three-pole relay can satisfy the same logical requirements, but it adds:

```text
COIL_DRIVE_ELECTRONICS
ENERGIZATION_TIMING
RELAY_PICKUP_AND_RELEASE_DYNAMICS
POSSIBLE_DRIVE_STATE_LOGIC
```

Those are not disqualifying, but they add auxiliary implementation and timing assumptions without improving the falsification logic.

Under the preregistered weakest-adequate rule, D1 dominates D2.

## 5. Why D3 does not qualify at this scope

An optical common-source design is scientifically plausible, but a generic optical detector is not enough to establish native binary semantics.

Without prospectively binding concrete detector hardware whose authoritative interface itself supplies a two-state digital output, the design risks moving an analyst-selected analog threshold into the measurement layer.

No external hardware/source search was authorized in this closed-record gate.

```text
D3_C3 = NOT_ESTABLISHED
D3_C12 = NOT_ESTABLISHED
```

D3 may be reconsidered in a separately sourced future design only if needed; it is unnecessary here because D1 already qualifies.

## 6. Frozen D1 physical architecture

The selected design class is:

```text
INTERFACE_CLASS = THREE_POLE_TWO_POSITION_MECHANICALLY_GANGED_DRY_CONTACT_INTERFACE
COMMON_STATE = ONE_MECHANICALLY_SHARED_TWO_POSITION_ACTUATOR
CHANNEL_COUNT = 3
CHANNEL_1 = PHYSICALLY_DISTINCT_CONTACT_POLE
CHANNEL_2 = PHYSICALLY_DISTINCT_CONTACT_POLE
CHANNEL_3 = PHYSICALLY_DISTINCT_CONTACT_POLE
RAW_ALPHABET_PER_CHANNEL = {OPEN,CLOSED}
```

The three poles must be electrically distinguishable acquisition paths.

Allowed recording architecture:

- three separately addressable dry-contact or digital input channels;
- one common logger/clock/storage device is permitted;
- each input must receive its state from its own physical contact pole;
- no software operation may derive one channel from another.

Forbidden:

```text
ONE_PHYSICAL_CONTACT_SPLIT_TO_THREE_SOFTWARE_FIELDS
ONE_GPIO_VALUE_COPIED_THREE_TIMES
DERIVED_BOOLEAN_COLUMNS
POST_DATA_CONTACT_STATE_RECODING
```

## 7. Prospective record schema

The future raw event record must contain at least:

```text
TRIAL_ID
CHANNEL_1_STATE
CHANNEL_2_STATE
CHANNEL_3_STATE
VALIDITY_CODE
ACQUISITION_TIMESTAMP
INTERFACE_VERSION
```

Substantive channel alphabets are exactly:

```text
OPEN
CLOSED
```

Non-substantive validity states are not channel values. Missing channels remain missing, not coerced to OPEN or CLOSED.

## 8. Joint record rule

One trial corresponds to one commanded stable actuator position and exactly one joint acquisition of all three contact channels.

At apparatus realization, a fixed settle interval must be frozen **before the first trial**. The default design requirement is:

```text
SETTLE_INTERVAL = 1000 milliseconds
SAMPLE_COUNT_PER_TRIAL = 1 joint sample
```

The settle interval may be changed before target freeze only if the apparatus-realization artifact prospectively replaces the default and supplies a non-response-based engineering reason. After target freeze it is immutable.

A/B/C disagreement after the frozen settle interval is response data and may not be reclassified as apparatus fault merely because it weakens the common-bit pattern.

## 9. Trial-state schedule

The future realization should use an exactly balanced deterministic schedule so both actuator states are represented without adaptive control:

```text
PLANNED_TRIAL_COUNT = 512
ODD_TRIALS = ACTUATOR_POSITION_0
EVEN_TRIALS = ACTUATOR_POSITION_1
POSITION_0_AND_POSITION_1_SEMANTICS = PHYSICAL_DETENT_IDENTITIES_FROZEN_AT_REALIZATION
```

The commanded actuator position is control metadata, not one of A/B/C and not used to choose or discard outcomes.

The alternating schedule is selected before data solely to guarantee a nondegenerate physical state occupation. It is not evidence that the recorded A/B/C distribution is a common bit.

## 10. Field identifiers and role assignment

Exact channel identifiers cannot be frozen until actual acquisition channels exist.

At apparatus realization, the three exact channel identifiers must be committed before the first trial. Then:

```text
SORT = Unicode code-point lexical order
A = first channel identifier
B = second channel identifier
C = third channel identifier
```

No post-data permutation is allowed.

## 11. Validity and missingness architecture

The future interface must use exactly these top-level validity classes or a prospectively frozen one-to-one refinement:

```text
VALID
MISSING_CHANNEL_1
MISSING_CHANNEL_2
MISSING_CHANNEL_3
ACQUISITION_FAILURE
TIMING_FAILURE
```

Rules:

- disagreement among A/B/C is never by itself invalid;
- a contact reading opposite the commanded actuator position is never by itself invalid;
- a trial may be invalid only for independently auditable acquisition/timing absence or failure;
- no validity rule may be altered after response data exist.

## 12. Apparatus identity burden before target freeze

A future apparatus-realization artifact must bind:

```text
APPARATUS_NAME
APPARATUS_VERSION
THREE_POLE_SWITCH_MANUFACTURER_IF_AVAILABLE
THREE_POLE_SWITCH_MODEL_OR_UNIQUE_PHYSICAL_DESCRIPTION
SWITCH_SERIAL_OR_PHOTO_ID_IF_NO_SERIAL
LOGGER_OR_ACQUISITION_DEVICE_IDENTITY
CHANNEL_IDENTIFIERS
WIRING_MANIFEST
INTERFACE_SCHEMA_VERSION
SETTLE_INTERVAL
TRIAL_COUNT
TRIAL_SCHEDULE
VALIDITY_RULE_VERSION
CUSTODY_PATH
HASH_ALGORITHM
PUBLIC_OR_AUDITABLE_ACCESS_PATH
```

If these are not available, target freeze fails rather than being inferred.

## 13. Data custody plan

Before the first trial, the apparatus-realization operation must freeze:

1. one append-only raw record file;
2. one apparatus manifest;
3. one protocol/version manifest;
4. SHA-256 hashing after capture closes;
5. a public repository path or equivalently auditable custody path for the raw record and manifests.

The project repository may serve as the authority/custody surface if the files and exact hashes are committed without alteration.

No response rows may be manually edited after capture. Corrections require a separately versioned immutable record with the original retained.

## 14. Expected common-bit direction

D1 is chosen because a common mechanical actuator is expected to create strong three-channel agreement.

That expectation has exactly this status:

```text
EXPECTED_OUTSIDE_MODEL_DIRECTION = YES
EMPIRICAL_EVIDENCE_FROM_EXPECTATION = ZERO
REFUTATION_FROM_DESIGN_ALONE = NO
```

The later physical data may:

- reject `T_ind` under a separately qualified analysis -> candidate refutation at target;
- fail to reject -> adversarial stress-test survival with zero positive empirical credit;
- remain analytically unresolved -> no verdict.

## 15. Analysis boundary

This design gate does not choose a `T_ind` finite-sample decision functional.

The next scientific sequence must be:

```text
APPARATUS_REALIZATION_AND_TARGET_FREEZE
-> NEGATIVE_ONLY_ANALYSIS_PREREGISTRATION
-> ONLY_THEN_PHYSICAL_TRIAL_EXECUTION_AND_RESPONSE_DATA
```

No trial may be generated before both target/interface freeze and analysis preregistration are canonical.

## 16. Target identity status

```text
ACTUAL_APPARATUS = NONE_BOUND
ACTUAL_CHANNEL_IDS = NONE_BOUND
TARGET_ID = NONE
NEXT_AVAILABLE_TARGET_ID = TGT-047
TGT_047_RESERVED = NO
TARGET_FREEZE = NOT_YET_POSSIBLE
```

The design class is qualified; an empirical target does not yet exist.

## 17. Claim ceiling

```text
PGH_OBJ_0052_REFUTED = NO
PGH_OBJ_0052_SUPPORTED = NO
PGH_OBJ_0052_TESTED = NO
PHYSICAL_GRAMMAR_FOUND = NO
STRONG_PGH_CONFIRMED = NO
R2B = UNSATISFIED
```

The operation establishes only that a concrete, minimally processed, in-principle `I`-compliant adversarial physical interface can be specified without changing the candidate.
