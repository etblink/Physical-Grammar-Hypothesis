#!/usr/bin/env python3
"""PGH derived-navigation builder and checker.

No third-party dependencies are required.

Authority rule:
    Git -> provenance authority
    canonical Markdown -> research/governance authority
    structured metadata -> derived navigation only
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parent.parent

INDEX_PATH = ROOT / "meta" / "PGH_CANONICAL_INDEX.json"
OPS_PATH = ROOT / "meta" / "PGH_OPERATION_REGISTRY.jsonl"
OBJECTS_PATH = ROOT / "meta" / "PGH_RESEARCH_OBJECT_REGISTRY.jsonl"
QUESTIONS_PATH = ROOT / "meta" / "PGH_OPEN_QUESTION_REGISTRY.jsonl"
SCHEMA_PATH = ROOT / "meta" / "PGH_NAVIGATION_SCHEMA_0_1_0.json"
STATE_PATH = ROOT / "CURRENT_STATE.md"

STATE_BEGIN = "<!-- PGH_CURRENT_STATE_CAPSULE_BEGIN -->"
STATE_END = "<!-- PGH_CURRENT_STATE_CAPSULE_END -->"
HANDOFF_BEGIN = "<!-- PGH_HANDOFF_CAPSULE_BEGIN -->"
HANDOFF_END = "<!-- PGH_HANDOFF_CAPSULE_END -->"

HEX40 = re.compile(r"^[0-9a-f]{40}$")
OP_ID = re.compile(r"^PGH-OP-[0-9]{4}$")
QUESTION_ID = re.compile(r"^PGH-Q-[0-9]{4}$")
OBJECT_ID = re.compile(r"^PGH-(?:OBJ|GRAM|DER|FAIL)-[0-9]{4}$")

OP_STATUSES = {
    "RECOMMENDED_NOT_STARTED",
    "AUTHORIZED_NOT_STARTED",
    "IN_PROGRESS",
    "QUALIFIED_LOCAL",
    "CANONICALLY_COMPLETE",
    "FAILED",
    "SUPERSEDED",
}
QUESTION_STATUSES = {
    "OPEN",
    "DEFERRED",
    "RESOLVED",
    "CLOSED_AS_ILL_POSED",
    "SUPERSEDED",
}

REQUIRED_INDEX_KEYS = {
    "schema_version",
    "authority",
    "indexed_research_baseline_commit",
    "indexed_research_baseline_tree",
    "current_phase",
    "latest_completed_operation",
    "current_handoff",
    "canonical_state",
    "canonical_hypothesis",
    "active_candidate_grammar",
    "counts",
    "next_recommended_operation",
    "next_operation_authorized",
    "source_bound_status",
    "fcp_relationship",
}


class CheckFailure(RuntimeError):
    pass


def fail(message: str) -> None:
    raise CheckFailure(message)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def require_path(path_text: str, context: str) -> None:
    path = ROOT / path_text
    if not path.exists():
        fail(f"{context}: missing path: {path_text}")


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"{rel(path)}: invalid JSON: {exc}")


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except Exception as exc:
        fail(f"{rel(path)}: cannot read: {exc}")
    for line_no, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except Exception as exc:
            fail(f"{rel(path)}:{line_no}: invalid JSONL record: {exc}")
        if not isinstance(value, dict):
            fail(f"{rel(path)}:{line_no}: record is not a JSON object")
        records.append(value)
    return records


def require_unique(records: Iterable[dict[str, Any]], key: str, source: Path) -> set[str]:
    seen: set[str] = set()
    for record in records:
        value = record.get(key)
        if not isinstance(value, str) or not value:
            fail(f"{rel(source)}: missing/non-string {key}")
        if value in seen:
            fail(f"{rel(source)}: duplicate {key}: {value}")
        seen.add(value)
    return seen


def extract_capsule(path: Path, begin: str, end: str) -> dict[str, Any]:
    # Python's text mode already accepts CRLF; explicit normalization also makes
    # the intended portability rule obvious.
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
    if text.count(begin) != 1 or text.count(end) != 1:
        fail(f"{rel(path)}: expected exactly one capsule marker pair")
    start = text.index(begin) + len(begin)
    stop = text.index(end, start)
    inside = text[start:stop]
    matches = re.findall(r"```json\s*(\{.*?\})\s*```", inside, flags=re.DOTALL)
    if len(matches) != 1:
        fail(f"{rel(path)}: expected exactly one fenced JSON object inside capsule")
    try:
        value = json.loads(matches[0])
    except Exception as exc:
        fail(f"{rel(path)}: invalid capsule JSON: {exc}")
    if not isinstance(value, dict):
        fail(f"{rel(path)}: capsule is not a JSON object")
    return value


def check_machine_file_lf() -> None:
    candidates = [
        INDEX_PATH,
        OPS_PATH,
        OBJECTS_PATH,
        QUESTIONS_PATH,
        SCHEMA_PATH,
        ROOT / "tools" / "pgh_navigation.py",
    ]
    for path in candidates:
        data = path.read_bytes()
        if b"\r\n" in data or b"\r" in data:
            fail(f"{rel(path)}: machine-readable file is not LF-only")


def validate_operations(records: list[dict[str, Any]]) -> tuple[set[str], dict[str, dict[str, Any]]]:
    registry_ids = require_unique(records, "registry_id", OPS_PATH)
    operation_ids = require_unique(records, "operation_id", OPS_PATH)
    by_operation: dict[str, dict[str, Any]] = {}
    for record in records:
        if not OP_ID.fullmatch(record["registry_id"]):
            fail(f"{rel(OPS_PATH)}: invalid registry_id: {record['registry_id']}")
        status = record.get("status")
        if status not in OP_STATUSES:
            fail(f"{rel(OPS_PATH)}: unrecognized operation status: {status}")
        if not isinstance(record.get("scientific_change"), bool):
            fail(f"{rel(OPS_PATH)}: scientific_change must be boolean for {record['operation_id']}")
        for field in ("inputs", "outputs"):
            if not isinstance(record.get(field), list) or not all(isinstance(x, str) for x in record[field]):
                fail(f"{rel(OPS_PATH)}: {field} must be a string array for {record['operation_id']}")
        if status == "CANONICALLY_COMPLETE":
            for output in record["outputs"]:
                require_path(output, f"completed operation {record['operation_id']}")
            handoff = record.get("handoff")
            if handoff is not None:
                if not isinstance(handoff, str):
                    fail(f"{rel(OPS_PATH)}: handoff must be string/null for {record['operation_id']}")
                require_path(handoff, f"completed operation {record['operation_id']}")
        by_operation[record["operation_id"]] = record
    return operation_ids, by_operation


def validate_objects(records: list[dict[str, Any]]) -> tuple[set[str], dict[str, dict[str, Any]]]:
    object_ids = require_unique(records, "object_id", OBJECTS_PATH)
    for object_id in object_ids:
        if not OBJECT_ID.fullmatch(object_id):
            fail(f"{rel(OBJECTS_PATH)}: invalid object_id: {object_id}")
    by_object = {record["object_id"]: record for record in records}
    for record in records:
        artifact = record.get("canonical_artifact")
        if artifact is not None:
            if not isinstance(artifact, str):
                fail(f"{rel(OBJECTS_PATH)}: canonical_artifact must be string/null for {record['object_id']}")
            require_path(artifact, f"research object {record['object_id']}")
        dependencies = record.get("dependencies")
        if not isinstance(dependencies, list) or not all(isinstance(x, str) for x in dependencies):
            fail(f"{rel(OBJECTS_PATH)}: dependencies must be string array for {record['object_id']}")
        for dependency in dependencies:
            if dependency not in object_ids:
                fail(f"{rel(OBJECTS_PATH)}: {record['object_id']} depends on unknown object {dependency}")
    return object_ids, by_object


def validate_questions(
    records: list[dict[str, Any]],
    operation_ids: set[str],
    object_ids: set[str],
) -> tuple[set[str], dict[str, dict[str, Any]]]:
    question_ids = require_unique(records, "question_id", QUESTIONS_PATH)
    by_question = {record["question_id"]: record for record in records}
    for record in records:
        qid = record["question_id"]
        if not QUESTION_ID.fullmatch(qid):
            fail(f"{rel(QUESTIONS_PATH)}: invalid question_id: {qid}")
        if record.get("status") not in QUESTION_STATUSES:
            fail(f"{rel(QUESTIONS_PATH)}: unrecognized status for {qid}: {record.get('status')}")
        created = record.get("created_by_operation")
        if created not in operation_ids:
            fail(f"{rel(QUESTIONS_PATH)}: {qid} references unknown operation {created}")
        related = record.get("related_objects")
        if not isinstance(related, list) or not all(isinstance(x, str) for x in related):
            fail(f"{rel(QUESTIONS_PATH)}: related_objects must be a string array for {qid}")
        for object_id in related:
            if object_id not in object_ids:
                fail(f"{rel(QUESTIONS_PATH)}: {qid} references unknown object {object_id}")
        resolution = record.get("resolution_artifact")
        if record["status"] == "RESOLVED" and not isinstance(resolution, str):
            fail(f"{rel(QUESTIONS_PATH)}: resolved question {qid} lacks resolution_artifact")
        if isinstance(resolution, str):
            require_path(resolution, f"resolved question {qid}")
    return question_ids, by_question


def validate_index(
    index: dict[str, Any],
    ops: list[dict[str, Any]],
    objects: list[dict[str, Any]],
    questions: list[dict[str, Any]],
    by_operation: dict[str, dict[str, Any]],
    by_object: dict[str, dict[str, Any]],
    by_question: dict[str, dict[str, Any]],
) -> None:
    if set(index) != REQUIRED_INDEX_KEYS:
        missing = sorted(REQUIRED_INDEX_KEYS - set(index))
        extra = sorted(set(index) - REQUIRED_INDEX_KEYS)
        fail(f"{rel(INDEX_PATH)}: key mismatch; missing={missing}, extra={extra}")
    if index["schema_version"] != "0.1.0":
        fail(f"{rel(INDEX_PATH)}: unsupported schema_version")
    if index["authority"] != "DERIVED_NAVIGATION_ONLY":
        fail(f"{rel(INDEX_PATH)}: authority must be DERIVED_NAVIGATION_ONLY")
    if not HEX40.fullmatch(index["indexed_research_baseline_commit"]):
        fail(f"{rel(INDEX_PATH)}: invalid baseline commit")
    if not HEX40.fullmatch(index["indexed_research_baseline_tree"]):
        fail(f"{rel(INDEX_PATH)}: invalid baseline tree")

    counts = index.get("counts")
    if not isinstance(counts, dict):
        fail(f"{rel(INDEX_PATH)}: counts must be object")
    expected = {
        "operation_records": len(ops),
        "research_object_records": len(objects),
        "open_question_records": len(questions),
        "open_questions": sum(q.get("status") == "OPEN" for q in questions),
    }
    if counts != expected:
        fail(f"{rel(INDEX_PATH)}: counts mismatch; expected={expected}, actual={counts}")

    latest = index["latest_completed_operation"]
    if latest not in by_operation or by_operation[latest]["status"] != "CANONICALLY_COMPLETE":
        fail(f"{rel(INDEX_PATH)}: latest_completed_operation is not canonically complete")

    grammar = index["active_candidate_grammar"]
    if grammar is not None and grammar not in by_object:
        fail(f"{rel(INDEX_PATH)}: unknown active_candidate_grammar: {grammar}")

    next_op = index["next_recommended_operation"]
    if next_op is not None and next_op not in by_operation:
        fail(f"{rel(INDEX_PATH)}: unknown next_recommended_operation: {next_op}")

    require_path(index["canonical_state"], "canonical index")
    require_path(index["canonical_hypothesis"], "canonical index")
    require_path(index["current_handoff"], "canonical index")

    state = extract_capsule(STATE_PATH, STATE_BEGIN, STATE_END)
    alignment = {
        "current_phase": "current_phase",
        "canonical_hypothesis": "canonical_hypothesis",
        "active_candidate_grammar": "active_candidate_grammar",
        "current_handoff": "current_handoff",
        "source_bound_status": "source_bound_status",
        "fcp_relationship": "fcp_relationship",
        "next_recommended_operation": "next_recommended_operation",
        "next_operation_authorized": "next_operation_authorized",
    }
    for index_key, state_key in alignment.items():
        if index[index_key] != state.get(state_key):
            fail(
                f"index/state mismatch for {index_key}: "
                f"index={index[index_key]!r}, state={state.get(state_key)!r}"
            )
    if state.get("open_question_count") != counts["open_questions"]:
        fail("CURRENT_STATE capsule open_question_count does not match registry")
    if not isinstance(state.get("do_not_assume"), list) or not state["do_not_assume"]:
        fail("CURRENT_STATE capsule requires nonempty do_not_assume")

    handoff_path = ROOT / index["current_handoff"]
    handoff = extract_capsule(handoff_path, HANDOFF_BEGIN, HANDOFF_END)
    required_handoff = {
        "capsule_schema_version",
        "operation_id",
        "status",
        "indexed_research_baseline_commit",
        "must_read",
        "outputs",
        "open_questions",
        "next_recommended_operation",
        "next_operation_authorized",
        "do_not_assume",
    }
    missing = required_handoff - set(handoff)
    if missing:
        fail(f"{rel(handoff_path)}: missing capsule keys: {sorted(missing)}")
    if handoff["capsule_schema_version"] != "0.1.0":
        fail(f"{rel(handoff_path)}: unsupported capsule schema")
    if handoff["operation_id"] != latest:
        fail(f"{rel(handoff_path)}: operation_id does not match latest completed operation")
    if handoff["indexed_research_baseline_commit"] != index["indexed_research_baseline_commit"]:
        fail(f"{rel(handoff_path)}: indexed baseline commit disagrees with index")
    if handoff["next_recommended_operation"] != next_op:
        fail(f"{rel(handoff_path)}: next operation disagrees with index")
    if handoff["next_operation_authorized"] != index["next_operation_authorized"]:
        fail(f"{rel(handoff_path)}: next-operation authorization disagrees with index")
    if not isinstance(handoff["do_not_assume"], list) or not handoff["do_not_assume"]:
        fail(f"{rel(handoff_path)}: do_not_assume must be nonempty")
    for field in ("must_read", "outputs"):
        if not isinstance(handoff[field], list) or not all(isinstance(x, str) for x in handoff[field]):
            fail(f"{rel(handoff_path)}: {field} must be a string array")
        for path_text in handoff[field]:
            require_path(path_text, f"{rel(handoff_path)} {field}")
    if not isinstance(handoff["open_questions"], list):
        fail(f"{rel(handoff_path)}: open_questions must be array")
    for qid in handoff["open_questions"]:
        if qid not in by_question:
            fail(f"{rel(handoff_path)}: unknown open question {qid}")
        if by_question[qid]["status"] not in {"OPEN", "DEFERRED"}:
            fail(f"{rel(handoff_path)}: non-open question listed in handoff: {qid}")


def run_check() -> None:
    required_core = [
        "README.md",
        "CURRENT_STATE.md",
        "HYPOTHESIS.md",
        "PRIMITIVES.md",
        "NONTRIVIALITY_TESTS.md",
        "RESEARCH_LOG.md",
        "meta/PGH_CANONICAL_INDEX.json",
        "meta/PGH_OPERATION_REGISTRY.jsonl",
        "meta/PGH_RESEARCH_OBJECT_REGISTRY.jsonl",
        "meta/PGH_OPEN_QUESTION_REGISTRY.jsonl",
        "meta/PGH_NAVIGATION_SCHEMA_0_1_0.json",
        "tools/pgh_navigation.py",
    ]
    for path_text in required_core:
        require_path(path_text, "core")

    # Parse schema even though validation is dependency-free/manual.
    schema = load_json(SCHEMA_PATH)
    if schema.get("$id") != "PGH_NAVIGATION_SCHEMA_0_1_0":
        fail(f"{rel(SCHEMA_PATH)}: unexpected schema id")

    ops = load_jsonl(OPS_PATH)
    objects = load_jsonl(OBJECTS_PATH)
    questions = load_jsonl(QUESTIONS_PATH)

    operation_ids, by_operation = validate_operations(ops)
    object_ids, by_object = validate_objects(objects)
    _, by_question = validate_questions(questions, operation_ids, object_ids)

    index = load_json(INDEX_PATH)
    if not isinstance(index, dict):
        fail(f"{rel(INDEX_PATH)}: index must be object")
    validate_index(index, ops, objects, questions, by_operation, by_object, by_question)
    check_machine_file_lf()

    print("PGH_NAVIGATION_CHECK=PASS")
    print(f"OPERATION_RECORD_COUNT={len(ops)}")
    print(f"RESEARCH_OBJECT_RECORD_COUNT={len(objects)}")
    print(f"OPEN_QUESTION_RECORD_COUNT={len(questions)}")
    print(f"OPEN_QUESTION_COUNT={sum(q.get('status') == 'OPEN' for q in questions)}")
    print(f"INDEXED_RESEARCH_BASELINE_COMMIT={index['indexed_research_baseline_commit']}")
    print(f"CURRENT_HANDOFF={index['current_handoff']}")
    print(f"NEXT_RECOMMENDED_OPERATION={index['next_recommended_operation']}")
    print(f"NEXT_OPERATION_AUTHORIZED={'YES' if index['next_operation_authorized'] else 'NO'}")


def git_tree_for(commit: str) -> str:
    try:
        completed = subprocess.run(
            ["git", "-C", str(ROOT), "rev-parse", f"{commit}^{{tree}}"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    except Exception as exc:
        fail(f"cannot resolve baseline tree for {commit}: {exc}")
    tree = completed.stdout.strip()
    if not HEX40.fullmatch(tree):
        fail(f"git returned invalid tree SHA for {commit}: {tree!r}")
    return tree


def build_index(baseline_commit: str) -> None:
    if not HEX40.fullmatch(baseline_commit):
        fail("--baseline-commit must be an exact 40-character lowercase Git SHA")

    ops = load_jsonl(OPS_PATH)
    objects = load_jsonl(OBJECTS_PATH)
    questions = load_jsonl(QUESTIONS_PATH)

    operation_ids, by_operation = validate_operations(ops)
    object_ids, by_object = validate_objects(objects)
    validate_questions(questions, operation_ids, object_ids)

    state = extract_capsule(STATE_PATH, STATE_BEGIN, STATE_END)
    completed = [r for r in ops if r.get("status") == "CANONICALLY_COMPLETE"]
    if not completed:
        fail("cannot build index without a completed operation")
    latest = completed[-1]["operation_id"]

    next_op = state.get("next_recommended_operation")
    if next_op is not None and next_op not in by_operation:
        fail(f"CURRENT_STATE references unknown next operation: {next_op}")

    grammar = state.get("active_candidate_grammar")
    if grammar is not None and grammar not in by_object:
        fail(f"CURRENT_STATE references unknown active candidate grammar: {grammar}")

    index = {
        "schema_version": "0.1.0",
        "authority": "DERIVED_NAVIGATION_ONLY",
        "indexed_research_baseline_commit": baseline_commit,
        "indexed_research_baseline_tree": git_tree_for(baseline_commit),
        "current_phase": state["current_phase"],
        "latest_completed_operation": latest,
        "current_handoff": state["current_handoff"],
        "canonical_state": "CURRENT_STATE.md",
        "canonical_hypothesis": state["canonical_hypothesis"],
        "active_candidate_grammar": grammar,
        "counts": {
            "operation_records": len(ops),
            "research_object_records": len(objects),
            "open_question_records": len(questions),
            "open_questions": sum(q.get("status") == "OPEN" for q in questions),
        },
        "next_recommended_operation": next_op,
        "next_operation_authorized": bool(state["next_operation_authorized"]),
        "source_bound_status": state["source_bound_status"],
        "fcp_relationship": state["fcp_relationship"],
    }
    INDEX_PATH.write_text(
        json.dumps(index, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"PGH_NAVIGATION_BUILD=PASS")
    print(f"INDEXED_RESEARCH_BASELINE_COMMIT={baseline_commit}")
    print(f"INDEXED_RESEARCH_BASELINE_TREE={index['indexed_research_baseline_tree']}")


def main() -> int:
    parser = argparse.ArgumentParser(description="PGH derived navigation utility")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("check", help="validate navigation without mutation")

    build = sub.add_parser("build", help="regenerate derived canonical index")
    build.add_argument(
        "--baseline-commit",
        required=True,
        help="exact logical research baseline commit to index",
    )

    args = parser.parse_args()
    try:
        if args.command == "check":
            run_check()
        elif args.command == "build":
            build_index(args.baseline_commit)
        else:
            fail(f"unknown command: {args.command}")
    except CheckFailure as exc:
        print(f"PGH_NAVIGATION_CHECK=FAIL", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
