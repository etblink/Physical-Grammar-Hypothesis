# PGH-1 R2 Compositional Doctrine Origin Gate — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_R2_COMPOSITIONAL_DOCTRINE_ORIGIN_GATE
REGISTRY_ID = PGH-OP-0046
CANONICAL_BASE = 7cc9c084d04ea6a54c5af353ee2bd29f3cec722f
WORKING_TARGET = PGH-OBJ-0017
STRUCTURAL_PACKAGE_MAP = PGH-OBJ-0018
FROZEN_ACCEPTED_SOURCE_COUNT = 70
NEW_SOURCE_SEARCH = FORBIDDEN
SUCCESSOR_GRAMMAR_SELECTION = FORBIDDEN
PHYSICAL_BRIDGE = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Test whether any current non-result-directed formal criterion selects the compositional doctrine `D` from which a structural package `Theta_D` is generated.

The gate does **not** assume that every primitive doctrine must itself be derived from a deeper doctrine. Failure of selection means underdetermination at current scope, not an infinite-regress theorem and not automatic refutation of PGH.

## Locked tests

### T1 — model plurality under bare composition

Test whether bare monoidal axioms entail symmetry, cartesianness, cocartesianness, or another selective doctrine.

Use explicit model controls:

- free nonsymmetric monoidal structure;
- free symmetric monoidal structure without copy/discard;
- cartesian categories with finite products.

If all satisfy weaker compositional structure while differing on stronger permissions, the weaker axioms do not select the stronger doctrine.

### T2 — duality-invariant selection obstruction

Finite products in a category `C` correspond to finite coproducts in `C^op`.

Test any proposed criterion `S` that is invariant under categorical opposition in the sense

\[
S(C)=S(C^{op}).
\]

Such a criterion cannot privilege a cartesian doctrine over the cocartesian dual purely by form while treating opposite presentations as equally admissible.

### T3 — common-core / minimality selector

Test whether selecting only structure common to competing doctrines yields enough `Theta` to retain the qualified structural-package generation result.

The control must distinguish:

```text
MINIMAL_COMMON_STRUCTURE
```

from

```text
SELECTIVE_STRUCTURE_REQUIRED_FOR_COPY_DISCARD_OR_OTHER_PERMISSIONS.
```

### T4 — maximality / closure selector

Test whether choosing a doctrine because it contains the most structural permissions provides a principled endpoint.

Unrestricted adjunction of generators, equations, universal constructions, or additional structure is a universal-encoding control against naive maximality.

### T5 — universal-property selector

Test the inference:

> doctrine `D` is defined by universal properties, therefore `D` is uniquely privileged.

Multiple inequivalent or dual universal-property doctrines count as a negative control.

### T6 — representation-invariance selector

Test whether equivalence-invariance, naturality, or coordinate independence selects a unique doctrine, rather than merely making each candidate doctrine presentation-independent.

### T7 — law-free anchor control

The law-free empirical reference anchor may supply reference labels and contact but no response law or structural permission package. It may not be used to choose `D` by fitting known physics.

## No-regress safeguard

The gate must not apply this invalid inference:

```text
D_IS_NOT_DERIVED_FROM_DEEPER_STRUCTURE
THEREFORE_D_IS_NOT_A_LEGITIMATE_PRIMITIVE_GRAMMAR
```

Whether a compact primitive doctrine can legitimately serve as the hypothesized grammar is a separate stopping-rule adjudication if current selection fails.

## Outcome space

```text
A = AN_ALREADY_ACCEPTED_NON_RESULT_DIRECTED_CRITERION_SELECTS_A_NONTRIVIAL_COMPOSITIONAL_DOCTRINE_OR_EQUIVALENCE_CLASS_WORTH_SUCCESSOR_GRAMMAR_TESTING
B = TESTED_INTRINSIC_CRITERIA_DO_NOT_SELECT_A_UNIQUE_OR_PRIVILEGED_NONTRIVIAL_DOCTRINE__DUALITY_MODEL_PLURALITY_OR_COMMON_CORE_CONTROLS_PRESERVE_UNDERDETERMINATION
C = A_MINIMAL_OR_COMMON_DOCTRINE_IS_SELECTED_BUT_IS_TOO_WEAK_TO_GENERATE_THE_REQUIRED_STRUCTURAL_PACKAGE
D = CURRENT_FORMAL_AND_SOURCE_BASELINE_IS_INSUFFICIENT_FOR_DOCTRINE_ORIGIN_ADJUDICATION
```

Outcomes B/C do not refute the possibility that one doctrine is posited as a primitive candidate grammar under a separately justified stopping rule.

## Required outputs

Commit 2 may add only:

```text
audits/PGH1_R2_COMPOSITIONAL_DOCTRINE_ORIGIN_GATE_0_1_0.md
research/formalizations/PGH1_COMPOSITIONAL_DOCTRINE_SELECTION_MAP_0_1_0.md
research/derivations/PGH_DERIVATION_COMPOSITIONAL_DOCTRINE_MODEL_PLURALITY_0_1_0.md
research/derivations/PGH_DERIVATION_DUALITY_INVARIANT_DOCTRINE_SELECTION_OBSTRUCTION_0_1_0.md
research/failures/PGH_FAIL_COMPOSITIONAL_DOCTRINE_SELECTOR_UNDERDETERMINATION_0_1_0.md
handoffs/PGH1_R2_COMPOSITIONAL_DOCTRINE_ORIGIN_GATE_HANDOFF_0_1_0.md
```

## Commit topology

```text
COMMIT_1_MESSAGE = Preregister PGH-1 R2 compositional doctrine origin gate
COMMIT_2_MESSAGE = Adjudicate PGH-1 R2 compositional doctrine origin gate
EXACT_COMMITS = 2
```

## Hard stops

```text
DO_NOT_SEARCH_NEW_SOURCES
DO_NOT_SELECT_A_DOCTRINE_BY_KNOWN_PHYSICAL_FIT
DO_NOT_TREAT_DUALITY_AS_PHYSICAL_EQUIVALENCE
DO_NOT_PROVE_INFINITE_REGRESS_BY_DEFINITION
DO_NOT_CREATE_SUCCESSOR_GRAMMAR
DO_NOT_BEGIN_PHYSICAL_BRIDGE
DO_NOT_CHANGE_FCP
```
