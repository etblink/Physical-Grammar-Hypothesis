# PGH-0 Empirical Generator Invariance and Seed Minimality Gate — Preregistration 0.1.0

## Status

```text
OPERATION_ID = PGH0_EMPIRICAL_GENERATOR_INVARIANCE_AND_SEED_MINIMALITY_GATE
REGISTRY_ID = PGH-OP-0024
OPERATION_CLASS = SOURCE_BOUND_FOUNDATIONAL_FEASIBILITY_GATE
STATUS = PREREGISTERED_IN_PROGRESS
CANONICAL_BASE = 89e54b1d3173a16730134fa1b188675aeb034b62
WORKING_BRANCH = research/pgh0-empirical-generator-invariance-seed-minimality
FROZEN_SOURCE_COUNT = 37
NEW_SOURCE_SEARCH = FORBIDDEN_UNLESS_A_SPECIFIC_BLOCKING_GAP_IS_DEMONSTRATED
R2_LAW_EXHAUSTION = FORBIDDEN
PHYSICAL_GRAMMAR_SELECTION = FORBIDDEN
EMPIRICAL_PREDICTION = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

The previous challenge established a formal grammar-generated empirical interface

\[
C_G^*(C_0)=Cl_{E(G)}(C_0)
\]

from a law-free empirical seed `C0`.

That result removes a separately listed interface oracle but leaves the seed itself apparently privileged.

This gate asks whether seed identity can be demoted to **generator presentation** when different seeds generate the same closure, and whether any general uniqueness/minimality principle can recover one canonical empirical seed without smuggling the target interface into the selection criterion.

## Fixed closure scope

Hold fixed for the gate:

```text
P = formal context universe
Cl = response-independent grammar-generated closure operator
```

`Cl` is treated as already fixed by the prior operation. The gate may not change the grammar, constructor extraction rule, response evaluator, or record map in order to obtain a desired seed result.

## Definitions

For seeds `A,B subseteq P`, define **generator equivalence**:

\[
A\sim_{Cl}B
\quad\Longleftrightarrow\quad
Cl(A)=Cl(B).
\]

A seed `A` generating `T=Cl(A)` is:

- **inclusion-irredundant** if no proper subset of `A` generates `T`;
- **minimum-cardinality** if no generating seed for `T` has smaller cardinality.

These notions must be kept distinct.

## Locked tests

### G1 — Generator-equivalence theorem

Test whether `~_Cl` is an equivalence relation and whether interface-generation results that depend only on `Cl(A)` are invariant under replacement of seed `A` by an equivalent seed `B`.

### G2 — Factorization boundary

For any seed-level quantity `Q`, test the distinction between:

\[
Q(A)=\bar Q(Cl(A))
\]

and a quantity that depends on the literal seed presentation.

If `Q` factors through closure, equal-closure seeds must agree. If it does not, equal-closure seeds may remain distinguishable.

No physical factorization may be assumed merely because it is mathematically convenient.

### G3 — Finite symmetry-related nonuniqueness

Construct a finite grammar closure with two different minimum seeds generating the same interface and related by an automorphism.

This is a basic control showing that minimum generators need not be literally unique.

### G4 — Finite non-automorphism-related nonuniqueness

Use the fixed two-element constructor system:

```text
P = {a,b}
f(a)=b
f(b)=b
g(a)=a
g(b)=a
```

Test:

```text
Cl({a}) = {a,b}
Cl({b}) = {a,b}
```

and determine whether any automorphism of the labeled constructor structure maps `a` to `b`.

This tests whether equal-closure minimum generators can be structurally inequivalent even before physical semantics is added.

### G5 — Infinite no-irredundant-generator control

Use:

```text
P = N
p(0)=0
p(n+1)=n
```

with closure under repeated application of `p`.

Test whether every unbounded subset of `N` generates all of `N`, and whether removing any one element from an unbounded subset leaves it unbounded and therefore still generating.

If so, the full generated interface has no inclusion-irredundant generating seed in this finitary unary system.

### G6 — Minimum-cardinality nonselection

Even when a minimum cardinality exists, test whether it selects a unique generator.

The finite G4 system is a required control: if both `{a}` and `{b}` are one-element generators, minimum size alone cannot select between them.

### G7 — Target-presupposition control

Reject criteria of the form:

```text
choose a smallest seed A such that Cl(A) = T_phys
```

as a physical-selection principle if `T_phys` is externally specified as the desired physical interface. Such a criterion presupposes the target it is meant to explain.

## Acceptance criteria

The seed/generator result may qualify only if:

```text
B1_EQUAL_CLOSURE_SEED_EQUIVALENCE_IS_PROVED
B2_CLOSURE_FACTORIZATION_BOUNDARY_IS_EXPLICIT
B3_NONUNIQUE_MINIMUM_GENERATORS_ARE_EXHIBITED
B4_NONAUTOMORPHIC_EQUAL_CLOSURE_GENERATORS_ARE_TESTED
B5_NO_IRREDUNDANT_GENERATOR_CONTROL_IS_TESTED
B6_MINIMUM_SIZE_IS_NOT_PROMOTED_TO_PHYSICAL_PRIVILEGE
B7_TARGET_INTERFACE_IS_NOT_PRESUPPOSED
B8_FULL_PHYSICAL_EQUIVALENCE_IS_NOT_INFERRED_FROM_EQUAL_CLOSURE
```

## Outcome space

```text
A = SEED_IDENTITY_REMAINS_ESSENTIAL_EVEN_AT_INTERFACE_GENERATION_SCOPE
B = EQUAL_CLOSURE_SEEDS_ARE_EQUIVALENT_ONLY_FOR_CLOSURE_FACTORING_STRUCTURE_AND_MINIMAL_GENERATORS_ARE_NOT_GENERALLY_UNIQUE_OR_GUARANTEED
C = FROZEN_CRITERIA_SELECT_A_UNIQUE_CANONICAL_EMPIRICAL_SEED
D = SOURCE_CORPUS_IS_INSUFFICIENT_AND_A_SPECIFIC_BLOCKING_GAP_IS_IDENTIFIED
E = UNRESOLVED
```

No outcome is a ranking.

## Required outputs

Commit 2 may add only:

```text
audits/PGH0_EMPIRICAL_GENERATOR_INVARIANCE_AND_SEED_MINIMALITY_GATE_0_1_0.md
research/derivations/PGH_DERIVATION_EMPIRICAL_GENERATOR_CLOSURE_EQUIVALENCE_0_1_0.md
research/failures/PGH_FAIL_UNIQUE_OR_MINIMAL_EMPIRICAL_SEED_0_1_0.md
handoffs/PGH0_EMPIRICAL_GENERATOR_INVARIANCE_AND_SEED_MINIMALITY_GATE_HANDOFF_0_1_0.md
```

Do not mutate current-state/navigation files on the scientific branch.

## Commit boundary

```text
COMMIT_1_MESSAGE = Preregister PGH-0 empirical generator invariance and seed minimality
COMMIT_2_MESSAGE = Adjudicate PGH-0 empirical generator invariance and seed minimality
```

Exactly two commits are permitted.

## Hard stops

Stop before:

- claiming equal generated closure is full physical equivalence;
- selecting one empirical seed as fundamental by simplicity or cardinality alone;
- changing `PGH-GRAM-0002`;
- beginning R2;
- empirical prediction;
- unbounded source expansion;
- changing FCP;
- mutating canonical `main` before independent review.
