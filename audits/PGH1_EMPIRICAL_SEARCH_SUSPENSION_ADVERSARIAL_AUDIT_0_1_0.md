# PGH-1 Empirical-Search Suspension Adversarial Audit — Adjudication 0.1.0

## Identity

```text
OPERATION_ID = PGH1_EMPIRICAL_SEARCH_SUSPENSION_ADVERSARIAL_AUDIT
PREREGISTRATION_COMMIT = c50b2ba2f8a6bd85aaa4fefe7b25699f047c627a
CANONICAL_BASE = 47b9f17f6cb9b0cf7f4e6273a35c24386d720dd4
CANONICAL_BASE_TREE = 9156c5f8c77b831c941ca208d73684c1593b3b90
CANDIDATE_PACKAGE = PGH-OBJ-0052
NEW_EXTERNAL_SOURCE_SEARCH = NO
NEW_TARGET_SEARCH = NO
NEW_REGISTRY_SEARCH = NO
NEW_DATASET_SEARCH = NO
RESPONSE_DATA_ACCESS = NO
CANDIDATE_REVISION = NO
```

## 1. Controlling result

```text
S1_CANDIDATE_IDENTITY_LOCATION = PASS_FOR_RESPONSE_BLIND_EXPANSION
S2_ANTI_LEAKAGE_TARGET = PASS_FOR_RESPONSE_BLIND_EXPANSION
S3_PRIOR_AUTHORIZATION_FOR_LATER_EXPANSION = PASS_FOR_RESPONSE_BLIND_EXPANSION
S4_COUNTERFACTUAL_CHOICE_INTEGRITY = PASS_FOR_RESPONSE_BLIND_EXPANSION
S5_TARGET_FAMILY_PRIVILEGING = PASS_FOR_RESPONSE_BLIND_EXPANSION_WITH_PROSPECTIVE_COVERAGE_CONTROLS
S6_CANDIDATE_OUTCOME_CONTAMINATION = PASS_FOR_RESPONSE_BLIND_EXPANSION
S7_FALSIFIABILITY_SELF_SEALING_RISK = PASS_FOR_RESPONSE_BLIND_EXPANSION
S8_WEAKEST_ADEQUATE_REPAIR = R1__NEW_PREREGISTERED_METADATA_ONLY_SEARCH_EXPANSION_UNDER_EXISTING_PGH_OBJ_0052

OUTCOME = B__STRICT_SUSPENSION_RULE_OVERREACHES__SAME_CANDIDATE_RESPONSE_BLIND_SEARCH_EXPANSION_MAY_BE_DESIGNED_PROSPECTIVELY

PGH_OP_0112_FACTUAL_NO_TARGET_RESULT = PRESERVED
PGH_OP_0112_SUSPENSION_PENDING_REVIEW = PRESERVED_HISTORICALLY
PGH_OP_0112_INDEPENDENT_ORIGIN_ONLY_RESUMPTION_RULE = SUPERSEDED_PROSPECTIVELY_AT_DEFINED_SCOPE
PGH_OBJ_0052_IDENTITY_CHANGED = NO
TARGET_SEARCH_REOPENED_BY_THIS_AUDIT = NO
NEXT_OPERATION_MAY_DESIGN_SEARCH_ARCHITECTURE = YES
NEXT_OPERATION_MAY_EXECUTE_SEARCH = NO_UNLESS_SEPARATELY_PREREGISTERED
```

The strict independent-origin requirement imposed by `PGH-OP-0112` is more restrictive than the earlier candidate identity and anti-leakage rules require.

The audit does **not** find that arbitrary search widening is legitimate. It finds that a new broader target-discovery architecture may be designed and frozen prospectively under the same `PGH-OBJ-0052` identity when the redesign uses only response-blind search-feasibility information and when the new universe, ordering, stopping rule and contamination controls are fixed before execution.

## 2. The key category error in the strict rule

The canonical record distinguishes three information classes:

```text
R_RESPONSE = target values, dependence, candidate statistic, T_ind compatibility, predicted relation
R_METADATA = authority, access, release identity, schema, native alphabets, joint indexing, validity/missingness
R_FEASIBILITY = whether a bounded metadata-search protocol returned any fully eligible targets
```

`PGH-OP-0108` and `PGH-OP-0110` exposed only `R_METADATA` and `R_FEASIBILITY`.

They did not expose `R_RESPONSE`.

The anti-rescue rules were built principally to prevent an observed or anticipated **hypothesis-relevant response pattern** from selecting the target, role mapping, grammar, scope, model subset, statistic or repair. Treating a zero-yield metadata search as epistemically equivalent to seeing a PGH outcome is not supported by the frozen earlier record.

