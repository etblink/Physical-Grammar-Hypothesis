# PGH-1 Bridge-Enriched Model-Class Schema 0.1.0

## Identity

```text
OBJECT_ID = PGH-OBJ-0030
OBJECT_CLASS = MODEL_CLASS_LAW_EXHAUSTION_SCHEMA
STATUS = PROVISIONAL_R2B_TEST_SCHEMA
TYPED_ANCHOR = PGH-OBJ-0025
BRIDGE_CANDIDATE = PGH-OBJ-0028
SEMANTIC_FIREWALL = PGH-OBJ-0029
CANDIDATE_GRAMMARS = PGH-GRAM-0006; PGH-GRAM-0007
```

## Bridge-enriched theory

For each context `c`, the theory contains:

- context object `X_c`;
- record objects `Y_r` for `r in R_c`;
- coproduct `O_c = coproduct_r Y_r`;
- one primitive bridge generator `n_c:X_c -> O_c`;
- the minimal law-free process-role semantics qualified by `PGH-OBJ-0029`.

No equation constraining the interpretation of `n_c` is included.

## Model-class consequence

A response property `P` counts as grammar-derived only when it holds in every model of the fixed bridge-enriched theory within a declared semantic class.

```text
ONE_MODEL_HAS_P = INSUFFICIENT
MODEL_SELECTED_BY_EMPIRICAL_FIT = NO_CREDIT
ALL_MODELS_HAVE_P = CANDIDATE_THEORY_CONSEQUENCE
```

## Universal-realizability criterion

For a response class `RSP`, if

\[
\forall h\in RSP\;\exists M_h:\quad M_h\models T
\]

and the bridge interpretation in `M_h` realizes exactly `h`, then the theory `T` does not select a proper nontrivial subset of `RSP`.

## Tested semantic classes

```text
SET_DETERMINISTIC = TESTED_FOR_PGH_GRAM_0006_AND_0007
RELATIONAL = TESTED_AS_COCARTESIAN_CONTROL_FOR_PGH_GRAM_0006
FINITE_STOCHASTIC = TESTED_AS_COCARTESIAN_CONTROL_FOR_PGH_GRAM_0006
```

These are formal controls, not claims that any class is the correct physical semantics.

## Current result

`PGH-DER-0028` establishes universal realizability of the tested response classes.

Therefore:

```text
CURRENT_BRIDGE_ENRICHED_GRAMMAR_HAS_SEMANTIC_CONTACT = YES
CURRENT_BRIDGE_ENRICHED_GRAMMAR_HAS_RESPONSE_LAW_EXHAUSTION = NO
```

## Next admissible strengthening

Any later constraint on `n_c` must be preregistered and must pass the no-smuggling controls.

Potential structural families may be tested, but none is selected here.

## Nonclaims

```text
ALL_MATHEMATICALLY_REALIZABLE_RESPONSES_ARE_PHYSICAL = NO
SET_REL_OR_STOCH_IS_FUNDAMENTAL = NO
BICARTESIAN_IS_BETTER_THAN_COCARTESIAN = NO
R2B = UNSATISFIED
```
