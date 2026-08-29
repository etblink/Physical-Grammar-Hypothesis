# PGH-1 Post-Kp Common Target Freeze 0.1.0

## Identity

```text
OBJECT_ID = PGH-OBJ-0048
TARGET_ID = TGT-008
OPERATION_ID = PGH1_POST_KP_COMMON_TARGET_MULTI_CANDIDATE_TARGET_DISCOVERY_AND_FREEZE
REGISTRY_ID = PGH-OP-0086
STATUS = FROZEN_COMMON_TARGET
FAMILY_PROTOCOL = PGH-OBJ-0047
TARGET = NOAA_NWS_NHC_ATLANTIC_HURDAT2_STANDARD_SYNOPTIC_SYSTEM_STATUS
```

## Authority and metadata identity

```text
AUTHORITY = NOAA / National Weather Service / National Hurricane Center
DATASET = Atlantic Hurricane Database (HURDAT2)
ARCHIVE_DOCUMENTED_SPAN = 1851-2025
ARCHIVE_UPDATE = 2026-02-27__INCLUDES_2025_SEASON
DATA_PAGE = https://www.nhc.noaa.gov/data/
FORMAT_DOCUMENTATION = https://www.nhc.noaa.gov/data/hurdat/hurdat2-format-atl-1851-2021.pdf
FUTURE_RAW_DATA_LOCATOR_CLASS = https://www.nhc.noaa.gov/data/hurdat/ ; resolve the Atlantic HURDAT2 1851-2025 release during separately authorized custody
```

No raw HURDAT2 event file was downloaded or opened during this freeze.

## Physical record

HURDAT2 is NHC's post-analysis best-track record for Atlantic tropical/subtropical cyclones. The selected empirical variable is the native categorical `status of system` at regular standard synoptic best-track times. The project does not interpret six-hour adjacency as fundamental causation and does not claim PGH explains tropical cyclones.

## Native alphabet

The authoritative format documentation supplies the exact nine-state field:

```text
TD = tropical cyclone of tropical-depression intensity
TS = tropical cyclone of tropical-storm intensity
HU = tropical cyclone of hurricane intensity
EX = extratropical cyclone
SD = subtropical cyclone of subtropical-depression intensity
SS = subtropical cyclone of subtropical-storm intensity
LO = low that is neither tropical/subtropical/extratropical cyclone
WV = tropical wave
DB = disturbance

ALPHABET_SIZE = 9
DISCRETIZATION = NONE
```

`DB` was introduced in 1980, `WV` in 1981, and `LO` in 1987. The range therefore begins with the first complete calendar year after the last current alphabet member was introduced.

## Frozen range

```text
START_YEAR = 1988
END_YEAR = 2025
RANGE_RULE = COMPLETE_CALENDAR_YEARS_1988_THROUGH_2025_INCLUSIVE
RANGE_SELECTION_BASIS = FIRST_COMPLETE_YEAR_AFTER_CURRENT_NINE_STATE_STATUS_ALPHABET_WAS_FULLY_AVAILABLE__THROUGH_LAST_COMPLETE_SEASON_IN_FROZEN_ARCHIVE
VALUE_DEPENDENT_CUTOFF = NO
```

Later custody must use the frozen Atlantic HURDAT2 release that includes the 2025 season and must ignore records outside this range.

## Eligible record rule

Only standard synoptic best-track records are eligible:

```text
ELIGIBLE_UTC_TIMES = 0000,0600,1200,1800
ASYNOPTIC_RECORDS = EXCLUDE
```

The record identifier may be present on a standard synoptic record (for example landfall `L`) but does not alter eligibility if the time is one of the four standard synoptic times.

Each HURDAT2 storm header defines a separate physical track/segment. Triples never cross storm boundaries.

Within a storm:

1. retain only standard synoptic records inside 1988–2025;
2. order by UTC time;
3. split into maximal runs whose successive timestamps differ by exactly six hours;
4. any missing/invalid/unrecognized status breaks the run;
5. partition each run from its first eligible record into consecutive nonoverlapping blocks of three;
6. discard one or two trailing records at the end of each run.

No gap compression or imputation is allowed.

## Frozen roles

For each retained block:

```text
A = earliest six-hour status record
B = intermediate six-hour status record
C = latest six-hour status record
ROLE_PERMUTATION = FORBIDDEN
```

The same A/B/C records confront all five successor packages:

```text
PGH-OBJ-0041 -> A independent C
PGH-OBJ-0042 -> A independent B given C
PGH-OBJ-0043 -> A independent B
PGH-OBJ-0044 -> B independent C given A
PGH-OBJ-0045 -> B independent C
```

## Support basis

A published NHC Joint Hurricane Testbed metadata source reports 5,409 Atlantic HURDAT2 six-hour observations in 1999–2016 alone, a strict subset of the frozen 1988–2025 range. NHC seasonal metadata show storm counts on the order of tens per season; the record-breaking 2020 page lists 31 systems. These metadata establish the preregistered >=1,000 triple-support threshold without inspecting the selected target's raw event values. Exact retained counts remain deliberately deferred to custody/parser qualification.

```text
E6_SAMPLE_SUPPORT = PASS_METADATA
R4_SCORE = 1_CONSERVATIVE__EXACT_RETAINED_COUNT_DEFERRED
```

## Missingness and validity

```text
IF record time is not a standard synoptic time -> exclude record before run formation
IF status is blank, malformed, or outside the frozen nine-state alphabet -> break run and exclude that record
IF six-hour timestamp continuity fails -> break run
IF a three-record block is incomplete -> discard block
IMPUTATION = FORBIDDEN
CROSS_STORM_JOIN = FORBIDDEN
GAP_COMPRESSION = FORBIDDEN
```

No other value-dependent filtering is allowed.

## Contamination

```text
CONTAMINATION = C1_GENERAL_DOMAIN_KNOWLEDGE_ONLY
```

General knowledge about tropical cyclones and one NHC metadata-support source concerning tropical-cyclone forecasting were encountered. No search sought or disclosed a qualitative or quantitative result for any of the five frozen independence hypotheses on the native HURDAT2 status sequence.

## Custody boundary

```text
RAW_DATA_HASH = NOT_YET_ESTABLISHED
RAW_DATA_BYTES_ACCESSED = NO
EVENT_STATUS_VALUES_INSPECTED = NO
DEPENDENCE_STATISTIC_COMPUTED = NO
TARGET_SPECIFIC_NULL_CALIBRATION = NOT_DESIGNED
```

A later separately authorized custody operation must resolve the exact frozen Atlantic HURDAT2 release locator, retrieve it without exploratory analysis, record byte hashes and provenance, and qualify a parser against this target freeze.

## Claim ceiling

```text
COMMON_TARGET = FROZEN
FIVE_CANDIDATES = UNTESTED
EMPIRICAL_RESULT = NONE
SUCCESSOR_VALIDATED = NO
STRONG_PGH_CONFIRMED = NO
R2B = UNSATISFIED
FCP_EFFECT = NONE
```
