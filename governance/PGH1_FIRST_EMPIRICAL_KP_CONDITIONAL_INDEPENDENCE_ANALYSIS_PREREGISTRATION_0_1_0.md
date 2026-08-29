# PGH-1 First Empirical Kp Conditional-Independence Analysis — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_FIRST_EMPIRICAL_KP_CONDITIONAL_INDEPENDENCE_ANALYSIS_PREREGISTRATION
REGISTRY_ID = PGH-OP-0064
CANONICAL_BASE = 92d26e8aff044911c557bb26557183e4f4854dd1
TARGET = PGH-OBJ-0037
TARGET_VARIABLE = GFZ_DEFINITIVE_PLANETARY_KP_3_HOUR_INDEX
TESTABLE_GRAMMAR = PGH-GRAM-0008
GRAMMAR_DERIVATION = PGH-DER-0030; PGH-DER-0031
SEMANTIC_BRIDGE = PGH-OBJ-0035
RAW_DATA_MATERIALIZED = NO
RAW_EVENT_VALUES_INSPECTED = NO
NEW_TARGET_SELECTION = FORBIDDEN
NEW_DISCRETIZATION = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Freeze the complete primary statistical analysis before materializing or inspecting the selected Kp event values.

The target prediction is the conditional-independence restriction transferred from `PGH-GRAM-0008`:

\[
H_0:\quad A\perp C\mid B.
\]

For the frozen empirical instantiation:

```text
A = first definitive Kp state in each retained scheduled three-record block
B = second definitive Kp state in the block
C = third definitive Kp state in the block
```

The alternative is unrestricted conditional dependence of `C` on `A` after conditioning on `B`.

No physical-causal interpretation of the Kp sequence is required for this statistical test.

## Frozen data identity

```text
AUTHORITY = GFZ Helmholtz Centre for Geosciences / ISGI
DOI = 10.5880/Kp.0001
VARIABLE = definitive Kp
START = 1932-01-01T00:00:00Z
END = 2025-12-31T23:59:59Z
NATIVE_ALPHABET_SIZE = 28
DISCRETIZATION = NONE
```

The exact target/triple/missingness rules in `PGH-OBJ-0037` are controlling and may not be changed.

## Materialization and custody sequence

Only after this preregistration is canonical:

1. retrieve the frozen definitive Kp range from the documented GFZ API or DOI/WDC representation;
2. preserve the exact downloaded bytes unchanged;
3. compute `SHA256_RAW` before statistical analysis;
4. parse to a normalized table containing expected timestamp, native Kp token, and definitive status only;
5. compute `SHA256_NORMALIZED`;
6. validate uniqueness, chronology, three-hour grid, native alphabet and status;
7. form scheduled non-overlapping triples exactly as frozen;
8. record retained/discarded block counts;
9. run the preregistered analysis without interactive inspection/tuning.

If two official representations of the same frozen range differ semantically, stop `INCONCLUSIVE_DATA_CUSTODY` rather than choosing by statistical result.

## Primary statistic

Let `n_abc` be the retained triple count for states `(a,b,c)` and use the standard zero-count convention `0 log 0 = 0`.

Define

\[
G^2 = 2\sum_{a,b,c:n_{abc}>0}
 n_{abc}\log\left(\frac{n_{abc}n_b}{n_{ab}n_{bc}}\right).
\]

This is equivalent to

\[
G^2=2N I_{\rm nat}(A;C\mid B).
\]

Report the effect size in bits per retained triple:

\[
I_{\rm bits}(A;C\mid B)=\frac{G^2}{2N\ln 2}.
\]

Also report, when `H(C|B)>0`,

\[
M = I(A;C\mid B)/H(C\mid B),
\]

as the fraction of residual conditional entropy associated with the additional `A` information. `M` is descriptive only and does not alter the verdict.

No Kp states may be merged or binned in the primary statistic.

## Calibration P1 — conditional permutation

```text
P1_REPLICATES = 4999
P1_ALPHA = 0.01
```

For each replicate, independently permute the observed `C` labels **within each observed B stratum**, leaving `(A,B)` and the stratum-specific `C` multiset fixed. Recompute `G^2`.

Use the Monte Carlo p-value

```text
p_perm = (1 + number(G2_perm >= G2_obs)) / (1 + P1_REPLICATES)
```

B strata of size 0/1 remain unchanged.

The pseudorandom seed is derived mechanically from the canonical preregistration commit:

```text
SEED_PERM = first_64_bits(SHA256(PREREGISTRATION_COMMIT_SHA || "|KP-PERM|"))
```

This calibration is the direct finite-table conditional-independence randomization control. Its known limitation is exchangeability across retained triples within B; the second calibration is frozen specifically to audit sensitivity to chronological dependence.

## Calibration P2 — phase-aware Markov parametric bootstrap

```text
P2_REPLICATES = 1999
P2_ALPHA = 0.01
SMOOTHING = JEFFREYS_1_2_PSEUDOCOUNT_PER_TRANSITION_CELL
```

