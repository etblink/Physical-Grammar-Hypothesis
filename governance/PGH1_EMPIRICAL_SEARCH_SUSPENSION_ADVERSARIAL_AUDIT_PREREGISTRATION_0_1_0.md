# PGH-1 Empirical-Search Suspension Adversarial Audit — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_EMPIRICAL_SEARCH_SUSPENSION_ADVERSARIAL_AUDIT
OPERATION_CLASS = CLOSED_RECORD_METHODOLOGICAL_ADVERSARIAL_AUDIT
CANONICAL_BASE = 47b9f17f6cb9b0cf7f4e6273a35c24386d720dd4
CANONICAL_BASE_TREE = 9156c5f8c77b831c941ca208d73684c1593b3b90
CANDIDATE_PACKAGE = PGH-OBJ-0052
ACTIVE_TARGET_SEARCH_AT_OPEN = SUSPENDED
TARGET_SELECTED_AT_OPEN = NO
TARGET_VALUES_ACCESSED_AT_OPEN = NO
NEW_EXTERNAL_SOURCE_SEARCH = FORBIDDEN
NEW_TARGET_SEARCH = FORBIDDEN
NEW_REGISTRY_SEARCH = FORBIDDEN
NEW_DATASET_SEARCH = FORBIDDEN
RESPONSE_DATA_ACCESS = FORBIDDEN
CANDIDATE_REVISION = FORBIDDEN_DURING_AUDIT
```

## 1. Purpose

Canonical `PGH-OP-0112` suspended active empirical target search after the repaired finite metadata-only search found no eligible target. It imposed a strong resumption rule: search may reopen only after an independently encountered public interface or an independently originated general target-discovery method.

That rule was intended to prevent result-directed rescue. The present audit asks whether it is **strictly required by the earlier PGH prospectivity/anti-leakage architecture**, or whether it overextends the concept of post-result contamination from hypothesis-relevant response outcomes to a purely metadata-level search-feasibility result.

The audit is hostile to both directions:

- it must not reopen search merely because empirical testing is desirable;
- it must not preserve suspension merely because suspension is administratively safer.

The controlling question is:

```text
DOES_ZERO_ELIGIBLE_TARGETS_FROM_A_RESPONSE_BLIND_METADATA_SEARCH
CREATE_THE_SAME_PROSPECTIVITY_CONTAMINATION_AS_OBSERVING_TARGET_RESPONSE_BEHAVIOR
SUCH_THAT_A_LATER_BROADER_BUT_PROSPECTIVELY_FROZEN_METADATA_ONLY_SEARCH
MUST_HAVE_INDEPENDENT_NON_PGH_ORIGIN?
```

## 2. Frozen closed record

No source outside this list may enter the adjudication.

```text
research/candidates/PGH1_POST_KP_NETWORK_SOURCE_SUCCESSOR_PACKAGE_0_1_0.md
  BLOB = 1846e8a176aed14341a829ca6e1e60c71f438afd

governance/PGH1_POST_KP_STRONG_PGH_SUCCESSOR_ADMISSION_STANDARD_0_1_0.md
  BLOB = a507ab1dcffce757475691f502d5e9bd32a19d30

research/failures/PGH_FAIL_POSTHOC_CAUSAL_WIRING_EMPIRICAL_INSTANTIATION_0_1_0.md
  BLOB = 0390cd8e1b94a8976b42da8519acac067771876b

governance/PGH1_POST_KP_NETWORK_SOURCE_SUCCESSOR_TARGET_DISCOVERY_AND_FREEZE_PREREGISTRATION_0_1_0.md
  BLOB = fcadccc02d34710fd4c9aa95501efb1b05592a0f

governance/PGH1_POST_KP_NETWORK_SOURCE_TARGET_DISCOVERY_TRANSPORT_REPAIR_AND_REEXECUTION_PREREGISTRATION_0_1_0.md
  BLOB = af7241896316a67cd3c8f06b94b4aa9b9c15ef56

empirical/PGH1_POST_KP_NETWORK_SOURCE_TARGET_DISCOVERY_REPAIRED_TARGET_FREEZE_0_1_0.md
  BLOB = c79a139984e04685c8e2d43da479d2a71e5cdda8

audits/PGH1_POST_NETWORK_SOURCE_NO_TARGET_DISCOVERY_RESEARCH_SEQUENCING_GATE_0_1_0.md
  BLOB = 1340bf90b7ce5882dc1f4bce2292c05b61bb99ad

audits/PGH1_POST_FCP_INDEPENDENT_TRIGGER_REASSESSMENT_0_1_0.md
  BLOB = d7a33d71df0c7a9d5f222d368d12a071c6067779
