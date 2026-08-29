# Physical Grammar Hypothesis

> **Status:** Speculative foundational research — independent incubation
>
> **Current phase:** `PGH-0_CONCEPTUAL_FORMULATION`
>
> **FCP relationship:** None at present. This repository is deliberately quarantined from the Foundational Convergence Program (FCP); it has no FCP framework status and no canonical effect on FCP.

## Purpose

The **Physical Grammar Hypothesis (PGH)** asks whether the deepest laws of physical possibility may be better understood as a compact, representation-independent **generative grammar**: a set of primitives and rules whose well-formed derivations, modulo physical equivalence, are exactly the physically possible structures of the universe.

The project begins from a deliberately stronger question than the generic claim that “physics can be represented by a formal language.” The research target is whether a nontrivial grammar can **generate and exclude physical possibilities without simply encoding known physical laws inside its rules**.

A schematic strong form is:

\[
P \cong W(G)/{\sim}
\]

where:

- `G` is a candidate fundamental grammar;
- `W(G)` is the class of structures or derivations well formed under that grammar;
- `~` identifies physically equivalent expressions;
- `P` is the class of physically possible states, processes, or histories.

At this stage, this is a **hypothesis under construction**, not an accepted theory of physics.

## Current research question

The opening PGH-0 challenge is:

> Can a minimal grammar built from something like **DISTINGUISH, COMPOSE, IDENTIFY** imply even one nontrivial restriction on physical possibility without importing space, time, causality, probability, geometry, quantum mechanics, dynamics, or another known physical law by hand?

If the answer is no, that failure is a substantive project result.

## Epistemic rules

This repository follows a small set of strict research rules:

1. **No-smuggling rule.** Renaming a known physical law as a “grammar rule” is not an explanation.
2. **Representation-invariance rule.** A candidate deep grammar must not depend on one arbitrary mathematical surface language.
3. **Exclusion rule.** A nontrivial grammar must rule out something that is otherwise mathematically describable; a grammar that generates everything explains nothing.
4. **Generative-compression rule.** The grammar should be materially simpler than the space of structures it generates.
5. **Failure conditions first.** Candidate principles should be accompanied by conditions under which they would fail.
6. **Failed derivations are first-class results.** Circular, trivial, or smuggled derivations are preserved rather than silently replaced.
7. **No premature physics claims.** Formal resemblance to gauge symmetry, conservation, locality, causal order, quantum theory, or other physics is not itself a derivation of those structures.
8. **No premature FCP import.** Nothing in this repository alters FCP unless a later, separately justified process explicitly establishes a relationship.

## Authority model

PGH now uses a lightweight authority hierarchy designed to scale:

```text
GIT = PROVENANCE_AUTHORITY
CANONICAL_MARKDOWN_ARTIFACTS = RESEARCH_AND_GOVERNANCE_AUTHORITY
STRUCTURED_NAVIGATION_LAYER = DERIVED_NAVIGATION_ONLY
```

If navigation metadata conflicts with a canonical research artifact, the canonical artifact wins.

## Repository map

### Current research authority

- [`CURRENT_STATE.md`](CURRENT_STATE.md) — exact present research state, live uncertainties, and next recommended test.
- [`HYPOTHESIS.md`](HYPOTHESIS.md) — weak, strong, and identity forms of PGH, including failure conditions.
- [`PRIMITIVES.md`](PRIMITIVES.md) — candidate minimal primitives and the anti-import firewall.
- [`NONTRIVIALITY_TESTS.md`](NONTRIVIALITY_TESTS.md) — tests distinguishing a genuine explanatory grammar from relabeling or universal encoding.
- [`RESEARCH_LOG.md`](RESEARCH_LOG.md) — chronological decisions, failures, and conceptual changes.

### Governance

- [`governance/PGH_REPOSITORY_OPENING_CHARTER_0_1_0.md`](governance/PGH_REPOSITORY_OPENING_CHARTER_0_1_0.md)
- [`governance/PGH_ARTIFACT_AND_PROVENANCE_POLICY_0_1_0.md`](governance/PGH_ARTIFACT_AND_PROVENANCE_POLICY_0_1_0.md)
- [`governance/PGH_NAVIGATION_AND_HANDOFF_POLICY_0_1_0.md`](governance/PGH_NAVIGATION_AND_HANDOFF_POLICY_0_1_0.md)
- [`governance/PGH_BRANCH_AND_REF_LIFECYCLE_POLICY_0_1_0.md`](governance/PGH_BRANCH_AND_REF_LIFECYCLE_POLICY_0_1_0.md)

