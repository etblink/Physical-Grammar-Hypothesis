# PGH-1 R2A Primitive Grammar Stopping-Rule Adjudication — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_R2A_PRIMITIVE_GRAMMAR_STOPPING_RULE_ADJUDICATION
REGISTRY_ID = PGH-OP-0047
CANONICAL_BASE = 4c95792e609297df5df76168d1335405f24a8c60
WORKING_TARGET = PGH-OBJ-0017
ANCHOR_TARGET = PGH-OBJ-0012
FROZEN_ACCEPTED_SOURCE_COUNT = 70
NEW_SOURCE_SEARCH = FORBIDDEN
PHYSICAL_BRIDGE = FORBIDDEN
SUCCESSOR_PHYSICAL_GRAMMAR_SELECTION = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Adjudicate whether the current post-meta-language requirement

```text
R2A = GENERATE_THE_SELECTIVE_STRUCTURAL_PACKAGE_FROM_SMALLER_STRUCTURE
```

is a mandatory truth-condition of anchored strong PGH, or a useful strengthening/discovery route that has been overextended into an infinite meta-derivation requirement.

The gate must explicitly distinguish:

1. a declared primitive candidate grammar;
2. a hidden extensional law table;
3. a grammar chosen after seeing the target physics;
4. an independent law set outside the grammar.

## Canonical texts controlling the adjudication

```text
HYPOTHESIS.md
NONTRIVIALITY_TESTS.md
research/formalizations/PGH0_ANCHORED_STRONG_PGH_SPECIFICATION_0_1_0.md
research/formalizations/PGH1_R2_POST_META_LANGUAGE_PRIOR_ART_RESIDUAL_0_1_0.md
research/failures/PGH_FAIL_COMPOSITIONAL_DOCTRINE_SELECTOR_UNDERDETERMINATION_0_1_0.md
```

## Locked tests

### T1 — hypothesis-text consistency

Determine whether anchored strong PGH requires the candidate grammar `G` itself to be generated from a meta-grammar, or instead takes `G` as the object whose consequences must exhaust substantive law.

### T2 — no-smuggling distinction

Test whether declaring structure inside `G` is automatically smuggling.

Countercontrols:

- arbitrary extensional formation/support tables;
- unrestricted primitive predicates that encode target supports;
- compact structural postulates fixed before target consequences are evaluated.

A declared primitive does not automatically pass. It must still survive the canonical N0–N10 tests.

### T3 — mandatory-regress test

Test whether requiring every primitive grammar structure to be derived from a deeper structure changes the hypothesis from

\[
A_{ref}+G\to P
\]

into an unbounded meta-hierarchy not present in the canonical hypothesis.

Do not infer that a finite explanatory hierarchy is impossible. The question is whether the extra demand is canonical PGH or an added methodological strengthening.

### T4 — candidate-vs-confirmed distinction

Test whether a primitive doctrine can be admitted only as a **candidate grammar** while remaining physically unconfirmed.

Candidate admission must not imply:

```text
PHYSICAL_PRIVILEGE
R2B_PASS
EMPIRICAL_SUCCESS
UNIQUE_GRAMMAR
```

### T5 — admissibility standard

A primitive candidate grammar may be acceptable only if a strict nontriviality standard can distinguish it from universal encoding.

Minimum candidate controls to test:

```text
FORMAL_DEFINABILITY
DECLARED_PRIMITIVES
PRE_TARGET_FIXATION
RESTRICTED_HYPOTHESIS_CLASS
NO_EXTENTIONAL_TARGET_TABLE
GENERATIVE_COMPRESSION
NONTRIVIAL_EXCLUSION
REPRESENTATION_DISCIPLINE_OR_EXPLICIT_TEST
LAW_FREE_SEMANTIC_BOUNDARY
INDEPENDENT_CONSEQUENCE
COUNTEREXAMPLE_EXPOSURE
SEPARATE_PHYSICAL_BRIDGE
```

### T6 — plurality control

Test whether multiple primitive candidate grammars may coexist at the hypothesis-testing stage without one being uniquely derivable.

Scientific candidacy must be distinguished from unique fundamental truth.

### T7 — law-exhaustion preservation

Even if primitive `G` is admissible, anchored strong PGH still requires substantive physical selection to come from `G` after `A_ref` is fixed, without an independent selector `L` doing the work.

## Outcome space

```text
A = MANDATORY_META_DERIVATION_IS_NOT_A_CANONICAL_PGH_REQUIREMENT__A_DECLARED_PRIMITIVE_GRAMMAR_MAY_BE_ADMITTED_AS_A_CANDIDATE_ONLY_IF_IT_PASSES_A_STRICT_NO_SMUGGLING_COMPRESSION_EXCLUSION_AND_FALSIFIABILITY_STANDARD__R2B_REMAINS_UNSATISFIED
B = ANCHORED_STRONG_PGH_REQUIRES_THE_SELECTIVE_STRUCTURAL_PACKAGE_TO_BE_DERIVED_FROM_SMALLER_STRUCTURE__PRIMITIVE_DOCTRINE_ADMISSION_WOULD_DOWNGRADE_OR_BLOCK_THE_STRONG_CLAIM
C = CANONICAL_ARTIFACTS_ARE_INTERNALLY_AMBIGUOUS_OR_CONFLICTING_ABOUT_THE_STOPPING_RULE
D = SOURCE_OR_METHODOLOGICAL_GAP_BLOCKS_A_RESPONSIBLE_ADJUDICATION
```

## Required outputs

Commit 2 may add only:

```text
audits/PGH1_R2A_PRIMITIVE_GRAMMAR_STOPPING_RULE_ADJUDICATION_0_1_0.md
research/formalizations/PGH1_PRIMITIVE_GRAMMAR_ADMISSIBILITY_STANDARD_0_1_0.md
research/formalizations/PGH1_POST_STOPPING_RULE_ANCHORED_R2_RESIDUAL_0_1_0.md
research/failures/PGH_FAIL_MANDATORY_META_DERIVATION_STOPPING_RULE_0_1_0.md
handoffs/PGH1_R2A_PRIMITIVE_GRAMMAR_STOPPING_RULE_ADJUDICATION_HANDOFF_0_1_0.md
```

## Commit topology

```text
COMMIT_1_MESSAGE = Preregister PGH-1 R2A primitive grammar stopping-rule adjudication
COMMIT_2_MESSAGE = Adjudicate PGH-1 R2A primitive grammar stopping rule
EXACT_COMMITS = 2
```

## Hard stops

```text
DO_NOT_ADMIT_ANY_SPECIFIC_DOCTRINE_AS_PHYSICAL_GRAMMAR
DO_NOT_TREAT_PRIMITIVE_AS_AUTOMATICALLY_NONSMUGGLED
DO_NOT_DEMAND_DERIVATION_FROM_NOTHING
DO_NOT_DECLARE_R2B_SATISFIED
DO_NOT_BEGIN_EMPIRICAL_FIT
DO_NOT_SEARCH_NEW_SOURCES
DO_NOT_CHANGE_FCP
```
