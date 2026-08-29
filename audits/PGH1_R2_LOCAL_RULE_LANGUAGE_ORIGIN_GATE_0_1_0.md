# PGH-1 R2 Local Rule Language Origin Gate — Adjudication 0.1.0

## Identity

```text
OPERATION_ID = PGH1_R2_LOCAL_RULE_LANGUAGE_ORIGIN_GATE
REGISTRY_ID = PGH-OP-0040
CANONICAL_BASE = 9e749614eca75beb103e91a08921c447d2698fbd
PREREGISTRATION_COMMIT = 1c0649d13cfd63a463f12a82aa50c61b63ead66e
WORKING_TARGET = PGH-OBJ-0012
LOCAL_ADMISSIBILITY_FAMILY_MAP = PGH-OBJ-0015
FROZEN_ACCEPTED_SOURCE_COUNT = 51
NEW_SOURCE_SEARCH = NONE
FCP_EFFECT = NONE
```

## Outcome

```text
OUTCOME = B__CANONICAL_OR_INVARIANT_META_LANGUAGE_CONSTRUCTIONS_EXIST_BUT_ARE_NONSELECTIVE_TOO_WEAK_OR_INHERIT_UNEARNED_SIGNATURE_TYPE_PROJECTION_SYMMETRY_OR_PRIMITIVE_STRUCTURE__NO_SUCCESSOR_GRAMMAR
SUCCESSOR_GRAMMAR_QUALIFIED = NO
R2_SATISFIED = NO
PHYSICAL_LAW_DERIVED = NO
```

## Executive result

This gate tests whether the language used to generate proper local admissibility supports can itself be fixed before seeing the support patterns or physical exclusions it will later generate.

The answer at current scope is negative, but not because meta-language construction is impossible.

Several mathematically canonical constructions exist:

- free/initial term languages conditional on a signature;
- automorphism-invariant relation languages conditional on a base structure and group action;
- role/type languages conditional on compositional incidence;
- coherence/equation languages conditional on a presentation projection;
- common structural cores conditional on a chosen class of representations.

The problem is explanatory location. Every tested construction is either:

1. too nonselective to generate a nontrivial support by itself; or
2. selective only because the signature, type structure, projection, symmetry action, primitive vocabulary, or representation class already contains the decisive information.

No tested construction simultaneously fixes the meta-language non-result-directly and generates a uniquely or otherwise independently privileged proper local support.

## T1 — Free-language nonselection

Let `Sigma` be a fixed many-sorted signature and let `T_Sigma(X)` be the free term algebra on variables/generators `X`, with no added equations.

Take two syntactically distinct well-sorted terms `t` and `u` of the same sort.

In the free term algebra, the interpretations of those terms are the terms themselves. Hence

\[
t\neq u
\]

in `T_Sigma(X)`.

Therefore the equation

\[
t=u
\]

cannot be valid in every `Sigma`-algebra unless it is already syntactic identity (modulo whatever definitional equality has been built into the term formation system).

Thus:

```text
FREE_TERM_GENERATION = CANONICAL_CONDITIONAL_ON_SIGNATURE
NONTRIVIAL_EQUATIONAL_LAW_FROM_FREE_GENERATION_ALONE = NO
```

A free language can impose arity/sort/typing restrictions, but those restrictions are carried by the signature/type formation rules supplied to the free construction.

This result is recorded as `PGH-DER-0015`.

## T2 — Renaming-invariant relation multiplicity

Let `D` be a finite set with no structure beyond identity, and let the full symmetric group `S_D` act diagonally on `D^n`.

An invariant relation is a union of action orbits.

### Binary case

For `|D| >= 2`, the action on `D^2` has exactly two orbits:

1. the diagonal
   \[
   \Delta=\{(x,x):x\in D\};
   \]
2. the off-diagonal
   \[
   \nabla=\{(x,y):x\neq y\}.
   \]

Therefore there are exactly

\[
2^2=4
\]

full-renaming-invariant binary supports:

```text
EMPTY
EQUALITY_ONLY
INEQUALITY_ONLY
FULL
```