```text
ZERO_ELIGIBLE_TARGETS_FROM_ONE_SEARCH != EMPIRICAL_RESULT_OF_PGH
SEARCH_FEASIBILITY_FEEDBACK != T_IND_BEHAVIOR
METADATA_AVAILABILITY != TARGET_RESPONSE
```

The zero-target result can motivate improving **coverage** without revealing which target would help or hurt PGH.

## 3. S1 — candidate identity location

```text
VERDICT = PASS_FOR_RESPONSE_BLIND_EXPANSION
```

`PGH-OBJ-0052` freezes `I` at the level of:

- eligibility conditions;
- native-binary treatment;
- deterministic field selection;
- deterministic A/B/C role assignment;
- allowed metadata classes;
- forbidden response/dependence information;
- a deterministic target tie-break after candidate-set closure.

Critically, the package says:

```text
AFTER_A_SEPARATELY_PREREGISTERED_BOUNDED_METADATA_ONLY_DISCOVERY_PASS_CLOSES_ITS_CANDIDATE_SET
    -> APPLY_THE_FROZEN_LEXICAL_TARGET_TIE_BREAK
```

It does **not** freeze one eternal search-engine query set, one fixed collection of scientific domains, or the exact D1-D5 lanes as part of `(G,J,S,I)`.

Those exact lanes and queries were introduced later in the separately preregistered `PGH-OP-0108` discovery operation.

Therefore:

```text
EXACT_SEARCH_UNIVERSE_IS_PART_OF_G_J_S_I = NO
ELIGIBILITY_AND_TARGET_SELECTION_RULES_ARE_PART_OF_I = YES
OP_0108_SEARCH_ARCHITECTURE_IS_DOWNSTREAM_EXECUTION_METHOD = YES
```

A new search pass can preserve candidate identity if it does not alter the frozen eligibility, field/role, contamination or target-selection rules.

## 4. S2 — anti-leakage target

```text
VERDICT = PASS_FOR_RESPONSE_BLIND_EXPANSION
```

The canonical leakage failure `PGH-FAIL-0033` identifies the invalid direction as:

```text
OBSERVED_PATTERN -> ROLE_ASSIGNMENT -> CLAIMED_PREDICTION
```

and requires the admissible direction:

```text
PREREGISTERED_ROLE_ASSIGNMENT -> GRAMMAR_RESTRICTION -> EMPIRICAL_TEST
```

That failure record explicitly permits target discovery to use:

```text
METADATA
FEASIBILITY
ACCESSIBILITY
MEASUREMENT_DEFINITION_INFORMATION
```

while forbidding use of the target conditional-independence outcome to select the system.

The strong successor standard similarly prohibits ranking targets by predicted relation, correlation, candidate statistic, residuals, favorable historical result or target-specific parameter fit.

Neither source says that learning a search protocol has poor metadata coverage permanently contaminates the candidate.

## 5. S3 — prior authorization for later expansion

```text
VERDICT = PASS_FOR_RESPONSE_BLIND_EXPANSION
```

This is the strongest direct contradiction to the strict OP-0112 resumption rule.

The canonical repaired target-freeze artifact, produced at `PGH-OP-0110`, states:

> A later expansion of the target-search architecture would be a new scientific operation with a new preregistration.

It then places the correct ceiling on that possibility:

- the expansion may not silently widen OP-0110;
- it may not use dependence/model-behavior information to choose new lanes or targets.

Thus the pre-OP-0112 record already distinguished:

```text
SILENT_POSTHOC_WIDENING = FORBIDDEN
SEPARATELY_PREREGISTERED_LATER_EXPANSION = PERMITTED_IN_PRINCIPLE
DEPENDENCE_DRIVEN_EXPANSION = FORBIDDEN
```

`PGH-OP-0112` subsequently added a further requirement that the discovery methodology have independent provenance outside the need to obtain a PGH target.

No new target-response exposure occurred between OP-0110 and OP-0112 that required this strengthening.

The strengthening was therefore a governance choice, not a consequence compelled by empirical contamination.

## 6. S4 — counterfactual-choice integrity

```text
VERDICT = PASS_FOR_RESPONSE_BLIND_EXPANSION
```

OP-0112 argued that the exact expansion would not have been designed had OP-0110 found a target, and therefore fails a counterfactual-choice test.

That test is too strong for search-method feasibility.

A scientific procedure may legitimately be redesigned after a **technical or coverage failure** without becoming outcome-selected, provided the redesign is frozen before the next execution and does not use the scientific response the procedure is meant to test.

Examples internal to this project already instantiate that principle: OP-0110 itself repaired the search-result transport after OP-0108 exposed a provenance defect, while keeping scientific rules frozen.

