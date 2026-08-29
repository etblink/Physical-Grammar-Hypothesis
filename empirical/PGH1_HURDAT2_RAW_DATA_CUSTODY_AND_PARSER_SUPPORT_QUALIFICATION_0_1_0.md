# PGH-1 HURDAT2 Raw-Data Custody and Parser/Support Qualification 0.1.0

```text
OPERATION_ID = PGH1_HURDAT2_RAW_DATA_CUSTODY_AND_PARSER_SUPPORT_QUALIFICATION
REGISTRY_ID = PGH-OP-0090
STATUS = TECHNICAL_FAILURE
OUTCOME = RAW_GIT_CUSTODY_BOUNDARY_VIOLATION
TARGET = PGH-OBJ-0048__TGT-008
ANALYSIS_PROTOCOL = PGH-OBJ-0049
PRIMARY_STATISTICS_EXECUTED = NO
CAL1_EXECUTED = NO
CAL2_EXECUTED = NO
CANDIDATE_VERDICT = NONE
FCP_EFFECT = NONE
```

## Failure finding

The preregistered opaque custody workflow successfully resolved the official Atlantic HURDAT2 1851-2025 release, downloaded it, hashed it, uploaded an Actions custody artifact, compiled/self-tested the frozen reference implementation, and passed `--parse-only` support qualification.

However, the workflow failed its own custody rule:

```text
RAW_FILE_MUST_NEVER_BE_COMMITTED_TO_GIT = VIOLATED
```

The temporary upload directory was not removed before `git add -A`. Consequently the public raw HURDAT2 file and custody metadata entered an unintegrated custody-branch construction commit.

```text
FIRST_CONSTRUCTION_COMMIT_CONTAINING_RAW = f560a5c5f9702f324a3139efff76cdc7dd7f0edb
CANONICAL_MAIN_CONTAINED_RAW = NO
SCIENTIFIC_CANDIDATE_INTEGRATED = NO
CUSTODY_BRANCH_REF_REWOUND_TO_PREREGISTRATION = YES
RAW_GIT_OBJECT_PURGE_CONFIRMED = NO
```

Because the preregistration states that the raw file must never be committed to Git, OP-0090 cannot qualify as Outcome A even though its raw hash, Actions artifact, and parser/support evidence are internally consistent.

## Preserved non-result evidence

The following facts arose before the transport violation was discovered and are retained only to define the bounded repair; they are not a qualified OP-0090 custody result:

```text
WORKFLOW_RUN_ID = 33274366213
ARTIFACT_ID = 9721043553
ARTIFACT_DIGEST = sha256:10a10afb2037287b820059727d1de8c6227be8c12f437b41b7c8cfc5c322af97
RESOLVED_HREF = /data/hurdat/hurdat2-1851-2025-02272026.txt
RAW_BYTE_COUNT = 7082381
RAW_SHA256 = 1b9b0c7beed5b4505838658b1d30e159fc84330c60891a58cfcf43ae55c37202
MASTER_SEED_HEX = f1a892274ed5782e7973cb19087cdb2ad5f03a21c840a9b6a75775a9b8f8ccd0
RETAINED_TRIPLES = 5861
PARSER_SUPPORT_OBSERVED = PASS
```

Independent artifact recovery verified the archived raw-member byte count/SHA-256 and downloaded artifact ZIP SHA-256 without inspecting event/status rows.

## Epistemic status

No primary `G2`, CAL1, CAL2, Holm decision, candidate verdict, or family verdict was computed. Therefore the transport failure does not expose which PGH candidate is favored and does not consume the prospective empirical test.

The parser-support count is known, so any repair must be strictly transport-only: it may not change the target, date range, parser, status alphabet, support threshold, statistics, calibrations, or verdict rules.

## Required repair

A separately frozen repair/requalification operation may reuse the already immutable Actions artifact `9721043553` and its exact metadata. It must:

1. make no new target or analysis choice;
2. avoid recommitting the raw member to Git;
3. verify the artifact digest and raw-member SHA-256/byte count;
4. reconstruct the custody result from the artifact metadata;
5. if parser re-execution is performed, use the unchanged canonical source in `--parse-only` only;
6. produce a clean custody record/handoff with no raw or custody payload path in the Git tree;
7. stop before primary empirical execution.

Truth over PGH requires preserving this failure rather than retroactively describing OP-0090 as compliant.
