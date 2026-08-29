# PGH-1 R2 Compositional Doctrine Origin Gate 0.1.0

## Identity

```text
OPERATION_ID = PGH1_R2_COMPOSITIONAL_DOCTRINE_ORIGIN_GATE
REGISTRY_ID = PGH-OP-0046
CANONICAL_BASE = 7cc9c084d04ea6a54c5af353ee2bd29f3cec722f
PREREGISTRATION_COMMIT = 1a60a42fc8e5ed2c8f25d8da126d54c321b1ba14
WORKING_TARGET = PGH-OBJ-0017
FROZEN_ACCEPTED_SOURCE_COUNT = 70
NEW_SOURCE_SEARCH = NONE
FCP_EFFECT = NONE
```

## Outcome

```text
OUTCOME = B__TESTED_INTRINSIC_CRITERIA_DO_NOT_SELECT_A_UNIQUE_OR_PRIVILEGED_NONTRIVIAL_COMPOSITIONAL_DOCTRINE__DUALITY_MODEL_PLURALITY_AND_COMMON_CORE_CONTROLS_PRESERVE_UNDERDETERMINATION
SUCCESSOR_GRAMMAR = NONE
R2A = UNSATISFIED
R2B = UNSATISFIED
INFINITE_REGRESS_PROVED = NO
PHYSICAL_LAW_DERIVED = NO
```

## Executive result

The previous gate established that a fixed compositional doctrine can generate a nontrivial structural package `Theta_D` by universal properties.

This gate tests whether accepted PGH structure already selects the doctrine `D`.

No tested criterion does so.

The result is **underdetermination**, not refutation and not an infinite-regress theorem.

## T1 — compositional doctrine model plurality

Bare monoidal structure has models with materially different stronger structure.

### Nonsymmetric control

The free strict monoidal category on two object-generators and no nonidentity morphism generators is monoidal but has no exchange map between distinct tensor words.

### Symmetric noncartesian control

The free symmetric monoidal category on the same generators has exchange/coherence maps but no arity-changing morphisms such as

\[
A\to A\otimes A
\]

or

\[
A\to I.
\]

Thus symmetry does not imply cartesianness.

### Cartesian control

A category with finite products has canonical diagonal and terminal maps.

Therefore weaker monoidal axioms admit realizations that disagree on symmetry, copy-like structure, and discard-like structure.

Consequently those stronger doctrines are not theorems of bare monoidal composition.

This result is frozen as `PGH-DER-0019`.

## T2 — duality-invariant doctrine-selection obstruction

Categorical opposition exchanges finite-product and finite-coproduct structure:

\[
\text{Products in }C
\quad\leftrightarrow\quad
\text{Coproducts in }C^{op}.
\]

Suppose a selector `S` is opposition-invariant:

\[
S(C)=S(C^{op}).
\]

Then `S` cannot, by opposition-invariant form alone, declare the product doctrine uniquely privileged while rejecting its coproduct dual. It must either:

- treat the dual doctrines together;
- select a self-dual or richer structure;
- or introduce additional orientation-sensitive data.

Thus representation discipline under opposition is compatible with doctrine plurality.

This result is frozen as `PGH-DER-0020`.

The theorem is formal only. It does not assert that categorical opposition is physical equivalence.

## T3 — common-core / minimality selector

A symmetric-monoidal-style common core can be retained while product- and coproduct-specific universal maps are removed.

The free symmetric monoidal control shows that such a core does not force diagonal or terminal maps.

Therefore common-core minimization sacrifices the very selectivity obtained in the structural-package generation gate.

```text
COMMON_CORE = REPRESENTATION_DISCIPLINED_BUT_TOO_WEAK
```

A complexity or simplicity metric that selects one stronger doctrine would itself require justification and is not fixed by current PGH.

## T4 — maximality / closure selector

No preregistered non-result-directed ordering makes one doctrine the unique maximal endpoint.

Product and coproduct structure may coexist; further closure, generators, equations, adjoints, traces, duals, or other structure may be added.

If `maximal` merely means adjoining every desired structural permission, selectivity disappears and the universal-encoding problem returns.

```text
NAIVE_MAXIMALITY = NOT_A_SELECTOR
```

This does not prove that no useful maximality principle can ever be defined.

## T5 — universal-property selector

Universal properties explain why maps are canonical **within** a chosen doctrine.

They do not uniquely select one doctrine because multiple non-equivalent or dual doctrines are themselves specified by universal properties.

```text
UNIVERSAL_PROPERTY = CONDITIONAL_CANONICALITY
UNIVERSAL_PROPERTY =/= UNIQUE_DOCTRINE_SELECTION
```

## T6 — representation invariance

Cartesian, cocartesian, symmetric, and other categorical properties can each be formulated invariantly under appropriate equivalence.

Thus representation robustness filters bad presentations but does not collapse the doctrine family to one member.

This recapitulates the project's broader distinction:

\[
\text{invariance}\neq\text{privilege}.
\]

## T7 — law-free anchor

The law-free empirical anchor contains no response-law or structural-package information with which to select a doctrine.

Using observed physical behavior to choose the doctrine would be legitimate later model testing, but it would not count as grammar-internal derivation of `D`.

## Failure preserved

```text
PGH-FAIL-0020 = COMPOSITIONAL_DOCTRINE_SELECTOR_UNDERDETERMINATION
```

No tested formal criterion simultaneously provides:

```text
NON_RESULT_DIRECTEDNESS
REPRESENTATION_DISCIPLINE
NONTRIVIAL_SELECTIVITY
UNIQUE_OR_INDEPENDENTLY_PRIVILEGED_DOCTRINE
```

## No-regress safeguard

The failure does **not** establish:

```text
EVERY_GRAMMAR_MUST_HAVE_A_META_GRAMMAR
PRIMITIVE_DOCTRINES_ARE_ILLEGITIMATE
INFINITE_EXPLANATORY_REGRESS_IS_UNAVOIDABLE
PGH_IS_REFUTED
```

A scientific hypothesis is allowed to contain primitive postulates. The unresolved issue is instead whether a primitive structural doctrine can satisfy PGH's own no-smuggling, compression, representation-independence, exclusion, and falsifiability requirements without merely restating known laws.

That is a separate hypothesis-boundary question.

## Scientific consequence

The sequence has reached a methodological boundary:

\[
D\to\Theta_D\to L(\Theta_D)\to P
\]

is a real generative architecture, but current PGH does not derive `D`.

The next scientifically responsible operation is therefore not another automatic meta-layer. It is an explicit adjudication of the **primitive-grammar stopping rule**.

Recommended:

```text
PGH1_R2A_PRIMITIVE_GRAMMAR_STOPPING_RULE_ADJUDICATION
```

It should decide when a compact doctrine may legitimately be posited as the grammar itself and what burden remains before such a doctrine earns physical-law credit.

## Source decision

```text
NEW_SOURCE_GAP_BLOCKING = NO
NEW_SOURCE_SEARCH_JUSTIFIED_IMMEDIATELY = NO
```

## Hard-stop verification

```text
CARTESIAN_SELECTED = NO
COCARTESIAN_SELECTED = NO
SYMMETRIC_SELECTED = NO
OPPOSITION_CALLED_PHYSICAL_EQUIVALENCE = NO
INFINITE_REGRESS_CLAIMED = NO
SUCCESSOR_GRAMMAR_CREATED = NO
R2A_DECLARED_SATISFIED = NO
R2B_DECLARED_SATISFIED = NO
PHYSICAL_LAW_DERIVED = NO
FCP_CHANGED = NO
```
