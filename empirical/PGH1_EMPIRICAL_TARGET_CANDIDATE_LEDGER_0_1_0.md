# PGH-1 Empirical Target Candidate Ledger 0.1.0

```text
OPERATION_ID = PGH1_EMPIRICAL_INSTANTIATION_TARGET_DISCOVERY_AND_FREEZE
REGISTRY_ID = PGH-OP-0063
VALUE_INSPECTION = NONE
DEPENDENCE_ANALYSIS = NONE
```

| ID | Dataset / system | Lane | Record / ordering | Native alphabet | Metadata disposition | Final contamination | Score |
|---|---|---|---|---|---|---|---:|
| TGT-001 | GFZ definitive planetary Kp | D1 | one Kp every 3 h UT; chronological | 28 native Kp states | **SELECT** | C1 after C2 review | **19** |
| TGT-002 | GFZ definitive C9 | D1 | one daily C9; chronological | integer `0..9` | eligible; loses tie-break | C1 | **19** |
| TGT-003 | GFZ Hp30 | D1 | half-hour chronological index | open-ended thirds | reject: no frozen finite discretization | C1 | — |
| TGT-004 | NOAA/NCEI local K archive | D1 | 3-hour station K | integer `0..9` | reject: station choice unfrozen | C1 | — |
| TGT-005 | NOAA/NCEI GOES X-ray flare reports | D3 | chronological flare events | letter class `A/B/C/M/X` | eligible | C1 after C2 review | **18** |
| TGT-006 | NOAA/NCEI Global Hourly present weather | D1 | station observation chronology | native categorical weather codes | reject: station/report filtering unfrozen | C2 not material after rejection | — |
| TGT-007 | CERN CMS tracker-hit open dataset | D2 | repeated events with detector/layer metadata | finite hit/subdetector/type IDs | reject: substantial reconstruction | C0/C1 | — |

## Authoritative metadata locators

```text
TGT-001/TGT-002:
  GFZ Kp DOI = 10.5880/Kp.0001
  https://kp.gfz.de/en/data
  https://kp.gfz.de/en/about-kp
  https://www.gfz.de/en/section/geomagnetism/data-products-services/kp-index/format-documentation-of-kpyymmwdc-files
  https://isdc.gfz.de/kp-index/explanation/related-indices/

TGT-003:
  https://kp.gfz.de/en/hp30-hp60/data
  https://kp.gfz.de/en/hp30-hp60/about-hpo
  DOI family = 10.5880/Hpo.0003

TGT-004:
  https://www.ncei.noaa.gov/products/geomagnetic-indices

TGT-005:
  https://www.ncei.noaa.gov/products/space-weather/legacy-data/solar-flares-events
  https://www.ncei.noaa.gov/products/goes-r-extreme-ultraviolet-xray-irradiance

TGT-006:
  https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database
  https://www.ncei.noaa.gov/access/search/datasets/global-hourly/

TGT-007:
  https://opendata.cern.ch/record/12220
  DOI = 10.7483/OPENDATA.CMS.CHC3.5KPG
```

## TGT-001 scoring rationale

```text
R1 = 2  fixed chronological 3-hour roles
R2 = 2  official native 28-state alphabet
R3 = 2  one direct time-indexed sequence
R4 = 2  1932-2025 gives 274672 scheduled slots before missing exclusions
R5 = 2  deterministic parse + fixed non-overlapping blocks
R6 = 2  definitive-status and production documentation; no value-dependent selection
R7 = 2  official GFZ DOI + HTTPS/API
R8 = 1  standard internationally recognized derived physical index
R9 = 2  no analyst discretization
R10 = 2 official stable archive
TOTAL = 19
```

## Contamination review

For TGT-001, the architecture was recorded first. The later permitted review found related Markov/transition modeling for other geomagnetic-intensity constructions, including daily maximum Kp/G categories, but no exact result for:

```text
VARIABLE = definitive GFZ three-hour Kp
RANGE = 1932-01-01 through 2025-12-31
BLOCKING = non-overlapping consecutive scheduled triples
```

Therefore:

```text
INITIAL = C2_HINTS_AT_TARGET_DEPENDENCE
REVIEW = NO_EXACT_TARGET_RESULT_DISCLOSED
FINAL = C1_GENERAL_DOMAIN_KNOWLEDGE
```

TGT-005 underwent the same review logic: Markov-style solar-flare process literature exists, but no exact chronological GOES flare-letter triple result was used or located, so its final scoring class is C1.

## Tie break

```text
TGT-001_SCORE = 19
TGT-002_SCORE = 19
TIE_1_NATIVE_FINITE = TIE
TIE_2_LARGER_EVENT_COUNT = TGT-001_KP
```
