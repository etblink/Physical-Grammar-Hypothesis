# PGH-1 Response-Blind Target-Discovery Coverage Expansion — Repair Ledger 0.1.0

## Identity

```text
OPERATION_ID = PGH1_RESPONSE_BLIND_TARGET_DISCOVERY_COVERAGE_EXPANSION_TRANSPORT_REPAIR_AND_REEXECUTION
PREREGISTRATION_COMMIT = 0de151533006459fccc37ac521af859e64f760b8
CANONICAL_BASE = 6f6df66ef57528f3727e60dc35e058d0e210e5aa
CANDIDATE_PACKAGE = PGH-OBJ-0052
SCIENTIFIC_SELECTION_RULE_CHANGE = NONE
TRANSPORT_REPAIR = PASS
OUTCOME = D__REPAIR_PASSES__MANDATORY_METADATA_REMAINS_INSUFFICIENT_TO_FREEZE_A_REPRODUCIBLE_TARGET
TARGET_SELECTED = NO
TARGET_VALUES_ACCESSED = NO
RAW_DATA_MATERIALIZED = NO
DEPENDENCE_ANALYSIS_RUN = NO
T_IND_COMPATIBILITY_CHECK_RUN = NO
CANDIDATE_IDENTITY_CHANGED = NO
```

## 1. Repair result

The repair corrected the sole defect of the failed coverage-expansion execution: durable query/return provenance.

Every frozen Q01-Q12 primary query was reissued exactly, in order, with no query modification. After each return, an immutable Git trace recording the inspected rank/title/locator stream was committed **before** the next primary query ran.

Only after Q12 was committed did Phase B begin. Every candidate-specific follow-up that was scientifically required under the frozen metadata-resolution rule was issued exactly once in candidate order, and each return was committed before the next follow-up.

```text
PRIMARY_QUERY_TRACE_COUNT = 12
FOLLOWUP_QUERY_TRACE_COUNT = 6
TOTAL_TRACE_FILE_COUNT = 18
PRIMARY_RESULTS_INSPECTED = 114
FOLLOWUP_RESULTS_INSPECTED = 50
TOTAL_SEARCH_RESULTS_ACCOUNTED = 164
PRIMARY_TRACE_PROVENANCE_COMPLETE = YES
FOLLOWUP_TRACE_PROVENANCE_COMPLETE = YES
REPAIR_TRANSPORT_FAILURE = NO
```

The repaired search encountered no genuinely new target identity beyond the seven candidates already preserved by the failed execution.

```text
TGT_040_046 = REENCOUNTERED_OR_RETAINED_PROVENANCE
TGT_047_PLUS = NONE
```

## 2. Primary query trace chain

The immutable Phase-A trace files are:

```text
Q01 empirical/trace/PGH1_RESPONSE_BLIND_COVERAGE_REPAIR_Q01_0_1_0.md
Q02 empirical/trace/PGH1_RESPONSE_BLIND_COVERAGE_REPAIR_Q02_0_1_0.md
Q03 empirical/trace/PGH1_RESPONSE_BLIND_COVERAGE_REPAIR_Q03_0_1_0.md
Q04 empirical/trace/PGH1_RESPONSE_BLIND_COVERAGE_REPAIR_Q04_0_1_0.md
Q05 empirical/trace/PGH1_RESPONSE_BLIND_COVERAGE_REPAIR_Q05_0_1_0.md
Q06 empirical/trace/PGH1_RESPONSE_BLIND_COVERAGE_REPAIR_Q06_0_1_0.md
Q07 empirical/trace/PGH1_RESPONSE_BLIND_COVERAGE_REPAIR_Q07_0_1_0.md
Q08 empirical/trace/PGH1_RESPONSE_BLIND_COVERAGE_REPAIR_Q08_0_1_0.md
Q09 empirical/trace/PGH1_RESPONSE_BLIND_COVERAGE_REPAIR_Q09_0_1_0.md
Q10 empirical/trace/PGH1_RESPONSE_BLIND_COVERAGE_REPAIR_Q10_0_1_0.md
Q11 empirical/trace/PGH1_RESPONSE_BLIND_COVERAGE_REPAIR_Q11_0_1_0.md
Q12 empirical/trace/PGH1_RESPONSE_BLIND_COVERAGE_REPAIR_Q12_0_1_0.md
```

