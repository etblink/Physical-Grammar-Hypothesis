# PGH-1 Post-Kp Network/Source Successor Package Completion and Admission Gate — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_POST_KP_NETWORK_SOURCE_SUCCESSOR_PACKAGE_COMPLETION_AND_ADMISSION_GATE
REGISTRY_ID = PGH-OP-0106
CANONICAL_BASE = 1c340760c5a1266b509cfd10a4b299ab0231be69
FORMAL_GRAMMAR = PGH-GRAM-0010
SEMANTIC_BRIDGE = PGH-OBJ-0051
ADMISSION_STANDARD = PGH-OBJ-0040
TARGET_DISCOVERY = FORBIDDEN
TARGET_METADATA_ACCESS = FORBIDDEN
EMPIRICAL_DATA = FORBIDDEN
NEW_SOURCE_SEARCH = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Complete one target-free successor identity

\[
\mathcal C=(G,J,S,I)
\]

for `PGH-GRAM-0010`, then apply the hard A0-A9 post-Kp strong-PGH admission standard.

This operation may establish only **target-discovery eligibility**. It may not discover, rank, inspect, or freeze an empirical target.

## Frozen inherited components

```text
G = PGH-GRAM-0010
  INDEPENDENT_SOURCE_TRIANGLE_PRIMITIVE_GRAMMAR_CANDIDATE

J = PGH-OBJ-0051
  FULL_OBSERVED_MODEL_CLASS_RELABELING_BRIDGE

OBSERVED_FORMAL_CLASS = T_ind

LATENT_SOURCE_PHYSICAL_ONTOLOGY = NONE
LOCAL_KERNEL_SELECTION = FORBIDDEN
MODEL_SUBSET_SELECTION = FORBIDDEN
```

No modification to `G` or `J` is permitted inside this gate.

## Proposed scope family

Only the already-qualified strong-PGH-compatible universal scope is eligible here:

```text
S = TRUE_FOR_ALL_I_ELIGIBLE_PHYSICAL_RECORD_INTERFACES
S_ORIGIN_CLASS = F0_UNIVERSAL
```

No restricted physical regime, known network architecture, causal-source metadata, laboratory-design condition, or external source-independence fact may be used to define scope.

If universal scope makes the package scientifically harsh, that is a feature of falsification exposure rather than a reason to narrow scope.

## Proposed prospective instantiation protocol `I`

`I` must remain outcome-neutral and source-ontology-neutral.

### Eligible empirical record interface

A candidate discovery unit is eligible only if metadata establishes all of:

```text
PUBLIC_OR_AUDITABLE_EVENT_LEVEL_ACCESS = YES
VERSIONED_OR_STABLY_IDENTIFIED_DATA_AUTHORITY = YES
REPEATED_JOINT_RECORD_INDEX = YES
AT_LEAST_THREE_DISTINCT_NATIVE_BINARY_RECORD_FIELDS = YES
JOINT_OBSERVATION_OF_SELECTED_FIELDS_PER_RECORD = YES
MISSINGNESS_OR_VALIDITY_CODES_DOCUMENTED = YES
OUTCOME_VALUES_NOT_REQUIRED_FOR_ELIGIBILITY = YES
```

`native binary` means the authoritative record specification exposes exactly two substantive states before missing/invalid codes. Target-specific thresholding, binning, state merging, learned encoding, or response-derived discretization is forbidden for the first test of this candidate identity.

### Field selection within an eligible discovery unit

If exactly three eligible binary fields exist, use all three.

If more than three exist:

1. identify eligible fields from metadata only;
2. order by stable authority-defined field identifier, using Unicode code-point lexical order on the exact identifier string after no semantic renaming;
3. select the first three.

This is an administrative canonicalization rule, not a scientific claim that earlier identifiers are more physical.

### Role assignment

Because the observable triangle grammar is symmetric under permutations of its three observed nodes:

```text
A/B/C_HAVE_NO_DISTINCT_PHYSICAL_ROLE_SEMANTICS
```

Assign the three selected binary field identifiers to `A,B,C` in the same canonical lexical order.

