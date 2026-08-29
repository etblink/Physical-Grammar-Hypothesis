# PGH-0 Empirical Substructure Privilege Gate — Preregistration 0.1.0

## Status

```text
OPERATION_ID = PGH0_EMPIRICAL_SUBSTRUCTURE_PRIVILEGE_GATE
REGISTRY_ID = PGH-OP-0026
OPERATION_CLASS = SOURCE_BOUND_FOUNDATIONAL_FEASIBILITY_GATE
STATUS = PREREGISTERED_IN_PROGRESS
CANONICAL_BASE = 142e022d063bd38e685fb359d365bf6ca334f3ce
WORKING_BRANCH = research/pgh0-empirical-substructure-privilege
FROZEN_SOURCE_COUNT = 37
NEW_SOURCE_SEARCH = FORBIDDEN_UNLESS_A_SPECIFIC_BLOCKING_GAP_IS_DEMONSTRATED
R2_LAW_EXHAUSTION = FORBIDDEN
PHYSICAL_GRAMMAR_SELECTION = FORBIDDEN
EMPIRICAL_PREDICTION = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

The seed/generator gate established that different empirical seeds may generate the same closed interface and are interchangeable for closure-factoring structure. Seed uniqueness and minimality therefore cannot generally carry physical privilege.

This gate asks whether privilege can instead attach to the **generated closed empirical substructure itself** through an intrinsic, response-independent property of the grammar/closure structure.

The gate must not use desired records, empirical success, target physical predictions, or an externally supplied `T_phys` to select a substructure.

## Fixed scope

Hold fixed:

```text
P = ambient formal context universe
Cl = response-independent grammar-generated closure operator
L = Fix(Cl) = lattice/poset of closed substructures
Aut = automorphisms preserving the fixed grammar/closure structure
```

The gate may compare members of `L` using only intrinsic formal properties available before any response law or empirical-success test.

## Locked selector families

Test separately and in this order.

### S1 — Smallest nontrivial closed substructure

Candidate rule:

```text
select a nonempty proper closed substructure minimal by inclusion or cardinality
```

Test existence, uniqueness, and symmetry dependence.

### S2 — Largest reachable/generated closed substructure

Candidate rule:

```text
select the maximal generated closed substructure, potentially P itself
```

Test whether this is unique but vacuous/overinclusive and whether it provides any physical irrelevance criterion rather than declaring every formal context empirical.

### S3 — Automorphism-invariant closed substructure

Candidate rule:

```text
select T in L fixed setwise by every grammar automorphism
```

Test uniqueness and whether only trivial extremes survive.

### S4 — Fixed-point/canonical-operator selection

First test `Cl(T)=T`. Because every member of `L` already satisfies this, determine whether closure-fixed-point status selects anything.

Then test the stronger proposal of an additional intrinsic endomap

\[
F:L\to L
\]

with a distinguished fixed point. Apply a universal-encoding control: if `F` is freely chosen, can any target closed `T` be made the unique fixed point by defining `F(S)=T`?

### S5 — Intersection selector

Candidate rules include:

```text
intersection of all nonempty generated closed substructures
intersection of all proper nontrivial generated closed substructures
```

Test whether the intersection is closed, whether it is nontrivial, and whether it tends to collapse to the empty/trivial core.

### S6 — Union/join selector

Candidate rules include the union or closure of the union of all law-free generated closed substructures.

Test whether this expands to `P` or another maximal object and thereby loses empirical discrimination.

### S7 — Intrinsic-description or simplicity tie-break

Any proposal to select the structurally simplest closed substructure must pass the prior PGH simplicity control: no unprivileged description language or complexity measure may be introduced.

### S8 — Empirical-success selector

Rules such as

```text
select T because its probes reproduce observed records
select T because it maximizes discrimination matching known physics
select T because its response profile agrees with experiment
```

must be classified as result-directed physical selection, not a grammar-intrinsic privilege criterion.

## Symmetry-obstruction theorem target

Let a selector predicate `C(T)` on closed substructures be invariant under grammar automorphisms:

\[
C(T)\Longleftrightarrow C(\alpha[T])
\]

for every `alpha in Aut`.

Test:

> If exactly one closed substructure `T*` satisfies `C`, must `T*` be fixed setwise by every automorphism?

If yes, a grammar whose automorphism group exchanges candidate proper empirical substructures but fixes only trivial extremes provides an obstruction to any unique intrinsic invariant selector choosing one of them.

## Required finite symmetric witness

Use:

```text
P = {a,b,c,d}
```

with one unary grammar constructor `s`:

```text
s(a)=b
s(b)=a
s(c)=d
s(d)=c
```

Closed substructures under `s` are exactly:

```text
empty
{a,b}
{c,d}
P
```

The grammar admits an automorphism exchanging the two pairs:

```text
a<->c
b<->d
```

Test all locked selector families on this witness.

Expected controls to test, not assume:

- two smallest nontrivial closed substructures;
- unique largest `P`;
- only `empty` and `P` fixed by every automorphism;
- intersection of the two proper nontrivial blocks is empty;
- join/union is `P`;
- all four closed sets are fixed points of `Cl`.

## Required asymmetric witness

Also test a grammar where an intrinsic selector *can* be unique, to avoid overclaiming impossibility.

Use:

```text
P={a,b}
f(a)=b
f(b)=b
```

Closed sets are:

```text
empty
{b}
{a,b}
```

The unique smallest nonempty closed substructure is `{b}`.

This control distinguishes:

```text
NO_GENERAL_INTRINSIC_SELECTOR
```

from the stronger and unjustified claim:

```text
NO_GRAMMAR_CAN_EVER_HAVE_A_UNIQUE_INTRINSIC_CLOSED_SUBSTRUCTURE
```

## Acceptance criteria

The gate qualifies only if:

```text
B1_SYMMETRY_OBSTRUCTION_IS_PROVED
B2_SMALLEST_SELECTOR_NONUNIQUENESS_IS_TESTED
B3_LARGEST_SELECTOR_TRIVIALITY_OR_SCOPE_IS_EXPOSED
B4_AUTOMORPHISM_INVARIANCE_IS_TESTED
B5_FIXED_POINT_UNDERDETERMINATION_IS_TESTED
B6_INTERSECTION_AND_UNION_CONTROLS_ARE_TESTED
B7_FREE_CANONICAL_OPERATOR_UNIVERSAL_ENCODING_IS_EXPOSED
B8_ASYMMETRIC_UNIQUE_SELECTOR_CONTROL_IS_INCLUDED
B9_EMPIRICAL_SUCCESS_IS_NOT_USED_AS_INTRINSIC_PRIVILEGE
B10_NO_GENERAL_IMPOSSIBILITY_CLAIM_IS_OVERSTATED
```

## Outcome space

```text
A = A_FROZEN_INTRINSIC_SELECTOR_UNIQUELY_AND_NONTRIVIALLY_SELECTS_EMPIRICAL_SUBSTRUCTURE_GENERALLY
B = INTRINSIC_SELECTORS_CAN_SELECT_IN_SPECIAL_GRAMMARS_BUT_NO_TESTED_GENERAL_CRITERION_AVOIDS_NONUNIQUENESS_TRIVIAL_EXTREMES_OR_EXTRA_SELECTOR_INPUT
C = ALL_NONTRIVIAL_SUBSTRUCTURE_SELECTION_REQUIRES_RESPONSE_LAW_OR_EMPIRICAL_SUCCESS_IMPORT
D = FROZEN_CORPUS_IS_INSUFFICIENT_AND_A_SPECIFIC_BLOCKING_GAP_IS_IDENTIFIED
E = UNRESOLVED
```

No outcome is a ranking.

## Required outputs

Commit 2 may add only:

```text
audits/PGH0_EMPIRICAL_SUBSTRUCTURE_PRIVILEGE_GATE_0_1_0.md
research/derivations/PGH_DERIVATION_INTRINSIC_SUBSTRUCTURE_SELECTOR_SYMMETRY_OBSTRUCTION_0_1_0.md
research/failures/PGH_FAIL_GENERIC_EMPIRICAL_SUBSTRUCTURE_PRIVILEGE_SELECTORS_0_1_0.md
handoffs/PGH0_EMPIRICAL_SUBSTRUCTURE_PRIVILEGE_GATE_HANDOFF_0_1_0.md
```

Do not mutate current-state/navigation files on the scientific branch.

## Commit boundary

```text
COMMIT_1_MESSAGE = Preregister PGH-0 empirical substructure privilege gate
COMMIT_2_MESSAGE = Adjudicate PGH-0 empirical substructure privilege gate
```

Exactly two commits are permitted.

## Hard stops

Stop before:

- claiming no physical empirical interface can ever be privileged;
- selecting a substructure because it matches known observations;
- changing `PGH-GRAM-0002`;
- beginning R2;
- empirical prediction;
- unbounded source expansion;
- changing FCP;
- mutating canonical `main` before independent review.
