# PGH-1 Response-Blind Target-Discovery Coverage Expansion Execution — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_RESPONSE_BLIND_TARGET_DISCOVERY_COVERAGE_EXPANSION_EXECUTION
OPERATION_CLASS = METADATA_ONLY_TARGET_DISCOVERY_AND_FREEZE
CANONICAL_BASE = a469018f321065d61212757d0e28ec59f2ae150b
CANONICAL_BASE_TREE = ccd5c81c435852006dc46bcdc893abe2f4e22a02
CANDIDATE_PACKAGE = PGH-OBJ-0052
DESIGN_PREREGISTRATION_BLOB = 68c088e4b314a0b7d6b3451d96f2ce37de8833e0
DESIGN_ADJUDICATION_BLOB = d8e69f8987dbad6d18c0f1fde6f2c3e37f98423a
DESIGN_HANDOFF_BLOB = 1277fdff89f90853796338c2c07e479a2193444b
TARGET_SEARCH = AUTHORIZED_ONLY_AS_FROZEN_BELOW
TARGET_VALUES = FORBIDDEN
RAW_DATA_MATERIALIZATION = FORBIDDEN
DEPENDENCE_ANALYSIS = FORBIDDEN
T_IND_COMPATIBILITY_CHECK = FORBIDDEN
TARGET_SPECIFIC_STATISTIC_DESIGN = FORBIDDEN
CANDIDATE_REVISION = FORBIDDEN
```

## 1. Purpose

Execute exactly the qualified response-blind Q01-Q12 metadata-search architecture and freeze either:

1. exactly one genuinely new eligible target selected by the already-frozen lexical metadata tuple; or
2. a no-target result for this exact finite execution.

The operation may discover identities and inspect public metadata/schema pages. It may not inspect row/event response values or any candidate-specific dependence/model-compatibility result.

## 2. Frozen query matrix

Exactly these twelve primary queries execute in this order:

```text
Q01 = official public dataset schema boolean fields version release
Q02 = authoritative public dataset data dictionary binary flag fields version release
Q03 = official public table schema boolean fields version release
Q04 = authoritative public table data dictionary binary flag fields version release
Q05 = official public archive schema boolean fields version release
Q06 = authoritative public archive data dictionary binary flag fields version release
Q07 = official public event schema boolean fields version release
Q08 = authoritative public event data dictionary binary flag fields version release
Q09 = official public observation schema boolean fields version release
Q10 = authoritative public observation data dictionary binary flag fields version release
Q11 = official public measurement schema boolean fields version release
Q12 = authoritative public measurement data dictionary binary flag fields version release
```

```text
QUERY_EDITING = FORBIDDEN
QUERY_REORDERING = FORBIDDEN
QUERY_SUBSTITUTION = FORBIDDEN
EXTRA_PRIMARY_QUERY = FORBIDDEN
ONE_PRIMARY_QUERY_PER_SEARCH_CALL = REQUIRED
```

## 3. Primary-search budgets

```text
MAX_RESULTS_INSPECTED_PER_PRIMARY_QUERY = 10
MAX_DISTINCT_SPECIFIC_CANDIDATES_ENTERED_PER_PRIMARY_QUERY = 3
MAX_TOTAL_DISTINCT_SPECIFIC_CANDIDATES_ADJUDICATED = 36
FULL_QUERY_MATRIX_CLOSURE = REQUIRED
EARLY_STOP_AFTER_ELIGIBLE_TARGET = FORBIDDEN
```

For each Q01-Q12, inspect returned results in returned order until the first of:

1. ten returned results have been inspected;
2. three distinct specific candidates have been entered for that query; or
3. the returned result set is exhausted.

Duplicates do not consume another candidate slot. A reencounter of a prior TGT-001..TGT-039 identity does consume a distinct-candidate slot for that query.

## 4. Two-phase execution order

To prevent eligibility metadata from influencing later primary retrieval:

```text
PHASE_A = EXECUTE_AND_CLOSE_Q01_THROUGH_Q12_PRIMARY_SEARCHES_ONLY
PHASE_B = AFTER_ALL_PRIMARY_QUERIES_CLOSE__RUN_PERMITTED_FOLLOWUPS_IN_CANDIDATE_ENCOUNTER_ORDER
```

No candidate-specific follow-up query may run before Q12 closes.

## 5. Candidate entry

A result enters candidate adjudication only when it identifies a specific dataset/interface/release family plausibly containing repeated physical, natural, instrumental or experimental records.

Generic portals, generic standards, generic documentation, journal articles without a specific dataset identity, software packages and administrative-only data are not candidate interfaces.

Search snippets may identify a candidate but may not establish a mandatory eligibility gate.

## 6. Encounter order and IDs

```text
ENCOUNTER_ORDER = Q01_TO_Q12__THEN_RETURNED_RESULT_ORDER__THEN_FIRST_DISTINCT_SPECIFIC_CANDIDATE
TGT_001_039 = PRIOR_ENCOUNTERS
NEXT_GENUINELY_NEW_TARGET_ID = TGT_040
```

If an encountered candidate is the same underlying prior target opportunity as TGT-001..TGT-039, retain its old ID and record `REENCOUNTERED_PRIOR_TARGET`.

A genuinely distinct new candidate receives TGT-040 onward in first-encounter order.

## 7. Duplicate rule

Duplicate URLs or access paths to the same authority-bound dataset/interface are collapsed. Final identity uses:

```text
CANONICAL_AUTHORITY_NAME
STABLE_DATASET_IDENTIFIER
VERSION_OR_RELEASE_IDENTIFIER
```

If release identity is initially unresolved, duplicate status remains provisional until the single allowed follow-up closes.

## 8. Follow-up metadata query rule

After all twelve primary searches close, each already-entered candidate with unresolved mandatory metadata may receive at most one follow-up search, in candidate encounter order.

Exact template:

```text
<CANDIDATE_EXACT_IDENTITY> schema data dictionary fields columns version release missing invalid API download format
```

```text
MAX_FOLLOWUP_METADATA_QUERIES_PER_CANDIDATE = 1
MAX_RESULTS_INSPECTED_PER_FOLLOWUP_QUERY = 10
SECOND_FOLLOWUP_QUERY = FORBIDDEN
TEMPLATE_EDITING_BY_MISSING_GATE = FORBIDDEN
```

If mandatory metadata remain unresolved afterward, the relevant gate remains `NOT_ESTABLISHED` and the candidate cannot qualify.

## 9. Mandatory eligibility burden

The existing operational gates remain unchanged:

```text
E1_PHYSICAL_RECORD_INTERFACE
E2_PUBLIC_AUDITABLE_ACCESS
E3_STABLE_IDENTITY
E4_RELEASE_IDENTITY
E5_AT_LEAST_THREE_NATIVE_BINARY_FIELDS
E6_JOINT_INDEXABILITY
E7_DETERMINISTIC_FIELD_SELECTION
E8_DETERMINISTIC_ROLE_ASSIGNMENT
E9_DOCUMENTED_VALIDITY_OR_NULL_HANDLING
E10_LOW_PREPROCESSING
E11_PRIOR_TARGET_NOVELTY
E12_NO_DEPENDENCE_CONTAMINATION
```

Any failed or unresolved mandatory gate makes the candidate ineligible for this operation.

No gate may be relaxed because the search again yields few or zero targets.

## 10. Native-binary and role rules

Native binary means exactly two substantive authority-defined states, excluding documented null/missing/invalid states.

Forbidden:

```text
THRESHOLDING
BINNING
STATE_MERGING
LEARNED_CLASSIFICATION
RESPONSE_DERIVED_DICHOTOMIZATION
```

If more than three qualifying native-binary fields exist, sort exact authority field identifiers by Unicode code-point lexical order and choose the first three. Assign A/B/C in the same order.

## 11. Authority rule

A mandatory gate may pass only from authoritative institutional metadata, official schema/data dictionary, official immutable release/version page, official access/API/download documentation, or an equivalently authority-bound stable source.

```text
SEARCH_SNIPPET_AS_GATE_EVIDENCE = NO
MIRROR_AS_CONTROLLING_METADATA_WHEN_AUTHORITY_EXISTS = NO
```

## 12. Contamination firewall

```text
C0 = NO_CANDIDATE_SPECIFIC_DEPENDENCE_INFORMATION
C1 = GENERAL_DOMAIN_KNOWLEDGE_ONLY
C2 = QUALITATIVE_CANDIDATE_SPECIFIC_DEPENDENCE_OR_MODEL_HINT
C3 = NUMERICAL_OR_EXACT_CANDIDATE_SPECIFIC_DEPENDENCE_OR_MODEL_RESULT
```

C0/C1 may remain eligible. C2/C3 are ineligible for first positive credit and must not be pursued further.

Forbidden search/follow-up concepts include correlation, independence, dependence, mutual information, entropy, Markov, causal, triangle, T_ind, network nonlocality, fit, compatibility and PGH.

## 13. Primary-return accounting

For every inspected result record:

```text
QUERY_ID
EXACT_QUERY_STRING
RETURNED_RANK
RESULT_TITLE
RESULT_LOCATOR
RESULT_HOST_IF_VISIBLE
DISPOSITION
CANDIDATE_ID_IF_ANY
```

Allowed dispositions:

```text
NONCANDIDATE_GENERIC_OR_NONSPECIFIC
SPECIFIC_CANDIDATE_ENTERED
DUPLICATE_OF_ALREADY_ENTERED_CANDIDATE
REENCOUNTERED_PRIOR_TARGET
NONAUTHORITATIVE_LEAD_ONLY
```

No entered candidate may later disappear from the ledger.

## 14. Candidate accounting

For every entered candidate record at least:

```text
CANDIDATE_ID
FIRST_ENCOUNTER_QUERY_AND_RANK
CANONICAL_AUTHORITY_NAME
STABLE_DATASET_IDENTIFIER
VERSION_OR_RELEASE_IDENTIFIER
CONTROLLING_AUTHORITY_LOCATORS
E1_E12_STATUS
NATIVE_BINARY_FIELD_IDENTIFIERS_IF_ESTABLISHED
JOINT_INDEXABILITY_STATUS
MISSINGNESS_VALIDITY_STATUS
CONTAMINATION_CLASS
FOLLOWUP_QUERY_USED_OR_NOT
REJECTION_GATE_IF_ANY
```

## 15. Final closure and target selection

Only after Phase A and Phase B close:

```text
CANDIDATE_SET = CLOSED_FOR_THIS_OPERATION
```

Remove rejected, unresolved-mandatory-gate, C2/C3 contaminated and prior-quarantined candidates.

For each remaining genuinely new eligible candidate, compute:

```text
(CANONICAL_AUTHORITY_NAME,
 STABLE_DATASET_IDENTIFIER,
 VERSION_OR_RELEASE_IDENTIFIER)
