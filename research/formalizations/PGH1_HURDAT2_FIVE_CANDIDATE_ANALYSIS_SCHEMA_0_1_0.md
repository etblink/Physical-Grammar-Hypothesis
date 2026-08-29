# PGH-1 HURDAT2 Five-Candidate Analysis Schema 0.1.0

```text
OBJECT_ID = PGH-OBJ-0049
TARGET = PGH-OBJ-0048
FAMILY = PGH-OBJ-0041..0045
STATUS = EXECUTABLE_PRE_DATA_SCHEMA
```

## Deterministic pipeline

```text
RAW_HURDAT2_BYTES
-> STRUCTURAL_PARSE
-> ATLANTIC_HEADER_AND_COUNT_VALIDATION
-> 1988_2025_FILTER
-> STANDARD_6H_TIME_FILTER
-> NATIVE_STATUS_MAP
-> MAXIMAL_VALID_6H_RUNS_PER_STORM
-> NONOVERLAPPING_3_RECORD_BLOCKS
-> ONE_COMMON_TRIPLE_TABLE_AND_BLOCK_RUN_VECTOR
-> SUPPORT_GATE
-> H1_H5_OBSERVED_G2
-> CAL1_4999
-> HOLM_CAL1
-> CAL2_1999
-> HOLM_CAL2
-> CANDIDATE_VERDICTS
-> FAMILY_VERDICT
```

No branch in this pipeline uses a candidate outcome to change parsing, filtering, roles, target range, state alphabet, or candidate membership.

## Native state map

```text
0 TD
1 TS
2 HU
3 EX
4 SD
5 SS
6 LO
7 WV
8 DB
```

Triple-state identifier:

```text
STATE_ID(a,b,c) = (9*a + b)*9 + c
STATE_SPACE = 729
```

## Primary statistics

```text
H1: G2(A,C)
H2: G2(A,B|C)
H3: G2(A,B)
H4: G2(B,C|A)
H5: G2(B,C)
```

Zero-count cells contribute zero. No asymptotic chi-square p-value is a primary decision input.

## CAL1 exact mutation map

```text
H1: mutate C globally
H2: mutate B within C
H3: mutate B globally
H4: mutate C within A
H5: mutate C globally
```

The reference code copies the retained triple vector for each replicate and mutates only the indicated field.

## CAL2 exact null construction

Let `w=2*n+1`, `W=sum w` and derive integer marginals. Candidate-null factors are:

```text
H1 q(a,b,c)=WA[a]*WC[c]*w[a,b,c] / (W^2*WAC[a,c])
H2 q(a,b,c)=WAC[a,c]*WBC[b,c] / (W*WC[c])
H3 q(a,b,c)=WA[a]*WB[b]*w[a,b,c] / (W^2*WAB[a,b])
H4 q(a,b,c)=WAB[a,b]*WAC[a,c] / (W*WA[a])
H5 q(a,b,c)=WB[b]*WC[c]*w[a,b,c] / (W^2*WBC[b,c])
```

Sampling `q_h` is factorized with integer categorical draws, avoiding floating probability tables.

Proposal mixture:

```text
R_h(y|x) = empirical_outgoing_count(x,y)/(T[x]+1)
           + q_h(y)/(T[x]+1)
```

The mixture is sampled by a uniform exact integer on `0..T[x]`; one outcome invokes an exact `q_h` draw, the remaining outcomes index the observed outgoing transition multiset.

MH acceptance uses exact rational cross-products with `boost::multiprecision::cpp_int`. Arbitrary-precision uniform integers use rejection from low-order assembled xoshiro words exactly as preregistered.

## Holm schema

For each calibration, candidates are sorted by `(exceed+1, H_ID)` because denominators are common within a calibration. At rank `k=1..5`, `d=6-k`, reject while

```text
100*d*(exceed+1) <= replicates+1
```

then stop. This is exact for `p <= 0.01/d`.

## Reference self-test coverage

The embedded synthetic self-test covers:

- all nine native status-code mappings;
- Atlantic header parsing, record-count validation, six-hour blocking, unknown-status breaks and continuity breaks;
- xoshiro256** `[1,2,3,4]` first output `11520`;
- deterministic stream derivation;
- bounded integer and Fisher-Yates sanity;
- an exactly independent zero-`G2` fixture;
- a positive-dependence fixture;
- exact normalization of all five synthetic `q_h` distributions;
- exact H2/H4 factor-form checks;
- Holm threshold boundary cases;
- tiny synthetic CAL1 and CAL2 execution smoke tests.

The self-test contains no HURDAT2 event values.
