# PGH-1 Response-Blind Target-Discovery Coverage Expansion Execution — Ledger 0.1.0

## Identity

```text
OPERATION_ID = PGH1_RESPONSE_BLIND_TARGET_DISCOVERY_COVERAGE_EXPANSION_EXECUTION
PREREGISTRATION_COMMIT = 4d9b18d30078164d8ca0a8703d44a05d8f538c38
CANDIDATE_PACKAGE = PGH-OBJ-0052
OUTCOME = D__EXECUTION_TECHNICALLY_FAILS__QUERY_OR_RETURN_PROVENANCE_NOT_AUDITABLE
TARGET_VALUES_ACCESSED = NO
RAW_DATA_MATERIALIZED = NO
DEPENDENCE_ANALYSIS_RUN = NO
T_IND_COMPATIBILITY_CHECK_RUN = NO
CANDIDATE_IDENTITY_CHANGED = NO
```

## 1. Controlling qualification failure

The exact Q01-Q12 primary searches were issued in the frozen order, and Phase B follow-up searches were issued for each entered candidate in encounter order. However, the durable successor execution record did not retain the exact `RESULT_LOCATOR` for every inspected Q01-Q10 primary-search result.

The preregistration required, for every inspected result:

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

Because that accounting cannot now be reconstructed without reissuing searches, this execution does not satisfy its own provenance gate.

```text
PHASE_A_Q01_Q12_ISSUED = YES
PHASE_B_TGT040_TGT046_FOLLOWUPS_ISSUED = YES
PER_RESULT_PRIMARY_LOCATOR_CAPTURE_COMPLETE = NO
SCIENTIFIC_NO_TARGET_OUTCOME_QUALIFIED = NO
TECHNICAL_FAILURE_OUTCOME = YES
```

The operation therefore freezes Outcome D even though the provisional candidate screen below contains no qualifying target.

## 2. Primary-search candidate encounter record

The surviving execution record establishes the following candidate-entry sequence. This sequence is preserved as provenance for repair.

| ID | First encounter | Candidate/interface | Provisional status |
|---|---|---|---|
| `TGT-040` | Q02 | RIPA Stop Data | entered |
| `TGT-041` | Q02 | NEMSIS Version 3.5.1 National EMS / EMS event interface | entered |
| `TGT-042` | Q08 | Crowd Counting Consortium event data | entered |
| `TGT-043` | Q08 | US EPA NHD Event Data | entered |
| `TGT-044` | Q10 | NCEP observational database / PREPBUFR interface | entered |
| `TGT-045` | Q10 | Wyoming Natural Diversity Database observations | entered |
| `TGT-046` | Q10 | MODIS Terra/Aqua/Combined EarthExplorer product/interface | entered |

Q01, Q03, Q04, Q05, Q06, Q07, Q09, Q11 and Q12 did not create a new candidate entry within their frozen budgets. Q10 closed at its three-candidate ceiling.

This summary does **not** substitute for the missing rank-by-rank locator ledger.

## 3. Provisional Phase-B candidate dispositions

These dispositions are retained only to preserve what was learned before the technical qualification failure was recognized. They are not promoted into a canonical Outcome-B no-target adjudication.

### TGT-040 — RIPA Stop Data

Provisional controlling metadata page:

```text
https://ripastops.org/articles/variables-and-schema
```

The encountered schema page establishes a large joint stop-record table and many 0/1 fields, but the same page also exposes candidate-specific empirical association/outcome statistics, including stop/search/force-rate comparisons across recorded attributes.

```text
E5_AT_LEAST_THREE_NATIVE_BINARY_FIELDS = PROVISIONALLY_PASS
E6_JOINT_INDEXABILITY = PROVISIONALLY_PASS
E12_NO_DEPENDENCE_CONTAMINATION = PROVISIONALLY_FAIL
CONTAMINATION_CLASS = C3_OR_AT_LEAST_C2
PROVISIONAL_DISPOSITION = INELIGIBLE_FOR_FIRST_POSITIVE_CREDIT
```

