# PGH-1 R2B SG4 Structural Process Constraint Adjudication — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_R2B_SG4_STRUCTURAL_PROCESS_CONSTRAINT_ADJUDICATION
REGISTRY_ID = PGH-OP-0058
CANONICAL_BASE = e98ed7b42e881b0ead04e42904ce443bd09ec7e2
FROZEN_DISTINCT_ACCEPTED_SOURCES = 85
SG4_SOURCE_INTAKE = PGH-OP-0057
BRIDGE_CANDIDATE = PGH-OBJ-0028
SEMANTIC_FIREWALL = PGH-OBJ-0029
MODEL_CLASS_SCHEMA = PGH-OBJ-0030
UNIVERSAL_REALIZABILITY = PGH-DER-0028
CURRENT_R2B_FAILURE = PGH-FAIL-0029
CANDIDATE_GRAMMARS = PGH-GRAM-0006; PGH-GRAM-0007
NEW_SOURCE_SEARCH = FORBIDDEN
EMPIRICAL_RESPONSE_DATA = FORBIDDEN
EMPIRICAL_MODEL_FIT = FORBIDDEN
NEW_PHYSICAL_CLAIM = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Use only the frozen 85-source PGH corpus and already accepted formal results to decide whether any SG4 structural-process mechanism earns a separate preregistered formal test against the current bridge-response universal-realizability failure.

This operation is source-bound adjudication and sequencing. It may classify a mechanism family for later testing. It may not add causal wiring, Markov axioms, bridge equations, response kernels, or a new physical grammar.

## Frozen mechanism families

```text
M1 = NORMALIZATION_BY_MARKOV_AFFINE_OR_TERMINAL_STRUCTURE
M2 = CAUSAL_DAG_FACTORIZATION_AND_CONDITIONAL_INDEPENDENCE
M3 = NETWORK_TOPOLOGY_OR_SOURCE_INDEPENDENCE_CORRELATION_CONSTRAINTS
M4 = CONDITIONING_DISINTEGRATION_AND_ABSTRACT_PROBABILISTIC_CALCULUS
```

## Fixed accounting layers

Every mechanism must keep these distinct:

```text
D = DOCTRINE_OR_PROCESS_CALCULUS
W = CAUSAL_GRAPH_WIRING_SIGNATURE_OR_NETWORK_TOPOLOGY
K = LOCAL_CHANNEL_KERNEL_BOX_OR_RESOURCE_ASSIGNMENTS
E = EMPIRICAL_PARAMETER_OR_RESPONSE_DATA
```

A structural consequence may receive later grammar-derived credit only for information following from frozen `D` and separately preregistered structural input `W`. Information in `K` or `E` may not be credited to the grammar.

## Locked adjudication tests

### S1 — response-class reduction

Ask whether the mechanism can, at fixed declared structural input, exclude a proper nontrivial subset of the response structures that `PGH-DER-0028` showed were otherwise universally realizable.

### S2 — input-location audit

Record exactly which selectivity comes from `D`, `W`, `K`, and `E`.

A mechanism fails immediate candidacy if its purported restriction is actually contained in a freely chosen local kernel, empirical table, or target-specific equation.

### S3 — pre-target fixation

A later formal test is justified only if its structural input can be stated before seeing the desired response law and can expose countermodels.

This does not require the structure to be meta-derived from nothing; the primitive-grammar stopping rule remains controlling.

### S4 — current-bridge compatibility

Ask whether the mechanism can be tested against the existing typed-anchor / aggregate-output bridge architecture without interpreting coproduct summands, morphism values, relational membership, or stochastic weights as physical outcomes by definition.

### S5 — family-universality control

Distinguish:

```text
FIXED_STRUCTURAL_INPUT
```

from

```text
UNRESTRICTED_FAMILY_OF_ALL_STRUCTURAL_INPUTS.
```

For causal/DAG mechanisms, test conceptually whether allowing all DAGs—including sufficiently connected/complete DAGs—can restore arbitrary dependency structure. If yes, causal selectivity belongs partly to the chosen graph and must be charged there.

### S6 — minimality / sequencing

If more than one family deserves later testing, prefer the least-loaded family that can genuinely reduce universal realizability, while preserving stronger families as later controls.

This is sequencing, not a physical likelihood ranking.

## Frozen family-specific questions

### M1 — normalization

The SG4 corpus establishes that Markov/terminal structure can encode normalization across a model class.

Test whether this reduces the response class relevant to `PGH-DER-0028`, given that the finite-stochastic control already ranged over normalized conditional distributions.

### M2 — causal/DAG factorization

The SG4 corpus establishes that fixed causal structures can imply factorization, conditional independence, and d-separation consequences across multiple probabilistic model classes.

