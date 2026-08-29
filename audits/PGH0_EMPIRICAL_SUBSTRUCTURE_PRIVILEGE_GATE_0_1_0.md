# PGH-0 Empirical Substructure Privilege Gate 0.1.0

## Identity

```text
OPERATION_ID = PGH0_EMPIRICAL_SUBSTRUCTURE_PRIVILEGE_GATE
REGISTRY_ID = PGH-OP-0026
CANONICAL_BASE = 142e022d063bd38e685fb359d365bf6ca334f3ce
PREREGISTRATION_COMMIT = adbac814dee09357948221ea1f4918be3df4f776
FROZEN_SOURCE_COUNT = 37
NEW_SOURCE_SEARCH = NONE
R2_LAW_EXHAUSTION = NOT_STARTED
PHYSICAL_GRAMMAR_SELECTION = NONE
EMPIRICAL_PREDICTION = NONE
FCP_EFFECT = NONE
```

## Outcome

```text
OUTCOME = B__INTRINSIC_SELECTORS_CAN_SELECT_IN_SPECIAL_GRAMMARS_BUT_NO_TESTED_GENERAL_CRITERION_AVOIDS_NONUNIQUENESS_TRIVIAL_EXTREMES_OR_EXTRA_SELECTOR_INPUT
SYMMETRY_OBSTRUCTION = QUALIFIED_FORMAL
GENERAL_INTRINSIC_EMPIRICAL_SUBSTRUCTURE_SELECTOR = NOT_FOUND
SPECIAL_GRAMMAR_UNIQUE_INTRINSIC_SUBSTRUCTURE = POSSIBLE
EMPIRICAL_SUCCESS_SELECTOR = REJECTED_AS_RESULT_DIRECTED
R1_SOLVED = NO
R2_STARTED = NO
```

The gate establishes a conditional obstruction, not a universal impossibility theorem. Grammar-intrinsic structure can uniquely distinguish a proper closed substructure in some asymmetric grammars, but none of the tested generic selector principles supplies a nontrivial, unique, representation-respecting physical interface across grammar structures.

---

## 1. Symmetry-obstruction theorem

Let `L` be the family of closed substructures of a fixed grammar/closure structure and let `Aut` be its automorphism group.

Suppose a selector predicate `C(T)` is intrinsic in the sense that for every automorphism `alpha`:

\[
C(T)\Longleftrightarrow C(\alpha[T]).
\]

If exactly one `T* in L` satisfies `C`, then for every `alpha in Aut`, `alpha[T*]` also satisfies `C`. By uniqueness:

\[
\alpha[T^*]=T^*.
\]

Therefore any uniquely selected substructure under an automorphism-invariant intrinsic criterion must itself be fixed setwise by the full automorphism group.

This is qualified as `PGH-DER-0011`.

---

## 2. Symmetric witness

Take:

```text
P={a,b,c,d}
s(a)=b
s(b)=a
s(c)=d
s(d)=c
```

Closure is repeated application of `s`.

The closed substructures are exactly:

```text
empty
A={a,b}
B={c,d}
P={a,b,c,d}
```

There is an automorphism `alpha` with:

```text
a->c
b->d
c->a
d->b
```

which exchanges `A` and `B`.

The full automorphism group also contains the swaps inside each pair. The only closed substructures fixed setwise by **every** automorphism are:

```text
empty
P
```

Thus no automorphism-invariant criterion can uniquely select `A` rather than `B` without additional symmetry-breaking structure.

---

## 3. S1 — smallest nontrivial closed substructure

In the symmetric witness:

```text
A={a,b}
B={c,d}
```

are both inclusion-minimal nonempty closed substructures and both have cardinality `2`.

Therefore:

```text
SMALLEST_NONTRIVIAL_SELECTOR = NONUNIQUE
```

A tie-break would require additional structure.

---

## 4. S2 — largest reachable/generated substructure

The unique largest closed substructure is `P`.

This criterion is formally unique but does not distinguish an empirical interface from the entire ambient formal context universe:

```text
LARGEST_SELECTOR = P
PROPER_EMPIRICAL_RESTRICTION = NONE
```

Selecting `P` may be a logically possible physical hypothesis, but its uniqueness alone does not establish that every formal context is physically empirical. It therefore supplies no general physical-irrelevance criterion.

---

## 5. S3 — automorphism-invariant closed substructure

In the symmetric witness the fully invariant closed sets are exactly:

```text
empty
P
```

Thus automorphism invariance alone selects only trivial extremes and remains nonunique between them.

```text
AUTOMORPHISM_INVARIANCE_ALONE = INSUFFICIENT
```

---

## 6. S4 — fixed-point / canonical-operator selection

Every closed substructure satisfies:

\[
Cl(T)=T.
\]

Therefore closure-fixed-point status identifies **all** members of `L` and selects nothing.

If a new endomap

\[
F:L\to L
\]

is freely introduced, then any desired target `T0 in L` can be made the unique fixed point by defining

\[
F(S)=T_0
\]

for every `S`.

Hence:

```text
CLOSURE_FIXED_POINT = UNDERDETERMINED
FREE_CANONICAL_ENDOMAP = UNIVERSAL_TARGET_ENCODER
```

A further operator helps only if its own origin is independently justified from already accepted grammar structure.

---

## 7. S5 — intersection selectors

In the symmetric witness:

\[
A\cap B=\varnothing.
\]

Thus the intersection of all proper nontrivial closed substructures is empty.

The intersection of all nonempty closed substructures is also empty because both `A` and `B` occur.

```text
INTERSECTION_SELECTOR = TRIVIAL_EMPTY_CORE
```

The empty set is closed but does not supply a nontrivial empirical interface.

---

## 8. S6 — union / join selectors

The union of the two minimal empirical blocks is:

\[
A\cup B=P.
\]

It is already closed, so the join/closure of their union is `P`.

```text
UNION_SELECTOR = WHOLE_FORMAL_UNIVERSE
```

Again this is canonical but empirically nonselective at the present level.

---

## 9. S7 — simplicity tie-break

Selecting the simplest member of `{A,B}` does not help in the symmetric witness: the grammar automorphism exchanges them, so any representation-respecting complexity assignment intrinsic to the structure must assign equal structural complexity.

More generally, an external encoding language can make either candidate shorter by convention, reproducing `PGH-FAIL-0003`.

```text
UNPRIVILEGED_SIMPLICITY_TIE_BREAK = REJECTED
```

---

## 10. S8 — empirical-success selection

A rule that selects a closed substructure because its generated probes reproduce observed records, known physics, or a target distinguishability partition is scientifically meaningful as **model testing**, but it is not a grammar-intrinsic privilege principle.

Under the present R1 question it would import the empirical result used to identify the interface.

```text
EMPIRICAL_SUCCESS_AS_INTRINSIC_SELECTOR = RESULT_DIRECTED
```

This does not say empirical testing is illegitimate. It says empirical success cannot be re-described as an internally derived grammar selector.

---

## 11. Asymmetric control — intrinsic uniqueness can occur

Take:

```text
P={a,b}
f(a)=b
f(b)=b
```

The closed substructures are:

```text
empty
{b}
P
```

The unique smallest nonempty closed substructure is `{b}`.

Therefore:

```text
UNIQUE_INTRINSIC_PROPER_CLOSED_SUBSTRUCTURE_CAN_EXIST = YES
```

The symmetric obstruction does not prove that every grammar is underdetermined. It proves that no selector claimed to work **generally from invariant closure structure alone** can uniquely choose one of symmetry-related proper substructures.

The physical significance of `{b}` in the asymmetric example is still not established merely by mathematical uniqueness.

---

## 12. Acceptance-criteria result