### TGT-041 — NEMSIS Version 3.5.1 National EMS / EMS event interface

Authoritative metadata retained:

```text
https://nemsis.org/technical-resources/version-3/version-3-data-dictionaries/
https://nemsis.org/media/nemsis_v3/release-3.5.1/DataDictionary/Ancillary/DEMEMS/Combined_ElementDetails_Full.txt
https://nemsis.org/media/nemsis_v3/release-3.5.1/DataDictionary/Ancillary/DEMEMS/Combined_ElementEnumerations.txt
```

The NEMSIS schema establishes repeated EMS event/PCR structure, documented nil/not-value handling, and multiple exact native yes/no fields. Examples include mass-casualty incident, ACN multiple impacts, high probability of injury, rollover, seatbelt use, airbag deployment, therapeutic hypothermia, medication administered by another unit, procedure performed prior to this unit, and procedure successful.

The single frozen follow-up did not establish public/auditable **event-level National EMS records** at the target scope; public schema/XSD/API-standard documentation alone is insufficient for E2.

```text
E3_STABLE_IDENTITY = PROVISIONALLY_PASS_AT_STANDARD_SCOPE
E5_AT_LEAST_THREE_NATIVE_BINARY_FIELDS = PROVISIONALLY_PASS
E6_JOINT_INDEXABILITY = PROVISIONALLY_PASS_AT_EVENT_SCHEMA_SCOPE
E9_DOCUMENTED_VALIDITY_OR_NULL_HANDLING = PROVISIONALLY_PASS
E2_PUBLIC_AUDITABLE_ACCESS = NOT_ESTABLISHED
PROVISIONAL_DISPOSITION = INELIGIBLE
```

### TGT-042 — Crowd Counting Consortium event data

Authoritative project page retained:

```text
https://ash.harvard.edu/programs/crowd-counting-consortium/
```

The encountered dictionary material exposed multiple 0/1 event fields such as `Online`, `ReportedPropertyDamage`, `TownsCities`, `Events`, and `Final`. The Harvard project page states that public data are published on Harvard Dataverse.

The frozen follow-up did not establish an exact immutable release/version identity from controlling authority metadata, and complete null/invalid handling was not established. The Dataverse interface encountered during adjudication was not retrievable in a way sufficient to close those gates.

```text
E5_AT_LEAST_THREE_NATIVE_BINARY_FIELDS = PROVISIONALLY_PASS
E6_JOINT_INDEXABILITY = PROVISIONALLY_PASS
E4_RELEASE_IDENTITY = NOT_ESTABLISHED
E9_DOCUMENTED_VALIDITY_OR_NULL_HANDLING = NOT_ESTABLISHED
PROVISIONAL_DISPOSITION = INELIGIBLE
```

### TGT-043 — US EPA NHD Event Data

The encountered authoritative NHD event-data dictionary described event identifiers, text/integer/date/geometry attributes and related metadata. It did not establish at least three jointly recorded native binary fields.

```text
E5_AT_LEAST_THREE_NATIVE_BINARY_FIELDS = PROVISIONALLY_FAIL
PROVISIONAL_DISPOSITION = INELIGIBLE
```

### TGT-044 — NCEP observational database / PREPBUFR interface

Authoritative metadata retained include NCEP BUFR tables and observational-processing documentation:

```text
https://www.emc.ncep.noaa.gov/emc/pages/infrastructure/bufrlib/tables/bufrtab_tableb.html
```

The material establishes an active BUFR/PREPBUFR observational architecture and current BUFR master-table versioning. It does not, within the one frozen follow-up, establish a single immutable target dataset/release plus at least three exact jointly recorded native-binary fields for that same target interface.

```text
E4_RELEASE_IDENTITY = NOT_ESTABLISHED_AT_TARGET_SCOPE
E5_AT_LEAST_THREE_NATIVE_BINARY_FIELDS = NOT_ESTABLISHED_AT_TARGET_SCOPE
E6_JOINT_INDEXABILITY = NOT_ESTABLISHED_AT_TARGET_SCOPE
PROVISIONAL_DISPOSITION = INELIGIBLE
```

