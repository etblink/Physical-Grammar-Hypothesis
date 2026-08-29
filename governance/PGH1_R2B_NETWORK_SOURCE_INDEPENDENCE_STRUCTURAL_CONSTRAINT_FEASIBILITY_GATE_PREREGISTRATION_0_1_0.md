# PGH-1 R2B Network/Source-Independence Structural-Constraint Feasibility Gate — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_R2B_NETWORK_SOURCE_INDEPENDENCE_STRUCTURAL_CONSTRAINT_FEASIBILITY_GATE
REGISTRY_ID = PGH-OP-0100
CANONICAL_BASE = feadbdc4e14051ad3fca21bec88d0603fb6033ef
SEQUENCING_SOURCE = PGH-OP-0098
SOURCE_BOUND_MECHANISM = SG4_M3__NETWORK_TOPOLOGY_SOURCE_INDEPENDENCE_RESOURCE_ARCHITECTURE
FROZEN_SG4_ACCEPTED_SOURCE_COUNT = 15
TOTAL_FROZEN_ACCEPTED_SOURCE_COUNT = 85
NEW_SOURCE_SEARCH = FORBIDDEN
EMPIRICAL_DATA = FORBIDDEN
TARGET_DISCOVERY = FORBIDDEN
PHYSICAL_NETWORK_SELECTION = FORBIDDEN
STRONG_PGH_CANDIDATE_ADMISSION = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Test, at finite target-free formal scope, whether an explicitly fixed multi-source network together with source independence can generate a genuine model-class exclusion that is structurally different from the retired three-role/two-edge path conditional-independence architecture.

This operation tests the **formal mechanism and its input accounting only**. It does not ask whether the tested network is physically privileged.

## Source-bound rationale frozen before this gate

The canonical SG4 source landscape and adjudication already establish, before the Kp/HURDAT2 empirical sequence, that:

```text
M2_CAUSAL_DAG_FACTORIZATION = SELECTIVE_FOR_FIXED_GRAPH
M3_NETWORK_SOURCE_CONSTRAINTS = POTENTIALLY_STRONGER
M3_SELECTIVE_INPUTS = NETWORK_TOPOLOGY; SOURCE_INDEPENDENCE; RESOURCE_ARCHITECTURE
M3_SEQUENCING_PRIORITY = AFTER_M2
```

OP-0098 selected M3 because this ordering predates the empirical failures. No Kp or HURDAT2 residual structure may be used below.

## Accounting layers

Retain the SG4 accounting:

```text
D = doctrine / ordinary finite stochastic composition
W = network topology + source-independence/resource architecture
K = local stochastic response kernels
E = empirical response/parameter data
```

The gate may credit an exclusion to `D+W` only if it holds for **all** allowed local kernels `K` and uses no empirical layer `E`.

## Main formal test: independent-source triangle

Define three finite latent/source variables:

```text
U = source shared only by A and B
V = source shared only by B and C
W = source shared only by C and A
```

with finite supports and mutually independent source law

\[
p(u,v,w)=p_U(u)p_V(v)p_W(w).
\]

Each observed binary output has an arbitrary local stochastic kernel:

\[
p_A(a\mid u,w),\qquad
p_B(b\mid u,v),\qquad
p_C(c\mid v,w),
\]

where `a,b,c in {0,1}`.

The induced observed model class is

\[
\mathcal T_{\mathrm{ind}}
=
\left\{
 p(a,b,c)=\sum_{u,v,w}
 p_U(u)p_V(v)p_W(w)
 p_A(a\mid u,w)
 p_B(b\mid u,v)
 p_C(c\mid v,w)
\right\}.
\]

Source cardinalities are arbitrary finite values. Local kernels are unrestricted normalized stochastic kernels. No numerical kernel is fixed in the model-class definition.

The triangle is chosen as a **formal minimal no-common-source control**: every observed pair has access to one source, but no source is shared by all three observed roles. It is not proposed as a physical topology.

## Exact exclusion witness W1

Freeze the target-free binary distribution

\[
p_*(000)=\tfrac12,\qquad
p_*(111)=\tfrac12,
\]

