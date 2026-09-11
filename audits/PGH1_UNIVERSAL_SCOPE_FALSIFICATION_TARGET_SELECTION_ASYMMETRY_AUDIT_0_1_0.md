# PGH-1 Universal-Scope Falsification Target-Selection Asymmetry Audit — Adjudication 0.1.0

## Identity

```text
OPERATION_ID = PGH1_UNIVERSAL_SCOPE_FALSIFICATION_TARGET_SELECTION_ASYMMETRY_AUDIT
PREREGISTRATION_COMMIT = b692cc1bfd12e584f04039acf66439d759576410
PREREGISTRATION_TREE = 371c784d4f08a46a908b907a3128234838ce77c4
CANONICAL_BASE = f44a3eefcaca3be56bb3fcd39b2e2f6456316489
CANDIDATE_PACKAGE = PGH-OBJ-0052
NEW_EXTERNAL_SOURCE_SEARCH = NO
NEW_TARGET_SEARCH = NO
NEW_EXPERIMENT_DESIGN = NO
TARGET_VALUES_ACCESSED = NO
CANDIDATE_REVISION = NO
```

## 1. Controlling result

```text
OUTCOME = B__REFUTATION_ASYMMETRY_QUALIFIES__ADVERSARIAL_I_ELIGIBLE_TARGET_MAY_REFUTE_UNIVERSAL_PGH_OBJ_0052__SURVIVAL_EARNS_ZERO_POSITIVE_CREDIT

OUTCOME_NEUTRAL_TARGET_SELECTION_REQUIRED_FOR_FIRST_POSITIVE_CREDIT = YES
ADVERSARIAL_TARGET_SELECTION_PERMITTED_FOR_REFUTATION_ONLY = YES
TARGET_MUST_SATISFY_FROZEN_I_WITHOUT_REVISION = YES
ANALYSIS_MUST_BE_FROZEN_BEFORE_RESPONSE_DATA = YES
NONREJECTION_ON_ADVERSARIAL_TARGET_POSITIVE_CREDIT = ZERO
EXPECTED_INCOMPATIBILITY_BY_ITSELF = NOT_REFUTATION
ACTUAL_QUALIFIED_REJECTION_REQUIRED = YES
```

The canonical PGH rules contain a real support/refutation asymmetry. They prohibit outcome-directed target choice as a basis for prospective **positive empirical credit**, but they do not erase logically valid negative evidence against a universal physical claim merely because the target was chosen to be severe.

A deliberately adversarial target is therefore admissible for **negative-only** testing if, and only if, the target independently passes the already-frozen `I` eligibility rules and the experiment-specific analysis is frozen before response data are inspected.

## 2. F1 — textual empirical-credit asymmetry

**Verdict: supports Outcome B.**

The strongest source-bound statement is in the post-Kp successor admission standard:

```text
KNOWN_KP_INCOMPATIBILITY = MAY_REFUTE_A_SUCCESSOR_IF_LOGICALLY_ENTAILED
KNOWN_KP_COMPATIBILITY = ZERO_PROSPECTIVE_CONFIRMATION_CREDIT
KP_AS_FIRST_POSITIVE_SUCCESSOR_TEST = FORBIDDEN
```

This is explicitly asymmetric. A known incompatibility can remain negative evidence, while known compatibility cannot be recycled into confirmation.

The same section says:

```text
The first positive empirical credit for a successor must come from a genuinely prospective target whose relevant behavior was not used to construct, select or tune the successor.
```

The object of the strict prospectivity rule is **positive empirical credit**. It does not state that a logically valid counterexample becomes invalid negative evidence solely because its incompatibility was anticipated.

The active package repeats the same ceiling:

```text
ANY_PRE_FREEZE_DISCOVERED_TARGET = INELIGIBLE_FOR_FIRST_POSITIVE_CREDIT
```

and separately defines candidate-level failure as:

```text
REJECT_T_ind = REFUTED_AT_TARGET
```

Therefore:

```text
CANONICAL_RULES_DISTINGUISH_POSITIVE_CREDIT_FROM_REFUTATION = YES
```

## 3. F2 — universal quantifier structure

**Verdict: supports Outcome B.**

`PGH-OBJ-0052` fixes:

```text
S = TRUE
```

and states that the candidate applies to **every** physical record interface satisfying frozen `I`.

Thus the candidate-level physical proposition has the form:

