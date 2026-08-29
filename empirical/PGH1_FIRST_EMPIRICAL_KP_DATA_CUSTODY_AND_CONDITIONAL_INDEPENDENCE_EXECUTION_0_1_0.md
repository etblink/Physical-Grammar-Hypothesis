# PGH-1 First Empirical Kp Data Custody and Conditional-Independence Execution 0.1.0

## Identity

```text
OPERATION_ID = PGH1_FIRST_EMPIRICAL_KP_DATA_CUSTODY_AND_CONDITIONAL_INDEPENDENCE_EXECUTION
REGISTRY_ID = PGH-OP-0065
REGISTRY_ENTRY = DEFERRED_TO_DEDICATED_NAVIGATION_RECONCILIATION
CANONICAL_PREREGISTRATION = e3a0291b2d546c1d426151ce6b8cb33f291e8937
TARGET = PGH-OBJ-0037
TARGET_ID = TGT-001
TARGET_VARIABLE = GFZ_DEFINITIVE_PLANETARY_KP_3_HOUR_INDEX
TESTABLE_GRAMMAR = PGH-GRAM-0008
TESTABLE_RESTRICTION = A_INDEPENDENT_OF_C_GIVEN_B
SEMANTIC_BRIDGE = PGH-OBJ-0035
FAILURE_RESULT = PGH-FAIL-0034
FCP_EFFECT = NONE
```

This artifact freezes the first preregistered empirical confrontation of `PGH-GRAM-0008` while preserving an interrupted-execution provenance discontinuity exactly rather than rewriting it away.

The target, date range, native alphabet, triple phase, statistic, two null definitions, replicate counts, alpha, smoothing rule, seed-derivation formulas, and verdict rule were canonical before raw Kp values were materialized.

## Execution chronology and recovery boundary

The predecessor Project Lead session materialized the frozen data, froze a local analysis implementation before revealing the Kp result, executed the preregistered analysis once, independently reviewed it, and reported a target refutation. The session then exceeded its execution window before committing the promised execution record.

The predecessor recovery trace is preserved as:

`empirical/pgh1_kp_first_test/predecessor_interrupted_execution_recovery.json`

```text
PREDECESSOR_EXECUTION = EXECUTED_LOCALLY__INTERRUPTED_BEFORE_REPOSITORY_FREEZE
PREDECESSOR_REPOSITORY_COMMIT = NONE
PREDECESSOR_NORMALIZED_SHA256_REPORTED = de46bc3ef778d89a1f31147fb62e424ffd7ab34e4e90e6ace5c07676e188a55a
PREDECESSOR_ANALYSIS_SOURCE_SHA256_REPORTED = 138b326fdac4207b277ac215634f80fa7930020dcf5534410dfcb619873c2e58
PREDECESSOR_ANALYSIS_SOURCE_BYTES_RECOVERED = NO
PREDECESSOR_NULL_OUTPUT_HASHES_RECOVERED = NO
PREDECESSOR_P_PERM = 0.0002__0_OF_4999
PREDECESSOR_P_MARKOV = 0.0005__0_OF_1999
PREDECESSOR_VERDICT = REFUTED_AT_KP_TARGET
```

Because the predecessor source bytes and null arrays were not recoverable, the successor did **not** pretend to recreate that exact pseudorandom realization. Instead it performed an independent deterministic reconstruction from the same canonical preregistration and exact official raw bytes. That reconstruction is corroborating recovery evidence after the result was known, not a replacement claim that its implementation was frozen before the project's first result revelation.

## Custody

```text
DATA_AUTHORITY = GFZ Helmholtz Centre for Geosciences / ISGI
DOI = 10.5880/Kp.0001
YEARS = 1932..2025 inclusive
CUSTODY_RUN = 33256555700
CUSTODY_ARTIFACT_ID = 9715990429
CUSTODY_ARTIFACT_NAME = pgh-kp-gfz-definitive-1932-2025
CUSTODY_ARTIFACT_ZIP_SHA256 = 75b9ccb2cfea1ef553d6635c58d7c67b8d41f408de020d21f1535ac83d2991e4
RAW_YEAR_FILES = 94
RAW_CONCAT_BYTES = 2218126
SHA256_RAW = 9700557ec8af6d27bbe9667c45f57a993bc7b5115022ac121bbc635885b9e8d2
YEARLY_HASH_MANIFEST_VERIFIED = YES_ALL_94
ARCHIVED_CONCAT_EQUALS_ASCENDING_YEAR_RECONCATENATION = YES_BYTE_FOR_BYTE
RAW_BYTES_COMMITTED_TO_GIT = NO
```