and all other outcomes have probability zero.

Call this the `NONDEGENERATE_PERFECT_COMMON_BIT` distribution.

Required theorem test:

```text
W1_TEST = PROVE_OR_REFUTE__p_* NOT_IN T_ind
```

The proof, if it exists, must cover arbitrary finite source cardinalities and arbitrary stochastic local kernels. It may not assume deterministic local response functions unless determinism is derived from the perfect-agreement support condition.

## Same-topology correlated-source control C1

Define `T_corr` by the same local access pattern and arbitrary local kernels, but replace mutual source independence by an arbitrary joint source law `p(u,v,w)`.

Required control:

```text
C1_TEST = SHOW_OR_REFUTE__p_* IN T_corr
```

A pass demonstrates that source independence, not merely the pairwise-access diagram, contributes essential selectivity.

## Common-source universality control C2

Define a one-common-source finite model

\[
p(a,b,c)=\sum_\lambda p(\lambda)
 p_A(a\mid\lambda)p_B(b\mid\lambda)p_C(c\mid\lambda).
\]

Required control:

```text
C2_TEST = PROVE_OR_REFUTE__EVERY_FINITE_JOINT_DISTRIBUTION_ON_A_B_C_IS_REPRESENTABLE
```

The intended universality witness, if valid, is `lambda=(a,b,c)` with deterministic coordinate projections.

## Structural-difference witness W2

A formal M3 pass must do more than rederive one of the six retired path-family independence constraints.

Freeze independent fair binary sources:

```text
U,V,W ~ Bernoulli(1/2), mutually independent
```

and deterministic triangle kernels:

```text
A = 1 iff (U,W) = (0,0)
B = 1 iff (U,V) = (0,0)
C = 1 iff (V,W) = (0,0)
```

This induces the exact observed distribution

```text
q(000) = 4/8
q(001) = 1/8
q(010) = 1/8
q(100) = 1/8
q(111) = 1/8
all other q = 0
```

Required exact checks:

```text
W2A = q IN T_ind
W2B = q violates A independent C
W2C = q violates A independent B given C
W2D = q violates A independent B
W2E = q violates B independent C given A
W2F = q violates B independent C
W2G = q violates A independent C given B
```

If W2A-W2G all pass, `T_ind` is not merely a subset of any one of the six retired path model classes and contains a witness outside their union.

Also check that `p_*` satisfies at least one of the historical noncollider path restrictions (indeed, test all three separator conditional independences). If so, `p_*` lies in the retired path-family union while being excluded by `T_ind` if W1 passes.

Together these controls establish **model-class incomparability** rather than a relabeled path-CI restriction.

## Universal-family control C3

The gate must state explicitly what happens when the restrictive source architecture is allowed to vary.

At minimum:

```text
ALLOW_COMMON_SOURCE = RESTORES_FINITE_JOINT_UNIVERSALITY_VIA_C2_IF_C2_PASSES
UNRESTRICTED_RESOURCE_ARCHITECTURE = NOT_SELECTIVE_AT_THIS_FINITE_SCOPE
```

Therefore a future statement such as “network grammar constrains correlations” earns no PGH credit unless the network/source architecture is explicitly part of candidate identity.

## Input-origin firewall

Even if W1/W2 pass:

```text
FORMAL_MODEL_CLASS_EXCLUSION = MAY_PASS
PHYSICAL_PRIVILEGE_OF_TRIANGLE_TOPOLOGY = NOT_ESTABLISHED
PHYSICAL_PRIVILEGE_OF_SOURCE_INDEPENDENCE = NOT_ESTABLISHED
STRONG_PGH_CANDIDATE = NOT_CREATED
R2B = NOT_SATISFIED_BY_FORMAL_FEASIBILITY_ALONE
```

The gate must classify the selective input rather than hiding it.

Possible input-accounting conclusions include:

```text
SOURCE_INDEPENDENCE_AS_EXPLICIT_PRIMITIVE_GRAMMAR_CONTENT = FORMALLY_PERMISSIBLE_BUT_PHYSICALLY_UNEARNED
SOURCE_INDEPENDENCE_AS_SEMANTIC_OR_EXTERNAL_PHYSICAL_ASSUMPTION = CANNOT_RECEIVE_STRONG_PGH_LAW_EXHAUSTION_CREDIT
```

