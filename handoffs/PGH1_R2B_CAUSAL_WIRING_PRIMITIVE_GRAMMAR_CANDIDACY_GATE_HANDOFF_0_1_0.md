# PGH-1 R2B Causal Wiring Primitive Grammar Candidacy Gate — Handoff 0.1.0

## Scientific result

```text
OPERATION_ID = PGH1_R2B_CAUSAL_WIRING_PRIMITIVE_GRAMMAR_CANDIDACY_GATE
REGISTRY_ID = PGH-OP-0060
STATUS = COMPLETE_CANDIDATE
PREREGISTRATION_COMMIT = 03e20180a54ae13a0b1b9b4216dc815b7b35af6f
OUTCOME = A__PGH_GRAM_0008_PASSES_FORMAL_PRIMITIVE_GRAMMAR_CANDIDACY_UNDER_PGH_OBJ_0020__ITS_FIXED_SPARSE_WIRING_GENERATES_NONTRIVIAL_MODEL_CLASS_EXCLUSION_WITH_FREE_LOCAL_KERNELS__NO_PHYSICAL_STATUS_OR_R2B_CREDIT_FOLLOWS
```

## New records

```text
PGH-GRAM-0008 = THREE_NODE_SPARSE_MARKOV_CHAIN_PRIMITIVE_GRAMMAR_CANDIDATE
PGH-OBJ-0034 = CAUSAL_WIRING_PRIMITIVE_GRAMMAR_CANDIDACY_SCHEMA
PGH-FAIL-0032 = CAUSAL_WIRING_PHYSICAL_SEMANTICS_PREMATURE
```

## Candidate definition

`PGH-GRAM-0008` contains three formal variable roles and fixed sparse wiring

\[
A\to B\to C
\]

with admissible finite normalized models

\[
p(a,b,c)=p(a)p(b\mid a)p(c\mid b).
\]

All local conditional kernels remain arbitrary normalized model data.

The candidate contains no empirical response table and no fitted numerical values.

## Why candidacy passes

```text
FORMALLY_DEFINED = YES
PRIMITIVES_EXPLICIT = YES
PRE_TARGET_AT_CURRENT_SCOPE = YES
UNIVERSAL_ENCODER = NO
EXTENSIONAL_TARGET_TABLE = NO
GENERATIVE_COMPRESSION = YES
NONTRIVIAL_EXCLUSION = YES
REPRESENTATION_COVARIANCE = YES
COUNTERMODEL_EXPOSURE = YES
PHYSICAL_BRIDGE = NONE
```

`PGH-DER-0029` supplies the exclusion theorem and locked counterdistribution.

`PGH-DER-0030` supplies the complete-DAG universal control.

## Important limitation

The chain factorization and conditional-independence result are established probabilistic graphical-model machinery.

```text
MATHEMATICAL_NOVELTY = NONE_CLAIMED
```

The PGH result is only that this known structural mechanism passes the project's formal primitive-grammar candidacy standard and has response-model exclusion power with free local parameters.

## Next recommended operation

```text
NEXT_RECOMMENDED_OPERATION = PGH1_R2B_CAUSAL_WIRING_PHYSICAL_SEMANTIC_FIREWALL_GATE
NEXT_OPERATION_AUTHORIZED = NO
```

The next gate should compare semantic readings of the same exact formal candidate, including:

1. graph as pure probabilistic factorization bookkeeping;
2. graph as dependency/generative-precedence structure;
3. graph as physical causation.

It must ask whether any substantive physical reading can be fixed independently of the conditional-independence pattern it later predicts.

No empirical data should be used unless a semantic reading survives first.

## Result ceiling

```text
FORMAL_PRIMITIVE_GRAMMAR_CANDIDATES = AT_LEAST_6_TOTAL_IN_PROJECT
PGH_GRAM_0008_PHYSICAL_STATUS = NONE
R2B = UNSATISFIED
PHYSICAL_LAW_DERIVED = NO
EMPIRICAL_PREDICTION = NONE
FCP_EFFECT = NONE
```

## Structured handoff capsule

<!-- PGH_HANDOFF_CAPSULE_BEGIN -->
```json
{
  "capsule_schema_version": "0.1.0",
  "operation_id": "PGH1_R2B_CAUSAL_WIRING_PRIMITIVE_GRAMMAR_CANDIDACY_GATE",
  "status": "COMPLETE_CANDIDATE",
  "indexed_research_baseline_commit": "b5107f219879c11f117ca1278a46a22fa150bf51",
  "must_read": [
    "audits/PGH1_R2B_CAUSAL_WIRING_PRIMITIVE_GRAMMAR_CANDIDACY_GATE_0_1_0.md",
    "research/grammars/PGH_GRAMMAR_THREE_NODE_SPARSE_MARKOV_CHAIN_CANDIDATE_0_1_0.md",
    "research/formalizations/PGH1_CAUSAL_WIRING_PRIMITIVE_GRAMMAR_CANDIDACY_SCHEMA_0_1_0.md",
    "research/failures/PGH_FAIL_CAUSAL_WIRING_PHYSICAL_SEMANTICS_PREMATURE_0_1_0.md"
  ],
  "outputs": [
    "audits/PGH1_R2B_CAUSAL_WIRING_PRIMITIVE_GRAMMAR_CANDIDACY_GATE_0_1_0.md",
    "research/grammars/PGH_GRAMMAR_THREE_NODE_SPARSE_MARKOV_CHAIN_CANDIDATE_0_1_0.md",
    "research/formalizations/PGH1_CAUSAL_WIRING_PRIMITIVE_GRAMMAR_CANDIDACY_SCHEMA_0_1_0.md",
    "research/failures/PGH_FAIL_CAUSAL_WIRING_PHYSICAL_SEMANTICS_PREMATURE_0_1_0.md",
    "handoffs/PGH1_R2B_CAUSAL_WIRING_PRIMITIVE_GRAMMAR_CANDIDACY_GATE_HANDOFF_0_1_0.md"
  ],
  "open_questions": ["PGH-Q-0017"],
  "next_recommended_operation": "PGH1_R2B_CAUSAL_WIRING_PHYSICAL_SEMANTIC_FIREWALL_GATE",
  "next_operation_authorized": false,
  "do_not_assume": [
    "PGH_GRAM_0008_IS_PHYSICAL",
    "DAG_ARROWS_ARE_PHYSICAL_CAUSES",
    "CONDITIONAL_INDEPENDENCE_IS_ALREADY_A_PHYSICAL_LAW",
    "R2B_HAS_PASSED"
  ]
}
```
<!-- PGH_HANDOFF_CAPSULE_END -->
