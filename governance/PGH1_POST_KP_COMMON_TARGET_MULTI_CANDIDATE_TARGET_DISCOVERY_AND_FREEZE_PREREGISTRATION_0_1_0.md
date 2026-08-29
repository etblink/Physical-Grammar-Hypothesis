# PGH-1 Post-Kp Common-Target Multi-Candidate Target Discovery and Freeze — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_POST_KP_COMMON_TARGET_MULTI_CANDIDATE_TARGET_DISCOVERY_AND_FREEZE
REGISTRY_ID = PGH-OP-0086
CANONICAL_BASE = 9393fc7defc66d65c34ececf578c2d08dee007c9
FAMILY_PROTOCOL = PGH-OBJ-0047
FAMILY = PGH-OBJ-0041..PGH-OBJ-0045
FAMILY_SIZE = 5
TARGET_VALUES = FORBIDDEN
DEPENDENCE_ANALYSIS = FORBIDDEN
TARGET_SPECIFIC_CALIBRATION = FORBIDDEN
DATA_CUSTODY = FORBIDDEN
NEW_SCIENTIFIC_SOURCE_INTAKE = FORBIDDEN
DATASET_METADATA_SEARCH = AUTHORIZED
FCP_EFFECT = NONE
```

## Purpose

Discover and freeze exactly one genuinely new empirical target that can confront all five admitted post-Kp successor packages under one common ordered three-role realization, using only target/result-neutral public metadata.

This operation selects a target identity, role architecture, record/range rule, and future raw-data locator class. It does not inspect target values, estimate any dependence quantity, or design the target-specific null calibrations.

## Frozen five-hypothesis family

The target must support one common realization of:

```text
H1 = A_INDEPENDENT_C
H2 = A_INDEPENDENT_B_GIVEN_C
H3 = A_INDEPENDENT_B
H4 = B_INDEPENDENT_C_GIVEN_A
H5 = B_INDEPENDENT_C
```

No candidate may be added, removed, replaced, or preferentially targeted during discovery.

## Binding prior-discovery quarantine

The exact pre-Kp discovery ledger is:

```text
empirical/PGH1_EMPIRICAL_TARGET_CANDIDATE_LEDGER_0_1_0.md
```

All seven recorded target opportunities are excluded from selection for first positive successor credit:

```text
TGT-001 = GFZ definitive planetary Kp
TGT-002 = GFZ definitive C9
TGT-003 = GFZ Hp30
TGT-004 = NOAA/NCEI local K archive
TGT-005 = NOAA/NCEI GOES X-ray flare reports
TGT-006 = NOAA/NCEI Global Hourly present weather
TGT-007 = CERN CMS tracker-hit open dataset
```

The quarantine applies to alternate packaging or trivial renaming of the same underlying record opportunity. It does not ban an entire scientific field merely because one dataset from that field appeared in the old ledger.

## Discovery firewall

Allowed search concepts are limited to metadata architecture:

```text
PUBLIC_PHYSICAL_DATASET
OFFICIAL_OR_AUTHORITATIVE_ARCHIVE
REPEATED_EVENT_OR_STATE_RECORDS
NATIVE_FINITE_CATEGORICAL_STATE
OBJECTIVE_CHRONOLOGICAL_OR_UPSTREAM_INTERMEDIATE_DOWNSTREAM_ORDER
JOINTLY_INDEXABLE_RECORDS
DOCUMENTED_FORMAT
DOCUMENTED_MISSINGNESS_OR_SELECTION
EVENT_COUNT_OR_RECORD_COUNT_METADATA
ARCHIVAL_STABILITY
```

Forbidden discovery/ranking concepts include:

```text
INDEPENDENCE
CONDITIONAL_INDEPENDENCE
CORRELATION
AUTOCORRELATION
MARKOV
MEMORYLESS
MUTUAL_INFORMATION
TRANSITION_PROBABILITY
MODEL_FIT
GOOD_FIT
BAD_FIT
WHICH_CANDIDATE_SURVIVES
EXPECTED_PGH_RESULT
```

No search query may intentionally seek a dataset because a dependence pattern is known or suspected.

## Permitted discovery lanes

Search is bounded to five architecture lanes. Lanes are not scientific preferences and may yield zero candidates.

```text
D1 = OFFICIAL_GEOPHYSICAL_OR_ENVIRONMENTAL_DISCRETE_STATE_SEQUENCES
D2 = OFFICIAL_TRACKED_PHYSICAL_SYSTEMS_WITH_REPEATED_NATIVE_DISCRETE_STATES
D3 = PUBLIC_EXPERIMENTAL_OR_INSTRUMENT_EVENT_RECORDS_WITH_NATIVE_FINITE_STATES
D4 = PUBLIC_ASTRONOMICAL_OR_SPACE_OBSERVATION_EVENT_STATE_RECORDS
D5 = OTHER_AUTHORITATIVE_NATURAL_PROCESS_EVENT_OR_STATE_SEQUENCES
```

## Mandatory eligibility criteria

A target is eligible only if all E1-E11 pass from metadata alone.

```text
E1_PHYSICAL_RECORD = records describe a physical/natural/experimental system rather than a purely administrative sequence
E2_OBJECTIVE_THREE_ROLE_ORDER = A/B/C are fixed by chronology or independently documented upstream/intermediate/downstream architecture
E3_COMMON_TARGET = the same records and same role assignment apply to all five frozen hypotheses
E4_JOINT_INDEXABILITY = repeated A/B/C triples can be formed without outcome-dependent matching
E5_NATIVE_FINITE_ALPHABET = primary analysis uses a documented finite categorical alphabet with no analyst-chosen binning
E6_SAMPLE_SUPPORT = metadata imply at least 1000 usable triples before ordinary documented missingness exclusions
E7_PUBLIC_AUDITABLE_ACCESS = event/state-level records are publicly retrievable or independently auditable
E8_DOCUMENTED_SELECTION = inclusion, cadence/event identity, missingness, and status rules are documented sufficiently for deterministic parsing
E9_LOW_PREPROCESSING = no scientific reconstruction, learned classifier, model inversion, or outcome-tuned feature engineering is required
E10_ARCHIVAL_IDENTITY = source authority, dataset/version/range rule, and future raw-data locator can be frozen reproducibly
E11_PRIOR_LEDGER_NOVELTY = target is not any TGT-001..TGT-007 opportunity or alternate packaging of the same underlying record opportunity
```

Failure of one mandatory criterion rejects the candidate from the primary target selection.

## Contamination classification

Contamination concerns information already known or accidentally encountered about the five frozen dependence claims.

```text
C0 = NO_RELEVANT_DEPENDENCE_EXPOSURE
C1 = GENERAL_DOMAIN_KNOWLEDGE_ONLY__NO_CANDIDATE_SPECIFIC_DEPENDENCE_RESULT
C2 = HINT_OR_QUALITATIVE_STATEMENT_ABOUT_ONE_OR_MORE_FROZEN_DEPENDENCES
C3 = NUMERICAL_OR_EXACT_RESULT_FOR_ONE_OR_MORE_FROZEN_DEPENDENCES
```

Primary eligibility:

```text
C0 = ELIGIBLE
C1 = ELIGIBLE_WITH_DISCLOSURE
C2 = INELIGIBLE_FOR_FIRST_POSITIVE_SUCCESSOR_CREDIT
C3 = INELIGIBLE_FOR_FIRST_POSITIVE_SUCCESSOR_CREDIT
```

No follow-up literature search may be performed to determine whether a candidate is likely to pass or fail. If an authoritative metadata page itself reveals C2/C3 information, record it and reject the candidate.

## Metadata-only ranking rubric

Every eligible candidate receives R1-R10, each scored 0, 1, or 2. Scores use only metadata known before target-value inspection.

```text
R1_ROLE_CLARITY
  2 = roles mechanically fixed by native chronology/documented physical architecture
  1 = deterministic but requires one preregisterable non-outcome convention
  0 = discretionary role assignment

