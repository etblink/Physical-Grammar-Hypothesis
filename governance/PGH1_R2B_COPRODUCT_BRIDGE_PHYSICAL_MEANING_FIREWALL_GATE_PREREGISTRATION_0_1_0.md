# PGH-1 R2B Coproduct Bridge Physical Meaning Firewall Gate — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_R2B_COPRODUCT_BRIDGE_PHYSICAL_MEANING_FIREWALL_GATE
REGISTRY_ID = PGH-OP-0054
CANONICAL_BASE = afaafff16209204a7d4443b3af6155fae36c6ddb
TYPED_ANCHOR = PGH-OBJ-0025
BRIDGE_STANDARD = PGH-OBJ-0027
BRIDGE_CANDIDATE = PGH-OBJ-0028
CANDIDATE_GRAMMARS = PGH-GRAM-0006; PGH-GRAM-0007
R2_TARGET = PGH-OBJ-0021
NEW_SOURCE_SEARCH = FORBIDDEN
EMPIRICAL_RESPONSE_DATA = FORBIDDEN
EMPIRICAL_MODEL_FIT = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Test whether the formally admitted coproduct aggregate-output bridge candidate can receive any response-relevant physical meaning without either:

1. importing a deterministic response map, allowed-response support, or response probability law through the semantic/model interpretation of the bridge morphism; or
2. weakening the interpretation so far that the bridge carries no substantive response-selective content.

The gate does not ask whether coproducts are physically fundamental.

It does not interpret morphism existence as physical response by default.

It does not use empirical outcomes to choose a semantic reading.

## Fixed formal candidate

For each context `c` with finite typed record fiber `R_c`, define

\[
O_c = \coprod_{r\in R_c} Y_r
\]

and one primitive bridge generator

\[
n_c:X_c\to O_c.
\]

No component arrow

\[
X_c\to Y_r
\]

is primitive or grammar-forced.

The typed anchor remains response-underdetermining as required by `PGH-DER-0023`.

## Semantic layers

The following must remain distinct:

```text
L1 = ABSTRACT_GRAMMAR_AND_BRIDGE_SYMBOL
L2 = CONCRETE_MODEL_OR_SEMANTIC_INTERPRETATION_OF_THE_SYMBOL
L3 = CANDIDATE_PHYSICAL_RESPONSE_MEANING
L4 = EMPIRICAL_ADEQUACY
```

Only L2/L3 feasibility is audited here.

L4 is forbidden.

## Locked theorem T1 — deterministic coproduct-tag pushforward

In a finite Set-style interpretation, let each summand `Y_r` be a set and let

\[
q:\coprod_{r\in R_c}Y_r\to R_c
\]

be the canonical summand-tag map.

For any interpretation

\[
\hat n_c:X_c\to\coprod_{r\in R_c}Y_r,
\]

form

\[
f_c=q\circ\hat n_c:X_c\to R_c.
\]

Test whether a response-relevant interpretation of `hat n_c` thereby determines a deterministic record-label map.

If yes, the concrete interpretation of `n_c` carries response-selection data even though the abstract bridge symbol does not contain component arrows syntactically.

## Locked theorem T2 — relational support pushforward

In a finite relational interpretation, let

\[
\hat n_c\subseteq X_c\times\coprod_{r\in R_c}Y_r.
\]

Define

\[
K_c(x,r)\iff \exists y\in Y_r:\;x\;\hat n_c\; y.
\]

Test whether interpreting `hat n_c` as physical process possibility induces an allowed-response support relation `K_c`.

If yes, a primitive concrete relation cannot receive grammar-derived response-law credit merely because it is packaged through a coproduct.

## Locked theorem T3 — stochastic pushforward

In a finite stochastic interpretation, let

\[
\hat n_c(y\mid x)
\]

be a normalized kernel on the disjoint union of summands.

Define the record-label marginal

\[
p_c(r\mid x)=\sum_{y\in Y_r}\hat n_c(y\mid x).
\]

Test whether the concrete interpretation of `n_c` therefore contains a response probability law at record-label scope.

## Locked control T4 — same abstract bridge, incompatible concrete responses

Use one context atom `X`, two singleton record objects `Y_0`,`Y_1`, and the same abstract bridge generator

\[
n:X\to Y_0+Y_1.
\]

In `Set`, take `X={*}`, `Y_0={0}`, `Y_1={1}`.

Compare two lawful interpretations:

\[
\hat n_0(*)=\iota_0(0),
\]

and

\[
\hat n_1(*)=\iota_1(1).
\]

The abstract grammar, typed anchor, and bridge symbol are held fixed.

Test whether the pushed-forward label maps differ.

If yes, the abstract bridge candidate does not determine the response law; model/semantic interpretation supplies the difference.

## Locked control T5 — existence/type-only reading

Consider the weaker semantic reading:

> the bridge asserts only that some aggregate process of type `X_c -> O_c` is admitted, without assigning physical response meaning to the specific morphism data or to summand membership.

Test whether this reading remains compatible with multiple incompatible response laws.

If yes, it may remain law-free, but the gate must determine whether it supplies any substantive response-selection needed for R2B.

