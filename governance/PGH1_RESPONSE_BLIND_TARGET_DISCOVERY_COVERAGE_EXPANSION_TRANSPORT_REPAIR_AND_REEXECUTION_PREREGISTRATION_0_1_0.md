# PGH-1 Response-Blind Target-Discovery Coverage Expansion — Transport Repair and Reexecution Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_RESPONSE_BLIND_TARGET_DISCOVERY_COVERAGE_EXPANSION_TRANSPORT_REPAIR_AND_REEXECUTION
OPERATION_CLASS = TRANSPORT_PROVENANCE_REPAIR_AND_METADATA_ONLY_REEXECUTION
CANONICAL_BASE = 6f6df66ef57528f3727e60dc35e058d0e210e5aa
CANONICAL_BASE_TREE = fa045b6ab431ca9e31a7f57826ce38c32ee867ed
CANDIDATE_PACKAGE = PGH-OBJ-0052
FAILED_EXECUTION_PREREGISTRATION_BLOB = 921c118b6c4858219797370edc17c57b7db2d06c
FAILED_EXECUTION_LEDGER_BLOB = 169b579820fac60a608a804c24290f52e4b3b097
FAILED_EXECUTION_TARGET_FREEZE_BLOB = c3b85d0825ac0c2f86ff2a8abbf321bf9d4af3ee
FAILED_EXECUTION_HANDOFF_BLOB = 613bfd7da260fc51a445a0d3614bee37f5b95502
DESIGN_PREREGISTRATION_BLOB = 68c088e4b314a0b7d6b3451d96f2ce37de8833e0
DESIGN_ADJUDICATION_BLOB = d8e69f8987dbad6d18c0f1fde6f2c3e37f98423a
DESIGN_HANDOFF_BLOB = 1277fdff89f90853796338c2c07e479a2193444b
SCIENTIFIC_SELECTION_RULE_CHANGE = NONE
TARGET_VALUES = FORBIDDEN
RAW_DATA_MATERIALIZATION = FORBIDDEN
DEPENDENCE_ANALYSIS = FORBIDDEN
T_IND_COMPATIBILITY_CHECK = FORBIDDEN
CANDIDATE_REVISION = FORBIDDEN
```

## 1. Purpose

Repair only the execution-record provenance failure that forced the prior response-blind coverage expansion to Outcome D.

The failed execution reached Q12 and preserved candidate identities, but not every exact primary-search result locator required by its preregistration. This repair therefore reissues the **same exact Q01-Q12 queries under the same scientific rules** while changing only the transport/capture mechanism.

The scientific design is not reopened.

## 2. Fully inherited scientific rules

The following are unchanged and incorporated from the failed execution and its canonical design gate:

```text
CANDIDATE_PACKAGE = PGH-OBJ-0052
QUERY_MATRIX = Q01_THROUGH_Q12_UNCHANGED
QUERY_ORDER = Q01_THROUGH_Q12_UNCHANGED
MAX_RESULTS_INSPECTED_PER_PRIMARY_QUERY = 10
MAX_DISTINCT_SPECIFIC_CANDIDATES_ENTERED_PER_PRIMARY_QUERY = 3
MAX_TOTAL_DISTINCT_SPECIFIC_CANDIDATES_ADJUDICATED = 36
FULL_QUERY_MATRIX_CLOSURE = REQUIRED
EARLY_STOP_AFTER_ELIGIBLE_TARGET = FORBIDDEN
TWO_PHASE_PRIMARY_THEN_FOLLOWUP_ORDER = UNCHANGED
FOLLOWUP_TEMPLATE = UNCHANGED
MAX_FOLLOWUP_METADATA_QUERIES_PER_CANDIDATE = 1
MAX_RESULTS_INSPECTED_PER_FOLLOWUP_QUERY = 10
E1_E12 = UNCHANGED
NATIVE_BINARY_RULE = UNCHANGED
FIELD_SELECTION = UNICODE_LEXICAL_FIRST_THREE_NATIVE_BINARY_FIELDS
ROLE_ASSIGNMENT = SAME_ORDER_TO_A_B_C
CONTAMINATION_CLASSES = UNCHANGED
TARGET_SELECTION = LEXICOGRAPHIC_AUTHORITY_DATASET_RELEASE_TUPLE
STOP_BOUNDARY = UNCHANGED
```

If this repair text conflicts with the canonical design or failed execution preregistration on a scientific matter, the earlier frozen scientific rule controls.

## 3. Exact primary queries

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
ONE_PRIMARY_QUERY_PER_SEARCH_CALL = REQUIRED
QUERY_EDITING = FORBIDDEN
QUERY_REORDERING = FORBIDDEN
QUERY_SUBSTITUTION = FORBIDDEN
EXTRA_PRIMARY_QUERY = FORBIDDEN
```

