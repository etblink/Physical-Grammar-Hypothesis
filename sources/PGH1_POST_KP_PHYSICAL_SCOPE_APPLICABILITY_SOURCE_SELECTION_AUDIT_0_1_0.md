# PGH-1 Post-Kp Physical Scope / Theory-Applicability Source Selection Audit 0.1.0

## Preregistered boundary

```text
PREREGISTRATION_COMMIT = 3ec88ce19432f33dc7c1b117f2d3107ddb8dc3e2
SEARCH_BEGAN_AFTER_PREREGISTRATION = YES
SEARCH_GAP = SG5_ONLY
SUCCESSOR_SELECTION = NONE
PHYSICAL_SECTOR_SELECTION = NONE
EMPIRICAL_TARGET_SEARCH = NONE
```

## Search method

Search was organized by the five preregistered lanes rather than by any desired answer about PGH. Candidate discovery emphasized publisher/proceedings pages, DOI records, authoritative institutional records, and primary sources.

The search did **not** include terms asking for systems where `A ⟂ C | B`, Markov behavior, Kp alternatives, or sources capable of excluding the failed Kp target.

## Coverage result

```text
SG5-L1_ACCEPTED = 4
SG5-L2_ACCEPTED = 6
SG5-L3_ACCEPTED = 3
SG5-L4_ACCEPTED = 6
SG5-L5_ACCEPTED = 2
TOTAL_NEW_ACCEPTED = 21
```

Cross-lane relevance is common; each source is counted once under its primary SG5 lane.

## Deduplication

Repository search across the pre-existing PGH source material found no exact author/title matches for the 21 frozen SG5 records. The existing 85-source corpus remains unchanged.

```text
PREEXISTING_REUSED = 0
NEW_DISTINCT_ACCEPTED = 21
RECONCILED_TOTAL = 106_AT_CURRENT_REPOSITORY_DEDUP_SCOPE
```

The phrase `AT_CURRENT_REPOSITORY_DEDUP_SCOPE` remains deliberate: it does not claim a universal bibliographic deduplication outside the project archive.

## Representative rejected/deferred candidates

### R-SG5-001 — Halbert White, Maximum Likelihood Estimation of Misspecified Models (1982)

```text
DISPOSITION = REJECT_REMOTE_RELEVANCE
```

High-authority misspecification theory, but its central task is estimator behavior under misspecification rather than scientific domain-of-applicability or physical-regime selection. L3 is better covered by sources explicitly connecting model discrepancy, validation, and prediction.

### R-SG5-002 — Box, Science and Statistics / generic “all models are wrong” literature

```text
DISPOSITION = REJECT_REDUNDANT_REMOTE_RELEVANCE
```

Useful methodological background but too generic for the frozen SG5 extraction fields once model discrepancy and V&V sources were admitted.

### R-SG5-003 — Aneesh Manohar, Introduction to Effective Field Theories (2018 lectures)

```text
DISPOSITION = REJECT_REDUNDANT
```

Authoritative and relevant, but L2 reached saturation with Wilson/Kogut, Appelquist/Carazzone, Weinberg, Polchinski, Georgi, and Burgess, covering RG, decoupling, effective Lagrangians, scale hierarchy, and power counting.

### R-SG5-004 — Recovering from Selection Bias in Causal and Statistical Inference (Bareinboim, Tian, Pearl, 2014)

```text
DISPOSITION = REJECT_REMOTE_RELEVANCE
```

Strong causal source, but sampling/selection-bias recoverability is not the same question as theory/domain transportability. The transportability series is more direct for SG5-L4.

### R-SG5-005 — Meta-Transportability of Causal Effects (Bareinboim & Pearl, 2013)

```text
DISPOSITION = REJECT_REDUNDANT
```

Directly relevant but redundant after the 2011, 2012, 2013 limited-experiment, and 2016 data-fusion sources establish the domain-difference/transportability machinery.

### R-SG5-006 — Visual Causal Feature Learning (Chalupka, Perona, Eberhardt)

```text
DISPOSITION = REJECT_PREDOMINANTLY_APPLICATION_EXAMPLE
```

Interesting causal abstraction work, but less direct than Rubenstein et al. for cross-level exact causal consistency.

### R-SG5-007 — Stanford Encyclopedia of Philosophy, Models in Science

```text
DISPOSITION = REJECT_WEAK_AUTHORITY_FOR_FREEZE
```

Excellent secondary orientation, but primary articles and monograph chapters were available for the relevant philosophical lanes.

### R-SG5-008 — Model Cards for Model Reporting

```text
DISPOSITION = REJECT_REMOTE_RELEVANCE
```

Explicit intended-use documentation is conceptually adjacent, but the main context is deployed machine learning governance rather than scientific theory/model applicability in the sense targeted by SG5.

### R-SG5-009 — broad effective-model application papers

```text
DISPOSITION = REJECT_PREDOMINANTLY_APPLICATION_EXAMPLE
```

Numerous domain-specific EFT/modeling papers use regime assumptions without contributing additional foundational content on how applicability is justified.

## Saturation audit

```text
ALL_FIVE_LANES_COVERED = YES
L2_AT_LEAST_3_INDEPENDENT_AUTHORITATIVE_ANCHORS = YES__6
L4_AT_LEAST_3_INDEPENDENT_AUTHORITATIVE_ANCHORS = YES__6
APPLICATION_VS_FIT_DISTINCTION_SOURCE_SUPPORTED = YES
REGIME_VALIDITY_SOURCE_SUPPORTED = YES
TRANSPORT_ASSUMPTION_SOURCE_SUPPORTED = YES
SEMANTIC_PARTIAL_APPLICABILITY_SOURCE_SUPPORTED = YES
ADDITIONAL_SEARCH_PREDOMINANTLY_REDUNDANT_OR_REMOTE = YES
```

## Outcome

```text
OUTCOME = A__SG5_CORPUS_QUALIFIED_AND_SATURATED__DOMAINS_OF_APPLICABILITY_REGIME_VALIDITY_AND_TRANSPORT_ASSUMPTIONS_HAVE_AUTHORITATIVE_COVERAGE__HAND_OFF_TO_SEPARATE_SOURCE_BOUND_SCOPE_ORIGIN_ADJUDICATION
```

## Firewalls verified

```text
SOURCE_USED_AS_EVIDENCE_PGH_TRUE = NO
RESTRICTED_PGH_SCOPE_SELECTED = NO
EFFECTIVE_THEORY_DOMAIN_PROMOTED_TO_PGH_SCOPE = NO
CAUSAL_TRANSPORT_RULE_PROMOTED_TO_PGH_META_GRAMMAR = NO
SOURCE_SELECTED_TO_EXCLUDE_KP = NO
SUCCESSOR_GRAMMAR_SELECTED = NO
PHYSICAL_SECTOR_SELECTED = NO
EMPIRICAL_TARGET_SEARCHED = NO
FCP_CHANGED = NO
```
