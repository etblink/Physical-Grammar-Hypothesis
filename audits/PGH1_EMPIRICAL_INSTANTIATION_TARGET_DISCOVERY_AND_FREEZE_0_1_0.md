# PGH-1 Empirical Instantiation Target Discovery and Freeze — Audit 0.1.0

## Identity
```text
OPERATION_ID = PGH1_EMPIRICAL_INSTANTIATION_TARGET_DISCOVERY_AND_FREEZE
REGISTRY_ID = PGH-OP-0063
PREREGISTRATION_COMMIT = de07706f324d5171cb96cc860310a20594c9e90e
CANONICAL_BASE = 7d27b6278db284cc4225ec87859c067cefb5d414
TARGET_SELECTION_PROTOCOL = PGH-OBJ-0036
TESTABLE_GRAMMAR = PGH-GRAM-0008
SEMANTIC_BRIDGE = PGH-OBJ-0035
EMPIRICAL_EVENT_VALUE_INSPECTION = NONE
DEPENDENCE_ANALYSIS = NONE
FCP_EFFECT = NONE
```

## Discovery boundary
Seven metadata-level candidates were recorded across D1/D2/D3 using only measurement architecture, public-access metadata, native alphabet, chronology/detector order, sample-volume metadata, preprocessing burden, missingness/selection documentation, and archival stability. No candidate was ranked using the predicted relation, correlations, conditional-independence statistics, Markov fit, or target-effect results.

```text
TGT-001 = GFZ definitive planetary Kp, 3-hour cadence
TGT-002 = GFZ definitive C9 daily geomagnetic index
TGT-003 = GFZ Hp30 half-hour geomagnetic index
TGT-004 = NOAA/NCEI local K-index multi-station archive
TGT-005 = NOAA/NCEI GOES X-ray flare-class event sequence
TGT-006 = NOAA/NCEI Global Hourly present-weather records
TGT-007 = CERN CMS tracker-hit open dataset
```

## Eligibility and contamination

### TGT-001 — GFZ definitive Kp
Passes all eligibility criteria. It is the official IAGA-endorsed planetary three-hour index, has a native 28-state alphabet, official definitive archive from 1932 onward, DOI `10.5880/Kp.0001`, and direct GFZ HTTPS/API access.

Contamination review was performed only after architecture discovery:
```text
INITIAL_CONTAMINATION = C2_HINTS_AT_TARGET_DEPENDENCE
REVIEW_FINDING = RELATED_MARKOV_TRANSITION_WORK_EXISTS_FOR_OTHER_GEOMAGNETIC_INTENSITY_CONSTRUCTIONS_INCLUDING_DAILY_MAXIMUM_KP_G_STATES
EXACT_FROZEN_TARGET_RESULT_DISCLOSED = NO
FINAL_CONTAMINATION = C1_GENERAL_DOMAIN_KNOWLEDGE
```
The exact frozen object is definitive three-hour Kp, fixed 1932–2025 range, non-overlapping scheduled triples. No disclosed result for that exact test was used or located.

### TGT-002 — GFZ C9
Passes all eligibility criteria. Native daily integer `0..9`; official GFZ archive; objective chronological order.
```text
FINAL_CONTAMINATION = C1_GENERAL_DOMAIN_KNOWLEDGE
```

### TGT-003 — GFZ Hp30
Rejected before scoring. Hpo is explicitly open-ended, while no target-specific finite discretization was precommitted.
```text
REJECTION = NATIVE_ALPHABET_OPEN_ENDED_AND_NO_PRECOMMITTED_DISCRETIZATION
```

### TGT-004 — NOAA/NCEI local K archive
Rejected before scoring because a single first target requires an additional unfrozen observatory-selection rule.
```text
REJECTION = SINGLE_TARGET_IDENTITY_REQUIRES_UNFROZEN_STATION_SELECTION
```

### TGT-005 — NOAA/NCEI GOES X-ray flare class
Eligible after review. UTC chronology and native flare-letter classes are objective; multi-generation instrument/product continuity is a documented caveat.
```text
INITIAL_CONTAMINATION = C2_HINTS_AT_TARGET_DEPENDENCE
EXACT_FROZEN_TARGET_RESULT_DISCLOSED = NO
FINAL_CONTAMINATION = C1_GENERAL_DOMAIN_KNOWLEDGE
```

### TGT-006 — NOAA/NCEI Global Hourly present weather
Rejected before scoring because station selection, report-type filtering, irregular/multiple reports, and missingness require material unfrozen choices.

### TGT-007 — CERN CMS tracker hits
Rejected before scoring because variable-length hit/track structures require substantial unfrozen reconstruction to produce exactly three categorical records per event.

## Frozen scores
| Candidate | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| TGT-001 GFZ Kp | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | **19** |
| TGT-002 GFZ C9 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | **19** |
| TGT-005 GOES flare class | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | **18** |

Kp/C9 receive R8=1 because they are standard derived physical indices. GOES receives R4=1 at metadata scope because the discovery operation did not enumerate the complete official event count across product eras, and R6=1 because instrument/product-era continuity requires documented handling.

## Tie break and selection
Kp and C9 tie at 19. `NATIVE_FINITE` ties. Kp has eight scheduled records per UT day while C9 has one, so `LARGER_EVENT_COUNT` selects Kp without inspecting values.

```text
OUTCOME = A__ONE_ELIGIBLE_C0_OR_C1_TARGET_IS_SELECTED_BY_THE_FROZEN_RUBRIC
SELECTED_TARGET_ID = TGT-001
SELECTED_TARGET = GFZ_DEFINITIVE_PLANETARY_KP_3_HOUR_INDEX
PGH_OBJECT = PGH-OBJ-0037
```

## Claim ceiling
```text
TARGET_SELECTED = YES
FINAL_CONTAMINATION = C1_GENERAL_DOMAIN_KNOWLEDGE
RAW_EVENT_VALUES_INSPECTED = NO
RAW_DATA_HASH = DEFERRED
STATISTICAL_TEST_PREREGISTERED = NO
CONDITIONAL_INDEPENDENCE_TESTED = NO
EMPIRICAL_RESULT = NONE
PHYSICAL_GRAMMAR_CONFIRMED = NO
R2B_SATISFIED = NO
FCP_EFFECT = NONE
```
