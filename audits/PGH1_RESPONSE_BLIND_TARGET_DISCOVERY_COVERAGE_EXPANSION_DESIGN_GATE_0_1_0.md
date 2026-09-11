# PGH-1 Response-Blind Target-Discovery Coverage Expansion Design Gate — Adjudication 0.1.0

## Identity

```text
OPERATION_ID = PGH1_RESPONSE_BLIND_TARGET_DISCOVERY_COVERAGE_EXPANSION_DESIGN_GATE
PREREGISTRATION_COMMIT = 7531019d0d061a4a401da42d6003fa0e75620363
PREREGISTRATION_TREE = 120d142ce1f55ceefd2e37eaffa3ea5ec2f372e6
CANONICAL_BASE = 3c2314c4952ccff35f2579d2e040f9df24430011
CANDIDATE_PACKAGE = PGH-OBJ-0052
TARGET_SEARCH_EXECUTED = NO
NEW_DATASET_INSPECTED = NO
NEW_TARGET_IDENTITY_DISCOVERED = NO
RESPONSE_DATA_ACCESSED = NO
DEPENDENCE_INFORMATION_ACCESSED = NO
CANDIDATE_REVISION = NO
```

## 1. Controlling result

```text
OUTCOME = A__D_A_ARCHITECTURE_TERM_GENERAL_WEB_MATRIX_QUALIFIES
SELECTED_ARCHITECTURE = D_A__ARCHITECTURE_TERM_GENERAL_WEB_MATRIX
D_B_NAMED_GENERAL_PURPOSE_REPOSITORY_UNIVERSE = FAIL
D_C_HYBRID = FAIL

SEARCH_ARCHITECTURE_FROZEN = YES
TARGET_SEARCH_AUTHORIZED_BY_THIS_OPERATION = NO
TARGET_SELECTED = NO
TARGET_VALUES_ACCESSED = NO
PGH_OBJ_0052_IDENTITY_CHANGED = NO
```

A finite, domain-neutral, architecture-term general-web matrix qualifies as the weakest adequate response-blind coverage expansion under unchanged `PGH-OBJ-0052`.

The design is broader than the prior D1-D5 scientific-domain lanes because it searches directly for the record/schema architecture required by frozen `I`, without naming scientific domains, institutions, prior target identities, triangle-network concepts, dependence concepts, or expected PGH behavior.

This operation freezes the method only. It does not execute a single search.

## 2. Candidate-architecture adjudication

### D-A — architecture-term general-web matrix

**Verdict: QUALIFIES.**

The closed record already supplies every concept needed to construct the search language:

- public/auditable record access;
- stable/versioned authority;
- repeated records/events/observations/measurements;
- schemas/data dictionaries/fields;
- native Boolean/binary/flag coding;
- version/release identity;
- missing/invalid handling;
- public download/API access.

No scientific-domain or target-specific fact is required to generate the matrix.

The matrix is finite, exact, ordered, response-blind and frozen before execution.

### D-B — named general-purpose repository/registry universe

**Verdict: FAIL.**

The frozen closed record does not contain a prospectively justified finite list of named cross-domain registries together with a completeness, ordering and stopping rationale independent of prior target identities.

Constructing such a list now would require at least one of:

```text
NEW_EXTERNAL_RESEARCH
TGT_001_039_IDENTITY_USE_AS_DESIGN_INPUT
UNFROZEN_JUDGMENT_ABOUT_WHICH_REPOSITORIES_ARE_GENERAL_PURPOSE
```

All are outside this design gate.

D-B therefore fails the weakest-adequate-design test even though a named-registry architecture could be scientifically reasonable in some separately sourced future methodology.

### D-C — hybrid web + named-repository architecture

**Verdict: FAIL.**

D-C requires both D-A and D-B to qualify. Because D-B fails, the hybrid inherits an under-justified named-universe component and adds discretion without necessity.

## 3. M1-M12 adjudication

