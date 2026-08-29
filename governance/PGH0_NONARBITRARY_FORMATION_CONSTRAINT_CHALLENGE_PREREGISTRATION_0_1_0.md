# PGH-0 Non-Arbitrary Formation Constraint Challenge — Preregistration 0.1.0

## Status

```text
OPERATION_ID = PGH0_NONARBITRARY_FORMATION_CONSTRAINT_CHALLENGE
REGISTRY_ID = PGH-OP-0005
OPERATION_CLASS = FOUNDATIONAL_FORMALIZATION
STATUS = PREREGISTERED_IN_PROGRESS
CANONICAL_BASE = 0b1b563c8ce9b40f42c55f74132440535856845e
SCIENTIFIC_INPUT_BASELINE = PGH-GRAM-0002
WORKING_BRANCH = research/pgh0-nonarbitrary-formation-constraint
SOURCE_BOUND_STATUS = NOT_YET_SOURCE_BOUND
NEW_SOURCE_SEARCH = FORBIDDEN
PHYSICAL_BRIDGE = NOT_AUTHORIZED
FCP_EFFECT = NONE
```

## Purpose

The previous PGH-0 operation established that a bare formation relation can encode an arbitrary admissibility table. This operation asks whether any weak structural constraint can produce a genuine exclusion without simply entering the exclusion by hand.

The target question is:

> What is the weakest non-arbitrary structural constraint on formation that yields an exclusion not merely entered as an admissibility table?

A second target is to distinguish **formal exclusion** from **non-arbitrary necessity**. A compact axiom may exclude structures while still being an unearned stipulation.

## Canonical starting point

The active baseline remains the extensional formation baseline:

\[
G=(A,F),\qquad F\subseteq A^3,
\]

with contextual identity/distinction derived from formation profiles.

The operation must preserve:

```text
PGH-GRAM-0002 = PROVISIONAL_FORMAL_BASELINE_NONPHYSICAL
PGH-DER-0001 = QUALIFIED
PGH-FAIL-0001 = FAILED_PRESERVED
```

No successor grammar is assumed.

## Meaning of “non-arbitrary” at this scope

A candidate constraint `C` may count as **non-arbitrary at current PGH scope** only if all of the following hold:

1. `C` is stated at rule/structural level rather than by enumerating desired allowed or forbidden tuples.
2. `C` is invariant under bijective relabeling of the formal carrier.
3. `C` admits at least one baseline formation structure and excludes at least one, unless a negative result is being established.
4. the motivation for `C` can be traced to an already adopted PGH methodological commitment—such as representation independence, extensionality, generativity, or generative compression—rather than to a desired physical result;
5. the physical conclusion is not present in equivalent form among the assumptions;
6. any additional equivalence of representations, parses, decompositions, or encodings is declared explicitly rather than treated as free;
7. a finite countermodel or witness is supplied whenever feasible.

Passing these conditions would establish only a **formal non-arbitrariness result**, not a law of nature.

## Distinction between covariance and homogeneity

The experiment must not conflate:

```text
RELABELING_COVARIANCE = the scientific content is unchanged under isomorphic renaming
```

with:

```text
STRONG_PERMUTATION_INVARIANCE = every permutation of the carrier is an automorphism of one fixed formation relation
```

The first is a representation-independence requirement. The second is a substantive homogeneity condition and must earn independent justification.

## Ordered candidate-constraint tests

The following order is frozen before adjudication.

### C1 — Isomorphism covariance / label neutrality

Test the requirement that admissibility of a candidate formation structure depends only on its isomorphism class.

Questions:

- Does isomorphism covariance itself exclude any formation structure?
- Can an arbitrary selection of isomorphism classes satisfy it?
- Does it produce generative compression or merely remove label dependence?

### C2 — Strong permutation invariance

Test the stronger condition

\[
F(a,b,c)\iff F(\pi a,\pi b,\pi c)
\]

for every permutation `pi` of `A`.

Questions:

- Does this exclude baseline relations?
- Is the exclusion a consequence of label neutrality, or does the condition add substantive homogeneity?
- What relational distinctions are erased?

A nontrivial exclusion is not enough for qualification if the premise is unearned.

### C3 — Extensional irredundancy

Re-test the extensional quotient as a candidate structural constraint rather than merely a canonicalization procedure.

Question:

> Does requiring no duplicate contextual profiles constrain formation behavior itself, or only redundant naming?

### C4 — Decomposition / parse coherence

Consider a restricted representation in which formation is encoded as a total deterministic binary operation

\[
\star:A\times A\to A.
\]

Conditionally assume that two binary parse trees differing only by parenthesization represent the same grammar-internal composite.

Test whether this forces

\[
(a\star b)\star c=a\star(b\star c).
\]

Required audit:

- distinguish the theorem from the premise that parenthesization is representational;
- give explicit associative and nonassociative finite witnesses;
- determine whether the coherence premise is already justified by current PGH commitments;
- do not promote associativity to physical law.