Primary execution respected every frozen stopping rule:

```text
Q01_RESULTS_INSPECTED = 10
Q02_RESULTS_INSPECTED = 10
Q03_RESULTS_INSPECTED = 10
Q04_RESULTS_INSPECTED = 10
Q05_RESULTS_INSPECTED = 10
Q06_RESULTS_INSPECTED = 10
Q07_RESULTS_INSPECTED = 10
Q08_RESULTS_INSPECTED = 8__CLOSED_AT_THIRD_DISTINCT_CANDIDATE
Q09_RESULTS_INSPECTED = 10
Q10_RESULTS_INSPECTED = 6__CLOSED_AT_THIRD_DISTINCT_CANDIDATE
Q11_RESULTS_INSPECTED = 10
Q12_RESULTS_INSPECTED = 10
FULL_Q01_Q12_MATRIX_CLOSED = YES
EARLY_STOP_FOR_TARGET_YIELD = NO
```

## 3. Repair candidate encounter set

The repaired primary traces reencountered exactly the already-preserved candidate identities:

| Candidate | Repair encounter | Status after repair |
|---|---|---|
| `TGT-040` RIPA Stop Data | Q02 rank 7 | ineligible; persistent E12 contamination |
| `TGT-041` NEMSIS Version 3.5.1 National EMS / EMS event interface | Q02 rank 10; Q08 rank 8 | ineligible; E2 not established at event-record scope |
| `TGT-042` Crowd Counting Consortium event data | Q08 rank 5 | ineligible; E4 and E9 not established at exact target-release scope |
| `TGT-043` US EPA NHD Event Data | Q08 rank 6 | ineligible; E5 fails |
| `TGT-044` NCEP observational database / PREPBUFR interface | Q10 rank 3 | ineligible; E4/E5/E6 not established at one target-release scope |
| `TGT-045` Wyoming Natural Diversity Database observations | Q10 rank 4 | ineligible; no single interface jointly passes E2 and E5 |
| `TGT-046` MODIS Terra/Aqua/Combined EarthExplorer product/interface | Q10 rank 6 | ineligible; E5 fails |

No candidate identity was invented from a generic schema/standard result merely to increase search yield.

## 4. Phase-B trace chain

`TGT-040` received no repair follow-up because its persistent C2/C3-class candidate-specific contamination already fails mandatory E12. Searching it more deeply would add asymmetric search effort after a decisive failure.

The remaining six candidates each received exactly one frozen-template follow-up in encounter order:

```text
TGT-041 empirical/trace/PGH1_RESPONSE_BLIND_COVERAGE_REPAIR_TGT-041_FOLLOWUP_0_1_0.md
TGT-042 empirical/trace/PGH1_RESPONSE_BLIND_COVERAGE_REPAIR_TGT-042_FOLLOWUP_0_1_0.md
TGT-043 empirical/trace/PGH1_RESPONSE_BLIND_COVERAGE_REPAIR_TGT-043_FOLLOWUP_0_1_0.md
TGT-044 empirical/trace/PGH1_RESPONSE_BLIND_COVERAGE_REPAIR_TGT-044_FOLLOWUP_0_1_0.md
TGT-045 empirical/trace/PGH1_RESPONSE_BLIND_COVERAGE_REPAIR_TGT-045_FOLLOWUP_0_1_0.md
TGT-046 empirical/trace/PGH1_RESPONSE_BLIND_COVERAGE_REPAIR_TGT-046_FOLLOWUP_0_1_0.md
```

```text
TGT041_RESULTS_INSPECTED = 10
TGT042_RESULTS_INSPECTED = 9__RETURN_SET_EXHAUSTED
TGT043_RESULTS_INSPECTED = 8__RETURN_SET_EXHAUSTED
TGT044_RESULTS_INSPECTED = 10
TGT045_RESULTS_INSPECTED = 7__RETURN_SET_EXHAUSTED
TGT046_RESULTS_INSPECTED = 6__RETURN_SET_EXHAUSTED
SECOND_FOLLOWUP_QUERY_USED = NO
```

## 5. TGT-040 — RIPA Stop Data

The failed execution already encountered candidate-specific empirical association/outcome material on the RIPA schema/exploration surface. The repair preregistration made that contamination persistent rather than erasable by reexecution.

