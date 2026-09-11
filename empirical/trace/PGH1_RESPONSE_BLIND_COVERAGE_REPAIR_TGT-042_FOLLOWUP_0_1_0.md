# PGH-1 Response-Blind Coverage Repair — TGT-042 Follow-up Trace 0.1.0

```text
CANDIDATE_ID = TGT-042
CANDIDATE_EXACT_IDENTITY = Crowd Counting Consortium event data
FOLLOWUP_EXECUTION_ORDER = 2
EXACT_QUERY_STRING = Crowd Counting Consortium event data schema data dictionary fields columns version release missing invalid API download format
MAX_RESULTS_INSPECTED = 10
RESULTS_INSPECTED = 9
RETURN_SET_EXHAUSTED = YES
SECOND_FOLLOWUP_QUERY = FORBIDDEN
TRACE_CAPTURED_BEFORE_NEXT_FOLLOWUP = YES
```

| Rank | Title | Locator | Host | Authority relevance / gate effect |
|---:|---|---|---|---|
| 1 | CCC Crowd Data Dictionary | https://github.com/rexdouglass/crowd-counting-consortium/blob/master/ccc_data_dictionary.md | github.com/rexdouglass/crowd-counting-consortium | Project-maintained dictionary; establishes multiple 0/1 event fields and same-row CSV architecture. |
| 2 | CCC Crowd Data repository | https://github.com/rexdouglass/crowd-counting-consortium | github.com/rexdouglass/crowd-counting-consortium | Project-maintained compiled public CSV; states weekly updating rather than immutable release identity. |
| 3 | CrowdCountingConsortium-data-import | https://github.com/inuwali/CrowdCountingConsortium-data-import | github.com/inuwali/CrowdCountingConsortium-data-import | NONAUTHORITATIVE_LEAD_ONLY; identifies phase-specific Harvard Dataverse persistent IDs but cannot pass E4/E9. |
| 4 | Crowd Counting Consortium — Harvard Ash Center | https://ash.harvard.edu/programs/crowd-counting-consortium/ | ash.harvard.edu | Authoritative project page; establishes public protest-event data and Dataverse publication/access. |
| 5 | CountTogether Public API — Data Models | https://developers.counttogether.app/docs/data-models.html | developers.counttogether.app | UNRELATED_RESULT. |
| 6 | FTC Events API | https://ftc-events.firstinspires.org/api-docs/index.html | ftc-events.firstinspires.org | UNRELATED_RESULT. |
| 7 | Atlassian Crowd database schema | https://developer.atlassian.com/server/crowd/crowd-database-schema/ | developer.atlassian.com | UNRELATED_RESULT. |
| 8 | Atlassian Crowd REST API 3.2.3 | https://docs.atlassian.com/atlassian-crowd/3.2.3/REST | docs.atlassian.com | UNRELATED_RESULT. |
| 9 | Crowd Counting Consortium — compiled repository README | https://github.com/rexdouglass/crowd-counting-consortium/blob/master/README.md | github.com/rexdouglass/crowd-counting-consortium | Duplicate/project documentation; public rolling dataset, no immutable release identity. |

## Direct authoritative navigation from returned results

The Harvard project page directly links its Crowd Counting Consortium Dataverse and states that CCC data are published monthly on a publicly accessible Dataverse. The authority-hosted collection URL was reached:

```text
https://dataverse.harvard.edu/dataverse/crowdcountingconsortium/
```

A phase-specific authority-hosted persistent dataset URL identified through the nonauthoritative lead was also reached:

```text
https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/RI9JFU
```

The Dataverse surface available to this execution returned only a JavaScript/robot-verification shell, so the operation could not establish from controlling authority metadata an exact immutable Dataverse release/version or complete null/invalid handling. The secondary repository's DOI/version assertions are not substituted for authoritative gate evidence.

## Gate effect

```text
E1_PHYSICAL_RECORD_INTERFACE = PASS
E2_PUBLIC_AUDITABLE_ACCESS = PASS
E3_STABLE_IDENTITY = PASS_AT_PROJECT_DATASET_FAMILY_SCOPE
E4_RELEASE_IDENTITY = NOT_ESTABLISHED_AT_EXACT_IMMUTABLE_TARGET_RELEASE_SCOPE
E5_AT_LEAST_THREE_NATIVE_BINARY_FIELDS = PASS
E6_JOINT_INDEXABILITY = PASS
E9_DOCUMENTED_VALIDITY_OR_NULL_HANDLING = NOT_ESTABLISHED
E10_LOW_PREPROCESSING = PASS_IN_PRINCIPLE_FOR_COMPILED_CSV
E11_PRIOR_TARGET_NOVELTY = PASS
E12_NO_DEPENDENCE_CONTAMINATION = PASS__NO_T_IND_OR_EQUIVALENT_COMPATIBILITY_RESULT_ENCOUNTERED
FOLLOWUP_RESULT = INELIGIBLE__E4_AND_E9_NOT_ESTABLISHED
```

No second follow-up is permitted, so the unresolved mandatory gates remain unresolved.