### C5 — Arity / encoding neutrality

Test whether an `n`-ary formation represented through binary auxiliary labels can be made invariant under choices of bracketing and auxiliary encoding without presupposing a privileged equivalence map.

Questions:

- Is there a unique representation-independent constraint?
- Does the requirement merely move arbitrariness into the translation/equivalence relation?

### C6 — Generative-compression / simplicity selection

Test whether the existing PGH commitment to generative compression can, at current scope, select a nontrivial family of `F` without a separately privileged complexity measure or encoding language.

Questions:

- Is description length representation-independent here?
- Can equally simple but inequivalent formation structures remain?
- Does simplicity alone produce a definite exclusion class?

### C7 — Extremal controls

Use two controls rather than preferred candidates:

```text
MAXIMAL_PERMISSIVENESS -> choose the largest admissible F
MINIMAL_PERMISSIVENESS -> choose the smallest admissible F
```

Test whether these collapse respectively to universal or empty formation when no additional structure is supplied.

These controls check whether “choose an extremum” disguises arbitrariness rather than resolving it.

## Required nontriviality audit

Apply N0–N9 from `NONTRIVIALITY_TESTS.md` to each candidate where meaningful, with special attention to:

```text
N1_UNIVERSAL_ENCODING
N2_NO_SMUGGLING
N3_NONUNIVERSAL_EXCLUSION
N4_REPRESENTATION_INVARIANCE
N5_SEMANTIC_LOAD
N6_GENERATIVE_COMPRESSION
N7_INDEPENDENT_CONSEQUENCE
N8_COUNTEREXAMPLE_EXPOSURE
N9_RELABELING_INVARIANCE
```

N10 remains out of scope.

## Conditional theorem rule

A theorem of the form

```text
IF extra structural premise P, THEN exclusion E
```

may be qualified as a **conditional formal derivation** even if `P` itself is not yet justified.

Such a theorem does not satisfy the operation’s central burden unless `P` is independently shown to arise from already adopted PGH commitments.

## Finite-model requirements

Where feasible, perform exhaustive finite checks at the smallest nontrivial carrier size.

At minimum:

- enumerate all total binary operations on a two-element carrier for the parse-coherence/associativity test;
- provide an explicit nonassociative table;
- count operations surviving the coherence condition;
- provide explicit formation relations showing that relabeling covariance and strong permutation invariance are different requirements.

Computational enumeration is validation, not proof by itself; exact reasoning must accompany it.

## Outcome space

The operation may conclude:

```text
A = REPRESENTATION_NEUTRALITY_ALONE_YIELDS_A_QUALIFIED_NONARBITRARY_CONSTRAINT
B = DECOMPOSITION_COHERENCE_YIELDS_A_QUALIFIED_NONARBITRARY_CONSTRAINT
C = ANOTHER_TESTED_CONSTRAINT_QUALIFIES
D = NONTRIVIAL_FORMAL_CONSTRAINTS_EXIST_BUT_ALL_REQUIRE_AN_UNEARNED_EXTRA_PREMISE
E = NO_TESTED_CONSTRAINT_EVEN_PRODUCES_NONTRIVIAL_FORMAL_EXCLUSION
F = CURRENT_BASELINE_REQUIRES_REPAIR
G = UNRESOLVED
```

The labels are descriptive, not rankings.

## Required outputs

Create at minimum:

```text
research/formalizations/PGH0_NONARBITRARY_FORMATION_CONSTRAINT_ADJUDICATION_0_1_0.md
handoffs/PGH0_NONARBITRARY_FORMATION_CONSTRAINT_CHALLENGE_HANDOFF_0_1_0.md
```

Create versioned derivation artifacts for any qualified conditional or unconditional theorem.

Create versioned failure artifacts for materially attractive candidate principles that fail the declared burden.

Do not update canonical registries or mutable `CURRENT_STATE.md` on the scientific branch merely to pre-integrate the result; post-integration reconciliation remains a separate maintenance step.

## Hard stop rules

This operation must stop before:

- claiming a physical law;
- claiming a physical grammar has been found;
- starting source intake;
- importing empirical data;
- identifying associativity, symmetry, locality, causality, time, probability, geometry, conservation, or gauge structure with physics;
- beginning the next scientific operation;
- mutating canonical `main` before review.

## Review boundary

The scientific candidate should consist of exactly two commits:

```text
COMMIT_1_MESSAGE = Preregister PGH-0 non-arbitrary formation constraint challenge
COMMIT_2_MESSAGE = Adjudicate PGH-0 non-arbitrary formation constraint challenge
```

Commit 1 must contain only this preregistration artifact.

Commit 2 may add only the adjudication, derivation/failure artifacts required by the result, and the handoff.

Canonical `main` remains unchanged until independent review accepts the candidate.
