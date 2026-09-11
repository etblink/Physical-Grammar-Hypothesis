# PGH-1 Response-Blind Coverage Repair — TGT-043 Follow-up Trace 0.1.0

```text
CANDIDATE_ID = TGT-043
CANDIDATE_EXACT_IDENTITY = US EPA NHD Event Data
FOLLOWUP_EXECUTION_ORDER = 3
EXACT_QUERY_STRING = US EPA NHD Event Data schema data dictionary fields columns version release missing invalid API download format
MAX_RESULTS_INSPECTED = 10
RESULTS_INSPECTED = 8
RETURN_SET_EXHAUSTED = YES
SECOND_FOLLOWUP_QUERY = FORBIDDEN
TRACE_CAPTURED_BEFORE_NEXT_FOLLOWUP = YES
```

| Rank | Title | Locator | Host | Authority relevance / gate effect |
|---:|---|---|---|---|
| 1 | NHD Event Data Dictionary | https://www.epa.gov/waterdata/nhd-event-data-dictionary | epa.gov | Authoritative field dictionary; event tables contain string/date/integer/double/geometry fields and no set of three native binary data fields. |
| 2 | NHDPlus Versioning | https://www.epa.gov/waterdata/nhdplus-versioning | epa.gov | Authoritative versioning documentation; does not cure E5. |
| 3 | Archived NHD Event Data Dictionary | https://19january2021snapshot.epa.gov/waterdata/nhd-event-data-dictionary_.html | epa.gov | Authoritative historical dictionary; same field architecture; no three native binary fields. |
| 4 | ICIS-NPDES DMR Summary and Data Element Dictionary | https://echo.epa.gov/tools/data-downloads/icis-npdes-dmr-summary | echo.epa.gov | Different EPA dataset/interface; not TGT-043. |
| 5 | Reach Address Database (RAD) | https://www.epa.gov/waterdata/reach-address-database-rad | epa.gov | Authoritative related interface; exposes `Navigable` Y/N flag but not three jointly recorded native binary fields. |
| 6 | Event Indexing Service — archived EPA | https://19january2021snapshot.epa.gov/waterdata/event-indexing-service_.html | epa.gov | Authoritative historical service schema; no three native binary fields established. |
| 7 | Archived NHDPlus Versioning | https://19january2021snapshot.epa.gov/waterdata/nhdplus-versioning_.html | epa.gov | Authoritative historical versioning; no E5 cure. |
| 8 | NHDPlus Version 2 User Guide | https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P10198U6.TXT | nepis.epa.gov | Authoritative user guide; version architecture, no E5 cure. |

## Gate effect

```text
E1_PHYSICAL_RECORD_INTERFACE = PASS
E3_STABLE_IDENTITY = PASS
E4_RELEASE_IDENTITY = AT_LEAST_PARTIALLY_ESTABLISHED_FOR_NHDPLUS_COMPONENTS
E5_AT_LEAST_THREE_NATIVE_BINARY_FIELDS = FAIL
FOLLOWUP_RESULT = INELIGIBLE__E5_FAIL
```

The `NULL?` column in the data dictionary is schema metadata, not an event-record binary field. The related RAD interface exposes one Y/N `Navigable` flag, still below the frozen threshold of three jointly recorded native binary fields. E5 therefore fails decisively.
