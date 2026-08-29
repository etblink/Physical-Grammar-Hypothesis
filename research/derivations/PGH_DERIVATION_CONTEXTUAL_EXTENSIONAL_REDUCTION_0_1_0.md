# PGH-DER-0001 — Contextual Extensional Reduction 0.1.0

## Identity

```text
DERIVATION_ID = PGH-DER-0001
OPERATION_ID = PGH0_MINIMAL_GRAMMAR_CHALLENGE
STATUS = QUALIFIED_FORMAL
CLAIM_SCOPE = BARE_FORMATION_WELL_FORMEDNESS_ONLY
PHYSICAL_CLAIM = NONE
```

## Claim

For a bare relational formation grammar `G = (A,F)` with

\[
F\subseteq A^3,
\]

grammar-internal `IDENTIFY` and `DISTINGUISH` need not be independent object-level primitives if the only grammar-internal test is well-formedness of finite formation structures.

They are induced by the complete formation-incidence profile of each label.

## Definitions

For `a in A` define:

\[
L_F(a)=\{(b,c):F(a,b,c)\},
\]

\[
R_F(a)=\{(b,c):F(b,a,c)\},
\]

\[
O_F(a)=\{(b,c):F(b,c,a)\}.
\]

Let

\[
P_F(a)=(L_F(a),R_F(a),O_F(a)).
\]

Define:

\[
a\equiv_F b \iff P_F(a)=P_F(b),
\]

and

\[
a\not\equiv_F b \iff P_F(a)\neq P_F(b).
\]

The first is grammar-internal identification; the second is grammar-internal distinction.

## Lemma 1 — Equivalence

`≡_F` is an equivalence relation.

### Proof

`≡_F` is equality of the ordered triples of sets `P_F(a)`. Equality is reflexive, symmetric, and transitive. Therefore `≡_F` is reflexive, symmetric, and transitive. QED.

## Lemma 2 — Coordinate substitution

If `a ≡_F a'`, then for every `b,c in A`:

\[
F(a,b,c)\leftrightarrow F(a',b,c),
\]

\[
F(b,a,c)\leftrightarrow F(b,a',c),
\]

\[
F(b,c,a)\leftrightarrow F(b,c,a').
\]

### Proof

The three biconditionals are respectively equality of `L_F`, `R_F`, and `O_F`. QED.

## Theorem 1 — Finite-context substitutability

Let `T` be any finite binary formation tree labeled by elements of `A`, with well-formedness determined solely by the requirement that every internal node satisfy `F(left,right,parent)`.

If one occurrence of label `a` is replaced by `a'` and `a ≡_F a'`, then `T` is well formed before replacement if and only if it is well formed after replacement.

### Proof

Only local formation clauses incident to the replaced occurrence can change. The occurrence may appear as first child, second child, or parent/result. Each affected clause is preserved by Lemma 2. Every other local clause is unchanged. Therefore conjunction of all local well-formedness clauses is preserved. QED.

## Theorem 2 — Converse contextual completeness

If substituting `a` for `b` preserves well-formedness in every finite one-hole formation context, then `a ≡_F b`.

### Proof

The allowed finite contexts include depth-one contexts placing the hole separately in:

1. the first argument of `F(-,x,y)`;
2. the second argument of `F(x,-,y)`;
3. the result coordinate of `F(x,y,-)`.

Preservation of well-formedness in all such contexts gives equality of `L_F(a)` with `L_F(b)`, `R_F(a)` with `R_F(b)`, and `O_F(a)` with `O_F(b)`. Hence `P_F(a)=P_F(b)`. QED.

## Corollary — Context profile equivalence

For the bare formation grammar:

\[
a\equiv_F b
\]

if and only if no finite formation context can distinguish the two labels by grammatical well-formedness.

Thus the one-step incidence definition and the preregistered all-context definition coincide at this scope.

## Theorem 3 — Quotient well-definedness

Let

\[
\bar A=A/{\equiv_F}.
\]

Define

\[
\bar F([a],[b],[c])\iff F(a,b,c).
\]

Then `Fbar` is well defined.

### Proof

Suppose `a≡a'`, `b≡b'`, and `c≡c'`. Apply Lemma 2 successively in the first, second, and result coordinates:

\[
F(a,b,c)
\leftrightarrow F(a',b,c)
\leftrightarrow F(a',b',c)
\leftrightarrow F(a',b',c').
\]

Therefore the truth value is independent of representatives. QED.

## Theorem 4 — Extensional reduction

The quotient grammar `(Abar,Fbar)` has no two distinct quotient elements with identical complete formation profiles.

### Proof

Assume `[a]` and `[b]` have identical quotient formation profiles. Pulling those incidences back to representatives shows that `a` and `b` have identical original incidence profiles, hence `a≡_F b`, so `[a]=[b]`. QED.

## Finite witness

Take

```text
A = {a,b,g}
```

and exactly the six formation facts:

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
L_F(a) = L_F(b) = {(g,g)}
R_F(a) = R_F(b) = {(g,g)}
O_F(a) = O_F(b) = {(g,g)}
```

so `a ≡_F b` despite literal metalanguage inequality `a != b`.

The quotient contains `X=[a]=[b]` and `G=[g]`, with:

```text
Fbar(X,G,G)
Fbar(G,X,G)
Fbar(G,G,X)
```

This gives an explicit counterexample to the claim that literal label distinction must be an independent grammatical distinction.

## Exact scope limitation

The result depends on:

```text
SEMANTIC_ASSUMPTION = WELL_FORMEDNESS_IS_THE_ONLY_GRAMMAR_INTERNAL_TEST
```

If a later theory introduces additional grammar-internal values, observables, weights, amplitudes, probabilities, geometry, or physical semantics, then its contextual equivalence may be finer than `≡_F`.

Therefore this derivation does NOT establish:

```text
ALL_POSSIBLE_EQUIVALENCE_IS_DERIVED_FROM_FORMATION = NO
PHYSICAL_IDENTITY_IS_CONTEXTUAL_EQUIVALENCE = NO
GAUGE_EQUIVALENCE_DERIVED = NO
OBSERVATIONAL_EQUIVALENCE_DERIVED = NO
```

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = ABSTRACT_FORMATION_RELATION
RULE_DEPENDENCIES = NONE_BEYOND_FORMATION_WELL_FORMEDNESS
LEMMA_DEPENDENCIES = PROFILE_EQUALITY; LOCAL_SUBSTITUTION
SEMANTIC_ASSUMPTIONS = WELL_FORMEDNESS_ONLY
PHYSICAL_ASSUMPTIONS = NONE
SOURCE_DEPENDENCIES = NONE
METALANGUAGE_DEPENDENCIES = EQUALITY; SET_OR_CLASS_MEMBERSHIP; RELATIONS; FINITE_TREES; QUANTIFICATION
```

## Result

```text
PGH-DER-0001 = QUALIFIED_FORMAL
IDENTIFY_INDEPENDENT_PRIMITIVE = REDUNDANT_AT_THIS_SCOPE
DISTINGUISH_INDEPENDENT_PRIMITIVE = REDUNDANT_AT_THIS_SCOPE
PHYSICAL_CONSEQUENCE = NONE
```