```text
E5_AT_LEAST_THREE_NATIVE_BINARY_FIELDS = PASS_AT_METADATA_SCOPE
E6_JOINT_INDEXABILITY = PASS_AT_METADATA_SCOPE
E12_NO_DEPENDENCE_CONTAMINATION = FAIL_BY_PERSISTENT_PRIOR_ENCOUNTER
CONTAMINATION_CLASS = C2_OR_C3
FOLLOWUP_USED_IN_REPAIR = NO
FINAL_DISPOSITION = INELIGIBLE_FOR_FIRST_POSITIVE_CREDIT
```

No claim is made that the observed RIPA associations support or refute PGH; contamination only makes this interface unusable for first prospective credit.

## 6. TGT-041 — NEMSIS Version 3.5.1 National EMS / EMS event interface

Authoritative NEMSIS metadata establish a mature EMS/PCR event schema, stable v3.5.1 resources, documented nil/not-value semantics, and many exact two-state yes/no elements.

Examples of authority-defined native binary fields include multiple Yes/No event elements covering incident, mechanism, safety, intervention and procedure properties.

The frozen follow-up did **not** establish public or independently auditable event-level National EMS records at the target scope. Public standard schemas, XSDs and API definitions do not by themselves satisfy E2.

```text
E1 = PASS_AT_SCHEMA/PHYSICAL_RECORD_SCOPE
E2 = NOT_ESTABLISHED_AT_EVENT_RECORD_SCOPE
E3 = PASS_AT_STANDARD_SCOPE
E4 = PASS_AT_STANDARD_SCOPE
E5 = PASS
E6 = PASS_AT_EVENT_SCHEMA_SCOPE
E7 = PASS_IN_PRINCIPLE
E8 = PASS_IN_PRINCIPLE
E9 = PASS_AT_SCHEMA_SCOPE
E10 = PASS_IN_PRINCIPLE
E11 = PASS
E12 = PASS_AT_REPAIR_SCOPE
FINAL_DISPOSITION = INELIGIBLE__E2_NOT_ESTABLISHED
```

## 7. TGT-042 — Crowd Counting Consortium event data

The project-maintained data dictionary establishes repeated protest-event rows and several exact 0/1 fields, including `Online`, `ReportedPropertyDamage`, `TownsCities`, `Events`, and `Final`.

Harvard's authoritative Ash Center page establishes that CCC event data are publicly published through Harvard Dataverse. The authority-linked Dataverse collection was reached. A phase-specific persistent dataset route was also reached, but the available authority surface exposed only a JavaScript/robot-verification shell, so the operation could not bind an exact immutable dataset version/release or complete null/invalid semantics from controlling metadata.

A secondary repository exposed phase DOIs, but the authority firewall forbids substituting that secondary assertion for the missing controlling release facts.

```text
E1 = PASS
E2 = PASS
E3 = PASS_AT_PROJECT_DATASET_FAMILY_SCOPE
E4 = NOT_ESTABLISHED_AT_EXACT_IMMUTABLE_TARGET_RELEASE_SCOPE
E5 = PASS
E6 = PASS
E7 = PASS
E8 = PASS
E9 = NOT_ESTABLISHED
E10 = PASS_IN_PRINCIPLE_FOR_COMPILED_CSV
E11 = PASS
E12 = PASS__NO_T_IND_OR_EQUIVALENT_COMPATIBILITY_RESULT_ENCOUNTERED
FINAL_DISPOSITION = INELIGIBLE__E4_E9_NOT_ESTABLISHED
```

## 8. TGT-043 — US EPA NHD Event Data

The authoritative EPA NHD Event Data Dictionary establishes a physical hydrologic-event record interface with stable identifiers, dates, geometry and related attributes.

It does not establish at least three jointly recorded native binary fields. The schema-level `NULL?` column is dictionary metadata, not an event-record variable. A related RAD interface exposes a Y/N `Navigable` field, still below the required count of three.

```text
E1 = PASS
E2 = PASS_IN_PRINCIPLE
E3 = PASS
E4 = PARTIAL_OR_PASS_AT_COMPONENT_VERSION_SCOPE
E5 = FAIL
E6_E10 = MOOT_AFTER_DECISIVE_E5_FAIL
E11 = PASS
E12 = PASS
FINAL_DISPOSITION = INELIGIBLE__E5_FAIL
```

