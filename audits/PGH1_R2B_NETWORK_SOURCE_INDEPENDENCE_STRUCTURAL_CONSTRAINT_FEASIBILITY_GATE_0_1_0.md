# PGH-1 R2B Network/Source-Independence Structural-Constraint Feasibility Gate 0.1.0

## Identity

```text
OPERATION_ID = PGH1_R2B_NETWORK_SOURCE_INDEPENDENCE_STRUCTURAL_CONSTRAINT_FEASIBILITY_GATE
REGISTRY_ID = PGH-OP-0100
PREREGISTRATION_COMMIT = 180b980f73ed87ae785a4a9f92411f724b63875f
CANONICAL_BASE = feadbdc4e14051ad3fca21bec88d0603fb6033ef
SOURCE_BOUND_MECHANISM = SG4_M3
NEW_SOURCE_SEARCH = NO
EMPIRICAL_DATA = NO
TARGET_DISCOVERY = NO
FCP_EFFECT = NONE
```

## Outcome

```text
OUTCOME = A__FORMAL_M3_FEASIBILITY_PASS__INDEPENDENT_SOURCE_NETWORK_GIVES_EXACT_NONTRIVIAL_EXCLUSION_STRUCTURALLY_DIFFERENT_FROM_RETIRED_PATH_CI__SELECTIVE_INPUTS_EXPLICIT__NO_PHYSICAL_CANDIDACY
```

The SG4 M3 mechanism is formally real at the tested finite scope.

A fixed pairwise-source triangle with mutually independent sources excludes at least one finite observed distribution for **all** local stochastic kernels. The exclusion disappears when source independence is dropped, and a common-source control is universal. A separate exact witness shows that the independent-source triangle can generate a distribution violating every independence restriction in the retired six-member minimal path family.

Therefore the mechanism is not merely a renamed sparse-DAG conditional-independence constraint.

No physical network, source-independence principle, or strong-PGH candidate is qualified by this result.

## 1. W1 — common-bit exclusion

The preregistered witness is

\[
p_*(000)=p_*(111)=\tfrac12.
\]

`PGH-DER-0033` proves for arbitrary finite source cardinalities and arbitrary local stochastic kernels that

\[
\boxed{p_*\notin T_{\mathrm{ind}}}.
\]

The proof does not assume deterministic kernels. Perfect observed agreement first forces each local kernel, at every positive-probability source triple, to have singleton support with the same output bit. The pairwise source-access equations then force that common bit to be independent of each source argument and hence constant. A nondegenerate shared random bit is impossible.

```text
W1 = PASS
LOCAL_KERNELS_FIXED_NUMERICALLY = NO
SOURCE_CARDINALITIES_FIXED = NO
EXCLUSION_HOLDS_MODEL_CLASS_WIDE = YES
```

## 2. C1 — same topology without source independence

With the same pairwise-access topology, permit arbitrary source correlation and set

\[
U=V=W=L
\]

for a fair common bit `L`. Each observed node returns the bit it receives.

Then the model realizes `p_*` exactly.

```text
C1 = PASS
PAIRWISE_ACCESS_TOPOLOGY_ALONE_EXCLUDES_p_* = NO
SOURCE_INDEPENDENCE_IS_ESSENTIAL_TO_W1 = YES
```

This is decisive input accounting: the exclusion cannot be credited merely to drawing a triangle diagram.

## 3. C2 — common-source universality

For arbitrary finite `q(a,b,c)`, set

\[
\Lambda=(a,b,c),\qquad p(\Lambda=(a,b,c))=q(a,b,c),
\]

and use deterministic coordinate projections.

This realizes every finite joint distribution.

```text
C2 = PASS
COMMON_SOURCE_CONTROL = FINITE_JOINT_UNIVERSAL
```

Thus allowing unrestricted common resource architecture restores the same kind of universality control that has repeatedly mattered throughout PGH.

## 4. W2 — triangle model violates all retired path independences

The preregistered fair-bit triangle construction yields