Two are nontrivial proper supports. Renaming invariance therefore does not uniquely choose one.

### Ternary case

For `|D| >= 3`, the action on `D^3` has five equality-pattern orbits, corresponding to the five set partitions of three argument positions:

```text
AAA
AAB
ABA
ABB
ABC
```

Hence there are

\[
2^5=32
\]

full-renaming-invariant ternary supports.

More generally, for `|D| >= n`, the orbits correspond to the Bell-number `B_n` equality patterns, so there are

\[
2^{B_n}
\]

renaming-invariant `n`-ary supports.

Thus:

```text
FULL_RENAMING_INVARIANCE = STRONG_ARBITRARITY_REDUCTION
FULL_RENAMING_INVARIANCE = NOT_UNIQUE_RULE_SELECTION
```

This result is recorded as `PGH-DER-0016`.

## M0 — unrestricted primitive adjunction

```text
STATUS = REJECT
```

For arbitrary target support `R`, adding a primitive predicate symbol `P_R` interpreted exactly as `R` makes the support one-symbol short while leaving its information content primitive.

Therefore:

```text
ONE_SYMBOL_DESCRIPTION != EXPLANATORY_COMPRESSION
```

The same objection applies to primitive operations, types, rewrite rules, or symmetry labels whose interpretation is chosen after the target support is known.

## M1 — free / initial language

```text
CANONICALITY = PASS_CONDITIONAL_ON_SIGNATURE
TARGET_RESULT_INDEPENDENCE = PASS_IF_SIGNATURE_PREEXISTS
SELECTIVITY_BEYOND_SIGNATURE = FAIL
R2_STATUS = CONDITIONAL_NOT_SUFFICIENT
```

The free construction solves a generativity problem, not the origin of its signature.

If the signature is untyped and unconstrained, free generation creates syntax but no nontrivial equations.

If the signature is typed or partial, it can exclude ill-formed compositions, but the selective content has moved into the type/arity/domain declarations.

## M2 — automorphism-invariant language

```text
CANONICALITY = PASS_CONDITIONAL_ON_BASE_STRUCTURE
REPRESENTATION_DISCIPLINE = STRONG
UNIQUE_NONTRIVIAL_SUPPORT = FAIL
SYMMETRY_ACTION_ORIGIN = UNESTABLISHED
R2_STATUS = CONDITIONAL_NOT_SUFFICIENT
```

The finite orbit counts show that even maximal label neutrality leaves multiple nontrivial proper relations.

Choosing equality, inequality, a particular union of equality-pattern orbits, or a smaller symmetry group remains an additional selection.

## M3 — compositional-role / type extraction

```text
FORMAL_AVAILABILITY = YES
INDEPENDENT_ORIGIN = FAIL_AT_CURRENT_SCOPE
```

Role classes and interface types can be constructed from participation/incidence profiles.

But when those profiles are extracted from `PGH-GRAM-0002`, the result inherits an arbitrary extensional formation relation already rejected as explanatory law by `PGH-FAIL-0001`.

When types are extracted from finite constituent positions in a presentation, the result is additionally presentation-conditional. A faithful alternative representation need not expose the same positions.

Therefore role/type extraction is not presently deeper than the structure from which it is extracted.

## M4 — projection-kernel coherence language

Given

\[
q:P\to I,
\]

the kernel equivalence

\[
p\sim_q p' \iff q(p)=q(p')
\]

canonically generates equations/coherence requirements relative to `q`.

But the project has already established that the physically or grammatically privileged projection is underdetermined (`PGH-FAIL-0004`).

Therefore:

```text
EQUATION_LANGUAGE_GIVEN_Q = CANONICAL
Q_ITSELF = UNPRIVILEGED_AT_CURRENT_SCOPE
META_LANGUAGE_ORIGIN = RELOCATED_NOT_SOLVED
```

## M5 — minimal/common structural core

For a pure domain under all renamings, equality structure is canonical, but the availability of equality does not uniquely select an admissibility rule.

The binary control already contains both equality and inequality as equally invariant nontrivial relations.

