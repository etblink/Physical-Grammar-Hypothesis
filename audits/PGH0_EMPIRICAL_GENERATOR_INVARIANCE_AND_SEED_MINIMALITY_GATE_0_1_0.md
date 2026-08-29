# PGH-0 Empirical Generator Invariance and Seed Minimality Gate 0.1.0

## Identity

```text
OPERATION_ID = PGH0_EMPIRICAL_GENERATOR_INVARIANCE_AND_SEED_MINIMALITY_GATE
REGISTRY_ID = PGH-OP-0024
CANONICAL_BASE = 89e54b1d3173a16730134fa1b188675aeb034b62
PREREGISTRATION_COMMIT = 13a753de4882d17f6f353ff0a3e0d7f3fe5b7d6f
FROZEN_SOURCE_COUNT = 37
NEW_SOURCE_SEARCH = NONE
R2_LAW_EXHAUSTION = NOT_STARTED
PHYSICAL_GRAMMAR_SELECTION = NONE
EMPIRICAL_PREDICTION = NONE
FCP_EFFECT = NONE
```

## Outcome

```text
OUTCOME = B__EQUAL_CLOSURE_SEEDS_ARE_EQUIVALENT_ONLY_FOR_CLOSURE_FACTORING_STRUCTURE_AND_MINIMAL_GENERATORS_ARE_NOT_GENERALLY_UNIQUE_OR_GUARANTEED
GENERATOR_EQUIVALENCE = QUALIFIED_FORMAL
CLOSURE_FACTORIZATION_BOUNDARY = QUALIFIED_FORMAL
UNIQUE_MINIMUM_SEED = NOT_GENERAL
INCLUSION_IRREDUNDANT_SEED = NOT_GUARANTEED
FULL_PHYSICAL_EQUIVALENCE_FROM_EQUAL_CLOSURE = NO
R1_SOLVED = NO
R2_STARTED = NO
```

The gate establishes that seed identity can be demoted to presentation **only for structure that depends on the seed through its generated closure**. It also establishes strong negative controls against treating minimum size or irredundancy as a general physical-selection principle.

---

## 1. G1 — Generator equivalence

For a fixed closure operator `Cl` define

\[
A\sim_{Cl}B
\quad\Longleftrightarrow\quad
Cl(A)=Cl(B).
\]

This is an equivalence relation because equality of generated closures is reflexive, symmetric, and transitive.

Therefore seed presentations are partitioned into generator-equivalence classes indexed by generated closed substructures.

This is qualified as part of `PGH-DER-0010`.

---

## 2. G2 — Factorization boundary

Suppose a seed-level quantity or interpretation `Q` factors through closure:

\[
Q(A)=\bar Q(Cl(A)).
\]

If `A~Cl B`, then

\[
Q(A)=\bar Q(Cl(A))=\bar Q(Cl(B))=Q(B).
\]

So every closure-factoring property is invariant under replacement of one generator by an equal-closure generator.

But equal closure does not force every possible seed-level property to agree.

For example, a quantity

```text
Q_A(S)=1 iff a in S
```

can distinguish two seeds whose closures are identical.

Therefore:

```text
SEED_CHOICE_IS_PRESENTATIONAL = YES_FOR_CLOSURE_FACTORING_STRUCTURE
SEED_CHOICE_IS_PRESENTATIONAL = NOT_ESTABLISHED_FOR_ALL_PHYSICAL_SEMANTICS
```

A physical interpretation may be demoted from seed identity to generated closure only if the relevant semantics itself factors through closure. That factorization is not inferred merely from mathematics.

---

## 3. G3 — Symmetry-related nonunique minimum generators

Let

```text
P={a,b}
s(a)=b
s(b)=a
```

with closure under repeated application of `s`.

Then:

```text
Cl({a})={a,b}
Cl({b})={a,b}
Cl(empty)=empty
```

Both singleton seeds are minimum-cardinality generators of the full closure, and the swap `a<->b` is an automorphism.

Thus literal uniqueness already fails in the simplest symmetry-related case.

---

## 4. G4 — Non-automorphism-related minimum generators

