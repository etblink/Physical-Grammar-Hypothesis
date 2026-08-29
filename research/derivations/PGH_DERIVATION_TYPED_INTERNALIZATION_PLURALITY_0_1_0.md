# PGH-DER-0025 — Typed Internalization Plurality

## Status

```text
DERIVATION_ID = PGH-DER-0025
STATUS = QUALIFIED_FORMAL
PHYSICAL_CLAIM = NONE
```

## Setup

Work in the bicartesian primitive grammar candidate `PGH-GRAM-0007` with one context generator `X` and two typed record generators `Y0,Y1` corresponding to the same fixed typed fiber

\[
R_c=\{r_0,r_1\}.
\]

Compare two internalizations of that same typing.

## Product-output packaging

Add one primitive morphism

\[
m:X\to Y0\times Y1.
\]

Product projections give

\[
\pi_0m:X\to Y0,
\qquad
\pi_1m:X\to Y1.
\]

But this is not a compression result. By the product universal property,

\[
\operatorname{Hom}(X,Y0\times Y1)
\cong
\operatorname{Hom}(X,Y0)\times\operatorname{Hom}(X,Y1).
\]

Hence specifying `m` is equivalent formal data to specifying the ordered pair of component arrows.

```text
PRODUCT_OUTPUT_GENERATOR = COMPONENT_ARROW_PAIR_PACKAGED_BY_UNIVERSAL_PROPERTY
DERIVATIONAL_CREDIT_FOR_COMPONENT_ARROWS = NO
```

## Coproduct-output internalization

Instead add one primitive morphism

\[
n:X\to Y0+Y1.
\]

Bicartesian structure does not force either

\[
X\to Y0
\]

or

\[
X\to Y1.
\]

### Separation for `X -> Y0`

Interpret in `Set` by

\[
X\mapsto1,
\quad
Y0\mapsto\varnothing,
\quad
Y1\mapsto1.
\]

Then

\[
Y0+Y1\cong1,
\]

so `n` can be interpreted as the identity `1->1`, while no function

\[
1\to\varnothing
\]

exists. Therefore no formal term `X->Y0` is forced.

### Separation for `X -> Y1`

Swap the assignments of `Y0` and `Y1`. The same argument shows no formal `X->Y1` is forced.

## Plurality conclusion

The typed semantic fiber and the bicartesian doctrine are identical, yet the bridge-level consequences differ depending on the internalization:

```text
TYPED_INTERFACE = SAME
GRAMMAR_DOCTRINE = SAME
PRODUCT_PACKAGING = EQUIVALENT_TO_COMPONENT_ARROW_PAIR
COPRODUCT_GENERIC_PROCESS = DOES_NOT_FORCE_COMPONENT_ARROWS
INTERNALIZATION_CHOICE = SUBSTANTIVE_FORMAL_DATA
```

Thus the typed interface plus doctrine do not determine one anchor-to-grammar interaction.

## Why this is still useful despite the product equivalence

The result does not rely on claiming product packaging is compressed.

Its value is the contrast: one lawful embedding of the typed fiber contains exactly the component-arrow information under the product universal property, whereas another lawful embedding supplies only a generic aggregate-output process and leaves component arrows underdetermined.

Therefore a later bridge must account for which kind of internalization is being assumed.

## Scope

No physical response interpretation is assigned to any morphism in this derivation.

The theorem establishes formal internalization plurality only.