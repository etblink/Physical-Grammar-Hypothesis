# PGH-1 R2B Causal Graph Parametric Restriction Gate 0.1.0

## Identity

```text
OPERATION_ID = PGH1_R2B_CAUSAL_GRAPH_PARAMETRIC_RESTRICTION_GATE
REGISTRY_ID = PGH-OP-0059
CANONICAL_BASE = bde9932538ffc9ab236e0059fa81df12934f9e93
PREREGISTRATION_COMMIT = b99d8f54e97562ea1e514f4c591f36dd127e2eac
FROZEN_SOURCE_CORPUS = 85_DISTINCT_ACCEPTED
NEW_SOURCE_SEARCH = NONE
EMPIRICAL_DATA = NONE
PHYSICAL_CAUSATION_CLAIM = NONE
FCP_EFFECT = NONE
```

## Outcome

```text
OUTCOME = A__THE_SPARSE_DAG_ENFORCES_A_NONTRIVIAL_CONDITIONAL_INDEPENDENCE_AND_EXCLUDES_THE_LOCKED_WITNESS_WHILE_THE_COMPLETE_DAG_REPRESENTS_ALL_FINITE_JOINTS__GRAPH_STRUCTURE_IS_FORMALLY_CONFIRMED_AS_A_SELECTIVE_INPUT_WITH_LOCAL_KERNELS_FREE
R2B = UNSATISFIED
PHYSICAL_GRAPH_SELECTED = NO
PHYSICAL_LAW_DERIVED = NO
EMPIRICAL_PREDICTION = NONE
```

## Executive result

The locked graph-parametric control succeeds exactly at formal model-class scope.

For the sparse chain

\[
A\to B\to C,
\]

with factorization

\[
p(a,b,c)=p(a)p(b\mid a)p(c\mid b),
\]

every admissible distribution satisfies

\[
\boxed{A\perp C\mid B}.
\]

The preregistered distribution with independent fair `A,B` and deterministic `C=A` violates this condition and is therefore excluded.

For the complete ordered DAG

\[
A\to B,\quad A\to C,\quad B\to C,
\]

every finite joint distribution is representable as

\[
p(a)p(b\mid a)p(c\mid a,b)
\]

by the ordinary chain rule.

The node set, alphabets, and freedom of local conditional kernels are held fixed. The difference in representable joint distributions is therefore chargeable to graph/wiring structure.

## T1 — sparse-chain conditional independence

Assume `p(b)>0`. From the sparse factorization,

\[
\begin{aligned}
p(a,c\mid b)
&=\frac{p(a)p(b\mid a)p(c\mid b)}{p(b)}\\
&=\frac{p(a)p(b\mid a)}{p(b)}p(c\mid b)\\
&=p(a\mid b)p(c\mid b).
\end{aligned}
\]

Thus

\[
A\perp C\mid B.
\]

This result is frozen as:

```text
PGH-DER-0029 = SPARSE_DAG_CONDITIONAL_INDEPENDENCE
```

No physical interpretation of the arrows is used in the proof.

## T2 — locked excluded witness

The preregistered joint distribution has nonzero atoms

```text
P(0,0,0)=1/4
P(0,1,0)=1/4
P(1,0,1)=1/4
P(1,1,1)=1/4
```

so `A` and `B` are independent fair bits and `C=A` deterministically.

For either `b`,

```text
P(A=0,C=0 | B=b) = 1/2
P(A=0 | B=b) = 1/2
P(C=0 | B=b) = 1/2
```

hence

\[
\frac12\ne\frac12\cdot\frac12=\frac14.
\]

Conditional independence fails.

Therefore the witness is not representable by `G_S`.

## T3 — complete-DAG finite joint universality

Let `p(a,b,c)` be any finite joint distribution.

Define

\[
p(a)=\sum_{b,c}p(a,b,c).
\]

When `p(a)>0`, define

\[
p(b\mid a)=\frac{p(a,b)}{p(a)}.
\]

