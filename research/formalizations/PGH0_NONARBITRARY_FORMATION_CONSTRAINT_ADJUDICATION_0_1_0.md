# PGH-0 Non-Arbitrary Formation Constraint Challenge — Adjudication 0.1.0

## 1. Operation

```text
OPERATION_ID = PGH0_NONARBITRARY_FORMATION_CONSTRAINT_CHALLENGE
REGISTRY_ID = PGH-OP-0005
CANONICAL_BASE = 0b1b563c8ce9b40f42c55f74132440535856845e
PREREGISTRATION_COMMIT = 0b5c6b21265a6df4599ff1f69cf4c9da37358a8e
SOURCE_BOUND_STATUS = NOT_YET_SOURCE_BOUND
NEW_SOURCE_COUNT = 0
PHYSICAL_BRIDGE = NOT_PERFORMED
```

The candidate constraints were tested in the preregistered order.

## 2. Central verdict

```text
OUTCOME = D__NONTRIVIAL_FORMAL_CONSTRAINTS_EXIST_BUT_ALL_REQUIRE_AN_UNEARNED_EXTRA_PREMISE
```

No tested principle currently qualifies as the sought representation-independent, non-arbitrary selector of formation.

The active baseline therefore remains:

```text
PGH-GRAM-0002 = EXTENSIONAL_FORMATION_BASELINE
STATUS = PROVISIONAL_FORMAL_BASELINE_NONPHYSICAL
SUCCESSOR_GRAMMAR_QUALIFIED = NO
```

Two new formal results do survive:

```text
PGH-DER-0002 = ISOMORPHISM_COVARIANCE_UNDERDETERMINATION
STATUS = QUALIFIED_FORMAL

PGH-DER-0003 = PARSE_COHERENCE_IMPLIES_ASSOCIATIVITY
STATUS = QUALIFIED_CONDITIONAL_FORMAL
```

Two attractive selection ideas are preserved as explicit failures:

```text
PGH-FAIL-0002 = STRONG_PERMUTATION_INVARIANCE_AS_LABEL_NEUTRALITY
PGH-FAIL-0003 = UNPRIVILEGED_SIMPLICITY_SELECTION
```

## 3. Baseline burden

The previous result showed that arbitrary `F subset A^3` can store any local admissibility table. The present burden is therefore not merely to find a compact condition that excludes some `F`.

The burden is stronger:

> The reason for imposing the condition must itself follow from existing PGH methodological commitments rather than being another selected rule whose necessity is unexplained.

This separates:

```text
FORMAL_EXCLUSION
```

from:

```text
NONARBITRARY_FORMAL_NECESSITY
```

and both from:

```text
PHYSICAL_NECESSITY
```

The last remains out of scope.

## 4. C1 — Isomorphism covariance / label neutrality

### Requirement

A candidate selection predicate `C(G)` should be unchanged by bijective relabeling:

\[
G\cong G'\Longrightarrow C(G)=C(G').
\]

This is necessary for the current representation-independence program.

### Result

It is not sufficient to select a formation law.

Let the formation structures of a fixed finite carrier size be partitioned into isomorphism classes. Any subset of those isomorphism classes defines an isomorphism-invariant selection predicate.

Therefore relabeling covariance constrains **how a selector may refer to labels**, but not **which structural classes it may choose**.

### Explicit two-label count

For a two-label carrier there are

\[
2^{2^3}=256
\]

ternary relations.

Under the nontrivial swap of the two labels, exactly 16 relations are fixed. Burnside's lemma therefore gives

\[
\frac{256+16}{2}=136
\]

isomorphism classes.

An arbitrary subset of these 136 classes is still relabeling-covariant. Thus even at this tiny size there are

\[
2^{136}
\]

possible class-selection predicates compatible with label neutrality.

### Verdict

```text
C1_RELABELING_COVARIANCE = NECESSARY_METHOD_CONSTRAINT
C1_NONARBITRARY_SELECTION = FAIL
C1_NONUNIVERSAL_EXCLUSION = NONE_BY_ITSELF
```

