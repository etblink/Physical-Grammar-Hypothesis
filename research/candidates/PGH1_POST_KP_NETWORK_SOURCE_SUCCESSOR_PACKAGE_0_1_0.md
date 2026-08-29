# PGH-OBJ-0052 — Post-Kp Independent-Source Triangle Strong-PGH Successor Package 0.1.0

## Status

```text
OBJECT_ID = PGH-OBJ-0052
DECLARING_OPERATION = PGH-OP-0106
PACKAGE_CLASS = STRONG_PGH_CANDIDATE
STATUS = TARGET_DISCOVERY_ELIGIBLE_CANDIDATE_PACKAGE
EMPIRICAL_VALIDATION = NONE
R2B = UNSATISFIED
FCP_EFFECT = NONE
```

## Complete frozen identity

\[
\mathcal C_{\triangle}=(G,J,S,I).
\]

```text
G = PGH-GRAM-0010
J = PGH-OBJ-0051
S = TRUE_FOR_ALL_I_ELIGIBLE_PHYSICAL_RECORD_INTERFACES
S_ORIGIN_CLASS = F0_UNIVERSAL
I = SYMMETRIC_NATIVE_BINARY_TRIPLE_RECORD_INSTANTIATION_PROTOCOL_V0_1_0
```

This package is frozen before target discovery.

## G — formal grammar

`PGH-GRAM-0010` fixes:

- three observed binary nodes;
- three pairwise latent sources arranged in a triangle;
- mutual independence of the latent sources;
- arbitrary finite latent cardinalities;
- arbitrary local stochastic kernels consistent with source incidence.

Its observable class is `T_ind`.

Qualified formal consequences include:

- the nondegenerate perfect-common-bit distribution is excluded (`PGH-DER-0033`);
- the class is not equivalent to the retired three-node path-CI family (`PGH-DER-0034`);
- correlated-source and common-source controls restore excluded behavior.

No physical ontology is assigned to the latent sources.

## J — semantic bridge

`PGH-OBJ-0051` maps the entire observable class `T_ind` to prospective empirical joint distributions on three binary record roles.

```text
FULL_CLASS_REALIZATION = YES
PROPER_SUBSET_SELECTION = NO
LOCAL_KERNEL_SELECTION = NO
LATENT_SOURCE_PHYSICAL_IDENTIFICATION = NO
NEW_RESPONSE_EQUATION = NO
EMPIRICAL_FIT = NO
```

The empirical statement is only:

\[
p_{emp}(\mathcal A,\mathcal B,\mathcal C)\in T_{ind}.
\]

## S — physical scope

```text
S = TRUE
```

The candidate claims applicability to every physical record interface that satisfies `I`.

No scale, regime, causal architecture, laboratory design, independent-source metadata, or external physical sector is used to narrow applicability.

This maximizes falsification exposure and avoids auxiliary scope-law relocation.

## I — prospective instantiation protocol

### Eligibility

A discovery unit is eligible only when metadata establishes:

```text
PUBLIC_OR_AUDITABLE_EVENT_LEVEL_ACCESS = YES
VERSIONED_OR_STABLY_IDENTIFIED_AUTHORITY = YES
REPEATED_JOINT_RECORD_INDEX = YES
AT_LEAST_THREE_DISTINCT_NATIVE_BINARY_RECORD_FIELDS = YES
SELECTED_FIELDS_JOINTLY_OBSERVED_PER_RECORD = YES
MISSINGNESS_OR_VALIDITY_CODES_DOCUMENTED = YES
```

No response values are needed to establish eligibility.

### Native-binary firewall

A field is eligible only when its authoritative schema declares exactly two substantive states, excluding missing/invalid codes.

Forbidden for the first test under this identity:

```text
TARGET_SPECIFIC_THRESHOLDING
BINNING
STATE_MERGING
LEARNED_ENCODING
RESPONSE_DERIVED_DISCRETIZATION
```

### Field selection

- If exactly three eligible binary fields exist, use all three.
- If more than three exist, sort the exact authority-defined field identifiers by Unicode code-point lexical order and use the first three.

