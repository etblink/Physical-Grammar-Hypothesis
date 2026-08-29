# PGH-FAIL-0006 — Semantic Anchor Extremes 0.1.0

## Identity

```text
DERIVATION_ID = PGH-FAIL-0006
OPERATION_ID = PGH0_MINIMAL_PHYSICAL_SEMANTIC_ANCHOR_CHALLENGE
STATUS = FAILED_PRESERVED
FAILURE_CLASS = TOO_WEAK_OR_SEMANTIC_SMUGGLING
NOVELTY_CLAIM = NONE
```

## Purpose

This artifact preserves the anchor forms that fail on opposite sides of the semantic Goldilocks problem.

## Failure A — Primitive physical equivalence

Stipulating the target relation directly as semantics fails because the anchor is defined by the result it is meant to explain.

```text
FAILURE = CIRCULAR_TARGET_STIPULATION
```

## Failure B — Vocabulary only

Declaring symbols to mean “record,” “observation,” or “probe” without specifying any comparison context is too weak to constrain physical significance.

```text
FAILURE = NONDISCRIMINATING_SEMANTICS
```

## Failure C — Full response table

If semantics specifies the record associated with every probe/state pair, it contains the response behavior that the candidate grammar was supposed to generate.

```text
FAILURE = RESPONSE_LAW_SMUGGLED_INTO_SEMANTICS
```

## Failure D — Complete task-possibility set

If semantics specifies the complete possible/impossible transformation set, it supplies substantive physical selection before the grammar is tested.

```text
FAILURE = POSSIBILITY_LAW_SMUGGLED_INTO_SEMANTICS
```

## Surviving middle schema

The context/record interface avoids these four failures at formal scope by specifying interface/record meanings while excluding the response map.

That survival does not establish physical correctness.

## Result

```text
TOO_WEAK_ANCHOR = VOCABULARY_ONLY
TOO_STRONG_ANCHOR = FULL_RESPONSE_OR_POSSIBILITY_TABLE
CIRCULAR_ANCHOR = PRIMITIVE_TARGET_EQUIVALENCE
FORMALLY_FEASIBLE_MIDDLE = CONTEXT_RECORD_INTERFACE
PHYSICAL_REALIZATION = UNESTABLISHED
```
