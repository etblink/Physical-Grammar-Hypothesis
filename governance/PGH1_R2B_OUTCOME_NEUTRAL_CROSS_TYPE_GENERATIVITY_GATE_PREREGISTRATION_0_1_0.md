# PGH-1 R2B Outcome-Neutral Cross-Type Generativity Gate — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_R2B_OUTCOME_NEUTRAL_CROSS_TYPE_GENERATIVITY_GATE
REGISTRY_ID = PGH-OP-0050
CANONICAL_BASE = 52f72bfca5a60f552d974d4b0c98705f104dcdfb
ANCHOR_SCHEMA = PGH-OBJ-0010
CANDIDATE_FAMILY = PGH-GRAM-0003..PGH-GRAM-0007
COMMON_BRIDGE_SCHEMA = PGH-OBJ-0023
R2_TARGET = PGH-OBJ-0021
NEW_SOURCE_SEARCH = FORBIDDEN
EMPIRICAL_DATA = FORBIDDEN
PHYSICAL_RESPONSE_INTERPRETATION = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Test whether a genuinely outcome-neutral cross-type relation between law-free empirical context labels and record labels can be nontrivial without importing additional context-record structure that already carries selective information.

The gate follows `PGH-DER-0021`, which showed that the five current primitive grammar doctrines generate no atomic context-to-record morphisms under the common free-model probe.

This operation does **not** add response morphisms to those grammars. It studies the minimum formal information required for any cross-type relation to be nontrivial.

## Formal setup

Let `C` and `R` be nonempty sets of context and record labels from the law-free empirical contact signature. No correspondence, metric, ordering, probability, outcome partition, or response relation between them is assumed.

Let

\[
S\subseteq C\times R
\]

be a candidate formal cross-type relation.

The full independent relabeling group is

\[
G=S_C\times S_R,
\]

acting by

\[
(\sigma,\tau)\cdot(c,r)=(\sigma(c),\tau(r)).
\]

This action formalizes the strongest label-neutrality condition available when the anchor gives `C` and `R` separately but supplies no cross-type relation between them.

## Locked theorem T1 — transitive-orbit dichotomy

Test:

> If `S` is invariant under the full independent relabeling action of `S_C x S_R`, must `S` be either empty or all of `C x R`?

Required proof route:

1. show the action on `C x R` is transitive;
2. show an invariant subset is a union of action orbits;
3. conclude that only `empty` and `C x R` are invariant.

No finite enumeration is sufficient by itself; the general proof is required.

## Locked theorem T2 — equivariant deterministic-map control

Where `|R| > 1`, test whether a function

\[
f:C\to R
\]

can be equivariant under independent relabeling in the natural sense

\[
f(\sigma c)=\tau f(c)
\]

for all independently chosen `sigma` and `tau`.

This is a strengthening/control on the relational theorem. Degenerate cardinality exceptions must be stated rather than hidden.

## Countercontrol C1 — coupled relabeling

If `C` and `R` are supplied with an additional bijection

\[
\phi:C\to R,
\]

then a coupled relabeling action may preserve relations such as the graph of `phi`.

The gate must treat `phi` as **additional cross-type structure**. It may demonstrate how the empty/full obstruction is escaped, but it may not receive explanatory credit merely because the resulting relation is invariant under the reduced/coupled symmetry.

## Countercontrol C2 — structured orbit decomposition

More generally, if extra structure reduces the acting group so that `C x R` splits into several orbits, then nontrivial invariant relations can be formed as unions of those orbits.

The gate must explicitly charge the orbit decomposition to the added structure. It may not infer that invariance itself generated the selectivity.

## Countercontrol C3 — empty/full semantic ceiling

Neither extreme is automatically physical law:

```text
EMPTY_RELATION = FORMAL_EXTREME_NOT_NO_RESPONSE_PREDICTION
FULL_RELATION = FORMAL_EXTREME_NOT_ALL_RESPONSES_POSSIBLE_PREDICTION
```

A later physical interpretation is separately required.

## Anti-smuggling firewall

The following are forbidden as primitive inputs in this gate:

```text
TARGET_RESPONSE_TABLE
CONTEXT_TO_RECORD_FUNCTION
PROBABILITY_OR_AMPLITUDE_KERNEL
EMPIRICALLY_CHOSEN_PARTITION
POST_HOC_CONTEXT_RECORD_CORRESPONDENCE
MODEL_SELECTED_BY_EMPIRICAL_FIT
```

If a nontrivial relation is obtained only after one of these is supplied, the relation is not outcome-neutral at the present explanatory level.

## Outcome space

```text
A = FULL_INDEPENDENT_RELABELING_FORCES_THE_EMPTY_OR_COMPLETE_DICHOTOMY_AND_EVERY_NONTRIVIAL_ESCAPE_REQUIRES_ADDITIONAL_CROSS_TYPE_OR_ORBIT_STRUCTURE__OUTCOME_NEUTRAL_RELATION_ALONE_DOES_NOT_SUPPLY_R2B_BRIDGE_SELECTIVITY
B = A_NONTRIVIAL_PROPER_CROSS_TYPE_RELATION_SURVIVES_FULL_INDEPENDENT_RELABELING_WITHOUT_ADDITIONAL_CROSS_TYPE_STRUCTURE__A_NEW_FORMAL_BRIDGE_ROUTE_IS_JUSTIFIED
C = THE_EMPTY_FULL_THEOREM_HOLDS_BUT_ONE_OR_MORE_EXISTING_ACCEPTED_PGH_GRAMMAR_OR_ANCHOR_STRUCTURES_ALREADY_SUPPLY_NON_RESULT_DIRECTED_CROSS_TYPE_ORBIT_STRUCTURE_SUFFICIENT_FOR_A_SEPARATE_BRIDGE_TEST
D = THE_NOTION_OF_OUTCOME_NEUTRALITY_USED_HERE_IS_FORMALLY_INCOHERENT_OR_TOO_STRONG_TO_TEST_THE_INTENDED_BRIDGE_PROBLEM
```

No outcome satisfies R2B or establishes physical response meaning.

## Required outputs

Commit 2 may add only:

```text
audits/PGH1_R2B_OUTCOME_NEUTRAL_CROSS_TYPE_GENERATIVITY_GATE_0_1_0.md
research/formalizations/PGH1_OUTCOME_NEUTRAL_CROSS_TYPE_RELATION_SCHEMA_0_1_0.md
research/derivations/PGH_DERIVATION_INDEPENDENT_RELABELING_CROSS_TYPE_DICHOTOMY_0_1_0.md
research/failures/PGH_FAIL_CROSS_TYPE_SYMMETRY_BREAKING_AS_HIDDEN_RESPONSE_STRUCTURE_0_1_0.md
handoffs/PGH1_R2B_OUTCOME_NEUTRAL_CROSS_TYPE_GENERATIVITY_GATE_HANDOFF_0_1_0.md
```

Expected object identities if earned:

```text
PGH-OBJ-0024 = OUTCOME_NEUTRAL_CROSS_TYPE_RELATION_SCHEMA
PGH-DER-0022 = INDEPENDENT_RELABELING_CROSS_TYPE_DICHOTOMY
PGH-FAIL-0024 = CROSS_TYPE_SYMMETRY_BREAKING_AS_HIDDEN_RESPONSE_STRUCTURE
```

## Commit topology

```text
COMMIT_1_MESSAGE = Preregister PGH-1 R2B outcome-neutral cross-type generativity gate
COMMIT_2_MESSAGE = Adjudicate PGH-1 R2B outcome-neutral cross-type generativity gate
EXACT_COMMITS = 2
```

## Hard stops

```text
DO_NOT_SEARCH_NEW_SOURCES
DO_NOT_USE_EMPIRICAL_RESPONSE_DATA
DO_NOT_ADD_TARGET_SPECIFIC_RESPONSE_ARROWS
DO_NOT_CALL_RELATION_MEMBERSHIP_PHYSICAL_RESPONSE
DO_NOT_TREAT_COUPLED_LABEL_STRUCTURE_AS_FREE
DO_NOT_DECLARE_CURRENT_GRAMMARS_PHYSICALLY_REFUTED
DO_NOT_DECLARE_R2B_SATISFIED
DO_NOT_MAKE_EMPIRICAL_PREDICTIONS
DO_NOT_CHANGE_FCP
```