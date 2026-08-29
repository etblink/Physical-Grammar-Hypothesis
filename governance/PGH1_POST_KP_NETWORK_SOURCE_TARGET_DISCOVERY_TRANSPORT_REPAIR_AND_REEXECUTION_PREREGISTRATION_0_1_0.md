# PGH-1 Post-Kp Network/Source Target-Discovery Transport Repair and Reexecution — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_POST_KP_NETWORK_SOURCE_TARGET_DISCOVERY_TRANSPORT_REPAIR_AND_REEXECUTION
REGISTRY_ID = PGH-OP-0110
CANONICAL_BASE = aeecb48f29be06b41fe99b53a7a240559dd264d1
FAILED_DISCOVERY_OPERATION = PGH-OP-0108
FAILED_DISCOVERY_PREREGISTRATION = governance/PGH1_POST_KP_NETWORK_SOURCE_SUCCESSOR_TARGET_DISCOVERY_AND_FREEZE_PREREGISTRATION_0_1_0.md
CANDIDATE_PACKAGE = PGH-OBJ-0052
SCIENTIFIC_SELECTION_RULE_CHANGE = NONE
SEARCH_TRANSPORT_CHANGE = BATCHED_TO_SEPARATE_CALLS_ONLY
TARGET_VALUES = FORBIDDEN
DEPENDENCE_ANALYSIS = FORBIDDEN
DATA_CUSTODY = FORBIDDEN
TARGET_SPECIFIC_ANALYSIS = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Repair only the search-result provenance defect that forced OP-0108 Outcome D.

OP-0108 issued all five preregistered primary metadata queries in one tool batch. The returned surface did not preserve an auditable association between each result and its D1-D5 query/lane. This operation reissues the **same exact five query strings**, one query per call, so returned order and lane identity are captured separately.

No scientific target-selection rule is changed.

## Fully inherited rules

Every scientific rule in the OP-0108 preregistration remains binding without modification, including:

```text
CANDIDATE_PACKAGE = PGH-OBJ-0052
QUARANTINE = TGT-001..TGT-014
NATIVE_BINARY_RULE = UNCHANGED
PHYSICAL_RECORD_RULE = UNCHANGED
LANES_D1_D5 = UNCHANGED
E1_E12 = UNCHANGED
PER_LANE_MAX_CANDIDATES = 6
PER_LANE_ELIGIBLE_STOP = 2
MAX_ADJUDICATED = 30
MAX_ELIGIBLE = 10
FOLLOWUP_METADATA_QUERY_RULE = UNCHANGED
CANDIDATE_SET_CLOSURE = UNCHANGED
TARGET_SELECTION = LEXICOGRAPHIC_AUTHORITY_DATASET_RELEASE_TUPLE
FIELD_SELECTION = UNICODE_LEXICAL_FIRST_THREE_NATIVE_BINARY_FIELDS
ROLE_ASSIGNMENT = SAME_ORDER_TO_A_B_C
RANGE_RELEASE_RULE = UNCHANGED
CONTAMINATION_CLASSES = UNCHANGED
STOP_BOUNDARY = UNCHANGED
```

The OP-0108 preregistration is incorporated by reference. If this repair text conflicts with it on a scientific matter, the OP-0108 rule controls.

## Exact reissued primary queries

The five strings are byte-for-byte the same as OP-0108:

```text
D1_QUERY = official astronomy mission catalog data dictionary boolean flag table release
D2_QUERY = official space mission event catalog data dictionary boolean flag release
D3_QUERY = official particle physics open data event schema boolean field release
D4_QUERY = official geophysical environmental event catalog data dictionary boolean flag release
D5_QUERY = official gravitational wave neutrino high energy transient catalog schema boolean flag release
```

Execution rule:

```text
ONE_QUERY_PER_TOOL_CALL = REQUIRED
QUERY_ORDER = D1,D2,D3,D4,D5
NO_SECOND_PRIMARY_QUERY_PER_LANE = YES
RETURNED_RESULT_ORDER_RECORDED_BEFORE_NEXT_LANE = YES
```

## Prior repair provenance

OP-0108 newly encountered target-interface identities `TGT-015..TGT-021`. They remain permanent provenance.

