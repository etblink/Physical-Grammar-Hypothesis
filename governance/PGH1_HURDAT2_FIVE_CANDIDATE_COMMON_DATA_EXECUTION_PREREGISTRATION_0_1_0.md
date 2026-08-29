# PGH-1 HURDAT2 Five-Candidate Common-Data Execution — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_HURDAT2_FIVE_CANDIDATE_COMMON_DATA_EXECUTION
REGISTRY_ID = PGH-OP-0094
CANONICAL_BASE = 752f4ff5889844c3df0f85e7b421cd71038bd90c
TARGET = PGH-OBJ-0048__TGT-008__ATLANTIC_HURDAT2_SYSTEM_STATUS
FAMILY_PROTOCOL = PGH-OBJ-0047
ANALYSIS_PROTOCOL = PGH-OBJ-0049
ANALYSIS_PROTOCOL_COMMIT = 802d5bf7858b00d4df5a1e6b955b65d16455ae6d
CANONICAL_CUSTODY_ARTIFACT_ID = 9721043553
FCP_EFFECT = NONE
```

This operation executes the already frozen empirical protocol. It does not select a target, candidate, statistic, calibration, multiplicity rule, seed, parser, role mapping, or verdict rule.

## Exact immutable inputs

```text
ARTIFACT_ID = 9721043553
ARTIFACT_NAME = PGH1_TGT008_HURDAT2_RAW_CUSTODY
ARTIFACT_DIGEST = sha256:10a10afb2037287b820059727d1de8c6227be8c12f437b41b7c8cfc5c322af97
ORIGINATING_WORKFLOW_RUN_ID = 33274366213
RAW_MEMBER = atlantic_hurdat2_1851_2025.txt
RAW_BYTE_COUNT = 7082381
RAW_SHA256 = 1b9b0c7beed5b4505838658b1d30e159fc84330c60891a58cfcf43ae55c37202
ANALYSIS_SOURCE = tools/pgh_hurdat2_five_candidate.cpp
ANALYSIS_SOURCE_SHA256 = 1b7fcd8e1958d5614a73cdb2226465bb41f355fbc2d7c3e6769b1f8f488682d4
MASTER_SEED_HEX = f1a892274ed5782e7973cb19087cdb2ad5f03a21c840a9b6a75775a9b8f8ccd0
EXPECTED_RETAINED_TRIPLES = 5861
```

Any mismatch is a technical failure. No alternate release, mirror, artifact, source, seed, parser, candidate family, role ordering, or range is permitted.

## Canonical executable invocation

```text
BUILD = g++ -std=c++20 -O2 -Wall -Wextra -pedantic -Werror tools/pgh_hurdat2_five_candidate.cpp -o $RUNNER_TEMP/pgh_hurdat2_five_candidate
SELF_TEST = $RUNNER_TEMP/pgh_hurdat2_five_candidate --self-test
ANALYZE = $RUNNER_TEMP/pgh_hurdat2_five_candidate --analyze <temporary-raw-member> f1a892274ed5782e7973cb19087cdb2ad5f03a21c840a9b6a75775a9b8f8ccd0
```

The raw artifact and all extracted raw bytes must remain beneath `$RUNNER_TEMP`; no raw payload may be staged or committed to Git.

## Frozen scientific execution

The executable must use its compiled constants and frozen implementation exactly:

```text
H1 = A independent C
H2 = A independent B given C
H3 = A independent B
H4 = B independent C given A
H5 = B independent C
CAL1_REPLICATES = 4999
CAL2_REPLICATES = 1999
FAMILY_ALPHA = 0.01
MULTIPLICITY = HOLM_STEP_DOWN_SEPARATELY_FOR_CAL1_AND_CAL2
```

Candidate and family verdicts are those already implemented by PGH-OBJ-0049. The execution wrapper may not override, reinterpret, soften, strengthen, or recompute them using another rule.

## Environment and output custody

Before execution, record:

```text
GIT_HEAD
ANALYSIS_SOURCE_SHA256
COMPILER_VERSION
OS_RELEASE
KERNEL
ARCHITECTURE
SIZEOF_LONG_DOUBLE
LIBC_VERSION
```

The complete stdout from the single successful `--analyze` invocation must be preserved verbatim. It must contain exactly one family verdict and exactly one H1-H5 `G2`, CAL1 exceedance, CAL2 exceedance, CAL1 Holm, CAL2 Holm, and candidate-verdict record per candidate, plus parser/support audit fields and `SURVIVAL_IS_CONFIRMATION=NO`.

The execution workflow may archive the verbatim machine output and environment record as a GitHub Actions artifact. Those files are result evidence, not raw data.

## Technical-failure discipline

A run is technical failure if any of the following occurs before a valid complete machine result exists:

```text
ARTIFACT_METADATA_MISMATCH
ARTIFACT_DIGEST_MISMATCH
RAW_HASH_OR_SIZE_MISMATCH
ANALYSIS_SOURCE_HASH_MISMATCH
STRICT_BUILD_FAILURE
SELF_TEST_FAILURE
PARSER_OR_SUPPORT_FAILURE
ANALYZE_NONZERO_EXIT
MISSING_OR_DUPLICATE_REQUIRED_RESULT_KEY
RAW_PAYLOAD_IN_GIT_TREE
```

A technical rerun, if needed, must use exactly the same frozen inputs and must record the failed attempt. A scientifically unfavorable result is not a technical failure and is never grounds for rerun.

## Result construction

After one valid successful machine execution, only these result paths may enter Commit 2:

```text
empirical/PGH1_HURDAT2_FIVE_CANDIDATE_COMMON_DATA_MACHINE_OUTPUT_0_1_0.txt
empirical/PGH1_HURDAT2_FIVE_CANDIDATE_COMMON_DATA_EXECUTION_RESULT_0_1_0.md
handoffs/PGH1_HURDAT2_FIVE_CANDIDATE_COMMON_DATA_EXECUTION_HANDOFF_0_1_0.md
```

The machine-output file must be a verbatim copy of executable stdout. The Markdown result may only bind identities, reproduce machine-emitted values/verdicts, apply the already-preregistered claim ceiling, and record environment/provenance. No post-result candidate repair, role reassignment, scope narrowing, graph substitution, or second-target launch is allowed in this operation.

## Commit topology

```text
COMMIT_1 = THIS_EXECUTION_PREREGISTRATION_ONLY
COMMIT_2 = THREE_RESULT_PATHS_ONLY
EXACT_SCIENTIFIC_COMMITS = 2
```

Temporary workflows/helpers and GitHub Actions execution artifacts must not enter the clean two-commit ancestry.

## Stop rule

After Commit 2 is qualified and canonically integrated:

```text
STOP_AFTER_FAMILY_RESULT
NO_AUTOMATIC_SECOND_TARGET
NO_FAILED_CANDIDATE_REPLACEMENT
NO_SCOPE_NARROWING
NO_ROLE_REASSIGNMENT
NO_GRAPH_REPAIR
```

A separate post-result scientific adjudication is required before any successor sequencing.

## Claim ceiling

```text
SURVIVAL_IS_CONFIRMATION = NO
UNIQUE_SURVIVOR_AT_ONE_TARGET_IS_FUNDAMENTAL_SELECTION = NO
STRONG_PGH_CONFIRMED = NO
R2B = UNSATISFIED
ONE_TARGET_FAMILY_REFUTATION_IS_GLOBAL_REFUTATION_OF_ALL_CONCEIVABLE_PGH = NO
FCP_EFFECT = NONE
```