No temporal, causal, upstream/downstream, spatial, or resource interpretation is required or credited.

### Repeated records

Each valid jointly observed record contributes one empirical triple `(A,B,C)`.

The later target-specific preregistration must freeze handling of duplicate record IDs, missing/invalid codes, time collisions, quality flags, and any dependence-preserving resampling or segmentation before materializing response values.

### Target-discovery metadata firewall

A later target-discovery operation may inspect only metadata needed to establish:

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

It may not inspect or derive:

```text
JOINT_OR_MARGINAL_COUNTS
CORRELATIONS
MUTUAL_INFORMATION
CONDITIONAL_INDEPENDENCE
MODEL_FIT_TO_T_ind
LATENT_NETWORK_FIT
ENTROPY_OR_ASSOCIATION_STATISTICS
TARGET_RESPONSE_VALUES
```

### Tie-breaking among eligible discovery units

A later target-discovery operation must first preregister a bounded metadata-only search procedure and close its discovered candidate set without response inspection.

Among all eligible discovery units in that closed set, choose the lexicographically smallest tuple

```text
(CANONICAL_AUTHORITY_NAME, STABLE_DATASET_IDENTIFIER, VERSION_OR_RELEASE_IDENTIFIER)
```

using exact metadata strings and Unicode code-point order.

If exact tuple identity is duplicated across mirrors, prefer the authority-hosted copy. If the authority itself provides multiple access encodings of the same version, prefer the least transformed event-level representation according to the authority documentation; if still tied, lexical access-path order decides.

No ranking by scientific familiarity, expected independence, causal-network interpretation, or apparent suitability for `T_ind` is allowed.

## Known-result quarantine

The following are known before this package freeze and may not provide positive successor credit:

```text
KP_TGT001 = KNOWN_FAILED_HISTORICAL_RESULT
HURDAT2_TGT008 = KNOWN_FAILED_FIVE_CANDIDATE_RESULT
ALL_TARGET_IDENTITIES_DISCOVERED_BEFORE_THIS_PACKAGE_FREEZE = INELIGIBLE_FOR_FIRST_POSITIVE_CREDIT
```

The package may use methodological lessons already canonically frozen, including full `C=(G,J,S,I)` identity and exact stochastic implementation semantics.

It may not inspect Kp, HURDAT2, or any older target to determine whether `PGH-GRAM-0010` fits them. Compatibility earns zero positive credit. A logically forced incompatibility may count only as negative evidence under a separately authorized analysis.

The first positive empirical credit, if ever earned, must come from a genuinely new target discovered after this package is canonically frozen.

## A5 failure and revision policy to test

The candidate package must adopt at minimum:

```text
VALID_PROSPECTIVE_REJECTION_OF_T_ind = REFUTED_AT_TARGET
VALID_TEST_NOT_REJECTING_T_ind = SURVIVES_TARGET_TEST__NOT_CONFIRMATION
CALIBRATION_OR_MODEL_MEMBERSHIP_INDETERMINACY = INCONCLUSIVE
```

After exposure, any change to `G`, `J`, `S`, native-binary eligibility, field-selection rule, role assignment, or target-selection rule creates a new candidate identity unless generated by an already-frozen deterministic rule.

No source-independence weakening, topology change, discretization change, subset selection, exception, scope restriction, or latent-resource repair may be made in place after a failure.

## A7 empirical-preregistration readiness contract

If the package passes A0-A9 and a later target is frozen, a separate pre-data analysis preregistration must either:

1. specify a valid finite-sample test/decision functional for compatibility with `T_ind`, plus adversarial controls; or
2. stop the empirical sequence as `ANALYSIS_NOT_YET_QUALIFIED` without accessing target response values.

It must freeze all items required by `PGH-OBJ-0040`, including support/missingness rules, indexing, decision threshold, verdict mapping, data hashes/custody, and any optimization tolerances or convergence rules needed for latent-model membership analysis.

Candidate admission here does not certify that such an analysis has already been constructed.

## A8 implementation-reproducibility contract