The relevant counterfactual is not:

```text
WOULD_WE_HAVE_IMPROVED_SEARCH_COVERAGE_IF_THE_FIRST_SEARCH_HAD_SUCCEEDED?
```

It is:

```text
WOULD_THE_NEW_SEARCH_ARCHITECTURE_AND_SELECTION_RULE_BE_ACCEPTABLE
REGARDLESS_OF_WHETHER_ITS_EVENTUAL_ELIGIBLE_TARGETS_SUPPORT_OR_REFUTE_PGH?
```

A prospectively frozen, response-blind expansion can satisfy that stronger scientific counterfactual.

## 7. S5 — target-family privileging

```text
VERDICT = PASS_FOR_RESPONSE_BLIND_EXPANSION_WITH_PROSPECTIVE_COVERAGE_CONTROLS
```

The risk identified by OP-0112 is real: TGT-001..TGT-039 may teach the project which institutions, domains or schemas are more likely to contain three native binary fields.

But metadata-level **eligibility yield** is not candidate-response behavior, and the risk can be controlled without demanding that the entire search method originate outside PGH.

A future design operation must therefore freeze controls such as:

```text
NO_LANE_OR_UNIVERSE_SELECTION_BASED_ON_NEAR_MISS_TGT_IDS
NO_USE_OF_TGT_001_039_RESPONSE_BEHAVIOR__NONE_WAS_ACCESSED
NO_DOMAIN_RANKING_BY_EXPECTED_PGH_RESULT
GENERAL_COVERAGE_RATIONALE_REQUIRED_FOR_EACH_UNIVERSE_COMPONENT
DETERMINISTIC_UNIVERSE_ORDER_REQUIRED
FINITE_OR_MECHANICALLY_BOUNDED_CLOSURE_REQUIRED
ELIGIBILITY_RULES_UNCHANGED
TARGET_TIE_BREAK_UNCHANGED
CONTAMINATION_RULES_UNCHANGED
```

Previously encountered candidates remain provenance records. Their existence may not be used to reverse-engineer a universe around near misses.

Independent origin is one valid way to reduce discretion, but it is not the only logically adequate control.

## 8. S6 — candidate-outcome contamination

```text
VERDICT = PASS_FOR_RESPONSE_BLIND_EXPANSION
```

The frozen record establishes:

```text
TARGET_VALUES_ACCESSED = NO
DEPENDENCE_INFORMATION_USED = NO
T_IND_COMPATIBILITY_USED = NO
CANDIDATE_VERDICT_OBSERVED = NO
```

Knowing that a dataset lacks three documented native-binary fields or stable release identity says whether it can instantiate the frozen test. It does not say whether its response distribution would lie in `T_ind`.

The same is true of learning that the five-query search architecture had insufficient coverage to find an eligible interface.

No present information supplies a directional PGH outcome signal that a new search can exploit.

## 9. S7 — falsifiability and self-sealing risk

```text
VERDICT = PASS_FOR_RESPONSE_BLIND_EXPANSION
```

The strict independent-origin rule creates a real asymmetry:

- the project is permitted to formulate a universal physical postulate;
- it is permitted one bounded metadata discovery strategy;
- if that strategy finds no testable interface, the project may not deliberately improve target discovery for the purpose of testing the claim unless the improved method happened to arise for another reason.

That is stricter than ordinary prospectivity requires and can make the hypothesis artificially difficult to falsify.

The appropriate anti-rescue firewall is to prevent **result-directed model or target choice**, not to require accidental provenance for every improvement in test infrastructure.

```text
TRUTH_SEEKING_REQUIRES_COSTLY_FAILURE
TRUTH_SEEKING_ALSO_REQUIRES_REASONABLE_ACCESS_TO_FAILURE_OPPORTUNITIES
```

This finding does not authorize unlimited search. It removes an unnecessary provenance condition while preserving pre-execution freeze and response blindness.

## 10. S8 — weakest adequate repair

```text
VERDICT = R1__NEW_PREREGISTERED_METADATA_ONLY_SEARCH_EXPANSION_UNDER_EXISTING_PGH_OBJ_0052
```

A new candidate identity is not required because the exact search universe is not part of frozen `(G,J,S,I)`.

The weakest adequate repair is:

1. preserve `PGH-OBJ-0052` exactly;
2. preserve `G`, `J`, `S`, `I`, native-binary eligibility, field selection, role assignment, target tie-break and contamination rules exactly;
3. open a separate **search-architecture design operation** before any new target search;
4. design a broader but finite or mechanically bounded response-blind metadata universe;
5. freeze its provenance, coverage rationale, deterministic ordering and stopping rule;
6. stop;
7. only then, in another separately preregistered operation, execute target discovery.

