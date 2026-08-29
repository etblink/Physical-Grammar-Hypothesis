# PGH-FAIL-0001 — Bare Formation Grammar Physical Sufficiency Failure 0.1.0

## Identity

```text
DERIVATION_ID = PGH-FAIL-0001
OPERATION_ID = PGH0_MINIMAL_GRAMMAR_CHALLENGE
STATUS = FAILED
CLAIMED_RESULT = BARE_FORMATION_RELATION_IS_SUFFICIENT_FOR_A_NONTRIVIAL_PHYSICAL_GRAMMAR
FAILURE_CLASS = NONEXCLUSIVE; UNDERDETERMINED
```

## Proposed idea

After reducing `IDENTIFY` and `DISTINGUISH` to contextual behavior, one might hope that a bare formation relation

\[
F\subseteq A^3
\]

already supplies the generative core required by strong PGH.

That hope fails.

## Failure witness — arbitrary table encoding

For any finite carrier `A` and any desired set of locally admitted triples

\[
S\subseteq A^3,
\]

choose

\[
F=S.
\]

The bare grammar then reproduces exactly the selected admissibility table.

Therefore the architecture does not explain why one relation `F` should obtain rather than another.

The substantive selection is stored directly in the relation itself.

## Extreme countermodels

Two grammars satisfy the same bare architecture:

### Universal formation

\[
F=A^3.
\]

Every local triple is admissible.

No nonuniversal exclusion follows.

### Empty formation

\[
F=\varnothing.
\]

No local triple is admissible.

The architecture itself does not prefer either extreme, or any intermediate relation.

## Why extensional quotienting does not repair the problem

Contextual extensional reduction removes labels that have identical grammatical behavior.

It does not constrain which grammatical behaviors exist.

A quotient can compress redundant names while leaving an otherwise arbitrary relation table.

Therefore:

```text
EXTENSIONALITY = CANONICALIZATION_OF_DESCRIPTION
EXTENSIONALITY = NOT_A_NONTRIVIAL_SELECTION_LAW
```

## Nontriviality failures

```text
N1_UNIVERSAL_ENCODING = FAIL
N3_NONUNIVERSAL_EXCLUSION = FAIL
N6_GENERATIVE_COMPRESSION = FAIL
N7_INDEPENDENT_CONSEQUENCE = FAIL
```

### N1

An arbitrary local admissibility pattern is reproduced by choosing `F` to be that pattern.

### N3

If `F(a,b,c)` is absent, the triple is excluded only because its absence was entered directly into the table. The bare architecture supplies no independent reason for the exclusion.

### N6

In the worst case the description of `F` is simply the full admissibility table. No generative compression is guaranteed.

### N7

No non-table-driven restriction follows from the bare architecture.

## What remains valid

The failure does not invalidate:

- the formal definition of the formation shell;
- contextual equivalence derived from incidence profiles;
- extensional quotienting;
- the finding that literal label duplication is grammatically redundant at bare well-formedness scope;
- the finding that some generative relation is needed for a generative grammar.

The valid remainder is retained as `PGH-GRAM-0002`, the Extensional Formation Baseline.

## Hidden import audit

```text
HIDDEN_PHYSICAL_IMPORT = NONE_FOUND
SELECTION_LOAD = ARBITRARY_CHOICE_OF_FORMATION_RELATION_F
SEMANTIC_MAP_SMUGGLING = NOT_APPLICABLE
```

The failure is therefore not that known physics was secretly inserted.

The deeper problem is that the candidate is *too permissive*: it can store essentially any desired local rule table without explaining the rule table.

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = ABSTRACT_FORMATION_RELATION
RULE_DEPENDENCIES = NONE
LEMMA_DEPENDENCIES = NONE
SEMANTIC_ASSUMPTIONS = LOCAL_WELL_FORMEDNESS_IS_MEMBERSHIP_IN_F
PHYSICAL_ASSUMPTIONS = NONE
SOURCE_DEPENDENCIES = NONE
METALANGUAGE_DEPENDENCIES = SET_OR_CLASS_MEMBERSHIP; RELATIONS; FINITE_CARRIERS_FOR_COUNTERMODEL
```

## Result

```text
PGH-FAIL-0001 = FAILED_PRESERVED
BARE_FORMATION_GRAMMAR_PHYSICAL_SUFFICIENCY = REJECTED
WHAT_REMAINS = FORMALLY_INTERESTING_NONPHYSICAL_BASELINE
NEXT_BURDEN = FIND_A_NONARBITRARY_CONSTRAINT_ON_FORMATION
SUPERSESSION_STATUS = NOT_SUPERSEDED
```