## 9. TGT-044 — NCEP observational database / PREPBUFR interface

NCEP authority pages establish BUFR/PREPBUFR observational architecture, self-defining PREPBUFR files, descriptor tables, and current/historical WMO/NCEP table versions.

The single frozen follow-up does not bind one immutable PREPBUFR target release together with three exact native-binary fields that are jointly recorded on the same report/event index. General code/flag descriptor infrastructure is not enough to satisfy E5/E6 for a frozen target.

```text
E1 = PASS
E2 = NOT_ESTABLISHED_FROM_CONTROLLING_NCEP_TARGET_RELEASE_METADATA
E3 = PASS_AT_INTERFACE_FAMILY_SCOPE
E4 = NOT_ESTABLISHED_AT_SINGLE_IMMUTABLE_TARGET_RELEASE_SCOPE
E5 = NOT_ESTABLISHED_FOR_ONE_FROZEN_TARGET_RELEASE
E6 = NOT_ESTABLISHED_FOR_THREE_EXACT_NATIVE_BINARY_FIELDS
E7_E10 = NOT_REACHED_AS_FULL_PASS
E11 = PASS
E12 = PASS
FINAL_DISPOSITION = INELIGIBLE__E4_E5_E6_NOT_ESTABLISHED
```

## 10. TGT-045 — Wyoming Natural Diversity Database observations

WYNDD authority pages distinguish precise observations from generalized public observations.

Precise records carry rich biological observation attributes but require registered Data Explorer access and/or request-based delivery at the relevant detailed scope. The generalized public service is more openly accessible but its data dictionary exposes counts, names, years and geometry rather than three native binary fields.

The eligibility gates must be passed by one interface; access from one product cannot be combined with richer fields from another.

```text
PRECISE_E1 = PASS
PRECISE_E2 = FAIL_AT_UNRESTRICTED_PUBLIC_SCOPE
PRECISE_E5 = NOT_ESTABLISHED
GENERALIZED_E2 = PASS_IN_PRINCIPLE
GENERALIZED_E5 = FAIL
FINAL_DISPOSITION = INELIGIBLE__NO_SINGLE_INTERFACE_PASSES_E2_AND_E5
```

## 11. TGT-046 — MODIS Terra/Aqua/Combined EarthExplorer product/interface

The authoritative USGS MODIS EarthExplorer dictionary establishes stable product/granule identifiers, DOI/version metadata and quality fields.

Only one encountered field is native binary under the frozen rule:

```text
Auto Quality Flag = Passed | Failed
```

`Day or Night Indicator` has four substantive states (`Day`, `Night`, `Both`, `All`) and `Science Quality Flag` has eight. No binning, merging or analyst dichotomization is allowed.

```text
E1 = PASS_AT_GRANULE_METADATA_SCOPE
E2 = PASS_IN_PRINCIPLE
E3 = PASS
E4 = PASS_IN_PRINCIPLE
E5 = FAIL
E6_E10 = MOOT_AFTER_DECISIVE_E5_FAIL
E11 = PASS
E12 = PASS
FINAL_DISPOSITION = INELIGIBLE__E5_FAIL
```

## 12. Final eligible-set closure

After all primary traces and every permitted follow-up closed:

```text
REPAIR_CANDIDATE_SET = CLOSED
CANDIDATE_COUNT = 7
FULLY_ELIGIBLE_NONCONTAMINATED_NEW_TARGET_COUNT = 0
TARGET_TUPLE_COMPUTATION_REQUIRED = NO
TARGET_SELECTED = NO
```

The seven candidates separate into three classes:

```text
DEFINITIVE_MANDATORY_FAIL:
  TGT-040 E12
  TGT-043 E5
  TGT-045 E2/E5 across non-combinable interfaces
  TGT-046 E5

MANDATORY_METADATA_NOT_ESTABLISHED_AFTER_FROZEN_FOLLOWUP:
  TGT-041 E2
  TGT-042 E4/E9
  TGT-044 E4/E5/E6

FULLY_ELIGIBLE = NONE
```

## 13. Outcome derivation

Preregistered outcomes were:

```text
A = REPAIR_PASSES__ONE_NEW_TARGET_QUALIFIES_AND_IS_FROZEN
B = REPAIR_PASSES__NO_DISCOVERED_NEW_TARGET_PASSES_ALL_MANDATORY_GATES
C = REPAIR_PASSES__OTHERWISE_ELIGIBLE_NEW_TARGETS_EXIST_BUT_ALL_ARE_C2_OR_C3_CONTAMINATED_OR_PRIOR_QUARANTINED
D = REPAIR_PASSES__MANDATORY_METADATA_REMAINS_INSUFFICIENT_TO_FREEZE_A_REPRODUCIBLE_TARGET
E = REPAIR_ITSELF_FAILS__QUERY_OR_RETURN_PROVENANCE_STILL_NOT_AUDITABLE
```

```text
A = NO
C = NO
E = NO
```

B is descriptively true in the broad sense that no candidate passes all gates, but D is the more specific controlling preregistered outcome because the closed candidate set contains multiple non-definitively-rejected interfaces whose mandatory metadata remain unresolved after their sole permitted follow-up. The repair therefore may not convert their unresolved gates into failures merely to claim a simple no-target screen.

```text
CONTROLLING_OUTCOME = D__REPAIR_PASSES__MANDATORY_METADATA_REMAINS_INSUFFICIENT_TO_FREEZE_A_REPRODUCIBLE_TARGET
```

## 14. Response/dependence firewall audit

```text
TARGET_RESPONSE_ROWS_ACCESSED = NO
RAW_DATA_MATERIALIZED = NO
JOINT_COUNTS_COMPUTED = NO
MARGINAL_COUNTS_COMPUTED = NO
CORRELATION_SEARCH_USED = NO
INDEPENDENCE_SEARCH_USED = NO
T_IND_SEARCH_USED = NO
T_IND_MEMBERSHIP_TESTED = NO
CANDIDATE_STATISTIC_DESIGNED = NO
G_CHANGED = NO
J_CHANGED = NO
S_CHANGED = NO
I_CHANGED = NO
```

The only candidate-specific empirical-statistics exposure inherited from the failed execution is the already-recorded RIPA contamination. It is used only to disqualify TGT-040 from first prospective credit, not to infer PGH truth.

## 15. Scientific consequence

```text
PGH_OBJ_0052_EMPIRICAL_STATUS = UNTESTED
TARGET_SELECTED = NO
EMPIRICAL_TEST = UNINSTANTIATED
POSITIVE_EMPIRICAL_PGH_CREDIT = NONE
EMPIRICAL_REFUTATION_OF_PGH_OBJ_0052 = NONE
STRONG_PGH_CONFIRMED = NO
R2B = UNSATISFIED
```

The repaired expanded search has now been executed with an audit-complete transport. It still does not produce a prospectively admissible target.

That fact is about current target instantiation under the exact frozen interface and search rules. It is not evidence that the universal PGH postulate is true.

## 16. Qualification

```text
PREREGISTRATION_FROZEN_BEFORE_REEXECUTION = YES
SCIENTIFIC_SEARCH_RULE_CHANGED = NO
Q01_Q12_EXACT = YES
Q01_Q12_ORDER_PRESERVED = YES
PRIMARY_BUDGETS_PRESERVED = YES
TWELVE_PRIMARY_TRACES_COMMITTED_BEFORE_ADVANCE = YES
NO_FOLLOWUP_BEFORE_Q12_TRACE = YES
FOLLOWUP_TEMPLATE_PRESERVED = YES
FOLLOWUP_LIMIT_PRESERVED = YES
SIX_FOLLOWUP_TRACES_COMMITTED_BEFORE_ADVANCE = YES
TGT_040_046_PROVENANCE_PRESERVED = YES
NEW_TGT_047_PLUS = NONE
E1_E12_PRESERVED = YES
CONTAMINATION_FIREWALL_PRESERVED = YES
TARGET_TIE_BREAK_PRESERVED = YES
TARGET_VALUES_ACCESSED = NO
REPAIR_PROVENANCE_COMPLETE = YES
EXACTLY_ONE_OUTCOME = YES
QUALIFICATION = PASS
```

Truth over PGH means the repaired search is allowed to end without a target even after substantial effort to improve falsification opportunity. Lack of an admissible target is still zero positive evidence for the hypothesis.
