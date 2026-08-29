# PGH-1 HURDAT2 Raw-Data Custody and Parser/Support Qualification — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_HURDAT2_RAW_DATA_CUSTODY_AND_PARSER_SUPPORT_QUALIFICATION
REGISTRY_ID = PGH-OP-0090
CANONICAL_BASE = b33df644570ad0cbc8cbc0e8d9269162c361e072
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

Establish byte-stable custody of the exact official NHC Atlantic HURDAT2 1851-2025 release, derive the already-frozen master seed from its raw SHA-256 and the canonical OP-0088 analysis-protocol commit, and run only the frozen parser/data-support qualification.

This operation is not empirical hypothesis execution. It may expose only aggregate parser/support counts required to decide whether the frozen target is technically executable.

## Official-source resolution

The workflow must begin from:

```text
METADATA_PAGE = https://www.nhc.noaa.gov/data/
```

It must fetch that page using HTTPS and resolve exactly one Atlantic HURDAT2 raw-data href satisfying all of:

```text
HOST = www.nhc.noaa.gov OR nhc.noaa.gov
PATH_PREFIX = /data/hurdat/
BASENAME_PREFIX = hurdat2-1851-2025-
EXTENSION = .txt
MATCH_COUNT = EXACTLY_1
```

The selected href must be present in the fetched NHC metadata page itself. A guessed filename, search-engine mirror, GitHub copy, third-party archive, Pacific HURDAT2 file, different year release, or manually substituted URL is forbidden.

If the metadata page cannot be fetched, if zero/multiple matching hrefs exist, or if the resolved URL leaves the allowed NHC host/path, the operation stops inconclusive before raw download.

## Raw retrieval and custody

The exact resolved raw bytes must be downloaded by HTTPS without printing file content. Record:

```text
METADATA_PAGE_FETCH_SHA256
RESOLVED_HREF
RESOLVED_ABSOLUTE_URL
EFFECTIVE_DOWNLOAD_URL
FETCH_UTC
RAW_BYTE_COUNT
RAW_SHA256
```

The raw file must never be committed to Git. It must be uploaded unchanged as a GitHub Actions artifact together with a machine-readable custody metadata file. The result record must bind the workflow run, artifact ID, artifact digest if available, and artifact URL if available.

No line, row, storm record, or status sequence from the raw file may be emitted to the workflow log or scientific Markdown artifact.

## Master-seed derivation

After `RAW_SHA256` is known, derive the master seed as SHA-256 of the exact UTF-8 bytes:

```text
PGH1_TGT008_HURDAT2_FIVE_CANDIDATE_0_1_0\n
RAW_SHA256=<64 lowercase hex>\n
ANALYSIS_PROTOCOL_COMMIT=802d5bf7858b00d4df5a1e6b955b65d16455ae6d\n
```

The resulting 64-lowercase-hex digest is `MASTER_SEED_HEX`.

No other entropy, clock time, workflow ID, artifact ID, parser count, or target value enters the master seed.

## Exact parser qualification

Compile the canonical source:

```text
SOURCE = tools/pgh_hurdat2_five_candidate.cpp
SOURCE_SHA256 = 1b7fcd8e1958d5614a73cdb2226465bb41f355fbc2d7c3e6769b1f8f488682d4
BUILD = g++ -std=c++20 -O2 -Wall -Wextra -pedantic -Werror
```

Before raw parsing, run:

```text
./pgh_hurdat2_five_candidate --self-test
```

Then run exactly:

```text
./pgh_hurdat2_five_candidate --parse-only <raw-file>
```

The parser output may contain only the frozen aggregate audit/support fields and `PGH_HURDAT2_PARSE_QUALIFICATION=PASS`. The workflow must reject the operation if parser output contains any primary-statistic or decision tokens including:

```text
_G2=
_CAL1_
_CAL2_
_VERDICT=
FAMILY_VERDICT=
```

## Qualification outcomes

```text
A = RAW_CUSTODY_AND_PARSER_SUPPORT_QUALIFY
B = OFFICIAL_RELEASE_RESOLUTION_FAILURE
C = RAW_CUSTODY_HASH_OR_ARTIFACT_FAILURE
D = REFERENCE_SELF_TEST_OR_BUILD_FAILURE
E = PARSER_OR_DATA_SUPPORT_FAILURE
F = PRIMARY_ANALYSIS_BOUNDARY_VIOLATION
```

Only Outcome A may hand off to full five-candidate execution.

Parser/data-support failure is not evidence for or against any candidate. No alternate target, release, range, state map, gap rule, or parser repair is authorized inside this operation after real data access.

## Required result outputs

Exactly these scientific outputs are permitted after the preregistration:

```text
empirical/PGH1_HURDAT2_RAW_DATA_CUSTODY_AND_PARSER_SUPPORT_QUALIFICATION_0_1_0.md
handoffs/PGH1_HURDAT2_RAW_DATA_CUSTODY_AND_PARSER_SUPPORT_QUALIFICATION_HANDOFF_0_1_0.md
```

Temporary workflow/scripts and raw bytes are transport/custody infrastructure and must not enter the clean scientific candidate tree.

## Commit topology

```text
COMMIT_1 = THIS_PREREGISTRATION_ONLY
COMMIT_2 = CUSTODY_RESULT_AND_HANDOFF_ONLY
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
RAW_DATA_MAY_BE_ACCESSED_OPAQUELY = YES
AGGREGATE_PARSER_SUPPORT_COUNTS_MAY_BE_RECORDED = YES
EMPIRICAL_HYPOTHESES_TESTED = NO
SURVIVAL_OR_REFUTATION = NONE
STRONG_PGH_CONFIRMED = NO
R2B = UNSATISFIED
FCP_EFFECT = NONE
```
