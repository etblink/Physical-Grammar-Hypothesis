# PGH-DER-0017 — Free Monoidal Arity and Order Nonselection

## Status

```text
DERIVATION_ID = PGH-DER-0017
STATUS = QUALIFIED_FORMAL
PHYSICAL_CLAIM = NONE
```

## Claim

Bare strict monoidal composition does not by itself generate copy-like, discard-like, or exchange-like structural morphisms.

## Construction

Take the free strict monoidal category on two object-generators `A,B` and no nonidentity morphism generators.

Its objects are tensor words in `A,B`. Its only morphisms are identity morphisms on identical words.

Hence:

\[
\operatorname{Hom}(A,A\otimes A)=\varnothing,
\]

\[
\operatorname{Hom}(A,I)=\varnothing,
\]

and

\[
\operatorname{Hom}(A\otimes B,B\otimes A)=\varnothing.
\]

The last hom-set is empty because the two tensor words are distinct in the free nonsymmetric monoidal category.

## Symmetric control

In the free symmetric monoidal category on the same colored generators, symmetry supplies

\[
\sigma_{A,B}:A\otimes B\to B\otimes A.
\]

But coherence maps preserve wire number and color multiplicity. Therefore:

\[
\operatorname{Hom}(A,A\otimes A)=\varnothing,
\qquad
\operatorname{Hom}(A,I)=\varnothing.
\]

Thus symmetry adds exchange without generating copy or discard.

## Consequence

```text
COMPOSITION_ALONE =>/=> COPY
COMPOSITION_ALONE =>/=> DISCARD
COMPOSITION_ALONE =>/=> EXCHANGE
SYMMETRY + COMPOSITION => EXCHANGE
SYMMETRY + COMPOSITION =>/=> COPY_OR_DISCARD
```

Structural permissions therefore carry information not contained in bare monoidal composition.

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = [FREE_STRICT_MONOIDAL_COMPOSITION]
RULE_DEPENDENCIES = NONE_FOR_T0; [SYMMETRY]_FOR_CONTROL
SEMANTIC_ASSUMPTIONS = NONE
PHYSICAL_ASSUMPTIONS = NONE
```