Test whether a graph-parametric formal gate is justified while keeping the DAG itself visible as selective input.

### M3 — network/source-independence constraints

The SG4 corpus establishes that particular network topologies and source-independence assumptions can imply response-level restrictions stronger than ordinary conditional independence and sometimes across generalized probabilistic theories.

Test whether this is more input-loaded than M2 because topology/resource-independence assumptions are themselves substantive.

### M4 — conditioning/disintegration calculus

The SG4 corpus establishes mature structural operations for conditioning, disintegration, Bayesian inversion, and statistical comparison.

Test whether these operations alone restrict the primitive bridge response class, or primarily provide calculus once a probabilistic model is supplied.

## Outcome space

```text
A = AT_LEAST_ONE_SG4_MECHANISM_CAN_BE_ATTACHED_TO_THE_CURRENT_BRIDGE_AS_AN_IMMEDIATE_FORMAL_CONSTRAINT_CANDIDATE_WITHOUT_NEW_SELECTIVE_STRUCTURAL_INPUT__A_DIRECT_BRIDGE_CONSTRAINT_GATE_IS_JUSTIFIED

B = SG4_CONFIRMS_REAL_MODEL_CLASS_CONSTRAINT_MECHANISMS_BUT_NO_IMMEDIATE_RESPONSE_RESTRICTION_FOLLOWS_FROM_THE_CURRENT_BRIDGE_ALONE__A_LEAST_LOADED_PARAMETRIC_CAUSAL_OR_STRUCTURAL_GATE_IS_JUSTIFIED_WITH_ITS_SELECTIVE_INPUT_EXPLICITLY_CHARGED

C = THE_85_SOURCE_CORPUS_IS_INSUFFICIENT_TO_SEPARATE_STRUCTURAL_CONSEQUENCE_FROM_LOCAL_MODEL_DATA_FOR_THE_RELEVANT_MECHANISMS__A_NARROW_SOURCE_GAP_MUST_BE_IDENTIFIED

D = NONE_OF_M1_TO_M4_MATERIALLY_BEAR_ON_THE_CURRENT_UNIVERSAL_REALIZABILITY_FAILURE__RETURN_TO_NON_SG4_DISCOVERY
```

No outcome satisfies R2B or establishes physical meaning.

## Expected classification discipline

The adjudication must not infer:

```text
NORMALIZATION = COMPLETE_RESPONSE_LAW
DAG = PHYSICAL_CAUSAL_STRUCTURE
D_SEPARATION = UNIVERSAL_PHYSICAL_LAW
NETWORK_INDEPENDENCE = GIVEN_BY_PGH
MARKOV_CATEGORY = PHYSICAL_GRAMMAR
LOCAL_KERNEL = GRAMMAR_DERIVED
```

## Required outputs

Commit 2 may add only:

```text
audits/PGH1_R2B_SG4_STRUCTURAL_PROCESS_CONSTRAINT_ADJUDICATION_0_1_0.md
research/formalizations/PGH1_SG4_STRUCTURAL_PROCESS_CONSTRAINT_ADJUDICATION_SCHEMA_0_1_0.md
research/failures/PGH_FAIL_STRUCTURAL_PROCESS_CONSTRAINT_INPUT_RELOCATION_0_1_0.md
handoffs/PGH1_R2B_SG4_STRUCTURAL_PROCESS_CONSTRAINT_ADJUDICATION_HANDOFF_0_1_0.md
```

Expected identities if earned:

```text
PGH-OBJ-0032 = SG4_STRUCTURAL_PROCESS_CONSTRAINT_ADJUDICATION_SCHEMA
PGH-FAIL-0030 = STRUCTURAL_PROCESS_CONSTRAINT_INPUT_RELOCATION
```

## Commit topology

```text
COMMIT_1_MESSAGE = Preregister PGH-1 R2B SG4 structural process constraint adjudication
COMMIT_2_MESSAGE = Adjudicate PGH-1 R2B SG4 structural process constraints
EXACT_COMMITS = 2
```

## Hard stops

```text
DO_NOT_SEARCH_NEW_SOURCES
DO_NOT_ADD_CAUSAL_GRAPH_TO_EXISTING_GRAMMAR
DO_NOT_ADD_MARKOV_OR_CAUSAL_AXIOMS_TO_EXISTING_GRAMMAR
DO_NOT_ADD_RESPONSE_EQUATIONS
DO_NOT_SELECT_A_GRAPH_BY_EMPIRICAL_FIT
DO_NOT_SELECT_LOCAL_KERNELS
DO_NOT_CALL_A_SOURCE_MECHANISM_PGH_DERIVED
DO_NOT_DECLARE_R2B_SATISFIED
DO_NOT_MAKE_EMPIRICAL_PREDICTIONS
DO_NOT_CHANGE_FCP
```
