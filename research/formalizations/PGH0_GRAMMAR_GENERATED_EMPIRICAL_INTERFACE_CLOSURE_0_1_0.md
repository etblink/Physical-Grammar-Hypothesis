# PGH-0 Grammar-Generated Empirical Interface Closure 0.1.0

## Identity

```text
OBJECT_CLASS = FORMALIZATION
OPERATION_ID = PGH0_GRAMMAR_GENERATED_EMPIRICAL_INTERFACE_CLOSURE_CHALLENGE
STATUS = PROVISIONAL_FORMAL_SCHEMA
PHYSICAL_CLAIM = NONE
```

## Purpose

This artifact records the qualified formal architecture for generating an empirical context family from a small law-free seed without separately listing the complete context universe.

## Data

Let:

```text
P = formal context universe
C0 subseteq P = law-free empirical contact seed
G = candidate grammar presentation
E = fixed response-independent extraction rule
Gamma_G = E(G) = finitary context constructors inherited from the grammar formation skeleton
```

The extraction rule may inspect formal formation structure, arity, type/interface compatibility, and context insertion positions. It may not inspect response values, record profiles, probabilities, empirical success, or a target distinguishability partition.

## Generated closure

Define a subset `S subseteq P` to be `Gamma_G`-closed when every defined constructor result on arguments from `S` also belongs to `S`.

Then define:

\[
C_G^*(C_0)
=
Cl_{\Gamma_G}(C_0)
=
\bigcap\{S\subseteq P:C_0\subseteq S,\ S\text{ is }\Gamma_G\text{-closed}\}.
\]

This is the unique least generated interface containing the seed.

For finitary constructors the same closure is obtained by finite-depth iteration:

\[
C_0\subseteq C_1\subseteq C_2\subseteq\cdots,
\]

where each stage adjoins every constructor output whose finite input tuple is already available, and

\[
C_G^*(C_0)=\bigcup_{n\ge0}C_n.
\]

## Response-law separation

The generated closure is defined before any evaluator `e` or record response law is supplied.

A record profile may subsequently be defined by

\[
O_{G,e}(x)(c)=\rho(e(c,x)),
\qquad c\in C_G^*(C_0),
\]

but `e` and the values of `O` are not inputs to the closure construction.

Therefore multiple incompatible response evaluators may share one generated empirical context family.

## Grammar-extraction convention

At current scope `E` is a formal extraction convention, not a physical law.

A canonical example is **all admissible one-hole context extension**:

- start from the grammar formation constructors/rules;
- hold all but one argument position fixed by well-formed formal expressions;
- treat the remaining position as the context hole;
- include the resulting partial context constructor whenever the original formation rule is formally admissible.

This uses only formation structure.

## Example

Let `G` contain a binary formal constructor `m(-,-)` and a well-formed ground term `a`.

The extraction gives context constructors such as

\[
L_a(C)=m(C,a),
\qquad
R_a(C)=m(a,C).
\]

With seed `C0={square}`, generated contexts include:

\[
\square,
\quad m(\square,a),
\quad m(a,\square),
\quad m(m(\square,a),a),
\quad \ldots
\]

No extensional list of this family is primitive.

## What the schema removes

Relative to fixed `(G,E,C0)`, the architecture does not require a separate object

```text
COMPLETE_EMPIRICAL_CONTEXT_LIST
```

or an arbitrary closure table specifying membership context by context.

## What the schema does not remove

It does not justify:

```text
PHYSICAL_PRIVILEGE_OF_G
PHYSICAL_PRIVILEGE_OF_E
PHYSICAL_PRIVILEGE_OF_C0
PHYSICAL_COMPLETENESS_OF_C_G_STAR
UNIQUENESS_OF_EMPIRICAL_GENERATING_SEED
PHYSICAL_RESPONSE_LAW
```

A sufficiently unconstrained grammar can itself encode arbitrary structure. The schema therefore removes one independent oracle but does not solve the foundational selection problem.

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = PGH-GRAM-0002; LAW_FREE_EMPIRICAL_CONTACT_SEED
RULE_DEPENDENCIES = RESPONSE_INDEPENDENT_GRAMMAR_TO_CONTEXT_EXTRACTION; LEAST_CLOSURE
LEMMA_DEPENDENCIES = PGH-DER-0009
SEMANTIC_ASSUMPTIONS = SEED_TOKENS_HAVE_EMPIRICAL_REFERENCE_ONLY
PHYSICAL_ASSUMPTIONS = NONE_BEYOND_UNESTABLISHED_EMPIRICAL_CONTACT_REFERENCE
SOURCE_DEPENDENCIES = FROZEN_37_SOURCE_LANDSCAPE
METALANGUAGE_DEPENDENCIES = SETS_OR_CLASSES; PARTIAL_FINITARY_OPERATIONS; INTERSECTIONS; FIXED_POINTS
```

## Status

```text
GRAMMAR_GENERATED_INTERFACE_CLOSURE = FORMALLY_FEASIBLE
SEPARATE_CLOSURE_ORACLE = NOT_REQUIRED_RELATIVE_TO_FIXED_G_E_C0
PHYSICAL_COMPLETENESS = UNESTABLISHED
R1_SOLVED = NO
R2_STARTED = NO
```