| Criterion | D-A | D-B | D-C |
|---|---|---|---|
| M1_RESPONSE_BLINDNESS | PASS | PASS_IN_PRINCIPLE | PASS_IN_PRINCIPLE |
| M2_CANDIDATE_IDENTITY_PRESERVATION | PASS | PASS_IN_PRINCIPLE | PASS_IN_PRINCIPLE |
| M3_NO_NEAR_MISS_TAILORING | PASS | NOT_ESTABLISHED | FAIL_BY_D_B |
| M4_DOMAIN_NEUTRALITY | PASS | NOT_ESTABLISHED | FAIL_BY_D_B |
| M5_FINITE_OR_MECHANICALLY_BOUNDED_CLOSURE | PASS | NOT_ESTABLISHED | FAIL_BY_D_B |
| M6_DETERMINISTIC_QUERY_OR_UNIVERSE_ORDER | PASS | NOT_ESTABLISHED | FAIL_BY_D_B |
| M7_AUDITABLE_RESULT_ACCOUNTING | PASS | PASS_IN_PRINCIPLE | PASS_IN_PRINCIPLE |
| M8_AUTHORITATIVE_METADATA_VERIFICATION | PASS | PASS_IN_PRINCIPLE | PASS_IN_PRINCIPLE |
| M9_CONTAMINATION_FIREWALL | PASS | PASS_IN_PRINCIPLE | PASS_IN_PRINCIPLE |
| M10_FINAL_TARGET_SELECTION_COMPATIBILITY | PASS | PASS_IN_PRINCIPLE | PASS_IN_PRINCIPLE |
| M11_EXECUTION_REPRODUCIBILITY_AT_PRACTICAL_SEARCH_SCOPE | PARTIAL | NOT_ESTABLISHED | NOT_ESTABLISHED |
| M12_COVERAGE_GAIN_OVER_D1_D5_WITHOUT_OUTCOME_DIRECTION | PASS_AT_ARCHITECTURE_SCOPE | NOT_ESTABLISHED | NOT_ESTABLISHED |

### M1 — response blindness

All D-A queries use only frozen metadata/record-interface terms. They contain no response, correlation, independence, fit, causal, triangle, network-nonlocality, candidate, target, or PGH terms.

```text
M1 = PASS
```

### M2 — candidate identity preservation

The design changes no part of `G`, `J`, `S`, or `I`. It changes only the downstream mechanism by which a separately preregistered discovery pass may encounter interfaces satisfying already-frozen `I`.

```text
M2 = PASS
```

### M3 — no near-miss tailoring

No TGT-001..TGT-039 identity or individual rejection reason was used to choose a query. Their existence matters only for later provenance/quarantine checking.

```text
M3 = PASS
```

### M4 — domain neutrality

No query contains a scientific field, experimental platform, institution, mission, instrument, geographic system, physical source class, or known target family.

```text
SCIENTIFIC_DOMAIN_TERMS = 0
INSTITUTION_NAMES = 0
KNOWN_TARGET_IDS_OR_NAMES = 0
M4 = PASS
```

### M5 — finite closure

The matrix contains exactly twelve primary queries. Each has a fixed returned-result and candidate-entry budget. All twelve queries must close before final target selection.

```text
PRIMARY_QUERY_COUNT = 12
FULL_MATRIX_CLOSURE = REQUIRED
EARLY_STOP_AFTER_ELIGIBLE_TARGET = FORBIDDEN
M5 = PASS
```

### M6 — deterministic order

The query order Q01-Q12 is frozen below. Returned results are processed in tool-returned order. Candidate encounter order is therefore deterministic relative to the recorded search return.

```text
M6 = PASS
```

### M7 — auditable result accounting

Every inspected primary-search result must be recorded in returned order with one disposition:

```text
NONCANDIDATE_GENERIC_OR_NONSPECIFIC
SPECIFIC_CANDIDATE_ENTERED
DUPLICATE_OF_ALREADY_ENTERED_CANDIDATE
REENCOUNTER_OF_TGT_001_039
NONAUTHORITATIVE_LEAD_ONLY
```

Controlling eligibility facts must be bound to authority-hosted or equivalently authoritative metadata, not search snippets.

```text
M7 = PASS
```

### M8 — authoritative metadata verification

Search results may identify a candidate, but a mandatory eligibility field can pass only from authoritative institutional metadata, an official schema/data dictionary, an official immutable release page, or an equivalently stable authority-bound record.

```text
SEARCH_SNIPPET_AS_GATE_EVIDENCE = NO
MIRROR_AS_CONTROLLING_METADATA_WHEN_AUTHORITY_EXISTS = NO
M8 = PASS
```

### M9 — contamination firewall

The existing contamination classes remain binding:

```text
C0_C1 = MAY_REMAIN_ELIGIBLE
C2_C3 = INELIGIBLE_FOR_FIRST_POSITIVE_CREDIT
```

