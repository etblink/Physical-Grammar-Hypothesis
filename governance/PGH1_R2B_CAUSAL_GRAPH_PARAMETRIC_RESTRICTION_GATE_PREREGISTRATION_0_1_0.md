# PGH-1 R2B Causal Graph Parametric Restriction Gate — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_R2B_CAUSAL_GRAPH_PARAMETRIC_RESTRICTION_GATE
REGISTRY_ID = PGH-OP-0059
CANONICAL_BASE = bde9932538ffc9ab236e0059fa81df12934f9e93
PARENT_ADJUDICATION = PGH-OP-0058
SG4_SOURCE_CORPUS = 85_DISTINCT_ACCEPTED
STRUCTURAL_ACCOUNTING = PGH-OBJ-0032
INPUT_RELOCATION_FAILURE = PGH-FAIL-0030
R2_TARGET = PGH-OBJ-0021
NEW_SOURCE_SEARCH = FORBIDDEN
EMPIRICAL_DATA = FORBIDDEN
PHYSICAL_CAUSATION_SEMANTICS = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Test, at pure finite probabilistic/formal scope, whether fixed causal/DAG wiring can impose a nontrivial model-class restriction while local conditional kernels remain free, and whether a more connected DAG on the same variables restores universal finite joint-distribution representability.

The gate is an input-accounting experiment. It does not select a physical graph, claim that the variables are physical causes, or add the graph to an existing `PGH-GRAM-*` identity.

## Fixed variable system

Use three binary formal variables:

```text
A,B,C in {0,1}
```

No empirical interpretation is assigned.

## Fixed graph pair

### Sparse graph

```text
G_S:
A -> B -> C
```

Factorization class:

\[
p(a,b,c)=p(a)p(b\mid a)p(c\mid b).
\]

### Complete ordered DAG

```text
G_K:
A -> B
A -> C
B -> C
```

Factorization class:

\[
p(a,b,c)=p(a)p(b\mid a)p(c\mid a,b).
\]

The node set and alphabets are identical. Only graph/wiring differs.

## Locked theorem T1 — sparse-chain conditional independence

Prove directly from the `G_S` factorization that

\[
A\perp C\mid B.
\]

At any `b` with `p(b)>0`, show

\[
p(a,c\mid b)=p(a\mid b)p(c\mid b).
\]

This is a formal graph-conditioned theorem, not a physical causal claim.

## Locked witness T2 — explicit distribution excluded by the sparse graph

Define the finite joint distribution:

```text
A = fair bit
B = independent fair bit
C = A deterministically
```

Equivalently, nonzero atoms are:

```text
P(0,0,0)=1/4
P(0,1,0)=1/4
P(1,0,1)=1/4
P(1,1,1)=1/4
```

Test whether this violates `A independent C given B` and is therefore excluded from the `G_S` factorization class.

The witness is frozen before adjudication and may not be replaced by a more convenient target.

## Locked theorem T3 — complete-DAG universal finite representability

For arbitrary finite joint distribution `p(a,b,c)`, test whether there exist conditional kernels such that

\[
p(a,b,c)=p(a)p(b\mid a)p(c\mid a,b).
\]

Use the ordinary chain-rule construction where conditioning events have positive mass, with arbitrary normalized conditional values on zero-probability parent configurations because those configurations contribute zero to the reconstructed joint.

If this holds, conclude that `G_K` imposes no proper restriction on the class of all finite joint distributions at this scope.

## Locked control T4 — same local-kernel freedom

Local conditional tables may vary arbitrarily subject only to normalization for both graph classes.

No numerical kernel is fixed by the grammar test.

Any difference in representable joint distributions must therefore be charged to graph/wiring structure rather than to chosen local parameter values.

## Locked control T5 — graph-family universality

If `G_S` excludes distributions but `G_K` represents all of them, conclude:

```text
FIXED_GRAPH_CAN_BE_SELECTIVE
UNRESTRICTED_GRAPH_FAMILY_INCLUDING_COMPLETE_DAG_IS_NOT_SELECTIVE_AT_JOINT_DISTRIBUTION_SCOPE
```

Do not infer that all DAGs are equivalent or that sparse graphs are physically preferred.

## Locked control T6 — representation and naming

Renaming `A,B,C` together with the corresponding graph incidence and probability arguments must transport the theorem covariantly.

Do not require arbitrary permutations to be automorphisms of one fixed directed graph.

This preserves the canonical covariance/automorphy distinction.

## Locked control T7 — bridge relevance ceiling

