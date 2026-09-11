# PGH-1 Response-Blind Target-Discovery Coverage Expansion Design Gate — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_RESPONSE_BLIND_TARGET_DISCOVERY_COVERAGE_EXPANSION_DESIGN_GATE
OPERATION_CLASS = PRE_SEARCH_METHODOLOGY_DESIGN
CANONICAL_BASE = 3c2314c4952ccff35f2579d2e040f9df24430011
CANONICAL_BASE_TREE = 4ce0cebcd1dc1057c2bcb402ff62fed8e1c37ad9
CANDIDATE_PACKAGE = PGH-OBJ-0052
TARGET_SEARCH_AT_OPEN = SUSPENDED
SEARCH_ARCHITECTURE_DESIGN_AUTHORIZED = YES
TARGET_SEARCH_DURING_THIS_OPERATION = FORBIDDEN
NEW_DATASET_INSPECTION = FORBIDDEN
NEW_TARGET_IDENTITY_DISCOVERY = FORBIDDEN
RESPONSE_DATA_ACCESS = FORBIDDEN
DEPENDENCE_INFORMATION_ACCESS = FORBIDDEN
CANDIDATE_REVISION = FORBIDDEN
```

## 1. Purpose

The canonical adversarial audit of `PGH-OP-0112` found that the independent-origin-only resumption requirement overreached the earlier response-blind prospectivity standard.

The present operation does **not** search for a target. Its sole purpose is to design and adjudicate one broader but bounded target-discovery architecture that could later be executed in a separately preregistered operation under the unchanged `PGH-OBJ-0052` identity.

The design must increase coverage without using:

- target response values;
- dependence or model-compatibility information;
- prior near-miss identities to tailor domains or institutions;
- expected PGH outcome;
- a changed eligibility rule;
- a changed target-selection rule.

## 2. Controlling candidate rules that may not change

The downstream search architecture must remain subordinate to the frozen package:

```text
G = PGH-GRAM-0010
J = PGH-OBJ-0051
S = TRUE_FOR_ALL_I_ELIGIBLE_PHYSICAL_RECORD_INTERFACES
I = SYMMETRIC_NATIVE_BINARY_TRIPLE_RECORD_INSTANTIATION_PROTOCOL_V0_1_0
```

Eligibility remains exactly:

```text
PUBLIC_OR_AUDITABLE_EVENT_LEVEL_ACCESS = YES
VERSIONED_OR_STABLY_IDENTIFIED_AUTHORITY = YES
REPEATED_JOINT_RECORD_INDEX = YES
AT_LEAST_THREE_DISTINCT_NATIVE_BINARY_RECORD_FIELDS = YES
SELECTED_FIELDS_JOINTLY_OBSERVED_PER_RECORD = YES
MISSINGNESS_OR_VALIDITY_CODES_DOCUMENTED = YES
```

Native-binary semantics, deterministic field selection, A/B/C assignment, metadata-only discovery, known-result quarantine, contamination rules and the final lexical target tie-break remain unchanged.

## 3. Frozen information allowed in design

The design may use only:

1. the syntax and concepts already present in frozen `I`;
2. the fact that the prior D1-D5 finite search returned zero eligible targets;
3. the methodological finding that domain-specific lanes did not provide sufficient coverage;
4. generic retrieval principles such as finite query matrices, exact query freezing, returned-order accounting, deduplication, authoritative-source verification, finite budgets and deterministic stopping;
5. the fact that TGT-001..TGT-039 exist as provenance/quarantine records.

It may **not** inspect the identities or individual metadata-failure reasons of TGT-001..TGT-039 for the purpose of designing the new universe.

```text
TGT_001_039_EXISTENCE_MAY_BE_KNOWN = YES
TGT_001_039_IDENTITIES_AS_DESIGN_INPUT = NO
TGT_001_039_NEAR_MISS_FAILURE_PATTERNS_AS_DESIGN_INPUT = NO
```

## 4. Frozen design candidates

Exactly three architecture classes are adjudicated.

### D-A — architecture-term general-web matrix

Construct a finite matrix of exact general-web queries using only terms derived from frozen `I` and generic metadata/retrieval language.

Allowed concept vocabulary:

```text
OFFICIAL
AUTHORITATIVE
PUBLIC
DATASET
DATA
SCHEMA
DATA_DICTIONARY
FIELDS
COLUMNS
BOOLEAN
BINARY
FLAG
TRUE_FALSE
ZERO_ONE
RECORD
EVENT
OBSERVATION
MEASUREMENT
TABLE
ARCHIVE
VERSION
RELEASE
DOWNLOAD
API
MISSING
INVALID
```

Forbidden query concepts include any scientific domain, institution, prior TGT identity, causal/dependence term, candidate name, triangle-network term or expected result.

### D-B — named general-purpose repository/registry universe

Freeze a finite list of named cross-domain repositories/registries and deterministic traversal rules.

This class is admissible only if the names and completeness rationale can be justified from the frozen closed record without new external research. Otherwise it must fail as under-specified or discretionary.

### D-C — hybrid web + named-repository architecture

Combine D-A and D-B under one deterministic closure rule.

D-C may pass only if both subarchitectures individually satisfy the design criteria and their union adds coverage without new discretionary weighting.

No fourth architecture may be invented after adjudication begins.

## 5. Design criteria

Each architecture receives `PASS`, `PARTIAL`, `FAIL`, or `NOT_ESTABLISHED` for:

```text
M1_RESPONSE_BLINDNESS
M2_CANDIDATE_IDENTITY_PRESERVATION
M3_NO_NEAR_MISS_TAILORING
M4_DOMAIN_NEUTRALITY
M5_FINITE_OR_MECHANICALLY_BOUNDED_CLOSURE
M6_DETERMINISTIC_QUERY_OR_UNIVERSE_ORDER
M7_AUDITABLE_RESULT_ACCOUNTING
M8_AUTHORITATIVE_METADATA_VERIFICATION
M9_CONTAMINATION_FIREWALL
M10_FINAL_TARGET_SELECTION_COMPATIBILITY
M11_EXECUTION_REPRODUCIBILITY_AT_PRACTICAL_SEARCH_SCOPE
M12_COVERAGE_GAIN_OVER_D1_D5_WITHOUT_OUTCOME_DIRECTION
```

A design qualifies only if all M1-M10 pass; M11-M12 may be `PASS` or `PARTIAL` only if the limitation cannot introduce result-directed discretion.

## 6. Query-construction discipline for D-A

If D-A is selected, the adjudication must freeze the exact query list in that same adjudication artifact before any query is executed.

The query set must satisfy:

```text
QUERY_COUNT_MIN = 6
QUERY_COUNT_MAX = 12
EVERY_QUERY_USES_ONLY_ALLOWED_DESIGN_VOCABULARY = YES
SCIENTIFIC_DOMAIN_TERMS = 0
INSTITUTION_NAMES = 0
KNOWN_TARGET_IDS_OR_NAMES = 0
DEPENDENCE_OR_MODEL_TERMS = 0
```

Queries may vary only to cover generic record/interface synonyms already licensed by `I`, such as:

- dataset vs archive/table;
- schema vs data dictionary;
- boolean/binary/flag/true-false;
- record/event/observation/measurement;
- version/release;
- public/download/API.

The adjudication must justify each query as a coverage combination rather than a target-specific guess.

## 7. Candidate-entry and budget design requirements

The selected design must freeze before execution:

```text
MAX_RESULTS_INSPECTED_PER_PRIMARY_QUERY
MAX_SPECIFIC_CANDIDATES_ENTERED_PER_PRIMARY_QUERY
MAX_TOTAL_SPECIFIC_CANDIDATES
DUPLICATE_IDENTITY_RULE
AUTHORITY_PAGE_REQUIREMENT
FOLLOWUP_METADATA_QUERY_BUDGET
FOLLOWUP_QUERY_TEMPLATE_RULE
CANDIDATE_ENCOUNTER_ORDER_RULE
CANDIDATE_ID_START
FULL_QUERY_MATRIX_CLOSURE_RULE
```

No early stopping merely because one eligible target is found is permitted unless the frozen final lexical target tie-break can be proven unaffected. Default expectation is full matrix closure before target selection.

## 8. Prior-target provenance and contamination

All TGT identities already encountered remain provenance records and cannot be relabeled as newly discovered.

```text
TGT_001_039 = PRIOR_ENCOUNTERS
NEXT_NEW_TARGET_ID = TGT_040
```

A duplicate or alternate packaging of a prior target retains its prior identity and cannot receive first positive credit merely because it reappears.

Encountering candidate-specific dependence/model information during a later search retains the existing contamination treatment:

```text
C0_C1 = MAY_REMAIN_ELIGIBLE
C2_C3 = INELIGIBLE_FOR_FIRST_POSITIVE_CREDIT
```

## 9. Follow-up metadata rule

A design may allow bounded follow-up metadata retrieval for an already-entered candidate only to resolve frozen eligibility fields.

Follow-up terms may include only:

```text
CANDIDATE_EXACT_IDENTITY
SCHEMA
DATA_DICTIONARY
FIELDS
COLUMNS
VERSION
RELEASE
MISSING
INVALID
API
DOWNLOAD
FORMAT
```

Forbidden follow-up terms include:

```text
CORRELATION
INDEPENDENCE
DEPENDENCE
MUTUAL_INFORMATION
ENTROPY
MARKOV
CAUSAL
TRIANGLE
T_IND
NETWORK_NONLOCALITY
FIT
COMPATIBILITY
PGH
```

## 10. Outcome space

Exactly one design outcome must be selected:

```text
A = D_A_ARCHITECTURE_TERM_GENERAL_WEB_MATRIX_QUALIFIES
B = D_B_NAMED_GENERAL_PURPOSE_REPOSITORY_UNIVERSE_QUALIFIES
C = D_C_HYBRID_QUALIFIES
D = NO_COVERAGE_EXPANSION_DESIGN_QUALIFIES
```

If multiple architectures technically pass, choose the weakest adequate design with the fewest new discretionary assumptions.

## 11. Exact output boundary

The adjudication commit may create exactly:

```text
audits/PGH1_RESPONSE_BLIND_TARGET_DISCOVERY_COVERAGE_EXPANSION_DESIGN_GATE_0_1_0.md
handoffs/PGH1_RESPONSE_BLIND_TARGET_DISCOVERY_COVERAGE_EXPANSION_DESIGN_GATE_HANDOFF_0_1_0.md
```

It may not execute or record any target search result.

## 12. Stop boundary

If a design qualifies, stop after freezing its exact search architecture.

A later separately preregistered operation is required to execute the frozen target-discovery design.

```text
SEARCH_ARCHITECTURE_MAY_BE_FROZEN = YES
TARGET_SEARCH_MAY_RUN = NO
TARGET_MAY_BE_SELECTED = NO
TARGET_VALUES_MAY_BE_ACCESSED = NO
```

Truth over PGH requires the search for a test to be broad enough to be meaningful and rigid enough not to hunt for a favorable answer.
