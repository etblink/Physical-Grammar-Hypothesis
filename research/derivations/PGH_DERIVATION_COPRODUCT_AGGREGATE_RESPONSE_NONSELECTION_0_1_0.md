# PGH-DER-0026 — Coproduct Aggregate Response Nonselection

## Status

```text
DERIVATION_ID = PGH-DER-0026
STATUS = QUALIFIED_FORMAL
PHYSICAL_CLAIM = NONE
```

## Setup

Let `X` be a context object and let `Y_1,...,Y_n` be distinct atomic record objects with `n>=2` in a free category with finite coproducts.

Add one primitive generic process

\[
n:X\to Y_1+\cdots+Y_n.
\]

No component arrow `X->Y_i` is added.

## Claim 1 — no component arrow is forced

For each fixed component `i`, there exists a finite-coproduct model in `Set` interpreting the presentation while admitting no function from the interpretation of `X` to the interpretation of `Y_i`.

### Proof

Interpret

\[
X\mapsto1,
\quad
Y_i\mapsto\varnothing.
\]

Choose one other component `j != i` and interpret

\[
Y_j\mapsto1.
\]

Interpret all remaining `Y_k` arbitrarily, for example as the empty set.

Then

\[
\coprod_kY_k\cong1,
\]

so the generator `n` can be interpreted as the identity map

\[
1\to1.
\]

But there is no function

\[
1\to\varnothing.
\]

Therefore a formal arrow `X->Y_i` cannot be forced by the free coproduct structure plus `n`; otherwise every model would interpret such an arrow. QED.

Because `i` was arbitrary, no individual component arrow is forced.

## Claim 2 — not information-equivalent to the component-arrow tuple

For products one has

\[
Hom(X,\prod_iY_i)\cong\prod_iHom(X,Y_i).
\]

No analogous equivalence holds for maps **into** a coproduct in general.

The `Set` separation above gives a direct cardinality witness. For `n=2`, take

\[
X=1,\quad Y_0=\varnothing,\quad Y_1=1.
\]

Then

\[
Hom(1,Y_0+Y_1)\cong Hom(1,1)
\]

is nonempty, whereas

\[
Hom(1,Y_0)\times Hom(1,Y_1)
\]

is empty.

Thus a generic map into a coproduct is not equivalent data to the tuple of component maps.

## Claim 3 — response underdetermination remains

When the corresponding typed fiber contains at least two labels, `PGH-DER-0023` supplies at least two deterministic response sections of the same typed interface.

The generic process `n` does not select a component arrow, so it supplies no formal rule choosing one of those response sections.

Hence at the formal bridge-candidate scope:

```text
GENERIC_CROSS_TYPE_PROCESS = YES
COMPONENT_RESPONSE_SELECTION = NO
MULTIPLE_RESPONSE_LAWS_REMAIN_COMPATIBLE = YES_AT_FORMAL_SEMANTIC_SCOPE
```

## Scope

This theorem does not say that coproducts represent physical alternatives or that `n` is a physical process.

It proves only that this primitive bridge candidate is formally weaker than a component response-edge tuple and remains response-underdetermining.