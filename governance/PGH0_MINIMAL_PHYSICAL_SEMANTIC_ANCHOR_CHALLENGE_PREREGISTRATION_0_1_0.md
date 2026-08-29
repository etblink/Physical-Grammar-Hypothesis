# PGH-0 Minimal Physical Semantic Anchor Challenge — Preregistration 0.1.0

## Status

```text
OPERATION_ID = PGH0_MINIMAL_PHYSICAL_SEMANTIC_ANCHOR_CHALLENGE
REGISTRY_ID = PGH-OP-0015
OPERATION_CLASS = SOURCE_BOUND_FOUNDATIONAL_FORMALIZATION
STATUS = PREREGISTERED_IN_PROGRESS
CANONICAL_BASE = 26b9d8616ef98a481e0ac67f807384ce4527c906
WORKING_BRANCH = research/pgh0-minimal-physical-semantic-anchor
FROZEN_SOURCE_COUNT = 37
NEW_SOURCE_SEARCH = FORBIDDEN_UNLESS_SPECIFIC_GAP_IS_DEMONSTRATED
R2_LAW_EXHAUSTION = FORBIDDEN
PHYSICAL_GRAMMAR_SELECTION = FORBIDDEN
EMPIRICAL_ADJUDICATION = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

The R1 feasibility gate established that formal equivalence does not by itself entail physical equivalence. This operation asks whether there exists a deliberately weak semantic anchor that can constrain physical significance without already containing the substantive response law, dynamics, or possibility structure that PGH aims to explain.

The target is not a physical theory. It is a minimal interface between formal grammar and physical significance.

## Acceptance criteria

A candidate anchor qualifies only as a **formally feasible semantic-anchor schema** if all of the following hold:

```text
A1_NOT_A_FULL_LAW_SET
A2_NOT_DEFINED_BY_TARGET_EQUIVALENCE
A3_SUPPORTS_NONTRIVIAL_DISTINGUISHABILITY_JUDGMENTS
A4_REUSABLE_ACROSS_MULTIPLE_CANDIDATE_GRAMMARS
A5_DOES_NOT_ENCODE_RESPONSE_OR_DYNAMICS_TABLE
A6_DOES_NOT_ENCODE_COMPLETE_POSSIBILITY_STRUCTURE
A7_EXPOSES_EXPLICIT_FAILURE_CONDITIONS
A8_SEPARATES_INTERFACE_SEMANTICS_FROM_GRAMMAR_GENERATED_RESPONSE
```

Qualification at this level does not establish that the anchor is physically realized, unique, representation-independent, or empirically correct.

## Locked candidate tests

Test in this order.

### S0 — Primitive physical-distinguishability relation

Directly stipulate `x ~phys y` or its complement.

Control question: does this merely encode the target equivalence and therefore fail A2?

### S1 — Vocabulary-only observational anchor

Specify only that certain formal symbols are called observations or records, with no contexts or response structure.

Control question: is this too weak to constrain physical significance?

### S2 — Full observation-response table

Specify all probe/state response pairs or all predicted records.

Control question: does this violate A1/A5 by placing the substantive response law in semantics?

### S3 — Full task-possibility anchor

Specify which tasks or transformations are physically possible/impossible.

Control question: does this violate A6 by importing the possibility structure that PGH aims to explain?

### S4 — Context/record interface anchor

Test the schema

```text
A_phys = (C, R, rho)
```

where:

- `C` is a declared family of formal one-hole contexts interpreted only as probe/interface types;
- `R` is a set of record labels;
- `rho` maps designated terminal/output labels to record labels;
- `A_phys` does **not** specify which output is produced by applying a context to a candidate structure.

Let a candidate grammar/evaluator `e` supply the response behavior. Define the record profile

\[
O_{A,e}(x)(c)=\rho(e(c[x]))
\]

where defined.

Define anchor-relative indistinguishability by equality of complete record profiles:

\[
x \sim_{A,e} y
\iff
O_{A,e}(x)=O_{A,e}(y).
\]

Required audits:

1. Does `A_phys` determine the response law by itself?
2. Can the same anchor be used with two different evaluators that generate different response profiles?
3. Can it produce nontrivial distinguishability once combined with a grammar?
4. Is the resulting equivalence noncircular relative to the generated response?
5. Does choosing `C` and `rho` still contain unresolved physical assumptions?

### S5 — Intervention-interface variant

Replace passive probe contexts with intervention/interface types while still forbidding a response table in the anchor.

Question: does this add genuine minimal semantic power, or merely rename/contextualize S4?

## Required finite witness

For S4 construct one finite anchor shared by at least two candidate evaluators.

The same `C`, `R`, and `rho` must permit:

- one evaluator under which two candidate structures are record-indistinguishable;
- another evaluator under which they are record-distinguishable.

This demonstrates that the anchor does not itself encode the response law.

Also provide at least one nontrivial anchor-relative equivalence partition.

## No-smuggling theorem target

If supported, qualify only the conditional/formal statement:

> A context/record interface can supply physical-significance vocabulary and comparison interfaces without determining the grammar-generated response map.

Do not infer:

- that the chosen probes are physically fundamental;
- that records exhaust physical significance;
- that observational equivalence is complete physical identity;
- that the anchor survives arbitrary faithful reformulation;
- that R1 is solved physically.

## Failure controls

The following should count against a candidate:

```text
TARGET_EQUIVALENCE_STIPULATED_DIRECTLY
FULL_PREDICTION_TABLE_IN_ANCHOR
FULL_POSSIBILITY_SET_IN_ANCHOR
ANCHOR_DEPENDS_ON_DESIRED_LAW_CLASS
ANCHOR_CANNOT_BE_REUSED_ACROSS_COMPETING_GRAMMARS
ANCHOR_HAS_NO_NONTRIVIAL_DISTINGUISHING_POWER
```

## Outcome space

```text
A = NO_TESTED_ANCHOR_IS_BOTH_NONTRIVIAL_AND_NONSMUGGLING
B = CONTEXT_RECORD_INTERFACE_IS_A_FORMALLY_FEASIBLE_MINIMAL_ANCHOR_BUT_PHYSICAL_REALIZATION_IS_UNESTABLISHED
C = ANOTHER_TESTED_ANCHOR_SCHEMA_QUALIFIES_FORMALLY
D = ANY_ANCHOR_STRONG_ENOUGH_FOR_R1_ALREADY_ENCODES_SUBSTANTIVE_PHYSICS_AT_CURRENT_SCOPE
E = FROZEN_CORPUS_IS_INSUFFICIENT_AND_A_SPECIFIC_SOURCE_GAP_IS_IDENTIFIED
F = UNRESOLVED
```

## Source discipline

Use the frozen operational/process, theoretical-equivalence, constructor, laws-as-constraints, and formal machinery sources only as comparison/control material. Source frequency is not evidence for the anchor.

No source expansion is permitted unless adjudication identifies a concrete missing semantic-framework question that blocks the test.

## Required outputs

Commit 2 may add only:

```text
audits/PGH0_MINIMAL_PHYSICAL_SEMANTIC_ANCHOR_CHALLENGE_0_1_0.md
research/formalizations/PGH0_CONTEXT_RECORD_SEMANTIC_ANCHOR_0_1_0.md        # only if S4 qualifies
research/derivations/PGH_DERIVATION_ANCHOR_RESPONSE_SEPARATION_0_1_0.md   # only if established
research/failures/PGH_FAIL_SEMANTIC_ANCHOR_EXTREMES_0_1_0.md             # if warranted
handoffs/PGH0_MINIMAL_PHYSICAL_SEMANTIC_ANCHOR_CHALLENGE_HANDOFF_0_1_0.md
```

Do not mutate current-state/navigation files on the scientific branch.

## Commit boundary

```text
COMMIT_1_MESSAGE = Preregister PGH-0 minimal physical semantic anchor
COMMIT_2_MESSAGE = Adjudicate PGH-0 minimal physical semantic anchor
```

Exactly two commits are permitted.

## Hard stops

Stop before:

- claiming a physically correct semantic anchor has been found;
- beginning R2 law exhaustion;
- deriving known physical dynamics from the anchor;
- selecting a physical grammar;
- empirical analysis;
- unbounded source expansion;
- changing FCP;
- mutating canonical `main` before independent review.
