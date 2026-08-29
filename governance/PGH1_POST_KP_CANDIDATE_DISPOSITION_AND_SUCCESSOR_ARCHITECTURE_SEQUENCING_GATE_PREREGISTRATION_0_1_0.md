# PGH-1 Post-Kp Candidate Disposition and Successor-Architecture Sequencing Gate — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_POST_KP_CANDIDATE_DISPOSITION_AND_SUCCESSOR_ARCHITECTURE_SEQUENCING_GATE
REGISTRY_ID = PGH-OP-0070
CANONICAL_BASE = 491cab16fa5fa399603c911073f5c0421d1a4db2
PREVIOUS_SCIENTIFIC_GATE = PGH-OP-0068
TESTED_GRAMMAR = PGH-GRAM-0008
FIRST_EMPIRICAL_FAILURE = PGH-FAIL-0035
POST_RESULT_SCOPE_FAILURE = PGH-FAIL-0036
NEW_EMPIRICAL_DATA = FORBIDDEN
SECOND_TARGET_SEARCH = FORBIDDEN
NEW_SOURCE_SEARCH = FORBIDDEN
SUCCESSOR_CONSTRUCTION = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Choose the scientifically appropriate disposition of unchanged `PGH-GRAM-0008` after its valid Kp instantiation failed and after `PGH-OP-0068` established that no pre-Kp physical-domain selector had been qualified.

This is a sequencing gate, not a successor-design gate.

It may decide what class of work should come next. It may not construct the next grammar, invent a new physical scope rule, inspect another empirical target, or search for literature that makes one route look better.

## Controlling facts frozen before this gate

```text
KP_TARGET_VALIDITY = RETAINED
KP_VERDICT = REFUTED_AT_KP_TARGET
PGH_GRAM_0008_FORMAL_STATUS = RETAINED
PGH_GRAM_0008_PHYSICAL_VALIDATION = NONE
PRE_KP_PHYSICAL_SCOPE_SELECTOR = NONE_QUALIFIED
UNCHANGED_CANDIDATE_SECOND_TARGET_PREDICTIVE_CREDIT = BLOCKED
R2B = UNSATISFIED
STRONG_PGH_CONFIRMED = NO
EVERY_POSSIBLE_PGH_REFUTED = NO
```

## Decision criteria and weights

Weights are sequencing priorities only. They are not scientific evidence, probabilities of PGH truth, or a scalar substitute for scientific reasoning. A route may be rejected despite a favorable weighted profile if it violates a hard methodological boundary.

```text
C1_EVIDENTIAL_INTEGRITY_AND_ANTI_RESCUE = 0.30
C2_FUTURE_PREDICTIVE_LEGITIMACY_AND_FALSIFIABILITY = 0.25
C3_EXPLANATORY_PROGRESS_TOWARD_STRONG_PGH_AND_R2B = 0.20
C4_AUXILIARY_FREEDOM_AND_PARSIMONY = 0.15
C5_PROVENANCE_CLARITY_REVERSIBILITY_AND_RESEARCH_OPTION_VALUE = 0.10
TOTAL = 1.00
```

### C1 — evidential integrity / anti-rescue

Prefer routes that preserve the Kp failure, avoid result-conditioned narrowing, and keep post-Kp additions visibly post-Kp.

### C2 — future predictive legitimacy / falsifiability

Prefer routes that allow a future candidate to state its physical scope and empirical consequences before target outcomes are known.

### C3 — explanatory progress toward strong PGH / R2B

Prefer routes that address the unresolved physical-selection burden rather than accumulate formally selective structures with no earned physical domain.

### C4 — auxiliary freedom / parsimony

Penalize routes that add scope predicates, semantic qualifications, graph changes, or target-specific exceptions merely because the first target failed.

### C5 — provenance clarity / reversibility / option value

Prefer routes that preserve useful formal results, make candidate identity changes explicit, and leave future work auditable without pretending continuity where the hypothesis changed.

## Routes to adjudicate

### R1 — continue unchanged PGH-GRAM-0008 to a second empirical target

```text
OLD_CANDIDATE_IDENTITY = RETAINED
SECOND_TARGET = LATER_ALLOWED
NEW_SCOPE_RULE = NONE
```

This route receives no credit merely because another metadata-eligible target exists. It must survive the OP-0068 finding that predictive credit for a second target under the unchanged identity is blocked.

### R2 — retire unchanged PGH-GRAM-0008 from physical-target testing and immediately design a scope-bearing successor

```text
OLD_CANDIDATE_PHYSICAL_TESTING = RETIRED
FORMAL_CONTROL_STATUS = RETAINED
NEXT_ROUTE = DIRECT_SUCCESSOR_ARCHITECTURE_DESIGN
```

This route must confront the fact that physical scope would be introduced after Kp. A future successor is allowed, but the gate must decide whether immediate successor design is scientifically mature or too exposed to post-result scope engineering.

### R3 — retire unchanged PGH-GRAM-0008 from physical-target testing and return upstream to grammar/bridge/scope architecture discovery before selecting a successor

