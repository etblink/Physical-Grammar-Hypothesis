# PGH-1 R2 Generated Cover and Compatibility Origin Gate — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_R2_GENERATED_COVER_AND_COMPATIBILITY_ORIGIN_GATE
REGISTRY_ID = PGH-OP-0036
CANONICAL_BASE = f094134838129f12def1eb20baa116756de6dd99
WORKING_TARGET = PGH-OBJ-0012
MECHANISM_SCHEMA = PGH-OBJ-0013
FORMAL_REFERENCE_BASELINE = PGH-GRAM-0002
FROZEN_LOCAL_GLOBAL_CORPUS_COUNT = 15
NEW_SOURCE_SEARCH = FORBIDDEN
SUCCESSOR_GRAMMAR_SELECTION = FORBIDDEN_UNLESS_OUTCOME_A
FCP_EFFECT = NONE
```

## Purpose

Determine whether the key inputs exposed by `PGH-FAIL-0014` can be generated from already accepted PGH structure without using a target physical impossibility:

1. a local-context cover;
2. a value/record domain;
3. overlap compatibility/restriction structure;
4. proper local admissibility supports.

The gate deliberately separates item 4 from items 1–3.

## Candidate generated architecture G1

Use only already accepted structures:

```text
LAW_FREE_EMPIRICAL_CONTACT_SIGNATURE = PGH-OBJ-0010
GRAMMAR_GENERATED_EMPIRICAL_CONTEXT_CLOSURE = PGH-OBJ-0011
FORMAL_REFERENCE_GRAMMAR = PGH-GRAM-0002
```

Conditional on a grammar presentation exposing finite formal support/constituent incidence for a generated context `c`, define:

```text
SUPPORT(c) = finite formal positions/subcomponents occurring in c
GENERATED_COVER = { SUPPORT(c) : c in the grammar-generated empirical context family }
```

This extraction may use syntax/incidence only. It may not inspect response values, empirical success, a target contextuality scenario, or a desired no-go theorem.

The gate must record if this cover extraction is merely presentation-conditional rather than representation-independent.

## Candidate domain inheritance G2

A law-free empirical anchor may supply record labels `R`.

At this scope the candidate local value domain may be inherited as a finite subset or typed family of record labels only if doing so does not add allowed-response relations, probabilities, or a complete physical possibility set.

The gate may establish formal availability of such a domain. It may not establish that every relevant physical variable is record-valued.

## Candidate overlap rule G3

For local assignments represented as ordinary functions on support sets, use only canonical restriction:

\[
\rho_{C,C'}:D^C\to D^{C'}
\]

for `C' subseteq C`, with compatibility defined as equality on overlaps.

No target-specific compatibility predicate may be introduced.

## Locked theorem test T1 — free-assignment gluing

Let `mathcal C` cover `V`, let `D` be nonempty, and assign the **full** local assignment set

\[
A(C)=D^C
\]

to every context.

For any chosen family `s_C in D^C` satisfying

