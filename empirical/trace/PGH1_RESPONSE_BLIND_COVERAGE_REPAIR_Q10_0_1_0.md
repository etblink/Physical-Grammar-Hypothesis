# PGH-1 Response-Blind Coverage Repair — Q10 Trace 0.1.0

```text
QUERY_ID = Q10
SEARCH_EXECUTION_ORDER = 10
EXACT_QUERY_STRING = authoritative public observation data dictionary binary flag fields version release
MAX_RESULTS_INSPECTED = 10
RESULTS_INSPECTED = 6
DISTINCT_SPECIFIC_CANDIDATES_ENTERED_OR_REENCOUNTERED = 3
CANDIDATE_CEILING_REACHED = YES
TRACE_CAPTURED_BEFORE_Q11 = YES
```

| Rank | Title | Locator | Host | Disposition | Candidate |
|---:|---|---|---|---|---|
| 1 | PDS4 Data Dictionary — v1 1K00 | https://pds.nasa.gov/datastandards/documents/dd/v1/PDS4_PDS_DD_1K00.pdf | pds.nasa.gov | NONCANDIDATE_GENERIC_OR_NONSPECIFIC__STANDARD | — |
| 2 | PDS4 Data Dictionary — current 1G00 | https://pds.nasa.gov/datastandards/documents/dd/current/PDS4_PDS_DD_1G00.pdf | pds.nasa.gov | NONCANDIDATE_GENERIC_OR_NONSPECIFIC__STANDARD | — |
| 3 | BUFR TABLE B — NCEP observational database / PREPBUFR | https://www.emc.ncep.noaa.gov/emc/pages/infrastructure/bufrlib/tables/TableB_0_STDv38_LOC7.html | emc.ncep.noaa.gov | REENCOUNTERED_PRIOR_TARGET | `TGT-044` |
| 4 | WYNDD Observation Data Dictionary | https://www.uwyo.edu/wyndd/find-data-info/about-our-data-information/codes-and-definitions/observation-data-dictionary.html | uwyo.edu | REENCOUNTERED_PRIOR_TARGET | `TGT-045` |
| 5 | PDS4 unabridged beta data dictionary | https://pds-engineering.jpl.nasa.gov/wp-content/uploads/documents/pds2010/design/data_design/pds4datadictionary_unabridged_beta.pdf | pds-engineering.jpl.nasa.gov | NONCANDIDATE_GENERIC_OR_NONSPECIFIC__STANDARD | — |
| 6 | MODIS Terra/Aqua/Combined Data Dictionary | https://www.usgs.gov/centers/eros/science/modis-terra-aqua-combined-data-dictionary | usgs.gov | REENCOUNTERED_PRIOR_TARGET | `TGT-046` |

## Closure

Q10 closed immediately when the third distinct candidate identity for the query was encountered at rank 6. Returned results beyond rank 6 were not inspected for candidate entry under the frozen per-query ceiling.
