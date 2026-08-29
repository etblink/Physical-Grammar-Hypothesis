# PGH-1 R2B Compositional Stochastic/Causal Source Selection Audit 0.1.0

## Identity

```text
OPERATION_ID = PGH1_R2B_COMPOSITIONAL_STOCHASTIC_CAUSAL_PROCESS_SOURCE_INTAKE
REGISTRY_ID = PGH-OP-0057
SOURCE_GAP = SG4_COMPOSITIONAL_STOCHASTIC_AND_CAUSAL_PROCESS_CONSTRAINTS
CANDIDATES_REVIEWED = 20+
ACCEPTED = 15
NEW_DISTINCT_ACCEPTED = 15
PREEXISTING_ACCEPTED = 70
TOTAL_DISTINCT_AFTER_FREEZE = 85
```

## Selection standard

Sources were admitted for distinctive mechanism coverage, not citation count or categorical vocabulary.

An accepted source had to contribute materially to at least one of:

```text
MARKOV_OR_PROBABILITY_STRUCTURE
CAUSAL_OR_BAYESIAN_NETWORK_COMPOSITION
CONDITIONAL_INDEPENDENCE_DISINTEGRATION_NORMALIZATION
EFFECTUS_OR_ADJACENT_PROBABILISTIC_PROCESS_STRUCTURE
STRUCTURAL_VS_LOCAL_MODEL_DATA_FIREWALL
```

## Authority balance

The freeze emphasizes peer-reviewed primary work and established monographs/articles.

One thesis is retained:

```text
FONG_2012_CAUSAL_THEORIES = ACCEPT
```

because it is an early direct categorical formulation of Bayesian-network syntax/semantics and makes the wiring-versus-model-functor distinction especially explicit. It is not used alone for any high-stakes source-level conclusion; later peer-reviewed causal/Markov sources provide independent coverage.

## Deduplication

All accepted titles/authors/locators were checked against:

```text
PGH0_REPRESENTATION_COHERENCE_SOURCE_REGISTER_0_1_0.md
PGH1_R2_LOCAL_GLOBAL_SOURCE_REGISTER_0_1_0.md
PGH1_R2_META_LANGUAGE_SOURCE_REGISTER_0_1_0.md
```

No exact accepted duplicate was found.

```text
DUPLICATE_ACCEPTED_COUNT = 0
NEW_DISTINCT_ACCEPTED = 15
```

Preprint/journal duplicates were collapsed into one source record using the peer-reviewed publication as the primary citation and arXiv as a secondary locator when useful.

## Mechanism coverage audit

### SG4A

Accepted core:

```text
GIRY_1982
JACOBS_2011
FRITZ_2020
FRITZ_LIANG_2023
FRITZ_GONDA_PERRONE_RISCHEL_2023
```

Coverage includes probability monads, convex/categorical probability, Markov-category axioms, free Markov structure and abstract statistical comparison.

```text
SG4A = PASS
```

### SG4B

Accepted core:

```text
FONG_2012
FRITZ_2012
COECKE_LAL_2013
HENSON_LAL_PUSEY_2014
FRITZ_2016
YIN_ZHANG_2021
FRITZ_KLINGLER_2023
```

Coverage includes causal syntax, Bayesian-network/generalized causal structures, theory-independent constraints, d-separation and abstract causal calculus.

```text
SG4B = PASS
```

### SG4C

Accepted core:

```text
SIMPSON_2018
CHO_JACOBS_2019
FRITZ_2020
FRITZ_KLINGLER_2023
FRITZ_GONDA_PERRONE_RISCHEL_2023
```

Coverage includes abstract independence, disintegration, Bayesian inversion, conditional independence and statistical sufficiency/comparison.

```text
SG4C = PASS
```

### SG4D

Accepted core:

```text
JACOBS_2011
JACOBS_2018
```

This lane is deliberately a representative adjacent control rather than a broad effectus survey.

```text
SG4D = PASS_MINIMAL_REPRESENTATIVE
```

### SG4E

The firewall is supported across multiple accepted sources rather than by one source label.

Key controls:

- Fong: causal syntax versus concrete stochastic model functor;
- Fritz & Liang: Markov doctrine and free signature boxes;
- Fritz & Klingler: causal compatibility/d-separation across heterogeneous models;
- Henson–Lal–Pusey: causal-structure constraints across generalized probabilistic theories;
- Fritz 2020: common categorical probability theory across multiple concrete probability settings.

```text
SG4E = PASS
```

## Rejection audit

### Perrone — Markov Categories and Entropy

```text
DISPOSITION = REJECT_REDUNDANT_FOR_CURRENT_MECHANISM
```

High-quality peer-reviewed source, but its entropy/divergence extension does not alter the core SG4 taxonomy needed for the next bridge-constraint decision. It remains a natural later source if quantitative information constraints become the explicit target.

### Coecke & Lal — Time Asymmetry of Probabilities Versus Relativistic Causal Structure

```text
DISPOSITION = REJECT_REDUNDANT_SPECIALIZED
```

Physically interesting but narrower than the accepted causal-category source for the present structural mechanism audit.

### Newer quantum Markovian causal-model papers

```text
DISPOSITION = REJECT_SPECIALIZED_LATE_EXTENSION
```

Potentially relevant to a future quantum-specific branch; current gate is theory-neutral and adequately represented without them.

### Broad open-system/network compositionality sources

```text
DISPOSITION = REJECT_REMOTE_RELEVANCE
```

Compositional architecture alone was already covered by the earlier PGH source landscape; SG4 requires probabilistic/causal model-class restriction mechanisms.

## Structural-vs-model-data finding

The selection audit confirms that the accepted corpus supports both sides of the firewall.

Structural information can include:

```text
MARKOV_TERMINALITY_NORMALIZATION
COPY_DELETE_OR_PROCESS_DOCTRINE
DAG_CAUSAL_WIRING
D_SEPARATION_RELATIONS
CONDITIONAL_INDEPENDENCE_AXIOMS
COMPOSITIONAL_FACTORISATION
```

Model-specific information can include:

```text
LOCAL_STOCHASTIC_CHANNELS
CONDITIONAL_PROBABILITY_TABLES
KERNEL_VALUES
GENERATING_BOX_INTERPRETATIONS
LATENT_RESOURCE_ASSIGNMENTS
EMPIRICAL_PARAMETER_VALUES
```

A future PGH formal gate must not credit the second group to the first merely because both are expressed in one categorical model.

## Saturation audit

Late searches mainly produced:

```text
DUPLICATE_PREPRINT_PUBLICATION_PAIRS
QUANTITATIVE_ENTROPY_EXTENSIONS
SPECIALIZED_QUANTUM_CAUSAL_APPLICATIONS
DOWNSTREAM_MARKOV_CATEGORY_REFINEMENTS
GENERAL_COMPOSITIONAL_NETWORK_SOURCES_WITHOUT_NEW_SG4_MECHANISM
```

No uncovered mechanism lane remained that could plausibly reverse the source-level taxonomy.

```text
REPRESENTATIVE_SATURATION = PASS
EXHAUSTIVE_BIBLIOGRAPHY = NO
```

## Outcome

```text
OUTCOME = A
SG4_CLOSED_AT_REPRESENTATIVE_SCOPE = YES
SOURCE_FREEZE_QUALIFIED_FOR_INDEPENDENT_REVIEW = YES
FORMAL_CONSTRAINT_SELECTED = NO
PHYSICAL_CLAIM = NONE
R2B = UNSATISFIED
FCP_EFFECT = NONE
```