```text
B1_SYMMETRY_OBSTRUCTION_IS_PROVED = PASS
B2_SMALLEST_SELECTOR_NONUNIQUENESS_IS_TESTED = PASS
B3_LARGEST_SELECTOR_TRIVIALITY_OR_SCOPE_IS_EXPOSED = PASS
B4_AUTOMORPHISM_INVARIANCE_IS_TESTED = PASS
B5_FIXED_POINT_UNDERDETERMINATION_IS_TESTED = PASS
B6_INTERSECTION_AND_UNION_CONTROLS_ARE_TESTED = PASS
B7_FREE_CANONICAL_OPERATOR_UNIVERSAL_ENCODING_IS_EXPOSED = PASS
B8_ASYMMETRIC_UNIQUE_SELECTOR_CONTROL_IS_INCLUDED = PASS
B9_EMPIRICAL_SUCCESS_IS_NOT_USED_AS_INTRINSIC_PRIVILEGE = PASS
B10_NO_GENERAL_IMPOSSIBILITY_CLAIM_IS_OVERSTATED = PASS
```

The preregistered outcome is therefore B.

---

## 13. Scientific interpretation

The R1 search has now passed through:

```text
formal equivalence
-> minimal semantic contact
-> representation robustness
-> grammar-generated interface closure
-> generator equivalence
-> intrinsic closed-substructure selection
```

At each stage, formal structure has removed avoidable representational choices, but no tested grammar-internal criterion has supplied the missing **physical privilege** in a general way.

This is now evidence that R1 has reached a real boundary rather than merely needing another routine closure construction.

The correct next step is therefore not to invent a seventh canonicality criterion. It is to adjudicate what the R1 failure means for residual strong PGH.

---

## 14. R1 consequence

```text
R1_FORMAL_EQUIVALENCE = INSUFFICIENT_FOR_PHYSICAL_PRIVILEGE
R1_LAW_FREE_EMPIRICAL_CONTACT = FORMALLY_ADMISSIBLE
R1_REPRESENTATION_ROBUSTNESS = PASS_CONDITIONALLY
R1_GRAMMAR_GENERATED_INTERFACE = FORMALLY_FEASIBLE
R1_GENERATOR_EQUIVALENCE = QUALIFIED_AT_CLOSURE_SCOPE
R1_GENERIC_INTRINSIC_SUBSTRUCTURE_SELECTOR = NOT_FOUND
R1_SPECIAL_GRAMMAR_INTRINSIC_UNIQUENESS = POSSIBLE
R1_PHYSICAL_PRIVILEGE = UNESTABLISHED
R1_SOLVED = NO
```

---

## 15. Source-gap decision

No specific frozen-corpus deficiency blocks this formal adjudication.

```text
SPECIFIC_SOURCE_GAP = NONE
SOURCE_EXPANSION_JUSTIFIED = NO
```

---

## 16. Next sequencing

Recommended next operation:

```text
NEXT_RECOMMENDED_OPERATION = PGH0_R1_PHYSICAL_IRRELEVANCE_BOUNDARY_ADJUDICATION
NEXT_OPERATION_AUTHORIZED = NO
```

That operation should determine whether:

1. residual strong PGH may consistently treat a law-free empirical interface/substructure as irreducible semantic contact while requiring grammar to generate substantive laws;
2. doing so weakens the original strong claim but leaves a scientifically nontrivial residual program;
3. R1 failure blocks or refutes the strong formulation because physical privilege remains external;
4. a sharply identified source gap—not another invented formal selector—is required before that judgment.

R2 must remain unstarted until this boundary is adjudicated.

---

## Final boundary

```text
GENERAL_INTRINSIC_EMPIRICAL_SUBSTRUCTURE_SELECTOR = NOT_FOUND
SPECIAL_INTRINSIC_UNIQUENESS = POSSIBLE
PHYSICAL_PRIVILEGE = UNESTABLISHED
R1_BOUNDARY_ADJUDICATION = REQUIRED
R1_SOLVED = NO
R2_STARTED = NO
PHYSICAL_GRAMMAR_FOUND = NO
PHYSICAL_LAW_DERIVED = NO
EMPIRICAL_PREDICTION = NONE
FCP_EFFECT = NONE
```
