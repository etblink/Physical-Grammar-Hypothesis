# PGH-1 HURDAT2 Custody Transport Repair and Requalification — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_HURDAT2_CUSTODY_TRANSPORT_REPAIR_AND_REQUALIFICATION
REGISTRY_ID = PGH-OP-0092
CANONICAL_BASE = 9251a77315e994ed884b4370d49cd3b6f1996f57
FAILED_OPERATION = PGH-OP-0090
TARGET = PGH-OBJ-0048__TGT-008__ATLANTIC_HURDAT2_SYSTEM_STATUS
ANALYSIS_PROTOCOL = PGH-OBJ-0049
ANALYSIS_PROTOCOL_COMMIT = 802d5bf7858b00d4df5a1e6b955b65d16455ae6d
PRIMARY_STATISTICS = FORBIDDEN
CAL1 = FORBIDDEN
CAL2 = FORBIDDEN
CANDIDATE_VERDICT = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Repair only the custody-transport defect canonically recorded by OP-0090. The repair must establish a compliant canonical custody binding to the already immutable GitHub Actions artifact without altering or reselecting any scientific object.

The historical raw-in-Git incident remains true and must remain visible. This operation does not claim object-database purge and does not rewrite OP-0090 as a success.

## Immutable evidence bound before repair

```text
FAILED_WORKFLOW_RUN_ID = 33274366213
ACTIONS_ARTIFACT_ID = 9721043553
ACTIONS_ARTIFACT_NAME = PGH1_TGT008_HURDAT2_RAW_CUSTODY
ACTIONS_ARTIFACT_DIGEST = sha256:10a10afb2037287b820059727d1de8c6227be8c12f437b41b7c8cfc5c322af97
EXPECTED_RAW_MEMBER = atlantic_hurdat2_1851_2025.txt
EXPECTED_RAW_BYTE_COUNT = 7082381
EXPECTED_RAW_SHA256 = 1b9b0c7beed5b4505838658b1d30e159fc84330c60891a58cfcf43ae55c37202
EXPECTED_MASTER_SEED = f1a892274ed5782e7973cb19087cdb2ad5f03a21c840a9b6a75775a9b8f8ccd0
EXPECTED_ANALYSIS_SOURCE_SHA256 = 1b7fcd8e1958d5614a73cdb2226465bb41f355fbc2d7c3e6769b1f8f488682d4
```

The known aggregate support report from the failed transport attempt is permitted only as an equality target for requalification:

```text
STORMS = 2004
RAW_RECORDS = 55605
IN_RANGE_RECORDS = 18702
STANDARD_RECORDS = 18192
RECOGNIZED_RECORDS = 18192
UNRECOGNIZED_STATUS_BREAKS = 0
CONTINUITY_BREAKS = 0
RUNS = 626
RETAINED_TRIPLES = 5861
TRAILING_RECORDS_DISCARDED = 609
PGH_HURDAT2_PARSE_QUALIFICATION = PASS
```

These facts may not be used to change any scientific rule, target, threshold, candidate, statistic, calibration or verdict.

## Repair execution

The repair workflow must:

1. use the repository-scoped GitHub token to retrieve artifact metadata for artifact ID `9721043553`;
2. require the exact artifact name, digest, workflow run binding, and non-expired status;
3. download that exact prior-run artifact using GitHub Actions artifact machinery;
4. extract/download it only beneath `$RUNNER_TEMP`, never beneath the repository checkout;
5. find exactly one expected raw member and exactly one `custody_metadata.txt` member;
6. verify the raw member byte count and SHA-256 against the values above;
7. verify the metadata member binds the same raw SHA, byte count, analysis commit, source SHA and master seed;
8. compile the canonical `tools/pgh_hurdat2_five_candidate.cpp` under the frozen strict C++20 build;
9. verify its source SHA-256;
10. run `--self-test`;
11. run only `--parse-only` against the temporary raw member;
12. require exact equality of the aggregate parser/support output listed above;
13. reject any parser output containing `_G2=`, `_CAL1_`, `_CAL2_`, `_VERDICT=` or `FAMILY_VERDICT=`;
14. remove all temporary workflow/helper files before scientific candidate construction;
15. verify no raw/custody payload file is present anywhere in the candidate Git tree.

## No new retrieval or method choice

```text
NEW_NHC_DOWNLOAD = FORBIDDEN
TARGET_SUBSTITUTION = FORBIDDEN
RELEASE_SUBSTITUTION = FORBIDDEN
RANGE_CHANGE = FORBIDDEN
PARSER_CHANGE = FORBIDDEN
STATUS_MAP_CHANGE = FORBIDDEN
SUPPORT_THRESHOLD_CHANGE = FORBIDDEN
STATISTIC_CHANGE = FORBIDDEN
CALIBRATION_CHANGE = FORBIDDEN
CANDIDATE_CHANGE = FORBIDDEN
```

If the immutable artifact cannot be requalified exactly, the repair fails. No fallback download or alternate artifact is authorized.

## Qualification outcomes

```text
A = CANONICAL_CUSTODY_REQUALIFIED_WITH_HISTORICAL_TRANSPORT_INCIDENT_RETAINED
B = ARTIFACT_METADATA_OR_DIGEST_MISMATCH
C = RAW_MEMBER_HASH_OR_SIZE_MISMATCH
D = CUSTODY_METADATA_MISMATCH
E = REFERENCE_BUILD_OR_SELF_TEST_FAILURE
F = PARSER_SUPPORT_REQUALIFICATION_MISMATCH
G = RAW_OR_CUSTODY_PAYLOAD_REENTERS_GIT
H = PRIMARY_ANALYSIS_BOUNDARY_VIOLATION
```

Only Outcome A may hand off to empirical execution.

## Scientific outputs

After this preregistration, only:

```text
empirical/PGH1_HURDAT2_CANONICAL_CUSTODY_REQUALIFICATION_0_1_0.md
handoffs/PGH1_HURDAT2_CUSTODY_TRANSPORT_REPAIR_AND_REQUALIFICATION_HANDOFF_0_1_0.md
```

may enter the clean scientific result commit.

Raw bytes, extracted artifact members, temporary scripts/workflows and validation reports must not enter that tree.

## Commit topology

```text
COMMIT_1 = THIS_PREREGISTRATION_ONLY
COMMIT_2 = REQUALIFICATION_RESULT_AND_HANDOFF_ONLY
EXACT_SCIENTIFIC_COMMITS = 2
```

## Stop boundary

```text
STOP_BEFORE_PRIMARY_G2
STOP_BEFORE_CAL1
STOP_BEFORE_CAL2
STOP_BEFORE_HOLM
STOP_BEFORE_CANDIDATE_VERDICT
STOP_BEFORE_FAMILY_ADJUDICATION
```

## Claim ceiling

```text
CANONICAL_CUSTODY_MAY_BE_REQUALIFIED = YES
HISTORICAL_TRANSPORT_INCIDENT_ERASED = NO
RAW_GIT_OBJECT_PURGE_CLAIM = NO
EMPIRICAL_HYPOTHESES_TESTED = NO
STRONG_PGH_CONFIRMED = NO
R2B = UNSATISFIED
FCP_EFFECT = NONE
```
