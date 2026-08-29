# PGH-0 Minimal Grammar Challenge — Qualified Local Handoff 0.1.0

## Status

```text
OPERATION_ID = PGH0_MINIMAL_GRAMMAR_CHALLENGE
REGISTRY_ID = PGH-OP-0003
STATUS = QUALIFIED_LOCAL_NOT_INTEGRATED
CANONICAL_BASE = ac6baff2596eedbe3902b07dfe5e5ee2e69ac918
PREREGISTRATION_COMMIT = 98ece4fb0d282072df33a629f8dbecde3ed1b1cf
WORKING_BRANCH = research/pgh0-minimal-grammar-challenge
CANONICAL_MAIN_MUTATION = NONE
SOURCE_BOUND_STATUS = NOT_YET_SOURCE_BOUND
NEW_SOURCE_COUNT = 0
```

## Scientific result

The opening D/C/I shell is not minimal as a set of three independent object-level primitives at bare grammatical well-formedness scope.

```text
MINIMALITY_OUTCOME = D__ALL_THREE_REFORMULATED_INTO_A_DIFFERENT_WEAKER_CORE
```

Detailed result:

```text
IDENTIFY_INDEPENDENT_PRIMITIVE = REDUNDANT_AT_MINIMAL_WELL_FORMEDNESS_SCOPE
DISTINGUISH_INDEPENDENT_PRIMITIVE = REDUNDANT_AT_MINIMAL_WELL_FORMEDNESS_SCOPE
BINARY_COMPOSE_AS_FUNDAMENTAL = NOT_ESTABLISHED
ABSTRACT_FORMATION_OR_GENERATIVE_RELATION = REQUIRED_FOR_GENERATIVE_GRAMMAR
```

A successor formal baseline is proposed:

```text
OBJECT_ID = PGH-GRAM-0002
NAME = EXTENSIONAL_FORMATION_BASELINE
STATUS = PROVISIONAL_FORMAL_BASELINE_NONPHYSICAL
```

It consists, at the weakest worked representation, of a formal carrier `A`, a ternary formation relation `F subset A^3`, and the extensional quotient induced by complete formation-incidence profiles.

## Qualified formal derivation

```text
DERIVATION_ID = PGH-DER-0001
RESULT = CONTEXTUAL_EXTENSIONAL_REDUCTION
STATUS = QUALIFIED_FORMAL
```

For each label `a`, the bare grammar induces its complete formation profile from the positions in which `a` participates in `F`.

Labels with identical profiles are substitutable in every finite formation context with respect to well-formedness.

Therefore the grammar induces contextual equivalence and contextual distinction without independent object-level `IDENTIFY` or `DISTINGUISH` primitives.

The quotient relation is well defined.

Scope limitation:

```text
SEMANTIC_SCOPE = BARE_WELL_FORMEDNESS_ONLY
PHYSICAL_IDENTITY_DERIVED = NO
GAUGE_EQUIVALENCE_DERIVED = NO
OBSERVATIONAL_EQUIVALENCE_DERIVED = NO
```

## Preserved failure

```text
FAILURE_ID = PGH-FAIL-0001
STATUS = FAILED_PRESERVED
FAILED_CLAIM = BARE_FORMATION_RELATION_IS_SUFFICIENT_FOR_A_NONTRIVIAL_PHYSICAL_GRAMMAR
```

Reason:

For any finite desired admissibility table `S subset A^3`, choosing `F=S` reproduces it directly.

Thus the bare formation shell explains no reason why one admissibility relation obtains rather than another.

The extensional quotient removes redundant labels but does not constrain the relation table itself.

## Nontriviality results

For proposed `PGH-GRAM-0002`:

```text
N0_FORMAL_DEFINABILITY = PASS
N1_UNIVERSAL_ENCODING = FAIL
N2_NO_SMUGGLING = PASS_FOR_PURE_FORMAL_REDUCTION
N3_NONUNIVERSAL_EXCLUSION = FAIL
N4_REPRESENTATION_INVARIANCE = PARTIAL
N5_SEMANTIC_LOAD = NOT_APPLICABLE
N6_GENERATIVE_COMPRESSION = FAIL
N7_INDEPENDENT_CONSEQUENCE = FAIL
N8_COUNTEREXAMPLE_EXPOSURE = PASS
N9_RELABELING_INVARIANCE = PASS
N10_PHYSICAL_BRIDGE = NOT_APPLICABLE
```

Candidate-level outcome:

```text
PGH-GRAM-0002_OUTCOME = FORMALLY_INTERESTING_NONPHYSICAL
OPENING_PGH0_GATE = FAIL_TO_ADVANCE_TO_PHYSICAL_BRIDGE
```

## Explicit finite witness

The derivation artifact contains a three-label witness:

```text
A = {a,b,g}
F = {
  (a,g,g), (b,g,g),
  (g,a,g), (g,b,g),
  (g,g,a), (g,g,b)
}
```

`a` and `b` have identical complete formation profiles and therefore merge in the extensional quotient despite being literally different labels.

