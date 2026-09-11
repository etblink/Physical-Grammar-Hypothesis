# PGH-1 Post-FCP Independent Trigger Reassessment — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_POST_FCP_INDEPENDENT_TRIGGER_REASSESSMENT
OPERATION_CLASS = READ_ONLY_CLOSED_RECORD_TRIGGER_ADJUDICATION
CANDIDATE_PACKAGE = PGH-OBJ-0052
CANONICAL_PGH_BASE = 4ef3308bbb0a71515a0331f3f00c72d18d599813
CANONICAL_PGH_BASE_TREE = 403d26c3dde89aefe6fab9705bb00deb66544dac
ACTIVE_TARGET_SEARCH_AT_OPEN = SUSPENDED
TARGET_SELECTED_AT_OPEN = NO
TARGET_VALUES_ACCESSED_AT_OPEN = NO
NEW_WEB_SEARCH = FORBIDDEN
NEW_REGISTRY_SEARCH = FORBIDDEN
NEW_DATASET_SEARCH = FORBIDDEN
NEW_SOURCE_INTAKE = FORBIDDEN
RESPONSE_DATA_ACCESS = FORBIDDEN
```

## 1. Purpose

Canonical PGH operation `PGH-OP-0112` suspended active empirical target search for `PGH-OBJ-0052` after the prior finite discovery operation found no eligible target and no independently justified broader target universe was already in place.

That suspension permits later resumption only through independently originated events:

```text
T_PGH_1 = INDEPENDENTLY_ENCOUNTERED_NEW_PUBLIC_INTERFACE
T_PGH_2 = INDEPENDENT_GENERAL_TARGET_DISCOVERY_METHOD
```

Subsequent FCP work independently encountered new scientific literature and adjudicated PGH for framework taxonomy. The present operation asks only whether **already-existing records produced for those non-target purposes** now satisfy either PGH resumption trigger.

This operation does not search for a target. It tests whether a target-search trigger already exists in the closed record.

## 2. Controlling prior PGH rule

The source-bound prior result is:

```text
PGH1_POST_NETWORK_SOURCE_NO_TARGET_DISCOVERY_RESEARCH_SEQUENCING_GATE = CANONICAL
PGH_OP = PGH-OP-0112
OUTCOME = B__R2_QUALIFIES__SUSPEND_ACTIVE_EMPIRICAL_TARGET_SEARCH_FOR_PGH_OBJ_0052
ACTIVE_TARGET_SEARCH = SUSPENDED
TARGET_SELECTED = NO
TARGET_VALUES_ACCESSED = NO
```

Frozen controlling artifact:

```text
audits/PGH1_POST_NETWORK_SOURCE_NO_TARGET_DISCOVERY_RESEARCH_SEQUENCING_GATE_0_1_0.md
BLOB = 1340bf90b7ce5882dc1f4bce2292c05b61bb99ad
```

The exact candidate package remains:

```text
research/candidates/PGH1_POST_KP_NETWORK_SOURCE_SUCCESSOR_PACKAGE_0_1_0.md
BLOB = 1846e8a176aed14341a829ca6e1e60c71f438afd
```

Nothing in this reassessment may relax or reinterpret `PGH-OP-0112` merely because direct empirical testing would be scientifically desirable.

## 3. Frozen post-suspension record universe

The reassessment may inspect only the following independently generated records already known before adjudication begins.

### PGH canonical controls

1. `PGH-OBJ-0052` candidate package — exact `I`, target tie-break, and contamination rules.
2. `PGH-OP-0112` no-target sequencing gate — exact resumption conditions.

### FCP records created for framework-taxonomy purposes, not PGH target discovery

3. `frameworks/pgh/FCP_PGH_STAGE1_SOURCE_INTAKE_0_1_0.md`
   - blob `a3ffa304b83568e33da5dd279157d14e3ef9f4f1`
   - includes 17 PGH proposal/provenance records, 10 external primary sources, and four FCP identity controls.

4. `audits/FCP_PGH_STAGE2_A_H_TAXONOMY_ADJUDICATION_0_1_0.md`
   - blob `250286852700a91ffeda5adba097af41e92d0203`
   - establishes Outcome B and preserves no empirical target/test.

5. `handoffs/FCP_PGH_STAGE2_A_H_TAXONOMY_GATE_HANDOFF_0_1_0.md`
   - blob `e3b7124ee818d4c814510b0e8acfd6286ee22e57`
   - records taxonomy firewalls and empirical non-adjudication.

6. `governance/POST_PGH_STAGE2_SCIENTIFIC_SEQUENCING_CORRECTIVE_0_1_0.md`
   - blob `13d7f82a13a8985c8260fa2ec24c14ba7195ad3a`
   - identifies the PGH suspension as controlling and routes here.

FCP canonical state at freeze:

```text
FCP_CANONICAL_MAIN = e7dd1473e5ab89b4657d33e9b05fe90ae2ae7a65
```

No later source, webpage, dataset description, repository, registry, supplementary file, citation trail, or search result may enter this adjudication.

## 4. Trigger T-PGH-1 — independently encountered public interface

An FCP record may qualify T-PGH-1 only if the information already frozen in the allowed record establishes all material `I`-eligibility fields without follow-up target-directed retrieval.

Required fields:

```text
PUBLIC_OR_AUDITABLE_EVENT_LEVEL_ACCESS = YES
VERSIONED_OR_STABLY_IDENTIFIED_AUTHORITY = YES
REPEATED_JOINT_RECORD_INDEX = YES
AT_LEAST_THREE_DISTINCT_NATIVE_BINARY_RECORD_FIELDS = YES
SELECTED_FIELDS_JOINTLY_OBSERVED_PER_RECORD = YES
MISSINGNESS_OR_VALIDITY_CODES_DOCUMENTED = YES
```

Additional provenance requirements:

```text
ENCOUNTER_ORIGIN_INDEPENDENT_OF_PGH_TARGET_SEARCH = YES
RESPONSE_VALUES_USED_TO_QUALIFY = NO
DEPENDENCE_INFORMATION_USED_TO_QUALIFY = NO
TARGET_BEHAVIOR_USED_TO_QUALIFY = NO
```

Allowed T-PGH-1 verdicts:

```text
QUALIFIED_TRIGGER
NOT_ESTABLISHED
DISQUALIFIED_BY_PROVENANCE
```

A paper describing an experiment is not automatically an eligible public interface. A theoretical construction is not an empirical interface. Missing eligibility metadata may not be filled by new search inside this operation.

## 5. Trigger T-PGH-2 — independent general target-discovery method

A frozen record may qualify T-PGH-2 only if it already establishes a concrete target-discovery universe or method whose origin is independent of the need to find a PGH target.

Required properties:

```text
METHOD_EXISTS_AS_IDENTIFIABLE_ARTIFACT_OR_EXTERNAL_PROGRAM = YES
PURPOSE_BROADER_THAN_OBTAINING_A_PGH_TARGET = YES
PROVENANCE_INDEPENDENT_OF_PRIOR_PGH_ZERO_TARGET_RESULT = YES
FINITE_OR_RULE_GOVERNED_UNIVERSE = YES
ORDERING_AND_STOPPING_RULE = ESTABLISHED
PGH_RESPONSE_BEHAVIOR_NOT_USED = YES
```

Allowed T-PGH-2 verdicts:

```text
QUALIFIED_TRIGGER
NOT_ESTABLISHED
DISQUALIFIED_BY_PROVENANCE
```

Generic intuition that registries or schema-first search could be useful is insufficient.

## 6. Source-by-source trigger accounting

Every one of the ten FCP external primary sources in the frozen Stage-1 intake must receive one trigger-accounting row with at least:

```text
SOURCE_ID
SOURCE_ROLE_IN_FCP
PHYSICAL_EXPERIMENT_OR_THEORY
PUBLIC_EVENT_LEVEL_INTERFACE_ESTABLISHED
STABLE_DATA_AUTHORITY_ESTABLISHED
REPEATED_JOINT_INDEX_ESTABLISHED
THREE_NATIVE_BINARY_FIELDS_ESTABLISHED
JOINT_OBSERVATION_ESTABLISHED
MISSINGNESS_VALIDITY_DOCUMENTED
INDEPENDENT_ENCOUNTER_PROVENANCE
T_PGH_1_EFFECT
T_PGH_2_EFFECT
AUTHORIZED_INFERENCE
FORBIDDEN_FOLLOWUP
```

The four FCP identity-control records do not need target-interface rows because they were framework controls rather than candidate empirical interfaces, but they must be explicitly reported as `NO_TRIGGER_ROLE`.

The 17 PGH proposal/provenance records remain candidate-definition/provenance controls and cannot become post-suspension independent triggers by repetition.

## 7. Decision rule

```text
IF T_PGH_1 = QUALIFIED_TRIGGER:
    ACTIVE_TARGET_SEARCH_MAY_REOPEN_ONLY_IN_SEPARATELY_PREREGISTERED_OPERATION = YES