R2_NATIVE_FINITE_RECORD
  2 = native finite categorical state is a first-class field
  1 = finite field exists but requires deterministic documented normalization
  0 = analyst discretization required

R3_JOINT_RECORD_IDENTITY
  2 = direct sequence/track/event records support unambiguous triples
  1 = deterministic join across documented tables
  0 = discretionary matching/reconstruction

R4_SAMPLE_SUPPORT
  2 = metadata imply >= 10000 usable triples before ordinary exclusions
  1 = metadata imply 1000..9999 usable triples
  0 = <1000 or cannot establish support

R5_PREPROCESSING_BURDEN
  2 = direct parsing plus fixed grouping only
  1 = deterministic moderate transformation
  0 = scientific reconstruction/modeling required

R6_SELECTION_MISSINGNESS_CLARITY
  2 = explicit documented rules/status fields
  1 = minor metadata ambiguity with conservative deterministic rule available
  0 = materially discretionary or undocumented

R7_ACCESS_REPRODUCIBILITY
  2 = official stable public archive/API/download with version/date identity
  1 = public but less stable/manual archive
  0 = not independently reproducible

R8_PHYSICAL_RECORD_INTERPRETATION
  2 = categorical field directly describes a documented physical state/class of the tracked system/event
  1 = standardized derived physical classification
  0 = predominantly administrative/analyst label

