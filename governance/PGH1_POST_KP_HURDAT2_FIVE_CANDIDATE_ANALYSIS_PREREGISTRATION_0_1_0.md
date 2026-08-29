# PGH-1 HURDAT2 Five-Candidate Analysis Protocol 0.1.0

```text
OBJECT_ID = PGH-OBJ-0049
DECLARING_OPERATION = PGH-OP-0088
STATUS = QUALIFIED_PRE_DATA_TARGET_SPECIFIC_ANALYSIS_PROTOCOL
TARGET = PGH-OBJ-0048__TGT-008__ATLANTIC_HURDAT2_SYSTEM_STATUS
FAMILY_PROTOCOL = PGH-OBJ-0047
PREREGISTRATION_COMMIT = 2580fe334a7239f1833167708d8914b43cb07857
REAL_DATA_ACCESSED = NO
FCP_EFFECT = NONE
```

## Binding scientific method

This artifact operationalizes, without changing, the method frozen in the OP-0088 preregistration.

Primary hypotheses:

```text
H1 = A independent C
H2 = A independent B given C
H3 = A independent B
H4 = B independent C given A
H5 = B independent C
```

Primary statistics are likelihood-ratio `G2` mutual-information / conditional-mutual-information statistics. `I_BITS` is descriptive only.

## Target parsing

```text
DATASET = Atlantic NHC HURDAT2
RANGE = 1988-2025 complete years
STANDARD_TIMES = 0000,0600,1200,1800 UTC
ALPHABET_ORDER = TD,TS,HU,EX,SD,SS,LO,WV,DB
STORM_BOUNDARIES_BREAK_RUNS = YES
NON_SIX_HOUR_GAPS_BREAK_RUNS = YES
UNKNOWN_OR_BLANK_STATUS_ON_ELIGIBLE_RECORD_BREAKS_RUN = YES
ROLE_PERMUTATION = FORBIDDEN
BLOCKING = nonoverlapping three-record blocks from start of each maximal valid six-hour run
TRAILING_RECORDS = DISCARD
```

Malformed headers, dates, times, record counts, duplicate/non-increasing standard timestamps, or structural violations are technical failures. Declared HURDAT2 storm record counts are verified exactly.

Data support requires at least 1000 retained triples and at least two observed states in each of A/B/C. Failure is `INCONCLUSIVE_DATA_SUPPORT` for the entire family.

## CAL1

```text
ARCHITECTURE = pooled fixed-margin conditional randomization
REPLICATES = 4999
P = (1 + EXCEED) / 5000
```

- H1: global permutation of C, A fixed.
- H2: permutation of B independently within observed C strata; A and C fixed.
- H3: global permutation of B, A fixed.
- H4: permutation of C independently within observed A strata; A and B fixed.
- H5: global permutation of C, B fixed.

CAL1 is exact for the stated pooled fixed-margin randomization scheme. It does not assert exchangeability under arbitrary storm-level serial dependence.

## CAL2

```text
ARCHITECTURE = candidate-null storm/run-preserving block-process bootstrap
REPLICATES = 1999
P = (1 + EXCEED) / 2000
SMOOTHING = integer Jeffreys weights w[a,b,c]=2*n[a,b,c]+1
```

For each H1-H5, the reference implementation constructs the exact null triple distribution `q_h` specified in the preregistration. It preserves the corresponding independence relation exactly while retaining the complementary smoothed nuisance conditional.

Observed within-block-run transitions define proposal kernel

```text
R_h(y|x) = (t[x,y] + q_h(y)) / (T[x] + 1)
```

and exact-rational Metropolis-Hastings correction targets `q_h`. Simulated block-run lengths match the observed block-run length vector; no simulated transition crosses a run or storm boundary.

CAL2 is explicitly model-dependent and is not claimed to cover every possible cyclone process.

## Monte Carlo and multiplicity

```text
FAMILY_ALPHA = 0.01
MULTIPLICITY = HOLM_STEP_DOWN
CAL1_AND_CAL2_CORRECTED_SEPARATELY = YES
P_VALUE_TIES = H_ID_ASCENDING
```

Holm uses integer-exact decision arithmetic from exceedance counts. A candidate is refuted only when both CAL1 and CAL2 Holm-reject it. Neither rejection yields survival; disagreement is inconclusive. Survival is not confirmation.

## Floating statistic semantics

```text
G2_TYPE = C++ long double
LOG = natural logarithm
NEGATIVE_ROUNDOFF_CLAMP = (-1e-9,0) -> 0
G2_LE_-1e-9 = TECHNICAL_FAILURE
EXCEED_TOLERANCE = replicate_G2 + 1e-12*max(1,abs(observed_G2)) >= observed_G2
QUANTILE = NOT_APPLICABLE
```

## Stochastic semantics

```text
PRNG = xoshiro256**
WORD = uint64_t
ARITHMETIC = modulo 2^64
BOUNDED_INTEGER = rejection-modulo threshold=(-n) mod n
PERMUTATION = descending Fisher-Yates
CATEGORICAL_SAMPLING = cumulative exact integer weights
UNIFORM_FLOAT = NOT_APPLICABLE
MH_ACCEPTANCE = exact arbitrary-precision integer comparison
STREAM_ISOLATION = calibration/hypothesis/replicate
STD_RANDOM_DISTRIBUTIONS = FORBIDDEN
```

Master seed construction and stream derivation are exactly those frozen in the OP-0088 preregistration. The executable accepts the resulting 64-lowercase-hex master digest.

## Reference executable

```text
SOURCE = tools/pgh_hurdat2_five_candidate.cpp
LANGUAGE = C++20
CANONICAL_EXECUTION_PLATFORM = little-endian 64-bit Linux
COMMAND_SELF_TEST = ./pgh_hurdat2_five_candidate --self-test
COMMAND_PARSE = ./pgh_hurdat2_five_candidate --parse-only <raw-file>
COMMAND_ANALYZE = ./pgh_hurdat2_five_candidate --analyze <raw-file> <master-seed-hex>
```

Canonical execution must record compiler, compiler version, OS/kernel/architecture, `sizeof(long double)`, and runtime/library context sufficient to reproduce the floating `G2` layer. Integer stochastic and Holm semantics are defined independently of standard-library random distributions.

## Failure and claim ceiling

Parser, custody, support, numerical, or reproducibility failure is inconclusive and cannot become evidence for any candidate. No candidate may be replaced, role-reassigned, scope-narrowed, or repaired after exposure under the same identity.

```text
REAL_DATA_ACCESSED = NO
EMPIRICAL_RESULT = NONE
CANDIDATE_VALIDATED = NO
STRONG_PGH_CONFIRMED = NO
R2B = UNSATISFIED
```
