# PGH-0 Minimal Grammar Formalization 0.1.0

## 1. Operation

```text
OPERATION_ID = PGH0_MINIMAL_GRAMMAR_CHALLENGE
REGISTRY_ID = PGH-OP-0003
CANONICAL_BASE = ac6baff2596eedbe3902b07dfe5e5ee2e69ac918
PREREGISTRATION_COMMIT = 98ece4fb0d282072df33a629f8dbecde3ed1b1cf
SOURCE_BOUND_STATUS = NOT_YET_SOURCE_BOUND
NEW_SOURCE_COUNT = 0
```

This artifact performs the formal reduction preregistered before the result was selected.

No physical interpretation is assumed.

## 2. Result summary

The opening three-name shell

\[
\{\mathrm{DISTINGUISH},\mathrm{COMPOSE},\mathrm{IDENTIFY}\}
\]

is not minimal as a set of independent object-level primitives under the weakest semantics in which the grammar exposes only formal well-formedness.

The result is:

```text
IDENTIFY_AS_INDEPENDENT_PRIMITIVE = NOT_REQUIRED_AT_MINIMAL_WELL_FORMEDNESS_SCOPE
DISTINGUISH_AS_INDEPENDENT_PRIMITIVE = NOT_REQUIRED_AT_MINIMAL_WELL_FORMEDNESS_SCOPE
BINARY_COMPOSE_AS_FUNDAMENTAL = NOT_ESTABLISHED
GENERATIVE_OR_FORMATION_RELATION = STILL_REQUIRED_FOR_A_GENERATIVE_GRAMMAR
```

The surviving formal core is therefore weakened to an **extensional formation baseline** rather than promoted as a physical grammar.

```text
SUCCESSOR_FORMAL_OBJECT = PGH-GRAM-0002
WORKING_NAME = EXTENSIONAL_FORMATION_BASELINE
STATUS = PROVISIONAL_FORMAL_BASELINE_NONPHYSICAL
```

## 3. Metalanguage boundary

Let `A` be a nonempty set of formal labels in the mathematical metalanguage.

Membership in `A`, literal equality of labels, quantification, finite products, relations, and finite trees are analysis machinery. They are not declared to be physical primitives.

The fact that the metalanguage distinguishes two symbols does not imply that the candidate grammar itself distinguishes them.

This separation is essential.

## 4. Weak formation shell

Begin with a ternary relation

\[
F \subseteq A\times A\times A.
\]

Write

\[
F(a,b,c)
\]

only to mean that the ordered formal pair `(a,b)` participates in an allowed local formation with formal result label `c`.

This does not mean:

```text
FIRST_ARGUMENT = EARLIER_IN_TIME
SECOND_ARGUMENT = LATER_IN_TIME
RESULT = PHYSICAL_OUTPUT
F = CAUSAL_PROCESS
A = PHYSICAL_OBJECT_SET
```

No uniqueness is required. For fixed `(a,b)`, zero, one, or many `c` may satisfy `F(a,b,c)`.

Therefore the shell is weaker than a partial binary function.

Not assumed:

```text
ASSOCIATIVITY
COMMUTATIVITY
IDENTITIES
INVERSES
TYPES
BOUNDARIES
LOCALITY
CAUSALITY
DETERMINISM
CATEGORY_STRUCTURE
```

## 5. Grammar-internal incidence profile

For each `a in A`, define three purely relational incidence sets:

\[
L_F(a)=\{(b,c):F(a,b,c)\},
\]

\[
R_F(a)=\{(b,c):F(b,a,c)\},
\]

\[
O_F(a)=\{(b,c):F(b,c,a)\}.
\]

Define the complete one-step formation profile

\[
P_F(a)=(L_F(a),R_F(a),O_F(a)).
\]

This profile records every way the label can affect local well-formedness in each coordinate.

## 6. Derived IDENTIFY

Define

\[
a\equiv_F b
\quad\Longleftrightarrow\quad
P_F(a)=P_F(b).
\]

This is reflexive, symmetric, and transitive because it is equality of mathematical profiles.

No independent object-level `IDENTIFY` relation is needed to obtain this grammar-internal equivalence.

The result is limited:

> `a ≡_F b` means only that the bare formation grammar cannot tell `a` and `b` apart through well-formedness.

It does not establish physical identity, gauge equivalence, observational equivalence, or metaphysical identity.

## 7. Derived DISTINGUISH

Define grammar-internal distinction by

\[
\mathrm{Dist}_F(a,b)
\quad\Longleftrightarrow\quad
P_F(a)\neq P_F(b).
\]

Thus under bare well-formedness semantics:

```text
DISTINGUISH = DIFFERENT_FORMATION_PROFILE
IDENTIFY = SAME_FORMATION_PROFILE
```

