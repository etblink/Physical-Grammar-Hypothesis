# PGH-0 Minimal Physical Semantic Anchor Challenge — Qualified Local Handoff 0.1.0

## Status

```text
OPERATION_ID = PGH0_MINIMAL_PHYSICAL_SEMANTIC_ANCHOR_CHALLENGE
REGISTRY_ID = PGH-OP-0015
STATUS = QUALIFIED_LOCAL_NOT_INTEGRATED
CANONICAL_BASE = 26b9d8616ef98a481e0ac67f807384ce4527c906
PREREGISTRATION_COMMIT = 51c021bf9b1d3f99f4bde6a2dc4069239c3d919f
WORKING_BRANCH = research/pgh0-minimal-physical-semantic-anchor
FROZEN_SOURCE_COUNT = 37
NEW_SOURCE_SEARCH = NONE
R2_STARTED = NO
FCP_EFFECT = NONE
```

## Scientific result

```text
OUTCOME = B__CONTEXT_RECORD_INTERFACE_IS_A_FORMALLY_FEASIBLE_MINIMAL_ANCHOR_BUT_PHYSICAL_REALIZATION_IS_UNESTABLISHED
FORMALLY_FEASIBLE_SEMANTIC_ANCHOR_SCHEMA = YES
PHYSICALLY_PRIVILEGED_ANCHOR_FOUND = NO
R1_SOLVED = NO
```

The qualified schema is:

```text
A_phys = (C, R, rho)
```

with probe/interface contexts `C`, record labels `R`, and a terminal-to-record interpretation `rho`. The candidate grammar/evaluator supplies the response map and is not part of the anchor.

## New formal result

```text
PGH-DER-0007 = ANCHOR_RESPONSE_SEPARATION
STATUS = QUALIFIED_FORMAL
```

A finite witness holds the same anchor fixed while two evaluators generate different record profiles. Therefore minimal interface semantics need not determine the response law.

## New preserved failure

```text
PGH-FAIL-0006 = SEMANTIC_ANCHOR_EXTREMES
STATUS = FAILED_PRESERVED
```

The challenge preserves four failures:

```text
PRIMITIVE_PHYSICAL_EQUIVALENCE = CIRCULAR
VOCABULARY_ONLY = TOO_WEAK
FULL_RESPONSE_TABLE = SEMANTIC_SMUGGLING
FULL_TASK_POSSIBILITY_SET = PHYSICAL_SELECTION_SMUGGLING
```

## R1 consequence

The purely formal selector route failed in the previous gate. This operation shows that a formal/semantic middle architecture is possible:

```text
INTERFACE_SEMANTICS + GRAMMAR_GENERATED_RESPONSE -> ANCHOR_RELATIVE_DISTINGUISHABILITY
```

But the physical choice of interface remains unproved.

```text
R1_REPRESENTATION_ROBUSTNESS = UNTESTED
R1_PHYSICAL_PRIVILEGE = UNESTABLISHED
```

## Source decision

```text
SPECIFIC_SOURCE_GAP = NONE_AT_CURRENT_OPERATION
SOURCE_EXPANSION_JUSTIFIED = NO
```

## Next recommended operation

```text
NEXT_RECOMMENDED_OPERATION = PGH0_CONTEXT_RECORD_ANCHOR_ROBUSTNESS_GATE
NEXT_OPERATION_AUTHORIZED = NO
```

The next gate should test whether genuinely different formal presentations can share the same interface semantics and whether anchor-relative equivalence commutes with faithful translation without importing substantive physics.

## Do not assume

- the context/record anchor is physically correct;
- records exhaust physical reality;
- observational equivalence is complete physical identity;
- the selected contexts are fundamental;
- the record map is unique;
- representation robustness has been established;
- R1 is solved;
- R2 has started;
- PGH is novel or true;
- any result changes FCP.

## Review boundary

Canonical `main` remains unchanged pending independent review.

Independent review should verify:

1. exact two-commit topology;
2. locked candidate order and outcome discipline;
3. the shared-anchor/two-evaluator finite witness;
4. that the anchor excludes the response law;
5. that the anchor nevertheless supports nontrivial record distinguishability when combined with a grammar;
6. that physical privilege and representation robustness remain explicitly unestablished;
7. that the semantic extremes are correctly rejected;
8. that R2 remains out of scope;
9. no source expansion or FCP effect.

<!-- PGH_HANDOFF_CAPSULE_BEGIN -->
```json
{
  "capsule_schema_version": "0.1.0",
  "operation_id": "PGH0_MINIMAL_PHYSICAL_SEMANTIC_ANCHOR_CHALLENGE",
  "status": "QUALIFIED_LOCAL_NOT_INTEGRATED",
  "indexed_research_baseline_commit": "26b9d8616ef98a481e0ac67f807384ce4527c906",
  "must_read": [
    "governance/PGH0_MINIMAL_PHYSICAL_SEMANTIC_ANCHOR_CHALLENGE_PREREGISTRATION_0_1_0.md",
    "audits/PGH0_MINIMAL_PHYSICAL_SEMANTIC_ANCHOR_CHALLENGE_0_1_0.md",
    "research/formalizations/PGH0_CONTEXT_RECORD_SEMANTIC_ANCHOR_0_1_0.md",
    "research/derivations/PGH_DERIVATION_ANCHOR_RESPONSE_SEPARATION_0_1_0.md",
    "research/failures/PGH_FAIL_SEMANTIC_ANCHOR_EXTREMES_0_1_0.md"
  ],
  "outputs": [
    "audits/PGH0_MINIMAL_PHYSICAL_SEMANTIC_ANCHOR_CHALLENGE_0_1_0.md",
    "research/formalizations/PGH0_CONTEXT_RECORD_SEMANTIC_ANCHOR_0_1_0.md",
    "research/derivations/PGH_DERIVATION_ANCHOR_RESPONSE_SEPARATION_0_1_0.md",
    "research/failures/PGH_FAIL_SEMANTIC_ANCHOR_EXTREMES_0_1_0.md",
    "handoffs/PGH0_MINIMAL_PHYSICAL_SEMANTIC_ANCHOR_CHALLENGE_HANDOFF_0_1_0.md"
  ],
  "open_questions": [
    "PGH-Q-0001",
    "PGH-Q-0004",
    "PGH-Q-0005",
    "PGH-Q-0006",
    "PGH-Q-0007",
    "PGH-Q-0009",
    "PGH-Q-0016",
    "PGH-Q-0017"
  ],
  "next_recommended_operation": "PGH0_CONTEXT_RECORD_ANCHOR_ROBUSTNESS_GATE",
  "next_operation_authorized": false,
  "do_not_assume": [
    "CONTEXT_RECORD_ANCHOR_IS_PHYSICALLY_CORRECT",
    "RECORD_EQUIVALENCE_IS_FULL_PHYSICAL_IDENTITY",
    "REPRESENTATION_ROBUSTNESS_HAS_BEEN_ESTABLISHED",
    "R1_IS_SOLVED",
    "R2_HAS_STARTED",
    "PGH_IS_NOVEL",
    "PGH_IS_TRUE",
    "PGH_HAS_ANY_CANONICAL_EFFECT_ON_FCP"
  ]
}
```
<!-- PGH_HANDOFF_CAPSULE_END -->
