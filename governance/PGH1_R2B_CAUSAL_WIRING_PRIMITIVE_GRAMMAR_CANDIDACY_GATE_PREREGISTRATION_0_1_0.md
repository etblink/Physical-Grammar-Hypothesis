# PGH-1 R2B Causal Wiring Primitive Grammar Candidacy Gate — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_R2B_CAUSAL_WIRING_PRIMITIVE_GRAMMAR_CANDIDACY_GATE
REGISTRY_ID = PGH-OP-0060
CANONICAL_BASE = b5107f219879c11f117ca1278a46a22fa150bf51
PRIMITIVE_GRAMMAR_STANDARD = PGH-OBJ-0020
PARAMETRIC_SCHEMA = PGH-OBJ-0033
SPARSE_RESTRICTION = PGH-DER-0029
COMPLETE_DAG_CONTROL = PGH-DER-0030
UNRESTRICTED_FAMILY_FAILURE = PGH-FAIL-0031
FROZEN_SOURCE_CORPUS = 85_DISTINCT_ACCEPTED
NEW_SOURCE_SEARCH = FORBIDDEN
EMPIRICAL_DATA = FORBIDDEN
PHYSICAL_CAUSATION_SEMANTICS = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Determine whether one fixed sparse Markov/DAG structural package qualifies as a new **formal primitive grammar candidate** under the already canonical `PGH-OBJ-0020` stopping rule, while keeping all physical interpretation and empirical graph selection outside this gate.

The operation does not ask whether the candidate is true, physically privileged, empirically adequate, or sufficient for R2B.

## Frozen candidate definition

Define trial candidate

```text
TRIAL_ID = PGH-GRAM-0008
TRIAL_NAME = THREE_NODE_SPARSE_MARKOV_CHAIN_PRIMITIVE_GRAMMAR_CANDIDATE
```

Its abstract variable roles are

```text
A,B,C
```

with arbitrary nonempty finite alphabets.

Its admissible models are normalized finite joint distributions satisfying

\[
p(a,b,c)=p(a)p(b\mid a)p(c\mid b).
\]

Equivalently, its fixed structural wiring is

\[
A\to B\to C.
\]

The local kernels

\[
p(a),\quad p(b\mid a),\quad p(c\mid b)
\]

are unrestricted model data subject only to normalization.

The candidate contains **no** fitted numerical kernel values and **no** empirical response table.

## Fixed null/control

Retain the complete ordered DAG control from `PGH-DER-0030`:

\[
A\to B,\quad A\to C,\quad B\to C.
\]

At finite joint-distribution scope it represents every joint distribution.

The control is used only to show that response selectivity comes from the sparse fixed wiring rather than from probability notation or DAG factorization in the abstract.

No new `PGH-GRAM-*` identity is assigned to the control in this gate.

## PGH-OBJ-0020 admissibility tests

### P0 — formal definability

Is the candidate model class mathematically exact?

### P1 — declared primitives

Are the graph/wiring structure, probability normalization, and factorization rule explicit rather than hidden in semantics?

### P2 — pre-target fixation

Was the candidate fixed before any empirical-fit operation or target physical response table?

The graph was selected as a preregistered minimal structural witness in the formal graph-parametric gate, not from empirical data.

### P3 — restricted hypothesis class / universal encoding

Does the fixed sparse graph fail to represent at least one explicit finite distribution, demonstrating that the candidate is not a universal response-table encoder at the tested scope?

### P4 — no extensional target table

Does the candidate avoid listing allowed joint outcomes or numerical probability values case by case?

### P5 — generative compression

Does one compact graph/factorization rule characterize an infinite family of joint distributions through freely varying local kernels?

### P6 — nontrivial formal exclusion

Does `PGH-DER-0029` plus the locked counterdistribution prove a proper model-class exclusion?

### P7 — representation discipline

Does consistent relabeling of variables, alphabets, and graph incidence transport the candidate covariantly without requiring all permutations to be graph automorphisms?

### P8 — semantic-load boundary

Does the candidate remain purely formal in this gate, without calling graph arrows physical causes or probabilities empirical frequencies by definition?

### P9 — independent formal consequence

Does the fixed wiring derive conditional independence rather than simply list it as a target response table?

### P10 — counterexample exposure

Are both an excluded distribution and a more permissive complete-DAG control explicit?

### P11 — physical bridge

Must remain:

```text
NOT_QUALIFIED
```

No physical semantics is tested here.

## Encoding firewall

The candidate fails if any of the following is needed to make it selective:

```text
NUMERICAL_KERNEL_VALUES
EMPIRICAL_RESPONSE_TABLE
TARGET_SPECIFIC_EQUATION_ADDED_AFTER_THE_FACT
HIDDEN_GRAPH_CHOICE_IN_SEMANTICS
```

The graph itself may be primitive under the stopping rule, but it must be part of the candidate identity and may not be disguised as neutral background.

## Complete-DAG interpretation

The complete-DAG control must not be misused to say that probability/DAG grammar is universally nonselective.

The correct comparison is:

```text
SAME_GENERAL_PROBABILISTIC_LANGUAGE
DIFFERENT_FIXED_WIRING
DIFFERENT_MODEL_CLASS_RESTRICTION
```

This is exactly why fixed wiring is candidate content.

## Outcome space

```text
A = PGH_GRAM_0008_PASSES_FORMAL_PRIMITIVE_GRAMMAR_CANDIDACY_UNDER_PGH_OBJ_0020__ITS_FIXED_SPARSE_WIRING_GENERATES_NONTRIVIAL_MODEL_CLASS_EXCLUSION_WITH_FREE_LOCAL_KERNELS__NO_PHYSICAL_STATUS_OR_R2B_CREDIT_FOLLOWS

B = THE_SPARSE_MARKOV_PACKAGE_FAILS_ONE_OR_MORE_HARD_PRIMITIVE_GRAMMAR_ADMISSIBILITY_TESTS__NO_NEW_GRAMMAR_IDENTITY_IS_QUALIFIED

C = FORMAL_CANDIDACY_DEPENDS_ON_AN_UNRESOLVED_SOURCE_OR_DEFINITIONAL_GAP__STOP_FOR_NARROW_REVIEW

D = THE_CANDIDATE_IS_FORMALLY_VALID_BUT_INFORMATION_EQUIVALENT_TO_AN_EXTENSIONAL_RESPONSE_TABLE_AT_THE_TESTED_SCOPE__REJECT_AS_HIDDEN_ENCODING
```

No outcome establishes a physical grammar.

## Required outputs

Commit 2 may add only:

```text
audits/PGH1_R2B_CAUSAL_WIRING_PRIMITIVE_GRAMMAR_CANDIDACY_GATE_0_1_0.md
research/grammars/PGH_GRAMMAR_THREE_NODE_SPARSE_MARKOV_CHAIN_CANDIDATE_0_1_0.md
research/formalizations/PGH1_CAUSAL_WIRING_PRIMITIVE_GRAMMAR_CANDIDACY_SCHEMA_0_1_0.md
research/failures/PGH_FAIL_CAUSAL_WIRING_PHYSICAL_SEMANTICS_PREMATURE_0_1_0.md
handoffs/PGH1_R2B_CAUSAL_WIRING_PRIMITIVE_GRAMMAR_CANDIDACY_GATE_HANDOFF_0_1_0.md
```

Expected identities if earned:

```text
PGH-GRAM-0008 = THREE_NODE_SPARSE_MARKOV_CHAIN_PRIMITIVE_GRAMMAR_CANDIDATE
PGH-OBJ-0034 = CAUSAL_WIRING_PRIMITIVE_GRAMMAR_CANDIDACY_SCHEMA
PGH-FAIL-0032 = CAUSAL_WIRING_PHYSICAL_SEMANTICS_PREMATURE
```

## Commit topology

```text
COMMIT_1_MESSAGE = Preregister PGH-1 R2B causal wiring primitive grammar candidacy gate
COMMIT_2_MESSAGE = Qualify PGH-1 R2B sparse Markov chain primitive grammar candidate
EXACT_COMMITS = 2
```

## Hard stops

```text
DO_NOT_SEARCH_NEW_SOURCES
DO_NOT_USE_EMPIRICAL_DATA
DO_NOT_CALL_A_B_C_PHYSICAL_VARIABLES
DO_NOT_CALL_DAG_ARROWS_PHYSICAL_CAUSES
DO_NOT_ASSIGN_PHYSICAL_PROBABILITY_MEANING
DO_NOT_FIX_LOCAL_KERNEL_VALUES
DO_NOT_MODIFY_PGH_GRAM_0003_THROUGH_0007
DO_NOT_DECLARE_R2B_SATISFIED
DO_NOT_DECLARE_PHYSICAL_LAW_DERIVED
DO_NOT_MAKE_EMPIRICAL_PREDICTIONS
DO_NOT_CHANGE_FCP
```
