# PGH-1 Response-Blind Coverage Repair — Q02 Trace 0.1.0

```text
QUERY_ID = Q02
SEARCH_EXECUTION_ORDER = 2
EXACT_QUERY_STRING = authoritative public dataset data dictionary binary flag fields version release
MAX_RESULTS_INSPECTED = 10
RESULTS_INSPECTED = 10
DISTINCT_SPECIFIC_CANDIDATES_ENTERED_OR_REENCOUNTERED = 2
TRACE_CAPTURED_BEFORE_Q03 = YES
```

| Rank | Title | Locator | Host | Disposition | Candidate |
|---:|---|---|---|---|---|
| 1 | O*NET Database Releases Archive | https://www.onetcenter.org/db_releases.html | onetcenter.org | NONCANDIDATE_GENERIC_OR_NONSPECIFIC__OCCUPATIONAL_ADMINISTRATIVE | — |
| 2 | Open Contracting Data Standard — Release Schema | https://standard.open-contracting.org/latest/en/schema/release/ | standard.open-contracting.org | NONCANDIDATE_GENERIC_OR_NONSPECIFIC__ADMINISTRATIVE_CONTRACTING | — |
| 3 | DCAT-US Dataset schema | https://resources.data.gov/standards/catalog/dcat-us-3/dataset/ | resources.data.gov | NONCANDIDATE_GENERIC_OR_NONSPECIFIC | — |
| 4 | LEHD Public Use Data Schema V4.2.0 | https://lehd.ces.census.gov/data/schema/V4.2.0/lehd_public_use_schema.pdf | lehd.ces.census.gov | NONCANDIDATE_GENERIC_OR_NONSPECIFIC__ADMINISTRATIVE_ECONOMIC_SCHEMA | — |
| 5 | LEHD Public Use Data Schema V4.3.1 | https://lehd.ces.census.gov/data/schema/V4.3.1/lehd_public_use_schema.pdf | lehd.ces.census.gov | NONCANDIDATE_GENERIC_OR_NONSPECIFIC__ADMINISTRATIVE_ECONOMIC_SCHEMA | — |
| 6 | PREMIS Data Dictionary Version 1 | https://www.loc.gov/standards/premis/v1/index.html | loc.gov | NONCANDIDATE_GENERIC_OR_NONSPECIFIC__DIGITAL_PRESERVATION_STANDARD | — |
| 7 | RIPA Explorer — Variable groups and schema changes | https://ripastops.org/articles/variables-and-schema | ripastops.org | REENCOUNTERED_PRIOR_TARGET__PERSISTENT_CONTAMINATION | `TGT-040` |
| 8 | DCAT-US Schema v3.0 | https://resources.data.gov/resources/dcat-us3/ | resources.data.gov | NONCANDIDATE_GENERIC_OR_NONSPECIFIC | — |
| 9 | LEHD Public Use Data Schema V4.10.1 | https://lehd.ces.census.gov/data/schema/V4.10.1/lehd_public_use_schema.pdf | lehd.ces.census.gov | NONCANDIDATE_GENERIC_OR_NONSPECIFIC__ADMINISTRATIVE_ECONOMIC_SCHEMA | — |
| 10 | NEMSIS Data Dictionaries & XSD — Version 3.5.1 | https://nemsis.org/technical-resources/version-3/version-3-data-dictionaries/ | nemsis.org | REENCOUNTERED_PRIOR_TARGET | `TGT-041` |

## Closure

Q02 closed at the ten-result inspection ceiling. `TGT-040` and `TGT-041` retain their existing provenance IDs; neither is assigned a new ID. The already encountered RIPA candidate-specific association information remains binding contamination and is not forgotten by repair.
