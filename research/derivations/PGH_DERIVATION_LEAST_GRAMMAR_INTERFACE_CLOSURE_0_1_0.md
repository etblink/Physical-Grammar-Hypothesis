# PGH-DER-0009 — Least Grammar Interface Closure 0.1.0

## Identity

```text
DERIVATION_ID = PGH-DER-0009
OPERATION_ID = PGH0_GRAMMAR_GENERATED_EMPIRICAL_INTERFACE_CLOSURE_CHALLENGE
STATUS = QUALIFIED_FORMAL
PHYSICAL_CLAIM = NONE
```

## Theorem 1 — Unique least constructor closure

Let `P` be a formal context universe, `C0 subseteq P`, and `Gamma` a family of partial finitary constructors valued in `P`.

Let

\[
\mathcal F=\{S\subseteq P:C_0\subseteq S\text{ and }S\text{ is }\Gamma\text{-closed}\}.
\]

Then

\[
Cl_\Gamma(C_0)=\bigcap_{S\in\mathcal F}S
\]

exists and is the unique least `Gamma`-closed superset of `C0`.

### Proof

`P` itself belongs to `F`, so `F` is nonempty. Every member contains `C0`, hence the intersection contains `C0`. Suppose a constructor `gamma` is defined on a finite tuple of elements of the intersection. Those arguments lie in every member of `F`; closure of each member therefore places `gamma` of that tuple in every member, hence in the intersection. Thus the intersection is closed. It is contained in every member of `F` by definition, so it is least. Least elements are unique. QED.

## Theorem 2 — Finitary iterative construction

Define

\[
C_{n+1}=C_n\cup\{\gamma(\vec c):\gamma\in\Gamma,\ \vec c\in C_n^{k_\gamma},\ \gamma(\vec c)\text{ defined}\}
\]

and

\[
C_\omega=\bigcup_{n\ge0}C_n.
\]

For finitary constructors,

\[
C_\omega=Cl_\Gamma(C_0).
\]

### Proof

Every stage lies in every closed superset of `C0` by induction, so `C_omega` is contained in the least closure. Conversely, any finite argument tuple drawn from `C_omega` is contained in some common stage `C_N`; its constructor result appears in `C_{N+1}`. Hence `C_omega` is closed and contains `C0`, so the least closure is contained in `C_omega`. QED.

## Theorem 3 — Response-law separation

If `C0` and `Gamma` are specified without reference to evaluator `e` or record map values, then `Cl_Gamma(C0)` is invariant under replacement of `e` by any other evaluator on the same formal context family.

### Proof

The definition of `Cl_Gamma(C0)` contains only `P`, `C0`, and `Gamma`. No occurrence of `e` or `rho(e(...))` enters the closure predicate. Therefore changing `e` cannot change the generated set. QED.

## Theorem 4 — No independent closure oracle under fixed grammar extraction

Let `E` be a fixed response-independent map from a grammar formation skeleton `G` to a constructor family `Gamma_G=E(G)`. Once `(G,E,C0)` is fixed,

\[
C_G^*(C_0)=Cl_{E(G)}(C_0)
\]

is fixed as well.

Therefore no additional independently selected extensional probe list or closure table is required to determine the formal generated interface.

### Scope

This is a dependency/nonduplication theorem. It does not prove that `G`, `E`, or `C0` is physically privileged.

## Nontrivial witness

Take `C0={c}` and unary constructors `L,R` producing distinct formal contexts.

At exact constructor depth `n`, there are `2^n` words in `{L,R}` applied to `c`. Through depth `n` there are

\[
2^{n+1}-1
\]

contexts.

Thus a one-element seed has a strictly larger, unbounded finite-depth closure.

Define two evaluators on the same closure:

```text
e_const(c',x)=u
```

for all contexts, and

```text
e_parity(c',x)=u  if depth(c') is even
e_parity(c',x)=v  if depth(c') is odd.
```

They yield incompatible record profiles while sharing exactly the same closure.

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = LAW_FREE_SEED; FORMAL_CONTEXT_UNIVERSE
RULE_DEPENDENCIES = FINITARY_CONSTRUCTOR_CLOSURE; OPTIONAL_FIXED_GRAMMAR_EXTRACTION
LEMMA_DEPENDENCIES = INTERSECTION_OF_CLOSED_SUPERSETS; FINITARY_STAGE_ARGUMENT
SEMANTIC_ASSUMPTIONS = NONE_BEYOND_LAW_FREE_SEED_REFERENCE
PHYSICAL_ASSUMPTIONS = NONE
SOURCE_DEPENDENCIES = FROZEN_37_SOURCE_LANDSCAPE
METALANGUAGE_DEPENDENCIES = SETS_OR_CLASSES; PARTIAL_OPERATIONS; INTERSECTION; NATURAL_NUMBER_ITERATION
```

## Result

```text
PGH-DER-0009 = QUALIFIED_FORMAL
LEAST_INTERFACE_CLOSURE = EXISTS_UNIQUELY
FINITE_SEED_NONTRIVIAL_EXPANSION = YES
RESPONSE_LAW_SEPARATION = YES
SEPARATE_CLOSURE_ORACLE_REQUIRED_RELATIVE_TO_FIXED_G_E_C0 = NO
PHYSICAL_COMPLETENESS = NOT_ESTABLISHED
```