```text
FOR_ALL_I_ELIGIBLE_INTERFACES x:
    p_emp^x in T_ind
```

A single valid in-scope physical interface whose empirical distribution is qualifiedly established outside `T_ind` is sufficient to falsify that universal proposition at the candidate level.

Target-selection neutrality is not part of the truth conditions of the universal statement. Scope and interface eligibility are.

```text
S_IS_UNIVERSAL_OVER_I = YES
ONE_QUALIFIED_IN_SCOPE_COUNTEREXAMPLE_IS_LOGICALLY_SUFFICIENT_FOR_REFUTATION = YES
```

## 4. F3 — formal outside-model witness

**Verdict: supports Outcome B.**

`PGH-DER-0033` proves:

```text
p_star(000) = 1/2
p_star(111) = 1/2
p_star NOT_IN T_ind
```

for the nondegenerate perfect common-bit distribution.

The same derivation shows that a correlated-source realization can produce `p_star` and that a one-common-source model can realize every finite joint distribution.

The existence of an explicit outside-model witness gives a legitimate adversarial falsification direction. Knowing the witness in advance cannot, by itself, manufacture the empirical fact that an independently frozen physical interface actually produces a distribution outside `T_ind`.

It can only motivate a severe test.

```text
FORMAL_OUTSIDE_MODEL_WITNESS_EXISTS = YES
WITNESS_KNOWLEDGE_INVALIDATES_POSITIVE_CREDIT_IF_USED_TO_SELECT_TARGET = YES
WITNESS_KNOWLEDGE_INVALIDATES_GENUINE_NEGATIVE_COUNTEREVIDENCE = NO
```

## 5. F4 — I does not require an independent-source physical architecture

**Verdict: supports Outcome B.**

Frozen `I` requires metadata-level properties:

```text
PUBLIC_OR_AUDITABLE_EVENT_LEVEL_ACCESS
VERSIONED_OR_STABLY_IDENTIFIED_AUTHORITY
REPEATED_JOINT_RECORD_INDEX
AT_LEAST_THREE_DISTINCT_NATIVE_BINARY_RECORD_FIELDS
SELECTED_FIELDS_JOINTLY_OBSERVED_PER_RECORD
MISSINGNESS_OR_VALIDITY_CODES_DOCUMENTED
```

It does **not** require the physical system to contain three mutually independent sources.

The candidate package is stronger still:

```text
No scale, regime, causal architecture, laboratory design, independent-source metadata, or external physical sector is used to narrow applicability.
```

The latent independent-source triangle is the model class claimed to describe the observable distribution, not an eligibility condition that the physical target must already possess.

```text
I_REQUIRES_INDEPENDENT_SOURCE_PHYSICAL_ARCHITECTURE = NO
COMMON_SOURCE_OR_OTHER_PHYSICAL_ARCHITECTURE_EXCLUDED_FROM_S_BY_DEFAULT = NO
```

## 6. F5 — constructed experimental interfaces are not excluded

**Verdict: supports Outcome B with a strict boundary.**

Nothing in frozen `I` limits eligible interfaces to naturally preexisting archival datasets. The candidate speaks of physical record interfaces, and its universal scope explicitly declines to narrow applicability by laboratory design.

The operational target rules used by the project likewise recognize physical, natural, instrumental and experimental record interfaces as physical-record classes.

Therefore a prospectively documented experimental/instrumental interface is not excluded **merely because it was constructed for a test**.

However construction supplies no exemption from `I`:

```text
EXPERIMENTALLY_CONSTRUCTED_INTERFACE_MAY_BE_I_ELIGIBLE = YES_IN_PRINCIPLE
DESIGNING_THREE_FIELDS_MAKES_THEM_ELIGIBLE_AUTOMATICALLY = NO
PUBLIC_OR_AUDITABLE_ACCESS_STILL_REQUIRED = YES
STABLE_INTERFACE_IDENTITY_STILL_REQUIRED = YES
NATIVE_BINARY_RULE_STILL_REQUIRED = YES
JOINT_INDEXABILITY_STILL_REQUIRED = YES
MISSINGNESS_VALIDITY_DOCUMENTATION_STILL_REQUIRED = YES
```

An experiment that requires changing `I` to admit itself cannot test the same candidate identity.

## 7. F6 — false-support and false-refutation risks are not symmetric

**Verdict: supports Outcome B.**

Selecting a target because its already-known behavior agrees with the candidate can generate circular apparent support:

```text
KNOWN_COMPATIBILITY -> TARGET_SELECTION -> CLAIMED_PREDICTION
```

That is precisely what the prospectivity rules prohibit.

Selecting a target because it is expected to be difficult for a **universal** law has a different logic:

```text
PRE_DATA_TARGET_AND_INTERFACE_FREEZE
-> PRE_DATA_ANALYSIS_FREEZE
-> PHYSICAL_DATA
-> QUALIFIED_REJECTION_OR_NONREJECTION
```

The expectation of failure is not itself evidence. A refutation exists only if the later physical data, under the frozen interface and qualified analysis, actually reject membership in `T_ind`.

Adversarial selection can still produce false negative claims if scope, measurement, missingness, analysis or calibration are manipulated. Therefore every existing interface and analysis firewall remains mandatory.

```text
ADVERSARIAL_SELECTION_ALONE = ZERO_NEGATIVE_EVIDENCE
QUALIFIED_EMPIRICAL_REJECTION = REQUIRED_FOR_REFUTATION
```

## 8. F7 — known-result quarantine is positive-credit scoped

**Verdict: supports Outcome B.**

The canonical language repeatedly uses:

```text
ZERO_POSITIVE_CREDIT
FIRST_POSITIVE_SUCCESSOR_TEST
FIRST_POSITIVE_EMPIRICAL_CREDIT
```

while separately preserving known incompatibility as potentially refuting.

The quarantine therefore blocks recycled confirmation, not all negative inference.

This is not a newly invented exception; it is already present in the successor admission standard.

## 9. F8 — survival credit on an adversarial target

**Verdict:**

```text
SURVIVAL_ON_ADVERSARIAL_TARGET = ZERO_POSITIVE_EMPIRICAL_CREDIT
```

A target chosen specifically because it is expected to stress or break `T_ind` is not an outcome-neutral sample from the candidate's claimed domain. Non-rejection can be recorded as stress-test survival information, but it does not become ordinary prospective confirmation.

Thus the asymmetry is intentionally one-way:

```text
QUALIFIED_REJECTION_ON_ADVERSARIAL_I_ELIGIBLE_TARGET = MAY_REFUTE_PGH_OBJ_0052
NONREJECTION_ON_SAME_TARGET = ZERO_POSITIVE_EMPIRICAL_CREDIT
```

This prevents the project from selecting a hostile target, seeing it survive, and then relabeling that survival as stronger confirmation than the target-selection process warrants.

## 10. F9 — experiment-specific prospective firewall remains mandatory

**Verdict: PASS only with full firewall.**

Before any response-data materialization, an adversarial falsification operation must freeze at least:

```text
TARGET_IDENTITY_AND_PHYSICAL_INTERFACE
AUTHORITY_OR_AUDITABLE_CUSTODY_IDENTITY
THREE_NATIVE_BINARY_FIELD_IDENTIFIERS
AUTHORITY_DEFINED_TWO_STATE_ALPHABETS
A_B_C_ROLE_ASSIGNMENT
RECORD_INDEX
VALIDITY_MISSINGNESS_RULES
COMPLETE_DATA_RANGE_OR_TRIAL_COUNT_RULE
DATA_CUSTODY_AND_HASHING_PATH
PRIMARY_T_ind_TEST_OR_DECISION_FUNCTIONAL
FINITE_SAMPLE_NULL_OR_CALIBRATION
ALPHA_AND_DECISION_THRESHOLD
STOCHASTIC_IMPLEMENTATION_IF_ANY
VERDICT_MAPPING
```

The sequence must remain:

```text
DESIGN_AND_TARGET_FREEZE
-> ANALYSIS_PREREGISTRATION
-> RESPONSE_DATA_MATERIALIZATION
-> EXECUTION
```

Expected incompatibility may motivate design but may not tune the test after data.

## 11. F10 — candidate revision remains forbidden

**Verdict: PASS.**

Outcome B creates no permission to change:

```text
G
J
S
I
```

If a proposed hostile target fails frozen `I`, it is not a counterexample to `PGH-OBJ-0052` under the same identity.

If the project wants a looser interface, thresholded variables, merged states, target-specific discretization or revised target-selection rule, that is a new candidate identity under the canonical post-Kp standard.

## 12. Why Outcome A fails

Symmetric outcome-neutral target selection is not source-bound as a validity condition for negative evidence.

