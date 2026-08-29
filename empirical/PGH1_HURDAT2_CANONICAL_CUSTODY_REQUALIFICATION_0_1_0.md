# PGH-1 HURDAT2 Canonical Custody Requalification 0.1.0

```text
OPERATION_ID = PGH1_HURDAT2_CUSTODY_TRANSPORT_REPAIR_AND_REQUALIFICATION
REGISTRY_ID = PGH-OP-0092
STATUS = QUALIFIED_CANDIDATE
OUTCOME = A__CANONICAL_CUSTODY_REQUALIFIED_WITH_HISTORICAL_TRANSPORT_INCIDENT_RETAINED
TARGET = PGH-OBJ-0048__TGT-008
ANALYSIS_PROTOCOL = PGH-OBJ-0049
ANALYSIS_PROTOCOL_COMMIT = 802d5bf7858b00d4df5a1e6b955b65d16455ae6d
PRIMARY_STATISTICS_EXECUTED = NO
CAL1_EXECUTED = NO
CAL2_EXECUTED = NO
CANDIDATE_VERDICT = NONE
FCP_EFFECT = NONE
```

## Canonical custody binding

```text
CANONICAL_CUSTODY_MEDIUM = GITHUB_ACTIONS_ARTIFACT
ARTIFACT_ID = 9721043553
ARTIFACT_NAME = PGH1_TGT008_HURDAT2_RAW_CUSTODY
ARTIFACT_DIGEST = sha256:10a10afb2037287b820059727d1de8c6227be8c12f437b41b7c8cfc5c322af97
ARTIFACT_SIZE_IN_BYTES = 623250
ORIGINATING_WORKFLOW_RUN_ID = 33274366213
RAW_MEMBER = atlantic_hurdat2_1851_2025.txt
RAW_BYTE_COUNT = 7082381
RAW_SHA256 = 1b9b0c7beed5b4505838658b1d30e159fc84330c60891a58cfcf43ae55c37202
MASTER_SEED_HEX = f1a892274ed5782e7973cb19087cdb2ad5f03a21c840a9b6a75775a9b8f8ccd0
ANALYSIS_SOURCE_SHA256 = 1b7fcd8e1958d5614a73cdb2226465bb41f355fbc2d7c3e6769b1f8f488682d4
```

OP-0092 requalified the exact prior artifact without a fresh NHC download. The qualifying repository-side run was:

```text
QUALIFYING_WORKFLOW_RUN = 33275089950
QUALIFYING_JOB = 99160291377
WORKFLOW_CONCLUSION = SUCCESS
OP0092_ARTIFACT_METADATA = PASS
OP0092_ARTIFACT_DIGEST = PASS
OP0092_RAW_MEMBER_IDENTITY = PASS
OP0092_CUSTODY_METADATA = PASS
OP0092_REFERENCE_BUILD_SELFTEST = PASS
OP0092_PARSE_SUPPORT_EQUALITY = PASS
OP0092_PRIMARY_ANALYSIS_BOUNDARY = PASS
OP0092_NO_RAW_IN_GIT_TREE = PASS
OP0092_REQUALIFICATION = PASS
```

The immediately preceding temporary harness run `33274705228` failed before any job was created because the disposable workflow definition was invalid. Repairing that harness did not change the OP-0092 preregistration, artifact identity, parser, target, support rule, statistics, calibrations, or verdict logic.

## Parser/support requalification

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

The aggregate parser/support output exactly matches the equality target frozen in the OP-0092 preregistration. It is used only to establish custody/parser reproducibility and supplies no positive or negative evidence for H1-H5.

## Historical incident retained

```text
FAILED_OPERATION = PGH-OP-0090
HISTORICAL_RAW_IN_GIT_INCIDENT = YES
FIRST_CONSTRUCTION_COMMIT_CONTAINING_RAW = f560a5c5f9702f324a3139efff76cdc7dd7f0edb
CANONICAL_MAIN_EVER_CONTAINED_RAW = NO
RAW_GIT_OBJECT_PURGE_CLAIM = NO
INCIDENT_ERASED_BY_REPAIR = NO
```

OP-0092 does not rewrite OP-0090 as a success. It establishes a compliant canonical custody binding for later empirical execution while preserving the historical provenance feedback.

## Candidate-tree custody check

All downloaded and extracted artifact bytes existed only beneath `$RUNNER_TEMP` during the qualifying run. The workflow verified that no `atlantic_hurdat2_1851_2025.txt`, `custody_metadata.txt`, or `custody_payload` path was present in the candidate Git tree.

## Boundary

```text
PRIMARY_G2 = NOT_EXECUTED
CAL1 = NOT_EXECUTED
CAL2 = NOT_EXECUTED
HOLM = NOT_EXECUTED
CANDIDATE_VERDICT = NONE
FAMILY_VERDICT = NONE
```

Canonical custody qualification and parser support are technical prerequisites only. They do not confirm, support, refute, or rank the five successor candidates.
