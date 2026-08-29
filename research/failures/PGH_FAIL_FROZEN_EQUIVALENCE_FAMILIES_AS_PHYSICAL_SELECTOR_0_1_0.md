# PGH-FAIL-0005 — Frozen Equivalence Families as a Complete Physical Selector 0.1.0

## Identity

```text
DERIVATION_ID = PGH-FAIL-0005
OPERATION_ID = PGH0_PHYSICAL_IRRELEVANCE_SELECTOR_FEASIBILITY_GATE
STATUS = FAILED
CLAIMED_RESULT = ONE_FROZEN_EQUIVALENCE_FAMILY_CAN_BY_ITSELF_SOLVE_R1
FAILURE_CLASS = PHYSICAL_SEMANTIC_UNDERDETERMINATION
NOVELTY_CLAIM = NONE
```

## Failed idea

The prior-art landscape provides several mature notions of formal, structural, theoretical, operational, and task-based equivalence.

A tempting next step is to adopt one of them directly as the PGH criterion for physical irrelevance.

The feasibility gate rejects that move.

## Candidate families tested

```text
S1 = DEFINITIONAL_OR_SYNTACTIC_EQUIVALENCE
S2 = CATEGORICAL_EQUIVALENCE
S3 = MORITA_EQUIVALENCE
S4 = DUALITY_OR_COMMON_CORE_EQUIVALENCE
S5 = STRUCTURAL_ISOMORPHIC_OR_UNIVALENT_EQUIVALENCE
S6 = OPERATIONAL_OR_EMPIRICAL_EQUIVALENCE
S7 = TASK_OR_POSSIBILITY_EQUIVALENCE
```

No family satisfies all R1 criteria.

## Failure pattern

Purely formal criteria can be precise and non-result-directed but do not, by form alone, establish that the preserved structure is physically relevant.

Physically interpreted criteria can track meaningful content only after observables, processes, tasks, common cores, physical morphisms, or other semantic structure has been selected.

Thus the candidate families separate into:

```text
FORMALLY_CLEAN_BUT_NOT_PHYSICALLY_PRIVILEGED
```

or

```text
PHYSICALLY_MEANINGFUL_BUT_SEMANTICALLY_LOADED
```

at current scope.

## Why categorical equivalence does not automatically solve R1

Categorical equivalence can remove presentation surplus only relative to a chosen category.

The choice of objects and especially morphisms determines which structure is being preserved. If those choices encode the physical content, then the category organizes the physical equivalence but does not independently derive which content is physical.

## Why Morita/definitional equivalence does not automatically solve R1

These criteria control formal intertranslatability and theoretical extensions. They are powerful notions of formal sameness but do not by themselves establish that formal sameness equals physical sameness across genuinely different mathematical formulations.

## Why duality/common-core equivalence does not automatically solve R1

A common-core account explicitly identifies invariant structure shared by dual descriptions. But specifying the correct common core already requires deciding what is representational surplus and what is physical content.

The selector has been relocated into the common-core identification.

## Why structural/isomorphic equivalence does not automatically solve R1

“Same up to isomorphism” is meaningful only after the structure to be preserved is fixed.

The PGH burden is upstream: which structure is physically significant enough that its isomorphisms should define physical identity?

## Why operational/empirical equivalence does not automatically solve R1

Operational agreement is physically relevant, but it requires a specification of observables, interventions, records, outcomes, or processes.

If those are defined using the target theory, then the equivalence criterion risks importing the physical content PGH intended to derive.

Empirical equivalence may also be too coarse to establish full physical identity.

## Why task/possibility equivalence does not automatically solve R1

Agreement on possible/impossible tasks is close to PGH's modal ambition.

But if the possibility structure is already known and used as the equivalence criterion, then the target physical law has been inserted at the selector stage rather than explained by grammar.

## Result

```text
FROZEN_EQUIVALENCE_FAMILY_SOLVES_R1_DIRECTLY = NO
AD_HOC_HYBRID_SOLVES_R1 = NOT_ACCEPTED
R1_REQUIRES_SEMANTIC_ANCHOR = YES
```

## Preserved value

The failure substantially narrows R1.

The next question is no longer:

> Which mathematical equivalence notion should PGH choose?

It is:

> What is the weakest physical semantic anchor that can constrain which formal equivalences matter without itself carrying the substantive physical laws?

This is a stronger and more failure-exposed research question.

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = PGH-OBJ-0008
RULE_DEPENDENCIES = R1_ACCEPTANCE_CRITERIA
LEMMA_DEPENDENCIES = PGH-DER-0006
SEMANTIC_ASSUMPTIONS = NONE_ACCEPTED_AS_PHYSICAL_SELECTOR
PHYSICAL_ASSUMPTIONS = NONE
SOURCE_DEPENDENCIES = FROZEN_37_SOURCE_LANDSCAPE
```
