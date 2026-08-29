# PGH-1 Post-Kp Physical Scope / Domain-Selection Gate — Handoff 0.1.0

## Scientific result

```text
OPERATION_ID = PGH1_POST_KP_PHYSICAL_SCOPE_DOMAIN_SELECTION_GATE
REGISTRY_ID = PGH-OP-0068
STATUS = COMPLETE_CANDIDATE
PREREGISTRATION_COMMIT = d1ae222f6df6ab541800f9b572e5abaf4e3037db
OUTCOME = C__NO_PRE_KP_PHYSICAL_SCOPE_SELECTOR_QUALIFIES__THE_EXISTING_CANDIDATE_IS_PHYSICALLY_SCOPE_UNDERDETERMINED__THE_KP_FAILURE_REMAINS_FOR_THE_FROZEN_INSTANTIATION__ANY_NEW_SCOPE_RULE_IS_A_POST_KP_HYPOTHESIS_REVISION
FCP_EFFECT = NONE
```

## New records

```text
PGH-OBJ-0038 = POST_KP_PHYSICAL_SCOPE_DOMAIN_SELECTION_SCHEMA
PGH-FAIL-0036 = POST_RESULT_PHYSICAL_SCOPE_SELECTION_RELOCATION
```

## Core finding

Before Kp, the project had:

```text
FORMAL_GRAMMAR = PGH-GRAM-0008
CONDITIONAL_SEMANTIC_BRIDGE = PGH-OBJ-0035
NONLEAKING_FIRST_TARGET_SELECTION_PROTOCOL = PGH-OBJ-0036
```

It did **not** have a qualified physical-domain predicate stating which real systems are governed by the grammar.

Those layers are not interchangeable.

Kp was validly selected as the first empirical instantiation and remains refuted. The failure may not be neutralized by declaring Kp out of scope after the result.

## Route results

```text
R0_NO_PHYSICAL_SCOPE = ACCURATE_DESCRIPTION_OF_PRE_KP_STATE
R1_METADATA_PROTOCOL_AS_SCOPE = REJECT_RETROACTIVE_PROMOTION
R2_PHYSICAL_CAUSAL_CHAIN_SCOPE = NOT_PRE_KP_QUALIFIED
R3_NAMED_PHYSICAL_SECTOR = NONE_PRE_KP
R4_RESULT_OR_MARKOV_FIT_SCOPE = REJECT_CIRCULAR
R5_STRONG_PGH_UNIVERSAL_READING = DOES_NOT_IDENTIFY_PGH_GRAM_0008_WITH_FINAL_UNIVERSAL_GRAMMAR
```

## Consequence for PGH-GRAM-0008

```text
FORMAL_STATUS = RETAINED
PHYSICAL_VALIDATION = NONE
KP_INSTANTIATION = REFUTED
FURTHER_SECOND_TARGET_CREDIT_UNDER_UNCHANGED_IDENTITY = BLOCKED_PENDING_SCOPE_RESOLUTION_OR_NEW_CANDIDATE
```

A future scope rule may be scientifically legitimate, but if it is first introduced after Kp it must define a new/revised hypothesis identity. It cannot change the Kp verdict or acquire retroactive predictive status.

## Method consequence

Future Monte Carlo preregistrations must freeze exact PRNG and sampling semantics, not only seed derivation.

## Next recommended operation

```text
NEXT_RECOMMENDED_OPERATION = PGH1_POST_KP_CANDIDATE_DISPOSITION_AND_SUCCESSOR_ARCHITECTURE_SEQUENCING_GATE
NEXT_OPERATION_AUTHORIZED = NO
```

The next operation should choose the scientifically appropriate disposition of the unchanged candidate and possible successor route **without** new empirical target search, external source intake, or successor construction.

## Stop boundary

```text
SECOND_TARGET_SELECTED = NO
NEW_SCOPE_RULE_CREATED = NO
NEW_GRAMMAR_CREATED = NO
EXTERNAL_SOURCE_SEARCH = NO
FCP_CHANGED = NO
```

## Structured handoff capsule

<!-- PGH_HANDOFF_CAPSULE_BEGIN -->
```json
{
  "capsule_schema_version": "0.1.0",
  "operation_id": "PGH1_POST_KP_PHYSICAL_SCOPE_DOMAIN_SELECTION_GATE",
  "status": "COMPLETE_CANDIDATE",
  "indexed_research_baseline_commit": "d3b4a7e0d98e94e60fbff72cbb3a8c95e31fbde8",
  "must_read": [
    "governance/PGH1_POST_KP_PHYSICAL_SCOPE_DOMAIN_SELECTION_GATE_PREREGISTRATION_0_1_0.md",
    "audits/PGH1_POST_KP_PHYSICAL_SCOPE_DOMAIN_SELECTION_GATE_0_1_0.md",
    "research/formalizations/PGH1_POST_KP_PHYSICAL_SCOPE_DOMAIN_SELECTION_SCHEMA_0_1_0.md",
    "research/failures/PGH_FAIL_POST_RESULT_PHYSICAL_SCOPE_SELECTION_RELOCATION_0_1_0.md",
    "audits/PGH1_POST_FIRST_EMPIRICAL_KP_RESULT_ADJUDICATION_0_1_0.md"
  ],
  "outputs": [
    "audits/PGH1_POST_KP_PHYSICAL_SCOPE_DOMAIN_SELECTION_GATE_0_1_0.md",
    "research/formalizations/PGH1_POST_KP_PHYSICAL_SCOPE_DOMAIN_SELECTION_SCHEMA_0_1_0.md",
    "research/failures/PGH_FAIL_POST_RESULT_PHYSICAL_SCOPE_SELECTION_RELOCATION_0_1_0.md",
    "handoffs/PGH1_POST_KP_PHYSICAL_SCOPE_DOMAIN_SELECTION_GATE_HANDOFF_0_1_0.md"
  ],
  "open_questions": ["PGH-Q-0017"],
  "next_recommended_operation": "PGH1_POST_KP_CANDIDATE_DISPOSITION_AND_SUCCESSOR_ARCHITECTURE_SEQUENCING_GATE",
  "next_operation_authorized": false,
  "do_not_assume": [
    "KP_IS_NOW_OUT_OF_SCOPE",
    "A_SECOND_TARGET_CAN_RESCUE_THE_UNCHANGED_CANDIDATE",
    "PGH_GRAM_0008_IS_THE_UNIVERSAL_GRAMMAR_OF_STRONG_PGH",
    "A_POST_KP_SCOPE_RULE_HAS_PRE_RESULT_STATUS",
    "STRONG_PGH_IS_CONFIRMED_OR_GLOBALLY_REFUTED",
    "R2B_HAS_PASSED"
  ]
}
```
<!-- PGH_HANDOFF_CAPSULE_END -->
