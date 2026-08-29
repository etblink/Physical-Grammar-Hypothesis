# CURRENT STATE

## Project status

```text
PROJECT = Physical Grammar Hypothesis
PROJECT_CLASS = SPECULATIVE_FOUNDATIONAL_RESEARCH
CURRENT_PHASE = PGH-0_CONCEPTUAL_FORMULATION
FCP_RELATIONSHIP = INDEPENDENT_INCUBATION
FCP_FRAMEWORK_STATUS = NONE
CANONICAL_EFFECT_ON_FCP = NONE
SOURCE_BOUND_STATUS = NOT_YET_SOURCE_BOUND
EMPIRICAL_STATUS = UNESTABLISHED
```

## Current strongest hypothesis

The strongest version presently under consideration is:

> There exists a compact, representation-independent generative grammar whose well-formed structures or derivations, modulo physical equivalence, correspond to the physically possible structures of the universe, with the fundamental laws of physics arising from that grammar rather than from an additional independently imposed dynamical rule set.

Schematic form:

\[
P \cong W(G)/{\sim}.
\]

This is a research hypothesis, not an established result.

## Current null hypothesis

```text
H0 = GRAMMATICAL_STRUCTURE_IS_A_FEATURE_OF_REPRESENTATION_AND_INDEPENDENT_PHYSICAL_LAWS_REMAIN_NECESSARY
```

The project has not yet produced evidence sufficient to prefer PGH over this null hypothesis.

## Current candidate primitive reduction

The initial conceptual list was:

```text
DISTINCTION
BOUNDARY
COMPOSITION
TRANSFORMATION
EQUIVALENCE
```

The current reduction candidate is:

```text
DISTINGUISH
COMPOSE
IDENTIFY
```

Current status:

```text
DISTINGUISH = CANDIDATE_PRIMITIVE_NOT_FORMALLY_FIXED
COMPOSE = CANDIDATE_PRIMITIVE_NOT_FORMALLY_FIXED
IDENTIFY = CANDIDATE_PRIMITIVE_NOT_FORMALLY_FIXED
BOUNDARY = CANDIDATE_DERIVED_NOT_PROVEN
TRANSFORMATION = CANDIDATE_DERIVED_NOT_PROVEN
CONTEXT = CANDIDATE_DERIVED_NOT_PROVEN
```

No claim has yet been established that three primitives are minimal, sufficient, independent, or even jointly coherent.

## What has been established

Only the following methodological points are currently accepted project state:

1. A useful PGH must be stronger than the statement that physics can be encoded formally.
2. A candidate grammar must face a no-smuggling audit.
3. A nontrivial candidate grammar must exclude something otherwise describable.
4. A candidate deep grammar must be tested for representation invariance.
5. A successful grammar should exhibit generative compression.
6. Formal resemblance to known physics is not itself a physical derivation.
7. Failed derivations must be preserved.
8. PGH remains independent of FCP at this stage.

## What has NOT been established

```text
MINIMAL_GRAMMAR = NONE
FORMAL_GRAMMAR = NONE
PHYSICAL_GRAMMAR_FOUND = NO
NONTRIVIAL_PHYSICAL_CONSTRAINT_DERIVED = NO
CONSERVATION_DERIVED = NO
SYMMETRY_DERIVED = NO
LOCALITY_DERIVED = NO
CAUSALITY_DERIVED = NO
TIME_DERIVED = NO
SPACE_DERIVED = NO
GEOMETRY_DERIVED = NO
QUANTUM_STRUCTURE_DERIVED = NO
PROBABILITY_DERIVED = NO
EMPIRICAL_PREDICTION = NONE
EMPIRICAL_DISCRIMINATOR = NONE
NATURAL_LANGUAGE_IDENTITY = NOT_ESTABLISHED
```

Earlier conversational observations that interface matching may resemble conservation, derivational order may resemble time, or contextual equivalence may resemble gauge/representation invariance are retained only as **analogy candidates**. They are not derivations.

## Anti-import firewall

Until separately derived or explicitly introduced as an assumption, do not import:

- space or spacetime;
- time;
- locality;
- causal order;
- probability;
- quantum theory;
- geometry or dimension;
- particles or fields;
- energy, momentum, mass, or charge;
- action principles or equations of motion;
- conservation laws;
- Hilbert-space structure;
- category theory as fundamental ontology;
- information or computation as fundamental ontology.

## Current nontriviality burden

A candidate grammar must survive the tests in `NONTRIVIALITY_TESTS.md`, especially:

```text
NO_SMUGGLING
NONUNIVERSAL_EXCLUSION
REPRESENTATION_INVARIANCE
SEMANTIC_LOAD_AUDIT
GENERATIVE_COMPRESSION
INDEPENDENT_CONSEQUENCE
```

No candidate currently has `PASS` status on the complete test set.

## Failed derivations

```text
FAILED_DERIVATION_COUNT = 0_FORMALLY_LOGGED
```

Several tempting analogies have been deliberately withheld from derivation status, so they are not counted as failed derivations yet.

## Open questions

Canonical open-question identities are now maintained in `meta/PGH_OPEN_QUESTION_REGISTRY.jsonl`.

The opening set remains:

