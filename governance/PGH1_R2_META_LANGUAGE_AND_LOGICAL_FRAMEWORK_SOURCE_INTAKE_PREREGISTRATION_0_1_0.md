# PGH-1 R2 Meta-Language and Logical-Framework Source Intake — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_R2_META_LANGUAGE_AND_LOGICAL_FRAMEWORK_SOURCE_INTAKE
REGISTRY_ID = PGH-OP-0042
CANONICAL_BASE = b3eef90e4e21265156e3290561f2cbea01363403
SOURCE_GAP_ID = SG3_META_LANGUAGE_AND_LOGICAL_FRAMEWORK_ORIGIN
WORKING_TARGET = PGH-OBJ-0012
META_LANGUAGE_MAP = PGH-OBJ-0016
FROZEN_PREEXISTING_ACCEPTED_SOURCE_COUNT = 51
SUCCESSOR_GRAMMAR_SELECTION = FORBIDDEN
PHYSICAL_LAW_ADJUDICATION = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Close the bounded SG3 source gap identified by the canonical local-rule-language origin gate.

The intake asks what mature formal disciplines say about the organization, translation, structural rules, and variability of logics/languages themselves. It does **not** ask which formalism is fundamental physics.

## Search lanes

### SG3-L1 — institution theory / abstract model theory / heterogeneous logic

Target sources on:

- institutions and satisfaction condition;
- morphisms/comorphisms or translations between logics;
- institution-independent model theory;
- general logics and heterogeneous specification.

Question: do these frameworks merely parameterize/relate logics, or supply an intrinsic criterion selecting one logic?

### SG3-L2 — logical frameworks / metalanguages

Target sources on:

- LF and related logical frameworks;
- encoding multiple object logics in a metalanguage;
- adequacy/representation of judgments and inference rules.

Question: what structure is fixed in the framework, and what remains supplied by the encoded object logic?

### SG3-L3 — categorical logic / type-theoretic language organization

Target sources on:

- hyperdoctrines, categorical semantics of logic;
- first-order categorical logic;
- categorical logic and type theory;
- syntax/semantics interfaces where logical structure is induced by categorical structure.

Question: does categorical organization derive a privileged logic, or characterize logics relative to chosen categorical structure?

### SG3-L4 — structural and substructural proof theory

Target sources on:

- sequent calculi and structural rules;
- exchange, weakening, contraction;
- linear logic, relevant logic, Lambek calculus, or other substructural systems where changing structural rules changes derivability/admissibility.

Question: are structural rules themselves derived from deeper neutral principles or chosen parameters that define different logics?

### SG3-L5 — translation/invariance/control lane

Target sources that directly compare or translate logics while preserving satisfaction, proof, or semantics.

Control question: can a framework be highly representation-independent while remaining neutral among many distinct object logics?

## Source-selection standard

Prefer, in order:

1. primary foundational papers;
2. standard monographs by principal contributors;
3. authoritative surveys where they map a field or terminology;
4. secondary sources only when needed to locate primary literature.

Every candidate must receive one disposition:

```text
ACCEPT
REJECT_REDUNDANT
REJECT_WEAK_AUTHORITY
REJECT_REMOTE_RELEVANCE
DEFER_ACCESS_OR_SCOPE
```

## Scientific firewalls

```text
NO_SOURCE_COUNTS_AS_EVIDENCE_OF_PGH_TRUTH
NO_SOURCE_COUNTS_AS_EVIDENCE_OF_PGH_NOVELTY_BY_ABSENCE
NO_FORMALISM_IS_PROMOTED_TO_SUCCESSOR_GRAMMAR
NO_LOGIC_IS_CALLED_PHYSICAL
NO_STRUCTURAL_RULE_IS_CALLED_A_LAW_OF_NATURE
NO_SOURCE_SEARCH_OUTSIDE_SG3_WITHOUT_NEW_GAP
NO_FCP_CHANGE
```

## Required extraction fields

For each accepted source record:

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
META_LANGUAGE_FIXED_STRUCTURE
META_LANGUAGE_VARIABLE_STRUCTURE
SELECTION_OR_NEUTRALITY_RESULT
PGH_RELEVANCE
```

## Saturation criterion

The intake may stop when:

- every SG3 lane has at least two independent authoritative anchors where the literature permits;
- additional candidates are predominantly redundant or remote;
- the distinction between language organization/translation and language selection is source-supported;
- structural-rule variability is source-supported;
- no major SG3 sublane remains uncovered.

Target accepted range:

```text
12_TO_24_SOURCES
```

The range is guidance, not a quota.

## Outcome space

```text
A = SG3_CORPUS_SHOWS_AN_ESTABLISHED_NON_RESULT_DIRECTED_META_LANGUAGE_SELECTION_PRINCIPLE_DIRECTLY_RELEVANT_TO_PGH__HAND_OFF_FOR_SEPARATE_ADJUDICATION
B = SG3_CORPUS_SHOWS_MATURE_LANGUAGE_ORGANIZATION_AND_TRANSLATION_MACHINERY_BUT_NO_GENERAL_SELECTION_OF_ONE_PRIVILEGED_LOGIC__HAND_OFF_FOR_FORMAL_OVERLAP_ADJUDICATION
C = SG3_CORPUS_SHOWS_MULTIPLE_INCOMPATIBLE_OR_SCOPE_DEPENDENT_META_LANGUAGE_SELECTION_PRINCIPLES_REQUIRING_SEPARATE_TAXONOMY
D = REPRESENTATIVE_CORPUS_INSUFFICIENT_OR_SOURCE_GAP_REMAINS
```

This source operation may classify the landscape but may not convert any outcome into a successor grammar.

## Required outputs

Commit 2 may add only:

```text
sources/PGH1_R2_META_LANGUAGE_SOURCE_REGISTER_0_1_0.md
sources/PGH1_R2_META_LANGUAGE_SOURCE_LANDSCAPE_0_1_0.md
sources/PGH1_R2_META_LANGUAGE_SOURCE_SELECTION_AUDIT_0_1_0.md
handoffs/PGH1_R2_META_LANGUAGE_SOURCE_INTAKE_HANDOFF_0_1_0.md
```

## Commit topology

```text
COMMIT_1_MESSAGE = Preregister PGH-1 R2 meta-language logical-framework source intake
COMMIT_2_MESSAGE = Freeze PGH-1 R2 meta-language logical-framework source corpus
EXACT_COMMITS = 2
```

## Stop boundary

After Commit 2 qualification:

```text
STOP_BEFORE_META_LANGUAGE_SCIENTIFIC_ADJUDICATION
STOP_BEFORE_SUCCESSOR_GRAMMAR_SELECTION
STOP_BEFORE_PHYSICAL_BRIDGE
```