A reading that is law-free only because it ignores the bridge's selective data cannot be credited with deriving physical law.

## Locked control T6 — free syntactic reading

In the free coproduct-capable grammar, `n_c` is a primitive formal arrow with no equation selecting any summand and no component arrow forced by `PGH-DER-0026`.

Test whether the syntactic candidate alone determines any response support, response map, or probability distribution.

Expected control: no such physical object follows without an additional semantic interpretation.

## Locked control T7 — semantic rebranding firewall

The following inferences are forbidden unless independently derived:

```text
COPRODUCT_SUMMAND = PHYSICAL_OUTCOME
MORPHISM_VALUE_IN_SUMMAND = ACTUAL_RESPONSE
RELATIONAL_MEMBERSHIP = PHYSICAL_POSSIBILITY
STOCHASTIC_WEIGHT = PHYSICAL_PROBABILITY
MORPHISM_EXISTS = RESPONSE_IS_POSSIBLE
```

A semantic label cannot convert model-supplied data into grammar-derived law.

## Outcome space

```text
A = AT_LEAST_ONE_RESPONSE_RELEVANT_SEMANTIC_READING_OF_THE_COPRODUCT_BRIDGE_REMAINS_RESPONSE_UNDERDETERMINING_WHILE_GENERATING_NONTRIVIAL_PHYSICAL_SELECTION_NOT_SUPPLIED_BY_MODEL_INTERPRETATION__A_LATER_R2B_LAW_EXHAUSTION_TEST_IS_JUSTIFIED

B = RESPONSE_RELEVANT_CONCRETE_READINGS_PUSH_THE_BRIDGE_INTERPRETATION_TO_A_RESPONSE_MAP_SUPPORT_OR_DISTRIBUTION_WHILE_LAW_FREE_EXISTENCE_OR_TYPE_ONLY_READINGS_REMAIN_NONSELECTIVE__THE_FORMAL_BRIDGE_CANDIDATE_FAILS_THE_PHYSICAL_MEANING_FIREWALL_AT_CURRENT_SCOPE

C = A_PLAUSIBLE_RESPONSE_RELEVANT_READING_WEAKER_THAN_RESPONSE_LAW_SURVIVES_BUT_THE_CURRENT_70_SOURCE_CORPUS_OR_FORMAL_BASELINE_IS_INSUFFICIENT_TO_ADJUDICATE_IT__A_NARROW_SOURCE_OR_FORMALISM_GAP_MUST_BE_IDENTIFIED

D = THE_TESTED_SEMANTIC_READINGS_ARE_NOT_COMPARABLE_ENOUGH_TO_SUPPORT_A_BOUNDED_ADJUDICATION
```

No outcome satisfies R2B or constitutes an empirical prediction.

## Required outputs

Commit 2 may add only:

```text
audits/PGH1_R2B_COPRODUCT_BRIDGE_PHYSICAL_MEANING_FIREWALL_GATE_0_1_0.md
research/formalizations/PGH1_COPRODUCT_BRIDGE_PHYSICAL_MEANING_FIREWALL_SCHEMA_0_1_0.md
research/derivations/PGH_DERIVATION_COPRODUCT_TAG_PUSHFORWARD_RESPONSE_EXTRACTION_0_1_0.md
research/failures/PGH_FAIL_COPRODUCT_BRIDGE_SEMANTIC_RESPONSE_RELOCATION_0_1_0.md
handoffs/PGH1_R2B_COPRODUCT_BRIDGE_PHYSICAL_MEANING_FIREWALL_GATE_HANDOFF_0_1_0.md
```

Expected identities if earned:

```text
PGH-OBJ-0029 = COPRODUCT_BRIDGE_PHYSICAL_MEANING_FIREWALL_SCHEMA
PGH-DER-0027 = COPRODUCT_TAG_PUSHFORWARD_RESPONSE_EXTRACTION
PGH-FAIL-0028 = COPRODUCT_BRIDGE_SEMANTIC_RESPONSE_RELOCATION
```

## Commit topology

```text
COMMIT_1_MESSAGE = Preregister PGH-1 R2B coproduct bridge physical meaning firewall gate
COMMIT_2_MESSAGE = Adjudicate PGH-1 R2B coproduct bridge physical meaning firewall gate
EXACT_COMMITS = 2
```

## Hard stops

```text
DO_NOT_SEARCH_NEW_SOURCES
DO_NOT_USE_EMPIRICAL_RESPONSE_DATA
DO_NOT_CHOOSE_SEMANTICS_BY_EMPIRICAL_FIT
DO_NOT_CALL_COPRODUCT_A_PHYSICAL_ALTERNATIVE_BY_DEFINITION
DO_NOT_CALL_MORPHISM_A_PHYSICAL_RESPONSE_BY_DEFINITION
DO_NOT_CREDIT_MODEL_SPECIFIC_RESPONSE_DATA_TO_THE_ABSTRACT_GRAMMAR
DO_NOT_DECLARE_R2B_SATISFIED
DO_NOT_MAKE_EMPIRICAL_PREDICTIONS
DO_NOT_CHANGE_FCP
```
