# PGH-FAIL-0034 — Frozen Kp Instantiation of PGH-GRAM-0008

## Status

```text
FAILURE_ID = PGH-FAIL-0034
STATUS = FAILED_PRESERVED
FAILURE_CLASS = EMPIRICAL_TARGET_REFUTATION
TARGET = PGH-OBJ-0037
TARGET_ID = TGT-001
GRAMMAR = PGH-GRAM-0008
SEMANTIC_BRIDGE = PGH-OBJ-0035
PREREGISTRATION = e3a0291b2d546c1d426151ce6b8cb33f291e8937
```

## Failed empirical instantiation

The prospectively frozen transfer of the sparse-chain restriction `A independent of C given B` to non-overlapping successive triples of definitive three-hour GFZ planetary Kp states is rejected under both preregistered calibration definitions.

```text
PREDECESSOR_P_PERM = 0.0002__0_OF_4999
PREDECESSOR_P_MARKOV = 0.0005__0_OF_1999
SUCCESSOR_RECONSTRUCTION_P_PERM = 0.0002__0_OF_4999
SUCCESSOR_RECONSTRUCTION_P_MARKOV = 0.0005__0_OF_1999
ALPHA = 0.01
VERDICT = REFUTED_AT_KP_TARGET
```

The result uses all 91,557 complete frozen triples and the full native 28-state alphabet. No state merging, alternative lag, role permutation, subperiod selection, or post-result null-definition substitution was used.

## Provenance qualification

The first execution occurred in the predecessor session but the session ended before it committed the execution record. Its reported analysis-source hash and normalized serialization hash are preserved in the execution recovery artifact. Exact predecessor source bytes and null arrays were not recoverable.

A successor implementation independently reconstructed the exact raw custody, schedule, contingency statistic, and both frozen Monte Carlo tests and obtained the same zero-exceedance counts and verdict. This second implementation is corroboration after the result was known, not a rewritten claim about the chronology of the first run.

The recovery also identified that the preregistration froze seed derivation but not the PRNG/sampling implementation. That affects bitwise Monte Carlo reproducibility but did not change the verdict across the two observed legitimate realizations.

## What failed

What failed is the **frozen Kp physical instantiation** of `PGH-GRAM-0008` through `PGH-OBJ-0035`/`PGH-OBJ-0037`.

The failure is empirical: the Kp sequence exhibits more residual `A`–`C` dependence given `B` than either preregistered null calibration produced at the preregistered threshold in both the first recovered run and the independent successor reconstruction.

## What did not fail by this result alone

```text
FORMAL_SPARSE_DAG_CONDITIONAL_INDEPENDENCE_DERIVATION = UNAFFECTED
PGH_GRAM_0008_AS_A_FORMAL_GRAMMAR_CANDIDATE = UNAFFECTED_AS_FORMAL_MATHEMATICS
EVERY_OTHER_EMPIRICAL_INSTANTIATION_OF_PGH_GRAM_0008 = NOT_TESTED_HERE
EVERY_POSSIBLE_PGH_GRAMMAR = NOT_REFUTED_HERE
STRONG_PGH = NOT_CONFIRMED
R2B = UNSATISFIED
FCP_EFFECT = NONE
```

## No repair inside the failed test

```text
CHANGE_LAG_OR_BLOCK_PHASE
MERGE_KP_STATES
DROP_RARE_STATES
SELECT_A_SUBPERIOD
SUBSTITUTE_A_DIFFERENT_TARGET
ADD_AN_EDGE_AFTER_SEEING_THE_RESULT
CHANGE_ALPHA_OR_CALIBRATION_DEFINITION
REINTERPRET_GRAPH_ARROWS_AS_CAUSAL_TO_ESCAPE_THE_TEST
```

Any future model refinement or second empirical target requires a separately justified and preregistered operation after this failure is canonical.
