# PGH-1 Post-Kp Common-Target Multi-Candidate Multiplicity Protocol Gate — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_POST_KP_COMMON_TARGET_MULTI_CANDIDATE_MULTIPLICITY_PROTOCOL_GATE
REGISTRY_ID = PGH-OP-0084
CANONICAL_BASE = 39aab2317246fe64eae1e57f86d1b9f72a34dfa3
CANDIDATE_FAMILY = [PGH-OBJ-0041,PGH-OBJ-0042,PGH-OBJ-0043,PGH-OBJ-0044,PGH-OBJ-0045]
FAMILY_SIZE = 5
TARGET_DISCOVERY = FORBIDDEN_IN_THIS_GATE
TARGET_METADATA = FORBIDDEN_IN_THIS_GATE
EMPIRICAL_DATA = FORBIDDEN
NEW_SOURCE_SEARCH = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Freeze the family-level empirical governance required to confront all five admitted post-Kp successor candidates on **one common prospectively selected target** without candidate-specific target shopping or uncorrected multiple testing.

This gate does not discover a target and does not define target-specific null generators beyond reusable statistic/decision templates.

## Candidate restrictions already frozen

```text
H1 = PGH-OBJ-0041 : A ⟂ C
H2 = PGH-OBJ-0042 : A ⟂ B | C
H3 = PGH-OBJ-0043 : A ⟂ B
H4 = PGH-OBJ-0044 : B ⟂ C | A
H5 = PGH-OBJ-0045 : B ⟂ C
```

No candidate may be added, removed, relabeled, or replaced after target discovery begins under this protocol.

## Common-target rule

One physical target must be selected for the **entire five-candidate family** using a common metadata-only eligibility/ranking protocol.

Every selected target must support the same ordered roles:

```text
A = EARLIEST_OR_UPSTREAM
B = INTERMEDIATE
C = LATEST_OR_DOWNSTREAM
```

and repeated jointly indexable finite records.

Candidate-specific target selection is prohibited.

## Prior-discovery quarantine

The post-Kp admission standard requires candidate identity to freeze before target discovery.

Therefore any target opportunity whose identity/metadata was already discovered or ranked in the pre-Kp first-target program is ineligible for **first positive post-Kp successor credit**, even if its candidate-relevant dependence behavior was never inspected.

The later target-discovery operation must bind the exact prior target-discovery ledger and exclude every target recorded there from primary-successor target selection.

```text
KP = INELIGIBLE_FOR_POSITIVE_SUCCESSOR_CREDIT
C9_IF_PREVIOUSLY_DISCOVERED = INELIGIBLE_FOR_PRIMARY_SUCCESSOR_TARGET
GOES_IF_PREVIOUSLY_DISCOVERED = INELIGIBLE_FOR_PRIMARY_SUCCESSOR_TARGET
ALL_OTHER_PREVIOUSLY_LEDGERED_TARGETS = SAME_QUARANTINE
```

Previously known targets may later serve only under a separately preregistered negative/control role. They may not be recycled as the first prospective success of a candidate designed after their discovery.

## Common target eligibility template

A future discovery/freeze operation must require all:

```text
PHYSICAL_RECORD_SCOPE
OBJECTIVE_ORDERED_THREE_ROLE_ARCHITECTURE
JOINT_EVENT_OR_INDEX_IDENTITY
FINITE_NATIVE_ALPHABET_OR_PRECOMMITTED_VALUE_MAPPING
PUBLIC_OR_AUDITABLE_EVENT_LEVEL_ACCESS
ADEQUATE_PROSPECTIVE_SAMPLE_SUPPORT
DOCUMENTED_SELECTION_MISSINGNESS_AND_MEASUREMENT_RULES
NO_USE_OF_CANDIDATE_DEPENDENCE_FOR_DISCOVERY_OR_RANKING
NO_PRIOR_DISCOVERY_BEFORE_POST_KP_CANDIDATE_FREEZE
```

The target ranking dimensions may use measurement-role clarity, native finite records, event-level access, sample size, preprocessing burden, missingness clarity, reproducibility, physical-record clarity and archival stability. They may not use any H1-H5 fit statistic or known dependence property.

## Candidate test statistics

### Marginal-independence candidates

For `X ⟂ Y` use the likelihood-ratio / mutual-information statistic

\[
G^2_{X;Y}=2N I_{nat}(X;Y).
\]

This applies to H1, H3 and H5 with their frozen variable pair.

### Conditional-independence candidates

For `X ⟂ Y | Z` use

\[
G^2_{X;Y\mid Z}=2N I_{nat}(X;Y\mid Z).
\]

This applies to H2 and H4.

Bits-scale mutual information and descriptive normalized effect measures may be reported but cannot replace the preregistered primary `G²` decision statistic.

## Calibration architecture

After a target is frozen and before its data values are materialized, the target-specific analysis preregistration must choose and fully specify **two materially distinct null calibrations** for every candidate, sharing nuisance/segment handling where scientifically appropriate.

At minimum:

```text
CALIBRATION_1 = NONPARAMETRIC_OR_CONDITIONAL_RANDOMIZATION_STYLE_NULL
CALIBRATION_2 = PARAMETRIC_OR_PROCESS_BOOTSTRAP_STYLE_NULL
```

The exact preservation constraints must be determined from target metadata/measurement structure, not candidate fit.

The preregistration must freeze complete stochastic implementation semantics required by `PGH-OBJ-0040`, including PRNG, random-word mappings, permutation/sampling algorithms, quantile conventions, software versions and deterministic seeds.

