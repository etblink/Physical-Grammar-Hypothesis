# PGH-1 R2B Compositional Stochastic/Causal Process Source Intake — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_R2B_COMPOSITIONAL_STOCHASTIC_CAUSAL_PROCESS_SOURCE_INTAKE
REGISTRY_ID = PGH-OP-0057
CANONICAL_BASE = 8f1fe09cdb94536107b53981a48966a36f0edb85
SOURCE_GAP = SG4_COMPOSITIONAL_STOCHASTIC_AND_CAUSAL_PROCESS_CONSTRAINTS
PARENT_DISCOVERY = PGH-OBJ-0031
CURRENT_DISTINCT_FROZEN_ACCEPTED_SOURCES = 70
SCIENTIFIC_ADJUDICATION = FORBIDDEN
NEW_GRAMMAR = FORBIDDEN
NEW_BRIDGE_CONSTRAINT = FORBIDDEN
EMPIRICAL_FIT = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Close SG4 at representative source-landscape scope by identifying primary or standard sources that show how compositional probabilistic/causal structure can constrain classes of processes without specifying every transition table or response distribution individually.

The operation is source intake only.

It may characterize what sources establish, but it may not select a Markov category, causal theory, Bayesian-network formalism, effectus, or other framework as the PGH grammar or physical bridge.

## Search lanes

### SG4A — Markov categories and synthetic probability

Prioritize sources introducing or developing categorical structures in which stochastic maps, copy/delete structure, conditional independence, sufficient statistics, or related probability concepts are expressed compositionally.

### SG4B — causal theories and compositional Bayesian networks

Prioritize sources where causal graph/process structure generates factorization, dependency, or correlation constraints while local conditional channels remain separate model data.

### SG4C — disintegration, conditional independence, normalization, and probabilistic process calculus

Prioritize sources showing how probability-theoretic operations or constraints arise structurally/diagrammatically rather than from one fixed numerical model.

### SG4D — effectus or adjacent probabilistic process frameworks

Include representative sources only when they add a distinct mechanism for organizing probabilistic/classical/quantum process structure or tests/predicates relevant to bridge constraints.

### SG4E — structural-vs-model-specific probability firewall

Actively seek sources or source-supported examples that make the distinction:

```text
STRUCTURAL_PROCESS_AXIOMS
!=
LOCAL_CHANNEL_OR_KERNEL_VALUES
```

The intake must record whether a formalism constrains the composition/factorization of models while leaving local process parameters as inputs.

## Source priority

Prefer, in order:

1. foundational primary papers introducing a mechanism;
2. standard peer-reviewed developments establishing key theorems;
3. authoritative monographs or substantial surveys for lane mapping;
4. arXiv/preprint sources only when foundational and no stronger published version is available or when needed to establish exact chronology/content.

Reject weak summaries, tertiary pages, duplicate versions, and papers whose relevance is only that they use probability categorically without addressing structural process constraints.

## Candidate-source tests

For every candidate, record:

```text
SOURCE_ID
CITATION
YEAR
LOCATOR_OR_DOI_OR_ARXIV
AUTHORITY_CLASS
LANE
MECHANISM
WHAT_THE_SOURCE_ESTABLISHES
WHAT_IT_DOES_NOT_ESTABLISH_FOR_PGH
DISPOSITION
DUPLICATE_STATUS
```

## PGH relevance tests

A source is materially relevant only if it helps answer at least one:

1. Can compositional structure impose response/process constraints across a model class?
2. Which constraints arise from wiring/causal/Markov structure rather than local numerical kernels?
3. How are conditional independence, normalization, disintegration, or causal compatibility represented structurally?
4. Which information remains free model data even after the compositional structure is fixed?
5. Can the mechanism be stated without assuming a target physical response table?

## No-smuggling source firewall

The landscape must distinguish:

```text
STRUCTURAL_FACTORISATION_OR_COMPOSITION_CONSTRAINT
LOCAL_CHANNEL_PARAMETER_INPUT
CAUSAL_GRAPH_OR_WIRING_INPUT
EMPIRICAL_PROBABILITY_TABLE
PHYSICAL_PRINCIPLE_ASSUMPTION
```

A paper is not evidence for PGH law exhaustion merely because it derives consequences from a DAG, Markov structure, causality axiom, or probabilistic calculus. Those inputs must remain visible.

## Deduplication

Deduplicate against all 70 existing accepted PGH sources by author/title/DOI/arXiv/locator and by known alternate publication versions.

A reused existing source may be cited for cross-lane control but must not increase the distinct accepted-source count.

## Saturation standard

Representative saturation requires:

- accepted coverage of all material SG4 lanes or an explicit justified empty lane;
- at least one foundational mechanism source for SG4A and SG4B;
- at least one source explicitly useful for the structural-vs-local-model-data distinction;
- late searches returning mainly duplicates, specialized extensions, or sources that do not change the mechanism taxonomy.

This is not an exhaustive bibliography.

## Outcome space

```text
A = SG4_IS_CLOSED_AT_REPRESENTATIVE_SCOPE_AND_THE_CORPUS_SUPPORTS_A_CLEAR_TAXONOMY_OF_STRUCTURAL_PROCESS_CONSTRAINTS_VERSUS_FREE_MODEL_DATA__NO_FORMAL_SELECTION_IS_MADE

B = SG4_IS_PARTIALLY_CLOSED_BUT_ONE_OR_MORE_MATERIAL_SUBLANES_REMAIN_UNDERREPRESENTED__NO_CONSTRAINT_SELECTION_IS_JUSTIFIED

C = THE_SEARCH_SHOWS_SG4_IS_NOT_DISTINCT_FROM_ALREADY_FROZEN_L9_OR_OTHER_CORPUS_LANES__THE_PROPOSED_GAP_IS_REJECTED

D = SOURCE_ACCESS_OR_AUTHORITY_IS_INSUFFICIENT_FOR_A_REPRESENTATIVE_FREEZE
```

## Required outputs

Commit 2 may add only:

```text
sources/PGH1_R2B_COMPOSITIONAL_STOCHASTIC_CAUSAL_SOURCE_REGISTER_0_1_0.md
sources/PGH1_R2B_COMPOSITIONAL_STOCHASTIC_CAUSAL_SOURCE_LANDSCAPE_0_1_0.md
sources/PGH1_R2B_COMPOSITIONAL_STOCHASTIC_CAUSAL_SOURCE_SELECTION_AUDIT_0_1_0.md
handoffs/PGH1_R2B_COMPOSITIONAL_STOCHASTIC_CAUSAL_PROCESS_SOURCE_INTAKE_HANDOFF_0_1_0.md
```

## Commit topology

```text
COMMIT_1_MESSAGE = Preregister PGH-1 R2B compositional stochastic causal source intake
COMMIT_2_MESSAGE = Freeze PGH-1 R2B compositional stochastic causal source corpus
EXACT_COMMITS = 2
```

## Hard stops

```text
DO_NOT_SELECT_MARKOV_CATEGORIES_AS_PGH_GRAMMAR
DO_NOT_SELECT_CAUSAL_THEORY_AS_PGH_GRAMMAR
DO_NOT_ADD_BRIDGE_EQUATIONS
DO_NOT_USE_EMPIRICAL_FIT_TO_RANK_SOURCES
DO_NOT_DECLARE_R2B_SATISFIED
DO_NOT_MAKE_EMPIRICAL_PREDICTIONS
DO_NOT_CHANGE_FCP
```