Now fix the preregistered labeled constructor structure:

```text
P={a,b}
f(a)=b
f(b)=b
g(a)=a
g(b)=a
```

### Generation

From `{a}`, applying `f` yields `b`, so

\[
Cl(\{a\})=\{a,b\}.
\]

From `{b}`, applying `g` yields `a`, so

\[
Cl(\{b\})=\{a,b\}.
\]

The empty seed generates nothing, so each singleton is minimum-cardinality.

### Automorphism test

The only nonidentity bijection swaps `a` and `b`.

For an automorphism `sigma`, preservation of `f` would require

\[
\sigma(f(a))=f(\sigma(a)).
\]

Under the swap:

\[
\sigma(f(a))=\sigma(b)=a,
\]

while

\[
f(\sigma(a))=f(b)=b.
\]

These are unequal. Hence the swap is not an automorphism.

Therefore the two minimum singleton generators produce exactly the same closure but are **not related by a grammar automorphism**.

```text
EQUAL_CLOSURE = YES
MINIMUM_CARDINALITY = YES_FOR_BOTH
AUTOMORPHISM_RELATED = NO
```

This defeats the idea that minimum generation plus grammar symmetry generally selects one empirical seed class.

---

## 5. G5 — Finitary closure with no inclusion-irredundant generator

Let

```text
P=N={0,1,2,...}
p(0)=0
p(n+1)=n
```

with closure under repeated application of the unary constructor `p`.

For any seed `S`, the generated closure is its downward closure.

### Characterization of generators of `N`

If `S` is unbounded, then for every `k in N` there exists `n in S` with `n>=k`. Repeated application of `p` to `n` reaches `k`. Therefore:

\[
Cl(S)=N.
\]

Conversely, if `S` is bounded by `M`, repeated predecessor steps cannot produce any integer greater than `M`, so `Cl(S) != N`.

Thus:

\[
Cl(S)=N
\quad\Longleftrightarrow\quad
S\text{ is unbounded}.
\]

### No irredundant generating seed

Remove any single element from an unbounded subset of `N`. The remainder is still unbounded, and therefore still generates `N`.

Hence every generating seed has every individual element redundant in the inclusion sense.

There is **no inclusion-irredundant generating seed** for the full closure.

This example uses only one unary finitary constructor.

```text
FINITARY_GRAMMAR = YES
FULL_CLOSURE_GENERATORS_EXIST = YES
INCLUSION_IRREDUNDANT_GENERATOR_EXISTS = NO
```

This is a decisive failure of a general “choose an irredundant seed” principle.

---

## 6. G6 — Minimum cardinality does not select

In the finite G4 example the minimum generating cardinality is `1`, but there are two different minimum generators and no grammar automorphism relates them.

In the predecessor example every generating seed is infinite and countable, so minimum cardinality `aleph_0` is attained by many different unbounded subsets, none inclusion-irredundant.

Therefore minimum cardinality and inclusion minimality are distinct and neither yields a general unique seed.

```text
MINIMUM_SIZE_SELECTS_UNIQUE_SEED = NO
```

---

## 7. G7 — Target-presupposition control

The criterion

> choose a smallest seed `A` such that `Cl(A)=T_phys`

cannot itself explain the physically relevant interface if `T_phys` has already been supplied externally as the target physical closure.

It converts a representation problem into an optimization problem **after the desired physical object has been assumed**.

Likewise, choosing a seed because it reproduces a desired empirical distinguishability partition is result-directed.

```text
TARGET_DEFINED_SEED_OPTIMIZATION = PHYSICAL_SELECTION_NOT_EXPLAINED
```

This is preserved in `PGH-FAIL-0010`.

---

## 8. Acceptance-criteria result

