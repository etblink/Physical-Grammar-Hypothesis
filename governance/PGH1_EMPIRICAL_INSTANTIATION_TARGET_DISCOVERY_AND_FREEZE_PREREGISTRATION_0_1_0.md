# PGH-1 Empirical Instantiation Target Discovery and Freeze — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_EMPIRICAL_INSTANTIATION_TARGET_DISCOVERY_AND_FREEZE
REGISTRY_ID = PGH-OP-0063
CANONICAL_BASE = 7d27b6278db284cc4225ec87859c067cefb5d414
TARGET_SELECTION_PROTOCOL = PGH-OBJ-0036
LEAKAGE_FAILURE = PGH-FAIL-0034
TESTABLE_GRAMMAR = PGH-GRAM-0008
SEMANTIC_BRIDGE = PGH-OBJ-0035
TARGET_PREDICTION = WITHHELD_FROM_DISCOVERY_SCORING
EMPIRICAL_EVENT_VALUE_INSPECTION = FORBIDDEN
DEPENDENCE_ANALYSIS = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Discover, metadata-screen, rank, and freeze at most one first empirical instantiation target under the already qualified nonleaking selection protocol.

This operation may search external public sources and inspect dataset/experiment metadata. It may not inspect candidate event values, dependence/correlation summaries relevant to the selected variable triple, conditional-independence results, or model-fit results.

If no candidate survives, report no target rather than relax the rules.

## Search lanes

### D1 — discrete public physical time series

Seek publicly archived physical measurements with native finite/categorical records at regular or clearly ordered observation times, enough history for repeated three-record blocks, stable timestamp identity, and auditable raw access.

### D2 — ordered categorical experimental readouts

Seek public experimental datasets with repeated trials/events and three objectively ordered detector/readout/process-stage records, preferably natively finite.

### D3 — ordered event/process archives

Seek physical event archives where three ordered records can be associated by a value-independent event or timestamp matching rule and where the role order comes from acquisition/process/spatial metadata.

## Frozen discovery-query discipline

Initial search phrases may use combinations of:

```text
public physical measurement time series discrete categorical archive event-level
public experimental data repeated trials categorical detector readout archive
public physical sensor index discrete time series download archive
public event-level physics data ordered detector stages archive
public geophysical discrete index time series official data
public space weather discrete index archive 3-hour data
public atmospheric categorical observation archive hourly data
public detector event data categorical hit layers open data
```

Queries may add source-authority terms such as `official`, `data center`, `open data`, `archive`, `documentation`, or a candidate name **after** that candidate has been independently identified.

Queries may not use:

```text
conditional independence
Markov property
memoryless
first-order Markov
A independent C given B
conditional correlation
```

except after a candidate has been identified and only to classify contamination.

## Candidate ledger minimum

Aim to identify at least five plausible metadata-level candidates across at least two lanes if the search supports them.

A smaller ledger is acceptable if late searches return only clearly ineligible or duplicative architectures.

## Metadata fields to collect

For every plausible candidate record only:

```text
CANDIDATE_ID
DATASET_OR_EXPERIMENT_NAME
PHYSICAL_SYSTEM
AUTHORITATIVE_SOURCE
PUBLIC_DATA_LOCATOR
RECORD_VARIABLE_DESCRIPTION
OBJECTIVE_ORDERING_RULE
NATIVE_DATA_TYPE_OR_ALPHABET
DOCUMENTED_SAMPLE_OR_EVENT_COUNT
JOINT_MATCHING_RULE
MISSINGNESS_OR_SELECTION_DOCUMENTATION
PREPROCESSING_REQUIRED
ARCHIVAL_DATE_OR_VERSION
CONTAMINATION_CLASS
ELIGIBILITY_DISPOSITION
REJECTION_REASON_IF_ANY
```

Do not download or inspect event values in this operation unless a source requires a tiny non-statistical format sample solely to establish file schema; if so, the sample must not be used to assess dependence and must be recorded explicitly.

## Frozen scoring scale

For each eligible `C0/C1` candidate, score R1–R10 from `PGH-OBJ-0036`:

```text
2 = STRONG / DIRECTLY SATISFIED
1 = ADEQUATE_WITH_MINOR_CAVEAT
0 = WEAK_OR_MATERIAL_AMBIGUITY
```

Total score range: `0..20`.

A candidate with any failed eligibility criterion is not scored for selection.

## Criterion interpretation

```text
R1 role clarity: 2 if order is intrinsic and documented; 1 if derived by one simple metadata rule; 0 if ambiguous.
R2 native finite: 2 native finite/categorical; 1 bounded integer requiring fixed grouping; 0 continuous requiring flexible discretization.
R3 joint access: 2 direct event/time indexed triples; 1 deterministic join across files; 0 aggregate-only/ambiguous.
R4 support: 2 clearly large sample relative to state space; 1 likely adequate; 0 sparse/unclear.
R5 preprocessing: 2 simple row/block selection; 1 modest deterministic parsing; 0 substantial reconstruction.
R6 selection/missingness: 2 explicit/simple; 1 documented caveats; 0 flexible/opaque.
R7 reproducibility: 2 official stable/raw archive; 1 durable scholarly archive; 0 weak hosting.
R8 physical-record clarity: 2 direct physical measurement/index; 1 derived but standard physical index; 0 semantically remote.
R9 discretization rigidity: 2 native categories; 1 externally fixed calibration; 0 analyst-chosen bins.
R10 archival stability: 2 stable official/permanent archive; 1 credible persistent repository; 0 unstable link/service.
```

