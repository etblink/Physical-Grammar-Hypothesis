# PGH-0 Non-Arbitrary Formation Constraint Challenge — Qualified Local Handoff 0.1.0

## Status

```text
OPERATION_ID = PGH0_NONARBITRARY_FORMATION_CONSTRAINT_CHALLENGE
REGISTRY_ID = PGH-OP-0005
STATUS = QUALIFIED_LOCAL_NOT_INTEGRATED
CANONICAL_BASE = 0b1b563c8ce9b40f42c55f74132440535856845e
PREREGISTRATION_COMMIT = 0b5c6b21265a6df4599ff1f69cf4c9da37358a8e
WORKING_BRANCH = research/pgh0-nonarbitrary-formation-constraint
CANONICAL_MAIN_MUTATION = NONE
SOURCE_BOUND_STATUS = NOT_YET_SOURCE_BOUND
NEW_SOURCE_COUNT = 0
```

## Scientific result

```text
OUTCOME = D__NONTRIVIAL_FORMAL_CONSTRAINTS_EXIST_BUT_ALL_REQUIRE_AN_UNEARNED_EXTRA_PREMISE
SUCCESSOR_GRAMMAR_QUALIFIED = NO
ACTIVE_BASELINE_REMAINS = PGH-GRAM-0002
PHYSICAL_BRIDGE = NOT_PERFORMED
```

The experiment distinguishes three levels that had previously been easy to blur:

```text
REPRESENTATION_COVARIANCE
FORMAL_COHERENCE_PREMISE
DERIVED_FORMAL_EXCLUSION
```

Relabeling covariance is required but too weak to select a formation law.

Stronger coherence principles can produce real exclusions, but the project has not yet justified which representation differences are entitled to be identified.

## Qualified result 1

```text
PGH-DER-0002 = ISOMORPHISM_COVARIANCE_UNDERDETERMINATION
STATUS = QUALIFIED_FORMAL
```

Any arbitrary subset of formation-structure isomorphism classes defines a relabeling-covariant selector.

On a two-label carrier there are 256 ternary relations but 136 isomorphism classes; therefore `2^136` different class-selection predicates satisfy label neutrality at that finite scope.

Conclusion:

```text
LABEL_NEUTRALITY = NECESSARY
LABEL_NEUTRALITY_ALONE_SELECTS_FORMATION = NO
```

## Qualified result 2

```text
PGH-DER-0003 = PARSE_COHERENCE_IMPLIES_ASSOCIATIVITY
STATUS = QUALIFIED_CONDITIONAL_FORMAL
```

For a total deterministic binary representation, if alternative three-term parenthesizations are required to yield the same grammar-internal result, associativity follows.

Exhaustive two-label validation:

```text
TOTAL_BINARY_OPERATIONS = 16
ASSOCIATIVE = 8
NONASSOCIATIVE = 8
```

Thus the rule has genuine exclusion power.

But:

```text
PARENTHESIZATION_INDEPENDENCE_ALREADY_JUSTIFIED = NO
ASSOCIATIVITY_IS_FUNDAMENTAL = NOT_ESTABLISHED
ASSOCIATIVITY_IS_PHYSICAL = NO
```

## Preserved failure 1

```text
PGH-FAIL-0002 = STRONG_PERMUTATION_INVARIANCE_AS_LABEL_NEUTRALITY
STATUS = FAILED_PRESERVED
```

Full permutation automorphy is not the same as covariance under renaming. It imposes structural homogeneity.

On a three-label carrier it leaves only 32 of `2^27` ternary relations, so it is highly selective, but the selectivity comes from an added premise rather than from label neutrality itself.

## Preserved failure 2

```text
PGH-FAIL-0003 = UNPRIVILEGED_SIMPLICITY_SELECTION
STATUS = FAILED_PRESERVED
```

Generative compression remains an important success criterion, but raw description length cannot select a formation law before a privileged or suitably invariant description framework is justified.

Any finite relation can be made short by adding a primitive token that names it.

## Other candidate results

### Extensionality

