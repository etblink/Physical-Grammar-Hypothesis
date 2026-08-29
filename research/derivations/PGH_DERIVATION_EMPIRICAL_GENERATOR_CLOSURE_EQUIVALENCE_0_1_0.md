# PGH-DER-0010 — Empirical Generator Closure Equivalence 0.1.0

## Identity

```text
DERIVATION_ID = PGH-DER-0010
OPERATION_ID = PGH0_EMPIRICAL_GENERATOR_INVARIANCE_AND_SEED_MINIMALITY_GATE
STATUS = QUALIFIED_FORMAL
PHYSICAL_CLAIM = NONE
```

## Generator equivalence

For a fixed closure operator `Cl`, define

\[
A\sim_{Cl}B \iff Cl(A)=Cl(B).
\]

This is an equivalence relation because equality of generated closures is reflexive, symmetric, and transitive.

## Factorization theorem

If a seed-level quantity factors through closure,

\[
Q(A)=\bar Q(Cl(A)),
\]

then equal-closure seeds satisfy `Q(A)=Q(B)`.

Therefore all closure-factoring structure is invariant under replacement of one generator by another generator of the same closed interface.

The converse is not automatic: a quantity depending on literal seed membership can distinguish seeds with identical closure. Any claim that seed identity is physically irrelevant therefore requires the relevant semantic dependence to factor through closure.

## Finite witness

Let

```text
P={a,b}
f(a)=b
f(b)=b
g(a)=a
g(b)=a
```

Then

\[
Cl(\{a\})=Cl(\{b\})=\{a,b\}.
\]

Both singleton seeds have minimum cardinality. The swap `a<->b` is not an automorphism because it does not commute with `f`:

\[
\sigma(f(a))=a\neq b=f(\sigma(a)).
\]

So equal-closure minimum generators need not be symmetry-related.

## Infinite witness

Let `P=N` with unary constructor

\[
p(0)=0,\qquad p(n+1)=n.
\]

A seed generates all of `N` exactly when it is unbounded. Removing one element from an unbounded subset leaves it unbounded. Hence every full generator remains generating after deletion of any one member, so no inclusion-irredundant generator exists for the full closure.

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = FIXED_GRAMMAR_GENERATED_CLOSURE
RULE_DEPENDENCIES = EQUALITY_OF_GENERATED_CLOSURES; OPTIONAL_CLOSURE_FACTORIZATION
SEMANTIC_ASSUMPTIONS = CLOSURE_FACTORIZATION_REQUIRED_FOR_SEED_INVARIANCE_BEYOND_GENERATION
PHYSICAL_ASSUMPTIONS = NONE
SOURCE_DEPENDENCIES = FROZEN_37_SOURCE_LANDSCAPE
METALANGUAGE_DEPENDENCIES = SETS; CLOSURE_OPERATORS; FUNCTIONS; CARDINALITY; AUTOMORPHISMS
```

## Result

```text
PGH-DER-0010 = QUALIFIED_FORMAL
GENERATOR_EQUIVALENCE = YES
CLOSURE_FACTORING_PROPERTIES_ARE_SEED_INVARIANT = YES
FULL_PHYSICAL_EQUIVALENCE = NOT_ESTABLISHED
UNIQUE_MINIMAL_GENERATOR = NOT_ESTABLISHED
```
