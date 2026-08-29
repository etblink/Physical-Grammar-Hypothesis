# PGH-1 Post-Kp Physical Scope / Domain-Selection Gate — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_POST_KP_PHYSICAL_SCOPE_DOMAIN_SELECTION_GATE
REGISTRY_ID = PGH-OP-0068
CANONICAL_BASE = d3b4a7e0d98e94e60fbff72cbb3a8c95e31fbde8
FIRST_EMPIRICAL_TARGET = PGH-OBJ-0037
FIRST_EMPIRICAL_FAILURE = PGH-FAIL-0035
TESTED_GRAMMAR = PGH-GRAM-0008
SEMANTIC_BRIDGE = PGH-OBJ-0035
OPEN_SCOPE_QUESTION = PGH-Q-0028
NEW_EMPIRICAL_DATA = NONE
NEW_TARGET_SEARCH = NONE
NEW_SOURCE_SEARCH = NONE
FCP_EFFECT = NONE
```

## Purpose

Determine whether the physical domain or scope in which `PGH-GRAM-0008` is supposed to apply can be fixed **without using the Kp failure to choose that scope**.

This operation occurs only after the first empirical Kp result and its interpretation adjudication became canonical. It therefore treats post-result scope freedom as dangerous by default.

The gate is not allowed to ask:

> Where does the grammar happen to work?

It asks:

> What physical scope, if any, had already been earned independently of the observed Kp conditional-dependence result, and what consequences follow if no such scope existed?

## Frozen epistemic boundary

The first Kp result remains canonical:

```text
KP_INSTANTIATION = REFUTED_AT_KP_TARGET
TARGET_SELECTION_VALIDITY = RETAINED
FORMAL_GRAMMAR_THEOREM = RETAINED
PGH_GRAM_0008_PHYSICAL_VALIDATION = NONE
```

This gate may not reinterpret the failed target as invalid merely because it failed.

## Pre-result scope-evidence cutoff

A scope selector may count as **pre-existing** only if it is stated or logically forced by versioned material canonical no later than:

```text
PRE_RESULT_CUTOFF = e3a0291b2d546c1d426151ce6b8cb33f291e8937
```

That cutoff is the canonical statistical preregistration commit, before the Kp values were analyzed.

Post-result artifacts may be used only to identify the already accepted claim boundary and the newly exposed scope burden. They may not supply a selector and then have that selector treated as though it existed before Kp.

## Frozen evidence set

Primary admissible pre-result evidence:

```text
HYPOTHESIS.md
research/grammars/PGH_GRAMMAR_THREE_NODE_SPARSE_MARKOV_CHAIN_CANDIDATE_0_1_0.md
audits/PGH1_R2B_CAUSAL_WIRING_PRIMITIVE_GRAMMAR_CANDIDACY_GATE_0_1_0.md
research/formalizations/PGH1_CAUSAL_WIRING_MODEL_CLASS_PHYSICAL_BRIDGE_SCHEMA_0_1_0.md
audits/PGH1_R2B_CAUSAL_WIRING_PHYSICAL_SEMANTIC_FIREWALL_GATE_0_1_0.md
research/derivations/PGH_DERIVATION_MODEL_CLASS_RESTRICTION_TRANSFER_0_1_0.md
research/formalizations/PGH1_EMPIRICAL_TARGET_SELECTION_PROTOCOL_0_1_0.md
audits/PGH1_EMPIRICAL_INSTANTIATION_TARGET_SELECTION_PREREGISTRATION_GATE_0_1_0.md
empirical/PGH1_FIRST_EMPIRICAL_INSTANTIATION_TARGET_FREEZE_0_1_0.md
governance/PGH1_FIRST_EMPIRICAL_KP_CONDITIONAL_INDEPENDENCE_ANALYSIS_PREREGISTRATION_0_1_0.md
```

Post-result boundary-only evidence:

```text
audits/PGH1_POST_FIRST_EMPIRICAL_KP_RESULT_ADJUDICATION_0_1_0.md
research/failures/PGH_FAIL_FIRST_EMPIRICAL_KP_PGH_GRAM_0008_INSTANTIATION_0_1_0.md
```

No external literature search is authorized in this gate.

## Scope-selector qualification standard

A candidate physical scope rule qualifies as **pre-existing and non-result-directed** only if all pass:

```text
S1_PRE_RESULT_PROVENANCE
S2_NO_KP_VALUE_OR_DEPENDENCE_INPUT
S3_NON_EXTENTIONAL_SCOPE_DESCRIPTION
S4_NOT_EQUIVALENT_TO_REQUIRING_THE_PREDICTED_CI
S5_NOT_SELECTED_BECAUSE_IT_EXCLUDES_KP
S6_PHYSICALLY_OR_SEMANTICALLY_INTERPRETABLE_WITHOUT_TARGET_FIT
S7_CLASSIFIES_TARGETS_USING_INFORMATION_AVAILABLE_BEFORE_DEPENDENCE_ANALYSIS
S8_DOES_NOT_IMPORT_AN_INDEPENDENT_PHYSICAL_LAW_THAT_DOES_THE_SELECTIVE_WORK
```

A rule fails S4 if it is equivalent to formulations such as:

```text
SYSTEMS_THAT_ARE_MARKOV_OF_ORDER_ONE
SYSTEMS_THAT_SATISFY_A_INDEPENDENT_C_GIVEN_B
SYSTEMS_WELL_FIT_BY_THE_SPARSE_CHAIN
```

when those properties are used to decide domain membership.

## Distinction between retroactive scope and future hypothesis revision

This gate must distinguish:

```text
PRE_KP_SCOPE_OF_EXISTING_CANDIDATE
```

from:

```text
NEW_POST_KP_SCOPE_RULE_FOR_A_FUTURE_REVISED_CANDIDATE
```

A scope rule first invented after the Kp failure cannot retroactively rescue the frozen Kp instantiation or be credited as though it belonged to the original physical candidacy of `PGH-GRAM-0008`.

A scientifically motivated new scope rule may later define a **new hypothesis/candidate identity**, but only under a separately preregistered operation with explicit post-failure provenance.

## Frozen candidate scope routes

The adjudication must test at least these routes:

### R0 — no physical scope beyond formal model class

`PGH-GRAM-0008` remains purely formal and the bridge supplies testability only after a separate empirical instantiation is chosen.

Question: does this leave the physical application domain underdetermined?

### R1 — empirical-architecture eligibility as scope

Use only the metadata/architecture criteria frozen in `PGH-OBJ-0036`.

Question: do those criteria define a physical scope, or only a nonleaking **target-selection procedure**? If treated as scope, does the already selected Kp target necessarily remain inside it?

### R2 — graph as physical causal/dependency scope

Restrict application to systems independently known to realize the chain `A -> B -> C`.

Question: was such physical graph semantics qualified before Kp, or would this import a stronger semantic/causal assumption that the canonical firewall explicitly declined to grant?

### R3 — domain-specific physical sector

Restrict the grammar to a named physical field, process class, or scale.

Question: was any such sector specified before Kp for reasons independent of the observed result?

### R4 — result-defined / Markov-fit scope

Restrict application to systems that satisfy or approximately satisfy the predicted conditional independence.

```text
DISPOSITION = REJECT_BY_PREREGISTRATION
```

This is circular target selection.

### R5 — strong-PGH universal reading

Ask whether the umbrella strong hypothesis or the role assigned to `PGH-GRAM-0008` requires a broad/universal physical scope rather than a domain-limited one.

The gate must not silently promote this small grammar candidate to the complete grammar of the universe if canonical artifacts never made that identification.

## Outcome space

```text
A = PRE_KP_SCOPE_RULE_EXISTS_AND_INCLUDES_KP__THE_KP_FAILURE_REMAINS_ADVERSE_WITHIN_THAT_SCOPE__NO_RESULT_DIRECTED_TARGET_SWITCH