No choice between those physical interpretations is made here unless it follows from already canonical PGH structure.

## Outcome space

```text
A = FORMAL_M3_FEASIBILITY_PASS__INDEPENDENT_SOURCE_NETWORK_GIVES_EXACT_NONTRIVIAL_EXCLUSION_STRUCTURALLY_DIFFERENT_FROM_RETIRED_PATH_CI__SELECTIVE_INPUTS_EXPLICIT__NO_PHYSICAL_CANDIDACY

B = TESTED_NETWORK_SOURCE_ARCHITECTURE_YIELDS_ONLY_ORDINARY_CI_OR_NORMALIZATION_RESTRICTIONS__NO_DISTINCT_M3_GAIN_AT_TESTED_SCOPE

C = NONTRIVIAL_EXCLUSION_EXISTS_BUT_REQUIRES_ADDITIONAL_UNFROZEN_RESOURCE_MEASUREMENT_OR_SETTING_ASSUMPTIONS__CURRENT_M3_SCHEMA_INCOMPLETE__NO_CANDIDACY

D = W1_EXCLUSION_FAILS_OR_UNRESTRICTED_LOCAL_KERNELS_RESTORE_THE_WITNESS__M3_TESTED_FORMAL_ROUTE_FAILS

E = FROZEN_SG4_RECORD_OR_CURRENT_FORMAL_RESOURCES_ARE_INSUFFICIENT_TO_ADJUDICATE_THE_EXACT_FINITE_TEST__FREEZE_SPECIFIC_GAP__NO_NEW_SOURCE_SEARCH_HERE
```

Outcome A is a **formal feasibility pass only**.

## Required outputs

After this preregistration, the adjudication commit may add only:

```text
research/formalizations/PGH1_NETWORK_SOURCE_INDEPENDENCE_STRUCTURAL_CONSTRAINT_SCHEMA_0_1_0.md
research/derivations/PGH_DERIVATION_TRIANGLE_INDEPENDENT_SOURCE_COMMON_BIT_EXCLUSION_0_1_0.md
research/derivations/PGH_DERIVATION_TRIANGLE_PATH_CI_INCOMPARABILITY_WITNESS_0_1_0.md
audits/PGH1_R2B_NETWORK_SOURCE_INDEPENDENCE_STRUCTURAL_CONSTRAINT_FEASIBILITY_GATE_0_1_0.md
handoffs/PGH1_R2B_NETWORK_SOURCE_INDEPENDENCE_STRUCTURAL_CONSTRAINT_FEASIBILITY_GATE_HANDOFF_0_1_0.md
```

A failure object may be added only if a preregistered failure mode is actually established; it may not be invented to preserve a preferred outcome.

No navigation surface may be modified inside OP-0100.

## Stop boundary

```text
STOP_BEFORE_PHYSICAL_NETWORK_SELECTION
STOP_BEFORE_STRONG_PGH_CANDIDATE_ADMISSION
STOP_BEFORE_SEMANTIC_TARGET_BRIDGE
STOP_BEFORE_TARGET_DISCOVERY
STOP_BEFORE_EMPIRICAL_DATA
STOP_BEFORE_NEW_SOURCE_SEARCH
STOP_BEFORE_FCP_EFFECT
```

## Claim ceiling

```text
M3_FORMAL_FEASIBILITY = NOT_PREJUDGED
NETWORK_SOURCE_INDEPENDENCE_IS_PHYSICAL_LAW = NO
TRIANGLE_TOPOLOGY_IS_PHYSICALLY_PRIVILEGED = NO
STRONG_PGH_CONFIRMED = NO
ACTIVE_PHYSICAL_PREDICTIVE_CANDIDATE = NONE
POSITIVE_EMPIRICAL_PGH_CREDIT = NONE
R2B = UNSATISFIED
FCP_EFFECT = NONE
```

Truth over PGH.
