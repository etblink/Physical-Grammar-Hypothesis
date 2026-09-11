# PGH-1 Response-Blind Coverage Repair — Q08 Trace 0.1.0

```text
QUERY_ID = Q08
SEARCH_EXECUTION_ORDER = 8
EXACT_QUERY_STRING = authoritative public event data dictionary binary flag fields version release
MAX_RESULTS_INSPECTED = 10
RESULTS_INSPECTED = 8
DISTINCT_SPECIFIC_CANDIDATES_ENTERED_OR_REENCOUNTERED = 3
CANDIDATE_CEILING_REACHED = YES
TRACE_CAPTURED_BEFORE_Q09 = YES
```

| Rank | Title | Locator | Host | Disposition | Candidate |
|---:|---|---|---|---|---|
| 1 | PDS4 Data Dictionary — v1 1K00 | https://pds.nasa.gov/datastandards/documents/dd/v1/PDS4_PDS_DD_1K00.pdf | pds.nasa.gov | NONCANDIDATE_GENERIC_OR_NONSPECIFIC__STANDARD | — |
| 2 | PDS4 Data Dictionary — current | https://pds.nasa.gov/datastandards/documents/dd/current/PDS4_PDS_DD_1G00.pdf | pds.nasa.gov | NONCANDIDATE_GENERIC_OR_NONSPECIFIC__STANDARD | — |
| 3 | PDS4 Data Dictionary — v1 1F00 | https://pds.nasa.gov/datastandards/documents/dd/v1/PDS4_PDS_DD_1F00.pdf | pds.nasa.gov | NONCANDIDATE_GENERIC_OR_NONSPECIFIC__STANDARD | — |
| 4 | Interoperable Europe specifications — Core Public Event Vocabulary | https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/specifications | interoperable-europe.ec.europa.eu | NONCANDIDATE_GENERIC_OR_NONSPECIFIC__EVENT_VOCABULARY | — |
| 5 | Crowd Counting Consortium data dictionary | https://github.com/rexdouglass/crowd-counting-consortium/blob/master/ccc_data_dictionary.md | github.com/rexdouglass/crowd-counting-consortium | REENCOUNTERED_PRIOR_TARGET | `TGT-042` |
| 6 | NHD Event Data Dictionary — EPA node route | https://www.epa.gov/node/115133 | epa.gov | REENCOUNTERED_PRIOR_TARGET | `TGT-043` |
| 7 | NHD Event Data Dictionary — EPA waterdata route | https://www.epa.gov/waterdata/nhd-event-data-dictionary | epa.gov | DUPLICATE_OF_ALREADY_ENTERED_CANDIDATE | `TGT-043` |
| 8 | NEMSIS Data Dictionaries & XSD — Version 3.5.1 | https://nemsis.org/technical-resources/version-3/version-3-data-dictionaries/ | nemsis.org | REENCOUNTERED_PRIOR_TARGET | `TGT-041` |

## Closure

Q08 closed when the third distinct candidate identity for the query was encountered. Returned results after rank 8 were not inspected for candidate entry under the frozen per-query ceiling.
