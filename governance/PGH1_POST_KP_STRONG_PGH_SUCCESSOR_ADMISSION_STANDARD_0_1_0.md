# PGH-1 Post-Kp Strong-PGH Successor Admission Standard 0.1.0

## Identity

```text
OBJECT_ID = PGH-OBJ-0040
OBJECT_NAME = POST_KP_STRONG_PGH_SUCCESSOR_ADMISSION_STANDARD
DECLARING_OPERATION = PGH-OP-0078
STATUS = QUALIFIED_GOVERNANCE_AND_SCIENTIFIC_ADMISSION_STANDARD
APPLIES_TO = ALL_POST_KP_CANDIDATES_SEEKING_STRONG_PGH_EMPIRICAL_CREDIT
FCP_EFFECT = NONE
```

## Purpose

This standard defines the minimum complete identity and hard-gate requirements for any future post-Kp candidate that seeks empirical credit for **strong PGH**.

It is intentionally stricter than the pre-Kp workflow because the first empirical confrontation exposed two distinct vulnerabilities:

1. physical scope was not part of the candidate identity before target selection;
2. stochastic implementation semantics were not completely frozen despite deterministic seed derivation.

The standard does not claim that satisfying these gates makes a candidate true or plausible. It only makes the candidate scientifically admissible for a prospective strong-PGH empirical test.

## Core candidate identity

Before empirical target discovery begins, the candidate must be frozen as

\[
\mathcal C=(G,J,S,I),
\]

with explicit lineage and version identity.

- `G` = formal grammar / model-class generator and its selective consequences;
- `J` = semantic bridge from the admitted formal model class to physical/empirical interpretation;
- `S` = physical applicability statement or scope-origin mechanism;
- `I` = prospective instantiation protocol mapping eligible systems/records to candidate roles.

If any component is generated from another, the derivation is part of candidate identity and must be frozen with it.

```text
TARGET_DISCOVERY_BEFORE_CANDIDATE_FREEZE = FORBIDDEN
TARGET_OUTCOME_USE_IN_CANDIDATE_SELECTION = FORBIDDEN
POST_EXPOSURE_G_J_S_I_CHANGE_UNDER_SAME_IDENTITY = FORBIDDEN
```

## Admission state machine

```text
DISCOVERY_ONLY
  -> FORMAL_AND_SEMANTIC_PACKAGE_COMPLETE
  -> STRONG_PGH_ADMISSION_REVIEW
  -> ADMISSION_PASS
  -> TARGET_DISCOVERY_ELIGIBLE
  -> TARGET_FROZEN
  -> EXPERIMENT_SPECIFIC_PREREGISTRATION_FROZEN
  -> DATA_CUSTODY
  -> EMPIRICAL_EXECUTION
```

No later state may be used to modify an earlier frozen state under the same candidate identity.

A failed admission gate routes the object to one of:

```text
FORMAL_ONLY
WEAKER_OR_EFFECTIVE_PGH
REVISED_NEW_CANDIDATE_IDENTITY
REJECTED
```

It does not route to `STRONG_PGH_ADMISSION_PASS` by averaging against other favorable properties.

## A0 — identity and provenance

Mandatory:

```text
NEW_POST_KP_CANDIDATE_ID
EXACT_VERSION
CANONICAL_PARENT_OR_LINEAGE
EXPLICIT_RELATION_TO_PGH_GRAM_0008
PRE_KP_VS_POST_KP_PROVENANCE_VISIBLE
TARGET_DISCOVERY_NOT_STARTED
```

A successor is a new hypothesis identity. It may inherit formal lessons from `PGH-GRAM-0008`, but it may not be presented as if its post-Kp changes belonged to the failed pre-Kp candidate.

## A1 — formal grammar `G`

`G` must specify, before target discovery:

- primitives / objects / generators;
- signature, arity and typing/interface structure as applicable;
- formation/composition rules;
- any equations, coherence, symmetry or rewrite rules;
- the admitted model class;
- at least one nontrivial formal consequence or exclusion;
- a countermodel or explicit outside-model witness where feasible;
- a universal/nonselective control demonstrating why the candidate is not merely an arbitrary complete encoder.

Strong-PGH admission fails if the operative response class is effectively an unrestricted table, complete model family, target-specific extensional list, or universal encoder.

```text
FORMAL_SELECTIVITY = REQUIRED
RULE_FORM_ALONE = INSUFFICIENT
SHORT_DESCRIPTION_ALONE = INSUFFICIENT
MATHEMATICAL_NOVELTY_CLAIM = NOT_REQUIRED
```

