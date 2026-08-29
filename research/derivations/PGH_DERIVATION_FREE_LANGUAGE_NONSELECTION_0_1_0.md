# PGH-DER-0015 — Free Language Nonselection 0.1.0

## Status

```text
DERIVATION_ID = PGH-DER-0015
DERIVATION_STATUS = QUALIFIED_FORMAL
PHYSICAL_CLAIM = NONE
NOVELTY_CLAIM = NONE
```

## Statement

Let `Sigma` be a fixed (possibly many-sorted) algebraic signature and let `T_Sigma(X)` be the free term algebra on generators/variables `X`, with no nontrivial equations imposed beyond syntactic/definitional identity.

Then no equation between syntactically distinct well-sorted terms is forced solely by free generation.

Equivalently, if `t` and `u` are syntactically distinct terms of the same sort, then

\[
t=u
\]

is not valid in all `Sigma`-algebras.

## Proof

Use the free term algebra `T_Sigma(X)` itself as a `Sigma`-algebra.

Each term evaluates to its own syntactic term element.

If `t` and `u` are syntactically distinct, then as elements of the free term algebra

\[
t\neq u.
\]

Therefore there exists a `Sigma`-algebra—namely the free term algebra—in which the proposed equation fails.

Hence the equation cannot follow from the signature and free construction alone.

## Consequence

A free construction can provide:

- arbitrary iteration of the given operations;
- substitution/composition according to the signature;
- canonical generated syntax relative to the supplied generators.

It cannot by itself provide a nontrivial equational law.

Any such law must enter through at least one additional source:

```text
SELECTIVE_SIGNATURE_OR_SORT_STRUCTURE
ADDITIONAL_EQUATIONS
REWRITE_OR_COHERENCE_RULES
SEMANTIC_RESTRICTION
```

If a typed/partial signature already rejects some compositions, that selectivity is genuine formal selectivity, but it resides in the type/domain declarations rather than being produced by free generation.

## PGH interpretation

```text
FREE_LANGUAGE_CANONICALITY = CONDITIONAL_ON_SIGNATURE
FREE_LANGUAGE_GENERATIVITY = YES
FREE_LANGUAGE_EQUATIONAL_SELECTIVITY = NO
SIGNATURE_ORIGIN = UNRESOLVED
R2_PHYSICAL_CREDIT = NONE
```

The theorem does not say free constructions are unimportant. It says a universal property cannot erase the need to account for the data supplied to that universal property.

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = []
RULE_DEPENDENCIES = [FREE_TERM_ALGEBRA_DEFINITION]
LEMMA_DEPENDENCIES = []
SEMANTIC_ASSUMPTIONS = NONE
PHYSICAL_ASSUMPTIONS = NONE
SOURCE_DEPENDENCIES = FROZEN_PRIOR_ART_CONTEXT_ONLY
```

## Failure exposure

A claimed PGH derivation of physical law from a free language fails this control if the allegedly derived law is actually encoded in:

- operation domains/codomains;
- sort declarations;
- primitive equations;
- primitive rewrite rules;
- semantic interpretation.

## Claim ceiling

```text
FORMAL_THEOREM = YES
META_LANGUAGE_SELECTED = NO
SUCCESSOR_GRAMMAR = NO
PHYSICAL_LAW_DERIVED = NO
```
