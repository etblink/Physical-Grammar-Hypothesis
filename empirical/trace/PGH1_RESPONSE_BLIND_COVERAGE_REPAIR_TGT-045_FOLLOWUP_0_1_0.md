# PGH-1 Response-Blind Coverage Repair — TGT-045 Follow-up Trace 0.1.0

```text
CANDIDATE_ID = TGT-045
CANDIDATE_EXACT_IDENTITY = Wyoming Natural Diversity Database observations
FOLLOWUP_EXECUTION_ORDER = 5
EXACT_QUERY_STRING = Wyoming Natural Diversity Database observations schema data dictionary fields columns version release missing invalid API download format
MAX_RESULTS_INSPECTED = 10
RESULTS_INSPECTED = 7
RETURN_SET_EXHAUSTED = YES
SECOND_FOLLOWUP_QUERY = FORBIDDEN
TRACE_CAPTURED_BEFORE_NEXT_FOLLOWUP = YES
```

| Rank | Title | Locator | Host | Authority relevance / gate effect |
|---:|---|---|---|---|
| 1 | WYNDD Observation Data Dictionary | https://www.uwyo.edu/wyndd/find-data-info/about-our-data-information/codes-and-definitions/observation-data-dictionary.html | uwyo.edu | Authoritative precise-observation schema; rich fields, but no three exact authority-defined native binary fields established. |
| 2 | WYNDD Species Observations | https://www.uwyo.edu/wyndd/find-data-info/about-our-data-information/our-core-data-information-products/species-observations.html | uwyo.edu | Authoritative; detailed observations are fulfilled by request and fee tier rather than unrestricted public event-level retrieval. |
| 3 | WYNDD Web Mapping Services | https://www.uwyo.edu/wyndd/find-data-info/about-our-data-information/our-core-data-information-products/web-mapping-services.html | uwyo.edu | Authoritative; precise observations require registered Data Explorer access, while generalized public observations expose no three native binary fields. |
| 4 | USGS Multi-Taxa Database Data Dictionary | https://pubs.usgs.gov/publication/tm16B1 | pubs.usgs.gov | Different dataset/interface; not TGT-045. |
| 5 | WYNDD Collect | https://www.uwyo.edu/wyndd/collect/index.html | uwyo.edu | Submission guidance, not public target access. |
| 6 | WYNDD Species Overlays | https://www.uwyo.edu/wyndd/find-data-info/about-our-data-information/our-core-data-information-products/species-overlays.html | uwyo.edu | Different generalized product; no three native binary fields. |
| 7 | WYNDD home | https://www.uwyo.edu/wyndd/index.html | uwyo.edu | Authority overview; Data Explorer exists, but does not cure precise-record access or E5. |

## Gate effect

```text
PRECISE_OBSERVATIONS__E1_PHYSICAL_RECORD_INTERFACE = PASS
PRECISE_OBSERVATIONS__E2_PUBLIC_AUDITABLE_ACCESS = FAIL_AT_UNRESTRICTED_PUBLIC_SCOPE__REGISTERED_OR_REQUEST_BASED_ACCESS
PRECISE_OBSERVATIONS__E5_AT_LEAST_THREE_NATIVE_BINARY_FIELDS = NOT_ESTABLISHED
GENERALIZED_PUBLIC_OBSERVATIONS__E2_PUBLIC_AUDITABLE_ACCESS = PASS_IN_PRINCIPLE
GENERALIZED_PUBLIC_OBSERVATIONS__E5_AT_LEAST_THREE_NATIVE_BINARY_FIELDS = FAIL
FOLLOWUP_RESULT = INELIGIBLE__NO_SINGLE_INTERFACE_PASSES_E2_AND_E5
```

The repair may not combine the access properties of the generalized service with the richer attributes of the restricted precise-observation service. No second follow-up is permitted.