```text
B1_EQUAL_CLOSURE_SEED_EQUIVALENCE_IS_PROVED = PASS
B2_CLOSURE_FACTORIZATION_BOUNDARY_IS_EXPLICIT = PASS
B3_NONUNIQUE_MINIMUM_GENERATORS_ARE_EXHIBITED = PASS
B4_NONAUTOMORPHIC_EQUAL_CLOSURE_GENERATORS_ARE_TESTED = PASS
B5_NO_IRREDUNDANT_GENERATOR_CONTROL_IS_TESTED = PASS
B6_MINIMUM_SIZE_IS_NOT_PROMOTED_TO_PHYSICAL_PRIVILEGE = PASS
B7_TARGET_INTERFACE_IS_NOT_PRESUPPOSED = PASS
B8_FULL_PHYSICAL_EQUIVALENCE_IS_NOT_INFERRED_FROM_EQUAL_CLOSURE = PASS
```

The preregistered outcome is therefore B.

---

## 9. Scientific interpretation

The result removes another unnecessary candidate primitive.

Strong PGH does not need one uniquely distinguished empirical seed **at interface-generation scope**. The more invariant object is the generated closed empirical substructure:

\[
[A]_{\sim_{Cl}}
\longleftrightarrow
Cl(A).
\]

Different seeds in the same generator-equivalence class can be treated as alternative presentations whenever downstream semantics factors through the closure.

But the gate does not establish that physical semantics must factor that way, and it does not select which generated closed substructure is physically empirical.

The residual burden therefore moves from:

> Which seed is fundamental?

more sharply to:

> Which generated empirical substructure, if any, is physically privileged, and by what non-result-directed criterion?

---

## 10. R1 consequence

```text
R1_LAW_FREE_EMPIRICAL_CONTACT = FORMALLY_ADMISSIBLE
R1_GRAMMAR_GENERATED_INTERFACE_CLOSURE = FORMALLY_FEASIBLE
R1_GENERATOR_EQUIVALENCE = QUALIFIED_AT_CLOSURE_SCOPE
R1_UNIQUE_EMPIRICAL_SEED_REQUIRED = NO_AT_CLOSURE_SCOPE
R1_SEED_MINIMALITY_SELECTION = FAILED_AS_GENERAL_PRINCIPLE
R1_PHYSICAL_SEMANTIC_FACTORIZATION = UNESTABLISHED
R1_EMPIRICAL_SUBSTRUCTURE_PRIVILEGE = UNESTABLISHED
R1_PHYSICAL_COMPLETENESS = UNESTABLISHED
R1_SOLVED = NO
```

---

## 11. Source-gap decision

No specific source deficiency blocks the formal gate.

```text
SPECIFIC_SOURCE_GAP = NONE
SOURCE_EXPANSION_JUSTIFIED = NO
```

---

## 12. Next sequencing

Recommended next operation:

```text
NEXT_RECOMMENDED_OPERATION = PGH0_EMPIRICAL_SUBSTRUCTURE_PRIVILEGE_GATE
NEXT_OPERATION_AUTHORIZED = NO
```

The next gate should stop optimizing seeds and instead test whether any intrinsic, non-result-directed property of generated closed substructures can select the empirical interface without importing the desired physical response structure.

Candidate control classes should include:

- smallest nontrivial closed substructure;
- largest grammar-generated reachable substructure;
- automorphism-invariant closed substructure;
- fixed-point/canonical closure constructions;
- intersection or union of empirically seeded closures;
- explicit underdetermination controls when multiple closed substructures satisfy the same intrinsic criterion.

R2 remains deferred.

---

## 13. Final boundary

```text
GENERATOR_EQUIVALENCE = QUALIFIED_FORMAL
SEED_PRESENTATION_INVARIANCE = PASS_FOR_CLOSURE_FACTORING_STRUCTURE
UNIQUE_MINIMUM_SEED = NOT_GENERAL
IRREDUNDANT_SEED_EXISTENCE = NOT_GENERAL
PHYSICAL_SEMANTIC_FACTORIZATION = UNESTABLISHED
EMPIRICAL_SUBSTRUCTURE_PRIVILEGE = UNESTABLISHED
PHYSICAL_GRAMMAR_FOUND = NO
PHYSICAL_LAW_DERIVED = NO
EMPIRICAL_PREDICTION = NONE
R1_SOLVED = NO
R2_STARTED = NO
FCP_EFFECT = NONE
```