## Semantic parser/support agreement

Both executions report the same frozen support semantics: 34,334 UT days, 274,672 scheduled records, native 28-state Kp alphabet, 91,557 non-overlapping complete triples, zero discarded blocks, and one trailing record.

The successor reconstruction uses an explicit TSV serialization and preserves its parser source:

```text
SUCCESSOR_PARSER_SHA256 = b94bae539e559131c6a77579a0056bbf60d0070af145fa97f4145edbbf6c6840
SUCCESSOR_NORMALIZED_SHA256 = cfcdc54545c8f2ec1a50adf6a414e4c8aeb43ebac1bf388ebd852ab34659258e
SUCCESSOR_NORMALIZED_BYTES = 7690846
SUCCESSOR_RETAINED_TRIPLE_INDEX_SHA256 = eff29630625f43c07263157928271274e722cb8b3bdc2125350a6e022dcff441
UT_DAYS = 34334
SCHEDULED_KP_RECORDS = 274672
FIRST_TIMESTAMP = 1932-01-01T00:00:00Z
LAST_TIMESTAMP = 2025-12-31T21:00:00Z
DUPLICATE_TIMESTAMPS = 0
GRID_ERRORS = 0
OBSERVED_NATIVE_ALPHABET_SIZE = 28
RETAINED_TRIPLES = 91557
DISCARDED_TRIPLES = 0
TRAILING_UNPAIRED_RECORDS = 1
DATA_SUPPORT_GATE = PASS
```

The predecessor normalized hash differs because its exact serialization bytes were not recovered. No evidence indicates a semantic-data difference: the raw hash, schedule, alphabet, retained triple count, observed `G2`, effect size, and inferential outcome all agree.

## Preregistration reproducibility limitation discovered during recovery

The canonical preregistration mechanically freezes `SEED_PERM` and `SEED_MARKOV`, but it does not name a PRNG or an exact permutation/categorical sampling mapping. Therefore the seed formula alone does not uniquely determine the Monte Carlo arrays across implementations.

```text
PREREGISTERED_NULL_DEFINITIONS = FIXED
PREREGISTERED_SEED_FORMULAS = FIXED
PRNG_ALGORITHM = NOT_FROZEN_IN_PREREGISTRATION
EXACT_MONTE_CARLO_REALIZATION = UNDERDETERMINED_BY_PREREGISTRATION
```

This is a reproducibility defect, not a license to choose a favorable null after seeing the result. It is preserved as a method limitation. The primary target verdict is accepted only because the predecessor execution and an independently implemented successor reconstruction both return the same minimum attainable Monte Carlo p-values and the same mechanical verdict.

## Successor deterministic reconstruction

The successor reconstruction fixed the following operational realization for replayability:

```text
SUCCESSOR_ANALYSIS_SOURCE_SHA256 = 97afaad9e0c06eae43447a33ae2373dce4e76ff317944682a03d6d0982136c3f
SEED_PERM = 9631348867133756348
SEED_MARKOV = 2988388260916591174
PRNG = std::mt19937_64
BOUNDED_INTEGER_MAPPING = rejection_modulo
UNIT_UNIFORM_MAPPING = high_53_bits_over_2^53
CATEGORICAL_SAMPLER = Vose_alias
P1_SHUFFLE = Fisher_Yates_with_frozen_bounded_mapping
P99_REPORTING = nearest_rank
HALF_SPLIT = floor_N_over_2_in_first_half_remainder_in_second
```

These details define the successor corroboration only; they are not retroactively claimed to have been part of the preregistration.

## Observed statistic — independently reproduced

```text
N = 91557
OCCUPIED_AxBxC_CELLS = 4966
G2_OBS = 8716.1945352372713387
I_BITS_A_C_GIVEN_B = 0.068672032894318807
H_C_GIVEN_B_BITS = 3.302168752811488250
M = 0.020796039825599761
OCCUPIED_CELL_MAX_COUNT = 677
OCCUPIED_CELL_MEDIAN_COUNT = 3
B_STRATA_LT_2 = 0
B_STRATA_LT_5 = 0
B_STRATA_LT_10 = 0
B_STRATA_LT_50 = 2
```

