# PGH-1 Local-to-Global Constraint Schema 0.1.0

## Status

```text
FORMALIZATION = PGH1_LOCAL_TO_GLOBAL_CONSTRAINT_SCHEMA
OPERATION_ID = PGH1_R2_LOCAL_TO_GLOBAL_MECHANISM_GATE
STATUS = PROVISIONAL_FORMAL_SCHEMA
PHYSICAL_GRAMMAR = NO
PHYSICAL_CLAIM = NONE
```

## Abstract datum

A local-constraint presentation is

\[
\mathcal L=(V,D,\mathcal C,\{R_C\}_{C\in\mathcal C}),
\]

where:

- `V` is a finite set of formal positions/variables;
- `D` is a finite value set;
- `C` in `mathcal C` is a local context, a subset of `V`;
- `R_C subseteq D^C` is the set of locally admissible assignments on context `C`.

No physical interpretation is assumed.

## Local satisfiability

A context is locally satisfiable when

\[
R_C\neq\varnothing.
\]

The whole presentation is locally satisfiable when every context is locally satisfiable.

## Overlap compatibility at relation/support level

For contexts `C,C'`, let `pi_I` denote restriction to the overlap

\[
I=C\cap C'.
\]

The local relations are overlap-compatible when

\[
\pi_I(R_C)=\pi_I(R_{C'}).
\]

This is compatibility of the **available local supports**, not the stronger claim that one chosen local assignment from each context forms a matching family.

The distinction matters: an actual family of functions agreeing pointwise on every overlap glues trivially to a function on the union. The obstruction studied here instead asks whether one can choose local assignments simultaneously so that all contexts are satisfied by a single global assignment.

## Global realization

Define

\[
\operatorname{Glob}(\mathcal L)
=
\{g\in D^V:\forall C\in\mathcal C,\ g|_C\in R_C\}.
\]

A local-to-global obstruction occurs when:

```text
EVERY_R_C_NONEMPTY = YES
OVERLAP_SUPPORT_COMPATIBILITY = YES
GLOBAL_REALIZATION_SET = EMPTY
```

This captures the structural pattern identified in the new source corpus without privileging sheaf, graph, hypergraph, or logical notation.

## Uniform-rule specialization

A stronger anti-table specialization is obtained when all local relations arise from one rule schema `R` transported uniformly across contexts of one type.

For graph edges and a fixed binary relation `neq`:

\[
R_{\{u,v\}}=\{(0,1),(1,0)\}
\]

for every edge.

No edge receives a specially tailored constraint.

## Odd-cycle family

Let `V={v_0,...,v_{n-1}}`, `D={0,1}`, and let the contexts be the edges of the cycle `C_n`.

For every edge require:

\[
x_i\neq x_{i+1}\quad (\text{indices mod }n).
\]

Equivalently:

\[
x_i\oplus x_{i+1}=1.
\]

For odd `n`, this produces a local-to-global obstruction.

For even `n`, two alternating global assignments exist.

Thus the same local rule can succeed or fail globally depending on the topology/cover structure.

## Representation controls

The mechanism can be written as:

```text
GRAPH = failure of 2-colorability on odd cycles
XOR = inconsistent parity equations around an odd cycle
LOCAL_GLOBAL_EXTENSION = nonempty compatible edge supports with no global section/assignment
```

The formal theorem therefore does not depend on the word “sheaf.”

## R2 promise

This schema is more structured than arbitrary formation-table exclusion because a compact repeated local rule plus global incidence pattern can imply impossibility that is nowhere individually listed.

However the schema leaves four inputs unearned:

```text
PHYSICAL_PRIVILEGE_OF_V = UNESTABLISHED
PHYSICAL_PRIVILEGE_OF_D = UNESTABLISHED
PHYSICAL_PRIVILEGE_OF_COVER_C = UNESTABLISHED
PHYSICAL_PRIVILEGE_OF_LOCAL_RULE_R = UNESTABLISHED
```

If these are selected to reproduce target physics, the no-smuggling problem returns.

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = FINITE_POSITIONS; FINITE_VALUE_DOMAIN; LOCAL_CONTEXT_FAMILY
RULE_DEPENDENCIES = LOCAL_ADMISSIBILITY_RELATIONS; RESTRICTION_TO_OVERLAPS; GLOBAL_EXTENSION_TEST
LEMMA_DEPENDENCIES = PGH-DER-0012
SEMANTIC_ASSUMPTIONS = NONE
PHYSICAL_ASSUMPTIONS = NONE
SOURCE_DEPENDENCIES = PGH-R2-SRC-001; PGH-R2-SRC-002; PGH-R2-SRC-004; PGH-R2-SRC-005; PGH-R2-SRC-006; PGH-R2-SRC-008; PGH-R2-SRC-009
METALANGUAGE_DEPENDENCIES = FINITE_SETS; FUNCTIONS; RELATIONS; GRAPH_OR_HYPERGRAPH_INCIDENCE; MOD2_ARITHMETIC_FOR_WITNESS
```

## Result

```text
LOCAL_TO_GLOBAL_CONSTRAINT_SCHEMA = FORMALLY_COHERENT
NON_TABLE_DRIVEN_OBSTRUCTION_EXISTS = YES
PHYSICAL_BRIDGE = NONE
SUCCESSOR_GRAMMAR = NONE
```