If the exact same interface reappears, retain the same TGT ID and re-adjudicate only newly resolved metadata gates. Do not create a duplicate ID.

A genuinely distinct newly encountered candidate receives the next unused ID beginning at `TGT-022` in encounter order.

TGT-015..TGT-021 are **not** promoted merely because they were already seen. They must still pass E1-E12 under authoritative metadata.

## Returned-result accounting

For each lane, immediately record:

1. the returned official/institution-hosted results in encounter order;
2. which results are non-specific dictionaries, portals, papers, news, mirrors, or otherwise not specific candidate interfaces;
3. each distinct specific dataset/interface admitted to candidate adjudication;
4. the exact mandatory gate that rejects it, or the metadata supporting every passed gate;
5. any follow-up metadata query used for an already-entered candidate.

Search-engine snippets alone may identify a candidate but may not establish a mandatory gate when an official metadata/schema page is available.

## Repair-success condition

The transport repair itself succeeds only if all five lane calls return separately captured result sets sufficient to execute the frozen per-lane accounting.

If a lane call itself is unavailable or its result provenance is again unrecoverable, the operation must record a technical repair failure and stop rather than substitute another query.

## Target selection

Only after D1-D5 have each closed under the inherited budget may the eligible set close and the inherited lexicographic selection rule run.

No score, scientific preference, sample-size preference, familiarity preference, or expected model behavior may override the frozen tuple order.

## Outcome space

```text
A = TRANSPORT_REPAIR_PASSES__ONE_NEW_TARGET_QUALIFIES_AND_IS_FROZEN
B = TRANSPORT_REPAIR_PASSES__NO_DISCOVERED_TARGET_PASSES_ALL_MANDATORY_GATES
C = TRANSPORT_REPAIR_PASSES__OTHERWISE_ELIGIBLE_TARGETS_EXIST_BUT_ALL_ARE_C2_OR_C3_CONTAMINATED
D = TRANSPORT_REPAIR_PASSES__METADATA_OR_ACCESS_IS_INSUFFICIENT_TO_FREEZE_A_REPRODUCIBLE_TARGET
E = TRANSPORT_REPAIR_ITSELF_FAILS__LANE_RESULT_PROVENANCE_STILL_NOT_AUDITABLE
```

## Allowed outputs

Commit 2 may contain only:

```text
empirical/PGH1_POST_KP_NETWORK_SOURCE_TARGET_DISCOVERY_TRANSPORT_REPAIR_LEDGER_0_1_0.md
empirical/PGH1_POST_KP_NETWORK_SOURCE_TARGET_DISCOVERY_REPAIRED_TARGET_FREEZE_0_1_0.md
handoffs/PGH1_POST_KP_NETWORK_SOURCE_TARGET_DISCOVERY_TRANSPORT_REPAIR_HANDOFF_0_1_0.md
```

## Commit topology

```text
COMMIT_1 = THIS_PREREGISTRATION_ONLY
COMMIT_2 = REPAIR_LEDGER_TARGET_FREEZE_AND_HANDOFF_ONLY
EXACT_COMMITS = 2
```

## Stop boundary

```text
STOP_AFTER_TARGET_IDENTITY_AND_ROLE_FREEZE_IF_ANY
STOP_BEFORE_TARGET_VALUE_INSPECTION
STOP_BEFORE_RAW_DATA_DOWNLOAD_OR_MATERIALIZATION
STOP_BEFORE_DATA_CUSTODY
STOP_BEFORE_TARGET_SPECIFIC_STATISTIC_OR_MODEL_MEMBERSHIP_TEST
STOP_BEFORE_CALIBRATION_DESIGN
STOP_BEFORE_ANY_CANDIDATE_VERDICT
```

## Claim ceiling

```text
PGH_OBJ_0052_IDENTITY_CHANGED = NO
TARGET_MAY_BE_FROZEN = YES
EMPIRICAL_DATA_ACCESSED = NO
PGH_OBJ_0052_TESTED = NO
PGH_OBJ_0052_VALIDATED = NO
STRONG_PGH_CONFIRMED = NO
R2B = UNSATISFIED
FCP_EFFECT = NONE
```

Truth over PGH.