```

The FCP taxonomy result may be mentioned only as context that PGH remains an empirically unadjudicated nonframework physical postulate. It may not supply a target or search universe.

## 3. Facts that are already fixed and may not be disputed

```text
PGH_OBJ_0052_WAS_FROZEN_BEFORE_OP_0108 = YES
OP_0108_AND_OP_0110_TARGET_DISCOVERY_WERE_METADATA_ONLY = YES
TARGET_VALUES_ACCESSED_IN_OP_0108_OR_OP_0110 = NO
DEPENDENCE_INFORMATION_USED_IN_OP_0108_OR_OP_0110 = NO
T_IND_COMPATIBILITY_USED_IN_OP_0108_OR_OP_0110 = NO
TARGET_SELECTED = NO
EMPIRICAL_PGH_RESULT_OBSERVED = NO
ZERO_ELIGIBLE_TARGETS_IN_FROZEN_FINITE_SEARCH = YES
NO_TARGET_RESULT_HAS_ZERO_EVIDENTIAL_SIGN = YES
```

The audit may dispute the **sequencing consequence** drawn from those facts, not the facts themselves.

## 4. Mandatory distinction: empirical outcome versus discovery feasibility

The audit must separately classify information encountered after package freeze into:

```text
R_RESPONSE = information about target response values, dependence, candidate statistic, T_ind membership, or predicted relation
R_METADATA = authoritative metadata about access, schema, field alphabets, release identity, joint indexing, validity/missingness, or search-result availability
R_FEASIBILITY = information that a particular bounded metadata-search protocol returned zero fully eligible targets
```

It must adjudicate whether `R_FEASIBILITY`, in the absence of `R_RESPONSE`, is sufficient by itself to trigger the same anti-rescue prohibition that applies after empirical exposure.

No category may be collapsed merely by calling all three "results."

## 5. Frozen competing hypotheses

```text
H_A_STRICT_SUSPENSION =
  OP_0112_IS_METHODologically_REQUIRED;
  designing a broader target-search architecture after zero eligible targets is post-result construction;
  only independently originated discovery machinery may reopen search.

H_B_RESPONSE_BLIND_EXPANSION =
  OP_0112_IS_OVERSTRICT;
  zero-target metadata feasibility does not reveal hypothesis-relevant behavior;
  a new broader target-search architecture may be prospectively designed and frozen under the same PGH-OBJ-0052 identity, provided it uses no response/dependence information and cannot silently alter I.

H_C_NEW_IDENTITY_ONLY =
  OP_0112_IS_OVERSTRICT_AS_A_PERMANENT_BARRIER,
  but a broader search architecture is sufficiently constitutive of I or target-selection identity that resumption requires a revised candidate identity rather than the same PGH-OBJ-0052.

H_D_UNRESOLVED =
  the frozen record does not determine whether broader search is compatible with the existing candidate identity or prospectivity standard.