\[
s_C|_{C\cap C'}=s_{C'}|_{C\cap C'}
\]

for all contexts, test whether a unique global assignment

\[
s\in D^V
\]

must exist with `s|_C=s_C` for every `C`.

If yes, cover plus ordinary overlap agreement alone cannot create a global obstruction.

## Locked support test T2

Replace `A(C)=D^C` by proper subsets

\[
R_C\subsetneq D^C.
\]

Test whether nonextendability can then occur, including the already-qualified odd-cycle inequality witness.

The gate must identify exactly which additional information is carried by the family `{R_C}`.

## No-smuggling controls

### N1 — response-derived support

Defining `R_C` from observed/known response tables, quantum probabilities, target Bell/contextuality supports, or any desired empirical partition is result-directed and receives no R2 credit.

### N2 — arbitrary support tables

Arbitrary proper subsets `R_C` can encode target exclusions. Properness alone is not explanatory.

### N3 — current-grammar support

If `R_C` is inherited directly from arbitrary well-formedness entries of `PGH-GRAM-0002`, the universal-table failure `PGH-FAIL-0001` remains in force.

### N4 — syntax-cover limitation

A cover mechanically extracted from one presentation is not automatically representation-independent. Any such result must remain conditional until translation robustness is shown.

### N5 — empirical-anchor firewall

Primitive record reference may supply labels, but may not supply which tuples are allowed, forbidden, likely, or impossible.

## Acceptance criteria

```text
A1_COVER_CAN_BE_MECHANICALLY_EXTRACTED_WITHOUT_TARGET_RESULT = tested
A2_CANONICAL_OVERLAP_RESTRICTION_IS_AVAILABLE = tested
A3_FREE_ASSIGNMENT_GLUING_THEOREM = tested
A4_NONTRIVIAL_OBSTRUCTION_REQUIRES_PROPER_LOCAL_SUPPORT_OR_EQUIVALENT_STRUCTURE = tested
A5_RESPONSE_DERIVED_SUPPORT_IS_REJECTED = tested
A6_ARBITRARY_SUPPORT_TABLE_UNIVERSAL_ENCODING_IS_EXPOSED = tested
A7_CURRENT_GRAMMAR_TABLE_FAILURE_IS_NOT_RELABELED_SUCCESS = tested
A8_REPRESENTATION_LIMITATION_OF_COVER_EXTRACTION_IS_EXPLICIT = tested
```

## Outcome space

```text
A = COVER_DOMAIN_COMPATIBILITY_AND_NONTRIVIAL_LOCAL_SUPPORT_ALL_FOLLOW_FROM_ALREADY_JUSTIFIED_PGH_STRUCTURE_AND_A_PROVISIONAL_SUCCESSOR_GRAMMAR_IS_QUALIFIED
B = COVER_DOMAIN_AND_ORDINARY_COMPATIBILITY_CAN_BE_GENERATED_CONDITIONALLY_BUT_FREE_ASSIGNMENTS_ALWAYS_GLUE_AND_THE_ORIGIN_OF_PROPER_LOCAL_ADMISSIBILITY_REMAINS_UNEARNED
C = EVEN_COVER_OR_COMPATIBILITY_CANNOT_BE_GENERATED_COHERENTLY_FROM_ACCEPTED_PGH_STRUCTURE
D = FROZEN_SOURCE_OR_FORMAL_SCOPE_IS_INSUFFICIENT
```

Outcome A requires an independently justified source of nontrivial local supports. It may not be selected during the gate because it makes the odd-cycle or a known physical obstruction work.

## Required outputs

Commit 2 may add only:

```text
audits/PGH1_R2_GENERATED_COVER_AND_COMPATIBILITY_ORIGIN_GATE_0_1_0.md
research/formalizations/PGH1_GENERATED_COVER_COMPATIBILITY_SCHEMA_0_1_0.md
research/derivations/PGH_DERIVATION_FREE_LOCAL_ASSIGNMENT_GLUING_0_1_0.md
research/failures/PGH_FAIL_LOCAL_ADMISSIBILITY_SUPPORT_ORIGIN_0_1_0.md
handoffs/PGH1_R2_GENERATED_COVER_AND_COMPATIBILITY_ORIGIN_GATE_HANDOFF_0_1_0.md
```

## Commit topology

```text
COMMIT_1_MESSAGE = Preregister PGH-1 R2 generated cover and compatibility origin gate
COMMIT_2_MESSAGE = Adjudicate PGH-1 R2 generated cover and compatibility origin gate
EXACT_COMMITS = 2
```

## Hard stops

```text
DO_NOT_IMPORT_TARGET_CONTEXTUALITY_SUPPORTS
DO_NOT_DEFINE_LOCAL_SUPPORT_FROM_OBSERVED_RESPONSE
DO_NOT_REUSE_ARBITRARY_F_AS_EXPLANATORY_LAW
DO_NOT_CLAIM_PRESENTATION_SUPPORT_IS_REPRESENTATION_INDEPENDENT
DO_NOT_CREATE_A_SUCCESSOR_GRAMMAR_UNLESS_OUTCOME_A_PASSES
DO_NOT_CHANGE_FCP
```
