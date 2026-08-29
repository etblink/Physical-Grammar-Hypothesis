# PGH-1 Post-Kp Physical Scope and Theory-Applicability Source Intake — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_POST_KP_PHYSICAL_SCOPE_AND_THEORY_APPLICABILITY_SOURCE_INTAKE
REGISTRY_ID = PGH-OP-0074
CANONICAL_BASE = a70e02cfa470b9dea9fa732130e043a24e7a002a
SOURCE_GAP_ID = SG5_PHYSICAL_SCOPE_THEORY_APPLICABILITY_AND_EFFECTIVE_REGIME_SELECTION
WORKING_SCHEMA = PGH-OBJ-0039
FROZEN_PREEXISTING_ACCEPTED_SOURCE_COUNT = 85
SUCCESSOR_GRAMMAR_SELECTION = FORBIDDEN
PHYSICAL_SCOPE_RULE_SELECTION = FORBIDDEN
NAMED_PHYSICAL_SECTOR_SELECTION = FORBIDDEN
EMPIRICAL_TARGET_SEARCH = FORBIDDEN
SOURCE_BOUND_SCIENTIFIC_ADJUDICATION = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Close only the source gap identified by `PGH-OP-0072`: how mature scientific and philosophical literatures characterize the domain of applicability, validity, transport, approximation, and breakdown of theories/models, especially in physics.

This intake asks what determines **where a model or theory is warranted to apply**. It does not ask which physical sector PGH should choose, and it may not promote any sourced applicability criterion into a PGH scope rule.

## Search lanes

### SG5-L1 — theory/model domains of applicability and validity

Target authoritative work on:

- domains of application / intended applications of scientific theories;
- model validity, applicability, adequacy, and representation;
- distinctions among empirical adequacy, representation, idealization, and domain restriction.

Extraction question: what fixes the class of systems or circumstances to which a theory/model is licensed to apply, and how much of that is independent of the model's successful outcomes?

### SG5-L2 — effective field theory, scale separation, and regime validity

Target foundational or authoritative work on:

- effective field theory and decoupling;
- renormalization-group/effective descriptions;
- cutoff, energy-scale, expansion-parameter, coupling, and power-counting regimes;
- breakdown scales and uncertainty from omitted operators/degrees of freedom.

Extraction question: how are applicability and breakdown conditions earned, and which conditions depend on independent physical structure?

### SG5-L3 — approximation, misspecification, and model breakdown

Target authoritative sources on:

- approximation validity and limiting assumptions;
- model misspecification and adequacy diagnostics;
- error estimates / domain restrictions that distinguish a model's useful regime from unrestricted application.

Extraction question: are validity conditions fixed prospectively, inferred from failures, or both, and what epistemic status do they have?

### SG5-L4 — transportability, invariance, and cross-domain validity

Target sources on:

- causal transportability / external validity;
- selection diagrams or explicit domain-difference variables;
- invariance-based prediction across environments;
- abstraction or transformations that preserve relevant causal/model structure.

Extraction question: what assumptions license transfer from one domain/environment to another, and are those assumptions substantive structure rather than mere target labels?

### SG5-L5 — semantic/structural applicability and partial interpretation

Target sources directly relevant to:

- model-to-world representation/application relations;
- partial interpretation / partial structures where they constrain applicability;
- structural similarity, abstraction, or interface conditions used to license application.

Extraction question: can applicability be a semantic/reference condition without itself encoding the substantive response law?

## Source-selection standard

Prefer in order:

1. primary foundational papers by principal contributors;
2. standard monographs or authoritative review articles;
3. high-quality philosophy-of-science sources directly focused on applicability/model validity;
4. secondary sources only when needed to locate or disambiguate primary work.

Every candidate receives one disposition:

```text
ACCEPT
REJECT_REDUNDANT
REJECT_WEAK_AUTHORITY
REJECT_REMOTE_RELEVANCE
REJECT_PREDOMINANTLY_APPLICATION_EXAMPLE
DEFER_ACCESS_OR_SCOPE
```

## Acceptance criteria

An accepted source must materially support at least one of:

```text
A1_EXPLICIT_DOMAIN_OR_REGIME_OF_VALIDITY
A2_PROSPECTIVE_APPLICABILITY_OR_BREAKDOWN_CRITERION
A3_ROLE_OF_INDEPENDENT_PHYSICAL_ASSUMPTIONS_IN_SCOPE
A4_TRANSPORT_OR_EXTERNAL_VALIDITY_ASSUMPTIONS
A5_SEMANTIC_OR_STRUCTURAL_APPLICATION_CONDITION
A6_DISTINCTION_BETWEEN_MODEL_FIT_AND_APPLICABILITY_JUSTIFICATION
```

A source is not accepted merely because it uses an effective model, discusses a physical sector, or contains the words "valid" or "applicable".

## Required extraction fields

For each accepted source:

