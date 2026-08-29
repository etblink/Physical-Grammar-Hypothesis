# PGH-DER-0027 — Coproduct Tag Pushforward Response Extraction 0.1.0

## Status

```text
DERIVATION_ID = PGH-DER-0027
STATUS = QUALIFIED_FORMAL
CLAIM_SCOPE = SEMANTIC_INFORMATION_ACCOUNTING_FOR_COPRODUCT_BRIDGE_MODELS
PHYSICAL_CLAIM = NONE
```

## Setup

Let

\[
O=\coprod_{r\in R}Y_r
\]

with canonical tag map

\[
q:O\to R
\]

that sends each element of summand `Y_r` to its record label `r`.

Let the abstract bridge contain one generator

\[
n:X\to O.
\]

The derivation concerns concrete interpretations of `n`, not the free syntactic generator by itself.

## Deterministic case

For any Set interpretation

\[
\hat n:X\to O,
\]

define

\[
f=q\circ\hat n:X\to R.
\]

Thus every concrete deterministic interpretation of the bridge carries a definite record-label map after forgetting within-summand payload.

The abstract generator does not determine which `f` occurs because distinct lawful interpretations of the same generator may yield different `f`.

## Relational case

For any relation

\[
\hat n\subseteq X\times O,
\]

define

\[
K(x,r)\iff \exists y\in Y_r:\;x\;\hat n\;y.
\]

Then `K` is the record-label support obtained by pushing the relation through the summand tags.

If relational membership is interpreted as physical possibility, `K` is response-support data carried by the concrete relation.

## Finite stochastic case

For any finite stochastic kernel

\[
\hat n(y\mid x)
\]

on `O`, define

\[
p(r\mid x)=\sum_{y\in Y_r}\hat n(y\mid x).
\]

Then `p` is the record-label marginal distribution induced by the kernel.

If kernel weights are interpreted as physical response probabilities, the response distribution is carried by the concrete interpretation.

## Fixed-syntax model-plurality witness

Let

```text
X = {*}
Y0 = {0}
Y1 = {1}
```

and keep the same abstract bridge generator

\[
n:X\to Y_0+Y_1.
\]

Interpret it once by

\[
\hat n_0(*)=\iota_0(0)
\]

and once by

\[
\hat n_1(*)=\iota_1(1).
\]

The induced label maps differ.

Therefore:

```text
ABSTRACT_BRIDGE_SYMBOL_DETERMINES_CONCRETE_RESPONSE = NO
MODEL_INTERPRETATION_CAN_CARRY_RESPONSE_SELECTION = YES
```

## Result

```text
PGH-DER-0027 = COPRODUCT_TAG_PUSHFORWARD_RESPONSE_EXTRACTION
DETERMINISTIC_RESPONSE_EXTRACTION = YES_CONDITIONALLY_ON_RESPONSE_READING
RELATIONAL_SUPPORT_EXTRACTION = YES_CONDITIONALLY_ON_RESPONSE_READING
STOCHASTIC_DISTRIBUTION_EXTRACTION = YES_CONDITIONALLY_ON_RESPONSE_READING
ABSTRACT_GRAMMAR_DERIVES_ANY_ONE_OF_THESE = NO_AT_CURRENT_SCOPE
PHYSICAL_CLAIM = NONE
```

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = PGH-OBJ-0025; PGH-OBJ-0028
RULE_DEPENDENCIES = COPRODUCT_TAGGING; ORDINARY_FUNCTION_RELATION_KERNEL_PUSHFORWARD
LEMMA_DEPENDENCIES = NONE_BEYOND_ELEMENTARY_COMPOSITION_AND_MARGINALIZATION
SEMANTIC_ASSUMPTIONS = ONLY_FOR_CONDITIONAL_RESPONSE_READINGS
PHYSICAL_ASSUMPTIONS = NONE
SOURCE_DEPENDENCIES = NONE_NEW
```
