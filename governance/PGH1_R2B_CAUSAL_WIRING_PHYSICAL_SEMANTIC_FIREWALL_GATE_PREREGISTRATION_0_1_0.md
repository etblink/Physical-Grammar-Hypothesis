# PGH-1 R2B Causal Wiring Physical Semantic Firewall Gate — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_R2B_CAUSAL_WIRING_PHYSICAL_SEMANTIC_FIREWALL_GATE
REGISTRY_ID = PGH-OP-0061
CANONICAL_BASE = c92729ba1e9ef6936a6fb5553380cc7aaa6ec224
GRAMMAR_CANDIDATE = PGH-GRAM-0008
GRAMMAR_CANDIDACY_SCHEMA = PGH-OBJ-0034
DERIVED_RESTRICTION = PGH-DER-0029
PREMATURE_SEMANTICS_FAILURE = PGH-FAIL-0032
FROZEN_SOURCE_CORPUS = 85_DISTINCT_ACCEPTED
EMPIRICAL_DATA = FORBIDDEN
EMPIRICAL_TARGET_SELECTION = FORBIDDEN
NEW_SOURCE_SEARCH = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Test whether `PGH-GRAM-0008` can receive a minimal empirical/physical semantic bridge that transfers its model-class restriction to a prospective empirical joint-distribution class **without adding response selectivity through the semantic map itself**.

The gate does not choose real-world variables, inspect data, interpret graph arrows as physical causes, or test empirical adequacy.

## Semantic layers

Keep distinct:

```text
L1 = FORMAL_GRAMMAR_MODEL_CLASS
L2 = MODEL_CLASS_REALIZATION_SEMANTIC_MAP
L3 = PROSPECTIVE_EMPIRICAL_VARIABLE_INSTANTIATION
L4 = EMPIRICAL_DATA_AND_ADEQUACY
```

This gate tests L2 only and defines requirements on a later L3.

L4 is forbidden.

## Locked reading S0 — pure bookkeeping

Treat `A,B,C`, probabilities, and graph structure as purely mathematical with no empirical interpretation.

Expected role:

```text
SEMANTIC_SAFETY = HIGH
PHYSICAL_TESTABILITY = NONE
```

This is the null reading.

## Locked reading S1 — faithful model-class realization bridge

Define three prospective record-valued empirical variable roles

\[
\mathcal A,\mathcal B,\mathcal C
\]

with finite alphabets bijectively matched to the formal alphabets of `A,B,C`.

A realization map `J` sends each grammar model

\[
p\in W(PGH\text{-}GRAM\text{-}0008)
\]

to the corresponding candidate empirical joint-response distribution over

\[
(\mathcal A,\mathcal B,\mathcal C)
\]

by the fixed alphabet/variable relabeling.

Required non-smuggling condition:

```text
J_MAY_NOT_SELECT_A_PROPER_SUBSET_OF_GRAMMAR_MODELS
J_MAY_NOT_FIX_LOCAL_KERNEL_VALUES
J_MAY_NOT_ADD_RESPONSE_EQUATIONS
J_MAY_NOT_USE_EMPIRICAL_DATA
```

At the abstract schema level, the image of `J` must be exactly the full grammar model class modulo the declared representation relabeling.

The semantic hypothesis is:

> for a later explicitly preregistered empirical instantiation, the candidate physically admissible joint-response models are the realized models of `PGH-GRAM-0008`.

Test whether this adds an independent law or merely gives empirical reference to the grammar's already-fixed model class.

## Locked theorem T1 — restriction transfer under full-class realization

If every formal model `p` satisfies a property `P`, and `J` faithfully transports the entire formal model class without selecting models or adding equations, then every realized candidate empirical model `J(p)` satisfies the transported property `J(P)`.

Apply this to

\[
P = A\perp C\mid B.
\]

If S1 passes, any later valid empirical instantiation predicts

\[
\boxed{\mathcal A\perp \mathcal C\mid \mathcal B}.
\]

This is a **candidate falsifiable restriction conditional on instantiation**, not an empirical result.

## Locked control S2 — arrow-as-physical-cause interpretation

Consider the stronger semantic reading:

> each formal arrow is, by definition, a direct physical causal relation and missing arrows are physical causal exclusions.

Test whether this stronger ontology is required for the candidate prediction.

If S1 already transfers the response restriction without it, S2 must not be smuggled in as necessary physical meaning.

The gate may leave causal ontology unqualified even if S1 passes.

## Locked control S3 — post-hoc empirical instantiation

Reject any later mapping of `A,B,C` to real observables chosen because the observed data already approximately satisfy the chain conditional independence.

A valid empirical instantiation must be fixed by a separate preregistration using target-selection criteria that do not inspect the target conditional-independence result.

## Locked control S4 — model selection in semantics

Hold `PGH-GRAM-0008` fixed.

If a semantic interpretation selects one kernel triple or one favored subset of grammar models because of empirical fit, the resulting response information is model-selection input and receives no grammar-derived law credit.

S1 passes only if the whole grammar class is realized at schema scope.