The failure artifact also gives the universal and empty relation countermodels.

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = ABSTRACT_FORMATION_RELATION
RULE_DEPENDENCIES = CONTEXT_PROFILE_DEFINITION; EXTENSIONAL_QUOTIENT
LEMMA_DEPENDENCIES = PROFILE_EQUALITY_IS_EQUIVALENCE; LOCAL_SUBSTITUTION
SEMANTIC_ASSUMPTIONS = WELL_FORMEDNESS_IS_THE_ONLY_GRAMMAR_INTERNAL_TEST_AT_THIS_STAGE
PHYSICAL_ASSUMPTIONS = NONE
SOURCE_DEPENDENCIES = NONE
METALANGUAGE_DEPENDENCIES = ORDINARY_LOGIC; EQUALITY; SET_OR_CLASS_MEMBERSHIP; RELATIONS; FINITE_TREES
```

## Important interpretation

This operation has **not** found the physical grammar.

It has found a useful lower baseline:

> A generative grammar needs some formation mechanism, but bare formation plus extensionality is only an architecture. Without an additional non-arbitrary restriction, it can encode arbitrary admissibility choices and therefore cannot explain physical possibility.

The first research problem has therefore become sharper rather than merely broader.

## Still open from the canonical registry

Relevant unresolved questions include:

```text
PGH-Q-0001
PGH-Q-0004
PGH-Q-0005
PGH-Q-0006
PGH-Q-0007
PGH-Q-0008
PGH-Q-0009
PGH-Q-0010
```

`PGH-Q-0002` and `PGH-Q-0003` have candidate resolutions in this branch but their canonical registry statuses remain unchanged until integration/reconciliation.

## Newly exposed burdens pending canonical registration

If this candidate is accepted and integrated, register at least the following new questions:

1. What is the weakest non-arbitrary structural constraint on formation that yields an exclusion not merely entered as an admissibility table?
2. Can formation/generativity be expressed in an arity- and ordering-neutral way that survives translation between genuinely different mathematical representations?

## Next recommended operation

```text
NEXT_RECOMMENDED_OPERATION = PGH0_NONARBITRARY_FORMATION_CONSTRAINT_CHALLENGE
NEXT_OPERATION_AUTHORIZED = NO
```

That future operation should begin from the failure of arbitrary `F`, not from an assumption that any familiar algebraic law is physically fundamental.

It should test candidate constraints one at a time and require explicit countermodels.

## Do not assume

- `PGH-GRAM-0002` is a physical grammar.
- extensionality is a law of nature.
- contextual equivalence is gauge equivalence.
- formation is binary at the fundamental level.
- ordered argument positions are temporal or causal.
- some formation relation is sufficient for PGH.
- generic composition entails locality.
- an absent formation triple is a derived exclusion rather than an inserted table entry.
- representation invariance has been established beyond relabeling/isomorphism.
- PGH has empirical support.
- this result changes FCP.

## Required review boundary

Canonical `main` remains unchanged.

Before integration, review whether:

1. the contextual-equivalence proof is sound at its declared scope;
2. the extensional quotient is well defined;
3. the binary-composition downgrade is justified without overclaiming;
4. the universal-table counterexample correctly blocks N1/N3/N6/N7;
5. no physical assumption entered the formal result;
6. the result should supersede `PGH-GRAM-0001` as the live candidate shell.

<!-- PGH_HANDOFF_CAPSULE_BEGIN -->
```json
{
  "capsule_schema_version": "0.1.0",
  "operation_id": "PGH0_MINIMAL_GRAMMAR_CHALLENGE",
  "status": "QUALIFIED_LOCAL_NOT_INTEGRATED",
  "indexed_research_baseline_commit": "ac6baff2596eedbe3902b07dfe5e5ee2e69ac918",
  "must_read": [
    "governance/PGH0_MINIMAL_GRAMMAR_CHALLENGE_PREREGISTRATION_0_1_0.md",
    "research/formalizations/PGH0_MINIMAL_GRAMMAR_FORMALIZATION_0_1_0.md",
    "research/derivations/PGH_DERIVATION_CONTEXTUAL_EXTENSIONAL_REDUCTION_0_1_0.md",
    "research/failures/PGH_FAIL_BARE_FORMATION_GRAMMAR_PHYSICAL_SUFFICIENCY_0_1_0.md"
  ],
  "outputs": [
    "research/formalizations/PGH0_MINIMAL_GRAMMAR_FORMALIZATION_0_1_0.md",
    "research/derivations/PGH_DERIVATION_CONTEXTUAL_EXTENSIONAL_REDUCTION_0_1_0.md",
    "research/failures/PGH_FAIL_BARE_FORMATION_GRAMMAR_PHYSICAL_SUFFICIENCY_0_1_0.md",
    "handoffs/PGH0_MINIMAL_GRAMMAR_CHALLENGE_HANDOFF_0_1_0.md"
  ],
  "open_questions": [
    "PGH-Q-0001",
    "PGH-Q-0004",
    "PGH-Q-0005",
    "PGH-Q-0006",
    "PGH-Q-0007",
    "PGH-Q-0008",
    "PGH-Q-0009",
    "PGH-Q-0010"
  ],
  "next_recommended_operation": "PGH0_NONARBITRARY_FORMATION_CONSTRAINT_CHALLENGE",
  "next_operation_authorized": false,
  "do_not_assume": [
    "PGH_GRAM_0002_IS_PHYSICAL",
    "EXTENSIONALITY_IS_A_PHYSICAL_LAW",
    "CONTEXTUAL_EQUIVALENCE_IS_GAUGE_EQUIVALENCE",
    "FORMATION_IS_FUNDAMENTALLY_BINARY",
    "ORDERED_ARGUMENTS_ARE_TEMPORAL_OR_CAUSAL",
    "BARE_FORMATION_IS_NONTRIVIALLY_EXPLANATORY",
    "COMPOSITIONALITY_IMPLIES_LOCALITY",
    "ABSENT_FORMATION_TRIPLES_ARE_DERIVED_EXCLUSIONS",
    "FULL_REPRESENTATION_INVARIANCE_HAS_BEEN_ESTABLISHED",
    "PGH_HAS_EMPIRICAL_SUPPORT",
    "PGH_HAS_ANY_CANONICAL_EFFECT_ON_FCP"
  ]
}
```
<!-- PGH_HANDOFF_CAPSULE_END -->