ELSE IF T_PGH_2 = QUALIFIED_TRIGGER:
    TARGET_DISCOVERY_METHOD_PROVENANCE_REVIEW_MAY_OPEN_SEPARATELY = YES

ELSE:
    ACTIVE_TARGET_SEARCH = REMAINS_SUSPENDED
    NEW_TARGET_SEARCH = NO
    TARGET_SELECTED = NO
    EMPIRICAL_TEST = UNINSTANTIATED
```

A qualified trigger does not itself select a target or grant access to response data.

## 8. FCP taxonomy firewall

The FCP result has no authority to weaken PGH empirical rules.

```text
FCP_OUTCOME_B => PGH_TARGET_SEARCH_REOPENED = NO
FCP_CRITERION_C_PASS => PGH_TARGET_SEARCH_REOPENED = NO
FCP_QUANTUM_NETWORK_COUNTERBOUNDARIES => ACTIVE_PGH_REFUTATION = NO
FCP_TAXONOMY_RESULT => POSITIVE_PGH_EMPIRICAL_CREDIT = NONE
```

Conversely, this trigger reassessment does not reopen FCP taxonomy.

## 9. Negative-history firewall

```text
PGH_GRAM_0008_KP_REFUTATION = PRESERVED
FAILED_PREDECESSOR_SUPPORTS_SUCCESSOR = NO
Kp_POSITIVE_SUCCESSOR_CREDIT = ZERO
HURDAT2_POSITIVE_SUCCESSOR_CREDIT = ZERO
POST_FCP_TRIGGER_REASSESSMENT_MAY_REVISE_G_J_S_I = NO
```

## 10. Exact output boundary

The adjudication commit may create exactly:

```text
audits/PGH1_POST_FCP_INDEPENDENT_TRIGGER_REASSESSMENT_0_1_0.md
handoffs/PGH1_POST_FCP_INDEPENDENT_TRIGGER_REASSESSMENT_HANDOFF_0_1_0.md
```

It may not modify the candidate package, target protocol, source register, prior failures, prior empirical artifacts, or FCP repository.

## 11. Stop boundary

After the trigger verdict is frozen, stop.

If no trigger qualifies, active target search remains suspended and no web/data search follows.

If a trigger qualifies, a separately preregistered downstream operation is required before any target search or data access.

Truth over PGH. A hard-to-test hypothesis does not earn weaker prospectivity rules.