### Role assignment

Sort the selected field identifiers by the same rule and assign them to `A,B,C` in order.

The role labels have no distinct physical semantics. The grammar is symmetric under observed-node permutations, so this canonicalization adds no causal, temporal, spatial, or resource claim.

### Repeated records

Every later valid jointly observed record contributes one empirical triple `(A,B,C)` after target-specific missingness/quality handling is frozen pre-data.

### Metadata allowed during target discovery

Only:

```text
AUTHORITY_AND_STABLE_ID
VERSION_OR_RELEASE_ID
ACCESS_PATH
RECORD_INDEX_DESCRIPTION
FIELD_IDENTIFIERS
NATIVE_FIELD_ALPHABETS
JOINT_INDEXABILITY
DOCUMENTED_MISSINGNESS_VALIDITY_CODES
DECLARED_RECORD_COUNT_OR_COVERAGE_IF_METADATA_SUPPLIES_IT
```

Forbidden during target discovery:

```text
RESPONSE_VALUES
JOINT_OR_MARGINAL_COUNTS
CORRELATIONS
MUTUAL_INFORMATION
CONDITIONAL_INDEPENDENCE
T_ind_FIT
LATENT_NETWORK_FIT
ENTROPY_OR_ASSOCIATION_STATISTICS
```

### Target tie-break

After a separately preregistered bounded metadata-only discovery pass closes its candidate set, select the lexicographically smallest exact metadata tuple:

```text
(CANONICAL_AUTHORITY_NAME, STABLE_DATASET_IDENTIFIER, VERSION_OR_RELEASE_IDENTIFIER)
```

Authority-hosted copy beats a mirror for duplicate identity; remaining access-path ties are lexical.

No target may be preferred because it is known, believed, or designed to contain independent physical sources.

## Failure and revision identity

A later qualified empirical test has only these candidate-level meanings:

```text
REJECT_T_ind = REFUTED_AT_TARGET
DO_NOT_REJECT_T_ind = SURVIVES_TARGET_TEST__NOT_CONFIRMATION
QUALIFIED_ANALYSIS_CANNOT_RESOLVE = INCONCLUSIVE
```

After exposure, any change to `G`, `J`, `S`, native-binary eligibility, field-selection/role rule, or target-selection rule creates a new candidate identity unless an already-frozen deterministic rule requires it.

No topology repair, source-correlation relaxation, discretization repair, subset selection, scope narrowing, or semantic exception is permitted in place.

## Known-result quarantine

```text
Kp_TGT001 = ZERO_POSITIVE_CREDIT
HURDAT2_TGT008 = ZERO_POSITIVE_CREDIT
ANY_PRE_FREEZE_DISCOVERED_TARGET = INELIGIBLE_FOR_FIRST_POSITIVE_CREDIT
```

No Kp or HURDAT2 compatibility analysis was used to admit this package.

The first positive empirical credit, if any, must arise from a new target discovered only after this package freeze.

## Empirical-preregistration readiness

After a new target is frozen and before response data are materialized, a separate analysis preregistration must either:

1. qualify a finite-sample test/decision functional for `T_ind` compatibility and all required adversarial controls; or
2. stop as `ANALYSIS_NOT_YET_QUALIFIED` without data access.

All stochastic and numerical implementation semantics required by `PGH-OBJ-0040` must be frozen at that later pre-data boundary.

## Claim ceiling

```text
TARGET_DISCOVERY_ELIGIBLE = YES
PHYSICAL_GRAMMAR_FOUND = NO
STRONG_PGH_CONFIRMED = NO
LATENT_SOURCE_ONTOLOGY_ESTABLISHED = NO
UNIQUE_GRAMMAR_ESTABLISHED = NO
EMPIRICAL_VALIDATION = NONE
R2B = UNSATISFIED
FCP_EFFECT = NONE
```

Admission means this candidate is sufficiently specified to risk a new prospective empirical failure. It does not mean it is likely to survive one.