This is formalized separately as `PGH-DER-0002`.

## 5. C2 — Strong permutation invariance

### Requirement tested

Demand, for one fixed relation `F`,

\[
F(a,b,c)\iff F(\pi a,\pi b,\pi c)
\]

for every permutation `pi` of the carrier.

### Nontrivial formal effect

This condition is strong.

For a three-label carrier, the action of the full permutation group on ordered triples has exactly five orbits, determined by equality pattern:

1. all three labels equal;
2. first equals second only;
3. first equals third only;
4. second equals third only;
5. all three distinct.

A fully permutation-invariant ternary relation is therefore determined by choosing which of these five orbits are admitted:

\[
2^5=32
\]

relations, compared with

\[
2^{27}=134{,}217{,}728
\]

arbitrary ternary relations.

So the condition produces enormous formal exclusion.

### Why it does not qualify

Label neutrality does not imply that every permutation is an automorphism of the same relational structure.

Example:

```text
A = {0,1,2}
F = {(0,0,0)}
```

Renaming `0` to `1` produces an isomorphic presentation with relation `{(1,1,1)}`. The physical or grammatical content may be label-neutral while the original relation is not invariant under that permutation as a fixed labeled table.

Demanding all permutations be automorphisms therefore adds **homogeneity**: no element may acquire relational individuality through `F`.

That is a substantive extra premise, not a consequence of representation independence.

### Verdict

```text
C2_FORMAL_EXCLUSION = PASS
C2_RELABELING_INVARIANCE = PASS
C2_JUSTIFIED_BY_LABEL_NEUTRALITY = FAIL
C2_NONARBITRARY_AT_CURRENT_SCOPE = FAIL
```

The conflation is preserved as `PGH-FAIL-0002`.

## 6. C3 — Extensional irredundancy

The previous PGH-0 result quotient-reduced labels with identical complete formation profiles.

As a canonicalization rule this remains valid.

But requiring an already-presented relation to be extensional does not select a substantive formation law.

### Exhaustive two-label check

Among all 256 ternary relations on a two-label carrier, exactly 254 already have distinct complete formation profiles for the two labels.

The only non-extensional cases are:

```text
F = empty
F = A^3
```

which collapse to one contextual class under the extensional quotient.

More generally, every formation structure has an extensional quotient. Thus extensionality chooses a reduced representative of contextual behavior rather than selecting which contextual behavior is allowed to exist.

### Verdict

```text
C3_CANONICALIZATION = PASS
C3_SUBSTANTIVE_FORMATION_SELECTION = FAIL
C3_GENERATIVE_COMPRESSION_OF_LAW = FAIL
```

Extensionality remains useful but does not solve `PGH-Q-0011`.

## 7. C4 — Decomposition / parse coherence

### Restricted representation

Consider a total deterministic binary operation

\[
\star:A\times A\to A.
\]

Assume, conditionally, that the two binary parse trees for three terms represent the same grammar-internal composite:

\[
((a\star b)\star c)\quad\text{and}\quad(a\star(b\star c)).
\]

If grammar-internal result identity is equality in this representation, coherence requires

\[
(a\star b)\star c=a\star(b\star c)
\]

for all `a,b,c`.

Thus parenthesization-independence forces associativity.

### Exact finite check

There are 16 total binary operations on a two-element carrier.

Exactly 8 are associative and 8 are nonassociative.

So coherence excludes half of the smallest nontrivial operation tables.

An explicit nonassociative table is:

```text
* | 0 1
--+----
0 | 0 0
1 | 1 0
```

For `a=1, b=0, c=1`:

```text
(1*0)*1 = 0
1*(0*1) = 1
```

An associative witness is XOR on `{0,1}`:

```text
* | 0 1
--+----
0 | 0 1
1 | 1 0
```

### Scientific interpretation

The theorem is exact **conditional on the coherence premise**.

What PGH has not established is that parenthesization must be representational rather than grammatically meaningful. A parse tree may itself carry legitimate structure.

