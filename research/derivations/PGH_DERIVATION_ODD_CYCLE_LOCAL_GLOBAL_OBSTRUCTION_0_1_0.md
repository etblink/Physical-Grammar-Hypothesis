# PGH-DER-0012 — Odd-Cycle Local-to-Global Obstruction 0.1.0

## Identity

```text
DERIVATION_ID = PGH-DER-0012
OPERATION_ID = PGH1_R2_LOCAL_TO_GLOBAL_MECHANISM_GATE
STATUS = QUALIFIED_FORMAL_CANDIDATE_PENDING_PROJECT_LEAD_REVIEW
PHYSICAL_CLAIM = NONE
```

## Theorem

Let `n=2k+1` be odd. Put binary variables

\[
x_0,\ldots,x_{n-1}\in\{0,1\}
\]

on the vertices of the cycle `C_n` and impose the same local rule on every edge:

\[
x_i\neq x_{i+1}
\]

with indices modulo `n`.

Then:

1. every edge constraint is individually satisfiable;
2. the support projections of adjacent edge constraints onto their shared vertex agree and equal `{0,1}`;
3. every proper path obtained by deleting one cycle edge is globally satisfiable;
4. the full odd cycle has no global satisfying assignment.

## Proof of global obstruction

Write the edge rule as

\[
x_i\oplus x_{i+1}=1.
\]

Sum all `n` equations modulo 2.

Every variable appears exactly twice on the left, so the left side is

\[
2(x_0+\cdots+x_{n-1})=0\pmod 2.
\]

The right side is

\[
n=1\pmod 2
\]

because `n` is odd.

Thus any global assignment would imply

\[
0=1\pmod 2,
\]

which is impossible.

Therefore:

\[
\operatorname{Glob}(\mathcal L)=\varnothing.
\]

## Local satisfiability

Each edge permits exactly:

```text
(0,1)
(1,0)
```

so every local relation is nonempty.

Projection of either edge relation onto either endpoint is `{0,1}`. Hence overlap supports agree at every shared vertex.

## Proper-substructure control

Delete any one edge from the cycle. The remaining graph is a path.

Choose an arbitrary value for one endpoint and alternate `0,1,0,1,...` along the path. This satisfies every remaining edge.

Thus no proper path already contains the contradiction.

The contradiction is genuinely global to closure around the odd cycle.

## Even-cycle control

For even `n`, the same alternating construction closes consistently and yields exactly two global assignments:

```text
0101...01
1010...10
```

Finite exhaustive checks for `n=3,4,5,6,7,8` reproduce:

```text
n=3 -> 0 solutions
n=4 -> 2 solutions
n=5 -> 0 solutions
n=6 -> 2 solutions
n=7 -> 0 solutions
n=8 -> 2 solutions
```

This shows that the uniform local rule alone does not decree impossibility; the global incidence pattern matters.

## Non-table-driven character

No list of forbidden global binary strings appears in the construction.

The complete specification is:

```text
BINARY_DOMAIN
CYCLE_INCIDENCE
ONE_UNIFORM_EDGE_RULE = endpoints differ
```

The family excludes all global assignments on every odd cycle by one parity argument.

Hence:

```text
NON_TABLE_DRIVEN_GLOBAL_EXCLUSION = YES
COMPACT_GENERATIVE_OR_CONSTRAINT_DESCRIPTION = YES
```

## Representation control

The same theorem appears as:

1. graph theory: odd cycles are not 2-colorable;
2. constraint algebra: the XOR system `x_i XOR x_(i+1)=1` is inconsistent for odd cycle length;
3. local/global extension: all edge supports are locally nonempty and overlap-compatible, but no global binary assignment lies in all local supports.

The obstruction therefore survives these straightforward faithful reformulations.

## What is not proved

The theorem does not establish:

```text
BINARY_VALUES_ARE_PHYSICAL
GRAPH_EDGES_ARE_PHYSICAL_CONTEXTS
INEQUALITY_IS_A_FUNDAMENTAL_PHYSICAL_RULE
ODD_CYCLES_ARE_PHYSICALLY_PRIVILEGED
CONTEXTUALITY_IS_DERIVED_FROM_PGH
PHYSICAL_LAW_DERIVED = NO
```

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = BINARY_DOMAIN; CYCLE_INCIDENCE
RULE_DEPENDENCIES = UNIFORM_EDGE_INEQUALITY
LEMMA_DEPENDENCIES = MOD2_PARITY
SEMANTIC_ASSUMPTIONS = NONE
PHYSICAL_ASSUMPTIONS = NONE
SOURCE_DEPENDENCIES = PGH-R2-SRC-002; PGH-R2-SRC-004; PGH-R2-SRC-006
METALANGUAGE_DEPENDENCIES = GRAPH_THEORY; BOOLEAN_ASSIGNMENTS; MOD2_ARITHMETIC
```

## Verdict

```text
PGH-DER-0012 = QUALIFIED_FORMAL_CANDIDATE_PENDING_REVIEW
LOCAL_TO_GLOBAL_OBSTRUCTION = PROVED
R2_PHYSICAL_CREDIT = NONE
```
