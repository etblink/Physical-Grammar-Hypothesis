# PGH-1 R2 Local-to-Global and Global-Constraint Source Intake — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_R2_LOCAL_TO_GLOBAL_AND_GLOBAL_CONSTRAINT_SOURCE_INTAKE
REGISTRY_ID = PGH-OP-0033
CANONICAL_BASE = 88c3fdb22140a3faaba61201ba5acb1eb0c18003
DISCOVERY_PREREGISTRATION = governance/PGH1_R2_CANDIDATE_GRAMMAR_DISCOVERY_AND_SOURCE_GAP_AUDIT_PREREGISTRATION_0_1_0.md
DISCOVERY_AUDIT = audits/PGH1_R2_CANDIDATE_GRAMMAR_DISCOVERY_AND_SOURCE_GAP_AUDIT_0_1_0.md
WORKING_TARGET = PGH-OBJ-0012
NEW_GRAMMAR_CONSTRUCTION = FORBIDDEN
PHYSICAL_GRAMMAR_SELECTION = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Close exactly the two concrete source gaps identified by the canonical PGH-1 discovery audit before any successor grammar is constructed.

## Search lanes

```text
SG1_LOCAL_TO_GLOBAL_OBSTRUCTION
  - local-to-global consistency and gluing
  - sheaf/presheaf or descent-style obstruction machinery
  - global-section/contextuality obstructions as a physical comparison case
  - locally consistent but globally unrealizable constraint systems

SG2_GLOBAL_CONSTRAINT_FORMALISM
  - formal all-at-once/global consistency approaches
  - global variational/constraint architectures as comparison controls
  - explicit distinction between generic consistency mechanism and a law-specific functional that already contains the dynamics
```

No third lane may be opened in this operation.

## Candidate-source acceptance criteria

Accept a source only if it materially supports one or more of:

```text
S1 = precise local-to-global/gluing/extension obstruction machinery
S2 = a physical application in which local compatibility fails to extend globally
S3 = formal global/all-at-once constraint architecture
S4 = a rigorous negative control showing how a global functional/constraint can merely encode the physical law
S5 = authoritative survey or standard monograph needed to map the lane
```

Prefer primary sources and authoritative surveys/monographs. Reject weak summaries, duplicate expositions, remote analogies, and sources whose only relevance is the word "constraint" or "context".

## Source-selection firewall

Inclusion does not imply that the formalism is PGH's grammar or that its physical interpretation is accepted.

The intake must preserve the distinction:

```text
LOCAL_TO_GLOBAL_OBSTRUCTION_MECHANISM != PHYSICAL_GRAMMAR
GLOBAL_CONSTRAINT_FORMALISM != LAW_EXHAUSTION
ACTION_OR_CONSTRAINT_FUNCTIONAL != GENERIC_GRAMMAR_IF_THE_FUNCTIONAL_ALREADY_ENCODES_THE_LAW
```

## Target corpus

```text
TARGET_ACCEPTED_SOURCE_COUNT = 12_TO_24
MINIMUM_SG1_ACCEPTED = 6
MINIMUM_SG2_ACCEPTED = 4
DUPLICATE_OR_REDUNDANT_SOURCES_MUST_BE_RECORDED
```

Saturation may stop below 24 when late searches are redundant.

## Required outputs

Commit 2 may add only:

```text
sources/PGH1_R2_LOCAL_GLOBAL_SOURCE_REGISTER_0_1_0.md
sources/PGH1_R2_LOCAL_GLOBAL_SOURCE_LANDSCAPE_0_1_0.md
sources/PGH1_R2_LOCAL_GLOBAL_SOURCE_SELECTION_AUDIT_0_1_0.md
handoffs/PGH1_R2_LOCAL_TO_GLOBAL_AND_GLOBAL_CONSTRAINT_SOURCE_INTAKE_HANDOFF_0_1_0.md
```

No grammar artifact, derivation, failure artifact, or current-state file may be created in this operation.

## Outcome space

```text
A = BOTH_SOURCE_GAPS_CLOSED_WITH_REPRESENTATIVE_SATURATED_CORPUS
B = SG1_CLOSED_BUT_SG2_REMAINS_SOURCE_INSUFFICIENT
C = SG2_CLOSED_BUT_SG1_REMAINS_SOURCE_INSUFFICIENT
D = ONE_OR_BOTH_LANES_FAIL_TO_YIELD_A_COHERENT_RESEARCH_NEIGHBORHOOD
```

No outcome selects a successor grammar.

## Commit topology

```text
COMMIT_1_MESSAGE = Preregister PGH-1 R2 local-to-global and global-constraint source intake
COMMIT_2_MESSAGE = Freeze PGH-1 R2 local-to-global and global-constraint source corpus
EXACT_COMMITS = 2
```

## Hard stops

```text
DO_NOT_SELECT_A_SUCCESSOR_GRAMMAR
DO_NOT_DERIVE_A_PHYSICAL_LAW
DO_NOT_EXPAND_BEYOND_SG1_AND_SG2
DO_NOT_REINTERPRET_PGH_GRAM_0002
DO_NOT_MODIFY_FCP
```
