# PGH-1 R2B Network/Source-Independence Structural-Constraint Feasibility Gate — Handoff 0.1.0

```text
OPERATION_ID = PGH1_R2B_NETWORK_SOURCE_INDEPENDENCE_STRUCTURAL_CONSTRAINT_FEASIBILITY_GATE
REGISTRY_ID = PGH-OP-0100
STATUS = COMPLETE_CANDIDATE
OUTCOME = A__FORMAL_M3_FEASIBILITY_PASS__INDEPENDENT_SOURCE_NETWORK_GIVES_EXACT_NONTRIVIAL_EXCLUSION_STRUCTURALLY_DIFFERENT_FROM_RETIRED_PATH_CI__SELECTIVE_INPUTS_EXPLICIT__NO_PHYSICAL_CANDIDACY
M3_FORMAL_FEASIBILITY = PASS
NEW_FORMAL_SCHEMA = PGH-OBJ-0050
NEW_DERIVATIONS = PGH-DER-0033;PGH-DER-0034
PHYSICAL_NETWORK_SELECTED = NO
STRONG_PGH_CANDIDATE = NONE
POSITIVE_EMPIRICAL_PGH_CREDIT = NONE
R2B = UNSATISFIED
FCP_EFFECT = NONE
```

## Core result

A finite independent-source triangle with arbitrary local stochastic kernels excludes the nondegenerate perfect-common-bit distribution. The same topology realizes that distribution when its sources may be correlated, and a common-source model is universal over finite joint distributions.

A second exact triangle distribution violates all six independence restrictions in the retired minimal path family. Conversely, the perfect-common-bit witness satisfies all three noncollider separator CIs while remaining impossible in the independent-source triangle.

Therefore the M3 model class is formally selective and structurally incomparable with the retired six-member path-CI family.

## Exposed burden

The result does not make the triangle or source independence physical. It exposes the selective assumptions exactly:

```text
NETWORK_TOPOLOGY = SUBSTANTIVE_STRUCTURAL_INPUT
SOURCE_INDEPENDENCE = SUBSTANTIVE_STRUCTURAL_INPUT
LOCAL_KERNEL_VALUES = FREE
EMPIRICAL_RESPONSE_VALUES = ABSENT
```

The next target-free question is whether topology + source independence may enter explicit primitive grammar identity under the existing stopping-rule/admission discipline, or whether doing so merely relocates independent physical law into resource architecture.

```text
NEXT_RECOMMENDED_OPERATION = PGH1_R2B_NETWORK_SOURCE_INDEPENDENCE_PRIMITIVE_INPUT_ADMISSIBILITY_GATE
NEXT_OPERATION_AUTHORIZED = NO
```

No topology search, physical bridge, target discovery, or empirical work is authorized by this handoff.

<!-- PGH_HANDOFF_CAPSULE_BEGIN -->
```json
{"capsule_schema_version":"0.1.0","operation_id":"PGH1_R2B_NETWORK_SOURCE_INDEPENDENCE_STRUCTURAL_CONSTRAINT_FEASIBILITY_GATE","status":"COMPLETE_CANDIDATE","indexed_research_baseline_commit":"feadbdc4e14051ad3fca21bec88d0603fb6033ef","must_read":["governance/PGH1_R2B_NETWORK_SOURCE_INDEPENDENCE_STRUCTURAL_CONSTRAINT_FEASIBILITY_GATE_PREREGISTRATION_0_1_0.md","research/formalizations/PGH1_NETWORK_SOURCE_INDEPENDENCE_STRUCTURAL_CONSTRAINT_SCHEMA_0_1_0.md","research/derivations/PGH_DERIVATION_TRIANGLE_INDEPENDENT_SOURCE_COMMON_BIT_EXCLUSION_0_1_0.md","research/derivations/PGH_DERIVATION_TRIANGLE_PATH_CI_INCOMPARABILITY_WITNESS_0_1_0.md","audits/PGH1_R2B_NETWORK_SOURCE_INDEPENDENCE_STRUCTURAL_CONSTRAINT_FEASIBILITY_GATE_0_1_0.md"],"outputs":["research/formalizations/PGH1_NETWORK_SOURCE_INDEPENDENCE_STRUCTURAL_CONSTRAINT_SCHEMA_0_1_0.md","research/derivations/PGH_DERIVATION_TRIANGLE_INDEPENDENT_SOURCE_COMMON_BIT_EXCLUSION_0_1_0.md","research/derivations/PGH_DERIVATION_TRIANGLE_PATH_CI_INCOMPARABILITY_WITNESS_0_1_0.md","audits/PGH1_R2B_NETWORK_SOURCE_INDEPENDENCE_STRUCTURAL_CONSTRAINT_FEASIBILITY_GATE_0_1_0.md"],"open_questions":["PGH-Q-0017","PGH-Q-0038"],"next_recommended_operation":"PGH1_R2B_NETWORK_SOURCE_INDEPENDENCE_PRIMITIVE_INPUT_ADMISSIBILITY_GATE","next_operation_authorized":false,"do_not_assume":["TRIANGLE_TOPOLOGY_IS_PHYSICAL","SOURCE_INDEPENDENCE_IS_PHYSICAL_LAW_FROM_GRAMMAR","M3_IS_A_STRONG_PGH_CANDIDATE","A_NETWORK_TARGET_IS_AUTHORIZED","POSITIVE_EMPIRICAL_PGH_EVIDENCE_EXISTS","R2B_HAS_PASSED"]}
```
<!-- PGH_HANDOFF_CAPSULE_END -->
