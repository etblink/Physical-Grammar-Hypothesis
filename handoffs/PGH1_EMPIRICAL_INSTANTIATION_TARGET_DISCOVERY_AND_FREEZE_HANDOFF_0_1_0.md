# PGH-1 Empirical Instantiation Target Discovery and Freeze — Handoff 0.1.0

## Result
```text
OPERATION_ID = PGH1_EMPIRICAL_INSTANTIATION_TARGET_DISCOVERY_AND_FREEZE
REGISTRY_ID = PGH-OP-0063
OUTCOME = A
SELECTED_TARGET_ID = TGT-001
SELECTED_TARGET = GFZ_DEFINITIVE_PLANETARY_KP_3_HOUR_INDEX
TARGET_OBJECT = PGH-OBJ-0037
TARGET_SELECTION_SCORE = 19/20
TIE_BREAK = Kp_OVER_C9_BY_LARGER_EVENT_COUNT
INITIAL_CONTAMINATION = C2_HINTS_AT_TARGET_DEPENDENCE
FINAL_CONTAMINATION = C1_GENERAL_DOMAIN_KNOWLEDGE_AFTER_REVIEW
```

## Meaning
The first PGH empirical instantiation target has been selected without inspecting the predicted dependence result. The target is the official GFZ definitive three-hour planetary Kp sequence on calendar years 1932–2025.

The target is selected by the previously frozen metadata rubric, not because its dependence behavior is known to agree with `PGH-GRAM-0008`.

## Frozen construction
```text
VARIABLE = definitive Kp
ALPHABET = official 28 Kp states
ORDER = chronological scheduled 3-hour UT slots
BLOCKING = non-overlapping consecutive scheduled triples
A = first slot of block
B = second slot of block
C = third slot of block
MISSING_RULE = discard block if any member missing/non-definitive; never compress gaps
DISCRETIZATION = none
SCHEDULED_RECORDS_BEFORE_MISSING_EXCLUSIONS = 274672
MAX_TRIPLES_BEFORE_MISSING_EXCLUSIONS = 91557
```

## Provenance
```text
DATA_AUTHORITY = GFZ Helmholtz Centre for Geosciences / ISGI
DATA_DOI = 10.5880/Kp.0001
DATA_PAGE = https://kp.gfz.de/en/data
RAW_DATA_HASH = DEFERRED
RAW_VALUES_INSPECTED = NO
```

## Not yet done
```text
NO_RAW_EVENT_VALUE_INSPECTION
NO_CORRELATION_OR_DEPENDENCE_COMPUTATION
NO_STATISTICAL_TEST_SELECTED_AFTER_VALUES
NO_EMPIRICAL_CONFIRMATION_OR_REFUTATION
NO_R2B_COMPLETION
NO_FCP_EFFECT
```

## Next operation
```text
PGH1_FIRST_EMPIRICAL_KP_CONDITIONAL_INDEPENDENCE_ANALYSIS_PREREGISTRATION
```

Before materialization it should freeze:

1. exact null/alternative semantics for `A ⟂ C | B`;
2. primary finite-sample conditional-independence statistic;
3. calibration/significance procedure;
4. handling of sparse native Kp cells without merging the 28-state alphabet in the primary test;
5. effect-size reporting independent of significance;
6. robustness checks that cannot replace the primary result;
7. treatment of deterministic time/block structure;
8. raw-data materialization and hashing procedure;
9. PASS/FAIL/INCONCLUSIVE rule for `PGH-GRAM-0008` at this target only.

Only after that preregistration is frozen may the raw definitive Kp values be materialized and the predicted relation evaluated.
