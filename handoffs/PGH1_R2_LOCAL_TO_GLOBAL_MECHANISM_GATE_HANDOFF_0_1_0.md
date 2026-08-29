# PGH-1 R2 Local-to-Global Mechanism Gate — Handoff 0.1.0

## Operation result

```text
OPERATION_ID = PGH1_R2_LOCAL_TO_GLOBAL_MECHANISM_GATE
REGISTRY_ID = PGH-OP-0034
STATUS = QUALIFIED_CANDIDATE_COMPLETE_NOT_INTEGRATED
OUTCOME = B__LOCAL_TO_GLOBAL_OBSTRUCTION_IS_A_QUALIFIED_NON_TABLE_DRIVEN_FORMAL_MECHANISM_BUT_COVER_DOMAIN_AND_LOCAL_RULE_PRIVILEGE_REMAIN_UNEARNED
CANONICAL_BASE = c60254f82bf2cca3628e2191e3968e622741197e
PREREGISTRATION_COMMIT = 630269b15ce39afe0332d5296311c88b5189271f
PROJECT_LEAD_INDEPENDENT_REVIEW = PENDING
FCP_EFFECT = NONE
```

## Qualified candidate result

```text
PGH-DER-0012 = ODD_CYCLE_LOCAL_TO_GLOBAL_OBSTRUCTION
PGH-FAIL-0014 = UNPRIVILEGED_LOCAL_GLOBAL_INPUT_SELECTION
```

The odd-cycle witness uses one identical local inequality rule on every edge. Every local constraint is satisfiable and every proper path is satisfiable, but the full odd cycle has no global binary assignment. The contradiction follows from parity, not from an extensional list of forbidden global configurations.

The same obstruction survives graph-coloring, XOR-constraint, and local/global-extension presentations.

## Scientific boundary

The mechanism is stronger than bare formation-table exclusion:

```text
NON_TABLE_DRIVEN_EXCLUSION = YES
COMPACT_UNIFORM_LOCAL_RULE = YES
GLOBAL_IMPOSSIBILITY_DERIVED = YES
```

But the following remain unearned inputs:

```text
PHYSICAL_PRIVILEGE_OF_COVER
PHYSICAL_PRIVILEGE_OF_VALUE_DOMAIN
PHYSICAL_PRIVILEGE_OF_LOCAL_RULE
PHYSICAL_BRIDGE
```

Therefore:

```text
SUCCESSOR_GRAMMAR = NONE
R2_SATISFIED = NO
PHYSICAL_GRAMMAR_FOUND = NO
PHYSICAL_LAW_DERIVED = NO
```

## Source use

The frozen PGH-1 source corpus supports local-to-global obstruction as a real generic and physical mechanism family while preserving representation controls. No new source search occurred in this gate.

## Recommended next operation

```text
NEXT_RECOMMENDED_OPERATION = PGH1_R2_GENERATED_COVER_AND_COMPATIBILITY_ORIGIN_GATE
NEXT_OPERATION_AUTHORIZED = NO
```

That gate should test whether context covers and compatibility relations can arise from deeper, independently motivated PGH structure tied only to the law-free empirical anchor, rather than being selected to reproduce a desired global impossibility.

It must not assume that graph incidence, sheaf covers, binary outcomes, contextuality scenarios, or inequality relations are fundamental.

## Structured handoff capsule

<!-- PGH_HANDOFF_CAPSULE_BEGIN -->
```json
{
  "capsule_schema_version": "0.1.0",
  "operation_id": "PGH1_R2_LOCAL_TO_GLOBAL_MECHANISM_GATE",
  "status": "QUALIFIED_CANDIDATE_COMPLETE_NOT_INTEGRATED",
  "indexed_research_baseline_commit": "c60254f82bf2cca3628e2191e3968e622741197e",
  "must_read": [
    "sources/PGH1_R2_LOCAL_GLOBAL_SOURCE_REGISTER_0_1_0.md",
    "sources/PGH1_R2_LOCAL_GLOBAL_SOURCE_LANDSCAPE_0_1_0.md",
    "governance/PGH1_R2_LOCAL_TO_GLOBAL_MECHANISM_GATE_PREREGISTRATION_0_1_0.md",
    "audits/PGH1_R2_LOCAL_TO_GLOBAL_MECHANISM_GATE_0_1_0.md",
    "research/formalizations/PGH1_LOCAL_TO_GLOBAL_CONSTRAINT_SCHEMA_0_1_0.md",
    "research/derivations/PGH_DERIVATION_ODD_CYCLE_LOCAL_GLOBAL_OBSTRUCTION_0_1_0.md",
    "research/failures/PGH_FAIL_UNPRIVILEGED_LOCAL_GLOBAL_INPUT_SELECTION_0_1_0.md"
  ],
  "outputs": [
    "governance/PGH1_R2_LOCAL_TO_GLOBAL_MECHANISM_GATE_PREREGISTRATION_0_1_0.md",
    "audits/PGH1_R2_LOCAL_TO_GLOBAL_MECHANISM_GATE_0_1_0.md",
    "research/formalizations/PGH1_LOCAL_TO_GLOBAL_CONSTRAINT_SCHEMA_0_1_0.md",
    "research/derivations/PGH_DERIVATION_ODD_CYCLE_LOCAL_GLOBAL_OBSTRUCTION_0_1_0.md",
    "research/failures/PGH_FAIL_UNPRIVILEGED_LOCAL_GLOBAL_INPUT_SELECTION_0_1_0.md",
    "handoffs/PGH1_R2_LOCAL_TO_GLOBAL_MECHANISM_GATE_HANDOFF_0_1_0.md"
  ],
  "next_recommended_operation": "PGH1_R2_GENERATED_COVER_AND_COMPATIBILITY_ORIGIN_GATE",
  "next_operation_authorized": false,
  "do_not_assume": [
    "LOCAL_TO_GLOBAL_OBSTRUCTION_IS_A_PHYSICAL_LAW",
    "ODD_CYCLE_STRUCTURE_IS_PHYSICALLY_PRIVILEGED",
    "BINARY_DOMAIN_IS_FUNDAMENTAL",
    "INEQUALITY_IS_A_FUNDAMENTAL_LOCAL_RULE",
    "SHEAF_THEORY_IS_THE_PGH_GRAMMAR",
    "CONTEXTUALITY_IS_DERIVED_FROM_PGH",
    "A_SUCCESSOR_GRAMMAR_HAS_BEEN_CREATED",
    "R2_IS_SATISFIED",
    "PGH_HAS_ANY_CANONICAL_EFFECT_ON_FCP"
  ]
}
```
<!-- PGH_HANDOFF_CAPSULE_END -->
