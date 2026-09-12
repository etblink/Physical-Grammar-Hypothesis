# D1 Apparatus Realization and Target-Freeze Checklist 0.1.0

Status: `TEMPLATE__NOT_EXECUTED`

This checklist becomes executable only in a separately governed `APPARATUS_REALIZATION_AND_TARGET_FREEZE` operation after the required physical hardware is in hand. Checking boxes in this template now has no scientific effect.

## Gate A — physical identity

- [ ] Confirm one physically common two-position actuator mechanically controls three distinct contact poles.
- [ ] Record apparatus name and version.
- [ ] Record switch manufacturer if available.
- [ ] Record switch model, or a unique physical description if no model is available.
- [ ] Bind serial number; if none exists, create a stable photo/physical identity record.
- [ ] Bind logger/acquisition-device identity.
- [ ] Bind exact acquisition channel identifiers.
- [ ] Confirm each acquisition channel receives state from its own physical contact pole.
- [ ] Confirm no one physical contact is split into three software fields.
- [ ] Confirm no recorded GPIO/input value is copied into another channel.
- [ ] Record wiring manifest before any response trial.

Failure of any item above stops target freeze.

## Gate B — channel role freeze

Before the first response trial:

1. list the three exact channel identifiers;
2. sort them by Unicode code-point lexical order;
3. assign `A = first`, `B = second`, `C = third`;
4. commit this assignment before response data exist.

No post-data permutation is allowed.

## Gate C — physical detent semantics

- [ ] Label the two stable mechanical detents `ACTUATOR_POSITION_0` and `ACTUATOR_POSITION_1` by stable physical identity only.
- [ ] Do not define either detent using observed A/B/C behavior.
- [ ] Record the identity method in the apparatus manifest.

## Gate D — acquisition protocol freeze

Default inherited protocol:

```text
TRIAL_COUNT = 512
ODD_TRIALS = ACTUATOR_POSITION_0
EVEN_TRIALS = ACTUATOR_POSITION_1
SETTLE_INTERVAL_MS = 1000
SAMPLE_COUNT_PER_TRIAL = 1 joint sample
RAW_ALPHABET_PER_CHANNEL = OPEN | CLOSED
```

- [ ] Accept the 1000 ms settle interval; OR
- [ ] Prospectively replace it before target freeze with a documented non-response-based engineering reason.
- [ ] Freeze the exact acquisition timestamp source/format.
- [ ] Freeze interface schema version.
- [ ] Freeze validity-rule version.

No timing or validity rule may be revised in response to observed channel agreement/disagreement.

## Gate E — validity semantics

Allowed top-level validity classes:

```text
VALID
MISSING_CHANNEL_1
MISSING_CHANNEL_2
MISSING_CHANNEL_3
ACQUISITION_FAILURE
TIMING_FAILURE
```

- [ ] Confirm A/B/C disagreement alone is never invalid.
- [ ] Confirm a contact state opposite the commanded actuator position alone is never invalid.
- [ ] Confirm missing channels remain missing and are never coerced to `OPEN` or `CLOSED`.
- [ ] Document any one-to-one refinement before response data exist.

## Gate F — custody freeze

Before the first response trial, freeze paths for:

```text
raw_record.csv
apparatus_manifest.json
protocol_manifest.json
```

- [ ] Raw record is append-only during the run.
- [ ] No response row will be manually edited after capture.
- [ ] SHA-256 is the frozen hash algorithm.
- [ ] Public repository path or equivalent auditable custody path is bound.
- [ ] Corrections, if ever needed, will be separately versioned while retaining the original.

## Gate G — target identity

Only after Gates A-F pass:

- [ ] Assign the next available target identifier under the separately governed operation.
- [ ] Bind the exact apparatus/interface identity to that target.
- [ ] Confirm no response trials have yet occurred.

This readiness package intentionally leaves `TGT-047` unassigned.

## Gate H — analysis firewall

After target freeze but before the first response trial:

- [ ] Open a separate negative-only analysis preregistration operation.
- [ ] Freeze the finite-sample `T_ind` decision functional and all implementation details required for deterministic replay.
- [ ] Freeze software/runtime/PRNG details if simulation is used.
- [ ] Freeze exclusion/missingness treatment without inspecting response values.
- [ ] Canonically commit the analysis preregistration.

If analysis preregistration is incomplete, **do not run physical trials**.

## Gate I — pre-run final stop/go

Immediately before first response trial, verify:

```text
APPARATUS_BOUND = YES
TARGET_FREEZE_CANONICAL = YES
ANALYSIS_PREREGISTRATION_CANONICAL = YES
RAW_RECORD_EMPTY_EXCEPT_HEADER = YES
CUSTODY_PATH_FROZEN = YES
```

If any value is `NO`, stop.

## Post-capture custody only

After the final trial:

1. close capture;
2. do not edit rows;
3. run structural validator in final mode;
4. compute SHA-256 of raw record and both manifests;
5. commit exact raw bytes and hashes;
6. only then execute the separately preregistered analysis.

This checklist never itself awards empirical support or refutation.