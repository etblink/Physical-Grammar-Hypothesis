# PGH-GRAM-0010 — Independent-Source Triangle Primitive Grammar Candidate 0.1.0

## Status

```text
GRAMMAR_ID = PGH-GRAM-0010
NAME = INDEPENDENT_SOURCE_TRIANGLE_PRIMITIVE_GRAMMAR_CANDIDATE
DECLARING_OPERATION = PGH-OP-0102
FORMAL_STATUS = NONTRIVIAL_FORMAL_CANDIDATE
PHYSICAL_STATUS = PHYSICAL_BRIDGE_UNESTABLISHED
STRONG_PGH_PACKAGE_STATUS = NOT_ADMITTED
FCP_EFFECT = NONE
```

## Primitive doctrine

The grammar declares the following formal structure as primitive candidate content:

```text
OBSERVED_NODE_CLASS = three binary roles
SOURCE_NODE_CLASS = three arbitrary-finite latent/source roles
INCIDENCE = U->{A,B}; V->{B,C}; W->{C,A}
SOURCE_FACTORISATION = p(U,V,W)=p(U)p(V)p(W)
LOCAL_PROCESS_CLASS = arbitrary normalized stochastic kernels compatible with incidence
```

The resulting observed model class is

\[
\mathcal T_{\mathrm{ind}}
=
\left\{
\sum_{u,v,w}p(u)p(v)p(w)
 p_A(a\mid u,w)p_B(b\mid u,v)p_C(c\mid v,w)
\right\}.
\]

Local source cardinalities and local kernel values are model data, not grammar rules.

## Representation identity

The candidate is defined up to graph isomorphism preserving:

```text
OBSERVED_VS_SOURCE_NODE_CLASS
PAIRWISE_SOURCE_INCIDENCE
MUTUAL_SOURCE_INDEPENDENCE
OBSERVED_BINARY_ALPHABET_SIZE
```

Renaming `A,B,C` or `U,V,W` while preserving this structure is representation change, not a new grammar.

The following change candidate identity:

```text
ADDING_OR_REMOVING_A_SOURCE
ADDING_A_COMMON_SOURCE
CHANGING_SOURCE_INDEPENDENCE
CHANGING_THE_INCIDENCE_GRAPH
ADDING_TARGET_SPECIFIC_KERNEL_OR_EQUATION_DATA
CHANGING_OBSERVED_ALPHABET_SIZE_UNDER_THIS_VERSION
```

## Generated formal consequence

`PGH-DER-0033` proves that the grammar excludes the nondegenerate perfect-common-bit distribution for every choice of local kernels and finite source cardinalities.

Thus the model class is proper.

`PGH-DER-0034` proves that this model class is structurally incomparable with the union of the six retired minimal path-CI model classes. The grammar is therefore not a relabeling of `PGH-GRAM-0008` or `PGH-GRAM-0009`.

## Universal/control boundary

If source independence is dropped, the same pairwise incidence can realize the perfect-common-bit witness.

If unrestricted common-source architecture is permitted, every finite observed joint distribution is representable.

Therefore the candidate's selectivity is explicitly charged to:

```text
FIXED_PAIRWISE_SOURCE_TOPOLOGY
+
MUTUAL_SOURCE_INDEPENDENCE
```

and not to its free local kernels.

## Known-result quarantine

This candidate was formalized after the canonical Kp and HURDAT2 results.

```text
Kp_POSITIVE_CREDIT = ZERO
HURDAT2_POSITIVE_CREDIT = ZERO
Kp_HURDAT2_PATTERN_SELECTION = FORBIDDEN
```

The candidate may receive no positive physical evidence until a complete future package `C=(G,J,S,I)` is frozen and confronted with a genuinely prospective target selected afterward.

Existing known targets may only be used under separately preregistered negative/control roles.

## Physical nonclaims

The formal grammar does not assert:

```text
THE_WORLD_HAS_TRIANGLE_SOURCE_TOPOLOGY
THE_THREE_SOURCES_ARE_PHYSICALLY_INDEPENDENT
THE_LATENT_SOURCE_NODES_ARE_CAUSES
A_B_C_ARE_ANY_PARTICULAR_OBSERVABLES
THE_BINARY_ALPHABET_HAS_PHYSICAL_PRIVILEGE
```

Any such claim belongs to a later physical bridge/instantiation package and must not be read back into the present grammar.

## Candidate ceiling

```text
P0_TO_P10_FORMAL_CANDIDACY = PASS_BY_OP0102
P11_PHYSICAL_BRIDGE = UNESTABLISHED
A0_A9_STRONG_SUCCESSOR_ADMISSION = NOT_RUN_FOR_COMPLETE_PACKAGE
PHYSICAL_PREDICTION = NONE
POSITIVE_EMPIRICAL_PGH_CREDIT = NONE
R2B = UNSATISFIED
FCP_EFFECT = NONE
```

Truth over PGH.
