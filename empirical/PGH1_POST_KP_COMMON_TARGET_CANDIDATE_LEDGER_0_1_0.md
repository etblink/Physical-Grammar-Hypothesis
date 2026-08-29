# PGH-1 Post-Kp Common-Target Candidate Ledger 0.1.0

## Identity

```text
OPERATION_ID = PGH1_POST_KP_COMMON_TARGET_MULTI_CANDIDATE_TARGET_DISCOVERY_AND_FREEZE
REGISTRY_ID = PGH-OP-0086
PREREGISTRATION_COMMIT = c825091ad7f24cee0c3d81e7530d366eb226a790
SEARCH_BEGAN_AFTER_PREREGISTRATION = YES
TARGET_VALUE_INSPECTION = NONE
DEPENDENCE_ANALYSIS = NONE
RAW_DATA_DOWNLOAD = NONE
```

The search used only the metadata architecture frozen in the preregistration. No query intentionally sought independence, conditional independence, correlation, serial behavior, model fit, or a target favorable to any successor package.

## Binding quarantine

All pre-Kp opportunities TGT-001 through TGT-007 remain ineligible for first positive successor credit, including alternate packaging of the same underlying record opportunity.

## Candidate ledger

| ID | Candidate | Lane | Mandatory disposition | Contamination | R1-R10 | Total |
|---|---|---|---|---|---|---:|
| TGT-008 | NOAA/NWS NHC Atlantic HURDAT2 — native system status | D1/D2 | **ELIGIBLE / SELECT** | C1 | 2,2,2,1,2,2,2,2,2,2 | **19** |
| TGT-009 | NOAA/NWS NHC NE/NC Pacific HURDAT2 — native system status | D1/D2 | ELIGIBLE / tie loses T7 | C1 | 2,2,2,1,2,2,2,2,2,2 | **19** |
| TGT-010 | NOAA/NCEI IBTrACS v4.01 — combined `NATURE` | D2 | ELIGIBLE | C1 | 2,2,2,2,2,1,2,1,2,2 | **18** |
| TGT-011 | NOAA/NCEI Storm Events — standardized event type, 2000–2025 | D1/D5 | ELIGIBLE | C1 | 1,2,2,1,2,2,2,1,2,2 | **17** |
| TGT-012 | Smithsonian GVP confirmed Holocene eruptions — VEI | D5 | REJECT E6 | C0 | — | — |
| TGT-013 | USGS ComCat — event `type` | D5 | REJECT E5 | C0 | — | — |
| TGT-014 | CERN LHCb masterclass events | D3 | REJECT E5/E9 | C0 | — | — |

No D4 astronomical/space candidate located in the bounded metadata search simultaneously cleared native finite physical state, objective ordered repeated records, support, and low-preprocessing requirements.

## TGT-008 — Atlantic HURDAT2

Authoritative metadata:

```text
AUTHORITY = NOAA / National Weather Service / National Hurricane Center
DATA_PAGE = https://www.nhc.noaa.gov/data/
FORMAT = https://www.nhc.noaa.gov/data/hurdat/hurdat2-format-atl-1851-2021.pdf
ARCHIVE_CLASS = https://www.nhc.noaa.gov/data/hurdat/
CURRENT_ARCHIVE_SPAN = 1851-2025
CURRENT_RELEASE_NOTE = updated 2026-02-27 to include 2025 season
RECORD_ARCHITECTURE = storm-segmented best track; predominantly standard 0000,0600,1200,1800 UTC records
```

The authoritative HURDAT2 format documents the native system-status field:

```text
TD = tropical depression
TS = tropical storm
HU = hurricane
EX = extratropical cyclone
SD = subtropical depression
SS = subtropical storm
LO = low that is neither tropical/subtropical/extratropical cyclone
WV = tropical wave
DB = disturbance
```

The same format metadata records that `DB` was first used in 1980, `WV` in 1981, and `LO` in 1987; therefore 1988 is the first complete calendar year after the last of the current nine status categories was introduced.