## 4. Repair transport change — durable per-call trace

The only methodological change is durable capture.

After **each** primary query returns and before the next primary query is issued, create one immutable trace file:

```text
empirical/trace/PGH1_RESPONSE_BLIND_COVERAGE_REPAIR_Q01_0_1_0.md
...
empirical/trace/PGH1_RESPONSE_BLIND_COVERAGE_REPAIR_Q12_0_1_0.md
```

Each primary trace must record every inspected result up to the frozen stopping rule with at least:

```text
QUERY_ID
EXACT_QUERY_STRING
SEARCH_EXECUTION_ORDER
RETURNED_RANK
RESULT_TITLE
RESULT_LOCATOR
RESULT_HOST_IF_VISIBLE
DISPOSITION
CANDIDATE_ID_IF_ANY
```

The trace file must be committed to the repair branch before the next query is executed.

A search call whose returned rank/title/locator stream cannot be captured sufficiently to create that trace produces immediate repair failure; no substitute query is allowed.

## 5. Primary candidate encounter and identity rules

Existing provenance is binding:

```text
TGT_001_039 = PRE_REPAIR_PRIOR_TARGETS
TGT_040_046 = ENCOUNTERED_IN_FAILED_COVERAGE_EXECUTION
NEXT_GENUINELY_NEW_ID = TGT_047
```

If TGT-040..TGT-046 reappear, retain the same ID. They do not become newly discovered again.

A genuinely distinct candidate first encountered during repair receives the next unused ID beginning at TGT-047.

Candidate entry, duplicate handling, per-query candidate ceilings and returned-order processing remain exactly those of the failed execution.

## 6. Persistent knowledge firewall

The repair cannot erase information already encountered.

In particular:

```text
TGT_040_RIPA_CONTAMINATION = PERSISTENT
TGT_040_MAY_NOT_REGAIN_FIRST_POSITIVE_CREDIT_BY_REEXECUTION = YES
```

Other provisional TGT-041..TGT-046 gate findings may be re-adjudicated if the repair return and its one frozen follow-up resolve metadata differently, but they retain their provenance identities.

No prior candidate may be favored, skipped, searched more deeply, or searched less deeply because of its provisional disposition.

## 7. Phase A closure

Phase A consists only of Q01-Q12 primary searches and twelve committed primary trace files.

```text
NO_CANDIDATE_SPECIFIC_FOLLOWUP_BEFORE_Q12_TRACE_COMMIT = YES
```

After Q12 trace is committed, derive the complete ordered repair candidate set from the trace files. Do not use the failed execution's candidate list as a shortcut; reencountered identities retain their IDs, and new identities are assigned in repair encounter order.

## 8. Phase B follow-up transport

After Phase A closes, each repair-entered candidate with unresolved mandatory metadata may receive at most one follow-up query, in repair encounter order, using the same frozen template:

```text
<CANDIDATE_EXACT_IDENTITY> schema data dictionary fields columns version release missing invalid API download format
```

After each follow-up returns and before the next follow-up is issued, create and commit exactly one candidate trace file:

