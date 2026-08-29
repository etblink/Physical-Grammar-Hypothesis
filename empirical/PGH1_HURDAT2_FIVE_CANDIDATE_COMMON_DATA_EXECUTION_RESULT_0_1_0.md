# PGH-1 HURDAT2 Five-Candidate Common-Data Execution Result 0.1.0

## Identity

```text
OPERATION_ID = PGH1_HURDAT2_FIVE_CANDIDATE_COMMON_DATA_EXECUTION
REGISTRY_ID = PGH-OP-0094
PREREGISTRATION_COMMIT = 4ce2d48e4adf69b40720e808cef5ceb83b2fde1d
TARGET = PGH-OBJ-0048__TGT-008__ATLANTIC_HURDAT2_SYSTEM_STATUS
FAMILY_PROTOCOL = PGH-OBJ-0047
ANALYSIS_PROTOCOL = PGH-OBJ-0049
ANALYSIS_PROTOCOL_COMMIT = 802d5bf7858b00d4df5a1e6b955b65d16455ae6d
EXECUTION_WORKFLOW_RUN = 33275343932
EXECUTION_JOB = 99160952420
EXECUTION_STATUS = SUCCESS
FCP_EFFECT = NONE
```

## Exact execution custody

```text
RAW_CUSTODY_ARTIFACT_ID = 9721043553
RAW_CUSTODY_ARTIFACT_DIGEST = sha256:10a10afb2037287b820059727d1de8c6227be8c12f437b41b7c8cfc5c322af97
RAW_SHA256 = 1b9b0c7beed5b4505838658b1d30e159fc84330c60891a58cfcf43ae55c37202
MASTER_SEED_HEX = f1a892274ed5782e7973cb19087cdb2ad5f03a21c840a9b6a75775a9b8f8ccd0
ANALYSIS_SOURCE_SHA256 = 1b7fcd8e1958d5614a73cdb2226465bb41f355fbc2d7c3e6769b1f8f488682d4
EXECUTION_EVIDENCE_ARTIFACT_ID = 9721337119
EXECUTION_EVIDENCE_ARTIFACT_DIGEST = sha256:b36bbe5a9619ab33cd3258acadcf3a991bcd0c2907f85bb5aa39246986727d9e
MACHINE_OUTPUT_SHA256 = 459a5958165d87740a09b9feb40c30daad702ca633f081319f4642bc45c00ffc
EXECUTION_ENVIRONMENT_SHA256 = 9f9f094995b9adba5b24a195c683de34bf6b1feabab77cd6f7d5d3b28bea5d88
```

The machine output is frozen verbatim at `empirical/PGH1_HURDAT2_FIVE_CANDIDATE_COMMON_DATA_MACHINE_OUTPUT_0_1_0.txt`.

## Execution environment

```text
EXECUTION_WORKFLOW_HEAD = 9af44fa39eca95144c408b8931691ed9c6de6c3f
COMPILER_VERSION = g++ (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0
OS_RELEASE = Ubuntu 24.04.4 LTS
KERNEL = Linux 6.17.0-1022-azure x86_64
ARCHITECTURE = x86_64
SIZEOF_LONG_DOUBLE = 16
LIBC_VERSION = ldd (Ubuntu GLIBC 2.39-0ubuntu8.8) 2.39
```

The successful workflow verified exact custody identity, raw hash/size, analysis source hash, strict build, self-test, required output key uniqueness, and absence of raw payload from the Git tree before sealing the evidence artifact.

## Data-support audit

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
DATA_SUPPORT = PASS
```

## Frozen five-candidate result

| Candidate | Frozen restriction | Observed G2 | CAL1 exceed / 4999 | CAL2 exceed / 1999 | CAL1 Holm | CAL2 Holm | Verdict |
|---|---|---:|---:|---:|---|---|---|
| H1 / PGH-OBJ-0041 | A independent C | 10668.711833313183863 | 0 | 0 | REJECT | REJECT | REFUTED_ON_COMMON_TARGET |
| H2 / PGH-OBJ-0042 | A independent B given C | 3697.8161452766481416 | 0 | 0 | REJECT | REJECT | REFUTED_ON_COMMON_TARGET |
| H3 / PGH-OBJ-0043 | A independent B | 14185.918691973693955 | 0 | 0 | REJECT | REJECT | REFUTED_ON_COMMON_TARGET |
| H4 / PGH-OBJ-0044 | B independent C given A | 3180.3435741363629685 | 0 | 0 | REJECT | REJECT | REFUTED_ON_COMMON_TARGET |
| H5 / PGH-OBJ-0045 | B independent C | 13668.446120833408783 | 0 | 0 | REJECT | REJECT | REFUTED_ON_COMMON_TARGET |

The frozen Monte Carlo formulas imply raw calibration p-values of `1/5000 = 0.0002` for CAL1 and `1/2000 = 0.0005` for CAL2 for each candidate. The scientific decision is not based on those raw values alone: the executable applied the separately preregistered Holm familywise procedure to each calibration family, and both corrected procedures rejected all five candidates.

## Preregistered family verdict

```text
H1_VERDICT = REFUTED_ON_COMMON_TARGET
H2_VERDICT = REFUTED_ON_COMMON_TARGET
H3_VERDICT = REFUTED_ON_COMMON_TARGET
H4_VERDICT = REFUTED_ON_COMMON_TARGET
H5_VERDICT = REFUTED_ON_COMMON_TARGET

FAMILY_VERDICT = CURRENT_FIVE_CANDIDATE_SUCCESSOR_FAMILY_REFUTED_AT_COMMON_TARGET
```

This is the exact family outcome specified before target discovery and before data access for the case in which all five candidates are refuted.

## Scientific meaning and claim ceiling

The result refutes the five current post-Kp successor candidate packages on TGT-008 under their frozen physical role assignments, scope, semantic bridges, statistics, dual calibrations, and multiplicity rule.

It does **not** establish any of the following:

```text
GLOBAL_REFUTATION_OF_ALL_CONCEIVABLE_PGH = NO
REFUTATION_OF_THE_FORMAL_DAG_THEOREMS = NO
PROOF_THAT_NO_OTHER_PHYSICAL_GRAMMAR_CAN_EXIST = NO
CONFIRMATION_OF_AN_ALTERNATIVE_GRAMMAR = NO
R2B_SATISFIED = NO
FCP_EFFECT = NONE
```

The historical Kp-refuted candidate remains failed; this result independently refutes all five later successor packages on a genuinely prospective target. No failed candidate may be repaired, role-reassigned, scope-narrowed, or replaced inside this operation.

## Stop rule

```text
SECOND_TARGET = NOT_OPENED
NEW_DAG = NOT_INTRODUCED
FAILED_CANDIDATE_REPLACEMENT = NO
SCOPE_NARROWING = NO
ROLE_REASSIGNMENT = NO
GRAPH_REPAIR = NO
POST_RESULT_SCIENTIFIC_ADJUDICATION = REQUIRED_SEPARATELY
```

Truth over PGH.
