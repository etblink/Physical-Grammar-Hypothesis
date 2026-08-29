# PGH-1 Post-Kp Successor Plurality Representation and Target-Free Selection Gate — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_POST_KP_SUCCESSOR_PLURALITY_REPRESENTATION_AND_TARGET_FREE_SELECTION_GATE
REGISTRY_ID = PGH-OP-0082
CANONICAL_BASE = 11cdd5ef3682f1ffb467d355e6b0f2203d0ad265
ADMITTED_PACKAGES = [PGH-OBJ-0041,PGH-OBJ-0042,PGH-OBJ-0043,PGH-OBJ-0044,PGH-OBJ-0045]
TARGET_DISCOVERY = FORBIDDEN
TARGET_METADATA = FORBIDDEN
EMPIRICAL_DATA = FORBIDDEN
Kp_FIT_OR_COMPATIBILITY_SELECTION = FORBIDDEN
NEW_SOURCE_SEARCH = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Determine, before any target discovery:

1. how many distinct **formal grammar classes** are represented by the five admitted candidate packages;
2. how many distinct **physical candidate packages `C=(G,J,S,I)`** remain after permitted representation transformations;
3. whether any scientifically substantive, target-free, non-result-directed principle selects a unique package;
4. if not, what plurality-preserving empirical governance must be frozen before target discovery.

## Representation rule

A transformation counts as a mere representation change for a candidate package only if it preserves the complete candidate identity, not merely the abstract graph.

For candidate package `C=(G,J,S,I)`, a proposed equivalence must preserve:

```text
FORMAL_MODEL_CLASS_UP_TO_ISOMORPHISM
BRIDGE_J_UP_TO_ALLOWED_RELABELLING
SCOPE_S
INSTANTIATION_ROLE_PREDICATES_IN_I
EMPIRICAL_PREDICTION_SET
FAILURE_CONDITIONS
```

A permutation of abstract variable names may be a formal representation transformation of `G` while **not** being a representation transformation of the physical package if `I` assigns noninterchangeable empirical roles such as earliest/upstream, intermediate, and latest/downstream.

## Formal-class hypotheses to test

The five packages appear to use only two abstract graph/Markov motifs:

```text
G_NC = THREE_NODE_NONCOLLIDER_PATH_CLASS__FORMALLY_REPRESENTED_BY_PGH_GRAM_0008
G_COL = THREE_NODE_COLLIDER_PATH_CLASS__PGH_GRAM_0009
```

This gate must verify rather than merely assume that collapse.

## Physical-package hypotheses to test

The package-level restrictions are:

```text
PGH-OBJ-0041 -> A ⟂ C
PGH-OBJ-0042 -> A ⟂ B | C
PGH-OBJ-0043 -> A ⟂ B
PGH-OBJ-0044 -> B ⟂ C | A
PGH-OBJ-0045 -> B ⟂ C
```

The gate must determine whether any permitted candidate-level representation transformation maps one restriction/role embedding to another while preserving the ordered empirical role predicates in `I`.

## Candidate selection criteria

A scientifically substantive target-free selector must be independently meaningful and must not merely impose an arbitrary total ordering.

Potential selectors to adjudicate:

### S1 — formal description length / primitive count

Does one package have strictly lower structural complexity under a representation-disciplined measure already justified by the project?

A tiny syntactic difference or notation-dependent string length receives no scientific privilege.

### S2 — symmetry / automorphism / invariance

Does one package have a uniquely stronger representation-invariant symmetry property that is both candidate-internal and scientifically relevant?

Symmetry may not be promoted from mathematical elegance to physical selection without justification.

### S3 — compatibility with ordered role architecture

Does the metadata-defined earliest/intermediate/latest role architecture itself select a separator or collider position without importing causal, dynamical, or Markov semantics?

Temporal order alone may not be treated as proof that arrows are physical causes or that the intermediate role is the separator.

### S4 — primitive-grammar economy / prior canonical doctrine

Does prior target-free PGH formal work privilege either noncollider or collider structure under the primitive grammar standard?

Historical use of `PGH-GRAM-0008` does not count as privilege after its failed physical instantiation.

### S5 — known-negative elimination

Known Kp failure may eliminate any package that logically entails the already-canonical failed restriction. It may not provide positive preference among candidates not already contradicted by the frozen historical result.

### S6 — administrative deterministic tie-break

