# PGH-1 Empirical Instantiation Target Selection Preregistration Gate — Audit 0.1.0

## Identity

```text
OPERATION_ID = PGH1_EMPIRICAL_INSTANTIATION_TARGET_SELECTION_PREREGISTRATION_GATE
REGISTRY_ID = PGH-OP-0062
PREREGISTRATION_COMMIT = 1a07bc4dd0090d5dd70646c71fae05230e890703
CANONICAL_BASE = d7f82ad8a7e5bb2b5a1a397002af42643ee50f65
```

## Outcome

```text
OUTCOME = A
TARGET_SELECTION_PROTOCOL = QUALIFIED
TARGET_DISCOVERY = NOT_STARTED
EMPIRICAL_TARGET = NONE
```

## Audit question

Can the first empirical target be selected without using the very dependence relation that `PGH-GRAM-0008` is intended to test?

## Result

Yes, at protocol-design scope.

A candidate can be screened and ranked using only physical-record eligibility, objective acquisition/process/spatial order, joint event identity, finite-alphabet status, event-count metadata, access/auditability, preprocessing burden, measurement/selection documentation, and contamination status.

None of these requires inspecting whether

\[
\mathcal A\perp\mathcal C\mid\mathcal B.
\]

## Role-assignment audit

The protocol prevents data-driven permutation by requiring role order to come from declared metadata:

```text
A = earliest/upstream
B = intermediate
C = latest/downstream
```

Candidates without objective ordering are excluded from the first test rather than assigned flexibly.

## Discretization audit

Native finite records are preferred.

Continuous targets are allowed only if the discretization can later be frozen from instrumentation, external calibration, standards, or physically meaningful thresholds before value inspection.

Optimizing bins for the target dependence result is explicitly forbidden.

## Ranking audit

The ten ranking criteria concern measurement quality, data architecture, support, preprocessing, reproducibility, and archival stability.

No target-dependence statistic is included.

The tie-break rule is fully preregistered and target-result independent.

## Contamination audit

The protocol distinguishes unavoidable general domain knowledge from disclosure of the exact target result.

A `C3` candidate cannot receive first-test predictive credit.

This prevents publication-history leakage from being mistaken for a prospective prediction.

## Search-query audit

Future discovery is forbidden from using target-result phrases to find candidates.

Candidate identification must occur before contamination checking for the exact target relation.

## Statistical boundary audit

The protocol does not authorize exploratory dependence analysis after target selection.

A separate statistical preregistration remains mandatory before any target-dependent computation.

## Preserved failure

```text
PGH-FAIL-0034 = EMPIRICAL_TARGET_SELECTION_RESULT_LEAKAGE
```

## Sequencing consequence

A separate metadata-only target discovery/freeze operation is justified.

```text
NEXT = PGH1_EMPIRICAL_INSTANTIATION_TARGET_DISCOVERY_AND_FREEZE
```

## Hard-stop verification

```text
EXTERNAL_TARGET_SEARCH_PERFORMED = NO
CANDIDATE_DATASET_NAMED = NO
EMPIRICAL_EVENT_VALUES_INSPECTED = NO
TARGET_DEPENDENCE_INSPECTED = NO
STATISTICAL_THRESHOLD_SELECTED = NO
FCP_CHANGED = NO
```
