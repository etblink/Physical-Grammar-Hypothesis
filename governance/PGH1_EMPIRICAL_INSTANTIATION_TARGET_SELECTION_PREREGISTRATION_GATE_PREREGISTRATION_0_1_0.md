# PGH-1 Empirical Instantiation Target Selection Preregistration Gate — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_EMPIRICAL_INSTANTIATION_TARGET_SELECTION_PREREGISTRATION_GATE
REGISTRY_ID = PGH-OP-0062
CANONICAL_BASE = d7f82ad8a7e5bb2b5a1a397002af42643ee50f65
TESTABLE_GRAMMAR = PGH-GRAM-0008
SEMANTIC_BRIDGE = PGH-OBJ-0035
TRANSFER_THEOREM = PGH-DER-0031
POSTHOC_FAILURE = PGH-FAIL-0033
FROZEN_SOURCE_CORPUS = 85_DISTINCT_ACCEPTED
TARGET_DISCOVERY = FORBIDDEN
EMPIRICAL_DATA_INSPECTION = FORBIDDEN
TARGET_CONDITIONAL_INDEPENDENCE_INSPECTION = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Freeze the rules by which a first empirical instantiation of `PGH-GRAM-0008` may later be discovered and selected, before any candidate target's relevant joint-distribution dependence pattern is inspected.

This operation does not choose a target, search external datasets, inspect sample values, compute conditional independence, or define a final statistical threshold.

Its sole scientific purpose is to prevent target-selection leakage.

## Candidate empirical form

A later target must supply repeated jointly indexable observations of three finite record-valued variables

\[
\mathcal A,\mathcal B,\mathcal C
\]

or variables admitting a fully preregistered finite discretization before target-pattern inspection.

The candidate prediction to be withheld during target discovery is

\[
\mathcal A\perp\mathcal C\mid\mathcal B.
\]

Discovery and ranking may not use whether a candidate appears to satisfy or violate this relation.

## Eligibility E0 — physical-record scope

The variables must be records of a physical system or physical measurement process, not purely social, financial, linguistic, or synthetic benchmark labels.

Computational/simulated data are ineligible for the first empirical instantiation unless the operation is explicitly reclassified as a simulation validation rather than a physical test.

## Eligibility E1 — objective three-role architecture

A candidate must expose three distinguishable record roles without using the target dependence pattern to define them.

For this first test, acceptable role assignment must come from one of:

```text
A. DECLARED_MEASUREMENT_OR_ACQUISITION_ORDER
B. DECLARED_PROCESS_STAGE_ORDER
C. DECLARED_SPATIAL_OR_INSTRUMENTAL_CHAIN_ORDER
```

The assignment rule is:

```text
EARLIEST_OR_UPSTREAM_ROLE -> A
INTERMEDIATE_ROLE -> B
LATEST_OR_DOWNSTREAM_ROLE -> C
```

If a candidate lacks an objective ordering from metadata/experimental design, it is ineligible for this first test.

No reordering of A/B/C after inspecting data is permitted.

## Eligibility E2 — joint sample identity

The three records must be jointly attributable to the same trial/event/unit of physical observation, or admit an auditable matching rule fixed independently of their values.

Aggregate marginals without joint event identity are ineligible.

## Eligibility E3 — finite alphabet / frozen discretization

Preference order:

```text
1. NATIVELY_FINITE_CATEGORICAL_RECORDS
2. FINITE_INTEGER_COUNT_RECORDS_WITH_A_PRIORI_BOUNDS_OR_PHYSICAL_CATEGORIES
3. CONTINUOUS_RECORDS_ONLY_IF_A_DISCRETIZATION_RULE_CAN_BE_FROZEN_BEFORE_VALUE_INSPECTION
```

For continuous variables, a future target-specific preregistration must define bins from instrumentation, standards, physically meaningful thresholds, or an external calibration rule—not by optimizing the target conditional-independence result.

## Eligibility E4 — public/auditable access

The raw or event-level data needed for a later joint-distribution analysis must be publicly downloadable, reproducibly queryable, or otherwise auditable by an independent reviewer.

Published summary statistics alone are insufficient unless they are mathematically sufficient for the exact preregistered test.