## Frozen selection rule

1. apply E0–E8 and contamination classification;
2. exclude failed eligibility and `C3` candidates;
3. send `C2` candidates to contamination review before scoring;
4. score remaining `C0/C1` candidates R1–R10;
5. choose the highest score;
6. apply the already frozen tie break if needed.

No target-result information may override the rule.

## Target freeze contents

If a target is selected, Commit 2 must freeze:

```text
SELECTED_TARGET_ID
AUTHORITATIVE_SOURCE_AND_RAW_DATA_LOCATOR
ARCHIVAL_VERSION_OR_DATE_IF_AVAILABLE
PHYSICAL_SYSTEM_DESCRIPTION
EXACT_ROLE_ASSIGNMENT_RULE
EXACT_RECORD_VARIABLE
EXACT_NATIVE_ALPHABET_OR_DISCRETIZATION_STATUS
EXACT_EVENT_OR_TRIPLE_CONSTRUCTION_RULE
TIME_RANGE_OR_EVENT_RANGE_SELECTION_RULE_CHOSEN_WITHOUT_VALUE_INSPECTION
MISSING_DATA_RULE_AT_TARGET_SELECTION_SCOPE
CONTAMINATION_CLASS
SELECTION_SCORE_AND_TIE_BREAK_STATUS
RAW_DATA_HASH = DEFERRED_IF_REMOTE_BYTES_NOT_YET_MATERIALIZED
```

No CI statistic or empirical result belongs in this target freeze.

## Time/event-range rule

Prefer the complete stable archive available under one consistent measurement definition.

If the archive spans documented definition changes, select the longest contiguous modern interval with one stated definition/version, based only on documentation chronology.

If multiple equal intervals remain, choose the earliest by date.

Do not choose a time interval based on values or dependence behavior.

## Triple construction rule

For ordered time-series data, use **non-overlapping consecutive triples** in chronological order unless the target's native trial structure already supplies three records per event.

For a time series indexed `x_0,x_1,...`, the prospective roles are:

```text
A = x_(3k)
B = x_(3k+1)
C = x_(3k+2)
```

for the frozen eligible range, after applying only documented missing-record exclusions.

This prevents overlapping-window duplication from being introduced by discretionary analysis.

## Contamination check timing

Only after a candidate is independently identified and its architecture recorded may documentation be searched for exact disclosures of the target relation.

The contamination check may classify but may not use a favorable/unfavorable result for ranking.

## Outcome space

```text
A = ONE_ELIGIBLE_UNCONTAMINATED_TARGET_IS_SELECTED_BY_THE_FROZEN_RUBRIC_AND_ITS_ROLE_ASSIGNMENT_DATA_IDENTITY_AND_TRIPLE_CONSTRUCTION_RULE_ARE_FROZEN_BEFORE_ANY_DEPENDENCE_ANALYSIS

B = MULTIPLE_CANDIDATES_SURVIVE_BUT_METADATA_OR_CONTAMINATION_INFORMATION_IS_INSUFFICIENT_TO_APPLY_THE_FROZEN_SELECTION_RULE_WITHOUT_A_NARROW_FOLLOWUP

C = NO_CANDIDATE_SURVIVES_THE_FROZEN_ELIGIBILITY_AND_CONTAMINATION_RULES__NO_FIRST_EMPIRICAL_TARGET_IS_FROZEN

D = TARGET_DISCOVERY_REVEALS_A_DEFECT_IN_PGH_OBJ_0036_THAT_PREVENTS_NONLEAKING_SELECTION__STOP_WITHOUT_TARGET
```

## Required outputs

Commit 2 may add only:

```text
audits/PGH1_EMPIRICAL_INSTANTIATION_TARGET_DISCOVERY_AND_FREEZE_0_1_0.md
empirical/PGH1_EMPIRICAL_TARGET_CANDIDATE_LEDGER_0_1_0.md
empirical/PGH1_FIRST_EMPIRICAL_INSTANTIATION_TARGET_FREEZE_0_1_0.md
handoffs/PGH1_EMPIRICAL_INSTANTIATION_TARGET_DISCOVERY_AND_FREEZE_HANDOFF_0_1_0.md
```

The target-freeze file may state `NO_TARGET` for outcomes B–D.

Expected object if outcome A:

```text
PGH-OBJ-0037 = FIRST_EMPIRICAL_INSTANTIATION_TARGET
```

## Commit topology

```text
COMMIT_1_MESSAGE = Preregister PGH-1 empirical target discovery and freeze
COMMIT_2_MESSAGE = Freeze PGH-1 first empirical instantiation target
EXACT_COMMITS = 2
```

## Hard stops

```text
DO_NOT_INSPECT_TARGET_EVENT_VALUES
DO_NOT_COMPUTE_CORRELATIONS_OR_DEPENDENCE
DO_NOT_SEARCH_BY_MARKOV_OR_CONDITIONAL_INDEPENDENCE_SUCCESS
DO_NOT_REORDER_VARIABLE_ROLES_AFTER_DISCOVERY
DO_NOT_TUNE_DISCRETIZATION
DO_NOT_SELECT_TIME_RANGE_BY_VALUES
DO_NOT_DEFINE_STATISTICAL_TEST_AFTER_SEEING_VALUES
DO_NOT_CLAIM_EMPIRICAL_CONFIRMATION_OR_REFUTATION
DO_NOT_CHANGE_FCP
```