B = PRE_KP_SCOPE_RULE_EXISTS_BUT_CONFLICTS_WITH_THE_CANONICAL_KP_TARGET_FREEZE__PROVENANCE_OR_PROTOCOL_INCONSISTENCY_REQUIRES_SEPARATE_RESOLUTION__KP_FAILURE_IS_NOT_ERASED

C = NO_PRE_KP_PHYSICAL_SCOPE_SELECTOR_QUALIFIES__THE_EXISTING_CANDIDATE_IS_PHYSICALLY_SCOPE_UNDERDETERMINED__KP_FAILURE_REMAINS_FOR_THE_FROZEN_INSTANTIATION__ANY_NEW_SCOPE_RULE_IS_A_POST_KP_HYPOTHESIS_REVISION

D = CANONICAL_COMMITMENTS_REQUIRE_A_BROAD_SCOPE_CONTAINING_KP__THE_KP_FAILURE_COUNTS_DIRECTLY_AGAINST_PGH_GRAM_0008_PHYSICAL_CANDIDACY_AT_THAT_BROAD_SCOPE__NO_SECOND_TARGET_RESCUE
```

No outcome authorizes a second empirical target inside this operation.

## Required adversarial questions

The adjudication must explicitly answer:

```text
Q1_WHAT_WAS_ACTUALLY_FIXED_BEFORE_KP
Q2_WHAT_INFORMATION_CLASSIFIED_KP_AS_A_VALID_TEST_OPPORTUNITY
Q3_WAS_THAT_CLASSIFIER_A_SCOPE_RULE_OR_ONLY_A_TARGET_SELECTION_RULE
Q4_WAS_ANY_PHYSICAL_DOMAIN_OF_PGH_GRAM_0008_NAMED_PRE_RESULT
Q5_WOULD_A_PROPOSED_SCOPE_HAVE_CLASSIFIED_KP_THE_SAME_WAY_BEFORE_THE_RESULT
Q6_DOES_THE_SCOPE_RULE_CARRY_THE_PHYSICAL_LAW_OR_GRAPH_SEMANTICS
Q7_IS_THE_RULE_UNIVERSAL_ENOUGH_TO_BE_MEANINGFUL_BUT_SELECTIVE_ENOUGH_NOT_TO_BE_TARGET_SHOPPING
Q8_IF_A_NEW_RULE_IS_NEEDED_DOES_IT_REQUIRE_A_NEW_CANDIDATE_IDENTITY
```

## Forbidden moves

```text
NO_SECOND_TARGET_SEARCH
NO_C9_OR_GOES_REPLACEMENT
NO_KP_LAG_PHASE_OR_BIN_SEARCH
NO_KP_CAUSAL_EXPLANATION_SEARCH
NO_GRAPH_REPAIR
NO_SCOPE_DEFINED_BY_CI_SUCCESS
NO_SCOPE_DEFINED_BY_MARKOV_FIT
NO_POST_KP_RULE_RELABELED_AS_PRE_KP
NO_EXTERNAL_SOURCE_SEARCH
NO_FCP_CHANGE
```

## Required outputs

A result commit may add only:

```text
audits/PGH1_POST_KP_PHYSICAL_SCOPE_DOMAIN_SELECTION_GATE_0_1_0.md
research/formalizations/PGH1_POST_KP_PHYSICAL_SCOPE_DOMAIN_SELECTION_SCHEMA_0_1_0.md
handoffs/PGH1_POST_KP_PHYSICAL_SCOPE_DOMAIN_SELECTION_GATE_HANDOFF_0_1_0.md
```

If and only if the adjudication establishes a new preserved failure, one additional file under `research/failures/` may be added with the next unused failure ID.

## Commit topology

```text
COMMIT_1 = PREREGISTRATION_ONLY
COMMIT_2 = ADJUDICATION_AND_HANDOFF_ONLY
EXACT_COMMITS = 2
```

## Stop boundary

After Commit 2 qualification:

```text
STOP_BEFORE_SECOND_TARGET_SELECTION
STOP_BEFORE_NEW_GRAMMAR_DESIGN
STOP_BEFORE_NEW_SCOPE_RULE_ENGINEERING
STOP_BEFORE_EXTERNAL_SOURCE_INTAKE
```
