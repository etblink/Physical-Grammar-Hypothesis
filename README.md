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

## Repository map

- [`governance/PGH_REPOSITORY_OPENING_CHARTER_0_1_0.md`](governance/PGH_REPOSITORY_OPENING_CHARTER_0_1_0.md) — project scope, epistemic boundaries, provenance discipline, and phase structure.
- [`CURRENT_STATE.md`](CURRENT_STATE.md) — exact present research state and next recommended test.
- [`HYPOTHESIS.md`](HYPOTHESIS.md) — weak, strong, and identity forms of PGH, including falsification conditions.
- [`PRIMITIVES.md`](PRIMITIVES.md) — candidate minimal primitives and the anti-import firewall.
- [`NONTRIVIALITY_TESTS.md`](NONTRIVIALITY_TESTS.md) — tests intended to distinguish a genuine explanatory grammar from relabeling or universal encoding.
- [`RESEARCH_LOG.md`](RESEARCH_LOG.md) — chronological decisions, failed ideas, and conceptual changes.
- [`handoffs/`](handoffs/) — compact continuation artifacts for resuming work without relying on chat context.

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
FAILED_DERIVATIONS_ARE_FIRST_CLASS_RESULTS = YES
```

The project should be judged by whether its hypotheses become precise, nontrivial, representation-independent, and capable of failure — not by whether PGH survives.