# PGH-1 Response-Blind Coverage Repair — TGT-041 Follow-up Trace 0.1.0

```text
CANDIDATE_ID = TGT-041
CANDIDATE_EXACT_IDENTITY = NEMSIS Version 3.5.1 National EMS EMS event interface
FOLLOWUP_EXECUTION_ORDER = 1
EXACT_QUERY_STRING = NEMSIS Version 3.5.1 National EMS EMS event interface schema data dictionary fields columns version release missing invalid API download format
MAX_RESULTS_INSPECTED = 10
RESULTS_INSPECTED = 10
SECOND_FOLLOWUP_QUERY = FORBIDDEN
TRACE_CAPTURED_BEFORE_NEXT_FOLLOWUP = YES
```

| Rank | Title | Locator | Host | Authority relevance / gate effect |
|---:|---|---|---|---|
| 1 | NEMSIS Data Dictionaries & XSD | https://nemsis.org/technical-resources/version-3/version-3-data-dictionaries/ | nemsis.org | Authoritative; establishes v3.5.1 standard, EMS PCR/Event API, schemas and data dictionaries; does not establish public event-level National EMS records. |
| 2 | NEMSIS Data Dictionaries & XSD — test site | https://test.nemsis.org/technical-resources/version-3/version-3-data-dictionaries/ | test.nemsis.org | Authority-hosted test mirror; same standard resources; no E2 closure. |
| 3 | NEMSIS v3.5 Resources | https://nemsis.org/v3-5-revision/v3-5-resources/ | nemsis.org | Authoritative release/resource index; no public event-level dataset access established. |
| 4 | NEMSIS Data Dictionary v3.5.1 build 250115 | https://git.nemsis.org/projects/NEP/repos/nemsis_public/raw/DataDictionary/PDFHTML/EMSDEMSTATE_National/NEMSISDataDictionary_Compressed.pdf?at=refs%2Ftags%2F3.5.1.250115 | git.nemsis.org | Authoritative dictionary; establishes standard structure/version; no E2 closure. |
| 5 | NEMSIS Data Dictionary Section Grouping | https://www.nemsis.org/media/nemsis_v3/release-3.5.1/DataDictionary/PDFHTML/EMSDEMSTATE/sample.html | nemsis.org | Authoritative; establishes element/recurrence/national indicators and usage semantics. |
| 6 | NEMSIS Data Dictionary v3.5.1 build 251001 | https://nemsis.org/media/nemsis_v3/release-3.5.1/DataDictionary/PDFHTML/EMSDEMSTATE/NEMSISDataDictionary.pdf | nemsis.org | Authoritative current v3.5.1 dictionary; no E2 closure. |
| 7 | NEMSIS v3.5 Resources — test site | https://test.nemsis.org/v3-5-revision/v3-5-resources/ | test.nemsis.org | Authority-hosted test mirror; no E2 closure. |
| 8 | NEMSIS National-only Data Dictionary v3.5.1 | https://nemsis.org/media/nemsis_v3/release-3.5.1/DataDictionary/PDFHTML/EMSDEMSTATE_National/NEMSISDataDictionary.pdf | nemsis.org | Authoritative national element dictionary; no event-level access established. |
| 9 | NEMSIS eSituation schema documentation | https://www.nemsis.org/media/nemsis_v3/release-3.5.1/DataDictionary/APIs/EMSDataSetAPI/eSituation_v3_xsd.html | nemsis.org | Authoritative EMS event schema; establishes joint PCR/event schema and nil/not-value semantics. |
| 10 | NEMSIS v3.5.1 highlighted data dictionary | https://nemsis.org/wp-content/uploads/2025/01/v3.5.1.250115-Data-Dictionary-with-Highlights.pdf | nemsis.org | Authority-hosted dictionary; no E2 closure. |

## Gate effect

```text
E1_PHYSICAL_RECORD_INTERFACE = PASS_AT_SCHEMA_SCOPE
E2_PUBLIC_AUDITABLE_ACCESS = NOT_ESTABLISHED_AT_EVENT_RECORD_SCOPE
E3_STABLE_IDENTITY = PASS_AT_STANDARD_SCOPE
E4_RELEASE_IDENTITY = PASS_AT_STANDARD_SCOPE
E5_AT_LEAST_THREE_NATIVE_BINARY_FIELDS = PASS_FROM_AUTHORITY_DICTIONARY
E6_JOINT_INDEXABILITY = PASS_AT_EMS_EVENT_SCHEMA_SCOPE
E9_DOCUMENTED_VALIDITY_OR_NULL_HANDLING = PASS_AT_SCHEMA_SCOPE
FOLLOWUP_RESULT = INELIGIBLE__E2_NOT_ESTABLISHED
```

The frozen follow-up resolves extensive standard metadata but does not establish publicly retrievable or independently auditable event-level National EMS records for the target interface. No second query is permitted.
