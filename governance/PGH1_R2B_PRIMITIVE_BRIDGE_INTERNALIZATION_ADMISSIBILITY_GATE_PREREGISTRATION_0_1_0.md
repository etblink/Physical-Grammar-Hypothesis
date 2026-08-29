# PGH-1 R2B Primitive Bridge Internalization Admissibility Gate — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_R2B_PRIMITIVE_BRIDGE_INTERNALIZATION_ADMISSIBILITY_GATE
REGISTRY_ID = PGH-OP-0053
CANONICAL_BASE = ef2b2a0e8e9dfe1ae8f5f584eff4556db7220139
TYPED_ANCHOR = PGH-OBJ-0025
INTERNALIZATION_SCHEMA = PGH-OBJ-0026
CANDIDATE_GRAMMARS = PGH-GRAM-0003..PGH-GRAM-0007
R2_TARGET = PGH-OBJ-0021
NEW_SOURCE_SEARCH = FORBIDDEN
EMPIRICAL_RESPONSE_DATA = FORBIDDEN
PHYSICAL_RESPONSE_INTERPRETATION = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Define and test a stopping rule for **primitive bridge/internalization hypotheses** analogous to the primitive-grammar admissibility standard `PGH-OBJ-0020`.

The operation must avoid two opposite errors:

1. demanding that every bridge primitive be derived from a still deeper bridge, creating a mandatory regress;
2. allowing an arbitrary response table or equivalent encoding to enter merely because it is labeled an internalization.

The gate tests formal bridge candidacy only. It may not establish physical correctness or R2B success.

## Primitive bridge admissibility standard to test

A primitive internalization `I` may enter formal bridge candidacy only if all of the following are satisfied:

```text
P0_EXPLICIT_PREREGISTRATION = YES
P1_PRE_TARGET_FIXATION = YES
P2_RESPONSE_UNDERDETERMINATION = YES
P3_COMPONENT_EDGE_EQUIVALENT_ENCODING = NO
P4_NONTRIVIAL_CROSS_TYPE_FORMAL_CONSEQUENCE = YES
P5_REPRESENTATION_COVARIANCE = YES_OR_EXPLICITLY_TESTABLE
P6_DECLARED_DEPENDENCE_ON_GRAMMAR_DOCTRINE = YES
P7_COUNTEREXAMPLE_EXPOSURE = YES
P8_MORPHISM_AS_PHYSICAL_RESPONSE = FORBIDDEN
P9_EMPIRICAL_FIT_USED_TO_CHOOSE_I = NO
```

No scalar score is allowed. A hard failure of P1, P2, P3, P8, or P9 blocks candidacy.

## Frozen controls

### I0 — external typed metadata only

`T` remains outside the grammar signature.

Expected role: inert control under `PGH-DER-0024`.

### I1 — direct edge internalization

For every typed pair add

\[
e_{c,r}:X_c\to Y_r.
\]

Expected role: reject as extensional cross-type edge encoding.

### I2 — product-packaged edge tuple

For a two-record fiber add

\[
m_c:X_c\to Y_{r_0}\times Y_{r_1}.
\]

Expected role: reject as information-equivalent to the component arrow pair by the product universal property.

### I3 — coproduct aggregate-output process

For each finite nonempty typed fiber

\[
R_c=\{r_1,\dots,r_n\},
\]

in a candidate grammar with finite coproducts, define

\[
O_c=\coprod_{r\in R_c}Y_r
\]

and add exactly one generic process generator

\[
n_c:X_c\to O_c.
\]

No component morphism `X_c -> Y_r` is primitive.

Test whether:

1. `n_c` is formally nontrivial cross-type structure;
2. individual component arrows remain unforced in the free coproduct/bicartesian controls;
3. the same primitive remains compatible with at least two incompatible response laws on the same typed fiber;
4. the construction transports covariantly under relabeling of `C`, `R`, and the typed fibers;
5. it is not information-equivalent to the component edge family under the coproduct universal property.

### I4 — context-role control

The bridge standard must record that representing a context as the source of a process is itself part of `I`.

This may enter candidacy as a declared primitive role assignment, but it may not be called derived or physically fundamental merely because the bridge test benefits from it.

## Locked theorem T1 — coproduct non-component selection

For a fiber with at least two atomic record objects, show that a generator

\[
n:X\to\coprod_i Y_i
\]

in the free coproduct/bicartesian presentation does not, by coproduct structure alone, force any particular component arrow

\[
X\to Y_i.
\]

Model-separation in `Set` is permitted and must cover each component by assigning that component the empty set while the coproduct remains inhabited through another summand.

## Locked comparison T2 — product versus coproduct information content

Record explicitly:

\[
Hom(X,\prod_iY_i)\cong\prod_i Hom(X,Y_i),
\]