Taking the intersection of all invariant candidate supports collapses toward triviality; allowing all invariant supports restores multiplicity.

More generally, a common structural core can be useful as a language of permissible distinctions while remaining too weak to select which permissible distinction becomes law.

```text
COMMON_CORE_LANGUAGE = POSSIBLE
COMMON_CORE_AS_UNIQUE_LAW_SELECTOR = FAIL_AT_CURRENT_SCOPE
```

## Meta-language origin relocation

The gate exposes a recursive explanatory pattern:

\[
\text{support table}
\to
\text{support formula}
\to
\text{restricted rule language}
\to
\text{meta-language construction}.
\]

At each step, explanatory progress occurs only if the new layer is more constrained and independently motivated than the layer it replaces.

Current PGH has not yet supplied a non-result-directed principle fixing the primitive vocabulary/signature/type/projection/symmetry package from which a selective local rule language follows.

This failure is preserved as `PGH-FAIL-0017`.

## Source-gap decision

Repository search of the frozen source landscape found no dedicated coverage for:

```text
INSTITUTION_THEORY / LOGICAL_FRAMEWORKS
CATEGORICAL_LOGIC_AS_LANGUAGE_ORGANIZATION
STRUCTURAL_PROOF_THEORY / STRUCTURAL_RULE_ORIGIN
```

The current outcome B does not depend on those literatures; the free-language and symmetry controls decide the tested candidates directly.

However, this is now a concrete source gap for the next operation because those fields explicitly study the organization, translation, and structural constraints of formal languages themselves.

```text
CURRENT_GATE_SOURCE_GAP_BLOCKING = NO
NEXT_SOURCE_INTAKE_JUSTIFIED = YES
SOURCE_GAP_ID = SG3_META_LANGUAGE_AND_LOGICAL_FRAMEWORK_ORIGIN
```

## Acceptance criteria

```text
A1_UNRESTRICTED_PRIMITIVE_ADJUNCTION_UNIVERSAL_ENCODING = PASS_EXPOSED
A2_FREE_LANGUAGE_NONSELECTION = PASS
A3_RENAMING_INVARIANT_RELATION_MULTIPLICITY = PASS
A4_ROLE_TYPE_EXTRACTION_ORIGIN = PASS_NEGATIVE_AT_CURRENT_SCOPE
A5_PROJECTION_KERNEL_LANGUAGE_ORIGIN = PASS_NEGATIVE_AT_CURRENT_SCOPE
A6_MINIMAL_COMMON_CORE_SELECTIVITY = PASS_NEGATIVE_AT_CURRENT_SCOPE
A7_TARGET_RESULT_NOT_USED_TO_CHOOSE_META_LANGUAGE = PASS
A8_SOURCE_GAP_DECISION = PASS_SPECIFIC_GAP_IDENTIFIED
```

## Scientific ceiling

```text
META_LANGUAGE_CAN_BE_GENERATED_CONDITIONALLY = YES
META_LANGUAGE_CAN_BE_REPRESENTATION_DISCIPLINED_CONDITIONALLY = YES
META_LANGUAGE_UNIQUELY_SELECTED_FROM_ACCEPTED_PGH = NO
PROPER_LOCAL_SUPPORT_FROM_INDEPENDENTLY_FIXED_META_LANGUAGE = NO
SUCCESSOR_GRAMMAR = NONE
R2_SATISFIED = NO
PHYSICAL_LAW_DERIVED = NO
EMPIRICAL_PREDICTION = NONE
FCP_EFFECT = NONE
```

## Hard-stop verification

```text
NEW_SOURCE_SEARCH_PERFORMED = NO
TARGET_PHYSICS_USED_TO_CHOOSE_META_LANGUAGE = NO
FREE_OR_INITIAL_CALLED_PHYSICALLY_PRIVILEGED = NO
INVARIANCE_CALLED_UNIQUE_SELECTION = NO
ARBITRARY_F_REUSED_AS_EXPLANATORY_META_LANGUAGE = NO
SUCCESSOR_GRAMMAR_CREATED = NO
FCP_CHANGED = NO
```