```text
OLD_CANDIDATE_PHYSICAL_TESTING = RETIRED
FORMAL_CONTROL_STATUS = RETAINED
NEXT_ROUTE = UPSTREAM_PROSPECTIVE_ARCHITECTURE_DISCOVERY
SUCCESSOR_IDENTITY = NOT_YET_SELECTED
```

This route preserves formal lessons from `PGH-GRAM-0008` while reopening the physical-selection problem under a mandatory prospective-scope requirement.

### R4 — close the current strong-PGH research program at this scope

```text
OLD_CANDIDATE_PHYSICAL_TESTING = RETIRED
NEXT_SUCCESSOR_WORK = NONE
PROJECT_STATUS = STOP_OR_ARCHIVE_AT_CURRENT_SCOPE
```

This is the truth-over-PGH termination control. It must be selected if no non-post-hoc route remains scientifically meaningful. It may not be rejected merely because continued research is interesting.

## Hard constraints

```text
HC1_KP_MAY_NOT_BE_RECLASSIFIED_OUT_OF_SCOPE
HC2_NO_SECOND_TARGET_OR_TARGET_METADATA_MAY_BE_INSPECTED
HC3_NO_NEW_SCOPE_PREDICATE_MAY_BE_INVENTED_IN_THIS_GATE
HC4_NO_SUCCESSOR_GRAMMAR_MAY_BE_CONSTRUCTED_IN_THIS_GATE
HC5_NO_GRAPH_REPAIR_OR_COMPLETE_DAG_PROMOTION
HC6_NO_EXTERNAL_SOURCE_SEARCH
HC7_NO_KP_REANALYSIS_OR_LAG_BIN_ROLE_EXPLORATION
HC8_NO_ROUTE_GETS_CREDIT_FOR_PRESERVING_PGH_AS_SUCH
HC9_FORMAL_RESULTS_MAY_BE_RETAINED_EVEN_IF_PHYSICAL_CANDIDACY_IS_RETIRED
HC10_FCP_REMAINS_UNCHANGED
```

## Outcome space

```text
A = CONTINUE_UNCHANGED_PGH_GRAM_0008_TO_FURTHER_PHYSICAL_TARGETS
B = RETIRE_UNCHANGED_PGH_GRAM_0008_FROM_PHYSICAL_TESTING__ROUTE_DIRECTLY_TO_EXPLICITLY_NEW_SCOPE_BEARING_SUCCESSOR_DESIGN
C = RETIRE_UNCHANGED_PGH_GRAM_0008_FROM_PHYSICAL_TESTING__RETAIN_AS_FORMAL_CONTROL__RETURN_UPSTREAM_TO_PROSPECTIVE_GRAMMAR_BRIDGE_SCOPE_ARCHITECTURE_DISCOVERY_BEFORE_SUCCESSOR_SELECTION
D = CLOSE_OR_ARCHIVE_STRONG_PGH_RESEARCH_AT_CURRENT_SCOPE__NO_SUCCESSOR_WORK_JUSTIFIED
E = INCONCLUSIVE_SEQUENCING__SPECIFIC_NONEMPIRICAL_INFORMATION_GAP_BLOCKS_DISPOSITION
```

## Adjudication discipline

The final result must provide:

1. route-by-route assessment under C1-C5;
2. explicit hard-constraint screening;
3. a qualitative or approximate relative weighting of live routes;
4. a non-scalar scientific rationale for the selected outcome;
5. exact disposition of `PGH-GRAM-0008` as formal object versus physical candidate;
6. exact next-operation class, if any;
7. a stop before successor construction or new target search.

## Claim ceiling

This gate can decide research sequencing and candidate disposition only.

It cannot establish:

```text
STRONG_PGH_TRUE
STRONG_PGH_FALSE_GLOBALLY
A_SUCCESSOR_GRAMMAR
A_PHYSICAL_SCOPE_RULE
A_SECOND_EMPIRICAL_PREDICTION
R2B_SATISFIED
```

## Required outputs

After preregistration, the adjudication commit may add only:

```text
audits/PGH1_POST_KP_CANDIDATE_DISPOSITION_AND_SUCCESSOR_ARCHITECTURE_SEQUENCING_GATE_0_1_0.md
handoffs/PGH1_POST_KP_CANDIDATE_DISPOSITION_AND_SUCCESSOR_ARCHITECTURE_SEQUENCING_GATE_HANDOFF_0_1_0.md
```

No navigation surfaces are modified inside the scientific operation.

## Commit topology

```text
COMMIT_1 = PREREGISTRATION_ONLY
COMMIT_2 = ADJUDICATION_AND_HANDOFF_ONLY
EXACT_COMMITS = 2
```

## Stop boundary

```text
STOP_BEFORE_SUCCESSOR_CONSTRUCTION
STOP_BEFORE_SCOPE_RULE_DESIGN
STOP_BEFORE_SOURCE_INTAKE
STOP_BEFORE_SECOND_TARGET_DISCOVERY
STOP_BEFORE_EMPIRICAL_ANALYSIS
```