### TGT-045 — Wyoming Natural Diversity Database observations

Authoritative observation dictionary retained:

```text
https://www.uwyo.edu/wyndd/find-data-info/about-our-data-information/codes-and-definitions/observation-data-dictionary.html
```

The precise observation interface is not established as unrestricted public/auditable event-level access at the required scope. The encountered public generalized observation layer does not expose at least three native binary fields.

```text
PRECISE_INTERFACE__E2_PUBLIC_AUDITABLE_ACCESS = PROVISIONALLY_FAIL
GENERALIZED_PUBLIC_INTERFACE__E5_AT_LEAST_THREE_NATIVE_BINARY_FIELDS = PROVISIONALLY_FAIL
PROVISIONAL_DISPOSITION = INELIGIBLE
```

### TGT-046 — MODIS Terra/Aqua/Combined EarthExplorer product/interface

Authoritative USGS metadata retained:

```text
https://www.usgs.gov/centers/eros/science/modis-terra-aqua-combined-data-dictionary
```

The encountered EarthExplorer MODIS dictionary establishes stable product/granule metadata and one clear native binary field, `Auto Quality Flag = Passed/Failed`. Other encountered categorical fields such as Day/Night Indicator and Science Quality Flag are not native binary under the frozen rule.

```text
E5_AT_LEAST_THREE_NATIVE_BINARY_FIELDS = PROVISIONALLY_FAIL
PROVISIONAL_DISPOSITION = INELIGIBLE
```

## 4. Provisional screen summary

```text
ENTERED_NEW_CANDIDATES = 7
TGT_RANGE = TGT_040..TGT_046
PROVISIONALLY_ELIGIBLE_AFTER_PHASE_B = 0
```

This does **not** qualify Outcome B because the rank-by-rank primary-search provenance record is incomplete.

```text
SUBSTANTIVE_SCREEN_SUGGESTS_ELIGIBLE_TARGET_COUNT = 0
SCIENTIFIC_NO_TARGET_OUTCOME_QUALIFIED = NO
```

## 5. Information firewalls

```text
TARGET_VALUES_ACCESSED = NO
RAW_EVENT_ROWS_ACCESSED = NO
JOINT_OR_MARGINAL_COUNTS_COMPUTED = NO
T_IND_MEMBERSHIP_TESTED = NO
DEPENDENCE_SEARCH_TERMS_USED = NO
CANDIDATE_REVISION = NO
```

Incidental candidate-specific association information on the RIPA page was treated as contamination, not as evidence for or against PGH.

## 6. Repair requirement

A transport/provenance repair may reissue the **same exact Q01-Q12 primary queries**, with no scientific selection-rule change, provided each returned-result stream is durably captured before the next query executes.

The repair must preserve:

```text
TGT_040..TGT_046 = ALREADY_ENCOUNTERED_PROVENANCE
SAME_ID_ON_REENCOUNTER = YES
NEXT_GENUINELY_NEW_ID = TGT_047
SCIENTIFIC_QUERY_MATRIX_CHANGE = NONE
ELIGIBILITY_RULE_CHANGE = NONE
TARGET_TIE_BREAK_CHANGE = NONE
CONTAMINATION_RULE_CHANGE = NONE
```

The repair may re-adjudicate TGT-040..TGT-046 if reencountered under the exact repair protocol, but may not erase already encountered contamination information.

## 7. Claim ceiling

```text
TARGET_SELECTED = NO
EMPIRICAL_TEST = UNINSTANTIATED
PGH_OBJ_0052_SUPPORT = NONE
PGH_OBJ_0052_REFUTATION = NONE
STRONG_PGH_CONFIRMED = NO
R2B = UNSATISFIED
```

A failed execution trace is not evidence for PGH and is not evidence against PGH.