Therefore:

```text
C4_CONDITIONAL_FORMAL_DERIVATION = PASS
C4_NONUNIVERSAL_EXCLUSION = PASS_CONDITIONALLY
C4_COHERENCE_PREMISE_ALREADY_EARNED = NO
C4_NONARBITRARY_AT_CURRENT_SCOPE = NOT_ESTABLISHED
```

This is preserved as `PGH-DER-0003` rather than promoted to a law of the baseline grammar.

## 8. C5 — Arity / encoding neutrality

An `n`-ary formation can often be represented by a binary tree with auxiliary labels for partial formations.

But two such encodings need not be literally isomorphic as bare `(A,F)` structures. To say that they represent the same formation content requires extra structure such as:

- a projection that forgets auxiliary labels;
- a translation map between encodings;
- an equivalence relation on derivation trees;
- or a common higher-level object to which both encodings map.

None of these is present in `PGH-GRAM-0002`.

If the translation/equivalence map may be chosen arbitrarily, the selection problem has merely moved from `F` into the map.

### Verdict

```text
C5_ARITY_NEUTRALITY_GOAL = WELL_MOTIVATED
C5_INTRINSIC_FORMULATION_FROM_BARE_F = NOT_AVAILABLE
C5_UNIQUE_CONSTRAINT = NOT_DERIVED
C5_SELECTION_ARBITRARINESS = UNRESOLVED_IN_TRANSLATION_STRUCTURE
```

This sharpens `PGH-Q-0012`.

## 9. C6 — Generative compression / simplicity

PGH requires a successful deep grammar to exhibit generative compression. That does not yet furnish a representation-independent selector.

For any finite relation `F`, one can define a description language with a primitive token whose meaning is exactly `F`. In that language, `F` has a one-token description.

Conversely, the same `F` can be given a deliberately verbose encoding.

Therefore raw description length cannot be treated as intrinsic until the project justifies a privileged or suitably invariant description framework.

Even after choosing a complexity measure, multiple inequivalent relations may tie for minimum complexity.

### Verdict

```text
C6_GENERATIVE_COMPRESSION_AS_GOAL = RETAINED
C6_PRIVILEGED_COMPLEXITY_MEASURE = NONE
C6_REPRESENTATION_INVARIANCE = FAIL_AT_CURRENT_SCOPE
C6_NONARBITRARY_SELECTION = FAIL
```

This failure is preserved as `PGH-FAIL-0003`.

## 10. C7 — Extremal controls

With no additional constraint:

```text
MAXIMAL_PERMISSIVENESS -> F = A^3
MINIMAL_PERMISSIVENESS -> F = empty
```

These reproduce the two extreme countermodels already exposed by `PGH-FAIL-0001`.

Choosing an extremum therefore does not explain physical or grammatical restriction; it only selects a trivial edge of the admissibility lattice.

```text
C7_MAXIMAL_CONTROL = TRIVIAL_UNIVERSAL_FORMATION
C7_MINIMAL_CONTROL = TRIVIAL_EMPTY_FORMATION
C7_NONARBITRARY_NONTRIVIAL_SELECTION = FAIL
```

## 11. Candidate comparison

| Candidate | Formal exclusion? | Relabeling-safe? | New unearned premise? | Solves central burden? |
|---|---:|---:|---:|---:|
| C1 Isomorphism covariance | No | Yes | No | No |
| C2 Strong permutation invariance | Yes | Yes | Yes: homogeneity | No |
| C3 Extensionality | Only redundant presentations | Yes | No | No |
| C4 Parse coherence | Yes, conditionally | Yes in binary representation | Yes: parse equivalence | No, not yet |
| C5 Arity/encoding neutrality | Not intrinsically formulated | Intended | Translation structure required | No |
| C6 Simplicity/compression | Potentially | Not yet | Complexity language/measure | No |
| C7 Extremal controls | Yes but trivial | Yes | Extremal choice | No |

## 12. Nontriviality implications