## Locked control S5 — representation covariance

Bijective renaming of formal variable roles/alphabet labels together with the corresponding empirical variable/alphabet labels must commute with `J`.

The candidate restriction must be transported, not tied to names.

## Locked control S6 — falsification exposure

A later empirical instantiation must expose a clear failure condition:

```text
OBSERVED_JOINT_RESPONSE_DISTRIBUTION_VIOLATES_A_INDEPENDENT_C_GIVEN_B
```

subject to a separately specified statistical/measurement protocol.

No such protocol or data analysis is performed here.

## Physical-law accounting

The gate must distinguish:

```text
FORMAL_RESTRICTION_DERIVED = YES_ALREADY_BY_PGH_DER_0029
SEMANTIC_BRIDGE_ADDS_EXTRA_RESTRICTION = MUST_BE_NO_FOR_S1
CANDIDATE_PHYSICAL_RESTRICTION = MAY_BECOME_YES_CONDITIONAL_ON_VALID_INSTANTIATION
PHYSICAL_LAW_EMPIRICALLY_ESTABLISHED = NO
R2B_LAW_EXHAUSTION = NO
```

## Outcome space

```text
A = A_FAITHFUL_FULL_MODEL_CLASS_REALIZATION_BRIDGE_ADDS_NO_EXTRA_RESPONSE_SELECTIVITY_AND_TRANSFERS_THE_GRAMMAR_DERIVED_CONDITIONAL_INDEPENDENCE_TO_ANY_SEPARATELY_PREREGISTERED_EMPIRICAL_INSTANTIATION__PGH_GRAM_0008_BECOMES_PHYSICALLY_TESTABLE_IN_PRINCIPLE_WITHOUT_PHYSICAL_CAUSATION_ONTOLOGY

B = EVERY_RESPONSE_RELEVANT_SEMANTIC_READING_EITHER_ADDS_MODEL_SELECTION_OR_LAW_CONTENT_OR_REMAINS_PURE_BOOKKEEPING__PGH_GRAM_0008_HAS_NO_NONCIRCULAR_PHYSICAL_TESTABILITY_BRIDGE_AT_CURRENT_SCOPE

C = A_PLAUSIBLE_FULL_CLASS_REALIZATION_READING_EXISTS_BUT_THE_CURRENT_SOURCE_OR_FORMAL_BASELINE_IS_INSUFFICIENT_TO_DISTINGUISH_SEMANTIC_REFERENCE_FROM_INDEPENDENT_LAW__A_NARROW_GAP_MUST_BE_IDENTIFIED

D = THE_NOTION_OF_MODEL_CLASS_REALIZATION_IS_TOO_UNDERSPECIFIED_TO_SUPPORT_A_BOUNDED_SEMANTIC_ADJUDICATION
```

No outcome empirically validates PGH.

## Required outputs

Commit 2 may add only:

```text
audits/PGH1_R2B_CAUSAL_WIRING_PHYSICAL_SEMANTIC_FIREWALL_GATE_0_1_0.md
research/formalizations/PGH1_CAUSAL_WIRING_MODEL_CLASS_PHYSICAL_BRIDGE_SCHEMA_0_1_0.md
research/derivations/PGH_DERIVATION_MODEL_CLASS_RESTRICTION_TRANSFER_0_1_0.md
research/failures/PGH_FAIL_POSTHOC_CAUSAL_WIRING_EMPIRICAL_INSTANTIATION_0_1_0.md
handoffs/PGH1_R2B_CAUSAL_WIRING_PHYSICAL_SEMANTIC_FIREWALL_GATE_HANDOFF_0_1_0.md
```

Expected identities if earned:

```text
PGH-OBJ-0035 = CAUSAL_WIRING_MODEL_CLASS_PHYSICAL_BRIDGE_SCHEMA
PGH-DER-0031 = MODEL_CLASS_RESTRICTION_TRANSFER
PGH-FAIL-0033 = POSTHOC_CAUSAL_WIRING_EMPIRICAL_INSTANTIATION
```

## Commit topology

```text
COMMIT_1_MESSAGE = Preregister PGH-1 R2B causal wiring physical semantic firewall gate
COMMIT_2_MESSAGE = Adjudicate PGH-1 R2B causal wiring physical semantic firewall gate
EXACT_COMMITS = 2
```

## Hard stops

```text
DO_NOT_SEARCH_NEW_SOURCES
DO_NOT_SELECT_REAL_WORLD_VARIABLES
DO_NOT_USE_EMPIRICAL_DATA
DO_NOT_CALL_ARROWS_PHYSICAL_CAUSES_BY_DEFINITION
DO_NOT_SELECT_A_SUBSET_OF_GRAMMAR_MODELS_IN_THE_SEMANTIC_MAP
DO_NOT_FIX_LOCAL_KERNEL_VALUES
DO_NOT_DECLARE_EMPIRICAL_VALIDATION
DO_NOT_DECLARE_R2B_SATISFIED
DO_NOT_CHANGE_FCP
```
