# PGH-1 Common Free-Model Empirical Bridge Schema 0.1.0

## Status

```text
OBJECT_ID = PGH-OBJ-0023
OBJECT_CLASS = PHYSICAL_BRIDGE_FEASIBILITY_SCHEMA
PHYSICAL_STATUS = UNESTABLISHED
R2B_STATUS = UNSATISFIED
```

## Purpose

Define one common, minimal bridge probe for all frozen primitive grammar candidates without importing a response law through semantics or model choice.

## Anchor seed

From the law-free anchor take only two classes of reference tokens:

```text
C = CONTEXT_REFERENCE_TOKENS
R = RECORD_REFERENCE_TOKENS
```

Introduce distinct atomic object generators:

\[
X_c\quad(c\in C),
\qquad
Y_r\quad(r\in R).
\]

No cross-type arrow, response relation, probability, amplitude, or empirical partition is primitive.

## Candidate-specific free structures

For each frozen grammar `G_i`:

\[
F_i=\operatorname{Free}_{G_i}(S_{ref}).
\]

The free structure is a controlled model used to expose what follows from doctrine plus anchor labels alone.

It does not replace the candidate grammar's model-class definition.

## Trial relation

Define

\[
B_i(c,r)\iff \operatorname{Hom}_{F_i}(X_c,Y_r)\neq\varnothing.
\]

This relation is formally well-defined.

Its interpretation as empirical response possibility is **not** established.

## Layer separation

```text
GRAMMAR_LAYER = EXISTENCE_OF_STRUCTURAL_MORPHISM
BRIDGE_LAYER = PROPOSED_MEANING_OF_MORPHISM_AS_RESPONSE_POSSIBILITY
EMPIRICAL_LAYER = WHICH_RESPONSES_OCCUR_OR_WITH_WHAT_PROBABILITY
```

A result at one layer may not be silently promoted to the next.

## Free-model result

For the current candidate family:

```text
PGH-GRAM-0003 -> B_i = EMPTY
PGH-GRAM-0004 -> B_i = EMPTY
PGH-GRAM-0005 -> B_i = EMPTY
PGH-GRAM-0006 -> B_i = EMPTY
PGH-GRAM-0007 -> B_i = EMPTY
```

The empty result means only that current doctrine plus anchor labels do not generate cross-type atomic morphisms under this anti-smuggling probe.

## Model-selection warning

An arbitrary model/anchor interpretation may make the same hom-existence relation empty or nonempty without changing the grammar doctrine.

Therefore a later bridge must separately justify model/interpretation restrictions rather than selecting a convenient model by known empirical fit.

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = [LAW_FREE_A_REF_LABEL_STRUCTURE, PGH-GRAM-0003..0007]
SEMANTIC_ASSUMPTIONS = [TRIAL_ONLY: MORPHISM_EXISTENCE_AS_RESPONSE_CANDIDATE]
PHYSICAL_ASSUMPTIONS = NONE_ESTABLISHED
RESPONSE_LAW_INPUT = NONE
```
