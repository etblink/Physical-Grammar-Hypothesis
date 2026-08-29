# CURRENT STATE

## Project status

```text
PROJECT = Physical Grammar Hypothesis
CURRENT_PHASE = PGH-1_HURDAT2_RAW_DATA_CUSTODY_QUALIFICATION
ACTIVE_PHYSICAL_PREDICTIVE_CANDIDATE = FIVE_PACKAGE_FAMILY__PGH_OBJ_0041_TO_0045
COMMON_TARGET = PGH-OBJ-0048__TGT-008__ATLANTIC_HURDAT2_SYSTEM_STATUS
TARGET_RANGE = 1988-2025
TARGET_SPECIFIC_ANALYSIS_PROTOCOL = PGH-OBJ-0049
TARGET_VALUES_ACCESSED = NO
EMPIRICAL_FAMILY_PROTOCOL = PGH-OBJ-0047
FROZEN_ACCEPTED_SOURCES = 106
FCP_EFFECT = NONE
```

## Pre-data analysis status

`PGH-OP-0088` is canonically complete. The five target-specific G2 statistics, CAL1 and CAL2, Holm familywise decision rules, HURDAT2 parser/support semantics, exact RNG/sampling rules and reference implementation are frozen before real target access.

The canonical analysis-protocol commit is `802d5bf7858b00d4df5a1e6b955b65d16455ae6d`. This exact SHA is an input to the master-seed derivation after raw custody establishes the HURDAT2 SHA-256.

## Next boundary

`PGH-OP-0090` is authorized for raw-data custody and parser/support qualification only. It may retrieve the exact official NHC Atlantic HURDAT2 1851-2025 release, hash it, derive the master seed, and run `--parse-only`. It must stop before any primary G2 output, CAL1/CAL2 execution, or candidate verdict.

## Navigation state

```text
LATEST_COMPLETED_OPERATION = POST_PGH1_HURDAT2_ANALYSIS_PREREG_NAVIGATION_RECONCILIATION
REGISTRY_ID = PGH-OP-0089
INDEXED_SCIENTIFIC_BASELINE = 802d5bf7858b00d4df5a1e6b955b65d16455ae6d
NEXT_RECOMMENDED_OPERATION = PGH1_HURDAT2_RAW_DATA_CUSTODY_AND_PARSER_SUPPORT_QUALIFICATION
NEXT_OPERATION_AUTHORIZED = YES
REGISTRY_ID_NEXT = PGH-OP-0090
```

<!-- PGH_CURRENT_STATE_CAPSULE_BEGIN -->
```json
{"capsule_schema_version":"0.1.0","project":"Physical Grammar Hypothesis","current_phase":"PGH-1_HURDAT2_RAW_DATA_CUSTODY_QUALIFICATION","canonical_hypothesis":"HYPOTHESIS.md","active_candidate_grammar":null,"current_handoff":"handoffs/POST_PGH1_HURDAT2_ANALYSIS_PREREG_NAVIGATION_RECONCILIATION_HANDOFF_0_1_0.md","source_bound_status":"106_DISTINCT_ACCEPTED_SOURCES_FROZEN__TGT_008_FROZEN__PGH_OBJ_0049_PRE_DATA_PROTOCOL_QUALIFIED","fcp_relationship":"INDEPENDENT_NO_EFFECT","next_recommended_operation":"PGH1_HURDAT2_RAW_DATA_CUSTODY_AND_PARSER_SUPPORT_QUALIFICATION","next_operation_authorized":true,"open_question_count":8,"do_not_assume":["RAW_HURDAT2_HAS_BEEN_DOWNLOADED","REAL_PARSER_HAS_RUN","ANY_G2_HAS_BEEN_COMPUTED","ANY_MONTE_CARLO_HAS_RUN","ANY_CANDIDATE_HAS_SURVIVED_OR_FAILED","R2B_HAS_PASSED"]}
```
<!-- PGH_CURRENT_STATE_CAPSULE_END -->

Truth over PGH.
