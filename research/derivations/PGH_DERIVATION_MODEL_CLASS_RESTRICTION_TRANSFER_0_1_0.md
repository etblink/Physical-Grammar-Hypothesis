# PGH-DER-0031 — Model-Class Restriction Transfer

## Status

```text
DERIVATION_ID = PGH-DER-0031
STATUS = QUALIFIED_FORMAL_SEMANTIC
PHYSICAL_CLAIM = CONDITIONAL_ONLY
```

## Setup

Let `W` be a formal model class and let every model `m in W` satisfy property `P`.

Let

\[
J:W\to E
\]

be a realization map into a candidate empirical model class such that:

1. `J` transports the whole formal class rather than selecting a favored proper subset;
2. `J` preserves the structure needed to state `P` under the declared representation mapping;
3. `J` adds no extra response equations or model-specific parameter values.

## Claim

Every realized model `J(m)` satisfies the transported property `J(P)`.

## Proof

For arbitrary `m in W`, the premise gives `m |= P`.

By structure preservation of `J`, the image satisfies the translated statement:

\[
J(m)\models J(P).
\]

Since `m` was arbitrary, the result holds for all realized models in `J(W)`.

No property of one selected model is used.

## PGH application

For

\[
W=W(PGH\text{-}GRAM\text{-}0008)
\]

and

\[
P=(A\perp C\mid B),
\]

`PGH-DER-0029` supplies the formal premise.

Under `PGH-OBJ-0035`, the transported candidate empirical restriction is

\[
\boxed{\mathcal A\perp\mathcal C\mid\mathcal B}.
\]

## Scope

This theorem does not establish that any actual physical variables instantiate the bridge.

It establishes only that a full-class semantic realization does not need to reinsert the conditional-independence law: once the grammar theorem is fixed, the restriction transfers to every valid realization.

```text
EMPIRICAL_TARGET = NONE
EMPIRICAL_VALIDATION = NONE
PHYSICAL_LAW_ESTABLISHED = NO
```