## A2 — semantic bridge `J`

`J` must be fixed for the **entire admitted model class**, not chosen separately for favorable models.

It may include legitimate fixed relabeling, units, representation maps, measurement roles or law-free reference contact.

It may not:

- choose favorable kernels/parameters after target inspection;
- choose a favorable subset of formal models;
- add target-specific equations needed for the prediction;
- use the target response table to define interpretation;
- treat causal/physical semantics as earned merely because a formal arrow exists.

```text
SEMANTIC_MODEL_SELECTION_CREDIT = FORBIDDEN
POSTHOC_MODEL_CLASS_RESTRICTION = FORBIDDEN
```

## A3 — physical scope `S`

`S` is mandatory and explicit before target discovery.

### Strong-PGH admissible forms

```text
S = TRUE
```

or a restricted `S` whose origin has already qualified under one of the non-relocating routes:

```text
F1 = G_OR_J_INTERNAL_DERIVATION_WITH_ANTI_ENCODING_AND_REPRESENTATION_PASS
F2 = GENUINELY_LAW_FREE_SEMANTIC_OR_REFERENCE_CONDITION_WITH_RESPONSE_FIREWALL_PASS
F4 = HIGHER_LEVEL_SELECTOR_THAT_ITSELF_PASSES_THE_SAME_ORIGIN_STANDARD_AND_TERMINATES
```

### Not sufficient for strong-PGH admission by itself

```text
F3 = INDEPENDENT_PHYSICAL_SECTOR_OR_EFFECTIVE_REGIME_CONDITION
```

Scale hierarchy, symmetry, coupling, equilibrium, degrees of freedom, causal/environmental structure, or other independent substantive physics may define excellent ordinary scientific scope. If those facts are external to the PGH candidate, the candidate must be labeled weaker/effective/conditional PGH rather than receiving strong-PGH law-exhaustion credit.

```text
PROSPECTIVE_NAMING_ALONE = INSUFFICIENT
FIT_DEFINED_SCOPE = REJECT
RESULT_DEFINED_SCOPE = REJECT
UNRESTRICTED_SCOPE_PREDICATE_LANGUAGE = REJECT
```

## A4 — prospective instantiation `I`

`I` must freeze how physical systems/records become candidate variables, roles, events, contexts or trials.

It must specify:

- eligibility conditions;
- role assignment;
- temporal/spatial ordering if relevant;
- native state/alphabet treatment;
- allowed relabelings;
- target discovery metadata fields;
- tie-breaking among eligible targets;
- exclusion rules independent of candidate outcome behavior.

It may not inspect or rank targets by:

- predicted relation;
- conditional independence/Markov fit;
- residuals;
- correlation structure;
- candidate statistic;
- favorable historical result;
- target-specific parameter fit.

```text
TARGET_SELECTION_PROTOCOL != PHYSICAL_SCOPE
TARGET_DISCOVERY = ALLOWED_ONLY_AFTER_ADMISSION_PASS
```

## A5 — failure cost and revision identity

Before empirical exposure, the candidate must state what results count as failure, survival, or inconclusive calibration.

After exposure:

- a failed target remains a failed target for that candidate identity;
- changing `G`, `J`, restricted `S`, or `I` creates a new/revised identity unless the change follows an already-frozen deterministic rule;
- adding an edge, equation, exception, scope restriction or semantic condition because of a result is a new candidate;
- a universal control cannot be promoted into an explanation merely to avoid exclusion.

```text
FAILURE_MUST_BE_COSTLY = YES
POST_RESULT_RESCUE_UNDER_SAME_IDENTITY = NO
```

## A6 — known-result quarantine

The project already knows the Kp result and the failure mode of `PGH-GRAM-0008`.

A successor may use the **methodological lesson** that candidate identity must include scope and complete implementation semantics.

It may not receive positive evidence from having been designed after that result.

```text
KNOWN_KP_INCOMPATIBILITY = MAY_REFUTE_A_SUCCESSOR_IF_LOGICALLY_ENTAILED
KNOWN_KP_COMPATIBILITY = ZERO_PROSPECTIVE_CONFIRMATION_CREDIT
KP_AS_FIRST_POSITIVE_SUCCESSOR_TEST = FORBIDDEN
DETAILED_KP_PATTERN_MINING_FOR_SUCCESSOR_DESIGN = FORBIDDEN
```

