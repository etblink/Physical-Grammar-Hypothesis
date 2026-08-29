# PGH-DER-0011 — Intrinsic Substructure Selector Symmetry Obstruction 0.1.0

## Identity

```text
DERIVATION_ID = PGH-DER-0011
OPERATION_ID = PGH0_EMPIRICAL_SUBSTRUCTURE_PRIVILEGE_GATE
STATUS = QUALIFIED_FORMAL
PHYSICAL_CLAIM = NONE
```

## Theorem

Let `L` be a family of closed substructures preserved by the automorphism group `Aut` of a fixed grammar/closure structure.

Let a selector predicate `C` be automorphism invariant:

\[
C(T)\Longleftrightarrow C(\alpha[T])
\]

for every `T in L` and `alpha in Aut`.

If exactly one `T* in L` satisfies `C`, then

\[
\alpha[T^*]=T^*
\]

for every `alpha in Aut`.

### Proof

If `C(T*)` holds, invariance gives `C(alpha[T*])`. Since `T*` is the unique selected member of `L`, `alpha[T*]=T*`. QED.

## Consequence

If the automorphism group exchanges two proper closed substructures `A` and `B`, then no automorphism-invariant selector can uniquely choose `A` while rejecting `B` unless some additional symmetry-breaking structure is supplied.

## Symmetric witness

Let

```text
P={a,b,c,d}
s(a)=b
s(b)=a
s(c)=d
s(d)=c
```

The closed sets are:

```text
empty
A={a,b}
B={c,d}
P
```

The automorphism

```text
a->c
b->d
c->a
d->b
```

exchanges `A` and `B`.

Hence no invariant intrinsic criterion can uniquely select one block rather than the other. The only closed substructures fixed by every automorphism are `empty` and `P`.

## Asymmetric limitation control

For

```text
P={a,b}
f(a)=b
f(b)=b
```

closed sets are `empty`, `{b}`, and `P`. The unique smallest nonempty closed substructure is `{b}`.

Therefore the theorem does not imply that intrinsic unique selection is impossible in every grammar. It constrains invariant selectors in the presence of grammar symmetry.

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = FIXED_CLOSURE_STRUCTURE
RULE_DEPENDENCIES = AUTOMORPHISM_INVARIANCE_OF_SELECTOR
LEMMA_DEPENDENCIES = UNIQUENESS
SEMANTIC_ASSUMPTIONS = NONE
PHYSICAL_ASSUMPTIONS = NONE
SOURCE_DEPENDENCIES = FROZEN_37_SOURCE_LANDSCAPE
METALANGUAGE_DEPENDENCIES = GROUP_ACTIONS; SETWISE_INVARIANCE; CLOSURE_SYSTEMS
```

## Result

```text
PGH-DER-0011 = QUALIFIED_FORMAL
UNIQUE_INTRINSIC_INVARIANT_SELECTION_REQUIRES_AUTOMORPHISM_FIXED_TARGET = YES
GENERAL_PHYSICAL_SELECTOR = NOT_DERIVED
```
