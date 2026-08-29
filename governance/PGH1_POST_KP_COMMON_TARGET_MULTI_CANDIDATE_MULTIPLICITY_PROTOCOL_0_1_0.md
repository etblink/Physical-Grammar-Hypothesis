# PGH-OBJ-0047 — Post-Kp Common-Target Multi-Candidate Multiplicity Protocol 0.1.0

```text
OBJECT_ID = PGH-OBJ-0047
STATUS = QUALIFIED_PRE_TARGET_EMPIRICAL_FAMILY_PROTOCOL
DECLARING_OPERATION = PGH-OP-0084
FAMILY = [PGH-OBJ-0041,PGH-OBJ-0042,PGH-OBJ-0043,PGH-OBJ-0044,PGH-OBJ-0045]
FAMILY_SIZE = 5
TARGET = NONE
FCP_EFFECT = NONE
```

## Frozen hypotheses

```text
H1: A ⟂ C
H2: A ⟂ B | C
H3: A ⟂ B
H4: B ⟂ C | A
H5: B ⟂ C
```

The five hypotheses are frozen as one empirical family. No candidate may be added, removed or replaced after target discovery begins.

## Common target

One newly discovered target must confront all five candidates.

The target must provide repeated jointly indexable finite records with objective roles:

```text
A = EARLIEST_OR_UPSTREAM
B = INTERMEDIATE
C = LATEST_OR_DOWNSTREAM
```

The discovery operation must use candidate-outcome-neutral metadata only.

## Prior-discovery quarantine

Every target recorded in the pre-Kp first-target discovery ledger is ineligible for first positive post-Kp successor credit.

This quarantine is broader than the known Kp result itself. The reason is procedural: the successor family was frozen after those target identities had already been discovered.

A later target-discovery operation must bind the old ledger and exclude all of its entries from primary-family target selection.

## Primary statistics

For H1, H3 and H5:

\[
G^2=2N I_{nat}(X;Y).
\]

For H2 and H4:

\[
G^2=2N I_{nat}(X;Y\mid Z).
\]

Descriptive effect sizes may accompany `G²` but cannot change the verdict.

## Two-calibration requirement

After target freeze but before data materialization, a target-specific preregistration must freeze two materially distinct calibration architectures for every candidate:

```text
CAL1 = nonparametric / conditional-randomization style null
CAL2 = parametric / process-bootstrap style null
```

The exact preservation structure is determined from target metadata and measurement architecture, never target dependence.

Every stochastic implementation detail required by `PGH-OBJ-0040` must be exact before data access.

## Familywise error control

```text
FAMILY_ALPHA = 0.01
NUMBER_OF_PRIMARY_HYPOTHESES = 5
PROCEDURE = HOLM_STEP_DOWN
```

Holm correction is applied independently to the five p-values from CAL1 and to the five p-values from CAL2.

For a calibration with ordered p-values

\[
p_{(1)}\le\dots\le p_{(5)},
\]

reject sequentially while

\[
p_{(k)}\le \frac{0.01}{6-k}.
\]

Stop at the first nonrejection; all remaining hypotheses are nonrejected for that calibration.

No raw/unadjusted p-value alone can refute a candidate.

## Candidate verdict

For candidate `i`:

```text
IF HOLM_REJECT_CAL1_i AND HOLM_REJECT_CAL2_i:
    REFUTED_ON_COMMON_TARGET

IF NOT HOLM_REJECT_CAL1_i AND NOT HOLM_REJECT_CAL2_i:
    SURVIVES_COMMON_TARGET_TEST

OTHERWISE:
    INCONCLUSIVE_CALIBRATION_DISAGREEMENT
```

Survival is not confirmation.

## Family verdict

```text
ALL_5_REFUTED
    -> CURRENT_FIVE_CANDIDATE_SUCCESSOR_FAMILY_REFUTED_AT_COMMON_TARGET

EXACTLY_1_SURVIVES_AND_0_INCONCLUSIVE
    -> UNIQUE_SURVIVOR_AT_THIS_TARGET__RELATIVE_DISCRIMINATION_ONLY

2_TO_5_SURVIVE_AND_0_INCONCLUSIVE
    -> PLURALITY_SURVIVES_COMMON_TARGET

ANY_INCONCLUSIVE
    -> FAMILY_RESULT_INCONCLUSIVE_IN_RELEVANT_PART
```

No family-level outcome confirms strong PGH.

## Technical-failure rule

Custody, parser, support, preprocessing, calibration or reproducibility failure produces an inconclusive verdict for the affected scope. Technical failure cannot count as evidence for another candidate.

## One-target stopping rule

This protocol covers exactly one new common target.

After the target result is adjudicated:

```text
NO_AUTOMATIC_SECOND_TARGET
NO_AUTOMATIC_NEW_DAG
NO_FAILED_CANDIDATE_REPLACEMENT
NO_SCOPE_NARROWING
NO_ROLE_REASSIGNMENT
```

Any continuation is a new preregistered operation.

## Exact sequence

```text
FAMILY_PROTOCOL_FROZEN
-> NEW_COMMON_TARGET_DISCOVERY_AND_FREEZE
-> TARGET_SPECIFIC_ANALYSIS_PREREGISTRATION
-> DATA_CUSTODY
-> FIVE_CANDIDATE_COMMON_DATA_EXECUTION
-> FAMILY_RESULT_ADJUDICATION
-> STOP
```