## Eligibility E5 — adequate sample support

Before inspecting the target dependence pattern, metadata must indicate enough repeated events to support estimation across the intended finite cells.

A later protocol must predefine minimum cell-support / smoothing / exact-test handling.

Targets with obviously sparse high-dimensional contingency structure are deprioritized or rejected.

## Eligibility E6 — measurement and selection clarity

The acquisition rule, missing-data rule, event selection, censoring, and known conditioning variables must be documented well enough to specify what joint distribution is being tested.

Targets requiring undocumented reconstruction or flexible event filtering are ineligible.

## Eligibility E7 — no known target-result use

Discovery may inspect:

```text
DATASET_TITLE
EXPERIMENTAL_PURPOSE
VARIABLE_DEFINITIONS
MEASUREMENT_ORDER
ALPHABET_OR_DATA_TYPE
SAMPLE_SIZE_METADATA
ACCESS_FORMAT
MISSINGNESS_DOCUMENTATION
EVENT_SELECTION_DOCUMENTATION
INSTRUMENT_DESCRIPTION
```

Discovery may **not** inspect or use for ranking:

```text
PAIRWISE_CORRELATIONS_AMONG_A_B_C
CONDITIONAL_CORRELATIONS
MUTUAL_INFORMATION_AMONG_A_B_C
MARKOV_OR_MEMORYLESSNESS_CLAIMS_FOR_THE_TARGET_TRIPLE
CONDITIONAL_INDEPENDENCE_TESTS
MODEL_FIT_TO_A_TO_B_TO_C
P_VALUES_OR_EFFECT_SIZES_RELEVANT_TO_THE_TARGET_CI
PLOTS_THAT_REVEAL_THE_TARGET_DEPENDENCE_PATTERN
```

If unavoidable documentation already discloses the exact target result for a candidate, that candidate must be flagged `CONTAMINATED_FOR_FIRST_TEST` and may not receive first-test predictive credit.

## Eligibility E8 — no theory-selection by known success

A target may not be selected because its field commonly assumes a Markov chain, because a published model already uses `A->B->C`, or because the relevant system is known to obey conditional independence.

The discovery query itself must not contain target-result phrases such as:

```text
conditional independence
Markov property holds
memoryless data
A independent C given B
```

except when checking contamination after a candidate has been identified independently.

## Ranking criteria

Among eligible uncontaminated candidates, rank before dependence inspection using only:

```text
R1_MEASUREMENT_ROLE_CLARITY
R2_NATIVE_FINITE_RECORDS
R3_EVENT_LEVEL_JOINT_ACCESS
R4_SAMPLE_SIZE_AND_CELL_SUPPORT
R5_MINIMAL_PREPROCESSING
R6_LOW_SELECTION_OR_MISSINGNESS_AMBIGUITY
R7_INDEPENDENT_REPRODUCIBILITY
R8_PHYSICAL_INTERPRETATION_CLARITY
R9_LOW_DISCRETIZATION_FLEXIBILITY
R10_STABLE_PUBLIC_ARCHIVAL_ACCESS
```

Each criterion must be scored on a frozen ordinal scale in the later discovery operation.

Tie breaking must be specified before target-result inspection.

## Frozen tie-break rule

If total rubric scores tie, choose in this order:

```text
1. NATIVE_FINITE_ALPHABETS_OVER_DISCRETIZED
2. LARGER_DOCUMENTED_EVENT_COUNT
3. FEWER_REQUIRED_PREPROCESSING_STEPS
4. EARLIER_PERMANENT_ARCHIVAL_PUBLICATION_DATE
5. LEXICOGRAPHIC_DATASET_OR_EXPERIMENT_IDENTIFIER
```

No scientific-result information may enter the tie break.

## Contamination classes

```text
C0 = NO_TARGET_RESULT_EXPOSURE_FOUND
C1 = GENERAL_DOMAIN_MODELING_KNOWLEDGE_ONLY
C2 = DOCUMENTATION_HINTS_AT_MEMORY_OR_DEPENDENCE_BUT_NOT_THE_EXACT_TRIPLE_RESULT
C3 = EXACT_OR_EFFECTIVELY_EXACT_TARGET_CI_RESULT_ALREADY_DISCLOSED
```