Literal metalanguage inequality may remain even when the grammar does not distinguish two labels.

Keeping a difference that has no possible grammatical effect would add haecceitic structure beyond this minimal grammar.

PGH-0 does not prohibit such extra structure in all future theories; it only finds that it is unnecessary for the minimal grammar studied here.

## 8. Compatibility with all finite formation contexts

A finite formation tree is a finite binary tree whose nodes are labeled in `A` and whose every internal node satisfies `F(left_label,right_label,parent_label)`.

Suppose `a ≡_F b`.

Replacing one occurrence of `a` by `b` can affect at most three local roles of that label:

1. first child of a parent;
2. second child of a parent;
3. parent/result of its own two children.

Equality of `L_F`, `R_F`, and `O_F` preserves the relevant `F` truth value in every case.

Therefore substitution of `a` by `b` preserves well-formedness of every finite labeled formation tree.

Conversely, the depth-one contexts that place the hole in each of these three roles recover the three incidence sets. Hence indistinguishability in all finite formation contexts is equivalent to equality of the incidence profile.

This validates the preregistered contextual-equivalence idea without requiring physical observables.

## 9. Extensional quotient

Let

\[
\bar A=A/{\equiv_F}.
\]

Define

\[
\bar F([a],[b],[c])
\quad\Longleftrightarrow\quad
F(a,b,c).
\]

Because equivalent labels have identical incidence in every coordinate, this definition is independent of the chosen representatives.

Thus the relation descends to the quotient.

The quotient contains no two distinct classes with the same complete formation profile.

This is the **extensional formation baseline**.

The quotient is a canonical reduction of redundant formal labels relative to the bare grammar's own well-formedness behavior.

It is not a physical law.

## 10. Explicit finite witness

Let

```text
A = {a, b, g}
```

and let `F` contain exactly:

```text
F(a,g,g)
F(b,g,g)
F(g,a,g)
F(g,b,g)
F(g,g,a)
F(g,g,b)
```

Then:

```text
P_F(a) = P_F(b)
P_F(a) != P_F(g)
```

so:

```text
a ≡_F b
a and b are literally different metalanguage labels
```

The extensional quotient has two classes:

```text
X = [a] = [b]
G = [g]
```

with formation relation:

```text
Fbar(X,G,G)
Fbar(G,X,G)
Fbar(G,G,X)
```

This finite witness demonstrates that literal label multiplicity is not required to carry distinct grammatical behavior.

## 11. M1 verdict — remove IDENTIFY

```text
M1_REMOVE_IDENTIFY = PASS_AT_MINIMAL_WELL_FORMEDNESS_SCOPE
```

An independent equivalence primitive is unnecessary because `≡_F` is induced by the formation relation.

Limitation:

If later semantics includes structure not visible through bare formation well-formedness, contextual equivalence may need refinement. The result therefore does not prove that every future PGH formalism can eliminate identity/equivalence structure.

## 12. M2 verdict — remove DISTINGUISH

```text
M2_REMOVE_DISTINGUISH = PASS_AT_MINIMAL_WELL_FORMEDNESS_SCOPE
```

Grammar-internal distinction is the failure of contextual equivalence.

A primitive notion of *literal* difference remains available in the metalanguage but carries no grammatical content unless it changes formation behavior.

## 13. M3 verdict — remove COMPOSE

Two different claims must be separated.

### 13.1 Is some generative/formation mechanism required?

Yes, by the meaning of a generative grammar used in this project.

A bare carrier `A` with only metalanguage equality can list labels but has no object-level rule that forms larger admissible structures from them.

Some additional formation, production, rewrite, extension, or equivalent generative relation is therefore required if the system is to be a grammar rather than a vocabulary.

This is a definitional architecture result, not a law of physics.

### 13.2 Is binary COMPOSE fundamental?

No such result follows.

An `n`-ary formation rule can be represented using binary relations by introducing auxiliary labels for partial formations and choosing a bracketing. Different bracketings and auxiliary-label schemes give different binary representations of the same higher-arity rule.

Therefore binary arity is representationally sufficient for many finite constructions but is not representation-independently privileged by PGH-0.

Verdict:

```text
M3_REMOVE_BINARY_COMPOSE = PASS
M3_REMOVE_ALL_GENERATIVITY = FAIL_BY_PROJECT_DEFINITION
SURVIVING_CORE = ABSTRACT_FORMATION_OR_GENERATIVE_RELATION
```

## 14. Minimality verdict

The preregistered three-name shell is superseded as an independent primitive basis.

```text
MINIMALITY_OUTCOME = D__ALL_THREE_REFORMULATED_INTO_A_DIFFERENT_WEAKER_CORE
```

More precisely:

- `IDENTIFY` becomes derived contextual equivalence;
- `DISTINGUISH` becomes derived contextual inequivalence;
- binary `COMPOSE` is weakened to an arity-neutral requirement for some formation/generative relation.

