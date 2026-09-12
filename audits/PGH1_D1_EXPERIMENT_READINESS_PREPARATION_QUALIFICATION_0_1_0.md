# PGH-1 D1 Experiment Readiness Preparation — Qualification 0.1.0

## Identity

```text
OPERATION = PGH1_D1_EXPERIMENT_READINESS_PREPARATION
CANONICAL_BASE = d8a16161f33d3bb8f97c15f095ca651c169f5896
CANONICAL_BASE_TREE = 772b0946912aeae73cfec6b1676e71911fb89cb5
BRANCH = preparation/pgh1-d1-experiment-readiness-v0.1
CONTROLLING_DESIGN = PGH-EXP-DESIGN-0001
CANDIDATE_PACKAGE = PGH-OBJ-0052
```

This is an infrastructure qualification only. It is not an empirical or scientific adjudication.

## Path-boundary result

Comparison from the exact base to the pre-qualification candidate showed a strict descendant with no divergence:

```text
STATUS = ahead
AHEAD_BY = 12
BEHIND_BY = 0
MERGE_BASE = d8a16161f33d3bb8f97c15f095ca651c169f5896
```

Changed paths before this qualification artifact were limited to:

```text
CURRENT_STATE.md
empirical/d1_readiness/APPARATUS_REALIZATION_CHECKLIST_0_1_0.md
empirical/d1_readiness/README.md
empirical/d1_readiness/apparatus_manifest.template.json
empirical/d1_readiness/protocol_manifest.template.json
empirical/d1_readiness/raw_record.schema.json
empirical/d1_readiness/synthetic/README.md
empirical/d1_readiness/synthetic/apparatus_manifest.synthetic.json
empirical/d1_readiness/synthetic/dry_run_valid.csv
empirical/d1_readiness/synthetic/protocol_manifest.synthetic.json
empirical/d1_readiness/validate_d1_capture.py
governance/PGH1_D1_EXPERIMENT_READINESS_PREPARATION_PREREGISTRATION_0_1_0.md
```

No candidate grammar, bridge, theorem, target ledger, real data artifact, or FCP artifact was modified.

## Synthetic structural replay

The committed fixture design was reproduced locally from the exact authored bytes using the committed standard-library-only validator contract.

Positive control:

```text
D1_STRUCTURAL_VALIDATION = PASS
MODE = synthetic
ROW_COUNT = 12
RAW_SHA256 = 2ee8442b151b12bb27da66091e1306abcb6fff84e9f38dc9c69d0ba399ff29f6
APPARATUS_MANIFEST_SHA256 = 3a8fb21443a2a2d0c63d25855a979c770d8890252e3d0b25c8efbc2348eef954
PROTOCOL_MANIFEST_SHA256 = fa7180cd9d258d5a3be705c5d2a848680860f7f0d011680572e3e007c1c8320c
VALIDATOR_SOURCE_SHA256 = af01a026a672d24c46ddcdfa8e6b3be4cd40bc1d6b623aaabb0a02e2e2c3fd8a
SCIENTIFIC_STATISTIC_COMPUTED = NO
SCIENTIFIC_VERDICT = NONE
```

The synthetic fixture deliberately contains both three-channel agreement and valid disagreement, every named single-channel missingness class, acquisition failure, and timing failure.

Negative structural control:

```text
MUTATION = trial 3 commanded position changed from ACTUATOR_POSITION_0 to ACTUATOR_POSITION_1
EXPECTED = FAIL
OBSERVED = FAIL
REASON = row 3: commanded position violates frozen odd/even schedule
SCIENTIFIC_STATISTIC_COMPUTED = NO
SCIENTIFIC_VERDICT = NONE
```

The malformed negative-control bytes were ephemeral and are not retained as an empirical or repository artifact.

## Preregistered gate adjudication

| Gate | Result | Basis |
|---|---|---|
| exact descendant of `d8a16161...` | PASS | compare metadata |
| bounded readiness-only paths | PASS | diff inspection |
| `TGT-047` remains unassigned | PASS | templates retain `UNBOUND`; synthetic target visibly synthetic |
| no fabricated real hardware identity | PASS | real templates contain `UNBOUND`; fixtures use `SYNTHETIC_*` |
| no physical response record | PASS | only explicitly synthetic fixture exists |
| native channel alphabet preserved | PASS | `{OPEN,CLOSED}` plus empty only for missingness |
| validity separated from channel state | PASS | schema + validator |
| forbidden copied/derived channels rejected | PASS | manifest flags must be false |
| final real schedule fixed at 512 | PASS | final validator requires exactly 512; synthetic mode is separately bounded |
| disagreement never invalid by itself | PASS | protocol flag false; disagreeing `VALID` rows pass synthetic replay |
| no analysis/statistical verdict logic | PASS | validator output explicitly `SCIENTIFIC_VERDICT=NONE` |
| current navigation reconciled | PASS | `CURRENT_STATE.md` names D1 gate as controlling state |
| stop at apparatus-realization boundary | PASS | no target freeze, analysis preregistration, or trials |

## Scientific firewall result

```text
ACTUAL_APPARATUS_BOUND = NO
ACTUAL_CHANNEL_IDS_BOUND = NO
TGT_047_ASSIGNED = NO
TARGET_VALUES_ACCESSED = NO
PHYSICAL_RESPONSE_DATA_GENERATED = NO
T_IND_DECISION_FUNCTIONAL_SELECTED = NO
EMPIRICAL_TEST_EXECUTED = NO
POSITIVE_EMPIRICAL_CREDIT = NONE
PGH_OBJ_0052_REFUTED = NO
PGH_OBJ_0052_SUPPORTED = NO
STRONG_PGH_CONFIRMED = NO
R2B = UNSATISFIED
```

## Qualification verdict

```text
READINESS_PREPARATION = PASS
DISPOSITION = PREPARED__NO_APPARATUS_BOUND__NO_TARGET_ASSIGNED__NO_DATA_GENERATED
NEXT_SCIENTIFIC_BOUNDARY = APPARATUS_REALIZATION_AND_TARGET_FREEZE
PHYSICAL_TRIAL_EXECUTION_AUTHORIZED = NO
```

Truth over PGH.