R9_DISCRETIZATION_RIGIDITY
  2 = no analyst discretization
  1 = only one externally mandated published classification mapping
  0 = free threshold/bin choice

R10_ARCHIVAL_STABILITY
  2 = institutional long-lived archive with stable documentation/versioning
  1 = authoritative but weaker persistence/version identity
  0 = unstable or ad hoc
```

Maximum score = 20.

## Selection rule and tie break

```text
SELECT = HIGHEST_TOTAL_AMONG_E1_E11_PASS_AND_C0_OR_C1
```

If tied:

```text
T1_HIGHER_R2_NATIVE_FINITE_RECORD
T2_HIGHER_R1_ROLE_CLARITY
T3_HIGHER_R4_SAMPLE_SUPPORT
T4_HIGHER_R5_PREPROCESSING_BURDEN
T5_HIGHER_R6_SELECTION_MISSINGNESS_CLARITY
T6_HIGHER_R7_ACCESS_REPRODUCIBILITY
T7_EARLIER_PUBLIC_ARCHIVE_OR_DATASET_START_DATE_IF_DOCUMENTED
T8_LEXICOGRAPHIC_CANONICAL_DATASET_IDENTIFIER
```

No dependence-related tie break is permitted.

## Range and triple-freeze rules

For a chronological record target, the freeze must state a deterministic complete-range rule from metadata, preferably complete calendar years ending before the freeze date or a fixed released dataset version.

For naturally segmented tracks/episodes, triples may not cross segment boundaries unless the archive itself defines continuity across them.

Unless a target's native record architecture requires another deterministic grouping, sequential eligible records within each segment are partitioned prospectively into non-overlapping triples from the documented segment start/order:

```text
A_k = first record in block
B_k = second record in block
C_k = third record in block
```

A candidate with a more natural documented three-stage upstream/intermediate/downstream record may use that native mapping instead; it must be declared before values are inspected.

Missing or invalid constituent records discard the whole triple. Gaps may not be compressed to create adjacency unless the archive defines the surviving records themselves as the native event sequence.

## Required freeze contents

The selected target artifact must freeze:

1. canonical dataset/system identity and authority;
2. metadata/documentation locators;
3. native categorical field and exact allowed states as documented, or the authoritative state-code table to be bound later without inspecting event values;
4. exact A/B/C role rule;
5. exact segment/block/triple rule;
6. deterministic range/version cutoff;
7. documented missing/invalid/status handling at metadata level;
8. future raw-data locator or retrieval class;
9. contamination class;
10. eligibility and score ledger;
11. explicit confirmation that target values/dependence were not inspected.

## Outcome space

```text
A = ONE_NEW_COMMON_TARGET_QUALIFIES_AND_IS_FROZEN
B = NO_DISCOVERED_TARGET_PASSES_MANDATORY_ELIGIBILITY
C = OTHERWISE_ELIGIBLE_TARGETS_EXIST_BUT_ALL_ARE_C2_OR_C3_CONTAMINATED
D = METADATA_OR_ACCESS_INSUFFICIENT_TO_FREEZE_A_REPRODUCIBLE_TARGET
```

The operation must accept B/C/D if warranted. It may not weaken eligibility after seeing the candidate pool.

## Commit topology

```text
COMMIT_1 = PREREGISTRATION_ONLY
COMMIT_2 = METADATA_LEDGER_TARGET_FREEZE_AND_HANDOFF_ONLY
EXACT_COMMITS = 2
```

## Allowed outputs after discovery

```text
empirical/PGH1_POST_KP_COMMON_TARGET_CANDIDATE_LEDGER_0_1_0.md
empirical/PGH1_POST_KP_COMMON_TARGET_FREEZE_0_1_0.md
handoffs/PGH1_POST_KP_COMMON_TARGET_DISCOVERY_AND_FREEZE_HANDOFF_0_1_0.md
```

No navigation surfaces are modified in this scientific operation.

## Stop boundary

```text
STOP_BEFORE_TARGET_VALUE_INSPECTION
STOP_BEFORE_RAW_DATA_DOWNLOAD_OR_MATERIALIZATION
STOP_BEFORE_DATA_CUSTODY
STOP_BEFORE_TARGET_SPECIFIC_ANALYSIS_PREREGISTRATION
STOP_BEFORE_CALIBRATION_DESIGN
STOP_BEFORE_DEPENDENCE_ANALYSIS
STOP_BEFORE_ANY_CANDIDATE_VERDICT
```

## Claim ceiling

```text
TARGET_MAY_BE_FROZEN = YES
EMPIRICAL_DATA_ACCESSED = NO
CANDIDATE_TESTED = NO
CANDIDATE_VALIDATED = NO
STRONG_PGH_CONFIRMED = NO
R2B = UNSATISFIED
FCP_EFFECT = NONE
```