1. `PGH-Q-0001` — Can `DISTINGUISH` be defined without presupposing a set of already individuated objects?
2. `PGH-Q-0002` — Can `COMPOSE` be defined without already importing boundaries, types, or causal ordering?
3. `PGH-Q-0003` — Can `IDENTIFY` be reduced to compositional indistinguishability in all contexts, making it derived rather than primitive?
4. `PGH-Q-0004` — Can boundary arise from the conditions under which composition is partial?
5. `PGH-Q-0005` — Can transformation be represented entirely as a compositional relation rather than a separate primitive?
6. `PGH-Q-0006` — Does any minimal grammar produce a genuine exclusion rather than a definitional tautology?
7. `PGH-Q-0007` — What kind of semantics map is weak enough not to carry the physics itself?
8. `PGH-Q-0008` — What would count as faithful translation between genuinely different mathematical surface languages?
9. `PGH-Q-0009` — Is “physical possibility” the right target object, or does that phrase already import too much modal/physical structure?
10. `PGH-Q-0010` — Can PGH be distinguished from structural realism, computation, category-theoretic foundations, informational reconstructions, and other nearby programs once source work begins?

## Scalability and navigation foundation

The repository now has a lightweight scalable navigation/provenance spine.

```text
PGH_REPOSITORY_SCALABILITY_AND_NAVIGATION_FOUNDATION = CANONICALLY_COMPLETE
SCIENTIFIC_CHANGE_FROM_INFRASTRUCTURE = NONE
HYPOTHESIS_CHANGE_FROM_INFRASTRUCTURE = NONE
PRIMITIVE_ADJUDICATION_FROM_INFRASTRUCTURE = NONE
NEW_DERIVATION_FROM_INFRASTRUCTURE = NONE
NEW_SOURCE_SEARCH_FROM_INFRASTRUCTURE = NONE
```

Authority remains:

```text
GIT = PROVENANCE_AUTHORITY
CANONICAL_MARKDOWN_ARTIFACTS = RESEARCH_AND_GOVERNANCE_AUTHORITY
STRUCTURED_NAVIGATION_LAYER = DERIVED_NAVIGATION_ONLY
```

Current navigation counts:

```text
OPERATION_RECORD_COUNT = 3
RESEARCH_OBJECT_RECORD_COUNT = 8
OPEN_QUESTION_RECORD_COUNT = 10
OPEN_QUESTION_COUNT = 10
```

Active working grammar identity:

```text
ACTIVE_CANDIDATE_GRAMMAR = PGH-GRAM-0001
```

This identity names the still-unfixed `{DISTINGUISH, COMPOSE, IDENTIFY}` candidate shell. It does not qualify it.

## Next recommended task

```text
NEXT_RECOMMENDED_TASK = PGH0_MINIMAL_GRAMMAR_CHALLENGE
TASK_STATUS = RECOMMENDED_NOT_STARTED
NEXT_OPERATION_AUTHORIZED = NO
```

Question:

> Starting only from the candidate operations DISTINGUISH, COMPOSE, and IDENTIFY, define the weakest coherent formal structure possible and determine whether any primitive is redundant and whether any nontrivial exclusion follows before physical interpretation is added.

The task should stop before claiming a physical consequence unless the nontriviality tests have been explicitly passed.

## Structured current-state capsule

<!-- PGH_CURRENT_STATE_CAPSULE_BEGIN -->
```json
{
  "capsule_schema_version": "0.1.0",
  "project": "Physical Grammar Hypothesis",
  "current_phase": "PGH-0_CONCEPTUAL_FORMULATION",
  "canonical_hypothesis": "HYPOTHESIS.md",
  "active_candidate_grammar": "PGH-GRAM-0001",
  "current_handoff": "handoffs/PGH_REPOSITORY_SCALABILITY_AND_NAVIGATION_FOUNDATION_HANDOFF_0_1_0.md",
  "source_bound_status": "NOT_YET_SOURCE_BOUND",
  "fcp_relationship": "INDEPENDENT_INCUBATION",
  "next_recommended_operation": "PGH0_MINIMAL_GRAMMAR_CHALLENGE",
  "next_operation_authorized": false,
  "open_question_count": 10,
  "do_not_assume": [
    "DISTINGUISH_COMPOSE_IDENTIFY_IS_MINIMAL",
    "BOUNDARY_IS_DERIVED",
    "TRANSFORMATION_IS_DERIVED",
    "DERIVATIONAL_ORDER_IS_PHYSICAL_TIME",
    "BOUNDARY_MATCHING_IS_CONSERVATION",
    "CONTEXTUAL_EQUIVALENCE_IS_GAUGE_SYMMETRY",
    "COMPOSITIONALITY_IMPLIES_LOCALITY",
    "CATEGORY_THEORY_IS_THE_PRIVILEGED_PGH_FORMALISM",
    "PGH_HAS_EMPIRICAL_SUPPORT",
    "PGH_HAS_ANY_CANONICAL_EFFECT_ON_FCP"
  ]
}
```
<!-- PGH_CURRENT_STATE_CAPSULE_END -->

## Continuation rule

A successor research instance should read, at minimum:

1. `governance/PGH_REPOSITORY_OPENING_CHARTER_0_1_0.md`
2. `governance/PGH_ARTIFACT_AND_PROVENANCE_POLICY_0_1_0.md`
3. `governance/PGH_NAVIGATION_AND_HANDOFF_POLICY_0_1_0.md`
4. `CURRENT_STATE.md`
5. `HYPOTHESIS.md`
6. `PRIMITIVES.md`
7. `NONTRIVIALITY_TESTS.md`
8. `RESEARCH_LOG.md`
9. `meta/PGH_CANONICAL_INDEX.json`
10. the current handoff named above.

Do not infer missing progress from phase names.

Do not protect PGH from failure.