The admission standard explicitly preserves known incompatibility as potentially refuting while denying known compatibility prospective confirmation credit.

Outcome A would erase that canonical asymmetry and would make a universal law artificially harder to falsify than its own governance requires.

```text
OUTCOME_A = REJECTED
```

## 13. Why Outcome C fails

The frozen record supplies no principled truth-conditional distinction between:

1. an already-existing physical interface known to violate the model; and
2. a prospectively constructed physical interface deliberately designed to challenge the same universal claim,

provided both satisfy the same frozen `I` and the latter's response data are not used to alter the interface or analysis.

The universal scope expressly does not exclude laboratory design.

A constructed test may have extra engineering and measurement burdens, but those are handled by `I`, custody and analysis qualification—not by declaring deliberate falsification logically inadmissible.

```text
OUTCOME_C = REJECTED
```

## 14. Outcome D not required

The load-bearing questions are resolved by explicit canonical text:

- positive credit versus known incompatibility is distinguished;
- scope is universal;
- `I` does not require independent-source physical architecture;
- laboratory design does not narrow scope;
- candidate and analysis firewalls remain available to control false counterexamples.

```text
OUTCOME_D = NOT_REQUIRED
```

## 15. Exact qualified route

The newly qualified route is:

```text
PGH_OBJ_0052_UNIVERSAL_SCOPE
-> ADVERSARIAL_I_ELIGIBLE_PHYSICAL_INTERFACE_DESIGN_MAY_BE_CONSIDERED
-> TARGET_AND_INTERFACE_MUST_FREEZE_BEFORE_RESPONSE_DATA
-> ANALYSIS_MUST_FREEZE_BEFORE_RESPONSE_DATA
-> IF_QUALIFIED_REJECT_T_ind:
       PGH_OBJ_0052 = REFUTED_AT_TARGET
-> IF_DO_NOT_REJECT_T_ind:
       PGH_OBJ_0052 = ADVERSARIAL_STRESS_TEST_SURVIVAL__ZERO_POSITIVE_EMPIRICAL_CREDIT
-> IF_ANALYSIS_OR_INTERFACE_NOT_QUALIFIED:
       NO_CANDIDATE_VERDICT
```

No target is selected by this audit.

## 16. Relation to repaired no-target searches

All prior outcome-neutral metadata searches remain valid and useful. They pursued a target capable of producing ordinary prospective survival information as well as potential refutation.

The present audit adds a distinct route:

```text
OUTCOME_NEUTRAL_ROUTE = REQUIRED_FOR_FIRST_POSITIVE_EMPIRICAL_CREDIT
ADVERSARIAL_ROUTE = NEGATIVE_ONLY_FALSIFICATION_ROUTE
```

The absence of an outcome-neutral target therefore no longer blocks the project from designing a deliberately severe negative-only test of its universal claim.

This does not retroactively change any prior search result.

## 17. Scientific consequence

```text
PGH_OBJ_0052_EMPIRICAL_TRUTH = UNADJUDICATED
PGH_OBJ_0052_REFUTED = NO
PGH_OBJ_0052_SUPPORTED = NO
ADVERSARIAL_FALSIFICATION_ROUTE_QUALIFIED = YES
ACTUAL_ADVERSARIAL_TARGET = NONE
TARGET_VALUES_ACCESSED = NO
STRONG_PGH_CONFIRMED = NO
R2B = UNSATISFIED
```

The next high-value operation is a separately preregistered **target-free adversarial physical-interface design gate**. It must choose the simplest physically auditable interface capable of testing an explicit outside-`T_ind` witness without changing `I`, and must stop before response data are generated or inspected.

## 18. Qualification

```text
PREREGISTRATION_FROZEN_BEFORE_ADJUDICATION = YES
CLOSED_RECORD_RESPECTED = YES
F1_F10_ALL_ADJUDICATED = YES
NEW_TARGET_SEARCH = NO
NEW_EXPERIMENT_DESIGN = NO
TARGET_VALUES_ACCESSED = NO
G_J_S_I_CHANGED = NO
POSITIVE_CREDIT_FIREWALL_PRESERVED = YES
NEGATIVE_ONLY_ROUTE_EXPLICIT = YES
EXACTLY_ONE_OUTCOME = YES
QUALIFICATION = PASS
```

Truth over PGH means a rule built to prevent self-confirmation cannot be repurposed to make a universal claim immune to purpose-built counterexamples.