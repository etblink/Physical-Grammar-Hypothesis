#!/usr/bin/env python3
"""
Structural/custody validator for the PGH-1 D1 experiment readiness package.

This program deliberately performs NO scientific test, null simulation,
p-value calculation, or empirical verdict. It only validates the frozen
capture schema, manifests, schedule, missingness/validity semantics, and
custody hashes.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from pathlib import Path

REQUIRED_COLUMNS = [
    "TRIAL_ID",
    "COMMANDED_POSITION",
    "CHANNEL_1_STATE",
    "CHANNEL_2_STATE",
    "CHANNEL_3_STATE",
    "VALIDITY_CODE",
    "ACQUISITION_TIMESTAMP",
    "INTERFACE_VERSION",
]
POSITIONS = {"ACTUATOR_POSITION_0", "ACTUATOR_POSITION_1"}
CHANNEL_STATES = {"OPEN", "CLOSED"}
VALIDITY_CODES = {
    "VALID",
    "MISSING_CHANNEL_1",
    "MISSING_CHANNEL_2",
    "MISSING_CHANNEL_3",
    "ACQUISITION_FAILURE",
    "TIMING_FAILURE",
}
MISSING_CODE_TO_INDEX = {
    "MISSING_CHANNEL_1": 0,
    "MISSING_CHANNEL_2": 1,
    "MISSING_CHANNEL_3": 2,
}

class ValidationError(Exception):
    pass

def fail(message: str) -> None:
    raise ValidationError(message)

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def load_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"{path}: invalid JSON: {exc}")
    if not isinstance(value, dict):
        fail(f"{path}: top-level JSON must be an object")
    return value

def contains_unbound(value) -> bool:
    if isinstance(value, dict):
        return any(contains_unbound(v) for v in value.values())
    if isinstance(value, list):
        return any(contains_unbound(v) for v in value)
    return isinstance(value, str) and value == "UNBOUND"

def validate_apparatus(m: dict, mode: str) -> None:
    if m.get("candidate_package") != "PGH-OBJ-0052":
        fail("apparatus manifest candidate_package must be PGH-OBJ-0052")
    if m.get("interface_class") != "THREE_POLE_TWO_POSITION_MECHANICALLY_GANGED_DRY_CONTACT_INTERFACE":
        fail("apparatus manifest interface_class mismatch")
    if m.get("common_state") != "ONE_MECHANICALLY_SHARED_TWO_POSITION_ACTUATOR":
        fail("apparatus manifest common_state mismatch")
    if m.get("hash_algorithm") != "SHA-256":
        fail("apparatus manifest hash_algorithm must be SHA-256")

    channels = m.get("channel_identifiers")
    if not isinstance(channels, list) or len(channels) != 3:
        fail("apparatus manifest must contain exactly three channel_identifiers")

    derivation = m.get("software_derivation")
    if not isinstance(derivation, dict):
        fail("apparatus manifest software_derivation must be an object")
    forbidden = [
        "one_contact_split_to_three_fields",
        "one_input_value_copied_three_times",
        "derived_boolean_columns",
    ]
    for key in forbidden:
        if derivation.get(key) is not False:
            fail(f"apparatus manifest forbids {key}; value must be false")

    wiring = m.get("wiring_manifest")
    if not isinstance(wiring, list) or len(wiring) != 3:
        fail("apparatus manifest wiring_manifest must have three entries")

    if mode == "final":
        if m.get("status") != "BOUND_BEFORE_RESPONSE_DATA":
            fail("final apparatus manifest status must be BOUND_BEFORE_RESPONSE_DATA")
        if contains_unbound(m):
            fail("final apparatus manifest contains UNBOUND")
        if len(set(channels)) != 3:
            fail("final apparatus manifest channel identifiers must be unique")
        if m.get("target_id") in (None, "", "UNBOUND") or str(m.get("target_id")).startswith("SYNTHETIC_"):
            fail("final apparatus manifest requires a separately bound real target_id")
        if m.get("bound_before_response_data") is not True:
            fail("final apparatus manifest must affirm bound_before_response_data=true")
        detents = m.get("physical_detents")
        if not isinstance(detents, dict) or detents.get("identity_is_response_independent") is not True:
            fail("final apparatus detent identities must be response-independent")
    else:
        if m.get("status") != "SYNTHETIC":
            fail("synthetic apparatus manifest status must be SYNTHETIC")
        if not str(m.get("target_id", "")).startswith("SYNTHETIC_"):
            fail("synthetic apparatus target_id must start SYNTHETIC_")
        if any(not str(x).startswith("SYNTH_") for x in channels):
            fail("synthetic channel identifiers must start SYNTH_")

def validate_protocol(p: dict, mode: str) -> int:
    if p.get("candidate_package") != "PGH-OBJ-0052":
        fail("protocol candidate_package must be PGH-OBJ-0052")
    if p.get("sample_count_per_trial") != 1:
        fail("sample_count_per_trial must equal 1")
    settle = p.get("settle_interval_ms")
    if not isinstance(settle, int) or settle <= 0:
        fail("settle_interval_ms must be a positive integer")
    if p.get("channel_alphabet") != ["OPEN", "CLOSED"]:
        fail("channel_alphabet must be exactly [OPEN, CLOSED]")
    if set(p.get("validity_codes", [])) != VALIDITY_CODES or len(p.get("validity_codes", [])) != len(VALIDITY_CODES):
        fail("protocol validity_codes must be exactly the frozen six codes")
    if p.get("disagreement_is_invalid") is not False:
        fail("disagreement_is_invalid must be false")
    if p.get("opposite_commanded_position_is_invalid") is not False:
        fail("opposite_commanded_position_is_invalid must be false")
    if p.get("missing_values_coerced_to_channel_states") is not False:
        fail("missing_values_coerced_to_channel_states must be false")
    if p.get("append_only_during_capture") is not True:
        fail("append_only_during_capture must be true")
    if p.get("manual_row_edits_after_capture") is not False:
        fail("manual_row_edits_after_capture must be false")
    if p.get("hash_algorithm") != "SHA-256":
        fail("protocol hash_algorithm must be SHA-256")

    schedule = p.get("schedule")
    if not isinstance(schedule, dict):
        fail("protocol schedule must be an object")
    if schedule.get("odd_trials") != "ACTUATOR_POSITION_0":
        fail("odd trials must command ACTUATOR_POSITION_0")
    if schedule.get("even_trials") != "ACTUATOR_POSITION_1":
        fail("even trials must command ACTUATOR_POSITION_1")
    if schedule.get("adaptive_control") is not False:
        fail("adaptive_control must be false")

    count = p.get("trial_count")
    if not isinstance(count, int):
        fail("trial_count must be integer")
    if mode == "final":
        if p.get("status") != "BOUND_BEFORE_RESPONSE_DATA":
            fail("final protocol status must be BOUND_BEFORE_RESPONSE_DATA")
        if count != 512:
            fail("final protocol trial_count must equal 512")
        if contains_unbound(p):
            fail("final protocol contains UNBOUND")
        if p.get("physical_trials_authorized") is not True:
            fail("final protocol requires physical_trials_authorized=true")
        if not p.get("target_freeze_commit") or not p.get("analysis_preregistration_commit"):
            fail("final protocol requires target freeze and analysis preregistration commits")
    else:
        if p.get("status") != "SYNTHETIC":
            fail("synthetic protocol status must be SYNTHETIC")
        if not (1 <= count <= 64):
            fail("synthetic trial_count must be between 1 and 64")
        if p.get("physical_trials_authorized") is not False:
            fail("synthetic physical_trials_authorized must be false")
        if not str(p.get("target_id", "")).startswith("SYNTHETIC_"):
            fail("synthetic target_id must start SYNTHETIC_")
    return count

def validate_rows(path: Path, expected_count: int, mode: str) -> None:
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != REQUIRED_COLUMNS:
            fail(f"raw record columns/order mismatch: {reader.fieldnames!r}")
        rows = list(reader)

    if len(rows) != expected_count:
        fail(f"row count {len(rows)} does not match protocol trial_count {expected_count}")

    versions = set()
    for index, row in enumerate(rows, start=1):
        try:
            trial_id = int(row["TRIAL_ID"])
        except Exception:
            fail(f"row {index}: TRIAL_ID must be integer")
        if trial_id != index:
            fail(f"row {index}: TRIAL_ID must be consecutive starting at 1")

        expected_position = "ACTUATOR_POSITION_0" if trial_id % 2 == 1 else "ACTUATOR_POSITION_1"
        if row["COMMANDED_POSITION"] != expected_position:
            fail(f"row {index}: commanded position violates frozen odd/even schedule")

        validity = row["VALIDITY_CODE"]
        if validity not in VALIDITY_CODES:
            fail(f"row {index}: invalid VALIDITY_CODE {validity!r}")

        states = [row["CHANNEL_1_STATE"], row["CHANNEL_2_STATE"], row["CHANNEL_3_STATE"]]
        for state in states:
            if state not in CHANNEL_STATES and state != "":
                fail(f"row {index}: channel state must be OPEN, CLOSED, or empty for missingness")

        if validity == "VALID":
            if any(state == "" for state in states):
                fail(f"row {index}: VALID row may not contain missing channel values")
        elif validity in MISSING_CODE_TO_INDEX:
            missing_i = MISSING_CODE_TO_INDEX[validity]
            if states[missing_i] != "":
                fail(f"row {index}: {validity} requires its named channel to be empty")
            for i, state in enumerate(states):
                if i != missing_i and state == "":
                    fail(f"row {index}: {validity} may name only one missing channel")
        # Acquisition/timing failure rows may contain any combination of native
        # readings and missing readings. Their invalidity must derive from the
        # independently audited acquisition/timing failure, not response pattern.

        timestamp = row["ACQUISITION_TIMESTAMP"]
        if not timestamp:
            fail(f"row {index}: ACQUISITION_TIMESTAMP is required")

        version = row["INTERFACE_VERSION"]
        if not version:
            fail(f"row {index}: INTERFACE_VERSION is required")
        versions.add(version)

        if mode == "synthetic":
            if not version.startswith("SYNTHETIC_"):
                fail(f"row {index}: synthetic INTERFACE_VERSION must start SYNTHETIC_")
            if not timestamp.startswith("0001-01-01T"):
                fail(f"row {index}: synthetic timestamp must use reserved 0001-01-01 date domain")
        else:
            if version.startswith("SYNTHETIC_"):
                fail(f"row {index}: final capture may not use synthetic interface version")
            if timestamp.startswith("0001-01-01T"):
                fail(f"row {index}: final capture may not use synthetic date domain")

    if len(versions) != 1:
        fail("INTERFACE_VERSION must be constant across the capture")

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["synthetic", "final"], required=True)
    parser.add_argument("--raw", type=Path, required=True)
    parser.add_argument("--apparatus", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    args = parser.parse_args()

    try:
        apparatus = load_json(args.apparatus)
        protocol = load_json(args.protocol)
        validate_apparatus(apparatus, args.mode)
        count = validate_protocol(protocol, args.mode)
        validate_rows(args.raw, count, args.mode)
    except ValidationError as exc:
        print("D1_STRUCTURAL_VALIDATION=FAIL")
        print(f"REASON={exc}")
        print("SCIENTIFIC_STATISTIC_COMPUTED=NO")
        print("SCIENTIFIC_VERDICT=NONE")
        return 2

    print("D1_STRUCTURAL_VALIDATION=PASS")
    print(f"MODE={args.mode}")
    print(f"ROW_COUNT={count}")
    print(f"RAW_SHA256={sha256(args.raw)}")
    print(f"APPARATUS_MANIFEST_SHA256={sha256(args.apparatus)}")
    print(f"PROTOCOL_MANIFEST_SHA256={sha256(args.protocol)}")
    print("SCIENTIFIC_STATISTIC_COMPUTED=NO")
    print("SCIENTIFIC_VERDICT=NONE")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
