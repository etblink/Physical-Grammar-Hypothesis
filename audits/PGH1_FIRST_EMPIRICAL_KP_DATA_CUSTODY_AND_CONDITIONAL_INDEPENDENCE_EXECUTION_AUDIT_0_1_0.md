# PGH-1 First Empirical Kp Execution — Independent Project Lead Recovery Audit 0.1.0

## Identity

```text
AUDITED_OPERATION = PGH1_FIRST_EMPIRICAL_KP_DATA_CUSTODY_AND_CONDITIONAL_INDEPENDENCE_EXECUTION
REGISTRY_ID = PGH-OP-0065
CANONICAL_PREREGISTRATION = e3a0291b2d546c1d426151ce6b8cb33f291e8937
TARGET = PGH-OBJ-0037
GRAMMAR = PGH-GRAM-0008
PRIMARY_VERDICT = REFUTED_AT_KP_TARGET
AUDIT_DISPOSITION = PASS_WITH_REPRODUCIBILITY_LIMITATION_RECORDED
```

## Recovery finding

The predecessor session executed the first real Kp analysis and reported a refutation before its execution window ended, but it did not commit its local execution record. Live `main` and the execution branch remained at the canonical preregistration commit. The exact predecessor source bytes and null arrays are not recoverable from repository history.

The audit therefore distinguishes two evidence layers:

```text
E1 = PREDECESSOR_FIRST_EXECUTION_RECOVERY_TRACE
E2 = SUCCESSOR_INDEPENDENT_DETERMINISTIC_RECONSTRUCTION
```

E2 is not represented as the historical first run.

## Custody and semantic parser review

```text
GITHUB_ARTIFACT_DIGEST_MATCH = PASS
ALL_94_YEARLY_SHA256_MATCH = PASS
RAW_CONCAT_REBUILD_MATCH = PASS
RAW_CONCAT_SHA256 = 9700557ec8af6d27bbe9667c45f57a993bc7b5115022ac121bbc635885b9e8d2
PREDECESSOR_NORMALIZED_SHA256_REPORTED = de46bc3ef778d89a1f31147fb62e424ffd7ab34e4e90e6ace5c07676e188a55a
SUCCESSOR_NORMALIZED_SHA256 = cfcdc54545c8f2ec1a50adf6a414e4c8aeb43ebac1bf388ebd852ab34659258e
EXPECTED_SCHEDULED_RECORDS = 274672
SUCCESSOR_OBSERVED_SCHEDULED_RECORDS = 274672
EXPECTED_MAX_TRIPLES = 91557
PREDECESSOR_RETAINED_TRIPLES_REPORTED = 91557
SUCCESSOR_RETAINED_TRIPLES = 91557
MISSING_OR_NONDEFINITIVE_BLOCKS = 0
NATIVE_ALPHABET_SIZE = 28
SUPPORT_GATE = PASS
```

The differing normalized hashes are not evidence of differing Kp values. The predecessor serialization bytes were not recovered; the successor parser deterministically emits a documented TSV. Shared semantic invariants and the observed contingency statistic agree.

## Independent observed-statistic reproduction

```text
PREDECESSOR_G2_REPORTED = 8716.1945
SUCCESSOR_G2 = 8716.1945352372713387
SUCCESSOR_INDEPENDENT_G2 = 8716.194535237304
PREDECESSOR_I_BITS_REPORTED = 0.0686720
SUCCESSOR_I_BITS = 0.068672032894318807
SUCCESSOR_INDEPENDENT_I_BITS = 0.06867203289431907
B_STRATUM_COUNTS_RECONSTRUCTED = YES
OCCUPIED_CELL_DIAGNOSTICS_RECONSTRUCTED = YES
HALF_DIAGNOSTICS_AGREE_WITH_PREDECESSOR_ROUNDING = YES
```

## Monte Carlo and verdict review

```text
PREDECESSOR_P1 = 0_OF_4999__P=0.0002
SUCCESSOR_P1 = 0_OF_4999__P=0.0002
PREDECESSOR_P2 = 0_OF_1999__P=0.0005
SUCCESSOR_P2 = 0_OF_1999__P=0.0005
MECHANICAL_VERDICT = REFUTED_AT_KP_TARGET
```

The predecessor and successor 99th-percentile null locations differ modestly. This is traced to an under-specification in the preregistration: the seed derivation is frozen but the PRNG and exact sampling mappings are not. The null definitions themselves are unchanged.

```text
RNG_UNDERSPECIFICATION = CONFIRMED
RESULT_DIRECTED_NULL_SELECTION = NO
VERDICT_SENSITIVITY_TO_THE_TWO_OBSERVED_REALIZATIONS = NONE
```

## Successor deterministic replay control

```text
SUCCESSOR_ANALYSIS_SOURCE_SHA256 = 97afaad9e0c06eae43447a33ae2373dce4e76ff317944682a03d6d0982136c3f
SUCCESSOR_RESULT_SHA256 = cf521ca52c9a603184e455a83bd600929b9c42ac41b2b6fb3b9149571ef503a2
SAME_BINARY_REPLAY_RESULT = BYTE_IDENTICAL
SAME_BINARY_REPLAY_P1 = BYTE_IDENTICAL
SAME_BINARY_REPLAY_P2 = BYTE_IDENTICAL
GCC_VERSION = 14.2.0
CLANG_VERSION = 17.0.0
CLANG_O3_RESULT = BYTE_IDENTICAL
CLANG_O3_P1 = BYTE_IDENTICAL
CLANG_O3_P2 = BYTE_IDENTICAL
```

An intentionally unoptimized replay exceeded a local execution window and produced no accepted partial result. Optimized same-binary and cross-compiler replays are exact.

## Adversarial interpretation review

P2 remains the stronger frozen countercontrol because it preserves fitted first-order cyclic Markov persistence and places the null distribution much closer to the observed statistic than P1. Both the predecessor execution and successor reconstruction nevertheless produce zero P2 exceedances in 1,999 replicates.

No explanation of the residual Kp dependence is imported into the primary result. No lag, state binning, subperiod, graph repair, or alternative target is substituted.

## Audit conclusion

```text
CUSTODY = PASS
SEMANTIC_DATA_IDENTITY = PASS
SUPPORT = PASS
PREREGISTRATION_CONFORMANCE_OF_NULL_DEFINITIONS = PASS
RNG_BITWISE_REPRODUCIBILITY_SPECIFICATION = INCOMPLETE_PREREGISTRATION_LIMITATION
PREDECESSOR_PRIMARY_RESULT_RECOVERY = SUFFICIENT_WITH_SUCCESSOR_CORROBORATION
SUCCESSOR_STATISTIC_RECOMPUTATION = PASS
SUCCESSOR_DETERMINISTIC_REPLAY = PASS
CROSS_COMPILER_REPLAY = PASS
VERDICT_RECOMPUTATION = PASS
PATH_BOUNDARY = PASS_PENDING_FINAL_TREE_CHECK__12_NEW_FILES_EXPECTED
SCIENTIFIC_DISPOSITION = ACCEPT_REFUTED_AT_KP_TARGET_WITH_REPRODUCIBILITY_LIMITATION_RECORDED
```
