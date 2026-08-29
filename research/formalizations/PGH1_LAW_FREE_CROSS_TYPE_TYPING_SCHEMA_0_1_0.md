# PGH-1 Law-Free Cross-Type Typing Schema 0.1.0

## Status

```text
OBJECT_ID = PGH-OBJ-0025
OBJECT_CLASS = SEMANTIC_TYPING_SCHEMA
STATUS = PROVISIONAL_FORMAL_SCHEMA
PHYSICAL_STATUS = UNESTABLISHED
R2B = UNSATISFIED
```

## Definition

Let `C` be a finite nonempty set of empirical context/interface labels and `R` a finite set of record labels.

A cross-type typing relation is

\[
T\subseteq C\times R.
\]

For each context `c`, define its declared record-label fiber

\[
R_c=\{r:(c,r)\in T\}.
\]

The semantic reading is:

> `r` is a well-typed record label in the declared output alphabet/interface for context `c`.

This is intentionally weaker than:

> `r` is a physically possible response to context `c`.

## Law-free criterion

A typing relation is **response-underdetermining** at this scope if it is held fixed while at least two incompatible response models remain admissible.

For deterministic response models this means there exist distinct sections

\[
f_1,f_2:C\to R
\]

such that

\[
(c,f_i(c))\in T
\]

for every `c`.

For probabilistic models, distinct distributions over the same fibers must remain possible.

Response underdetermination is necessary for this typing to count as law-free semantic structure under anchored PGH. It is not sufficient to establish physical privilege or completeness.

## Representation covariance

Under bijections

\[
\sigma:C\to C',\qquad\tau:R\to R',
\]

the typing transports as

\[
T'=(\sigma\times\tau)[T].
\]

A deterministic section transports by

\[
f'=\tau\circ f\circ\sigma^{-1}.
\]

Thus response multiplicity is representation-covariant.

No full permutation automorphy of one fixed typed relation is required.

## What the schema permits

```text
CONTEXT_SPECIFIC_RECORD_ALPHABET = YES
MULTIPLE_RESPONSE_LAWS_ON_SAME_TYPING = REQUIRED
PROBE_RECORD_REFERENCE = YES_AT_SEMANTIC_SCOPE
```

## What the schema forbids as primitive meaning

```text
T_MEMBERSHIP_MEANS_PHYSICAL_POSSIBILITY = NO
T_MEMBERSHIP_MEANS_NONZERO_PROBABILITY = NO
T_MEMBERSHIP_MEANS_OBSERVED_RESPONSE = NO
TARGET_RESPONSE_FUNCTION = NO
PROBABILITY_OR_AMPLITUDE_RULE = NO
```

## Singleton caution

If every fiber is a singleton and deterministic response is the target model class, `T` already determines a unique response function and fails the minimum response-underdetermination test.

A singleton typing cannot be rescued merely by renaming the determined response as a type rule.

## Physical ceiling

```text
LAW_FREE_TYPED_INTERFACE_FORMALLY_FEASIBLE = YES
WHY_THIS_TYPING_IS_PHYSICALLY_PRIVILEGED = UNESTABLISHED
TYPING_COMPLETENESS = UNESTABLISHED
GRAMMAR_GENERATED_RESPONSE = NO
PHYSICAL_BRIDGE = NONE
R2B = UNSATISFIED
```