```text
q(000)=1/2
q(001)=1/8
q(010)=1/8
q(100)=1/8
q(111)=1/8
```

with all other outcomes zero.

This is an explicit member of `T_ind`.

### Marginal independence checks

For each observed role,

\[
P(A=1)=P(B=1)=P(C=1)=\tfrac14.
\]

For each pair,

\[
P(A=1,B=1)=P(A=1,C=1)=P(B=1,C=1)=\tfrac18,
\]

where independence would require `1/16`.

Therefore all three collider-center marginal-independence restrictions fail.

### Conditional independence checks

For `A independent B | C`, condition on `C=0`:

\[
P(C=0)=\tfrac34,
\]

\[
P(A=1\mid C=0)=P(B=1\mid C=0)=\tfrac16,
\]

but

\[
P(A=1,B=1\mid C=0)=0\neq\tfrac1{36}.
\]

By cyclic symmetry, identical calculations refute

\[
B\perp C\mid A
\]

and

\[
A\perp C\mid B.
\]

Hence

```text
W2A = PASS__q_IN_T_ind
W2B = PASS__A_NOT_INDEPENDENT_C
W2C = PASS__A_NOT_INDEPENDENT_B_GIVEN_C
W2D = PASS__A_NOT_INDEPENDENT_B
W2E = PASS__B_NOT_INDEPENDENT_C_GIVEN_A
W2F = PASS__B_NOT_INDEPENDENT_C
W2G = PASS__A_NOT_INDEPENDENT_C_GIVEN_B
```

The independent-source triangle therefore contains a distribution outside the union of all six retired path model classes.

## 5. Reverse incomparability control

For `p_*`, conditioning on any one role fixes the other two deterministically to the same bit. Thus

\[
A\perp C\mid B,
\qquad
A\perp B\mid C,
\qquad
B\perp C\mid A.
\]

So `p_*` belongs to the retired noncollider path-family union.

Yet W1 proves `p_*` is outside the independent-source triangle.

Together:

```text
EXISTS q: q IN T_ind AND q NOT_IN MINIMAL_PATH_UNION
EXISTS p_*: p_* IN MINIMAL_PATH_UNION AND p_* NOT_IN T_ind
```

Therefore

```text
T_ind VS RETIRED_MINIMAL_PATH_FAMILY = MODEL_CLASS_INCOMPARABLE
M3 = STRUCTURALLY_DIFFERENT_FROM_ROTATING_ANOTHER_PATH_CI
```

This establishes the key scientific purpose of OP-0100.

## 6. C3 — unrestricted architecture control

The common-source universality proof establishes that if resource architecture is left unrestricted enough to include a shared latent carrying the full joint outcome, finite-joint selectivity disappears.

Accordingly:

```text
FIXED_INDEPENDENT_SOURCE_ARCHITECTURE_CAN_BE_SELECTIVE = YES
UNRESTRICTED_RESOURCE_ARCHITECTURE_IS_SELECTIVE = NO_AT_TESTED_SCOPE
```

The same lesson that applied to graph families therefore survives at a richer level: the mechanism family is not explanatory until the restrictive structural member is part of the declared hypothesis identity.

## 7. What source independence is doing

The strongest positive result is not “networks constrain probability” in the abstract.

It is:

\[
\boxed{
\text{fixed source-access topology}
+
\text{mutual source independence}
\Longrightarrow
\text{a proper observed model class}
}
\]

while local stochastic kernels remain free.

This is exactly the SG4 structural-vs-model-data distinction.

But the same proof reveals where the substantive information lives:

```text
W_TOPOLOGY = SELECTIVE_INPUT
W_SOURCE_INDEPENDENCE = SELECTIVE_INPUT
K_LOCAL_KERNEL_VALUES = FREE
E_EMPIRICAL_VALUES = ABSENT
```

Dropping source independence admits the excluded witness. Adding unrestricted common resources restores universality. The source/resource assumptions therefore do real work and may not be treated as neutral semantics.

