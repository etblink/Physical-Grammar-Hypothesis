# PGH-FAIL-0024 — Cross-Type Symmetry Breaking as Hidden Response Structure

## Status

```text
FAILURE_ID = PGH-FAIL-0024
STATUS = FAILED_PRESERVED
PHYSICAL_CLAIM = NONE
```

## Primary failure exposed by this gate

The attempted identification

```text
OUTCOME_NEUTRALITY = FULL_INDEPENDENT_PERMUTATION_AUTOMORPHY
```

fails.

Canonical `PGH-FAIL-0002` already establishes the general principle:

```text
RELABELING_COVARIANCE = REPRESENTATION_NEUTRALITY
FULL_PERMUTATION_AUTOMORPHY = SUBSTANTIVE_HOMOGENEITY
```

The same distinction applies to cross-type context-record structure.

A nontrivial relation can transform covariantly under relabeling without being fixed pointwise/setwise by every permutation of one fixed labeled carrier.

Therefore the empty/full theorem of `PGH-DER-0022` cannot be promoted to a theorem about outcome neutrality itself.

## Secondary failure — post-hoc symmetry reduction

The opposite mistake also fails.

Given any target relation

\[
S\subseteq C\times R,
\]

define its setwise stabilizer

\[
H_S=\{g\in S_C\times S_R:gS=S\}.
\]

Then `S` is invariant under `H_S` by construction.

Thus:

```text
THERE_EXISTS_A_SYMMETRY_GROUP_PRESERVING_S = TRIVIAL_IF_GROUP_MAY_BE_CHOSEN_AFTER_S
```

Selecting a reduced/coupled symmetry because it stabilizes the desired response pattern merely hides the target relation in the chosen orbit structure.

## Coupled-correspondence control

A supplied bijection `phi:C->R` can make its graph invariant under a coupled relabeling group. This is formally legitimate, but the origin of `phi` must be audited.

If `phi` is chosen after observing the desired response pairing, explanatory credit fails.

## What remains open

This failure does **not** establish that all cross-type structure is substantive response law.

A typed empirical interface may remain law-free if it is:

1. fixed independently of response data;
2. covariant under faithful representation change;
3. compatible with multiple empirically incompatible response laws while held fixed;
4. weaker than an allowed-response relation, probability rule, or target empirical partition.

That possibility is the correct next target.

## Failure classification

```text
FAILURE_CLASS = REPRESENTATION_CONFUSION; POST_HOC_SYMMETRY_SELECTION
OVERSTRONG_PREMISE = FULL_INDEPENDENT_AUTOMORPHY_AS_NEUTRALITY
HIDDEN_IMPORT_CONTROL = SETWISE_STABILIZER_OF_ARBITRARY_TARGET
WHAT_REMAINS_VALID = AUTOMORPHY_DICHOTOMY_AS_CONDITIONAL_THEOREM; COVARIANT_TYPED_INTERFACE_REMAINS_OPEN
```