A lexicographic or other arbitrary deterministic rule may be acceptable for **operational scheduling** but does not constitute scientific evidence, unique grammar selection, or stronger prior probability.

The gate must decide whether an operational tie-break is preferable to carrying the plurality into a common-target multi-candidate program.

## Multiple-candidate empirical option

If no scientific selector qualifies and the packages share a common admissible target interface, the gate may recommend—but not yet construct—a common-target multi-candidate empirical protocol.

Such a later protocol would need to freeze before target discovery:

```text
CANDIDATE_FAMILY = FIXED
COMMON_TARGET_SELECTION_RULE = CANDIDATE_OUTCOME_NEUTRAL
MULTIPLE_HYPOTHESIS_OR_FAMILYWISE_DECISION_RULE = FIXED
CANDIDATE_SPECIFIC_TESTS = FIXED_AT_APPROPRIATE_STAGE
SEQUENTIAL_REPLACEMENT_AFTER_FAILURE = FORBIDDEN_WITHOUT_NEW_PREREGISTRATION
KNOWN_KP_POSITIVE_CREDIT = ZERO
```

No target may be discovered inside this gate.

## Outcome space

```text
A = PLURALITY_COLLAPSES_TO_ONE_PHYSICALLY_EQUIVALENT_CANDIDATE__UNIQUE_PACKAGE_RETAINS_ADMISSION

B = MULTIPLE_PHYSICALLY_DISTINCT_PACKAGES_REMAIN__A_SCIENTIFIC_TARGET_FREE_SELECTOR_QUALIFIES__FREEZE_ONE_WINNER__STOP_BEFORE_TARGET_DISCOVERY

C = FORMAL_GRAMMAR_CLASSES_COLLAPSE_BUT_MULTIPLE_PHYSICALLY_DISTINCT_C_PACKAGES_REMAIN__NO_SCIENTIFIC_TARGET_FREE_SELECTOR_QUALIFIES__RETAIN_PLURALITY__ROUTE_TO_COMMON_TARGET_MULTIPLICITY_GOVERNANCE

D = ALL_PACKAGES_REPRESENTATION_EQUIVALENT_ONLY_AFTER_USING_PHYSICALLY_UNJUSTIFIED_ROLE_PERMUTATIONS__DO_NOT_COLLAPSE__SELECTION_BLOCKED

E = SPECIFIC_FORMAL_OR_SOURCE_GAP_BLOCKS_REPRESENTATION_ADJUDICATION
```

## Hard constraints

```text
HC1_NO_TARGET_DISCOVERY_OR_METADATA
HC2_NO_EMPIRICAL_FIT_SELECTION
HC3_NO_KP_POSITIVE_SELECTION
HC4_NO_PHYSICAL_CAUSATION_ASSIGNED_TO_DAG_ARROWS
HC5_NO_SYMMETRY_ELEGANCE_AS_PHYSICAL_EVIDENCE_BY_ITSELF
HC6_NO_ADMINISTRATIVE_TIE_BREAK_MISLABELED_AS_SCIENTIFIC_SELECTION
HC7_NO_POSTHOC_COLLAPSE_THAT_CHANGES_I_ROLE_SEMANTICS
HC8_FCP_UNCHANGED
```

## Required outputs

```text
audits/PGH1_POST_KP_SUCCESSOR_PLURALITY_REPRESENTATION_AND_TARGET_FREE_SELECTION_GATE_0_1_0.md
research/formalizations/PGH1_POST_KP_SUCCESSOR_PLURALITY_EQUIVALENCE_MAP_0_1_0.md
handoffs/PGH1_POST_KP_SUCCESSOR_PLURALITY_REPRESENTATION_AND_TARGET_FREE_SELECTION_GATE_HANDOFF_0_1_0.md
```

No navigation surfaces are modified in this scientific operation.

## Commit topology

```text
COMMIT_1 = PREREGISTRATION_ONLY
COMMIT_2 = ADJUDICATION_EQUIVALENCE_MAP_AND_HANDOFF
EXACT_COMMITS = 2
```

## Stop boundary

```text
STOP_BEFORE_TARGET_DISCOVERY
STOP_BEFORE_MULTI_CANDIDATE_EMPIRICAL_PROTOCOL_CONSTRUCTION
STOP_BEFORE_NEW_SOURCE_SEARCH
```