```

No hypothesis is preferred in advance.

## 6. Adjudication criteria

Each criterion receives:

```text
PASS_FOR_STRICT_SUSPENSION
PASS_FOR_RESPONSE_BLIND_EXPANSION
PASS_FOR_NEW_IDENTITY_ONLY
UNRESOLVED
```

### S1 — candidate identity location

Determine whether the exact discovery **universe/lanes/query architecture** is part of `I`, or whether `I` freezes eligibility, role assignment, metadata classes, tie-breaking and contamination rules while leaving each bounded discovery pass to a separately preregistered downstream operation.

### S2 — anti-leakage target

Determine what the canonical anti-leakage rules are actually designed to prevent:

```text
TARGET_RESPONSE_DRIVEN_SELECTION
MODEL_COMPATIBILITY_DRIVEN_SELECTION
FAVORABLE_OUTCOME_DRIVEN_ROLE_ASSIGNMENT
```

versus whether they also forbid adaptation to response-blind search feasibility.

### S3 — prior authorization for later expansion

Test the exact statement in the repaired no-target result that:

> a later expansion of the target-search architecture would be a new scientific operation with a new preregistration.

Determine whether OP-0112 validly narrowed this prior allowance, and what new evidence or governance premise justified the narrowing.

### S4 — counterfactual-choice integrity

Ask whether a new expansion can be frozen by a rule that would be acceptable regardless of whether it later finds zero, one or many eligible targets.

The fact that expansion is motivated by an earlier search's **coverage failure** does not automatically answer this criterion either way.

### S5 — target-family privileging

Determine whether the known TGT-001..TGT-039 metadata create an unavoidable ability to favor scientific domains or institutions likely to produce eligible targets.

If such risk exists, determine whether deterministic coverage rules and explicit quarantine are sufficient to neutralize it, or whether only independent provenance can.

### S6 — candidate-outcome contamination

Determine whether any information presently known can reveal or proxy the eventual PGH verdict for a newly selected target.

Metadata such as binary-field availability may increase test feasibility but is not automatically candidate-outcome information.

### S7 — falsifiability / self-sealing risk

Determine whether the strict independent-origin requirement makes the hypothesis materially harder to confront than its own earlier prospective rules require.

```text
ANTI_RESCUE_DISCIPLINE != LICENSE_TO_CREATE_A_SELF_SEALING_HYPOTHESIS
```

This criterion cannot by itself override genuine leakage risk, but genuine leakage risk cannot be assumed merely because a new test-enabling method is designed after a feasibility failure.

### S8 — weakest adequate repair

If OP-0112 is overstrict, identify the weakest correction that preserves all response-blindness and candidate-identity protections.

Possible repairs include:

```text
R0 = NO_CHANGE
R1 = NEW_PREREGISTERED_METADATA_ONLY_SEARCH_EXPANSION_UNDER_EXISTING_PGH_OBJ_0052
R2 = NEW_CANDIDATE_IDENTITY_WITH_REVISED_I_THEN_NEW_SEARCH
R3 = DEFER
```

## 7. Hard firewalls

This audit may not:

```text
DESIGN_THE_ACTUAL_NEW_SEARCH_UNIVERSE
NAME_NEW_TARGET_DATASETS
RUN_WEB_SEARCH
RUN_REGISTRY_SEARCH
INSPECT_SUPPLEMENTARY_DATA
INSPECT_TARGET_VALUES
CHECK_T_IND_COMPATIBILITY
REVISE_G_J_S_I
REOPEN_TARGET_DISCOVERY
SELECT_A_TARGET
GRANT_EMPIRICAL_CREDIT
```

If a less restrictive route is justified, the audit may authorize only a **separately preregistered downstream design operation**.

## 8. Outcome derivation

Exactly one outcome must be selected:

```text
A = STRICT_SUSPENSION_RULE_UPHELD
B = STRICT_SUSPENSION_RULE_OVERREACHES__SAME_CANDIDATE_RESPONSE_BLIND_SEARCH_EXPANSION_MAY_BE_DESIGNED_PROSPECTIVELY
C = STRICT_SUSPENSION_RULE_OVERREACHES__ONLY_NEW_CANDIDATE_IDENTITY_MAY_REOPEN_SEARCH
D = UNRESOLVED_AT_FROZEN_RECORD_SCOPE
```

### Outcome A requires

The frozen earlier standards must positively imply that search-feasibility feedback alone contaminates subsequent search-architecture design, or that independent provenance is the only available way to control target-family discretion.

### Outcome B requires

All of the following:

```text
EXACT_SEARCH_UNIVERSE_NOT_PART_OF_FROZEN_G_J_S_I = YES
NO_RESPONSE_OR_DEPENDENCE_INFORMATION_USED = YES
PRIOR_RECORD_ALREADY_PERMITTED_LATER_EXPANSION_BY_NEW_PREREGISTRATION = YES
TARGET_FAMILY_PRIVILEGE_CAN_BE_CONTROLLED_WITHOUT_INDEPENDENT_ORIGIN = YES
NEW_SEARCH_CAN_BE_FROZEN_BEFORE_EXECUTION = YES
```

### Outcome C requires

The strict independent-origin barrier is excessive, but changing the discovery architecture changes a constitutive part of `I` or target-selection identity enough to require a new candidate ID.

### Outcome D requires

The frozen record leaves a load-bearing identity or contamination question genuinely indeterminate.

## 9. Supersession discipline

A result against OP-0112 does not delete or rewrite it.

If Outcome B or C is reached:

```text
OP_0112_HISTORICAL_RESULT = PRESERVED
OP_0112_STRICT_RESUMPTION_RULE = SUPERSEDED_PROSPECTIVELY_AT_DEFINED_SCOPE
NO_RETROACTIVE_TARGET_SEARCH = YES
NO_RETROACTIVE_EMPIRICAL_CREDIT = YES
```

The post-FCP trigger reassessment also remains valid under the then-controlling OP-0112 rule; it is not retroactively called an error.

## 10. Output boundary

The adjudication commit may create exactly:

```text
audits/PGH1_EMPIRICAL_SEARCH_SUSPENSION_ADVERSARIAL_AUDIT_0_1_0.md
handoffs/PGH1_EMPIRICAL_SEARCH_SUSPENSION_ADVERSARIAL_AUDIT_HANDOFF_0_1_0.md
```

No current-state/navigation mutation occurs inside the scientific audit.

## 11. Stop boundary

Stop after the methodological verdict and handoff are frozen.

Even if Outcome B or C is reached, no new target-search architecture may be designed or executed until a separate prospective operation is opened.

Truth over PGH includes testing whether our safeguards protect scientific integrity or merely protect the hypothesis.
