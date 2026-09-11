# PGH-1 Response-Blind Coverage Repair — TGT-046 Follow-up Trace 0.1.0

```text
CANDIDATE_ID = TGT-046
CANDIDATE_EXACT_IDENTITY = MODIS Terra Aqua Combined EarthExplorer product interface
FOLLOWUP_EXECUTION_ORDER = 6
EXACT_QUERY_STRING = MODIS Terra Aqua Combined EarthExplorer product interface schema data dictionary fields columns version release missing invalid API download format
MAX_RESULTS_INSPECTED = 10
RESULTS_INSPECTED = 6
RETURN_SET_EXHAUSTED = YES
SECOND_FOLLOWUP_QUERY = FORBIDDEN
PHASE_B_FOLLOWUP_SEARCH = CLOSED
```

| Rank | Title | Locator | Host | Authority relevance / gate effect |
|---:|---|---|---|---|
| 1 | MODIS (Terra, Aqua, Combined) Data Dictionary | https://www.usgs.gov/centers/eros/science/modis-terra-aqua-combined-data-dictionary | usgs.gov | Authoritative EarthExplorer dictionary; establishes one native binary `Auto Quality Flag` (Passed/Failed), while `Day or Night Indicator` and `Science Quality Flag` have more than two substantive states. |
| 2 | MODIS Characterization Support Team L1B Documents | https://mcst.gsfc.nasa.gov/l1b-documents | mcst.gsfc.nasa.gov | Authority-hosted product documentation for specific L1B products; different product-level interface, does not turn the encountered broad EarthExplorer candidate into an E5 pass. |
| 3 | eMODIS NDVI Data Dictionary | https://www.usgs.gov/centers/eros/science/emodis-ndvi-data-dictionary | usgs.gov | Different EarthExplorer product family; not TGT-046. |
| 4 | MODIS BRDF/Albedo product information | https://modis.gsfc.nasa.gov/data/dataprod/mod43.php | modis.gsfc.nasa.gov | Different specific MODIS product family; not TGT-046. |
| 5 | CERES documentation | https://ceres.larc.nasa.gov/data/documentation/ | ceres.larc.nasa.gov | Different NASA measurement/product family; not TGT-046. |
| 6 | QuickDRI Data Dictionary | https://www.usgs.gov/centers/eros/science/quickdri-data-dictionary | usgs.gov | Different USGS product family; not TGT-046. |

## Gate effect

```text
E1_PHYSICAL_RECORD_INTERFACE = PASS_AT_GRANULE_METADATA_SCOPE
E2_PUBLIC_AUDITABLE_ACCESS = PASS_IN_PRINCIPLE
E3_STABLE_IDENTITY = PASS_AT_PRODUCT_GRANULE_SCOPE
E4_RELEASE_IDENTITY = PASS_IN_PRINCIPLE_VIA_DOI_AND_VERSION_FIELDS
E5_AT_LEAST_THREE_NATIVE_BINARY_FIELDS = FAIL
E6_JOINT_INDEXABILITY = MOOT_AFTER_E5_FAIL
E9_DOCUMENTED_VALIDITY_OR_NULL_HANDLING = NOT_NEEDED_AFTER_DECISIVE_E5_FAIL
FOLLOWUP_RESULT = INELIGIBLE__E5_FAIL
```

The controlling USGS dictionary exposes only one exact two-state field: `Auto Quality Flag = Passed/Failed`. `Day or Night Indicator` has Day/Night/Both/All, and `Science Quality Flag` has eight substantive values. No analyst binning or state merging is allowed. E5 therefore fails decisively.