NHC metadata also document standard synoptic times and distinguish additional asynoptic records. A NOAA/NHC Joint Hurricane Testbed metadata source states that Atlantic HURDAT2 for 1999–2016 alone contains 5,409 six-hour observations. NHC's exceptionally active 2020 season page lists only 31 systems. Together these metadata make the >=1,000 within-storm nonoverlapping-triple requirement comfortably supportable without reading the raw HURDAT2 event file. R4 is nevertheless scored conservatively as 1 rather than 2 because an exact frozen-range retained-triple count is deferred to later custody.

```text
E1=PASS E2=PASS E3=PASS E4=PASS E5=PASS E6=PASS
E7=PASS E8=PASS E9=PASS E10=PASS E11=PASS
```

Contamination disclosure: general meteorological knowledge and a metadata-support NHC report about tropical-cyclone forecasting were encountered. No numerical or qualitative result for any of the five frozen independence statements on the HURDAT2 `status` sequence was sought or inspected.

```text
CONTAMINATION = C1_GENERAL_DOMAIN_KNOWLEDGE_ONLY
```

## TGT-009 — NE/NC Pacific HURDAT2

NHC publishes a separate 1949–2025 NE/NC Pacific HURDAT2 with the same direct six-hour best-track architecture and a native finite status field. It earns the same conservative 19/20 score.

The frozen tie breaks R2, R1, R4, R5, R6, and R7 remain tied. T7 therefore selects the earlier documented archive start:

```text
ATLANTIC_START = 1851
NE_NC_PACIFIC_START = 1949
T7_WINNER = TGT-008
```

No scientific preference for the Atlantic basin is inferred from this administrative tie break.

## TGT-010 — IBTrACS v4.01

Authoritative NCEI metadata identify DOI `10.25921/82ty-9e16`, global tropical-cyclone tracks from the 1840s to present, and generally 3-hour/six-hour observations. The first-class `NATURE` field is finite:

```text
DS, TS, ET, SS, NR, MX
```

However `NATURE` is a combined classification assigned from all available agency storm types; `MX` explicitly represents conflicting agency reports. The state is therefore a standardized synthesized physical classification rather than a direct single-authority native status. R6 and R8 are scored 1, leaving total 18.

## TGT-011 — NOAA Storm Events

NCEI supplies official bulk CSV records and documents 48 standardized event types from 1996 onward; from 2000 the NWS data-entry interface used a drop-down event-type selector. The 2000–2025 complete-year window therefore has a rigid finite classification and large public bulk archive.

The sequence is weaker than a tracked physical system: simultaneous events across geography require a deterministic secondary ordering after begin time, and the database records significant reportable phenomena rather than one evolving object. R1 and R8 are therefore 1. It remains eligible but ranks below HURDAT2.

## TGT-012 — Smithsonian GVP confirmed eruptions

VOTW v5.4.0 (7 Aug 2026; DOI `10.5479/si.GVP.VOTW5-2026.5.4`) provides 9,916 confirmed Holocene eruptions and a finite VEI scale 0–8. Metadata do not establish that >=1,000 nonoverlapping chronological triples survive when every constituent must have a valid VEI and deterministic temporal ordering. Because E6 is mandatory, this candidate is rejected rather than scored.

## TGT-013 — USGS ComCat

ComCat is an authoritative public physical-event catalog with exact UTC origin times. Its documented `type` field gives typical values such as `earthquake` and `quarry`, but the metadata page used in discovery does not supply a complete stable finite state alphabet suitable for the frozen E5 requirement. PAGER alert colors are finite but are a derived impact product available only for a subset and would change the target object. TGT-013 is rejected at E5.

## TGT-014 — CERN LHCb masterclass events

The CERN Open Data Portal provides 5,250 preselected LHCb events, but the record is a derived/masterclass sample and its metadata do not expose one native finite categorical physical-state field that can be read sequentially without additional reconstruction/classification. It fails E5 and E9.

## Selection

```text
HIGHEST_SCORE = 19
TIED = TGT-008;TGT-009
T1_R2 = TIE
T2_R1 = TIE
T3_R4 = TIE
T4_R5 = TIE
T5_R6 = TIE
T6_R7 = TIE
T7_EARLIER_ARCHIVE_START = TGT-008
SELECTED_TARGET = TGT-008
OUTCOME = A__ONE_NEW_COMMON_TARGET_QUALIFIES_AND_IS_FROZEN
```

No target values were opened, downloaded, materialized, or analyzed.