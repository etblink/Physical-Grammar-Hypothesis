# PGH-1 D1 Experiment Readiness Package

Status: `PRE_DATA_INFRASTRUCTURE_ONLY`

This directory prepares the already-qualified D1 mechanically ganged three-pole dry-contact interface for a later, separately governed physical realization. Nothing in this directory is empirical evidence.

## Controlling sequence

```text
CURRENT STATE
  D1 design class qualified
  actual apparatus not bound
  target not assigned
  response data absent

LATER, SEPARATELY GOVERNED
  1. apparatus realization + target freeze
  2. negative-only analysis preregistration
  3. only then physical trial execution
  4. immutable custody + qualified analysis
```

Do not create real response rows before steps 1 and 2 are canonical.

## Files

- `APPARATUS_REALIZATION_CHECKLIST_0_1_0.md` — human operator gate sequence.
- `apparatus_manifest.template.json` — fields that must be bound to the actual hardware before target freeze.
- `protocol_manifest.template.json` — frozen acquisition protocol fields.
- `raw_record.schema.json` — machine-readable structural contract for capture rows.
- `validate_d1_capture.py` — standard-library-only structural/custody validator. It produces no scientific verdict.
- `synthetic/dry_run_valid.csv` — deliberately mixed non-empirical fixture.
- `synthetic/apparatus_manifest.synthetic.json` — synthetic apparatus fixture.
- `synthetic/protocol_manifest.synthetic.json` — synthetic protocol fixture.

## Scientific firewall

The validator checks only structural facts such as required fields, native channel values, validity-code semantics, alternating schedule, count, manifest completeness, and SHA-256. It does **not** compute a PGH test statistic, choose a null, estimate a p-value, or decide whether `PGH-OBJ-0052` survives or fails.

Channel disagreement is valid response content. It is never an apparatus-failure rule merely because the three channel states differ.

## Real-capture custody shape

The later real operation should create a fresh immutable capture directory, not overwrite the synthetic directory. At minimum it should contain:

```text
raw_record.csv
apparatus_manifest.json
protocol_manifest.json
```

After capture closes, compute and record SHA-256 for all three files, commit the exact bytes without manual row edits, and retain any correction as a new version while preserving the original.

## No target assignment here

`TGT-047` remains unassigned. Templates use `UNBOUND` placeholders. Replacing those placeholders with real hardware identities is part of the future apparatus-realization operation, not this readiness package.