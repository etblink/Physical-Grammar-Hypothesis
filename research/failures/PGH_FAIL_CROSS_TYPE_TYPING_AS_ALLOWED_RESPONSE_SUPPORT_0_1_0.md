# PGH-FAIL-0025 — Cross-Type Typing as Allowed Response Support

## Status

```text
FAILURE_ID = PGH-FAIL-0025
STATUS = FAILED_PRESERVED
PHYSICAL_CLAIM = NONE
```

## Failed move

Attempt:

> Treat a context-record typing relation `T` as primitive semantic structure while interpreting `T(c,r)` to mean that `r` is a physically possible/nonzero-support response to `c`, then claim downstream response exclusion as grammar-derived.

This fails.

Once membership means physical possibility or nonzero support, `T` is already an allowed-response relation and carries substantive modal/physical selection.

## Empirical-reconstruction failure

If the fibers are chosen by

```text
R_c = RESPONSES_OBSERVED_OR_ALREADY_PREDICTED_POSSIBLE_FOR_CONTEXT_c
```

then the typing structure has been reconstructed from the target response content.

Relabeling it as an output alphabet does not remove that information.

## Singleton-response encoding

Suppose each fiber is

\[
R_c=\{f(c)\}
\]

for a target deterministic response map `f`.

Then `T` is exactly the graph of `f`.

```text
TYPE_DECLARATION = RESPONSE_FUNCTION_IN_DISGUISE
LAW_FREE_CRITERION = FAIL
```

## Arbitrary-fiber caution

Even when `T` passes response underdetermination, arbitrary fiber choice can carry semantic or physical structure.

Therefore:

```text
MULTIPLE_RESPONSE_LAWS_ON_SAME_T = NECESSARY_FOR_LAW_FREE_STATUS
MULTIPLE_RESPONSE_LAWS_ON_SAME_T = NOT_PHYSICAL_PRIVILEGE_PROOF
```

The reason for the chosen typing must remain explicit and separately auditable.

## What remains valid

A typing relation may be admitted as a provisional law-free semantic interface if its meaning is only record-label/type compatibility and the same `T` remains compatible with multiple incompatible response laws.

That surviving possibility is represented by `PGH-OBJ-0025` and `PGH-DER-0023`.

## Failure classification

```text
FAILURE_CLASS = SEMANTIC_SMUGGLING; TARGET_RESPONSE_REENCODING
HIDDEN_IMPORT = PHYSICAL_ALLOWED_RESPONSE_SUPPORT_OR_TARGET_RESPONSE_FUNCTION
WHAT_REMAINS_VALID = RESPONSE_UNDERDETERMINING_TYPED_INTERFACE_AT_FORMAL_SEMANTIC_SCOPE
```