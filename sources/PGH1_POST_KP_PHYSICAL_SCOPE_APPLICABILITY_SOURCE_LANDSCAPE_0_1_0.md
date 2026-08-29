# PGH-1 Post-Kp Physical Scope / Theory-Applicability Source Landscape 0.1.0

## Identity

```text
SOURCE_GAP_ID = SG5_PHYSICAL_SCOPE_THEORY_APPLICABILITY_AND_EFFECTIVE_REGIME_SELECTION
FROZEN_NEW_ACCEPTED = 21
FROZEN_TOTAL_ACCEPTED = 106_AT_CURRENT_REPOSITORY_DEDUP_SCOPE
SOURCE_BOUND_ADJUDICATION = NOT_PERFORMED
```

## Landscape summary

The SG5 corpus separates at least five mature ways in which scientific applicability is constrained. The separation is descriptive. It does not yet decide which, if any, can satisfy strong-PGH law-exhaustion requirements.

### 1. Target-relative modeling and representation

Morrison/Morgan, Giere, Maki, and Weisberg converge on a broad methodological point: models are used for particular targets and purposes through mediating, representational, idealizing, or isolating relations. A model's formal existence does not make it a representation of every possible system. Target specification and assumptions are part of actual scientific use.

```text
MODEL_FORM_ALONE -> NO_UNIVERSAL_TARGET_RELATION
TARGET_AND_PURPOSE -> EXPLICIT_IN_APPLICATION
ISOLATION_OR_IDEALIZATION -> ASSUMPTION_BEARING
```

This literature does not provide one unique criterion that selects the correct physical domain for an arbitrary formal grammar.

### 2. Effective theories and regime validity

Wilson/Kogut, Appelquist/Carazzone, Weinberg, Polchinski, Georgi, and Burgess provide especially strong physical examples of prospectively restricted domains.

Applicability is organized through substantive structure such as:

```text
ENERGY_OR_MOMENTUM_SCALE
HEAVY_VS_LIGHT_DEGREES_OF_FREEDOM
DECOUPLING
CUTOFF
RENORMALIZATION_GROUP_FLOW
POWER_COUNTING
EXPANSION_PARAMETER
SYMMETRIES
```

These conditions can be specified independently of whether one particular dataset fits. They also show why ordinary physics can legitimately use restricted-scope theories without making the restrictions arbitrary.

For PGH accounting, however, these examples immediately raise rather than settle the central issue: scale hierarchies, symmetry content, degrees of freedom, and decoupling assumptions are substantive physical information. A later adjudication must decide whether importing analogous information as `S` would be compatible with strong PGH or would instantiate `PGH-FAIL-0037`.

### 3. Validation, inadequacy, and predictive uncertainty

Oberkampf/Trucano, Kennedy/O'Hagan, and Roy/Oberkampf distinguish several concepts that are easy to collapse incorrectly:

```text
VERIFICATION != VALIDATION
CALIBRATION != MODEL_ADEQUACY
BEST_FIT != ZERO_MODEL_DISCREPANCY
VALIDATION_EVIDENCE != UNRESTRICTED_EXTRAPOLATION_LICENSE
PREDICTIVE_UNCERTAINTY_INCLUDES_MODEL_FORM_AND_EPISTEMIC_COMPONENTS
```

This lane is a strong control against defining physical scope as “where the model happens to fit.” Scientific application may be revised after failures, but mature validation practice records inadequacy and uncertainty rather than converting every failure into a silently narrowed theory domain.

### 4. Transportability and invariance across environments

Pearl/Bareinboim and subsequent transportability work provide a formal model of cross-domain validity: transfer is licensed only under explicit assumptions about what differs and what remains invariant between domains. Peters/Buhlmann/Meinshausen use invariance across environments as a criterion, while Rubenstein et al. require exact transformations to preserve intervention-level conclusions across descriptions.

```text
CROSS_DOMAIN_TRANSFER = CONDITIONAL
DOMAIN_DIFFERENCE_ASSUMPTIONS = EXPLICIT
INVARIANCE = STRUCTURAL_CLAIM_NOT_TARGET_LABEL
TRANSPORT_FAILURE = FORMALLY_EXPOSABLE
```

This is directly relevant to prospective scope discipline. It also shows that formal transport rules commonly depend on causal/environmental structure supplied to the problem; the formalism does not choose those facts from nothing.

### 5. Semantic and partial-structural applicability

da Costa/French and Bueno/French/Ladyman show that relations between theoretical/mathematical structures and empirical/physical domains can be partial and structurally articulated. Applicability need not mean literal identity or total isomorphism.

This keeps open the narrow possibility identified in OP-0072 that some parts of `S` or `I` could be semantic/reference conditions rather than additional response laws. But these sources do not establish that semantic relations select a unique physical domain independently of empirical/modeling inputs.

## Cross-lane distinctions now source-qualified

The corpus is sufficient to make the following distinctions available for a later adjudication:

```text
D1_MODEL_TARGET_RELATION != MODEL_FORM
D2_PROSPECTIVE_REGIME_CONDITION != RESULT_SELECTED_EXCEPTION
D3_CALIBRATION_OR_FIT != MODEL_ADEQUACY
D4_VALIDATION != UNIVERSAL_EXTRAPOLATION
D5_TRANSPORT_REQUIRES_DOMAIN_DIFFERENCE_AND_INVARIANCE_ASSUMPTIONS
D6_SEMANTIC_APPLICABILITY_CAN_BE_PARTIAL_WITHOUT_BEING_AUTOMATIC
D7_RESTRICTED_SCOPE_CAN_BE_GOOD_ORDINARY_SCIENCE_WHILE_REMAINING_SUBSTANTIVE_PHYSICAL_INPUT
```

## What the corpus does not establish

```text
NO_GENERAL_UNIQUE_SCOPE_SELECTOR_FOR_ARBITRARY_GRAMMAR
NO_PGH_COMPATIBLE_RESTRICTED_SCOPE_RULE_SELECTED
NO_PROOF_UNIVERSAL_SCOPE_IS_MANDATORY_FOR_STRONG_PGH
NO_PROOF_ALL_SEMANTIC_SCOPE_CONDITIONS_ARE_LAW_FREE
NO_SUCCESSOR_GRAMMAR
NO_PHYSICAL_SECTOR
NO_EMPIRICAL_TARGET
```

## Readiness for next stage

All five preregistered lanes have authoritative coverage. L2 and L4 each exceed the minimum of three independent anchors. L1/L3/L5 jointly separate applicability from mere empirical success. Additional search was increasingly redundant or application-specific.

```text
SG5_SATURATION = PASS_REPRESENTATIVE
READY_FOR_SEPARATE_SOURCE_BOUND_SCOPE_ORIGIN_ADJUDICATION = YES
```
