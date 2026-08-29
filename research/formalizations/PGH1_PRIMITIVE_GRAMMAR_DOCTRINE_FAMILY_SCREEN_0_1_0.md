# PGH-1 Primitive Grammar Doctrine Family Screen 0.1.0

## Status

```text
OBJECT_ID = PGH-OBJ-0022
OBJECT_CLASS = PRIMITIVE_GRAMMAR_CANDIDATE_FAMILY_MAP
PHYSICAL_STATUS = NONE
```

## Candidate identities

```text
PGH-GRAM-0003 = BARE_MONOIDAL_PRIMITIVE_GRAMMAR_CANDIDATE
PGH-GRAM-0004 = SYMMETRIC_MONOIDAL_PRIMITIVE_GRAMMAR_CANDIDATE
PGH-GRAM-0005 = CARTESIAN_PRIMITIVE_GRAMMAR_CANDIDATE
PGH-GRAM-0006 = COCARTESIAN_PRIMITIVE_GRAMMAR_CANDIDATE
PGH-GRAM-0007 = BICARTESIAN_PRIMITIVE_GRAMMAR_CANDIDATE
```

## Shared candidate boundary

Each `PGH-GRAM-*` identity refers only to the doctrine axioms/universal-property structure named above.

It does **not** include later target-specific:

```text
GENERATORS
RELATIONS
EQUATIONS
REWRITE_RULES
RESPONSE_TABLES
PROBABILITY_RULES
PHYSICAL_INTERPRETATIONS
```

Adding any such substantive content changes the candidate and requires separate provenance/adjudication.

## Model-class semantics

For each candidate `G`, its abstract well-formed structures are its models:

\[
W(G)=\{X:X\models G\}.
\]

A finite generator seed is not part of the candidate definition and is not required for formal candidacy.

Free seeded constructions may later be used as controlled models, but they do not define the candidate itself.

## Experimental roles

```text
PGH-GRAM-0003 = WEAK_COMPOSITION_CONTROL
PGH-GRAM-0004 = SYMMETRY_EXCHANGE_CONTROL
PGH-GRAM-0005 = PRODUCT_STRUCTURAL_CANDIDATE
PGH-GRAM-0006 = COPRODUCT_DUAL_CANDIDATE
PGH-GRAM-0007 = BICARTESIAN_RICH_CONTROL
```

No role implies physical priority.

## Physical ceiling

```text
FORMAL_CANDIDACY = YES
PHYSICAL_REFERENCE_MAPPING = NONE
PHYSICAL_BRIDGE = NONE
SUBSTANTIVE_PHYSICAL_LAW_EXHAUSTION = UNTESTED
EMPIRICAL_PREDICTION = NONE
```

## Assumption ancestry

All candidates inherit:

```text
CANDIDATE_STANDARD = PGH-OBJ-0020
ANCHOR_POLICY = PGH-OBJ-0012 / LAW_FREE_A_REF
TARGET_RESULT_INPUT = NONE
```

Candidate-specific structural assumptions are exactly those of the named doctrine and must remain explicit in any later bridge test.
