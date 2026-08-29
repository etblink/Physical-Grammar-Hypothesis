# PGH-FAIL-0003 — Unprivileged Simplicity Selection 0.1.0

## Identity

```text
DERIVATION_ID = PGH-FAIL-0003
OPERATION_ID = PGH0_NONARBITRARY_FORMATION_CONSTRAINT_CHALLENGE
STATUS = FAILED
CLAIMED_RESULT = GENERATIVE_COMPRESSION_ALONE_SELECTS_A_NONARBITRARY_FORMATION_LAW
FAILURE_CLASS = REPRESENTATION_DEPENDENT; UNDERDETERMINED
```

## Proposed idea

PGH requires a successful grammar to exhibit generative compression. It is tempting to turn that methodological burden into a selection law:

> Prefer the simplest formation relation or grammar.

At current PGH scope this does not yield a representation-independent selector.

## Recoding argument

Let `F` be any finite formation relation.

One can define a formal description language `L_F` containing a primitive token whose stipulated denotation is exactly `F`.

In `L_F`, the description of `F` can be one token long.

A different language can force the same relation to be described tuple by tuple.

Therefore raw description length depends on the representational language unless the project first justifies a privileged or invariant complexity framework.

## Why generic “simplicity” is insufficient

Even after a complexity convention is fixed:

- multiple inequivalent relations can have equal complexity;
- the choice of primitives changes description length;
- finite-description additive constants can change rankings among small candidates;
- a simplicity rule does not by itself explain why the chosen complexity notion is physically or grammatically privileged.

This does not invalidate generative compression as a burden on successful PGH theories.

It blocks using an **unprivileged** complexity measure as the missing non-arbitrary law.

## Result

```text
GENERATIVE_COMPRESSION_AS_SUCCESS_CRITERION = RETAINED
RAW_DESCRIPTION_LENGTH_AS_INTRINSIC_SELECTOR = REJECTED
PRIVILEGED_COMPLEXITY_MEASURE = NONE
NONARBITRARY_FORMATION_CONSTRAINT_DERIVED = NO
```

## What remains valid

A later source-bound or formal operation may test complexity notions that possess stronger invariance properties.

This failure does not prejudge those possibilities.

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = FORMATION_RELATION
RULE_DEPENDENCIES = SIMPLICITY_PREFERENCE
LEMMA_DEPENDENCIES = RECODING_ARGUMENT
SEMANTIC_ASSUMPTIONS = DESCRIPTION_LENGTH_DEPENDS_ON_A_DESCRIPTION_LANGUAGE
PHYSICAL_ASSUMPTIONS = NONE
SOURCE_DEPENDENCIES = NONE
METALANGUAGE_DEPENDENCIES = FINITE_DESCRIPTIONS; FORMAL_LANGUAGES; ENCODINGS
```

## Result status

```text
PGH-FAIL-0003 = FAILED_PRESERVED
UNPRIVILEGED_SIMPLICITY_SELECTION = REJECTED
SUPERSESSION_STATUS = NOT_SUPERSEDED
```
