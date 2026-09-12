# PGH-1 D1 Experiment Readiness Preparation — Handoff 0.1.0

## Exact disposition

```text
OPERATION = PGH1_D1_EXPERIMENT_READINESS_PREPARATION
BASE = d8a16161f33d3bb8f97c15f095ca651c169f5896
DESIGN_ID = PGH-EXP-DESIGN-0001
CANDIDATE_PACKAGE = PGH-OBJ-0052
READINESS_PREPARATION = PASS
DISPOSITION = PREPARED__NO_APPARATUS_BOUND__NO_TARGET_ASSIGNED__NO_DATA_GENERATED
```

## What is ready

Repository-side infrastructure is prepared for a future D1 physical realization:

- apparatus-realization and target-freeze operator checklist;
- apparatus manifest template;
- protocol manifest template;
- raw-record structural schema;
- standard-library structural/custody validator;
- deliberately mixed synthetic fixture set;
- explicit custody and non-editing rules;
- reconciled current-state navigation.

The package can test its own structural machinery without generating evidence or encoding a preferred response pattern.

## What reality must still supply

A later separately governed operation must bind the actual physical facts:

```text
REAL_THREE_POLE_SWITCH
REAL_SWITCH_IDENTITY
REAL_ACQUISITION_DEVICE
REAL_THREE_CHANNEL_IDENTIFIERS
REAL_WIRING_MANIFEST
REAL_PHYSICAL_DETENT_IDENTITIES
REAL_CUSTODY_PATH
REAL_ACCESS_PATH
ANY_PROSPECTIVE_ENGINEERING_DEVIATION_FROM_1000_MS_DEFAULT
```

Only after these are bound prospectively may the next available target identifier be assigned.

## Mandatory sequence from here

```text
1. APPARATUS_REALIZATION_AND_TARGET_FREEZE
2. NEGATIVE_ONLY_ANALYSIS_PREREGISTRATION
3. ONLY THEN PHYSICAL_TRIAL_EXECUTION_AND_RESPONSE_DATA
4. IMMUTABLE CUSTODY
5. PREREGISTERED ANALYSIS
6. EMPIRICAL ADJUDICATION
```

Step 2 must bind all deterministic replay details needed by the chosen finite-sample `T_ind` functional. If simulation is used, the PRNG, seed derivation, sampling mapping, software/runtime identity, and replicate counts must be frozen explicitly; earlier PGH experience established that underspecified RNG machinery weakens bitwise reproducibility even when a verdict is insensitive.

## Current stop state

```text
ACTUAL_APPARATUS = NONE_BOUND
TARGET_ID = NONE
NEXT_AVAILABLE_TARGET_ID = TGT-047
TGT_047_RESERVED = NO
TARGET_FREEZE = NOT_COMPLETE
ANALYSIS_PREREGISTRATION = NOT_COMPLETE
PHYSICAL_RESPONSE_DATA = NONE
PHYSICAL_TRIAL_EXECUTION_AUTHORIZED = NO
```

No additional repository-side scientific derivation is needed before the physical apparatus exists. The next honest scientific action is contact with the hardware, not another theoretical substitute.

Truth over PGH.