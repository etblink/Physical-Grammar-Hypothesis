# PGH-FAIL-0009 — Arbitrary or Response-Sensitive Interface Closure 0.1.0

## Identity

```text
DERIVATION_ID = PGH-FAIL-0009
OPERATION_ID = PGH0_GRAMMAR_GENERATED_EMPIRICAL_INTERFACE_CLOSURE_CHALLENGE
STATUS = FAILED_PRESERVED
FAILURE_CLASS = UNIVERSAL_ENCODING_AND_PHYSICS_SMUGGLING
```

## Failed route A — arbitrary closure operator

An arbitrary extensive, monotone, idempotent closure operator does not explain the empirical interface.

For any target `T` satisfying `C0 subseteq T subseteq P`, define

\[
Cl_T(S)=S\cup T.
\]

Then `Cl_T` is a valid closure operator and

\[
Cl_T(C_0)=T.
\]

Thus any desired target interface can be entered directly into the closure map.

```text
ARBITRARY_CLOSURE_OPERATOR = UNIVERSAL_TARGET_ENCODER
NONARBITRARY_PHYSICAL_SELECTION = NO
```

## Failed route B — freely selected constructor family

Replacing an arbitrary closure operator by a least generated closure does not fix the problem if the constructor family itself is free.

For any target `T` containing a nonempty seed `C0`, choose `c* in C0` and introduce one partial constructor for every `t in T minus C0`:

\[
\gamma_t(c^*)=t.
\]

No constructor produces values outside `T`.

Then the least constructor closure is exactly `T`.

Nullary constructors make the encoding still more direct.

```text
LEAST_CLOSURE = CANONICAL_RELATIVE_TO_GAMMA
FREE_GAMMA = STILL_UNIVERSALLY_EXPRESSIVE
```

Therefore least closure by itself is not a non-arbitrariness principle.

## Failed route C — response-sensitive generation

The following kinds of rules are not law-free empirical-interface closure:

```text
add context c iff c distinguishes target states
add context c iff evaluator e(c,x) returns record r
add context c iff a response is declared physically possible
include/weight c according to response probability p(r|c,x)
```

They inspect the empirical regularity or possibility relation that the grammar is supposed to generate.

They therefore move substantive physics into the interface-generation rule.

```text
RESPONSE_SENSITIVE_CLOSURE = PHYSICS_SMUGGLED
```

## What survives

This failure does not invalidate least closure itself.

It motivates the narrower qualified architecture in which:

```text
Gamma_G = fixed response-independent extraction from grammar formation structure
```

and the physical privilege of `G`, the extraction rule, and the empirical seed remains explicitly unresolved.

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = LAW_FREE_EMPIRICAL_SEED
RULE_DEPENDENCIES = CLOSURE_OR_CONSTRUCTOR_SELECTION
LEMMA_DEPENDENCIES = NONE
SEMANTIC_ASSUMPTIONS = NONE_FOR_UNIVERSAL_ENCODING_CONTROL
PHYSICAL_ASSUMPTIONS = RESPONSE_SENSITIVE_ROUTES_EXPLICITLY_IMPORT_TARGET_PHYSICS
SOURCE_DEPENDENCIES = FROZEN_37_SOURCE_LANDSCAPE
```

## Result

```text
PGH-FAIL-0009 = FAILED_PRESERVED
ARBITRARY_CLOSURE_AS_PHYSICAL_SELECTOR = REJECTED
FREE_CONSTRUCTOR_FAMILY_AS_PHYSICAL_SELECTOR = REJECTED
RESPONSE_SENSITIVE_INTERFACE_GENERATION = REJECTED
```