No follow-up query may contain a dependence/model term. If candidate-specific compatibility information is encountered incidentally, it is recorded and handled under the frozen contamination rule; it may not be pursued.

```text
M9 = PASS
```

### M10 — final target-selection compatibility

The matrix closes first. Every new eligible candidate is then subject to the unchanged lexical tuple rule:

```text
(CANONICAL_AUTHORITY_NAME,
 STABLE_DATASET_IDENTIFIER,
 VERSION_OR_RELEASE_IDENTIFIER)
```

No search rank, domain, sample size, apparent statistical power, familiarity, ease of analysis, or expected PGH outcome may override that tie-break.

```text
M10 = PASS
```

### M11 — practical reproducibility

The query strings, order, budgets and accounting rules are reproducible. General-web ranking itself is time-dependent, so the exact external result set cannot be guaranteed to recur later.

That limitation is neutralized prospectively by requiring the execution operation to freeze:

```text
EXECUTION_DATE_TIME
SEARCH_TOOL_OR_PROVIDER_IDENTITY
EXACT_QUERY_STRING
RETURNED_RESULT_ORDER
RETURNED_RESULT_LOCATORS
PER_RESULT_DISPOSITION
```

No discretion is created by later ranking drift because only the actual frozen execution return may enter that operation.

```text
M11 = PARTIAL__EXTERNAL_RANKING_TIME_VARIANCE_WITH_AUDITABLE_EXECUTION_FREEZE
```

### M12 — coverage gain without outcome direction

The prior D1-D5 architecture partitioned discovery by five scientific domains. D-A removes those domain boundaries and instead searches directly on interface architecture. In query-space terms this admits discoverability from any scientific domain indexed under the frozen metadata vocabulary.

The design does not guarantee that more eligible targets will be found. Its coverage gain is architectural rather than outcome-based.

```text
M12 = PASS_AT_ARCHITECTURE_SCOPE
```

## 4. Exact frozen query matrix

The selected architecture uses two metadata-language forms across six generic interface-surface nouns derived from the allowed preregistered vocabulary.

Surface nouns:

```text
DATASET
TABLE
ARCHIVE
EVENT
OBSERVATION
MEASUREMENT
```

`DATA` and `RECORD` are not given separate primary rows because they are maximally generic retrieval terms already represented by the selected surface nouns and would add noise rather than a distinct interface class. This choice is frozen before execution and is not based on any target identity.

For each surface noun there are exactly two query forms:

- `S` form: official/public + schema + boolean + fields + version/release;
- `D` form: authoritative/public + data dictionary + binary/flag + fields + version/release.

Exact ordered strings:

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

Query audit:

```text
QUERY_COUNT = 12
EVERY_QUERY_USES_ONLY_ALLOWED_DESIGN_VOCABULARY = YES
SCIENTIFIC_DOMAIN_TERMS = 0
INSTITUTION_NAMES = 0
KNOWN_TARGET_IDS_OR_NAMES = 0
DEPENDENCE_OR_MODEL_TERMS = 0
PGH_TERMS = 0
```

No query may be edited, reordered, supplemented, shortened or substituted during execution.

## 5. Frozen primary-search budget

```text
PRIMARY_QUERY_ORDER = Q01_THROUGH_Q12
ONE_PRIMARY_QUERY_PER_TOOL_CALL = REQUIRED
MAX_RESULTS_INSPECTED_PER_PRIMARY_QUERY = 10
MAX_DISTINCT_SPECIFIC_CANDIDATES_ENTERED_PER_PRIMARY_QUERY = 3
MAX_TOTAL_DISTINCT_SPECIFIC_CANDIDATES_ADJUDICATED = 36
FULL_QUERY_MATRIX_CLOSURE_RULE = ALL_12_PRIMARY_QUERIES_MUST_CLOSE
EARLY_STOP_IF_ELIGIBLE_TARGET_FOUND = NO
```

For each query, inspect returned results in returned order until the first of:

1. ten results have been inspected;
2. three distinct specific candidate identities have been entered; or
3. the returned result set is exhausted.

A duplicate does not consume another distinct-candidate slot. A reencountered prior target does consume a distinct-candidate slot for that query because skipping it to search deeper would introduce asymmetric post hoc coverage.

All twelve primary queries execute even if one or more eligible targets are encountered early.

