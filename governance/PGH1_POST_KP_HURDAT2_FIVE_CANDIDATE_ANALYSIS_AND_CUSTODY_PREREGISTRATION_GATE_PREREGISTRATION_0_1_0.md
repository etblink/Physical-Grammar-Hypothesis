# PGH-1 Post-Kp HURDAT2 Five-Candidate Analysis and Custody Preregistration Gate — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_POST_KP_HURDAT2_FIVE_CANDIDATE_ANALYSIS_AND_CUSTODY_PREREGISTRATION_GATE
REGISTRY_ID = PGH-OP-0088
CANONICAL_BASE = b795dec4fb286e320f3904f9c21d90ec92f4cc8a
TARGET = PGH-OBJ-0048__TGT-008__ATLANTIC_HURDAT2_SYSTEM_STATUS
FAMILY_PROTOCOL = PGH-OBJ-0047
SUCCESSOR_ADMISSION_STANDARD = PGH-OBJ-0040
TARGET_VALUES_ACCESS = FORBIDDEN
RAW_DATA_DOWNLOAD = FORBIDDEN
DATA_CUSTODY = NOT_PERFORMED
DEPENDENCE_ANALYSIS = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Freeze a complete, executable, target-specific analysis protocol for the five admitted successor packages before any Atlantic HURDAT2 event value is accessed.

This gate must resolve the implementation ambiguity that remained in the first Kp experiment. It therefore freezes not only the statistics and calibrations but also parser semantics, random-number semantics, Monte Carlo conventions, Holm tie/decision rules, output order, custody sequencing, and a synthetic-data reference implementation.

It may not retrieve, materialize, inspect, parse, summarize, or hash the real HURDAT2 raw file.

## Frozen target and family

The target identity/range/roles are immutable from `PGH-OBJ-0048`:

```text
TARGET = Atlantic NHC HURDAT2 native system status
RANGE = complete years 1988-2025
ALPHABET = TD,TS,HU,EX,SD,SS,LO,WV,DB
ELIGIBLE_TIMES = 0000,0600,1200,1800 UTC
SEGMENT = individual storm
GAP_RULE = exact six-hour continuity; gap breaks run
BLOCKING = nonoverlapping triples from each maximal continuous run
A = first record
B = second record
C = third record
```

The five primary hypotheses remain:

```text
H1 = A_INDEPENDENT_C
H2 = A_INDEPENDENT_B_GIVEN_C
H3 = A_INDEPENDENT_B
H4 = B_INDEPENDENT_C_GIVEN_A
H5 = B_INDEPENDENT_C
```

No target, role, range, alphabet, candidate, or blocking change is allowed in this gate.

## Primary statistics

For H1, H3, H5 use the likelihood-ratio mutual-information statistic

```text
G2(X,Y) = 2 * sum_{x,y:n_xy>0} n_xy * ln(n_xy*N/(n_x*n_y))
I_BITS = G2/(2*N*ln(2))
```

For H2 and H4 use

```text
G2(X,Y|Z) = 2 * sum_{x,y,z:n_xyz>0} n_xyz * ln(n_xyz*n_z/(n_xz*n_yz))
I_BITS = G2/(2*N*ln(2))
```

`G2` is the sole primary statistic. `I_BITS` is descriptive only and cannot change a verdict.

## CAL1 — pooled fixed-margin conditional randomization

CAL1 is a nonparametric/fixed-margin permutation calibration on the retained triple table.

```text
REPLICATES = 4999
P_VALUE = (1 + number_of_replicates_with_G2_ge_observed) / 5000
```

Candidate-specific randomization:

```text
H1: keep A fixed; Fisher-Yates shuffle C globally across all retained triples
H2: keep A,C fixed; Fisher-Yates shuffle B independently within each observed C-state stratum
H3: keep A fixed; Fisher-Yates shuffle B globally
H4: keep A,B fixed; Fisher-Yates shuffle C independently within each observed A-state stratum
H5: keep B fixed; Fisher-Yates shuffle C globally
```

Each H1-H5 replicate uses its own deterministic random stream. No year/storm/run stratification is added because that would test a different conditional null than the frozen pooled-distribution hypothesis.

CAL1 preserves the null-relevant pooled margins exactly but does not claim exact validity under arbitrary cross-triple serial/storm clustering. That limitation is frozen and is one reason the family protocol requires a materially different CAL2 and requires both calibrations to reject before candidate refutation.

## CAL2 — null-stationary storm/run-preserving block-process bootstrap

CAL2 is a candidate-constrained parametric/process bootstrap on the sequence of retained three-record blocks.

```text
REPLICATES = 1999
P_VALUE = (1 + number_of_replicates_with_G2_ge_observed) / 2000
```