The gate establishes only a formal mechanism by which explicit structural wiring can reduce a process-model class.

It does not yet establish:

```text
A,B,C = PHYSICAL_VARIABLES
ARROWS = PHYSICAL_CAUSATION
DAG = EMPIRICALLY_CORRECT
DAG = GENERATED_BY_EXISTING_PGH_GRAMMAR
CONDITIONAL_INDEPENDENCE = COMPLETE_PHYSICAL_LAW
```

A later semantic/candidate-identity gate is required before any physical bridge credit.

## Outcome space

```text
A = THE_SPARSE_DAG_ENFORCES_A_NONTRIVIAL_CONDITIONAL_INDEPENDENCE_AND_EXCLUDES_THE_LOCKED_WITNESS_WHILE_THE_COMPLETE_DAG_REPRESENTS_ALL_FINITE_JOINTS__GRAPH_STRUCTURE_IS_FORMALLY_CONFIRMED_AS_A_SELECTIVE_INPUT_WITH_LOCAL_KERNELS_FREE

B = THE_SPARSE_AND_COMPLETE_DAG_CLASSES_DO_NOT_DIFFER_IN_THE_LOCKED_TEST_OR_THE_SPARSE_CONDITIONAL_INDEPENDENCE_FAILS__M2_DOES_NOT_PROVIDE_THE_EXPECTED_RESTRICTION

C = THE_COMPLETE_DAG_UNIVERSALITY_OR_SPARSE_GRAPH_RESTRICTION_DEPENDS_ON_AN_UNRESOLVED_SOURCE_OR_FORMALISM_GAP__STOP_FOR_NARROW_REVIEW

D = THE_GRAPH_FACTORISATION_TEST_CANNOT_BE_RELATED_TO_THE_CURRENT_PGH_BRIDGE_PROBLEM_WITHOUT_ALREADY_IMPORTING_PHYSICAL_SEMANTICS__PRESERVE_AS_EXTERNAL_COMPARISON_ONLY
```

No outcome satisfies R2B or selects a physical graph.

## Required outputs

Commit 2 may add only:

```text
audits/PGH1_R2B_CAUSAL_GRAPH_PARAMETRIC_RESTRICTION_GATE_0_1_0.md
research/formalizations/PGH1_CAUSAL_GRAPH_PARAMETRIC_RESTRICTION_SCHEMA_0_1_0.md
research/derivations/PGH_DERIVATION_SPARSE_DAG_CONDITIONAL_INDEPENDENCE_0_1_0.md
research/derivations/PGH_DERIVATION_COMPLETE_DAG_FINITE_JOINT_UNIVERSALITY_0_1_0.md
research/failures/PGH_FAIL_UNRESTRICTED_DAG_FAMILY_RESPONSE_CONSTRAINT_0_1_0.md
handoffs/PGH1_R2B_CAUSAL_GRAPH_PARAMETRIC_RESTRICTION_GATE_HANDOFF_0_1_0.md
```

Expected identities if earned:

```text
PGH-OBJ-0033 = CAUSAL_GRAPH_PARAMETRIC_RESTRICTION_SCHEMA
PGH-DER-0029 = SPARSE_DAG_CONDITIONAL_INDEPENDENCE
PGH-DER-0030 = COMPLETE_DAG_FINITE_JOINT_UNIVERSALITY
PGH-FAIL-0031 = UNRESTRICTED_DAG_FAMILY_RESPONSE_CONSTRAINT
```

## Commit topology

```text
COMMIT_1_MESSAGE = Preregister PGH-1 R2B causal graph parametric restriction gate
COMMIT_2_MESSAGE = Adjudicate PGH-1 R2B causal graph parametric restriction gate
EXACT_COMMITS = 2
```

## Hard stops

```text
DO_NOT_SEARCH_NEW_SOURCES
DO_NOT_USE_EMPIRICAL_DATA
DO_NOT_CALL_ARROWS_PHYSICAL_CAUSES
DO_NOT_ADD_G_S_OR_G_K_TO_AN_EXISTING_GRAMMAR_IDENTITY
DO_NOT_SELECT_G_S_BY_PHYSICAL_FIT
DO_NOT_FIX_LOCAL_KERNEL_VALUES_EXCEPT_THE_LOCKED_COUNTERWITNESS_FOR_EXCLUSION_TESTING
DO_NOT_DECLARE_R2B_SATISFIED
DO_NOT_MAKE_EMPIRICAL_PREDICTIONS
DO_NOT_CHANGE_FCP
```