This does not establish that one unique mathematical formalism is fundamental.

## 15. Universal-table counterexample

The surviving bare formation relation is still far too unconstrained to support strong PGH.

For any finite carrier `A` and any desired local admissibility table

\[
S\subseteq A^3,
\]

choose simply

\[
F=S.
\]

Then the grammar reproduces exactly that table.

Every local exclusion is therefore selectable by hand through the choice of `F`.

At this level the grammar has explained no reason for one admissibility relation rather than another.

Two extreme countermodels make the point explicit:

```text
F = A^3       -> every local triple is allowed
F = empty     -> no local triple is allowed
```

The architecture itself chooses neither.

## 16. Nontriviality results for PGH-GRAM-0002

```text
N0_FORMAL_DEFINABILITY = PASS
N1_UNIVERSAL_ENCODING = FAIL
N2_NO_SMUGGLING = PASS_FOR_THE_PURE_FORMAL_REDUCTION
N3_NONUNIVERSAL_EXCLUSION = FAIL
N4_REPRESENTATION_INVARIANCE = PARTIAL
N5_SEMANTIC_LOAD = NOT_APPLICABLE
N6_GENERATIVE_COMPRESSION = FAIL
N7_INDEPENDENT_CONSEQUENCE = FAIL
N8_COUNTEREXAMPLE_EXPOSURE = PASS
N9_RELABELING_INVARIANCE = PASS
N10_PHYSICAL_BRIDGE = NOT_APPLICABLE
```

Explanations:

- **N0:** membership in `F`, contextual equivalence, and quotienting are exact.
- **N1:** arbitrary admissibility tables can be encoded directly in `F`.
- **N2:** no physical content is used in the formal reduction itself. This does not mean a future physically chosen `F` would pass the same audit.
- **N3:** absent triples are exclusions, but their absence is inserted in `F`; no compact grammar-internal principle derives them.
- **N4:** the reduction is invariant under bijective relabeling/isomorphism of `(A,F)`, but no genuinely different mathematical surface-language translation has yet been tested.
- **N5:** there is no physical semantics map in this operation.
- **N6:** arbitrary `F` may require a table as complex as the admissibility facts it encodes.
- **N7:** no independent physical or even non-table-driven formation restriction follows.
- **N8:** full, empty, and duplicate-profile finite models expose definite failure modes.
- **N9:** profile equality and the quotient are invariant under arbitrary bijective renaming of labels.

## 17. Candidate-level outcome

```text
PGH-GRAM-0002_OUTCOME = FORMALLY_INTERESTING_NONPHYSICAL
OPENING_PGH0_GATE = FAIL_TO_ADVANCE_TO_PHYSICAL_BRIDGE
```

This is not a rejection of PGH.

It is a rejection of the idea that **bare generativity plus extensional reduction is already enough**.

## 18. Dependency ancestry

```text
PRIMITIVE_DEPENDENCIES = ABSTRACT_FORMATION_RELATION
RULE_DEPENDENCIES = CONTEXT_PROFILE_DEFINITION; EXTENSIONAL_QUOTIENT
LEMMA_DEPENDENCIES = PROFILE_EQUALITY_IS_EQUIVALENCE; PROFILE_EQUALITY_PRESERVES_LOCAL_FORMATION
SEMANTIC_ASSUMPTIONS = WELL_FORMEDNESS_IS_THE_ONLY_GRAMMAR_INTERNAL_TEST_AT_THIS_STAGE
PHYSICAL_ASSUMPTIONS = NONE
SOURCE_DEPENDENCIES = NONE
METALANGUAGE_DEPENDENCIES = ORDINARY_LOGIC; SET_OR_CLASS_MEMBERSHIP; EQUALITY; FINITE_TREES; RELATIONS
```

## 19. What remains live

The central next problem becomes sharper:

> What is the weakest non-arbitrary, representation-independent constraint on formation/generativity that produces a restriction not merely entered as an admissibility table?

A second unresolved problem is:

> Can the formation relation itself be formulated without privileging binary arity, ordered argument positions, or one mathematical surface language?

These are new research burdens, not solved by the present reduction.

## 20. Hard non-effects

```text
PHYSICAL_LAW_DERIVED = NO
PHYSICAL_GRAMMAR_FOUND = NO
EMPIRICAL_PREDICTION = NONE
EMPIRICAL_DISCRIMINATOR = NONE
CONSERVATION_DERIVED = NO
TIME_DERIVED = NO
LOCALITY_DERIVED = NO
CAUSALITY_DERIVED = NO
GAUGE_STRUCTURE_DERIVED = NO
PHYSICAL_SYMMETRY_DERIVED = NO
FCP_EFFECT = NONE
```