```text
SOURCE_ID
LANE
AUTHOR
TITLE
YEAR
SOURCE_CLASS
LOCATOR
AUTHORITY_NOTE
DIRECT_RELEVANCE
APPLICABILITY_OBJECT
SCOPE_OR_VALIDITY_CONDITION
CONDITION_ORIGIN
PROSPECTIVE_OR_POSTHOC_STATUS
INDEPENDENT_PHYSICS_ROLE
TRANSFER_OR_BREAKDOWN_RESULT
PGH_RELEVANCE_WITHOUT_CREDIT
```

## Anti-rescue and anti-association firewalls

```text
NO_SOURCE_COUNTS_AS_EVIDENCE_PGH_IS_TRUE
NO_SOURCE_COUNTS_AS_EVIDENCE_A_RESTRICTED_PGH_SCOPE_EXISTS
NO_EFFECTIVE_THEORY_DOMAIN_IS_PROMOTED_TO_PGH_SCOPE
NO_CAUSAL_TRANSPORT_RULE_IS_PROMOTED_TO_PGH_META_GRAMMAR
NO_PHILOSOPHICAL_MODEL_APPLICABILITY_CRITERION_IS_TREATED_AS_PHYSICAL_LAW
NO_SOURCE_SELECTED_BECAUSE_IT_CAN_EXCLUDE_KP
NO_SOURCE_SELECTED_BECAUSE_IT_FAVORS_MARKOV_OR_CONDITIONAL_INDEPENDENCE_MODELS
NO_SUCCESSOR_GRAMMAR_OR_PHYSICAL_SECTOR_SELECTION
NO_EMPIRICAL_TARGET_SEARCH
NO_FCP_CHANGE
```

## Deduplication

New sources must be deduplicated against the frozen 85-source corpus at author/title/DOI-or-stable-locator level where possible.

Overlap is allowed only when a previously frozen source genuinely contains SG5-relevant material not previously extracted; such a source should be marked `PREEXISTING_REUSED`, not counted as a new distinct accepted source.

## Saturation criterion

The intake may stop when:

- all five lanes have authoritative coverage where the literature permits;
- L2 and L4 each have at least three independent primary/authoritative anchors;
- L1/L3/L5 collectively establish the distinction between application/validity conditions and mere empirical success;
- additional candidates are predominantly redundant, narrowly application-specific, or remote from the scope-origin question;
- the corpus is sufficient for a later separate source-bound adjudication of architecture families F0-F4 from `PGH-OP-0072`.

Target new accepted range:

```text
14_TO_24_DISTINCT_SOURCES
```

The range is guidance, not a quota.

## Outcome space

```text
A = SG5_CORPUS_QUALIFIED_AND_SATURATED__DOMAINS_OF_APPLICABILITY_REGIME_VALIDITY_AND_TRANSPORT_ASSUMPTIONS_HAVE_AUTHORITATIVE_COVERAGE__HAND_OFF_TO_SEPARATE_SOURCE_BOUND_SCOPE_ORIGIN_ADJUDICATION
B = SG5_CORPUS_QUALIFIED_BUT_ONE_OR_MORE_LANES_REMAIN_MATERIALLY_UNDERCOVERED__SPECIFIC_RESIDUAL_GAP_RECORDED
C = REPRESENTATIVE_LITERATURE_SHOWS_SG5_SPLITS_INTO_DISTINCT_TAXONOMIES_REQUIRING_SEPARATE_SOURCE_FREEZES_BEFORE_ADJUDICATION
D = SOURCE_ACCESS_OR_AUTHORITY_INSUFFICIENT_TO_FREEZE_A_REPRESENTATIVE_CORPUS
```

No outcome may itself decide whether restricted scope is compatible with strong PGH.

## Required outputs

Commit 2 may add only:

```text
sources/PGH1_POST_KP_PHYSICAL_SCOPE_APPLICABILITY_SOURCE_REGISTER_0_1_0.md
sources/PGH1_POST_KP_PHYSICAL_SCOPE_APPLICABILITY_SOURCE_LANDSCAPE_0_1_0.md
sources/PGH1_POST_KP_PHYSICAL_SCOPE_APPLICABILITY_SOURCE_SELECTION_AUDIT_0_1_0.md
handoffs/PGH1_POST_KP_PHYSICAL_SCOPE_APPLICABILITY_SOURCE_INTAKE_HANDOFF_0_1_0.md
```

## Commit topology

```text
COMMIT_1 = PREREGISTRATION_ONLY
COMMIT_2 = SOURCE_CORPUS_FREEZE_ONLY
EXACT_COMMITS = 2
```

## Stop boundary

After Commit 2 qualification:

```text
STOP_BEFORE_SOURCE_BOUND_SCOPE_ORIGIN_ADJUDICATION
STOP_BEFORE_SUCCESSOR_GRAMMAR_SELECTION
STOP_BEFORE_PHYSICAL_SECTOR_SELECTION
STOP_BEFORE_EMPIRICAL_TARGET_DISCOVERY
STOP_BEFORE_EMPIRICAL_ANALYSIS
```