When `p(a,b)>0`, define

\[
p(c\mid a,b)=\frac{p(a,b,c)}{p(a,b)}.
\]

On zero-probability parent configurations choose arbitrary normalized conditionals; those terms contribute zero to the joint.

Then for every `(a,b,c)`,

\[
p(a,b,c)=p(a)p(b\mid a)p(c\mid a,b).
\]

Thus the complete DAG represents every finite joint distribution.

This result is frozen as:

```text
PGH-DER-0030 = COMPLETE_DAG_FINITE_JOINT_UNIVERSALITY
```

## Local-kernel freedom

Neither graph fixes numerical conditional kernels.

The sparse graph restricts **which variables may appear in which conditional factors** while allowing the factor values themselves to vary freely subject to normalization.

Therefore its conditional-independence result is not a hidden response table.

## Family-universality consequence

The combined theorems establish:

```text
FIXED_SPARSE_GRAPH = SELECTIVE
COMPLETE_DAG = UNIVERSAL_AT_FINITE_JOINT_SCOPE
UNRESTRICTED_DAG_FAMILY_INCLUDING_COMPLETE_DAG = NOT_SELECTIVE_AT_FAMILY_SCOPE
```

This failure is frozen as:

```text
PGH-FAIL-0031 = UNRESTRICTED_DAG_FAMILY_RESPONSE_CONSTRAINT
```

The result does not say sparse graphs are physically preferable. It says that any response exclusion credited to a DAG grammar must be charged to the fixed graph structure rather than to the mere fact of using DAGs.

## Representation discipline

Renaming variables together with graph incidence and probability arguments transports the theorem covariantly.

No requirement is made that every permutation of `A,B,C` be an automorphism of one fixed directed graph.

Thus the result preserves the PGH covariance/automorphy distinction.

## What the gate establishes

```text
COMPACT_STRUCTURAL_WIRING_CAN_EXCLUDE_RESPONSE_MODELS = YES_FORMAL
LOCAL_KERNEL_VALUES_CAN_REMAIN_FREE = YES
SELECTIVE_INFORMATION_LOCATION = GRAPH_WIRING
GRAPH_PHYSICAL_MEANING = NONE
```

This is the first PGH-1 response-model test in which an explicit non-table structural input removes models from the universally realizable class while leaving local response parameters free.

## What the gate does not establish

```text
A_B_C_ARE_PHYSICAL_VARIABLES = NO
DAG_ARROWS_ARE_PHYSICAL_CAUSES = NO
SPARSE_GRAPH_IS_PHYSICALLY_CORRECT = NO
CAUSAL_GRAPH_IS_GENERATED_BY_EXISTING_PGH_GRAMMAR = NO
R2B = UNSATISFIED
```

## Next scientific operation

Recommended:

```text
PGH1_R2B_CAUSAL_WIRING_PRIMITIVE_GRAMMAR_CANDIDACY_GATE
```

Purpose:

- test whether a fixed sparse Markov/DAG wiring plus free local kernels can enter primitive grammar candidacy under `PGH-OBJ-0020`;
- keep the graph explicit in candidate identity;
- compare against the complete-DAG nonselective control;
- forbid physical interpretation or empirical graph selection;
- determine whether the mechanism is a legitimate new formal grammar candidate rather than merely an external modeling constraint.

## Hard-stop verification

```text
NEW_SOURCE_SEARCH = NO
EMPIRICAL_DATA_USED = NO
GRAPH_SELECTED_BY_PHYSICAL_FIT = NO
ARROWS_CALLED_PHYSICAL_CAUSES = NO
LOCAL_KERNEL_VALUES_FIXED_BY_CANDIDATE = NO
EXISTING_GRAMMAR_IDENTITY_MODIFIED = NO
R2B_SATISFIED = NO
PHYSICAL_LAW_DERIVED = NO
EMPIRICAL_PREDICTION = NONE
FCP_CHANGED = NO
```
