# PGH-0 Empirical Generator Invariance and Seed Minimality Gate — Handoff 0.1.0

## Operation result

```text
OPERATION_ID = PGH0_EMPIRICAL_GENERATOR_INVARIANCE_AND_SEED_MINIMALITY_GATE
STATUS = QUALIFIED_CANDIDATE_COMPLETE_NOT_INTEGRATED
OUTCOME = B__EQUAL_CLOSURE_SEEDS_ARE_EQUIVALENT_ONLY_FOR_CLOSURE_FACTORING_STRUCTURE_AND_MINIMAL_GENERATORS_ARE_NOT_GENERALLY_UNIQUE_OR_GUARANTEED
CANONICAL_BASE = 89e54b1d3173a16730134fa1b188675aeb034b62
PREREGISTRATION_COMMIT = 13a753de4882d17f6f353ff0a3e0d7f3fe5b7d6f
PROJECT_LEAD_INDEPENDENT_REVIEW = PENDING
PUBLICATION_AUTHORIZED = NO
FCP_EFFECT = NONE
```

## Qualified result

```text
PGH-DER-0010 = EMPIRICAL_GENERATOR_CLOSURE_EQUIVALENCE
STATUS = QUALIFIED_FORMAL
```

For a fixed grammar-generated closure `Cl`, seed sets are generator-equivalent when they generate the same closed interface:

\[
A\sim_{Cl}B \iff Cl(A)=Cl(B).
\]

Every downstream quantity that factors through `Cl` is invariant under replacement of one seed by an equal-closure seed.

This does **not** establish full physical equivalence unless the relevant physical semantics itself factors through generated closure.

## Preserved failure

```text
PGH-FAIL-0010 = UNIQUE_OR_MINIMAL_EMPIRICAL_SEED
STATUS = FAILED_PRESERVED
```

Controls establish that:

- minimum generators can be nonunique;
- equal-closure minimum generators need not be related by a grammar automorphism;
- a finitary unary closure can have no inclusion-irredundant generating set;
- selecting the smallest seed after specifying a desired physical closure merely presupposes the target.

## R1 consequence

```text
R1_GENERATOR_EQUIVALENCE = QUALIFIED_AT_CLOSURE_SCOPE
R1_UNIQUE_EMPIRICAL_SEED_REQUIRED = NO_AT_CLOSURE_SCOPE
R1_SEED_MINIMALITY_SELECTION = FAILED_AS_GENERAL_PRINCIPLE
R1_PHYSICAL_SEMANTIC_FACTORIZATION = UNESTABLISHED
R1_EMPIRICAL_SUBSTRUCTURE_PRIVILEGE = UNESTABLISHED
R1_SOLVED = NO
```

The live question is no longer which seed is fundamental. It is which generated closed empirical substructure, if any, is physically privileged and why.

## Recommended next operation

```text
NEXT_RECOMMENDED_OPERATION = PGH0_EMPIRICAL_SUBSTRUCTURE_PRIVILEGE_GATE
NEXT_OPERATION_AUTHORIZED = NO
```

That gate should test intrinsic, non-result-directed candidate selectors on generated closed substructures rather than on their generating seeds.

Required control classes:

```text
SMALLEST_NONTRIVIAL_CLOSED_SUBSTRUCTURE
LARGEST_REACHABLE_CLOSED_SUBSTRUCTURE
AUTOMORPHISM_INVARIANT_CLOSED_SUBSTRUCTURE
FIXED_POINT_OR_CANONICAL_CLOSURE
INTERSECTION_OR_UNION_OF_SEEDED_CLOSURES
MULTIPLE_SUBSTRUCTURE_UNDERDETERMINATION
```

It must not begin R2 or treat an empirically successful substructure as privileged merely because it matches desired observations.

## Structured handoff capsule

<!-- PGH_HANDOFF_CAPSULE_BEGIN -->
```json
{
  "capsule_schema_version": "0.1.0",
  "operation_id": "PGH0_EMPIRICAL_GENERATOR_INVARIANCE_AND_SEED_MINIMALITY_GATE",
  "status": "QUALIFIED_CANDIDATE_COMPLETE_NOT_INTEGRATED",
  "indexed_research_baseline_commit": "89e54b1d3173a16730134fa1b188675aeb034b62",
  "must_read": [
    "CURRENT_STATE.md",
    "research/formalizations/PGH0_GRAMMAR_GENERATED_EMPIRICAL_INTERFACE_CLOSURE_0_1_0.md",
    "research/derivations/PGH_DERIVATION_EMPIRICAL_GENERATOR_CLOSURE_EQUIVALENCE_0_1_0.md",
    "research/failures/PGH_FAIL_UNIQUE_OR_MINIMAL_EMPIRICAL_SEED_0_1_0.md"
  ],
  "outputs": [
    "governance/PGH0_EMPIRICAL_GENERATOR_INVARIANCE_AND_SEED_MINIMALITY_GATE_PREREGISTRATION_0_1_0.md",
    "audits/PGH0_EMPIRICAL_GENERATOR_INVARIANCE_AND_SEED_MINIMALITY_GATE_0_1_0.md",
    "research/derivations/PGH_DERIVATION_EMPIRICAL_GENERATOR_CLOSURE_EQUIVALENCE_0_1_0.md",
    "research/failures/PGH_FAIL_UNIQUE_OR_MINIMAL_EMPIRICAL_SEED_0_1_0.md",
    "handoffs/PGH0_EMPIRICAL_GENERATOR_INVARIANCE_AND_SEED_MINIMALITY_GATE_HANDOFF_0_1_0.md"
  ],
  "open_questions": [
    "PGH-Q-0016",
    "PGH-Q-0017",
    "PGH-Q-0021"
  ],
  "next_recommended_operation": "PGH0_EMPIRICAL_SUBSTRUCTURE_PRIVILEGE_GATE",
  "next_operation_authorized": false,
  "do_not_assume": [
    "EQUAL_GENERATED_CLOSURE_IS_FULL_PHYSICAL_EQUIVALENCE",
    "MINIMUM_SEED_IS_UNIQUE",
    "IRREDUNDANT_SEED_EXISTS",
    "SEED_MINIMALITY_SELECTS_PHYSICAL_INTERFACE",
    "EMPIRICAL_SUBSTRUCTURE_IS_PHYSICALLY_PRIVILEGED",
    "R1_IS_SOLVED",
    "R2_HAS_STARTED",
    "PGH_HAS_ANY_CANONICAL_EFFECT_ON_FCP"
  ]
}
```
<!-- PGH_HANDOFF_CAPSULE_END -->
