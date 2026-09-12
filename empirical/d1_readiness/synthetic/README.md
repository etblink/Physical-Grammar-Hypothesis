# Synthetic D1 Dry-Run Fixtures

Status: `NON_EMPIRICAL__STRUCTURAL_TEST_ONLY`

These files are synthetic parser/custody fixtures. They are not measurements, predictions, simulations of the eventual apparatus, or evidence for/against PGH.

The fixture intentionally mixes:

- all-three-channel agreement;
- valid three-channel disagreement;
- each single-channel missingness code;
- acquisition failure;
- timing failure.

This mixture is deliberate: the dry run must prove that the infrastructure accepts lawful response diversity rather than privileging the expected common-bit direction.

Reserved synthetic markers:

```text
TARGET_ID starts SYNTHETIC_
CHANNEL_IDENTIFIERS start SYNTH_
INTERFACE_VERSION starts SYNTHETIC_
ACQUISITION_TIMESTAMP date = 0001-01-01
```

Reference command from repository root:

```text
python empirical/d1_readiness/validate_d1_capture.py \
  --mode synthetic \
  --raw empirical/d1_readiness/synthetic/dry_run_valid.csv \
  --apparatus empirical/d1_readiness/synthetic/apparatus_manifest.synthetic.json \
  --protocol empirical/d1_readiness/synthetic/protocol_manifest.synthetic.json
```

Expected scientific output is always:

```text
SCIENTIFIC_STATISTIC_COMPUTED=NO
SCIENTIFIC_VERDICT=NONE
```

A deliberately malformed fixture should fail structurally; no malformed fixture is retained here because it is generated ephemerally by validation tests.