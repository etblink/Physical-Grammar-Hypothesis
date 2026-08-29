# PGH-1 Post-Kp Common-Target Discovery and Freeze — Handoff 0.1.0

## Result

```text
OPERATION_ID = PGH1_POST_KP_COMMON_TARGET_MULTI_CANDIDATE_TARGET_DISCOVERY_AND_FREEZE
REGISTRY_ID = PGH-OP-0086
OUTCOME = A__ONE_NEW_COMMON_TARGET_QUALIFIES_AND_IS_FROZEN
TARGET_ID = TGT-008
TARGET_OBJECT = PGH-OBJ-0048
TARGET = NOAA_NWS_NHC_ATLANTIC_HURDAT2_STANDARD_SYNOPTIC_SYSTEM_STATUS
FROZEN_RANGE = 1988-2025
NATIVE_ALPHABET_SIZE = 9
TARGET_VALUES_ACCESSED = NO
RAW_DATA_DOWNLOADED = NO
DEPENDENCE_ANALYSIS = NO
FCP_EFFECT = NONE
```

## Scientific meaning

The five post-Kp successor packages now have one common prospectively selected empirical target. The target was selected solely from preregistered metadata architecture. Atlantic HURDAT2 tied the NE/NC Pacific HURDAT2 on the 19/20 metadata score and won only the frozen T7 tie break because its public archive begins earlier (1851 vs. 1949).

No selection credit comes from expected tropical-cyclone behavior, and no candidate has survived or failed anything yet.

## Binding target realization

```text
RECORD = native HURDAT2 system status
ELIGIBLE_TIMES = standard 0000/0600/1200/1800 UTC only
SEGMENT = individual storm
CONTINUITY = exact six-hour timestamp adjacency
BLOCKING = nonoverlapping triples within each maximal continuous run
A = first status
B = second status
C = third status
NO_ROLE_PERMUTATION = YES
NO_GAP_COMPRESSION = YES
NO_CROSS_STORM_TRIPLES = YES
```

The frozen alphabet is `TD,TS,HU,EX,SD,SS,LO,WV,DB`.

## Next scientific work

The next operation should be a **target-specific analysis and custody sequencing/preregistration gate**, still without reading target values. It must translate the already-qualified family protocol to HURDAT2 while freezing complete implementation semantics before any stochastic computation.

At minimum it must decide prospectively:

1. exact raw-file release identity/custody procedure;
2. parser and retained-triple validation rules;
3. one statistic per frozen H1–H5 claim using a common finite-table framework where possible;
4. CAL1 and CAL2 constructions appropriate to storm-segmented categorical six-hour tracks;
5. Monte Carlo counts, deterministic seed derivation, PRNG, bounded-integer mapping, unit-uniform mapping, shuffle and categorical sampler semantics;
6. Holm implementation/tie handling at family alpha 0.01 separately for CAL1 and CAL2;
7. support/inconclusive gates and output serialization;
8. known-result quarantine and one-target stopping rule.

It must stop before raw-data materialization unless that same separately authorized operation explicitly includes a custody phase after the complete analysis preregistration is frozen.

## Hard boundary

```text
DO_NOT_OPEN_HURDAT2_RAW_FILE_YET
DO_NOT_INSPECT_STATUS_SEQUENCE
DO_NOT_ESTIMATE_ANY_OF_H1_TO_H5
DO_NOT_CHOOSE_A_CANDIDATE
DO_NOT_CHANGE_TARGET_RANGE_OR_ROLE_RULE
DO_NOT_USE_PACIFIC_HURDAT2_AS_BACKUP_AFTER_RESULTS
DO_NOT_SELECT_A_SECOND_TARGET
```

<!-- PGH_HANDOFF_CAPSULE_BEGIN -->
```json
{"capsule_schema_version":"0.1.0","operation_id":"PGH1_POST_KP_COMMON_TARGET_MULTI_CANDIDATE_TARGET_DISCOVERY_AND_FREEZE","registry_id":"PGH-OP-0086","status":"COMPLETE_CANDIDATE","target_id":"TGT-008","target_object":"PGH-OBJ-0048","target":"NOAA_NWS_NHC_ATLANTIC_HURDAT2_STANDARD_SYNOPTIC_SYSTEM_STATUS","outputs":["empirical/PGH1_POST_KP_COMMON_TARGET_CANDIDATE_LEDGER_0_1_0.md","empirical/PGH1_POST_KP_COMMON_TARGET_FREEZE_0_1_0.md","handoffs/PGH1_POST_KP_COMMON_TARGET_DISCOVERY_AND_FREEZE_HANDOFF_0_1_0.md"],"open_questions":["PGH-Q-0017"],"next_recommended_operation":"PGH1_POST_KP_HURDAT2_FIVE_CANDIDATE_ANALYSIS_AND_CUSTODY_PREREGISTRATION_GATE","next_operation_authorized":false,"do_not_assume":["RAW_DATA_HAS_BEEN_ACCESSED","ANY_CANDIDATE_HAS_SURVIVED","TROPICAL_CYCLONE_STATUS_IS_CAUSAL","PACIFIC_HURDAT2_IS_AN_AUTOMATIC_FALLBACK","R2B_HAS_PASSED"]}
```
<!-- PGH_HANDOFF_CAPSULE_END -->
