# PGH-1 Network/Source-Independence Structural-Constraint Schema 0.1.0

## Identity

```text
OBJECT_ID = PGH-OBJ-0050
DECLARING_OPERATION = PGH-OP-0100
STATUS = QUALIFIED_TARGET_FREE_FORMAL_SCHEMA
SOURCE_BOUND_MECHANISM = SG4_M3
PHYSICAL_STATUS = NONE
FCP_EFFECT = NONE
```

## Information accounting

```text
D = ordinary finite stochastic composition
W = fixed source-access topology + source-independence/resource assumptions
K = arbitrary local normalized stochastic kernels
E = absent empirical layer
```

The formal model class receives structural-exclusion credit only for consequences that hold for every allowed `K` once `D+W` is fixed.

## Independent-source triangle

Let `U,V,W` be arbitrary finite source variables with mutually independent joint law

\[
p(u,v,w)=p_U(u)p_V(v)p_W(w).
\]

Observed binary roles receive sources pairwise:

```text
A receives U,W
B receives U,V
C receives V,W
NO SOURCE IS COMMON TO A,B,C
```

Local response laws are arbitrary stochastic kernels:

\[
p_A(a\mid u,w),\quad p_B(b\mid u,v),\quad p_C(c\mid v,w).
\]

Thus

\[
\boxed{
p(a,b,c)=\sum_{u,v,w}p_U(u)p_V(v)p_W(w)
 p_A(a\mid u,w)p_B(b\mid u,v)p_C(c\mid v,w)
}
\]

defines `T_ind`.

No source cardinality or numerical local response kernel is selected by the schema.

## Same-topology correlated-source control

`T_corr` uses the same access pattern and local kernels but permits arbitrary `p(u,v,w)` rather than a product source law.

This control isolates the selective contribution of source independence from the pairwise-access diagram itself.

## Common-source control

`T_common` permits one finite source `Lambda` shared by all observed roles:

\[
p(a,b,c)=\sum_\lambda p(\lambda)
 p_A(a\mid\lambda)p_B(b\mid\lambda)p_C(c\mid\lambda).
\]

For finite observed alphabets, `T_common` is universal over joint distributions by taking `lambda=(a,b,c)` and deterministic coordinate projections.

## Formal exclusion witness

Define

\[
p_*(000)=p_*(111)=\tfrac12,
\]

with all other outcomes zero.

`PGH-DER-0033` proves:

```text
p_* NOT_IN T_ind
p_* IN T_corr
p_* IN T_common
```

Thus the exclusion requires the independent-source resource architecture.

## Structural-difference witness

With independent fair binary sources and deterministic local functions

```text
A = 1 iff U=0 and W=0
B = 1 iff U=0 and V=0
C = 1 iff V=0 and W=0
```

the triangle produces

```text
q(000)=4/8
q(001)=1/8
q(010)=1/8
q(100)=1/8
q(111)=1/8
```

`PGH-DER-0034` proves that `q` violates all six role-conditioned independence restrictions in the retired minimal path family, while `p_*` satisfies all three noncollider separator conditional independences.

Therefore the independent-source triangle model class is structurally incomparable with the union of the six retired path model classes at this finite observed scope.

## Explanatory boundary

The mechanism establishes:

```text
FIXED_NETWORK_PLUS_SOURCE_INDEPENDENCE_CAN_EXCLUDE_MODELS_WITH_LOCAL_KERNELS_FREE = YES
```

It does not establish:

```text
WHY_THIS_NETWORK = EXPLAINED
WHY_SOURCE_INDEPENDENCE_IS_PHYSICAL = EXPLAINED
TRIANGLE_TOPOLOGY = PHYSICALLY_PRIVILEGED
STRONG_PGH_CANDIDATE = CREATED
R2B = SATISFIED
```

If network topology and source independence later enter candidate grammar identity as explicit primitives, their physical motivation remains a separate burden. If they are instead supplied by external target physics or semantics, their exclusion power cannot be credited to strong PGH grammar.

Truth over PGH.
