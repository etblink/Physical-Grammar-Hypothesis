# PGH-1 Adversarial Physical-Interface Design Gate — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_ADVERSARIAL_PHYSICAL_INTERFACE_DESIGN_GATE
OPERATION_CLASS = PRE_DATA_NEGATIVE_ONLY_INTERFACE_DESIGN
CANONICAL_BASE = 56ce58c3b13ba1188e096ed187c2a96c205e9b40
CANDIDATE_PACKAGE = PGH-OBJ-0052
ADVERSARIAL_FALSIFICATION_ROUTE = QUALIFIED
TARGET_SELECTED_AT_OPEN = NO
RESPONSE_DATA_ACCESS = FORBIDDEN
PHYSICAL_TRIAL_EXECUTION = FORBIDDEN
RAW_DATA_GENERATION = FORBIDDEN
CANDIDATE_REVISION = FORBIDDEN
NEW_EXTERNAL_SOURCE_SEARCH = FORBIDDEN
```

## 1. Purpose

Design and adjudicate one deliberately hostile physical record interface for a **negative-only** test of the universal `PGH-OBJ-0052` claim.

This operation does not generate physical data and does not test `T_ind`.

The selected design must satisfy the unchanged prospective instantiation burden of frozen `I` without relying on software copies, analyst thresholding, state merging, response-derived encoding, or post-data repair.

The operation may freeze an interface construction specification and a pre-data execution boundary. It may not freeze an actual empirical target until the physical apparatus exists and all target identity metadata required by `I` are instantiated.

## 2. Controlling scientific facts

The operation is bound to:

```text
G = PGH-GRAM-0010
J = PGH-OBJ-0051
S = TRUE_FOR_ALL_I_ELIGIBLE_PHYSICAL_RECORD_INTERFACES
I = SYMMETRIC_NATIVE_BINARY_TRIPLE_RECORD_INSTANTIATION_PROTOCOL_V0_1_0
PACKAGE = PGH-OBJ-0052
```

The canonical asymmetry audit establishes:

```text
ADVERSARIAL_I_ELIGIBLE_TARGET_SELECTION_FOR_REFUTATION_ONLY = ALLOWED
NONREJECTION_POSITIVE_CREDIT = ZERO
TARGET_MUST_SATISFY_FROZEN_I = YES
ANALYSIS_MUST_FREEZE_BEFORE_RESPONSE_DATA = YES
```

The canonical formal witness establishes:

```text
p_star(000)=1/2
p_star(111)=1/2
p_star NOT_IN T_ind
```

Knowledge of this witness may motivate a hostile interface, but it is not empirical evidence.

## 3. Frozen I requirements that no design may relax

A future realized interface must establish before target freeze:

```text
PUBLIC_OR_AUDITABLE_EVENT_LEVEL_ACCESS = YES
VERSIONED_OR_STABLY_IDENTIFIED_AUTHORITY = YES
REPEATED_JOINT_RECORD_INDEX = YES
AT_LEAST_THREE_DISTINCT_NATIVE_BINARY_RECORD_FIELDS = YES
SELECTED_FIELDS_JOINTLY_OBSERVED_PER_RECORD = YES
MISSINGNESS_OR_VALIDITY_CODES_DOCUMENTED = YES
```

Native binary means exactly two substantive authority-defined states, excluding documented missing/invalid states.

Forbidden:

```text
TARGET_SPECIFIC_THRESHOLDING
POST_DATA_BINNING
STATE_MERGING
LEARNED_ENCODING
RESPONSE_DERIVED_DISCRETIZATION
THREE_SOFTWARE_COPIES_OF_ONE_RECORDED_BIT
```

Hardware-native digital outputs or physical contact states may qualify only if the two-state semantics are fixed by the interface before data and are recorded as three physically distinct channels.

## 4. Exactly three design candidates

### D1 — mechanically ganged three-pole switch interface

One mechanically common two-position actuator controls three physically distinct electrical contact poles.

Each pole is recorded independently as a native binary contact state:

```text
FIELD_A_RAW = CONTACT_1_STATE in {OPEN,CLOSED}
FIELD_B_RAW = CONTACT_2_STATE in {OPEN,CLOSED}
FIELD_C_RAW = CONTACT_3_STATE in {OPEN,CLOSED}
```

The three contact circuits must be electrically distinguishable acquisition channels. A single software value copied into three columns is forbidden.

The actuator state itself is not one of A/B/C and need not be used in analysis.

### D2 — common-armature three-pole electromechanical relay interface

One coil drives one common electromechanical armature controlling three physically distinct contact poles. Each pole is independently recorded as `{OPEN,CLOSED}`.

The drive signal is not one of A/B/C.

### D3 — one binary optical source with three independent digital detector channels

One two-state physical optical source is observed by three physically distinct detector channels whose output interfaces are natively digital and fixed pre-data.

No analyst-selected intensity threshold or post-recording digitization is permitted.

No fourth design may be invented after adjudication begins.

## 5. Design criteria

Each D1-D3 receives `PASS`, `PARTIAL`, `FAIL`, or `NOT_ESTABLISHED` on:

```text
C1_PHYSICAL_COMMON_SOURCE_OR_COMMON_STATE_ARCHITECTURE
C2_THREE_PHYSICALLY_DISTINCT_BINARY_RECORD_CHANNELS
C3_NATIVE_BINARY_WITHOUT_ANALYST_THRESHOLDING
C4_REPEATED_JOINT_RECORD_INDEX_FEASIBLE
C5_PRE_DATA_FIELD_AND_ROLE_DETERMINISM
C6_MISSING_INVALID_HANDLING_CAN_BE_FROZEN
C7_STABLE_INTERFACE_IDENTITY_CAN_BE_BOUND
C8_PUBLIC_OR_AUDITABLE_EVENT_LEVEL_CUSTODY_FEASIBLE
C9_MINIMAL_AUXILIARY_PROCESSING
C10_LOW_RISK_OF_SOFTWARE_COPY_OBJECTION
C11_DIRECT_STRESS_OF_COMMON_BIT_EXCLUSION
C12_IMPLEMENTABLE_WITHOUT_CHANGING_G_J_S_I
C13_PRE_DATA_ANALYSIS_FREEZE_FEASIBLE
C14_RESULT_INTERPRETATION_IS_NEGATIVE_ONLY
```

A design qualifies only if C2-C8, C10, C12-C14 pass. C1, C9 and C11 may be comparative criteria used to choose the weakest adequate design.

If multiple designs qualify, choose the design with the least additional measurement machinery and fewest hidden analog-to-digital assumptions.

## 6. Required construction-level freeze if a design qualifies

The adjudication must freeze at least:

```text
SELECTED_DESIGN_CLASS
PHYSICAL_COMMON_STATE_MECHANISM
THREE_CHANNEL_DEFINITION
RAW_TWO_STATE_ALPHABET_PER_CHANNEL
JOINT_TRIAL_INDEX
TRIAL_VALIDITY_RULE
MISSING_INVALID_CODES
ROLE_ASSIGNMENT_RULE
DATA_RECORD_SCHEMA
APPARATUS_IDENTITY_FIELDS_REQUIRED_AT_REALIZATION
CUSTODY_AND_PUBLICATION_PLAN
PRE_DATA_NO_INSPECTION_RULE
```

The design may specify a future trial-count rule and drive/state schedule, but those do not instantiate a target until the apparatus exists and is assigned stable hardware/interface identity.

## 7. Common-bit witness discipline

The design may deliberately aim to realize strong three-channel agreement because the route is negative-only.

However:

```text
EXPECTED_COMMON_BIT_BEHAVIOR = ZERO_EMPIRICAL_EVIDENCE
DESIGN_INTENT = NOT_REFUTATION
ACTUAL_QUALIFIED_DATA_REQUIRED = YES
```

If the later physical record does not reject `T_ind`, the result is only adversarial stress-test survival with zero positive empirical credit.

## 8. Anti-artifact controls

A qualified design must make the following separable:

```text
COMMON_PHYSICAL_STATE
CHANNEL_1_PHYSICAL_CONTACT_OR_SENSOR
CHANNEL_2_PHYSICAL_CONTACT_OR_SENSOR
CHANNEL_3_PHYSICAL_CONTACT_OR_SENSOR
RECORDING_PATH
```

The recording system may share clocking and storage, but each A/B/C value must originate from a distinct physical channel.

Forbidden shortcuts include:

```text
ONE_GPIO_READ_COPIED_THREE_TIMES
ONE_SENSOR_STREAM_RELABELED_AS_THREE_FIELDS
SOFTWARE_DUPLICATION
POST_DATA_DEBOUNCE_TUNING
POST_DATA_THRESHOLD_TUNING
OUTCOME_DRIVEN_TRIAL_EXCLUSION
```

## 9. Pre-data validity rule architecture

The selected design must use an outcome-independent trial validity rule.

At minimum, a future realization must distinguish:

```text
VALID_TRIAL
MISSING_CHANNEL_1
MISSING_CHANNEL_2
MISSING_CHANNEL_3
APPARATUS_FAULT
TIMING_FAULT
```

A trial may not be marked invalid merely because A, B and C disagree.

Disagreement is response data, not an apparatus fault by definition.

## 10. Role assignment

The three physical channel identifiers must be frozen before data.

At realization, exact channel identifiers are sorted by Unicode code-point order and assigned:

```text
A = first identifier
B = second identifier
C = third identifier
```

No post-data channel permutation is allowed.

## 11. Data custody boundary

This design operation does not create event data.

A future realization must define before first trial:

```text
APPARATUS_MANIFEST
INTERFACE_VERSION
CHANNEL_IDENTIFIERS
RECORD_SCHEMA_VERSION
TRIAL_RANGE_RULE
CUSTODY_LOCATION
RAW_FILE_NAMING_RULE
HASH_ALGORITHM
HASH_RECORDING_LOCATION
PUBLIC_OR_AUDITABLE_ACCESS_PATH
```

## 12. Outcome space

Exactly one outcome:

```text
A = D1_MECHANICALLY_GANGED_THREE_POLE_SWITCH_QUALIFIES
B = D2_COMMON_ARMATURE_THREE_POLE_RELAY_QUALIFIES
C = D3_COMMON_OPTICAL_SOURCE_THREE_DIGITAL_DETECTORS_QUALIFIES
D = NO_ADVERSARIAL_PHYSICAL_INTERFACE_DESIGN_QUALIFIES
```

## 13. Output boundary

The adjudication commit may create exactly:

```text
audits/PGH1_ADVERSARIAL_PHYSICAL_INTERFACE_DESIGN_GATE_0_1_0.md
research/experimental-designs/PGH1_ADVERSARIAL_COMMON_STATE_INTERFACE_SPEC_0_1_0.md
handoffs/PGH1_ADVERSARIAL_PHYSICAL_INTERFACE_DESIGN_GATE_HANDOFF_0_1_0.md
```

No data file, target freeze, analysis result, or candidate verdict may be created.

## 14. Stop boundary

If a design qualifies, stop after freezing the construction and custody specification.

The next operation must be a separate apparatus-realization and target-freeze operation. That operation may require external hardware/human action.

```text
PHYSICAL_APPARATUS_EXISTS = NOT_ASSUMED
TARGET_ID = NONE
TARGET_VALUES = NONE
PGH_OBJ_0052_TESTED = NO
```

Truth over PGH requires making the universal claim face the hardest legitimate in-scope physical interface, while keeping construction intent separate from empirical evidence.