### Scalable research layout

- [`research/`](research/) — versioned derivations, failures, formalizations, models, and representation tests as they are created.
- [`sources/`](sources/) — reserved source-intake area; PGH is explicitly not yet source-bound.
- [`handoffs/`](handoffs/) — durable human + machine-readable continuation artifacts.

### Derived navigation

- [`meta/PGH_CANONICAL_INDEX.json`](meta/PGH_CANONICAL_INDEX.json)
- [`meta/PGH_OPERATION_REGISTRY.jsonl`](meta/PGH_OPERATION_REGISTRY.jsonl)
- [`meta/PGH_RESEARCH_OBJECT_REGISTRY.jsonl`](meta/PGH_RESEARCH_OBJECT_REGISTRY.jsonl)
- [`meta/PGH_OPEN_QUESTION_REGISTRY.jsonl`](meta/PGH_OPEN_QUESTION_REGISTRY.jsonl)
- [`meta/PGH_NAVIGATION_SCHEMA_0_1_0.json`](meta/PGH_NAVIGATION_SCHEMA_0_1_0.json)
- [`tools/pgh_navigation.py`](tools/pgh_navigation.py)

The navigation layer is derived orientation, not scientific authority.

## Stable identities

PGH uses durable IDs:

```text
PGH-OP-####    operations
PGH-Q-####     open questions
PGH-OBJ-####   general research objects
PGH-DER-####   derivations
PGH-FAIL-####  failed derivations
PGH-GRAM-####  candidate grammars
```

The numeric suffix is an identity only. It is not a score, ranking, or phase level.

## Failed derivations and assumption ancestry

A failed derivation remains preserved.

Substantive derivations should expose:

```text
PRIMITIVE_DEPENDENCIES
RULE_DEPENDENCIES
LEMMA_DEPENDENCIES
SEMANTIC_ASSUMPTIONS
PHYSICAL_ASSUMPTIONS
SOURCE_DEPENDENCIES
```

This is intended to make hidden physical imports traceable rather than relying on prose memory.

## Project phases

The phase names are descriptive checkpoints, not claims of success:

- **PGH-0 — Conceptual formulation:** define the hypothesis and minimal anti-triviality conditions.
- **PGH-1 — Minimal primitives:** determine the weakest candidate primitive set.
- **PGH-2 — Formal grammar:** specify a precise rule system without importing physics.
- **PGH-3 — Nontrivial derivations:** test whether the grammar entails substantive restrictions.
- **PGH-4 — Representation-invariance tests:** test candidate invariants across genuinely different mathematical formulations.
- **PGH-5 — Physical/falsifiable consequences:** ask whether any derived restriction reaches empirical or observational content.

Advancement through these labels is not automatic.

## Relationship to linguistics

“Grammar” is initially used in an abstract sense: well-formedness, composition, equivalence, contextual admissibility, transformation, reference, and generativity. The project does **not** currently claim that the contingent syntax of any human language is identical to physical law.

A much stronger linguistic–physical identity hypothesis may eventually be formulated, but it is not assumed at project opening.

## Navigation check

From a normal checkout:

```text
python -B tools/pgh_navigation.py check
```

Derived index regeneration requires an explicit logical research baseline:

```text
python -B tools/pgh_navigation.py build --baseline-commit <commit>
```

Markdown parsers are expected to tolerate CRLF checkouts; machine-readable JSON/JSONL/Python files are pinned to LF.

## Current status

```text
PROJECT = Physical Grammar Hypothesis
PROJECT_CLASS = SPECULATIVE_FOUNDATIONAL_RESEARCH
FCP_RELATIONSHIP = INDEPENDENT_INCUBATION
FCP_FRAMEWORK_STATUS = NONE
CANONICAL_EFFECT_ON_FCP = NONE
CURRENT_PHASE = PGH-0_CONCEPTUAL_FORMULATION
EMPIRICAL_STATUS = UNESTABLISHED
SOURCE_BOUND_STATUS = NOT_YET_SOURCE_BOUND
ACTIVE_CANDIDATE_GRAMMAR = PGH-GRAM-0001
FAILED_DERIVATIONS_ARE_FIRST_CLASS_RESULTS = YES
NEXT_RECOMMENDED_OPERATION = PGH0_MINIMAL_GRAMMAR_CHALLENGE
NEXT_OPERATION_AUTHORIZED = NO
```

The project should be judged by whether its hypotheses become precise, nontrivial, representation-independent, and capable of failure — not by whether PGH survives.
