# PGH-DER-0024 — External Typing Structural Inertness

## Status

```text
DERIVATION_ID = PGH-DER-0024
STATUS = QUALIFIED_FORMAL
PHYSICAL_CLAIM = NONE
```

## Claim

Typed semantic metadata that is not represented anywhere in a grammar's formal signature, generators, equations, typing judgments, or inference rules cannot change that grammar's generated formal consequences merely by being externally associated with the same labels.

## Setup

Let `G` be a fixed candidate grammar and `S_ref` the discrete anchor-label seed used in `PGH-OBJ-0023`.

Let `T` be a typed semantic relation carried only as external metadata.

Write

\[
Free_G(S_{ref})
\]

for the free grammar construction.

If the formal input to `Free_G` is unchanged when `T` is mentioned externally, then

\[
Free_G(S_{ref};T_{external})=Free_G(S_{ref})
\]

up to the same canonical identification used for the free construction.

## Reason

A formal derivation is determined by the candidate grammar's declared formal data.

External metadata absent from those data supplies no production, morphism generator, equation, type judgment, rewrite, relation, or universal-property input from which a new formal consequence could be derived.

Thus a change in analyst interpretation with no change to the formal presentation is not a change in grammar derivability.

## Consequence for the typed anchor

The response-underdetermining relation `T` of `PGH-OBJ-0025` does not, while left external, repair the empty atomic cross-type hom relation found in `PGH-DER-0021`.

```text
TYPING_PRESENT_AS_EXTERNAL_METADATA = YES
GRAMMAR_SIGNATURE_CHANGED = NO
NEW_CROSS_TYPE_MORPHISMS_GENERATED = NO
```

## Scope

This is a bookkeeping/formal-dependence result. It does not say that semantic metadata is scientifically irrelevant.

It says only that semantic metadata must be internalized through explicit formal structure before it can alter grammar derivability.

That internalization then becomes an auditable assumption.