The first positive empirical credit for a successor must come from a genuinely prospective target whose relevant behavior was not used to construct, select or tune the successor.

## A7 — empirical preregistration readiness

Candidate-level admission must precede target discovery.

After a target is prospectively frozen and before data materialization, the experiment-specific preregistration must freeze:

- primary statistic or decision functional;
- null/control structure;
- support/missingness rules;
- sample segmentation and indexing;
- resampling/replicate counts;
- alpha/decision thresholds;
- exact verdict mapping;
- data authority/custody path and hashes.

A target-specific statistic may therefore be chosen **after target freeze but before data access**, provided it is not selected from target outcomes.

## A8 — implementation reproducibility

For stochastic or simulation-based inference, seed derivation is not enough.

Before data materialization, freeze:

```text
PRNG_ALGORITHM
RANDOM_WORD_WIDTH_AND_ENDIANNESS_IF_RELEVANT
WORD_TO_BOUNDED_INTEGER_MAPPING
REJECTION_OR_MODULO_RULE
UNIFORM_FLOAT_MAPPING
PERMUTATION_ALGORITHM
CATEGORICAL_SAMPLER
TIE_HANDLING
QUANTILE_CONVENTION
P_VALUE_CONVENTION
SOFTWARE_RUNTIME_AND_VERSION_ASSUMPTIONS
DETERMINISTIC_SEED_DERIVATION
```

If an item is inapplicable, mark it explicitly `NOT_APPLICABLE` rather than leaving it unspecified.

## A9 — claim ceiling and hypothesis class

Every admitted object must state which claim class it seeks:

```text
STRONG_PGH_CANDIDATE
WEAKER_EFFECTIVE_OR_CONDITIONAL_PGH_CANDIDATE
FORMAL_ONLY_OBJECT
```

A candidate relying on independent F3 physical scope defaults to the weaker/effective class unless the relevant scope-generating physics has itself been PGH-compatibly internalized.

No single empirical survival establishes strong PGH, uniqueness, fundamental ontology, or universal physical grammar.

## Hard-gate rule

```text
STRONG_PGH_ADMISSION_PASS = A0_PASS AND A1_PASS AND A2_PASS AND A3_PASS AND A4_PASS AND A5_PASS AND A6_PASS AND A7_PASS AND A8_PASS AND A9_PASS
```

There is no weighted compensation.

A single hard-gate failure means:

```text
STRONG_PGH_ADMISSION = FAIL
```

until a new/revised candidate identity is constructed and reviewed.

## Required admission record for each future candidate

Each candidate seeking strong-PGH admission must have a frozen record containing at minimum:

```text
CANDIDATE_ID
CANDIDATE_VERSION
LINEAGE
G_ARTIFACT
J_ARTIFACT
S_ARTIFACT_OR_UNIVERSAL_DECLARATION
S_ORIGIN_CLASS
I_ARTIFACT
FORMAL_SELECTIVITY_WITNESS
COUNTERMODEL_OR_EXCLUSION_WITNESS
UNIVERSAL_CONTROL
REPRESENTATION_DISCIPLINE_STATEMENT
KNOWN_RESULT_QUARANTINE_STATEMENT
FAILURE_AND_REVISION_RULE
CLAIM_CLASS
A0_A9_VERDICTS
TARGET_DISCOVERY_ELIGIBLE = YES_OR_NO
```

## Candidate-family selection rule

If a target-free generation operation produces multiple candidates, candidate selection or pruning may use only frozen formal/admission criteria.

No empirical target metadata, behavior or known favorable fit may break ties.

If multiple candidates survive without a target-free principled tie-break, the project must either carry the plurality forward under a preregistered multiplicity rule or perform another target-free selection gate. It may not inspect targets to choose the winner.

## Consequence for PGH-GRAM-0008

```text
PGH_GRAM_0008 = FORMAL_METHOD_CONTROL
PHYSICAL_TESTING = RETIRED
KP_FAILURE = RETAINED
POST_KP_STANDARD_APPLIED_RETROACTIVELY_TO_CHANGE_HISTORY = NO
```

The new standard governs successors; it does not rewrite the historical test.

## Next permitted scientific class

After this standard is canonical and navigation is reconciled, the next target-free operation may generate and screen a finite successor candidate family under A0-A9.

```text
NEXT_RECOMMENDED_OPERATION = PGH1_POST_KP_STRONG_PGH_SUCCESSOR_CANDIDATE_GENERATION_AND_ADMISSION_SCREEN
```

That operation must still stop before empirical target discovery.