## 8. Relation to primitive-grammar stopping rule

The canonical stopping-rule adjudication permits explicit primitive structural content without requiring infinite meta-derivation.

Therefore OP-0100 does **not** classify the existence of a primitive source-independence axiom as an automatic failure.

However:

```text
FORMALLY_PERMISSIBLE_PRIMITIVE != PHYSICALLY_MOTIVATED_PRIMITIVE
```

The present gate establishes only that such explicit structure can generate a nontrivial exclusion.

Before a strong-PGH candidate can exist, a separate target-free gate must determine whether network topology and source independence can enter candidate grammar identity without either:

1. being selected because of desired empirical behavior;
2. being supplied by an external physical causal/resource story that does the substantive law-selection work;
3. becoming an unrestricted family whose flexibility restores universality.

## 9. Why Outcome B is rejected

Outcome B would say the tested network supplies only ordinary CI or normalization constraints.

That is false at this finite scope. The two-direction witness proves model-class incomparability with the entire six-member path-CI union.

## 10. Why Outcome C is rejected

No extra settings, measurement choices, Bell scenario, quantum resource, or unfrozen auxiliary assumption was needed.

The exact exclusion follows from the preregistered finite triangle topology, mutual source independence, and arbitrary local stochastic kernels.

Therefore the current schema is complete for the tested formal question.

## 11. Why Outcome D is rejected

The W1 theorem covers arbitrary finite latent cardinalities and arbitrary local kernels. Enlarging `K` within the declared class does not restore `p_*`.

## 12. Why Outcome E is rejected

The frozen SG4 corpus and the self-contained finite proof suffice. No new source search is needed for formal feasibility.

## 13. Scientific disposition

Create and retain:

```text
PGH-OBJ-0050 = NETWORK_SOURCE_INDEPENDENCE_STRUCTURAL_CONSTRAINT_SCHEMA
PGH-DER-0033 = TRIANGLE_INDEPENDENT_SOURCE_COMMON_BIT_EXCLUSION
PGH-DER-0034 = TRIANGLE_PATH_CI_INCOMPARABILITY_WITNESS
```

All receive **formal** status only.

No candidate grammar ID is created.

The next scientifically appropriate question is not another network topology and not a target. It is the status of the selective inputs just exposed:

```text
CAN_FIXED_NETWORK_TOPOLOGY_AND_SOURCE_INDEPENDENCE_BE_ADMITTED_AS_EXPLICIT_PRIMITIVE_GRAMMAR_CONTENT
WITHOUT_RELOCATING_SUBSTANTIVE_PHYSICAL_LAW_INTO_RESOURCE_ARCHITECTURE?
```

Recommended next operation:

```text
PGH1_R2B_NETWORK_SOURCE_INDEPENDENCE_PRIMITIVE_INPUT_ADMISSIBILITY_GATE
```

That gate must remain target-free and must be allowed to conclude that the formal mechanism cannot earn strong-PGH physical candidacy.

## Claim ceiling

```text
M3_FORMAL_FEASIBILITY = PASS
STRUCTURALLY_DIFFERENT_FROM_RETIRED_PATH_CI = YES
PHYSICAL_NETWORK_SELECTED = NO
SOURCE_INDEPENDENCE_PHYSICALLY_PRIVILEGED = NO
STRONG_PGH_CANDIDATE = NONE
PHYSICAL_LAW_DERIVED = NO
POSITIVE_EMPIRICAL_PGH_CREDIT = NONE
R2B = UNSATISFIED
FCP_EFFECT = NONE
```

## Stop verification

```text
NEW_SOURCE_SEARCH = NO
EMPIRICAL_DATA = NO
TARGET_DISCOVERY = NO
PHYSICAL_TOPOLOGY_SELECTION = NO
CANDIDATE_ADMISSION = NO
SEMANTIC_TARGET_BRIDGE = NO
Kp_HURDAT2_PATTERN_USE = NO
FCP_CHANGED = NO
```

Truth over PGH.
