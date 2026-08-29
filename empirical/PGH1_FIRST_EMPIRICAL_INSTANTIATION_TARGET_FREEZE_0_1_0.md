# PGH-1 First Empirical Instantiation Target Freeze 0.1.0

## Identity
```text
OBJECT_ID = PGH-OBJ-0037
OPERATION_ID = PGH1_EMPIRICAL_INSTANTIATION_TARGET_DISCOVERY_AND_FREEZE
REGISTRY_ID = PGH-OP-0063
STATUS = FROZEN_CANDIDATE_PENDING_INTEGRATION
SELECTED_TARGET_ID = TGT-001
SELECTED_TARGET = GFZ_DEFINITIVE_PLANETARY_KP_3_HOUR_INDEX
```

## Authoritative source and raw-data identity
```text
DATA_AUTHORITY = GFZ Helmholtz Centre for Geosciences / International Service of Geomagnetic Indices
DATA_PUBLICATION = Geomagnetic Kp index
DATA_DOI = 10.5880/Kp.0001
DATA_PAGE = https://kp.gfz.de/en/data
DOCUMENTATION = https://kp.gfz.de/en/about-kp
FORMAT_DOCUMENTATION = https://www.gfz.de/en/section/geomagnetism/data-products-services/kp-index/format-documentation-of-kpyymmwdc-files
```

The later materialization operation must retrieve **definitive** Kp values only. A documented API-form locator for the frozen range is:

```text
https://kp.gfz.de/app/json/?start=1932-01-01T00:00:00Z&end=2025-12-31T23:59:59Z&index=Kp&status=def
```

If a DOI/WDC representation is used for byte-stable custody instead, it must represent the same definitive variable/range and its exact locator and bytes must be recorded before analysis.

## Physical record
Kp is the official planetary three-hour geomagnetic-activity index derived from standardized local K indices of the contributing observatory network. This freeze targets the record sequence only. It does not interpret time adjacency as fundamental causation and does not claim PGH explains geomagnetism.

## Exact variable and alphabet
```text
VARIABLE = definitive Kp index
CADENCE = one record per 3-hour UT interval
NATIVE_ALPHABET_SIZE = 28
NATIVE_ALPHABET = 0o,0+,1-,1o,1+,2-,2o,2+,...,8-,8o,8+,9-,9o
DISCRETIZATION = NONE
```
A lossless numeric-third parser encoding is permitted; bin merging is forbidden in the primary test.

## Frozen range
```text
START = 1932-01-01T00:00:00Z
END = 2025-12-31T23:59:59Z
RANGE_RULE = COMPLETE_CALENDAR_YEARS_1932_THROUGH_2025_INCLUSIVE
```
The cutoff is value-independent: 2025 is the last complete calendar year before the 2026-08-29 freeze.

```text
UT_DAYS = 34334
SCHEDULED_KP_RECORDS = 274672
MAX_NONOVERLAPPING_TRIPLES = 91557
TRAILING_UNPAIRED_RECORDS = 1
```
These counts precede documented missing/non-definitive exclusions.

## Exact roles and blocks
Index the expected 3-hour UT slots chronologically from the frozen start as `x_0,x_1,...` without compressing gaps.

```text
A_k = x_(3k)
B_k = x_(3k+1)
C_k = x_(3k+2)
```

```text
A = earliest scheduled Kp record in block
B = intermediate scheduled Kp record in block
C = latest scheduled Kp record in block
ROLE_PERMUTATION = FORBIDDEN
```

## Missing/non-definitive rule
For each scheduled block:

```text
IF all three scheduled slots contain definitive Kp values:
    retain block
ELSE:
    discard entire block
```

Do not compress time, join across gaps, or impute.

## Contamination
```text
INITIAL_CONTAMINATION = C2_HINTS_AT_TARGET_DEPENDENCE
REVIEW_RESULT = RELATED_DOMAIN_MARKOV_WORK_BUT_NO_EXACT_FROZEN_TARGET_RESULT_DISCLOSED
FINAL_CONTAMINATION = C1_GENERAL_DOMAIN_KNOWLEDGE
```
This final class is fixed before analysis and is eligible under `PGH-OBJ-0036`.

## Selection score
```text
R1=2 R2=2 R3=2 R4=2 R5=2 R6=2 R7=2 R8=1 R9=2 R10=2
TOTAL = 19
```
C9 also scored 19. The frozen tie-break selected Kp at `LARGER_EVENT_COUNT` after `NATIVE_FINITE` tied.

## Custody boundary
```text
RAW_DATA_HASH = DEFERRED_UNTIL_POST_ANALYSIS_PREREGISTRATION_MATERIALIZATION
RAW_EVENT_VALUES_INSPECTED = NO
DEPENDENCE_STATISTIC_COMPUTED = NO
```

## Claim ceiling
```text
EMPIRICAL_TARGET = FROZEN
EMPIRICAL_ANALYSIS = NOT_STARTED
EMPIRICAL_RESULT = NONE
PGH_GRAM_0008_CONFIRMED = NO
PGH_GRAM_0008_REFUTED = NO
R2B_SATISFIED = NO
PHYSICAL_LAW_DERIVED = NO
FCP_EFFECT = NONE
```
