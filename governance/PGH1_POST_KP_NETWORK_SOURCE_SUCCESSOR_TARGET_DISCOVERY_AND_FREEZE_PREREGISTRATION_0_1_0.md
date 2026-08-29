# PGH-1 Post-Kp Network/Source Successor Target Discovery and Freeze — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_POST_KP_NETWORK_SOURCE_SUCCESSOR_TARGET_DISCOVERY_AND_FREEZE
REGISTRY_ID = PGH-OP-0108
CANONICAL_BASE = 9b225b7b234ad1f4bf907fd2dcf8b2628d6c80bb
PACKAGE_SCIENTIFIC_COMMIT = e4ab7459b958f04243a188747257778a178c05c6
CANDIDATE_PACKAGE = PGH-OBJ-0052
FORMAL_GRAMMAR = PGH-GRAM-0010
SEMANTIC_BRIDGE = PGH-OBJ-0051
SCOPE = TRUE
TARGET_DISCOVERY_METADATA_SEARCH = AUTHORIZED
TARGET_VALUES = FORBIDDEN
DEPENDENCE_ANALYSIS = FORBIDDEN
T_IND_COMPATIBILITY_CHECK = FORBIDDEN
TARGET_SPECIFIC_STATISTIC_DESIGN = FORBIDDEN
DATA_CUSTODY = FORBIDDEN
NEW_SCIENTIFIC_SOURCE_INTAKE = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Discover and freeze exactly one genuinely new physical record interface eligible to confront `PGH-OBJ-0052`, using public metadata/schema information only.

This operation may freeze target identity, release/version, the three binary record fields selected by the already-frozen `I`, their administrative A/B/C assignment, record-index architecture, metadata-level validity/missingness rules, and future raw-data locator class.

It may not inspect row/event values, calculate any association or model-membership quantity, design the target-specific finite-sample test, materialize target data, or infer whether the target is likely to support or refute `PGH-OBJ-0052`.

## Frozen candidate package

No component may change during this operation:

```text
G = PGH-GRAM-0010
J = PGH-OBJ-0051
S = TRUE_FOR_ALL_I_ELIGIBLE_PHYSICAL_RECORD_INTERFACES
I = SYMMETRIC_NATIVE_BINARY_TRIPLE_RECORD_INSTANTIATION_PROTOCOL_V0_1_0
```

Target discovery cannot add source ontology, causal semantics, topology metadata, latent-resource assumptions, binning, or a favorable model subset.

## Binding prior-discovery quarantine

The following project-discovered target opportunities predate the freeze of `PGH-OBJ-0052` and are ineligible for first positive credit, including alternate packaging or trivial renaming of the same underlying records:

```text
TGT-001 = GFZ definitive planetary Kp
TGT-002 = GFZ definitive C9
TGT-003 = GFZ Hp30
TGT-004 = NOAA/NCEI local K archive
TGT-005 = NOAA/NCEI GOES X-ray flare reports
TGT-006 = NOAA/NCEI Global Hourly present weather
TGT-007 = CERN CMS tracker-hit open dataset
TGT-008 = NOAA/NWS/NHC Atlantic HURDAT2 system status
TGT-009 = NOAA/NWS/NHC NE/NC Pacific HURDAT2 system status
TGT-010 = NOAA/NCEI IBTrACS v4.01 NATURE
TGT-011 = NOAA/NCEI Storm Events standardized event type
TGT-012 = Smithsonian GVP confirmed Holocene eruptions VEI
TGT-013 = USGS ComCat event type
TGT-014 = CERN LHCb masterclass events
```

The quarantine does not ban an institution or scientific field. A distinct post-freeze dataset/release with nonoverlapping underlying records may be considered if it otherwise passes the frozen rules.

## Discovery firewall

Allowed concepts are metadata/schema concepts only:

```text
OFFICIAL_OR_AUTHORITATIVE_PHYSICAL_DATASET
PUBLIC_RECORD_TABLE_OR_EVENT_ARCHIVE
STABLE_DATASET_IDENTIFIER
VERSION_OR_RELEASE_IDENTIFIER
ROW_OR_EVENT_INDEX
NATIVE_BINARY_FIELD
BOOLEAN_OR_ZERO_ONE_CODE_TABLE
JOINT_FIELD_AVAILABILITY
FIELD_DESCRIPTION
MISSING_OR_INVALID_CODE
RECORD_COUNT_OR_COVERAGE_METADATA
PUBLIC_API_OR_DOWNLOAD
ARCHIVAL_STABILITY
```

Forbidden search, follow-up, ranking, and adjudication concepts include:

```text
INDEPENDENCE
SOURCE_INDEPENDENCE
CONDITIONAL_INDEPENDENCE
CORRELATION
ASSOCIATION
MUTUAL_INFORMATION
ENTROPY_RELATION
MARKOV
MEMORYLESS
LATENT_NETWORK_FIT
TRIANGLE_NETWORK_FIT
BILOCALITY
NETWORK_NONLOCALITY
T_IND
MODEL_COMPATIBILITY
GOOD_FIT
BAD_FIT
WHICH_RESULT_WILL_SURVIVE
EXPECTED_PGH_RESULT
```

No candidate may be preferred because it is advertised as, designed as, or physically interpreted as a three-independent-source system.

## Native-binary rule

A field counts as native binary only when the authoritative schema defines exactly two substantive states for that field, excluding documented missing/invalid/null states.

Allowed examples at schema level include native Boolean values or an authority-defined two-state code such as `0/1`, `Y/N`, `true/false`.

Forbidden:

```text
ANALYST_THRESHOLDING
ANALYST_BINNING
STATE_MERGING
LEARNED_CLASSIFICATION
RESPONSE_DERIVED_DICHOTOMIZATION
POST_SEARCH_FIELD_REDEFINITION
```

## Physical-record rule

The row/event must describe a physical, natural, instrumental, or experimental object/event/measurement state. A table whose selected binary fields are purely administrative bookkeeping, access-control, publication-status, or file-management flags is ineligible.

Instrument/quality/diagnostic flags may qualify only when the authority documents them as properties of the scientific observation/event or its measured signal, rather than repository administration.

## Frozen five discovery lanes

Search is bounded to five record-interface lanes. They are architecture coverage lanes, not likelihood judgments:

```text
D1 = ASTRONOMICAL_MISSION_OR_SOURCE_CATALOG_TABLES
D2 = SPACE_OR_HELIOPHYSICS_EVENT_OR_OBSERVATION_TABLES
D3 = LABORATORY_OR_COLLIDER_EVENT_RECORD_TABLES
D4 = EARTH_GEOPHYSICAL_OR_ENVIRONMENTAL_EVENT_TABLES
D5 = GRAVITATIONAL_WAVE_NEUTRINO_OR_HIGH_ENERGY_TRANSIENT_CATALOG_TABLES
```

## Fixed search queries and budget

Exactly one primary web search query is permitted per lane:

```text
D1_QUERY = official astronomy mission catalog data dictionary boolean flag table release
D2_QUERY = official space mission event catalog data dictionary boolean flag release
D3_QUERY = official particle physics open data event schema boolean field release
D4_QUERY = official geophysical environmental event catalog data dictionary boolean flag release
D5_QUERY = official gravitational wave neutrino high energy transient catalog schema boolean flag release
```

For each lane:

1. inspect search results in returned order;
2. only authoritative/institution-hosted metadata, schema, data-dictionary, DOI, or official archive pages may supply eligibility facts;
3. adjudicate at most six distinct specific dataset/interface candidates;
4. stop the lane when two candidates have passed all mandatory eligibility gates or six distinct candidates have been adjudicated, whichever occurs first;
5. do not skip an otherwise relevant candidate because its scientific domain seems favorable or unfavorable to PGH;
6. mirrors may locate an official record but may not supply controlling metadata when an official source exists.