For the first empirical test:

```text
ELIGIBLE = C0; C1
REVIEW_REQUIRED = C2
INELIGIBLE_FOR_PREDICTIVE_CREDIT = C3
```

## Candidate discovery discipline

The later discovery operation must:

1. search by physical-record architecture and data accessibility, not by predicted dependence;
2. create a candidate ledger before inspecting candidate event values;
3. record URLs/identifiers and metadata provenance;
4. score eligibility/ranking only from permitted information;
5. freeze the selected target, role assignment, and raw-data identity before running any dependence computation;
6. retain rejected candidates and reasons.

## Statistical-protocol boundary

This gate does not choose the final conditional-independence statistic.

After target selection but before inspecting dependence results, a separate protocol must freeze:

```text
NULL_AND_ALTERNATIVE
ESTIMATOR_OR_EXACT_TEST
SIGNIFICANCE_OR_DECISION_RULE
EFFECT_SIZE_OR_DIVERGENCE_MEASURE
SPARSE_CELL_HANDLING
MULTIPLE_TESTING_RULE_IF_ANY
MISSING_DATA_RULE
ROBUSTNESS_CHECKS
```

No exploratory target-dependence analysis may occur before that protocol is frozen.

## Outcome space

```text
A = A_NONLEAKING_TARGET_SELECTION_PROTOCOL_CAN_BE_FROZEN_WITH_OBJECTIVE_ROLE_ASSIGNMENT_ELIGIBILITY_RANKING_CONTAMINATION_AND_TIE_BREAK_RULES__A_SEPARATE_TARGET_DISCOVERY_OPERATION_IS_JUSTIFIED

B = THE_FIRST_EMPIRICAL_TARGET_CANNOT_BE_SELECTED_WITHOUT_USING_INFORMATION_ENTANGLED_WITH_THE_PREDICTED_CONDITIONAL_INDEPENDENCE__EMPIRICAL_TESTABILITY_REMAINS_ONLY_IN_PRINCIPLE

C = THE_PROTOCOL_IS_PLAUSIBLE_BUT_A_SPECIFIC_DATA_DISCOVERY_OR_STATISTICAL_DESIGN_GAP_MUST_BE_RESOLVED_BEFORE_TARGET_SEARCH

D = THE_CURRENT_SEMANTIC_BRIDGE_IS_TOO_UNDERSPECIFIED_TO_DEFINE_NONLEAKING_TARGET_SELECTION
```

## Required outputs

Commit 2 may add only:

```text
audits/PGH1_EMPIRICAL_INSTANTIATION_TARGET_SELECTION_PREREGISTRATION_GATE_0_1_0.md
research/formalizations/PGH1_EMPIRICAL_TARGET_SELECTION_PROTOCOL_0_1_0.md
research/failures/PGH_FAIL_EMPIRICAL_TARGET_SELECTION_RESULT_LEAKAGE_0_1_0.md
handoffs/PGH1_EMPIRICAL_INSTANTIATION_TARGET_SELECTION_PREREGISTRATION_GATE_HANDOFF_0_1_0.md
```

Expected identities if earned:

```text
PGH-OBJ-0036 = EMPIRICAL_TARGET_SELECTION_PROTOCOL
PGH-FAIL-0034 = EMPIRICAL_TARGET_SELECTION_RESULT_LEAKAGE
```

## Commit topology

```text
COMMIT_1_MESSAGE = Preregister PGH-1 empirical instantiation target selection gate
COMMIT_2_MESSAGE = Qualify PGH-1 empirical target selection protocol
EXACT_COMMITS = 2
```

## Hard stops

```text
DO_NOT_SEARCH_EXTERNAL_TARGETS
DO_NOT_NAME_CANDIDATE_DATASETS
DO_NOT_INSPECT_EMPIRICAL_EVENT_VALUES
DO_NOT_INSPECT_TARGET_CONDITIONAL_INDEPENDENCE
DO_NOT_CHOOSE_STATISTICAL_THRESHOLD
DO_NOT_CLAIM_AN_EMPIRICAL_PREDICTION_HAS_BEEN_TESTED
DO_NOT_CHANGE_FCP
```