The design operation may use the fact that the first search had inadequate coverage, but may not use near-miss target identities to tailor the universe around them and may not inspect any response/dependence information.

## 11. Why Outcome A fails

Outcome A required positive support that `R_FEASIBILITY` alone creates the same contamination as `R_RESPONSE`, or that independent non-PGH provenance is the only adequate discretion control.

The frozen record establishes neither.

Instead:

- the package delegates candidate-set discovery to separately preregistered bounded passes;
- the anti-leakage rules focus on response/model-behavior selection;
- `PGH-FAIL-0033` explicitly allows metadata and feasibility information;
- the repaired no-target result itself explicitly permits later expansion as a new preregistered operation.

Therefore the strict OP-0112 rule is not source-bound as a necessary consequence of earlier PGH methodology.

## 12. Why Outcome C fails

Outcome C would require the exact search universe to be constitutive of `I` or the target-selection rule.

It is not.

The frozen candidate defines what an eligible interface is, how fields and roles are fixed, what metadata may be used, what response information is forbidden, and how the final eligible set is tie-broken. The concrete D1-D5 universe was introduced only in downstream OP-0108.

Changing the downstream search coverage while preserving those candidate rules does not change the candidate's physical proposition or instantiation mapping.

## 13. Supersession semantics

```text
PGH_OP_0112_NO_TARGET_FACT = PRESERVED
PGH_OP_0112_DECISION_TO_AVOID_SILENT_WIDENING = PRESERVED
PGH_OP_0112_DECISION_TO_AVOID_DEPENDENCE_DRIVEN_SEARCH = PRESERVED
PGH_OP_0112_INDEPENDENT_ORIGIN_ONLY_RESUMPTION_REQUIREMENT = SUPERSEDED_PROSPECTIVELY
PGH_OP_0115_TRIGGER_REASSESSMENT = HISTORICALLY_VALID_UNDER_THEN_CONTROLLING_RULE
```

No historical artifact is edited.

The post-FCP trigger reassessment remains a valid closed-record result: under the OP-0112 rule then in force, no independent trigger existed. It simply no longer controls whether a **new response-blind search architecture may be deliberately designed**.

## 14. New prospective boundary

This audit does **not** itself reopen empirical target search.

```text
ACTIVE_TARGET_SEARCH = STILL_SUSPENDED_PENDING_SEARCH_ARCHITECTURE_DESIGN
TARGET_SELECTED = NO
TARGET_VALUES_ACCESSED = NO
EMPIRICAL_TEST = UNINSTANTIATED
```

The next scientifically authorized operation is design-only:

```text
NEXT_OPERATION = PGH1_RESPONSE_BLIND_TARGET_DISCOVERY_COVERAGE_EXPANSION_DESIGN_GATE
NEXT_OPERATION_CLASS = PRE_SEARCH_METHODOLOGY_DESIGN
NEW_TARGET_SEARCH_DURING_NEXT_OPERATION = FORBIDDEN
NEW_DATASET_INSPECTION_DURING_NEXT_OPERATION = FORBIDDEN
RESPONSE_DATA_ACCESS = FORBIDDEN
```

That operation must freeze a broader search universe without using target outcomes or near-miss-specific tailoring.

## 15. Claim ceiling

```text
PGH_OBJ_0052_IS_TRUE = NO_CLAIM
PGH_OBJ_0052_IS_FALSE = NO_CLAIM
PGH_OBJ_0052_EMPIRICAL_SUPPORT = NONE
PGH_OBJ_0052_EMPIRICAL_REFUTATION = NONE
SEARCH_ARCHITECTURE_EXPANSION_IS_SCIENTIFICALLY_PERMISSIBLE = YES_UNDER_FROZEN_CONTROLS
SEARCH_ARCHITECTURE_EXPANSION_IS_ALREADY_QUALIFIED = NO
TARGET_DISCOVERY_IS_REOPENED = NO
```

## 16. Qualification

```text
PREREGISTRATION_FROZEN_BEFORE_ADJUDICATION = YES
FROZEN_CLOSED_RECORD_ONLY = YES
NEW_EXTERNAL_SOURCE_SEARCH = NO
NEW_TARGET_SEARCH = NO
NEW_DATASET_SEARCH = NO
TARGET_VALUES_ACCESSED = NO
DEPENDENCE_INFORMATION_ACCESSED = NO
CANDIDATE_IDENTITY_CHANGED = NO
EXACTLY_ONE_OUTCOME = YES
OUTCOME = B
QUALIFICATION = PASS
```

Truth over PGH requires safeguards that prevent us from choosing a favorable answer, not safeguards that prevent us from making a fair test possible.