while no analogous natural equivalence

\[
Hom(X,\coprod_iY_i)\cong\prod_i Hom(X,Y_i)
\]

holds in general.

This is an anti-compression control.

## Locked response-underdetermination T3

Hold `T` and `I3` fixed. Reuse the response multiplicity established by `PGH-DER-0023` for a multi-element typed fiber.

The gate must verify that `I3` does not itself select one of those response sections or a probability distribution.

If a physical interpretation of `n_c` is needed to establish that claim, the result must remain at formal semantic scope.

## Outcome space

```text
A = A_STRICT_PRIMITIVE_BRIDGE_ADMISSIBILITY_STANDARD_IS_COHERENT_AND_AT_LEAST_ONE_GENERIC_AGGREGATE_OUTPUT_INTERNALIZATION_PASSES_FORMAL_CANDIDACY_WITHOUT_COMPONENT_EDGE_ENCODING__PHYSICAL_MEANING_AND_R2B_REMAIN_UNESTABLISHED
B = THE_STANDARD_IS_COHERENT_BUT_ALL_TESTED_INTERNALIZATIONS_ARE_INERT_RESPONSE_DETERMINING_OR_INFORMATION_EQUIVALENT_TO_COMPONENT_EDGE_INPUT__NO_FORMAL_BRIDGE_CANDIDATE_SURVIVES
C = ANY_PRIMITIVE_BRIDGE_INTERNALIZATION_STRONG_ENOUGH_TO_INTERACT_WITH_THE_GRAMMAR_NECESSARILY_COLLAPSES_INTO_SUBSTANTIVE_RESPONSE_LAW__ANCHORED_R2B_IS_BLOCKED_FOR_THE_CURRENT_CANDIDATE_FAMILY
D = A_NONTRIVIAL_FORMAL_BRIDGE_CANDIDATE_EXISTS_BUT_THE_PRESENT_STANDARD_CANNOT_DISTINGUISH_IT_FROM_RESPONSE_LAW_WITHOUT_A_SPECIFIC_SOURCE_OR_SEMANTIC_GAP_AUDIT
```

No outcome establishes physical response meaning, empirical adequacy, or R2B success.

## Required outputs

Commit 2 may add only:

```text
audits/PGH1_R2B_PRIMITIVE_BRIDGE_INTERNALIZATION_ADMISSIBILITY_GATE_0_1_0.md
research/formalizations/PGH1_PRIMITIVE_BRIDGE_INTERNALIZATION_ADMISSIBILITY_STANDARD_0_1_0.md
research/formalizations/PGH1_COPRODUCT_AGGREGATE_OUTPUT_BRIDGE_CANDIDATE_0_1_0.md
research/derivations/PGH_DERIVATION_COPRODUCT_AGGREGATE_RESPONSE_NONSELECTION_0_1_0.md
research/failures/PGH_FAIL_BRIDGE_EDGE_EQUIVALENT_INTERNALIZATIONS_0_1_0.md
handoffs/PGH1_R2B_PRIMITIVE_BRIDGE_INTERNALIZATION_ADMISSIBILITY_GATE_HANDOFF_0_1_0.md
```

Expected identities if earned:

```text
PGH-OBJ-0027 = PRIMITIVE_BRIDGE_INTERNALIZATION_ADMISSIBILITY_STANDARD
PGH-OBJ-0028 = COPRODUCT_AGGREGATE_OUTPUT_BRIDGE_CANDIDATE
PGH-DER-0026 = COPRODUCT_AGGREGATE_RESPONSE_NONSELECTION
PGH-FAIL-0027 = BRIDGE_EDGE_EQUIVALENT_INTERNALIZATIONS
```

## Commit topology

```text
COMMIT_1_MESSAGE = Preregister PGH-1 R2B primitive bridge internalization admissibility gate
COMMIT_2_MESSAGE = Adjudicate PGH-1 R2B primitive bridge internalization admissibility gate
EXACT_COMMITS = 2
```

## Hard stops

```text
DO_NOT_SEARCH_NEW_SOURCES
DO_NOT_USE_EMPIRICAL_RESPONSE_DATA
DO_NOT_SELECT_I_BY_PHYSICAL_FIT
DO_NOT_INTERPRET_GENERIC_PROCESS_AS_OBSERVED_OR_POSSIBLE_RESPONSE
DO_NOT_CALL_PRODUCT_PACKAGING_COMPRESSION
DO_NOT_ASSIGN_A_NEW_PGH_GRAM_ID_TO_A_BRIDGE_ENRICHMENT
DO_NOT_DECLARE_PHYSICAL_BRIDGE_QUALIFIED
DO_NOT_DECLARE_R2B_SATISFIED
DO_NOT_MAKE_EMPIRICAL_PREDICTIONS
DO_NOT_CHANGE_FCP
```