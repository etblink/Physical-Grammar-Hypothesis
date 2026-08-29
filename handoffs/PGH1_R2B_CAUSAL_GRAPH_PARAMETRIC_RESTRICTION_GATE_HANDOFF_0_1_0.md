# PGH-1 R2B Causal Graph Parametric Restriction Gate — Handoff 0.1.0

## Scientific result

```text
OPERATION_ID = PGH1_R2B_CAUSAL_GRAPH_PARAMETRIC_RESTRICTION_GATE
REGISTRY_ID = PGH-OP-0059
STATUS = COMPLETE_CANDIDATE
PREREGISTRATION_COMMIT = b99d8f54e97562ea1e514f4c591f36dd127e2eac
OUTCOME = A__THE_SPARSE_DAG_ENFORCES_A_NONTRIVIAL_CONDITIONAL_INDEPENDENCE_AND_EXCLUDES_THE_LOCKED_WITNESS_WHILE_THE_COMPLETE_DAG_REPRESENTS_ALL_FINITE_JOINTS__GRAPH_STRUCTURE_IS_FORMALLY_CONFIRMED_AS_A_SELECTIVE_INPUT_WITH_LOCAL_KERNELS_FREE
```

## New records

```text
PGH-OBJ-0033 = CAUSAL_GRAPH_PARAMETRIC_RESTRICTION_SCHEMA
PGH-DER-0029 = SPARSE_DAG_CONDITIONAL_INDEPENDENCE
PGH-DER-0030 = COMPLETE_DAG_FINITE_JOINT_UNIVERSALITY
PGH-FAIL-0031 = UNRESTRICTED_DAG_FAMILY_RESPONSE_CONSTRAINT
```

## Core result

For the sparse graph

```text
A -> B -> C
```

factorization forces

\[
A\perp C\mid B.
\]

The locked distribution with independent fair `A,B` and `C=A` violates that condition and is excluded.

For the complete ordered DAG

```text
A -> B
A -> C
B -> C
```

all finite joint distributions are representable by the chain rule.

Thus:

```text
FIXED_SPARSE_WIRING = NONTRIVIALLY_SELECTIVE
LOCAL_CONDITIONAL_KERNELS = FREE
COMPLETE_DAG = UNIVERSAL_AT_FINITE_JOINT_SCOPE
SELECTIVE_INFORMATION = GRAPH_WIRING
```

## Scientific meaning

This is the first PGH-1 response-model control in which compact structural wiring removes members from a previously universal model class without numerically fixing the local response kernels.

It remains a formal result only.

```text
ARROWS_AS_PHYSICAL_CAUSES = NOT_ASSUMED
GRAPH_AS_PHYSICAL_STRUCTURE = NOT_QUALIFIED
PHYSICAL_LAW_DERIVED = NO
R2B = UNSATISFIED
```

## Next recommended operation

```text
NEXT_RECOMMENDED_OPERATION = PGH1_R2B_CAUSAL_WIRING_PRIMITIVE_GRAMMAR_CANDIDACY_GATE
NEXT_OPERATION_AUTHORIZED = NO
```

That gate should ask whether a fixed sparse Markov/DAG structural package can enter **formal primitive grammar candidacy** under `PGH-OBJ-0020` without inheriting physical meaning.

Required controls should include:

- graph fixed before any physical-fit evaluation;
- local conditional kernels remain model data rather than grammar rules;
- compact/non-extensional graph description;
- explicit exclusion theorem from `PGH-DER-0029`;
- complete-DAG/nonselective control from `PGH-DER-0030`;
- representation covariance under graph relabeling;
- no claim that causal arrows are physically real.

## Result ceiling

```text
STRUCTURAL_RESPONSE_RESTRICTION_MECHANISM = QUALIFIED_FORMAL
FORMAL_CAUSAL_GRAMMAR_CANDIDATE = NOT_YET_ASSIGNED
PHYSICAL_CAUSAL_GRAMMAR = NONE
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
  "operation_id": "PGH1_R2B_CAUSAL_GRAPH_PARAMETRIC_RESTRICTION_GATE",
  "status": "COMPLETE_CANDIDATE",
  "indexed_research_baseline_commit": "bde9932538ffc9ab236e0059fa81df12934f9e93",
  "must_read": [
    "audits/PGH1_R2B_CAUSAL_GRAPH_PARAMETRIC_RESTRICTION_GATE_0_1_0.md",
    "research/formalizations/PGH1_CAUSAL_GRAPH_PARAMETRIC_RESTRICTION_SCHEMA_0_1_0.md",
    "research/derivations/PGH_DERIVATION_SPARSE_DAG_CONDITIONAL_INDEPENDENCE_0_1_0.md",
    "research/derivations/PGH_DERIVATION_COMPLETE_DAG_FINITE_JOINT_UNIVERSALITY_0_1_0.md",
    "research/failures/PGH_FAIL_UNRESTRICTED_DAG_FAMILY_RESPONSE_CONSTRAINT_0_1_0.md"
  ],
  "outputs": [
    "audits/PGH1_R2B_CAUSAL_GRAPH_PARAMETRIC_RESTRICTION_GATE_0_1_0.md",
    "research/formalizations/PGH1_CAUSAL_GRAPH_PARAMETRIC_RESTRICTION_SCHEMA_0_1_0.md",
    "research/derivations/PGH_DERIVATION_SPARSE_DAG_CONDITIONAL_INDEPENDENCE_0_1_0.md",
    "research/derivations/PGH_DERIVATION_COMPLETE_DAG_FINITE_JOINT_UNIVERSALITY_0_1_0.md",
    "research/failures/PGH_FAIL_UNRESTRICTED_DAG_FAMILY_RESPONSE_CONSTRAINT_0_1_0.md",
    "handoffs/PGH1_R2B_CAUSAL_GRAPH_PARAMETRIC_RESTRICTION_GATE_HANDOFF_0_1_0.md"
  ],
  "open_questions": ["PGH-Q-0017"],
  "next_recommended_operation": "PGH1_R2B_CAUSAL_WIRING_PRIMITIVE_GRAMMAR_CANDIDACY_GATE",
  "next_operation_authorized": false,
  "do_not_assume": [
    "DAG_ARROWS_ARE_PHYSICAL_CAUSES",
    "SPARSE_GRAPH_IS_PHYSICALLY_CORRECT",
    "UNRESTRICTED_DAG_FAMILY_IS_SELECTIVE",
    "R2B_HAS_PASSED"
  ]
}
```
<!-- PGH_HANDOFF_CAPSULE_END -->