```text
EXTENSIONALITY = CANONICALIZATION_NOT_SUBSTANTIVE_SELECTION
```

On a two-label carrier, 254 of 256 ternary relations are already extensional under the complete profile criterion. The only non-extensional cases are empty and universal formation.

### Arity / encoding neutrality

```text
ARITY_NEUTRALITY = WELL_MOTIVATED
INTRINSIC_FORMULATION_FROM_BARE_F = NOT_YET_AVAILABLE
```

Equating different auxiliary/binary encodings requires an additional translation, projection, or equivalence structure. Without justification, arbitrariness moves into that structure.

### Extremal controls

```text
MAXIMAL_PERMISSIVENESS = UNIVERSAL_FORMATION
MINIMAL_PERMISSIVENESS = EMPTY_FORMATION
```

Neither gives the sought nontrivial law.

## Main conceptual advance

The promising mechanism is now narrower:

\[
\text{justified representation equivalence}
\Longrightarrow
\text{coherence condition}
\Longrightarrow
\text{nontrivial formal exclusion}.
\]

The right-hand implication can work: `PGH-DER-0003` demonstrates it in the binary special case.

The unresolved burden is the left-hand implication.

The next problem is therefore not “which algebraic axiom looks physical?” It is:

> Which differences between formation representations can be declared irrelevant without encoding the desired algebraic law into the equivalence declaration itself?

## Nontriviality status

```text
NONARBITRARY_FORMATION_CONSTRAINT_FOUND = NO
FORMAL_NONUNIVERSAL_EXCLUSION_FOUND = YES_CONDITIONALLY
REPRESENTATION_INVARIANCE = DEEPENED_NOT_SOLVED
GENERATIVE_COMPRESSION_SELECTOR = NOT_ESTABLISHED
PHYSICAL_GRAMMAR_FOUND = NO
EMPIRICAL_SUPPORT = NONE
```

## Current open-question impact

The result directly sharpens:

```text
PGH-Q-0011
PGH-Q-0012
PGH-Q-0008
```

It does not canonically resolve them on this unintegrated branch.

## New burdens pending canonical registration

If this candidate is accepted and integrated, register at least:

1. Can representation equivalence for formation be defined without presupposing the coherence equation it is meant to derive?
2. Can decomposition coherence be formulated for relational and variable-arity formation without privileging binary functions?
3. What is the weakest translation structure needed to compare two formation presentations?

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = PGH-GRAM-0002
RULE_DEPENDENCIES = ISOMORPHISM_COVARIANCE; CONDITIONAL_PARSE_COHERENCE
LEMMA_DEPENDENCIES = PGH-DER-0002; PGH-DER-0003
SEMANTIC_ASSUMPTIONS = BARE_WELL_FORMEDNESS; CONDITIONAL_PARSE_EQUIVALENCE_ONLY_WHERE_DECLARED
PHYSICAL_ASSUMPTIONS = NONE
SOURCE_DEPENDENCIES = NONE
```

## Do not assume

- `PGH-GRAM-0002` is physical.
- associativity is fundamental.
- associativity is physical.
- arbitrary parenthesizations represent the same grammar object.
- full permutation invariance follows from label neutrality.
- relational homogeneity is a law of nature.
- simplicity or compression already has a privileged measure.
- arity neutrality has been formally achieved.
- representation equivalence has been derived.
- any physical law has been obtained.
- PGH has empirical support.
- this result changes FCP.

## Next recommended operation

```text
NEXT_RECOMMENDED_OPERATION = PGH0_REPRESENTATION_EQUIVALENCE_AND_COHERENCE_CHALLENGE
NEXT_OPERATION_AUTHORIZED = NO
```

## Review boundary

Canonical `main` remains unchanged.

Before integration, independently review:

1. the isomorphism-covariance underdetermination theorem;
2. the Burnside count for the two-label finite witness;
3. the covariance-versus-homogeneity distinction;
4. the exact 32-of-`2^27` strong-permutation count for three labels;
5. the 254-of-256 extensionality count for two-label ternary relations;
6. the 8-of-16 associativity enumeration;
7. whether `PGH-DER-0003` is properly limited to a conditional theorem;
8. whether simplicity failure is correctly scoped to unprivileged encodings;
9. whether outcome `D` follows without preselecting the result.

<!-- PGH_HANDOFF_CAPSULE_BEGIN -->
```json
{
  "capsule_schema_version": "0.1.0",
  "operation_id": "PGH0_NONARBITRARY_FORMATION_CONSTRAINT_CHALLENGE",
  "status": "QUALIFIED_LOCAL_NOT_INTEGRATED",
  "indexed_research_baseline_commit": "0b1b563c8ce9b40f42c55f74132440535856845e",
  "must_read": [
    "governance/PGH0_NONARBITRARY_FORMATION_CONSTRAINT_CHALLENGE_PREREGISTRATION_0_1_0.md",
    "research/formalizations/PGH0_NONARBITRARY_FORMATION_CONSTRAINT_ADJUDICATION_0_1_0.md",
    "research/derivations/PGH_DERIVATION_ISOMORPHISM_COVARIANCE_UNDERDETERMINATION_0_1_0.md",
    "research/derivations/PGH_DERIVATION_PARSE_COHERENCE_ASSOCIATIVITY_0_1_0.md",
    "research/failures/PGH_FAIL_STRONG_PERMUTATION_INVARIANCE_AS_LABEL_NEUTRALITY_0_1_0.md",
    "research/failures/PGH_FAIL_UNPRIVILEGED_SIMPLICITY_SELECTION_0_1_0.md"
  ],
  "outputs": [
    "research/formalizations/PGH0_NONARBITRARY_FORMATION_CONSTRAINT_ADJUDICATION_0_1_0.md",
    "research/derivations/PGH_DERIVATION_ISOMORPHISM_COVARIANCE_UNDERDETERMINATION_0_1_0.md",
    "research/derivations/PGH_DERIVATION_PARSE_COHERENCE_ASSOCIATIVITY_0_1_0.md",
    "research/failures/PGH_FAIL_STRONG_PERMUTATION_INVARIANCE_AS_LABEL_NEUTRALITY_0_1_0.md",
    "research/failures/PGH_FAIL_UNPRIVILEGED_SIMPLICITY_SELECTION_0_1_0.md",
    "handoffs/PGH0_NONARBITRARY_FORMATION_CONSTRAINT_CHALLENGE_HANDOFF_0_1_0.md"
  ],
  "open_questions": [
    "PGH-Q-0001",
    "PGH-Q-0004",
    "PGH-Q-0005",
    "PGH-Q-0006",
    "PGH-Q-0007",
    "PGH-Q-0008",
    "PGH-Q-0009",
    "PGH-Q-0010",
    "PGH-Q-0011",
    "PGH-Q-0012"
  ],
  "next_recommended_operation": "PGH0_REPRESENTATION_EQUIVALENCE_AND_COHERENCE_CHALLENGE",
  "next_operation_authorized": false,
  "do_not_assume": [
    "ASSOCIATIVITY_IS_FUNDAMENTAL",
    "ASSOCIATIVITY_IS_PHYSICAL",
    "PARENTHESIZATION_IS_ALWAYS_REPRESENTATIONAL",
    "FULL_PERMUTATION_INVARIANCE_FOLLOWS_FROM_LABEL_NEUTRALITY",
    "HOMOGENEITY_IS_PHYSICAL",
    "SIMPLICITY_HAS_A_PRIVILEGED_MEASURE",
    "ARITY_NEUTRALITY_HAS_BEEN_ACHIEVED",
    "REPRESENTATION_EQUIVALENCE_HAS_BEEN_DERIVED",
    "A_NONARBITRARY_FORMATION_LAW_HAS_BEEN_FOUND",
    "PGH_HAS_EMPIRICAL_SUPPORT",
    "PGH_HAS_ANY_CANONICAL_EFFECT_ON_FCP"
  ]
}
```
<!-- PGH_HANDOFF_CAPSULE_END -->