```text
empirical/trace/PGH1_RESPONSE_BLIND_COVERAGE_REPAIR_<TGT-ID>_FOLLOWUP_0_1_0.md
```

Each follow-up trace records the exact query and every inspected returned result up to rank 10, with title, locator, host, authority relevance and gate effect.

No second follow-up is permitted.

## 9. Authority and contamination rules

Unchanged:

- search snippets identify candidates but do not pass mandatory gates;
- controlling facts require authoritative institutional metadata or equivalent authority-bound stable documentation;
- C0/C1 may remain eligible;
- C2/C3 are ineligible for first positive credit;
- forbidden dependence/model search terms remain forbidden;
- no response values, counts, correlations, compatibility or T_ind behavior may be inspected intentionally.

## 10. Final repair outputs

After all required traces close, one final adjudication commit may create exactly:

```text
empirical/PGH1_RESPONSE_BLIND_TARGET_DISCOVERY_COVERAGE_EXPANSION_REPAIR_LEDGER_0_1_0.md
empirical/PGH1_RESPONSE_BLIND_TARGET_DISCOVERY_COVERAGE_EXPANSION_REPAIRED_TARGET_FREEZE_0_1_0.md
handoffs/PGH1_RESPONSE_BLIND_TARGET_DISCOVERY_COVERAGE_EXPANSION_TRANSPORT_REPAIR_HANDOFF_0_1_0.md
```

The trace directory remains part of the canonical candidate because it is the repaired audit evidence.

## 11. Commit topology

```text
COMMIT_1 = THIS_PREREGISTRATION_ONLY
COMMIT_2_THROUGH_COMMIT_13 = EXACTLY_ONE_IMMUTABLE_PRIMARY_TRACE_FOR_Q01_THROUGH_Q12
FOLLOWUP_TRACE_COMMITS = EXACTLY_ONE_PER_PERMITTED_REPAIR_CANDIDATE_FOLLOWUP_IN_ENCOUNTER_ORDER
FINAL_COMMIT = REPAIR_LEDGER_PLUS_REPAIRED_TARGET_FREEZE_PLUS_HANDOFF
```

No trace commit may modify a previous trace file. Trace files are append-only by filename and immutable after creation.

The variable number of follow-up commits is determined solely by the repair-entered candidate set and frozen metadata-resolution rule.

## 12. Outcome space

Exactly one:

```text
A = REPAIR_PASSES__ONE_NEW_TARGET_QUALIFIES_AND_IS_FROZEN
B = REPAIR_PASSES__NO_DISCOVERED_NEW_TARGET_PASSES_ALL_MANDATORY_GATES
C = REPAIR_PASSES__OTHERWISE_ELIGIBLE_NEW_TARGETS_EXIST_BUT_ALL_ARE_C2_OR_C3_CONTAMINATED_OR_PRIOR_QUARANTINED
D = REPAIR_PASSES__MANDATORY_METADATA_REMAINS_INSUFFICIENT_TO_FREEZE_A_REPRODUCIBLE_TARGET
E = REPAIR_ITSELF_FAILS__QUERY_OR_RETURN_PROVENANCE_STILL_NOT_AUDITABLE
```

No widening or redesign is permitted inside this repair.

## 13. Stop boundary

```text
STOP_AFTER_TARGET_IDENTITY_FIELDS_AND_ROLES_FREEZE_IF_ANY
STOP_AFTER_NO_TARGET_OR_TECHNICAL_REPAIR_RESULT_IF_NONE
STOP_BEFORE_TARGET_VALUES
STOP_BEFORE_RAW_DATA_MATERIALIZATION
STOP_BEFORE_TARGET_SPECIFIC_ANALYSIS
STOP_BEFORE_T_IND_MEMBERSHIP_TEST
STOP_BEFORE_CANDIDATE_VERDICT
```

## 14. Claim ceiling

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

The purpose of the extra trace commits is provenance durability, not scientific flexibility. Truth over PGH requires the transport layer to be at least as strict as the hypothesis test it is meant to enable.