Any later stochastic, simulation, optimization-with-random-starts, permutation, bootstrap, Monte Carlo, or randomized search procedure must freeze all implementation semantics required by `PGH-OBJ-0040` before data materialization.

If the later analysis is fully deterministic, every stochastic item must be explicitly marked `NOT_APPLICABLE` and deterministic numerical tolerances/runtime semantics must still be frozen.

## A9 proposed claim class

Because `S=TRUE` uses the already-qualified F0 scope architecture, the package seeks only:

```text
CLAIM_CLASS = STRONG_PGH_CANDIDATE
```

A pass means only `TARGET_DISCOVERY_ELIGIBLE=YES`.

It does not mean strong PGH is confirmed, the triangle is physically true, latent sources are real, or R2B has been empirically satisfied.

## Admission matrix to execute

The adjudication must issue explicit PASS/FAIL for:

```text
A0_IDENTITY_AND_PROVENANCE
A1_FORMAL_GRAMMAR_G
A2_SEMANTIC_BRIDGE_J
A3_PHYSICAL_SCOPE_S
A4_PROSPECTIVE_INSTANTIATION_I
A5_FAILURE_COST_AND_REVISION_IDENTITY
A6_KNOWN_RESULT_QUARANTINE
A7_EMPIRICAL_PREREGISTRATION_READINESS
A8_IMPLEMENTATION_REPRODUCIBILITY
A9_CLAIM_CEILING_AND_STRONG_VS_WEAK_LABELING
```

No weighted compensation is permitted.

## Outcome space

```text
A = COMPLETE_NETWORK_SOURCE_SUCCESSOR_PACKAGE_PASSES_A0_A9__FREEZE_NEW_CANDIDATE_IDENTITY__TARGET_DISCOVERY_ELIGIBLE__STOP

B = PROSPECTIVE_INSTANTIATION_I_CANNOT_BE_MADE_OUTCOME_NEUTRAL_WITHOUT_EXTERNAL_SOURCE_ARCHITECTURE_OR_RESPONSE_INFORMATION__ROUTE_FORMAL_ONLY__STOP

C = ONE_OR_MORE_OTHER_A0_A9_GATES_FAIL__NO_STRONG_PGH_ADMISSION__STOP

D = SPECIFIC_FORMAL_OR_SOURCE_INFORMATION_GAP_PREVENTS_COMPLETE_ADJUDICATION__NO_ADMISSION_CREDIT__STOP

E = PACKAGE_REQUIRES_INDEPENDENT_F3_PHYSICAL_SCOPE_OR_EQUIVALENT_EXTERNAL_PHYSICS__DOWNGRADE_TO_WEAKER_EFFECTIVE_OR_CONDITIONAL_PGH__STOP
```

## Required outputs if adjudication proceeds

The result commit may add only:

```text
research/candidates/PGH1_POST_KP_NETWORK_SOURCE_SUCCESSOR_PACKAGE_0_1_0.md
audits/PGH1_POST_KP_NETWORK_SOURCE_SUCCESSOR_PACKAGE_ADMISSION_LEDGER_0_1_0.md
audits/PGH1_POST_KP_NETWORK_SOURCE_SUCCESSOR_PACKAGE_COMPLETION_AND_ADMISSION_GATE_0_1_0.md
handoffs/PGH1_POST_KP_NETWORK_SOURCE_SUCCESSOR_PACKAGE_COMPLETION_AND_ADMISSION_GATE_HANDOFF_0_1_0.md
```

If and only if Outcome A passes, the package receives the next stable `PGH-OBJ` identity in the result commit.

No navigation surfaces are modified inside OP-0106.

## Hard stop

```text
STOP_BEFORE_TARGET_DISCOVERY
STOP_BEFORE_TARGET_METADATA_ACCESS
STOP_BEFORE_EMPIRICAL_DATA
STOP_BEFORE_TARGET_SPECIFIC_STATISTIC_DESIGN
STOP_BEFORE_NEW_SOURCE_SEARCH
STOP_BEFORE_FCP_EFFECT
```

Truth over PGH.
