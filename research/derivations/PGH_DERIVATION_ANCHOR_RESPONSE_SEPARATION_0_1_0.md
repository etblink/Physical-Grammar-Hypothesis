# PGH-DER-0007 — Anchor/Response Separation 0.1.0

## Identity

```text
DERIVATION_ID = PGH-DER-0007
OPERATION_ID = PGH0_MINIMAL_PHYSICAL_SEMANTIC_ANCHOR_CHALLENGE
STATUS = QUALIFIED_FORMAL
PHYSICAL_CLAIM = NONE
NOVELTY_CLAIM = NONE
```

## Claim

A context/record semantic anchor can be held fixed while multiple candidate evaluators generate different record-response behavior.

Therefore the anchor schema does not logically encode the response law.

## Setup

Let

\[
A=(C,R,\rho)
\]

be a context/record anchor and let `e` be a candidate evaluator. Record profiles are

\[
O_{A,e}(x)(c)=\rho(e(c,x)).
\]

The anchor consists only of interface contexts, record labels, and the terminal-to-record interpretation; `e` is external to the anchor.

## Finite witness

Choose:

```text
X = {x,y}
C = {c}
T = {u,v}
R = {0,1}
rho(u) = 0
rho(v) = 1
```

Define two evaluators using the exact same anchor.

### Evaluator 1

```text
e_same(c,x) = u
e_same(c,y) = u
```

Then:

```text
O_(A,e_same)(x) = 0
O_(A,e_same)(y) = 0
```

so `x` and `y` are anchor-relative indistinguishable.

### Evaluator 2

```text
e_split(c,x) = u
e_split(c,y) = v
```

Then:

```text
O_(A,e_split)(x) = 0
O_(A,e_split)(y) = 1
```

so `x` and `y` are anchor-relative distinguishable.

## Consequence

The same semantic interface permits at least two different response laws.

Thus:

```text
ANCHOR_DETERMINES_RESPONSE_LAW = NO
ANCHOR_CAN_SUPPORT_NONTRIVIAL_DISTINGUISHABILITY = YES_WHEN_COMBINED_WITH_EVALUATOR
```

This establishes a formal separation between minimal interface semantics and grammar-generated response.

## General statement

Whenever a fixed anchor admits two evaluators `e1,e2` such that

\[
\rho(e_1(c,x))\neq\rho(e_2(c,x))
\]

for some anchored context/state pair, the response profile is not a function of the anchor alone.

The finite witness proves existence of such an architecture.

## What is not established

```text
ANCHOR_IS_PHYSICALLY_CORRECT = NO
ANCHOR_IS_UNIQUE = NO
ANCHOR_IS_REPRESENTATION_INDEPENDENT = NO
RECORD_EQUIVALENCE_IS_FULL_PHYSICAL_EQUIVALENCE = NO
R1_SOLVED = NO
PHYSICAL_LAW_DERIVED = NO
```

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = CONTEXT_SET; RECORD_SET; TERMINAL_RECORD_MAP; CANDIDATE_EVALUATOR
RULE_DEPENDENCIES = RECORD_PROFILE_COMPOSITION
LEMMA_DEPENDENCIES = NONE
SEMANTIC_ASSUMPTIONS = DECLARED_CONTEXTS_ARE_INTERFACES; DECLARED_TERMINALS_HAVE_RECORD_INTERPRETATION
PHYSICAL_ASSUMPTIONS = NO_DYNAMICS_OR_RESPONSE_LAW
SOURCE_DEPENDENCIES = FROZEN_37_SOURCE_LANDSCAPE_AS_CONTEXT_ONLY
```
