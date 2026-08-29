# PGH-1 R2B Typed Anchor Grammar Interaction Gate — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_R2B_TYPED_ANCHOR_GRAMMAR_INTERACTION_GATE
REGISTRY_ID = PGH-OP-0052
CANONICAL_BASE = a648cba1d674f97f6dac053b2112c430f3ee57d6
TYPED_ANCHOR = PGH-OBJ-0025
CANDIDATE_FAMILY = PGH-GRAM-0003..PGH-GRAM-0007
R2_TARGET = PGH-OBJ-0021
NEW_SOURCE_SEARCH = FORBIDDEN
EMPIRICAL_RESPONSE_DATA = FORBIDDEN
PHYSICAL_RESPONSE_INTERPRETATION = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Determine whether the newly qualified law-free typed anchor can interact nontrivially with the five primitive grammar candidates without importing response structure through the anchor-to-grammar internalization itself.

The gate distinguishes:

```text
TYPED_SEMANTIC_METADATA
GRAMMAR_SIGNATURE_INTERNALIZATION
GRAMMAR_GENERATED_STRUCTURE
PHYSICAL_RESPONSE_INTERPRETATION
```

These may not be collapsed.

## Common setup

Let

\[
T\subseteq C\times R
\]

be a fixed response-underdetermining typed interface satisfying `PGH-OBJ-0025`.

Use the same finite control fiber

```text
C = {c}
R_c = {r0,r1}
```

when a one-context witness suffices.

No target response law, probability, or empirical outcome is used.

## T1 — external-metadata inertness

Represent context and record labels as the same discrete atomic object generators used in the earlier common free-model bridge, while leaving `T` external to the candidate grammar signature.

Test whether

\[
Free_G(S_{ref};T_{external})
\]

has any different grammar-generated morphisms from

\[
Free_G(S_{ref}).
\]

Expected logical control: metadata that is not part of the grammar signature cannot alter grammar derivability merely by being mentioned alongside it.

## T2 — edge internalization control

Internalize every typed pair `(c,r) in T` by adding a generating morphism

\[
e_{c,r}:X_c\to Y_r.
\]

Test whether the resulting trial hom relation contains `T` by construction.

If yes, this internalization cannot receive explanatory credit for generating a cross-type relation later read by morphism existence.

This is an encoding control, not a claim that typed edges are intrinsically physical responses.

## T3 — bicartesian product-output internalization

For a context `c` with typed labels `r0,r1`, in the bicartesian candidate introduce an outcome object by product

\[
O_c=Y_{r0}\times Y_{r1}
\]

and one generic context/process generator

\[
m_c:X_c\to O_c.
\]

No individual `X_c -> Y_ri` response arrow is added.

Test whether product projections generate both

\[
X_c\to Y_{r0},\qquad X_c\to Y_{r1}.
\]

## T4 — bicartesian coproduct-output internalization

Use the same typed fiber and same bicartesian doctrine, but define

\[
O'_c=Y_{r0}+Y_{r1}
\]

with one generic context/process generator

\[
n_c:X_c\to O'_c.
\]

Test whether either individual

\[
X_c\to Y_{r0}\quad\text{or}\quad X_c\to Y_{r1}
\]

is forced by bicartesian structure plus `n_c` alone.

Model-separation proofs in `Set` are allowed.

## T5 — internalization plurality test

If T3 and T4 give different cross-type hom consequences for the same `T` and same grammar doctrine, classify the anchor-to-grammar internalization as substantive additional structure unless a separate non-result-directed principle selects one.

Do not select product or coproduct because of known physical behavior.

## T6 — context-role representation control

Record explicitly that representing a context token as:

```text
ATOMIC_OBJECT
GENERIC_PROCESS_WITH_TYPED_CODOMAIN
OTHER_INTERFACE_STRUCTURE
```

is itself part of the internalization choice.

No representation may be called fundamental merely because it makes a bridge work.

