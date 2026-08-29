# PGH-FAIL-0023 — Unrestricted Model Selection as Semantic Smuggling

## Status

```text
FAILURE_ID = PGH-FAIL-0023
STATUS = FAILED_PRESERVED
FAILURE_CLASS = SEMANTIC_MAP_SMUGGLING / UNDERDETERMINED
```

## Failed move

> Fix a broad candidate grammar doctrine, then choose whichever model and anchor interpretation yields the desired context-to-record relation, and credit that relation to the grammar.

## Countercontrol

The grammar doctrine can remain fixed while model/anchor interpretation changes the trial hom-existence relation.

`Set` supplies a simple separation.

### Interpretation A

\[
X_c\mapsto 1,
\qquad
Y_r\mapsto\varnothing.
\]

Then

\[
\operatorname{Hom}(1,\varnothing)=\varnothing.
\]

### Interpretation B

\[
X_c\mapsto\varnothing,
\qquad
Y_r\mapsto 1.
\]

Then exactly one function exists from the empty set to the singleton.

Appropriate product, coproduct, or monoidal structure on `Set` makes it a lawful model of each relevant doctrine class.

Thus:

```text
GRAMMAR_DOCTRINE = FIXED
ANCHOR_INTERPRETATION = VARIABLE
TRIAL_RESPONSE_RELATION = VARIABLE
```

## Consequence

A response relation obtained by selecting the model/interpretation after seeing the desired empirical behavior cannot receive grammar-derived explanatory credit.

The model restriction or semantic map must itself be independently justified, preregistered, or counted as additional substantive structure.

## What remains allowed

Later empirical comparison may legitimately test already-preregistered model/interpretation families.

What fails is retroactive selection followed by the claim that the grammar alone generated the result.

## Nonclaims

```text
ALL_MODEL_SELECTION_IS_ILLEGITIMATE = NO
SEMANTICS_CAN_NEVER_CONNECT_GRAMMAR_TO_PHYSICS = NO
MORPHISM_EXISTENCE_IS_PHYSICAL_RESPONSE = NOT_ESTABLISHED
R2B_IS_SATISFIED = NO
```