No successor grammar passes the opening physical/nontriviality gate.

The most important updates are:

```text
N1_UNIVERSAL_ENCODING = STILL_UNRESOLVED_FOR_ANY_SUCCESSOR
N2_NO_SMUGGLING = PASS_FOR_THE_PURE_FORMAL_THEOREMS_ONLY
N3_NONUNIVERSAL_EXCLUSION = PASS_CONDITIONALLY_FOR_PARSE_COHERENCE
N4_REPRESENTATION_INVARIANCE = DEEPENED_BUT_NOT_SOLVED
N6_GENERATIVE_COMPRESSION = STILL_UNESTABLISHED_AS_A_SELECTOR
N7_INDEPENDENT_CONSEQUENCE = CONDITIONAL_ONLY
N8_COUNTEREXAMPLE_EXPOSURE = PASS
N9_RELABELING_INVARIANCE = PASS_FOR_QUALIFIED_FORMAL_RESULTS
N10_PHYSICAL_BRIDGE = NOT_APPLICABLE
```

The central PGH gate remains closed.

## 13. What the experiment actually found

The experiment did not find a deep law of formation.

It identified a hierarchy:

\[
\text{label covariance}
<
\text{structural coherence premise}
<
\text{derived algebraic restriction}.
\]

The first level is too weak to select.

The second can generate real exclusions, but PGH must still justify **which representational differences are declared irrelevant**.

The third then follows conditionally.

This changes the sharpest research question from

> Which algebraic law should formation obey?

into

> What representation-equivalence or coherence principle can be justified without already encoding the law it will force?

## 14. New research burden

The best surviving lead is not “associativity is fundamental.”

It is:

```text
COHERENCE_AS_A_GENERATOR_OF_CONSTRAINT = PROMISING
PARTICULAR_COHERENCE_RELATION = NOT_YET_JUSTIFIED
```

The project should next attempt to formulate representation equivalence and coherence for general relational formation without presupposing binary arity, associativity, physical identity, or a privileged translation map.

## 15. Dependency ancestry

```text
PRIMITIVE_DEPENDENCIES = PGH-GRAM-0002_EXTensional_FORMATION_BASELINE
RULE_DEPENDENCIES = ISOMORPHISM_COVARIANCE; CONDITIONAL_PARSE_COHERENCE
LEMMA_DEPENDENCIES = BURNSIDE_COUNT_SPECIAL_CASE; ASSOCIATIVITY_EQUIVALENCE_IN_BINARY_TOTAL_CASE
SEMANTIC_ASSUMPTIONS = BARE_WELL_FORMEDNESS; CONDITIONAL_PARSE_EQUIVALENCE_FOR_PGH-DER-0003_ONLY
PHYSICAL_ASSUMPTIONS = NONE
SOURCE_DEPENDENCIES = NONE
METALANGUAGE_DEPENDENCIES = ORDINARY_LOGIC; FINITE_SETS; RELATIONS; FUNCTIONS; PERMUTATIONS; EQUALITY; FINITE_ENUMERATION
```

## 16. Hard non-effects

```text
PHYSICAL_GRAMMAR_FOUND = NO
PHYSICAL_LAW_DERIVED = NO
ASSOCIATIVITY_IS_PHYSICAL = NO
SYMMETRY_IS_PHYSICAL = NO
LOCALITY_DERIVED = NO
CAUSALITY_DERIVED = NO
TIME_DERIVED = NO
CONSERVATION_DERIVED = NO
GAUGE_STRUCTURE_DERIVED = NO
EMPIRICAL_PREDICTION = NONE
FCP_EFFECT = NONE
```

## 17. Next recommended operation

```text
NEXT_RECOMMENDED_OPERATION = PGH0_REPRESENTATION_EQUIVALENCE_AND_COHERENCE_CHALLENGE
NEXT_OPERATION_AUTHORIZED = NO
```

That future operation should ask whether a noncircular notion of equivalence between formation representations can be defined strongly enough to force coherence but weakly enough not to encode the desired algebraic law.