Native-order B-stratum counts:

```text
0o=3363, 0+=6770, 1-=7906, 1o=8283, 1+=8159, 2-=7862, 2o=7799, 2+=7389, 3-=6631, 3o=5960, 3+=5179, 4-=4181, 4o=3373, 4+=2381, 5-=1869, 5o=1336, 5+=976, 6-=623, 6o=460, 6+=310, 7-=211, 7o=159, 7+=126, 8-=99, 8o=55, 8+=52, 9-=33, 9o=12
```

## Calibration agreement across the interrupted first execution and successor reconstruction

```text
PREDECESSOR_P1 = 0_OF_4999__P=0.0002
SUCCESSOR_P1 = 0_OF_4999__P=0.0002
PREDECESSOR_P2 = 0_OF_1999__P=0.0005
SUCCESSOR_P2 = 0_OF_1999__P=0.0005
```

The predecessor trace reported the observation approximately 1,398.6 above its P1 99th percentile and 307.5 above its P2 99th percentile. The successor deterministic realization gives:

```text
SUCCESSOR_P1_NULL_MEDIAN_G2 = 7094.6721287846048654
SUCCESSOR_P1_NULL_99TH_G2 = 7324.9076679059890012
SUCCESSOR_OBS_MINUS_P1_99TH = 1391.2868673312823375
SUCCESSOR_P2_NULL_MEDIAN_G2 = 8084.3356114157068077
SUCCESSOR_P2_NULL_99TH_G2 = 8397.5847685969310987
SUCCESSOR_OBS_MINUS_P2_99TH = 318.6097666403402400
```

The different Monte Carlo quantiles are expected from different unfrozen PRNG realizations. Crucially, both realizations return zero exceedances under both frozen null definitions.

## Mechanical primary verdict

```text
P_PERM = 0.0002 <= 0.01
P_MARKOV = 0.0005 <= 0.01
VERDICT = REFUTED_AT_KP_TARGET
```

No alternative target, lag, phase, state grouping, alpha, null definition, smoothing rule, or subperiod was substituted after observing the result.

## Mandatory descriptive diagnostics — successor independent reconstruction

```text
FIRST_HALF_N = 45778
FIRST_HALF_G2 = 7059.9986476589583617
FIRST_HALF_I_BITS = 0.111248034401463233
SECOND_HALF_N = 45779
SECOND_HALF_G2 = 6388.7654031339625362
SECOND_HALF_I_BITS = 0.100668867433805320
```

The predecessor trace independently reported the same half-sample mutual informations to the shown rounded precision (`0.11125`, `0.10067`). These are descriptive only.

## Successor exact output bindings

```text
SUCCESSOR_ANALYSIS_RESULT_JSON_SHA256 = cf521ca52c9a603184e455a83bd600929b9c42ac41b2b6fb3b9149571ef503a2
SUCCESSOR_P1_NULL_TSV_SHA256 = 60a260d9ca754b0503154ed858476fcfc38341487b0a9ddecaa8943d019fce9f
SUCCESSOR_P2_NULL_TSV_SHA256 = a0780098a4c1fe52b359c713a47ce9234af9a13603faba22754b9a0234a6e7eb
```

The successor result JSON and all three implementation/review sources are committed. The large normalized table, retained-triple table, compiled binaries, and complete null TSV realizations are not committed; their exact SHA-256 identities are preserved in this execution record where material, and the committed sources define their reconstruction.

## Claim ceiling

```text
FROZEN_KP_INSTANTIATION_OF_PGH_GRAM_0008 = REFUTED
PGH_GRAM_0008_CONFIRMED = NO
STRONG_PGH_CONFIRMED = NO
PHYSICAL_GRAMMAR_CONFIRMED = NO
EVERY_POSSIBLE_PGH_REFUTED = NO
R2B_SATISFIED = NO
CAUSAL_ONTOLOGY_INFERRED = NO
POST_RESULT_PHYSICAL_EXPLANATION_SEARCH = NOT_PERFORMED
FCP_EFFECT = NONE
```