## Familywise multiplicity rule

Set

```text
FAMILY_ALPHA = 0.01
M = 5
```

For each calibration separately, apply **Holm's step-down procedure** to the five candidate p-values.

Rationale:

- controls familywise probability of falsely refuting one or more true candidate restrictions under arbitrary dependence among tests;
- does not require candidate p-values to be independent;
- does not privilege marginal versus conditional hypotheses;
- is deterministic once the five p-values are frozen.

No unadjusted p-value may by itself produce a candidate refutation verdict.

## Candidate-level verdict rule

For each candidate `Hi`, define:

```text
R1_i = HOLM_REJECTED_UNDER_CALIBRATION_1
R2_i = HOLM_REJECTED_UNDER_CALIBRATION_2
```

Then:

```text
IF R1_i=YES AND R2_i=YES:
    VERDICT_i = REFUTED_ON_COMMON_TARGET

IF R1_i=NO AND R2_i=NO:
    VERDICT_i = SURVIVES_COMMON_TARGET_TEST

IF R1_i != R2_i:
    VERDICT_i = INCONCLUSIVE_CALIBRATION_DISAGREEMENT
```

Survival is not confirmation of exact independence or strong PGH.

## Support and custody ceiling

Target-specific preregistration must define support/missingness thresholds before data access.

Any custody failure, parser ambiguity, insufficient support, nonfrozen preprocessing, or inability to implement both calibrations yields `INCONCLUSIVE` for affected candidate(s) or the entire family as appropriate.

No candidate may be favored because another candidate encounters a technical failure.

## Family-level outcome rule

After all five candidate verdicts are frozen:

```text
ALL_FIVE_REFUTED = CURRENT_FIVE_CANDIDATE_SUCCESSOR_FAMILY_REFUTED_AT_COMMON_TARGET

EXACTLY_ONE_SURVIVES_AND_NONE_INCONCLUSIVE = UNIQUE_SURVIVOR_AT_THIS_TARGET__NOT_CONFIRMED

MULTIPLE_SURVIVE_AND_NONE_INCONCLUSIVE = PLURALITY_SURVIVES_COMMON_TARGET

ANY_INCONCLUSIVE = FAMILY_RESULT_PARTLY_OR_FULLY_INCONCLUSIVE_AS_SPECIFIED
```

A unique survivor receives **relative discriminatory status only**. It does not become a confirmed fundamental grammar and must face a later genuinely prospective test before stronger credit.

## Sequential-replacement firewall

During the common-target experiment:

```text
NO_NEW_DAG_VARIANTS
NO_NEW_SEMANTIC_ROLE_PERMUTATIONS
NO_SCOPE_NARROWING
NO_REPLACEMENT_CANDIDATE_AFTER_REJECTION
NO_NEW_TARGET_WITHIN_SAME_FAMILY_RESULT
```

After the common-target result is canonically adjudicated, any next candidate generation or target is a new separately preregistered operation.

## Stopping rule

This protocol authorizes **one common target** for the frozen five-candidate family.

The empirical sequence is:

```text
FREEZE_FAMILY_PROTOCOL
-> DISCOVER_AND_FREEZE_ONE_NEW_COMMON_TARGET
-> FREEZE_TARGET_SPECIFIC_STATISTICAL_AND_IMPLEMENTATION_PREREGISTRATION
-> DATA_CUSTODY
-> EXECUTE_ALL_FIVE_TESTS_ON_SAME_FROZEN_DATA
-> FAMILY_RESULT_ADJUDICATION
-> STOP
```

No second target is automatically authorized by survival or failure.

## Outcome space for this protocol gate

```text
A = COMMON_TARGET_FIVE_CANDIDATE_MULTIPLICITY_PROTOCOL_QUALIFIES__TARGET_DISCOVERY_MAY_BE_SEPARATELY_OPENED

B = MULTIPLICITY_OR_CALIBRATION_ARCHITECTURE_INADEQUATE__REVISE_BEFORE_TARGET_DISCOVERY

C = PREVIOUS_TARGET_DISCOVERY_CONTAMINATION_PREVENTS_ANY_GENUINELY_PROSPECTIVE_NEW_TARGET_ROUTE

D = SPECIFIC_INFORMATION_GAP_BLOCKS_PROTOCOL
```

## Required outputs

```text
governance/PGH1_POST_KP_COMMON_TARGET_MULTI_CANDIDATE_MULTIPLICITY_PROTOCOL_0_1_0.md
audits/PGH1_POST_KP_COMMON_TARGET_MULTI_CANDIDATE_MULTIPLICITY_PROTOCOL_GATE_0_1_0.md
handoffs/PGH1_POST_KP_COMMON_TARGET_MULTI_CANDIDATE_MULTIPLICITY_PROTOCOL_GATE_HANDOFF_0_1_0.md
```

## Commit topology

```text
COMMIT_1 = PREREGISTRATION_ONLY
COMMIT_2 = QUALIFIED_PROTOCOL_AUDIT_AND_HANDOFF
EXACT_COMMITS = 2
```

## Stop boundary

```text
STOP_BEFORE_TARGET_DISCOVERY
STOP_BEFORE_TARGET_METADATA_SEARCH
STOP_BEFORE_EMPIRICAL_DATA
STOP_BEFORE_TARGET_SPECIFIC_STATISTICAL_PREREGISTRATION
```
