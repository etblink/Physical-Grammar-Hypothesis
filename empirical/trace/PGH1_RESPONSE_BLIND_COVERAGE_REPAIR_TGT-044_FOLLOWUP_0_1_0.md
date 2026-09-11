# PGH-1 Response-Blind Coverage Repair — TGT-044 Follow-up Trace 0.1.0

```text
CANDIDATE_ID = TGT-044
CANDIDATE_EXACT_IDENTITY = NCEP observational database PREPBUFR interface
FOLLOWUP_EXECUTION_ORDER = 4
EXACT_QUERY_STRING = NCEP observational database PREPBUFR interface schema data dictionary fields columns version release missing invalid API download format
MAX_RESULTS_INSPECTED = 10
RESULTS_INSPECTED = 10
SECOND_FOLLOWUP_QUERY = FORBIDDEN
TRACE_CAPTURED_BEFORE_NEXT_FOLLOWUP = YES
```

| Rank | Title | Locator | Host | Authority relevance / gate effect |
|---:|---|---|---|---|
| 1 | NCEP BUFR Table B — current | https://www.emc.ncep.noaa.gov/emc/pages/infrastructure/bufrlib/tables/bufrtab_tableb.html | emc.ncep.noaa.gov | Authoritative descriptor table; current BUFR master table version 46, but not a single immutable PREPBUFR target release. |
| 2 | NCEP BUFR Table B — master table version 24 | https://emc.ncep.noaa.gov/emc/pages/infrastructure/bufrlib/tables/TableB_0_STDv24_LOC7.html | emc.ncep.noaa.gov | Authoritative historical descriptor table; no target-release closure. |
| 3 | PREPBUFR Processing at NCEP | https://www.emc.ncep.noaa.gov/emc/pages/infrastructure/obs-data/prepbufr.doc/document.php | emc.ncep.noaa.gov | Authoritative architecture documentation; establishes self-defining files/message types, not three exact jointly recorded native-binary fields for a frozen target release. |
| 4 | NCEP BUFR Table B — master table version 14 | https://www.emc.ncep.noaa.gov/emc/pages/infrastructure/bufrlib/tables/TableB_0_STDv14_LOC7.html | emc.ncep.noaa.gov | Authoritative historical descriptor table; no target-release closure. |
| 5 | Observational Data Processing at NCEP | https://www.emc.ncep.noaa.gov/emc/pages/infrastructure/obs-data-processing.php | emc.ncep.noaa.gov | Authoritative processing overview; confirms PREPBUFR use and BUFR descriptors, but not exact immutable target release or E5/E6. |
| 6 | PREPBUFR repository README | https://github.com/kotsuki-lab/PREPBUFR/blob/main/README.md | github.com/kotsuki-lab/PREPBUFR | NONAUTHORITATIVE_LEAD_ONLY; points to external archive downloads, cannot pass gates. |
| 7 | NCEP BUFR Table B — version 31 legacy host | https://www.nco.ncep.noaa.gov/sib/jeff/bufrtab_tableb.html | nco.ncep.noaa.gov | Authority-hosted legacy descriptor table; no target-release closure. |
| 8 | DART PREPBUFR documentation | https://docs.dart.ucar.edu/en/latest/observations/obs_converters/NCEP/prep_bufr/prep_bufr.html | docs.dart.ucar.edu | NONCONTROLLING_LEAD; describes archive access, not NCEP authority evidence for the frozen target. |
| 9 | NCEP BUFR Table B — version 23 legacy host | https://www.nco.ncep.noaa.gov/sib/jeff/TableB_0_STDv23_LOC7.html | nco.ncep.noaa.gov | Authority-hosted historical descriptor table; no target-release closure. |
| 10 | NCEP BUFR Table B — version 13 legacy host | https://www.nco.ncep.noaa.gov/sib/jeff/TableB_0_STDv13_LOC7.html | nco.ncep.noaa.gov | Authority-hosted historical descriptor table; no target-release closure. |

## Gate effect

```text
E1_PHYSICAL_RECORD_INTERFACE = PASS
E2_PUBLIC_AUDITABLE_ACCESS = NOT_ESTABLISHED_FROM_CONTROLLING_NCEP_TARGET_RELEASE_METADATA
E3_STABLE_IDENTITY = PASS_AT_PREPBUFR_INTERFACE_FAMILY_SCOPE
E4_RELEASE_IDENTITY = NOT_ESTABLISHED_AT_SINGLE_IMMUTABLE_TARGET_RELEASE_SCOPE
E5_AT_LEAST_THREE_NATIVE_BINARY_FIELDS = NOT_ESTABLISHED_FOR_ONE_FROZEN_TARGET_RELEASE
E6_JOINT_INDEXABILITY = NOT_ESTABLISHED_FOR_THREE_EXACT_NATIVE_BINARY_FIELDS
E9_DOCUMENTED_VALIDITY_OR_NULL_HANDLING = PARTIAL_AT_BUFR_STANDARD_SCOPE
FOLLOWUP_RESULT = INELIGIBLE__E4_E5_E6_NOT_ESTABLISHED
```

The presence of general BUFR code/flag tables does not by itself establish three exact two-state fields jointly present in one prospectively frozen PREPBUFR release. No second follow-up is permitted.