Fit a three-phase first-order null process to the frozen chronology using only retained complete blocks and immediately adjacent retained blocks:

```text
PHASE_0 = P(B_k | A_k)
PHASE_1 = P(C_k | B_k)
PHASE_2 = P(A_(k+1) | C_k)  only when block k+1 is the immediately next scheduled complete block
```

Missing/discarded blocks break simulation segments. Estimate each 28x28 phase-transition matrix with `1/2` Jeffreys pseudocount in every cell. Estimate the initial-A distribution at segment starts with the same `1/2` smoothing.

For each bootstrap replicate:

1. reproduce the observed lengths of contiguous retained-block segments;
2. simulate each segment using the fitted cyclic transition sequence `A→B→C→next A`;
3. ignore no simulated values and create the same triple positions;
4. compute the same native-28-state `G^2`.

Use

```text
p_markov = (1 + number(G2_boot >= G2_obs)) / (1 + P2_REPLICATES)
```

with seed

```text
SEED_MARKOV = first_64_bits(SHA256(PREREGISTRATION_COMMIT_SHA || "|KP-MARKOV|"))
```

This calibration is a robustness null for one-step chronological persistence. It is not itself declared to be the physical PGH grammar and cannot replace P1.

## Sparse-state handling

Primary analysis keeps all 28 Kp states.

```text
NO_STATE_MERGING
NO_RARE_CELL_DROPPING
NO_POSTHOC_BINNING
NO_CONTINUITY_CORRECTION_TO_G2
```

Report:

- retained triple count `N`;
- number of occupied `A×B×C` cells;
- all `n_b` stratum counts;
- number of B strata with fewer than 2, 5, 10, and 50 observations;
- maximum and median cell counts among occupied cells.

If fewer than 1,000 complete triples survive the frozen custody/missingness rule, stop `INCONCLUSIVE_DATA_SUPPORT`. This threshold is a data-integrity stop, not an effect-size criterion.

## Primary verdict rule

```text
IF data custody/parser/support stop is triggered:
    VERDICT = INCONCLUSIVE

ELSE IF p_perm <= 0.01 AND p_markov <= 0.01:
    VERDICT = REFUTED_AT_KP_TARGET

ELSE IF p_perm > 0.01 AND p_markov > 0.01:
    VERDICT = SURVIVES_FIRST_KP_TEST

ELSE:
    VERDICT = INCONCLUSIVE_CALIBRATION_DISAGREEMENT
```

Boundary equality is rejection because the rule uses `<= 0.01`.

`SURVIVES_FIRST_KP_TEST` means only that this target did not reject the transferred conditional-independence restriction under either frozen calibration. It is **not** confirmation of strong PGH, `PGH-GRAM-0008`, causal semantics, or law exhaustion.

`REFUTED_AT_KP_TARGET` means the frozen empirical instantiation of `PGH-GRAM-0008` fails at this target. It does not by itself refute every possible PGH grammar.

## Secondary descriptive diagnostics

The following are mandatory reports but may not replace the primary verdict:

```text
1. G2 and I_bits on the full retained target.
2. M = I/H(C|B) when defined.
3. G2/I_bits separately for the first and second chronological halves, split by retained-block index before analysis.
4. Per-B contribution to total G2, sorted only after calculation for reporting.
5. Difference between observed G2 and median/99th percentile of each frozen null calibration.
```

The half-sample diagnostic is descriptive only; no subperiod becomes a replacement primary target.

## Implementation firewall

The execution code must be written to implement this document without changing:

```text
TARGET
DATE_RANGE
TRIPLE_RULE
ALPHABET
G2_FORMULA
P1_REPLICATES
P2_REPLICATES
ALPHA
SMOOTHING
VERDICT_RULE
```

Bug fixes after raw-data materialization are permitted only if they are demonstrably semantics-preserving and must be recorded before re-execution. A bug requiring a scientific/statistical choice triggers a stop and new preregistration; the observed result may not guide the choice.

## Outcome space for execution

```text
A = SURVIVES_FIRST_KP_TEST
B = REFUTED_AT_KP_TARGET
C = INCONCLUSIVE_CALIBRATION_DISAGREEMENT
D = INCONCLUSIVE_DATA_CUSTODY_OR_SUPPORT
```

## Claim ceiling

```text
TARGET = FROZEN
ANALYSIS_METHOD = PREREGISTERED
RAW_DATA = NOT_YET_MATERIALIZED
EMPIRICAL_RESULT = NONE
PGH_CONFIRMED = NO
R2B_SATISFIED = NO
FCP_EFFECT = NONE
```

## Next operation after integration

```text
PGH1_FIRST_EMPIRICAL_KP_DATA_CUSTODY_AND_CONDITIONAL_INDEPENDENCE_EXECUTION
```

That operation may materialize/hash the frozen data, implement the frozen analysis, execute it once, freeze exact outputs, and adjudicate only under the verdict rule above.