```

Select the lexicographically smallest exact tuple using Unicode code-point order.

No search rank, domain, sample size, expected power, familiarity, ease of later analysis or expected PGH behavior may override the tuple.

## 16. Outcome space

Exactly one outcome:

```text
A = EXECUTION_PASSES__ONE_NEW_TARGET_QUALIFIES_AND_IS_FROZEN
B = EXECUTION_PASSES__NO_DISCOVERED_NEW_TARGET_PASSES_ALL_MANDATORY_GATES
C = EXECUTION_PASSES__OTHERWISE_ELIGIBLE_NEW_TARGETS_EXIST_BUT_ALL_ARE_C2_OR_C3_CONTAMINATED_OR_PRIOR_QUARANTINED
D = EXECUTION_TECHNICALLY_FAILS__QUERY_OR_RETURN_PROVENANCE_NOT_AUDITABLE
```

No widening is permitted inside this operation after any outcome becomes apparent.

## 17. Required outputs

Commit 2 may create exactly:

```text
empirical/PGH1_RESPONSE_BLIND_TARGET_DISCOVERY_COVERAGE_EXPANSION_EXECUTION_LEDGER_0_1_0.md
empirical/PGH1_RESPONSE_BLIND_TARGET_DISCOVERY_COVERAGE_EXPANSION_TARGET_FREEZE_0_1_0.md
handoffs/PGH1_RESPONSE_BLIND_TARGET_DISCOVERY_COVERAGE_EXPANSION_EXECUTION_HANDOFF_0_1_0.md
```

## 18. Commit topology

```text
COMMIT_1 = THIS_PREREGISTRATION_ONLY
COMMIT_2 = LEDGER_PLUS_TARGET_FREEZE_PLUS_HANDOFF_ONLY
EXACT_SCIENTIFIC_COMMITS = 2
```

## 19. Stop boundary

Stop after target identity/fields/roles are frozen, or after a no-target/technical-failure result is frozen.

```text
TARGET_VALUES_ACCESS = FORBIDDEN
RAW_DATA_DOWNLOAD_OR_MATERIALIZATION = FORBIDDEN
TARGET_SPECIFIC_ANALYSIS = FORBIDDEN
T_IND_MEMBERSHIP_TEST = FORBIDDEN
CANDIDATE_VERDICT = FORBIDDEN
```

## 20. Claim ceiling

```text
PGH_OBJ_0052_IDENTITY_CHANGED = NO
TARGET_MAY_BE_FROZEN = YES
EMPIRICAL_DATA_ACCESSED = NO
PGH_OBJ_0052_TESTED = NO
PGH_OBJ_0052_VALIDATED = NO
PGH_OBJ_0052_REFUTED = NO
STRONG_PGH_CONFIRMED = NO
R2B = UNSATISFIED
```

Truth over PGH requires accepting whatever the frozen search returns without changing the search after seeing its yield.