## Outcome space

```text
A = THE_TYPED_ANCHOR_HAS_A_CANONICAL_NON_RESULT_DIRECTED_INTERNALIZATION_IN_AT_LEAST_ONE_FROZEN_GRAMMAR_THAT_GENERATES_NEW_CROSS_TYPE_STRUCTURE_WITHOUT_EDGE_ENCODING__A_SEPARATE_PHYSICAL_MEANING_TEST_IS_JUSTIFIED
B = EXTERNAL_TYPING_IS_STRUCTURALLY_INERT_WHILE_LAWFUL_INTERNALIZATIONS_OF_THE_SAME_TYPING_CAN_CHANGE_CROSS_TYPE_MORPHISM_CONSEQUENCES__THE_INTERNALIZATION_MAP_IS_A_NEW_BRIDGE_BURDEN_AND_R2B_REMAINS_UNSATISFIED
C = EVERY_NONTRIVIAL_INTERNALIZATION_OF_TYPED_ANCHOR_STRUCTURE_IS_EQUIVALENT_TO_PRIMITIVE_RESPONSE_EDGE_ENCODING__TYPED_ANCHOR_CANNOT_INTERACT_LAW_FREE_WITH_CURRENT_GRAMMARS
D = CURRENT_FORMAL_CANDIDATES_ARE_INSUFFICIENT_TO_COMPARE_TYPED_ANCHOR_INTERNALIZATIONS
```

No outcome establishes physical response meaning or empirical adequacy.

## Required outputs

Commit 2 may add only:

```text
audits/PGH1_R2B_TYPED_ANCHOR_GRAMMAR_INTERACTION_GATE_0_1_0.md
research/formalizations/PGH1_TYPED_ANCHOR_GRAMMAR_INTERNALIZATION_SCHEMA_0_1_0.md
research/derivations/PGH_DERIVATION_EXTERNAL_TYPING_STRUCTURAL_INERTNESS_0_1_0.md
research/derivations/PGH_DERIVATION_TYPED_INTERNALIZATION_PLURALITY_0_1_0.md
research/failures/PGH_FAIL_TYPED_ANCHOR_INTERNALIZATION_AS_BRIDGE_SELECTOR_0_1_0.md
handoffs/PGH1_R2B_TYPED_ANCHOR_GRAMMAR_INTERACTION_GATE_HANDOFF_0_1_0.md
```

Expected identities if earned:

```text
PGH-OBJ-0026 = TYPED_ANCHOR_GRAMMAR_INTERNALIZATION_SCHEMA
PGH-DER-0024 = EXTERNAL_TYPING_STRUCTURAL_INERTNESS
PGH-DER-0025 = TYPED_INTERNALIZATION_PLURALITY
PGH-FAIL-0026 = TYPED_ANCHOR_INTERNALIZATION_AS_BRIDGE_SELECTOR
```

## Commit topology

```text
COMMIT_1_MESSAGE = Preregister PGH-1 R2B typed anchor grammar interaction gate
COMMIT_2_MESSAGE = Adjudicate PGH-1 R2B typed anchor grammar interaction gate
EXACT_COMMITS = 2
```

## Hard stops

```text
DO_NOT_SEARCH_NEW_SOURCES
DO_NOT_USE_EMPIRICAL_RESPONSE_DATA
DO_NOT_ADD_TARGET_RESPONSE_FUNCTIONS
DO_NOT_CALL_MORPHISM_EXISTENCE_PHYSICAL_RESPONSE
DO_NOT_SELECT_PRODUCT_OR_COPRODUCT_BY_PHYSICAL_FIT
DO_NOT_TREAT_CONTEXT_AS_OBJECT_OR_PROCESS_WITHOUT_DECLARING_THE_CHOICE
DO_NOT_DECLARE_R2B_SATISFIED
DO_NOT_MAKE_EMPIRICAL_PREDICTIONS
DO_NOT_CHANGE_FCP
```