## 6. Candidate-entry rule

A returned item may enter candidate adjudication only if it identifies a specific dataset/interface/release family plausibly containing repeated physical, natural, instrumental or experimental records.

Generic portals, generic documentation pages, journal articles without a specific dataset identity, software packages, administrative-only tables and generic schema standards are not candidate interfaces.

Entry is permissive relative to final eligibility: uncertainty at first encounter is resolved by authoritative metadata rather than by skipping a potentially eligible candidate.

```text
CANDIDATE_ENTRY_USES_RESPONSE_BEHAVIOR = NO
CANDIDATE_ENTRY_USES_EXPECTED_PGH_RESULT = NO
```

## 7. Candidate encounter order and IDs

Encounter ordering is frozen as:

```text
PRIMARY_QUERY_ORDER
  -> RETURNED_RESULT_ORDER
  -> FIRST_DISTINCT_SPECIFIC_CANDIDATE_ENCOUNTER
```

Prior provenance remains binding:

```text
TGT_001_039 = PRIOR_ENCOUNTERS
NEXT_GENUINELY_NEW_TARGET_ID = TGT_040
```

A candidate matching the same underlying release/interface opportunity as TGT-001..TGT-039 retains the prior TGT ID and is recorded as a reencounter. It receives no new ID and cannot become a new first-positive-credit target merely through a new access path.

A genuinely distinct post-freeze candidate receives the next unused ID beginning at TGT-040 in first-encounter order.

## 8. Duplicate-identity rule

During primary accounting, obvious duplicate access paths to the same authority/dataset are provisionally collapsed.

After authoritative metadata resolves identity, two entries are the same candidate when they resolve to the same underlying authority-bound dataset/interface release, even if reached through different URLs, mirrors or documentation pages.

Canonical identity fields are:

```text
CANONICAL_AUTHORITY_NAME
STABLE_DATASET_IDENTIFIER
VERSION_OR_RELEASE_IDENTIFIER
```

If release identity is not yet resolved, deduplication remains provisional until the single allowed follow-up metadata query closes.

## 9. Frozen follow-up metadata budget

At most one follow-up metadata search is allowed per already-entered candidate, and only when at least one mandatory eligibility field remains unresolved after the primary result and directly linked authoritative pages are inspected.

```text
MAX_FOLLOWUP_METADATA_QUERIES_PER_CANDIDATE = 1
MAX_RESULTS_INSPECTED_PER_FOLLOWUP_QUERY = 10
FOLLOWUP_QUERY_ONLY_FOR_ALREADY_ENTERED_CANDIDATE = YES
SECOND_FOLLOWUP_QUERY = FORBIDDEN
```

Exact follow-up template:

```text
<CANDIDATE_EXACT_IDENTITY> schema data dictionary fields columns version release missing invalid API download format
```

The candidate exact identity is the only variable portion.

The template may not be altered based on which gate is missing. If mandatory metadata remain unresolved after this one follow-up, the unresolved gate remains `NOT_ESTABLISHED` and the candidate cannot qualify.

No dependence/model term may enter a follow-up query.

## 10. Eligibility and authority rule

The later execution must preserve the existing PGH-OBJ-0052 / OP-0108 operational eligibility burden without relaxation, including:

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

No gate may be weakened because the broader search remains sparse.

The native-binary rule remains exact: no analyst thresholding, binning, state merging, learned classification or response-derived dichotomization.

## 11. Search-return accounting

For every inspected primary and follow-up result, the execution ledger must record at least:

```text
QUERY_ID
QUERY_STRING
RETURNED_RANK
RESULT_TITLE
RESULT_LOCATOR
RESULT_HOST_OR_AUTHORITY_IF_VISIBLE
DISPOSITION
CANDIDATE_ID_IF_ANY
CONTROLLING_AUTHORITY_LOCATOR_IF_ANY
```

For every entered candidate, record:

```text
E1_E12_STATUS
NATIVE_BINARY_FIELD_COUNT_ESTABLISHED_FROM_AUTHORITY_METADATA
JOINT_INDEXABILITY_STATUS
MISSINGNESS_VALIDITY_STATUS
CONTAMINATION_CLASS
FOLLOWUP_QUERY_USED_OR_NOT
REJECTION_GATE_IF_ANY
```

No candidate can disappear from the ledger after entry.

## 12. Final set closure and target selection

