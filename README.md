# Physical Grammar Hypothesis

> **Status:** Speculative foundational research — independent incubation
>
> **Current phase:** `PGH-0_CONCEPTUAL_FORMULATION`
>
> **FCP relationship:** None at present. This repository is deliberately quarantined from the Foundational Convergence Program (FCP); it has no FCP framework status and no canonical effect on FCP.

## Purpose

The **Physical Grammar Hypothesis (PGH)** asks whether the deepest laws of physical possibility may be understood as a compact, representation-independent generative grammar whose well-formed structures or derivations correspond, modulo physical equivalence, to physically possible structures.

A schematic strong form is:

\[
P \cong W(G)/{\sim}.
\]

PGH is a research hypothesis under construction, not an accepted theory of physics.

## Current result

The first bounded formal challenge, `PGH0_MINIMAL_GRAMMAR_CHALLENGE`, is canonically complete.

The opening shell

```text
PGH-GRAM-0001 = {DISTINGUISH, COMPOSE, IDENTIFY}
```

did **not** survive as three independent primitives at bare formation well-formedness scope.

The current baseline is:

```text
ACTIVE_CANDIDATE_GRAMMAR = PGH-GRAM-0002
NAME = EXTENSIONAL_FORMATION_BASELINE
STATUS = PROVISIONAL_FORMAL_BASELINE_NONPHYSICAL
```

At the weakest worked representation, a carrier `A` with a bare formation relation

\[
F\subseteq A^3
\]

induces grammar-internal contextual equivalence and distinction from complete formation-incidence profiles. This yields the qualified formal result `PGH-DER-0001`.

However, bare formation fails as a nontrivial physical grammar: for any desired local admissibility table `S`, setting `F=S` simply stores that table directly. This preserved failure is `PGH-FAIL-0001`.

Therefore:

```text
PHYSICAL_GRAMMAR_FOUND = NO
NONTRIVIAL_PHYSICAL_CONSTRAINT_DERIVED = NO
PGH-GRAM-0002_OUTCOME = FORMALLY_INTERESTING_NONPHYSICAL
```

## Current research question

The next recommended challenge is:

> What is the weakest **non-arbitrary** structural constraint on formation that yields an exclusion not merely entered as an admissibility table?

It is not yet authorized.

```text
NEXT_RECOMMENDED_OPERATION = PGH0_NONARBITRARY_FORMATION_CONSTRAINT_CHALLENGE
NEXT_OPERATION_AUTHORIZED = NO
```

## Epistemic rules

1. **No-smuggling.** Renaming a known physical law as a grammar rule is not an explanation.
2. **Representation invariance.** Candidate deep structure must not depend on one arbitrary surface language.
3. **Nontrivial exclusion.** A useful grammar must derive exclusions rather than merely list them.
4. **Generative compression.** The rule system should be materially simpler than the structures it accounts for.
5. **Failure conditions first.** Candidate principles must be exposed to counterexamples.
6. **Failed derivations are first-class results.**
7. **Formal resemblance is not physical derivation.**
8. **No premature FCP import.**

## Authority model

```text
GIT = PROVENANCE_AUTHORITY
CANONICAL_MARKDOWN_ARTIFACTS = RESEARCH_AND_GOVERNANCE_AUTHORITY
STRUCTURED_NAVIGATION_LAYER = DERIVED_NAVIGATION_ONLY
```

If navigation metadata conflicts with a canonical research artifact, the canonical artifact wins.

## Key current artifacts

- [`CURRENT_STATE.md`](CURRENT_STATE.md) — exact live research state.
- [`HYPOTHESIS.md`](HYPOTHESIS.md) — weak, strong, and identity formulations.
- [`NONTRIVIALITY_TESTS.md`](NONTRIVIALITY_TESTS.md) — formal anti-triviality suite.
- [`research/formalizations/PGH0_MINIMAL_GRAMMAR_FORMALIZATION_0_1_0.md`](research/formalizations/PGH0_MINIMAL_GRAMMAR_FORMALIZATION_0_1_0.md) — first formal baseline.
- [`research/derivations/PGH_DERIVATION_CONTEXTUAL_EXTENSIONAL_REDUCTION_0_1_0.md`](research/derivations/PGH_DERIVATION_CONTEXTUAL_EXTENSIONAL_REDUCTION_0_1_0.md) — qualified formal derivation.
- [`research/failures/PGH_FAIL_BARE_FORMATION_GRAMMAR_PHYSICAL_SUFFICIENCY_0_1_0.md`](research/failures/PGH_FAIL_BARE_FORMATION_GRAMMAR_PHYSICAL_SUFFICIENCY_0_1_0.md) — preserved first failure.
- [`meta/PGH_CANONICAL_INDEX.json`](meta/PGH_CANONICAL_INDEX.json) — derived orientation.
- [`handoffs/`](handoffs/) — durable continuation artifacts.

## Stable identities

```text
PGH-OP-####    bounded operations
PGH-Q-####     research questions
PGH-OBJ-####   research objects
PGH-DER-####   derivations
PGH-FAIL-####  failed derivations
PGH-GRAM-####  candidate grammars
```

Numeric suffixes are identities, not rankings.

## Navigation check

```text
python -B tools/pgh_navigation.py check
```

Machine-readable JSON/JSONL/Python files are pinned to LF; Markdown parsers must tolerate ordinary CRLF checkouts.

## Current status

```text
PROJECT = Physical Grammar Hypothesis
PROJECT_CLASS = SPECULATIVE_FOUNDATIONAL_RESEARCH
CURRENT_PHASE = PGH-0_CONCEPTUAL_FORMULATION
SOURCE_BOUND_STATUS = NOT_YET_SOURCE_BOUND
EMPIRICAL_STATUS = UNESTABLISHED
ACTIVE_CANDIDATE_GRAMMAR = PGH-GRAM-0002
QUALIFIED_FORMAL_DERIVATION_COUNT = 1
FAILED_DERIVATION_COUNT = 1
NEXT_RECOMMENDED_OPERATION = PGH0_NONARBITRARY_FORMATION_CONSTRAINT_CHALLENGE
NEXT_OPERATION_AUTHORIZED = NO
FCP_RELATIONSHIP = INDEPENDENT_INCUBATION
CANONICAL_EFFECT_ON_FCP = NONE
```

The project should be judged by whether its hypotheses become precise, nontrivial, representation-independent, and capable of failure—not by whether PGH survives.