Maximum specific candidates adjudicated = 30. Maximum eligible candidates retained = 10.

A follow-up metadata query is allowed only to resolve a missing mandatory schema fact for an already-entered candidate. It must contain only the candidate identity plus metadata terms such as `schema`, `data dictionary`, `fields`, `version`, `release`, `missing`, `API`, or `download` and may not contain any forbidden dependence/model term.

## Mandatory eligibility gates

A candidate interface is eligible only if all gates pass from metadata alone:

```text
E1_PHYSICAL_RECORD_INTERFACE
  repeated rows/events describe a physical, natural, instrumental, or experimental record rather than purely administrative data

E2_PUBLIC_AUDITABLE_ACCESS
  row/event-level records are publicly retrievable or independently auditable

E3_STABLE_IDENTITY
  authoritative institution and stable dataset/table identifier are freezeable

E4_RELEASE_IDENTITY
  an explicit immutable release/version/snapshot identity is available, or the authority supplies an equivalently immutable archival release identifier

E5_AT_LEAST_THREE_NATIVE_BINARY_FIELDS
  authoritative schema documents >=3 jointly recorded native binary fields under the frozen native-binary rule

E6_JOINT_INDEXABILITY
  the selected fields occur on the same native row/event index without outcome-dependent matching

E7_DETERMINISTIC_FIELD_SELECTION
  if >3 fields qualify, exact authority field identifiers can be sorted by Unicode code-point lexical order and the first three selected without scientific discretion

E8_DETERMINISTIC_ROLE_ASSIGNMENT
  selected field identifiers can be sorted by the same rule and assigned A/B/C in that order; no physical role semantics are added

E9_DOCUMENTED_VALIDITY_OR_NULL_HANDLING
  schema documents null/missing/invalid representation sufficiently for later deterministic parsing, or the release format disallows such values for the selected fields

E10_LOW_PREPROCESSING
  future analysis can obtain the three native binary fields by direct parsing/query plus fixed validity filtering; no scientific reconstruction, model inversion, learned classifier, or target-dependent feature engineering is required

E11_PRIOR_TARGET_NOVELTY
  candidate is not TGT-001..TGT-014 and is not alternate packaging of their underlying record opportunity

E12_NO_DEPENDENCE_CONTAMINATION
  metadata inspected during discovery do not reveal a numerical or qualitative result about the candidate's compatibility with the frozen triangle observed model class or equivalent dependence properties
```

Failure of one gate rejects the candidate for this operation. Eligibility may not be weakened after candidate discovery.

## Candidate-set closure and selection

After all five lane budgets terminate, the eligible set closes permanently for OP-0108.

No score is used. Selection follows the already-frozen `PGH-OBJ-0052` administrative tie-break exactly.

For each eligible candidate define:

```text
CANONICAL_AUTHORITY_NAME = formal institutional authority name on the controlling official metadata page
```

If multiple coequal authorities are listed, sort their formal names by Unicode code-point order and join with ` / `.

```text
STABLE_DATASET_IDENTIFIER = DOI if a dataset DOI exists; otherwise the exact official immutable dataset/table identifier
VERSION_OR_RELEASE_IDENTIFIER = exact official release/version/snapshot identifier
```

Select the lexicographically smallest exact tuple:

```text
(CANONICAL_AUTHORITY_NAME,
 STABLE_DATASET_IDENTIFIER,
 VERSION_OR_RELEASE_IDENTIFIER)
```

Unicode code-point lexical order is used. No substantive scientific property may break a tie.

If duplicate official access paths represent the same release, prefer the authority-hosted canonical metadata/download path; remaining path ties are lexical.

## Frozen field and role rule

For the selected target:

1. enumerate every field that passes the native-binary rule from the authoritative schema, without reading data values;
2. sort exact field identifiers by Unicode code-point order;
3. choose the first three;
4. assign `A`, `B`, `C` in that same order;
5. record the authority's exact two substantive states and documented null/invalid representation for each field.

No later field replacement is allowed under `PGH-OBJ-0052` because of missingness frequency, variance, imbalance, dependence, statistical power, or empirical result.

## Range/release rule

The target is the complete immutable release/snapshot selected by the metadata tuple unless the release itself is partitioned into independently identified files/tables. If a deterministic subtable is required, the exact subtable identifier must be fixed from metadata before any values are accessed.

No row sampling or date-window optimization is allowed in target discovery. Any future computational subsampling, if scientifically required, must be preregistered after target freeze and before data materialization and may not alter target identity.

## Contamination classes

```text
C0 = no candidate-specific dependence/model-class information encountered
C1 = general domain knowledge only; no candidate-specific triangle/dependence result
C2 = qualitative candidate-specific dependence/model-class hint encountered
C3 = numerical/exact candidate-specific dependence/model-class result encountered
```

`C0/C1` may remain eligible. `C2/C3` are ineligible for first positive credit and are retained in the ledger as contaminated rejections.

No follow-up search is allowed to determine whether a C2/C3 hint is reassuring or damaging.

## Required outputs

If discovery executes, Commit 2 may contain only:

```text
empirical/PGH1_POST_KP_NETWORK_SOURCE_SUCCESSOR_TARGET_CANDIDATE_LEDGER_0_1_0.md
empirical/PGH1_POST_KP_NETWORK_SOURCE_SUCCESSOR_TARGET_FREEZE_0_1_0.md
handoffs/PGH1_POST_KP_NETWORK_SOURCE_SUCCESSOR_TARGET_DISCOVERY_AND_FREEZE_HANDOFF_0_1_0.md
```

No navigation surfaces are modified in this scientific operation.

## Outcome space

```text
A = ONE_NEW_TARGET_QUALIFIES_AND_IS_FROZEN
B = NO_DISCOVERED_TARGET_PASSES_ALL_MANDATORY_GATES
C = OTHERWISE_ELIGIBLE_CANDIDATES_EXIST_BUT_ALL_ARE_C2_OR_C3_CONTAMINATED
D = METADATA_OR_ACCESS_IS_INSUFFICIENT_TO_FREEZE_A_REPRODUCIBLE_TARGET
```

B/C/D must be accepted if warranted. No new lane, query, field transformation, or eligibility relaxation may be added because the initial pool is inconvenient.

## Commit topology

```text
COMMIT_1 = PREREGISTRATION_ONLY
COMMIT_2 = CANDIDATE_LEDGER_TARGET_FREEZE_AND_HANDOFF_ONLY
EXACT_COMMITS = 2
```

## Stop boundary

```text
STOP_AFTER_TARGET_IDENTITY_AND_ROLE_FREEZE
STOP_BEFORE_TARGET_VALUE_INSPECTION
STOP_BEFORE_RAW_DATA_DOWNLOAD_OR_MATERIALIZATION
STOP_BEFORE_DATA_CUSTODY
STOP_BEFORE_TARGET_SPECIFIC_ANALYSIS_PREREGISTRATION
STOP_BEFORE_FINITE_SAMPLE_MODEL_MEMBERSHIP_STATISTIC
STOP_BEFORE_CALIBRATION_DESIGN
STOP_BEFORE_ANY_CANDIDATE_VERDICT
```

## Claim ceiling

```text
TARGET_MAY_BE_FROZEN = YES
EMPIRICAL_DATA_ACCESSED = NO
PGH_OBJ_0052_TESTED = NO
PGH_OBJ_0052_VALIDATED = NO
STRONG_PGH_CONFIRMED = NO
R2B = UNSATISFIED
FCP_EFFECT = NONE
```

Truth over PGH.