After Q01-Q12 and all permitted candidate follow-ups close:

```text
CANDIDATE_SET = CLOSED_FOR_THIS_EXECUTION
```

Then:

1. exclude rejected, unresolved mandatory-gate, contaminated C2/C3 and prior-quarantined candidates;
2. enumerate every remaining genuinely new eligible candidate;
3. compute the unchanged lexical metadata tuple;
4. choose exactly the lexicographically smallest tuple.

If no candidate remains eligible, the execution must record a no-target outcome. It may not widen the matrix inside the same operation.

## 13. Counterfactual-choice audit

The frozen D-A matrix would be the same whether the later search returns:

```text
ZERO_ELIGIBLE_TARGETS
ONE_ELIGIBLE_TARGET
MANY_ELIGIBLE_TARGETS
A_TARGET_LIKELY_TO_REFUTE_PGH
A_TARGET_LIKELY_TO_SURVIVE_PGH
```

No response information is available during discovery, and final selection is administrative rather than scientific.

This satisfies the prospective counterfactual-choice requirement.

## 14. Relation to prior suspension and trigger reassessment

Historical results remain preserved:

```text
PGH_OP_0110_FINITE_D1_D5_NO_TARGET = PRESERVED
PGH_OP_0112_NO_TARGET_SUSPENSION = HISTORICAL_RESULT_PRESERVED
PGH_OP_0115_CLOSED_RECORD_TRIGGER_REASSESSMENT = HISTORICALLY_VALID
PGH_OP_0112_INDEPENDENT_ORIGIN_ONLY_RULE = SUPERSEDED_BY_LATER_ADVERSARIAL_AUDIT
```

The present gate does not reinterpret the old D1-D5 search as defective. It defines a new, prospectively frozen coverage architecture after the methodological audit established that response-blind coverage expansion is scientifically permissible.

## 15. Next operation boundary

A separate operation may now be preregistered to execute exactly the frozen Q01-Q12 matrix.

That later operation must:

```text
USE_EXACT_Q01_Q12 = YES
USE_EXACT_BUDGETS = YES
USE_EXACT_FOLLOWUP_TEMPLATE = YES
PRESERVE_TGT_001_039_QUARANTINE = YES
BEGIN_NEW_IDS_AT_TGT_040 = YES
ACCESS_RESPONSE_VALUES = NO
RUN_DEPENDENCE_ANALYSIS = NO
RUN_T_IND_TEST = NO
STOP_AFTER_TARGET_FREEZE_OR_NO_TARGET_RESULT = YES
```

The execution operation may discover and freeze one target identity if the frozen rules yield one. It still may not materialize response data or perform empirical analysis.

## 16. Claim ceiling

```text
SEARCH_ARCHITECTURE_QUALIFIED = YES
TARGET_SEARCH_EXECUTED = NO
TARGET_SELECTED = NO
TARGET_VALUES_ACCESSED = NO
PGH_OBJ_0052_TESTED = NO
PGH_OBJ_0052_VALIDATED = NO
PGH_OBJ_0052_REFUTED = NO
POSITIVE_EMPIRICAL_PGH_CREDIT = NONE
STRONG_PGH_CONFIRMED = NO
R2B = UNSATISFIED
```

## 17. Qualification

```text
PREREGISTRATION_FROZEN_BEFORE_ADJUDICATION = YES
CLOSED_RECORD_DESIGN_ONLY = YES
D_A_D_B_D_C_ALL_ADJUDICATED = YES
M1_M12_REPORTED = YES
D_A_M1_M10_ALL_PASS = YES
D_A_M11 = PARTIAL_NONDISCRETIONARY
D_A_M12 = PASS_AT_ARCHITECTURE_SCOPE
EXACT_QUERY_MATRIX_FROZEN = YES
EXACT_BUDGETS_FROZEN = YES
EXACT_FOLLOWUP_RULE_FROZEN = YES
NEW_TARGET_SEARCH = NO
NEW_DATASET_INSPECTION = NO
RESPONSE_DATA_ACCESS = NO
DEPENDENCE_INFORMATION_ACCESS = NO
CANDIDATE_IDENTITY_CHANGED = NO
EXACTLY_ONE_OUTCOME = YES
QUALIFICATION = PASS
```

Truth over PGH now requires executing the frozen broader search exactly as designed, accepting either another null discovery or a genuinely prospective target without adapting the method to either result.