### Smoothed triple table

Let `n[a,b,c]` be observed retained-triple counts for the nine-state alphabet and define integer Jeffreys weights

```text
w[a,b,c] = 2*n[a,b,c] + 1
W = sum_{a,b,c} w[a,b,c] = 2*N + 729
```

Define exact integer marginals `WA,WB,WC,WAB,WAC,WBC` by summing `w`.

For each hypothesis define a strictly positive null triple distribution `q_h`:

```text
H1 A independent C:
  q = (WA[a]/W) * (WC[c]/W) * (w[a,b,c]/WAC[a,c])

H2 A independent B given C:
  q = (WC[c]/W) * (WAC[a,c]/WC[c]) * (WBC[b,c]/WC[c])
    = WAC[a,c]*WBC[b,c] / (W*WC[c])

H3 A independent B:
  q = (WA[a]/W) * (WB[b]/W) * (w[a,b,c]/WAB[a,b])

H4 B independent C given A:
  q = (WA[a]/W) * (WAB[a,b]/WA[a]) * (WAC[a,c]/WA[a])
    = WAB[a,b]*WAC[a,c] / (W*WA[a])

H5 B independent C:
  q = (WB[b]/W) * (WC[c]/W) * (w[a,b,c]/WBC[b,c])
```

Thus every `q_h` satisfies the corresponding frozen null exactly while preserving the complementary smoothed nuisance conditional distribution where applicable.

### Observed block-transition proposal

For each maximal continuous HURDAT2 record run, partitioning creates a block-run of length `L=floor(record_run_length/3)`. Let `x_t=(A_t,B_t,C_t)` denote its 729-state block sequence.

Count only adjacent block transitions inside the same block-run:

```text
t[x,y] = number of observed x -> y transitions
T[x] = sum_y t[x,y]
```

For candidate h, define proposal kernel

```text
R_h(y|x) = ( t[x,y] + q_h(y) ) / ( T[x] + 1 )
```

Operationally this is sampled exactly by drawing one integer uniformly from `0..T[x]`:

- if the draw is `< T[x]`, use that draw as a cumulative index into the empirical outgoing transitions from x;
- if the draw equals `T[x]`, draw y exactly from `q_h`.

If `T[x]=0`, proposal is exactly `q_h`.

### Metropolis-Hastings correction

Use `R_h` as a proposal and apply an exact-rational Metropolis-Hastings correction with target `q_h`.

For each block-run:

1. draw the first block exactly from `q_h`;
2. for each later block, propose from `R_h(.|current)`;
3. accept with probability

```text
min(1, q_h(y) R_h(x|y) / (q_h(x) R_h(y|x)))
```

represented and decided with arbitrary-precision integer arithmetic; no floating uniform is permitted.

Because each simulated run starts from `q_h` and the MH kernel has invariant distribution `q_h`, every simulated block position has candidate-null marginal `q_h`; the proposal carries empirical within-run block-transition structure as nuisance information. The exact vector of observed block-run lengths is preserved, and no transition crosses a run/storm boundary.

CAL2 is explicitly model-dependent. It is not claimed to reproduce every possible cyclone process; it is a second, materially distinct process calibration whose assumptions are exposed rather than hidden.

## Family multiplicity and verdicts

`PGH-OBJ-0047` remains binding:

```text
FAMILY_ALPHA = 0.01
PROCEDURE = HOLM_STEP_DOWN
APPLY_SEPARATELY = CAL1_AND_CAL2
```

Within each calibration order candidates by `(p_value, H_ID)` ascending. At rank k=1..5, with `d=6-k`, reject while

```text
p <= 0.01/d
```

and stop at the first nonrejection.

Monte Carlo p-values are rational. The reference implementation must decide Holm without floating arithmetic using

```text
100 * d * (1 + exceed_count) <= (replicates + 1)
```

for the candidate at that rank.

Candidate verdict:

```text
CAL1_REJECT AND CAL2_REJECT -> REFUTED_ON_COMMON_TARGET
NOT_CAL1_REJECT AND NOT_CAL2_REJECT -> SURVIVES_COMMON_TARGET_TEST
otherwise -> INCONCLUSIVE_CALIBRATION_DISAGREEMENT
```

Family verdict remains exactly as `PGH-OBJ-0047`. Survival is not confirmation.

## Parser and data-support semantics to freeze

The result of this gate must specify and implement at minimum:

1. HURDAT2 header detection and declared record-count verification;
2. Atlantic basin identity and 1988-2025 record-year filtering;
3. standard-time filter `0000/0600/1200/1800`;
4. exact nine-state status map in frozen order;
5. malformed header/date/time/count as technical parser failure;
6. duplicate or non-increasing standard timestamp within a storm as technical parser failure;
7. blank/unrecognized status on an otherwise valid in-range standard record as a run break/exclusion, not imputation;
8. exact Gregorian six-hour continuity; gaps break runs;
9. storm boundaries always break runs;
10. run-from-first-record nonoverlapping three-record blocking and trailing-record discard;
11. parser audit counts and candidate-independent retained triple/block-run sequence;
12. no value-dependent filtering beyond the frozen validity/status rules.

Data-support gate:

```text
N_RETAINED_TRIPLES >= 1000
AT_LEAST_TWO_OBSERVED_STATES_IN_EACH_ROLE_A_B_C
```

Failure produces `INCONCLUSIVE_DATA_SUPPORT` for the entire five-candidate target test. Absent conditioning states are simply absent strata; they are not imputed.

## Floating-statistic convention

Reference `G2` uses C++ `long double` and the natural logarithm. Terms with zero cell count are omitted.

If numerical roundoff yields `-1e-9 < G2 < 0`, clamp to zero. A value `G2 <= -1e-9` is a technical failure.

For Monte Carlo exceedance, count a replicate as at least as extreme when

```text
replicate_G2 + 1e-12 * max(1, abs(observed_G2)) >= observed_G2
```

This convention is conservative for near-ties and is frozen before data access.

No null quantile is needed for a verdict:

```text
QUANTILE_CONVENTION = NOT_APPLICABLE
```

## Exact stochastic semantics

The gate result must freeze and reference-implement the following:

```text
PRNG = xoshiro256** with four uint64 state words
PRNG_OUTPUT = uint64
STATE_WORD_ARITHMETIC = modulo 2^64
ROTATE = exact 64-bit left rotate
BOUNDED_INTEGER = rejection-modulo using threshold = (-n) mod n
PERMUTATION = descending Fisher-Yates
CATEGORICAL_SAMPLER = cumulative integer weights + bounded integer draw
UNIFORM_FLOAT_MAPPING = NOT_APPLICABLE
MH_ACCEPTANCE = exact arbitrary-precision integer comparison
```

Reference xoshiro256** transition must follow the published algorithmic form:

```text
result = rotl(s[1] * 5, 7) * 9
t = s[1] << 17
s[2] ^= s[0]
s[3] ^= s[1]
s[1] ^= s[2]
s[0] ^= s[3]
s[2] ^= t
s[3] = rotl(s[3],45)
```

All arithmetic above is unsigned 64-bit wraparound.

### Master seed

After a later custody operation establishes the lowercase raw-file SHA-256 and after this gate has a canonical result commit, define ASCII seed material exactly as:

```text
PGH1_TGT008_HURDAT2_FIVE_CANDIDATE_0_1_0\n
RAW_SHA256=<64 lowercase hex>\n
ANALYSIS_PROTOCOL_COMMIT=<40 lowercase hex>\n
```

The master seed is the 32-byte SHA-256 digest of those exact UTF-8 bytes.

The reference executable may accept that digest as 64 lowercase hex rather than implementing SHA-256 internally. Custody must record both seed material and resulting digest.

Parse the 32 master-seed bytes into four consecutive big-endian uint64 words `m0..m3`.

For calibration `cal in {1,2}`, hypothesis `h in {1..5}`, and zero-based replicate `r`, derive one xoshiro stream by:

```text
x = m0 ^ rotl(m1,13) ^ rotl(m2,29) ^ rotl(m3,47)
    ^ (0x9E3779B97F4A7C15 * cal)
    ^ (0xD1B54A32D192ED03 * h)
    ^ (0x94D049BB133111EB * (r+1))
```

Use standard SplitMix64 stepping from x to produce four state words. If all four are zero, set `s[3]=1`.

No global mutable random stream is shared across candidates or replicates.

## Arbitrary-precision uniform integer

For MH acceptance with positive arbitrary-precision denominator `D`:

1. if `D=1`, return 0;
2. let `k=bit_length(D-1)`;
3. generate `ceil(k/64)` xoshiro words and place word j at bits `[64j,64j+63]` (little-word order);
4. mask to the low k bits;
5. reject and redraw if the integer is `>=D`.

This yields exact uniform `0..D-1` sampling.

## Reference implementation and qualification

The result commit may contain only the following scientific outputs:

```text
governance/PGH1_POST_KP_HURDAT2_FIVE_CANDIDATE_ANALYSIS_PREREGISTRATION_0_1_0.md
research/formalizations/PGH1_HURDAT2_FIVE_CANDIDATE_ANALYSIS_SCHEMA_0_1_0.md
tools/pgh_hurdat2_five_candidate.cpp
audits/PGH1_POST_KP_HURDAT2_FIVE_CANDIDATE_ANALYSIS_AND_CUSTODY_PREREGISTRATION_GATE_0_1_0.md
handoffs/PGH1_POST_KP_HURDAT2_FIVE_CANDIDATE_ANALYSIS_AND_CUSTODY_PREREGISTRATION_GATE_HANDOFF_0_1_0.md
```

The C++20 reference implementation must provide `--self-test` using only embedded synthetic HURDAT-like records and deterministic mathematical fixtures. Self-test must cover parser segmentation/blocking, the nine-state mapping, a zero-G2 independence fixture, a positive-dependence fixture, the xoshiro known vector beginning with state `[1,2,3,4] -> output 11520`, bounded/permutation sanity, q-hypothesis normalization/factorization checks on synthetic counts, deterministic stream derivation, and exact Holm boundary cases.

A temporary unintegrated validation workflow may compile and run self-test. Its workflow/script history must not enter the final two-commit scientific candidate.

## Runtime assumptions

```text
REFERENCE_LANGUAGE = C++20
REFERENCE_PLATFORM = little-endian 64-bit Linux for canonical execution
INTEGER_DECISIONS = algorithmically exact and platform-independent under C++ unsigned semantics
G2_FLOATING = long double; compiler/libm metadata must be recorded at execution
STD_RANDOM_DISTRIBUTIONS = FORBIDDEN
```

No standard-library random distribution may define stochastic semantics.

## Custody sequencing — frozen but not executed here

The next separate operation, if later authorized, must:

1. retrieve NHC Data Archive metadata page `https://www.nhc.noaa.gov/data/`;
2. resolve the Atlantic `HURDAT2 1851-2025` download link supplied by NHC under Best Track Data;
3. require that resolved URL is under `https://www.nhc.noaa.gov/data/hurdat/` and corresponds to the 1851-2025 Atlantic release;
4. retrieve those raw bytes without exploratory viewing;
5. record exact URL, retrieval timestamp, byte count, SHA-256, and NHC metadata-page identity;
6. derive and record the master seed from the canonical analysis-protocol commit and raw SHA-256;
7. run only parser/custody qualification first;
8. stop on wrong release identity, malformed structure, support failure, or parser failure rather than substituting another HURDAT release or Pacific target.

The current NHC metadata page identifies the official Atlantic HURDAT2 archive as 1851-2025 and updated for the 2025 season. The raw file itself remains unopened here.

## Outcome space

```text
A = COMPLETE_TARGET_SPECIFIC_PROTOCOL_AND_REFERENCE_IMPLEMENTATION_QUALIFY_PRE_DATA
B = TARGET_SPECIFIC_PROTOCOL_CANNOT_BE_MADE_COMPLETE_WITHOUT_UNFROZEN_SCIENTIFIC_CHOICE
C = REFERENCE_IMPLEMENTATION_FAILS_SYNTHETIC_QUALIFICATION_AND_CANNOT_BE_REPAIRED_WITHIN_FROZEN_METHOD
D = INTERNAL_INCONSISTENCY_WITH_TARGET_FREEZE_OR_FAMILY_PROTOCOL
```

The gate may repair implementation bugs discovered solely by synthetic self-test while preserving the frozen statistical method. Any repair that changes the scientific calibration/statistic/verdict method requires explicit documentation and a new preregistered gate version before data access.

## Commit topology

```text
COMMIT_1 = THIS_PREREGISTRATION_ONLY
COMMIT_2 = QUALIFIED_PROTOCOL_SCHEMA_REFERENCE_IMPLEMENTATION_AUDIT_AND_HANDOFF_ONLY
EXACT_COMMITS = 2
```

## Stop boundary

```text
STOP_BEFORE_HURDAT2_RAW_DOWNLOAD
STOP_BEFORE_RAW_BYTES_HASH
STOP_BEFORE_REAL_PARSER_EXECUTION
STOP_BEFORE_REAL_TARGET_COUNTS
STOP_BEFORE_MONTE_CARLO_EXECUTION
STOP_BEFORE_ANY_H1_H5_RESULT
STOP_BEFORE_CANDIDATE_ADJUDICATION
```

## Claim ceiling

```text
TARGET_SPECIFIC_ANALYSIS_MAY_BE_PREREGISTERED = YES
REAL_DATA_ACCESSED = NO
CANDIDATE_TESTED = NO
SUCCESSOR_VALIDATED = NO
STRONG_PGH_CONFIRMED = NO
R2B = UNSATISFIED
FCP_EFFECT = NONE
```
