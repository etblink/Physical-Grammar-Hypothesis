# PGH-1 Universal-Scope Falsification Target-Selection Asymmetry Audit — Handoff 0.1.0

## Exact result

```text
OPERATION_ID = PGH1_UNIVERSAL_SCOPE_FALSIFICATION_TARGET_SELECTION_ASYMMETRY_AUDIT
PREREGISTRATION_COMMIT = b692cc1bfd12e584f04039acf66439d759576410
CANDIDATE_PACKAGE = PGH-OBJ-0052

OUTCOME = B__REFUTATION_ASYMMETRY_QUALIFIES__ADVERSARIAL_I_ELIGIBLE_TARGET_MAY_REFUTE_UNIVERSAL_PGH_OBJ_0052__SURVIVAL_EARNS_ZERO_POSITIVE_CREDIT

OUTCOME_NEUTRAL_TARGET_SELECTION_REQUIRED_FOR_FIRST_POSITIVE_CREDIT = YES
ADVERSARIAL_TARGET_SELECTION_PERMITTED_FOR_REFUTATION_ONLY = YES
ADVERSARIAL_FALSIFICATION_ROUTE_QUALIFIED = YES
ACTUAL_ADVERSARIAL_TARGET = NONE
TARGET_VALUES_ACCESSED = NO
PGH_OBJ_0052_REFUTED = NO
PGH_OBJ_0052_SUPPORTED = NO
STRONG_PGH_CONFIRMED = NO
R2B = UNSATISFIED
```

## Controlling scientific distinction

The canonical post-Kp admission standard already distinguishes positive credit from negative evidence:

```text
KNOWN_KP_INCOMPATIBILITY = MAY_REFUTE_A_SUCCESSOR_IF_LOGICALLY_ENTAILED
KNOWN_KP_COMPATIBILITY = ZERO_PROSPECTIVE_CONFIRMATION_CREDIT
```

The active candidate has universal physical scope:

```text
S = TRUE_FOR_ALL_I_ELIGIBLE_PHYSICAL_RECORD_INTERFACES
```

Therefore a deliberately severe target does not become invalid negative evidence merely because it was chosen to challenge the candidate. What matters for refutation is that the physical interface genuinely satisfies frozen `I`, the candidate identity is unchanged, and the empirical rejection is obtained under a fully prospective analysis.

## Frozen asymmetry

```text
QUALIFIED_REJECT_T_ind_ON_ADVERSARIAL_I_ELIGIBLE_TARGET
  -> MAY_REFUTE_PGH_OBJ_0052_AT_TARGET

DO_NOT_REJECT_T_ind_ON_ADVERSARIAL_TARGET
  -> ADVERSARIAL_STRESS_TEST_SURVIVAL_ONLY
  -> POSITIVE_EMPIRICAL_CREDIT = ZERO

EXPECTED_INCOMPATIBILITY_BEFORE_DATA
  -> NEGATIVE_EMPIRICAL_CREDIT = ZERO
  -> ACTUAL_QUALIFIED_REJECTION_STILL_REQUIRED
```

The project may not select a hostile target, fail to reject, and then relabel survival as ordinary prospective support.

## Frozen candidate identity

```text
G = PGH-GRAM-0010
J = PGH-OBJ-0051
S = TRUE_FOR_ALL_I_ELIGIBLE_PHYSICAL_RECORD_INTERFACES
I = SYMMETRIC_NATIVE_BINARY_TRIPLE_RECORD_INSTANTIATION_PROTOCOL_V0_1_0
CANDIDATE_IDENTITY_CHANGED = NO
```

An adversarial target that requires changing `G`, `J`, `S`, native-binary eligibility, field selection, role assignment, access rules, missingness rules, or any other constitutive part of `I` cannot test the same candidate identity.

## Formal adversarial direction

Canonical `PGH-DER-0033` establishes an explicit outside-model witness:

```text
p_star(000) = 1/2
p_star(111) = 1/2
p_star NOT_IN T_ind
```

and proves more generally that any nondegenerate perfect-agreement distribution supported only on `{000,111}` is outside `T_ind`, while correlated/common-source controls can realize such behavior.

This is a legitimate falsification direction, not a positive prediction.

## Physical-interface eligibility remains mandatory

A deliberately constructed experimental or instrumental record interface may qualify in principle because frozen `S` does not exclude laboratory design and frozen `I` does not require an independent-source physical architecture.

It must nevertheless satisfy, before response analysis:

```text
PUBLIC_OR_AUDITABLE_EVENT_LEVEL_ACCESS = YES
VERSIONED_OR_STABLY_IDENTIFIED_AUTHORITY = YES
REPEATED_JOINT_RECORD_INDEX = YES
AT_LEAST_THREE_DISTINCT_NATIVE_BINARY_RECORD_FIELDS = YES
SELECTED_FIELDS_JOINTLY_OBSERVED_PER_RECORD = YES
MISSINGNESS_OR_VALIDITY_CODES_DOCUMENTED = YES
```

No thresholding, binning, learned encoding, state merging, or post-data redefinition is permitted to force eligibility.

## Pre-data analysis firewall

Before any response-data materialization, a downstream adversarial test must freeze at least:

```text
TARGET_IDENTITY_AND_PHYSICAL_INTERFACE
AUDITABLE_CUSTODY_OR_AUTHORITY_IDENTITY
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

Sequence:

```text
DESIGN_AND_TARGET_FREEZE
-> ANALYSIS_PREREGISTRATION
-> RESPONSE_DATA_MATERIALIZATION
-> EXECUTION
```

## Relation to prior outcome-neutral searches

All prior target-discovery searches remain valid and preserved. They sought an outcome-neutral target capable of generating ordinary prospective survival information as well as possible refutation.

The new route is additional and negative-only:

```text
OUTCOME_NEUTRAL_ROUTE = REQUIRED_FOR_FIRST_POSITIVE_EMPIRICAL_CREDIT
ADVERSARIAL_ROUTE = QUALIFIED_NEGATIVE_ONLY_FALSIFICATION_ROUTE
```

The repaired no-target result remains zero evidence for PGH.

## Next operation

```text
NEXT_OPERATION = PGH1_ADVERSARIAL_PHYSICAL_INTERFACE_DESIGN_GATE
NEXT_OPERATION_CLASS = TARGET_FREE_NEGATIVE_ONLY_PHYSICAL_INTERFACE_DESIGN
TARGET_VALUES = FORBIDDEN
ACTUAL_DATA_GENERATION = FORBIDDEN
G_J_S_I_REVISION = FORBIDDEN
```

The design gate should compare a small finite set of minimal physical-interface architectures capable of stressing the explicit outside-`T_ind` common-agreement witness while satisfying frozen `I` without semantic or measurement trickery.

It should prefer physical simplicity, independent auditability, exact native binary states, low ambiguity, deterministic record indexing, explicit missingness, and straightforward independent replication.

A separate pre-data analysis gate must follow any design selection before a physical experiment may generate or materialize response data.

## Qualification

```text
CLOSED_RECORD_AUDIT = PASS
POSITIVE_CREDIT_FIREWALL = PRESERVED
NEGATIVE_ONLY_ROUTE = QUALIFIED
ACTUAL_TARGET_SELECTED = NO
EXPERIMENT_DESIGNED = NO
RESPONSE_DATA_ACCESSED = NO
CANDIDATE_REVISION = NO
QUALIFICATION = PASS
```

Truth over PGH means deliberately hard tests are allowed to break a universal claim, while never being recycled into confirmation if they fail to break it.