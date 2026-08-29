# PGH-1 R2 Generated Cover and Compatibility Origin Gate — Adjudication 0.1.0

## Identity

```text
OPERATION_ID = PGH1_R2_GENERATED_COVER_AND_COMPATIBILITY_ORIGIN_GATE
REGISTRY_ID = PGH-OP-0036
CANONICAL_BASE = f094134838129f12def1eb20baa116756de6dd99
PREREGISTRATION_COMMIT = 6d564f6cb21aba9bbf4f6788402f308bd4489e31
WORKING_TARGET = PGH-OBJ-0012
MECHANISM_SCHEMA = PGH-OBJ-0013
FORMAL_REFERENCE_BASELINE = PGH-GRAM-0002
NEW_SOURCE_SEARCH = NONE
FCP_EFFECT = NONE
```

## Outcome

```text
OUTCOME = B__COVER_DOMAIN_AND_ORDINARY_COMPATIBILITY_CAN_BE_GENERATED_CONDITIONALLY_BUT_FREE_ASSIGNMENTS_ALWAYS_GLUE_AND_THE_ORIGIN_OF_PROPER_LOCAL_ADMISSIBILITY_REMAINS_UNEARNED
SUCCESSOR_GRAMMAR_QUALIFIED = NO
R2_SATISFIED = NO
PHYSICAL_LAW_DERIVED = NO
```

## Executive result

The gate separates four ingredients of the local-to-global mechanism:

1. local-context cover;
2. value/record domain;
3. overlap compatibility;
4. proper local admissibility supports.

Items 1–3 can be obtained conditionally without inspecting a target physical result:

- a presentation exposing finite constituent incidence can mechanically induce a cover from supports of grammar-generated contexts;
- a law-free empirical anchor can supply record labels as a formal value domain without supplying response laws;
- ordinary functional restriction supplies a canonical overlap map and equality on overlaps supplies compatibility.

However, these three ingredients alone do not generate any local-to-global obstruction when each local context admits the full assignment set `D^C`.

The missing selective ingredient is a family of proper local admissibility supports

\[
R_C\subsetneq D^C.
\]

At current scope PGH has no independently justified mechanism that generates such supports without either importing response/possibility law, using arbitrary support tables, or reusing the arbitrary extensional formation table already rejected by `PGH-FAIL-0001`.

## T1 — Free-assignment gluing theorem

Let `mathcal C` cover `V`, let `D` be nonempty, and let

\[
s_C\in D^C
\]

be chosen for every context `C` such that for all `C,C'`

\[
s_C|_{C\cap C'}=s_{C'}|_{C\cap C'}.
\]

Define, for each `v in V`,

\[
s(v)=s_C(v)
\]

using any context containing `v`.

The cover condition guarantees existence of at least one such context. Pairwise compatibility makes the definition independent of the chosen context. Thus `s in D^V` exists and restricts to every `s_C`.

If `t in D^V` has the same restrictions, then for any `v` and any `C` containing `v`,

\[
t(v)=t|_C(v)=s_C(v)=s(v),
\]

so `t=s`.

Therefore:

```text
FREE_ASSIGNMENT_GLUING = UNIQUE
COVER_PLUS_ORDINARY_COMPATIBILITY_GLOBAL_OBSTRUCTION = NO
```

This is recorded separately as `PGH-DER-0013`.

## T2 — Proper local supports

When local assignment spaces are replaced by proper subsets

\[
R_C\subsetneq D^C,
\]

the previous theorem no longer says that a compatible global realization must exist, because the support constraints can prevent any family of local choices from being globally compatible.

The already-qualified odd-cycle witness provides the locked control. For binary values and the same local inequality support on every edge,

\[
R_{\{i,i+1\}}=\{(0,1),(1,0)\},
\]

cycle counts are:

```text
C3 = 0 global assignments
C4 = 2
C5 = 0
C6 = 2
C7 = 0
C8 = 2
```

Thus proper supports can combine with global incidence to generate non-table-driven global impossibility.

But the support family itself carries substantive selective information: it says which local tuples are admitted and which are not.

## No-smuggling audit

### N1 — response-derived support

```text
STATUS = REJECTED_FOR_R2_CREDIT
```

If `R_C` is extracted from observed response tables, quantum probabilities/supports, Bell/contextuality data, or a desired empirical partition, the target physical regularity has already entered upstream.

### N2 — arbitrary support tables

```text
STATUS = UNIVERSAL_ENCODING_RISK
```

Arbitrary proper subsets can encode arbitrary local exclusions. Properness alone is not explanatory.

In the extreme, taking one context equal to the entire domain `V` and setting its support to any desired set `S subseteq D^V` directly encodes `S` as the allowed global models.

### N3 — support inherited from PGH-GRAM-0002

```text
STATUS = REJECTED_AS_RELABELED_TABLE
```

`PGH-GRAM-0002` permits arbitrary extensional formation data. Defining the local supports from arbitrary entries of that relation does not cure `PGH-FAIL-0001`; it only changes where the table is stored.

### N4 — generated-cover representation limitation

```text
COVER_EXTRACTION = FORMALLY_AVAILABLE_CONDITIONALLY
REPRESENTATION_INDEPENDENCE = NOT_ESTABLISHED
```

`SUPPORT(c)` can be read mechanically from a presentation that exposes finite constituent incidence, but a faithful change of formal language could alter the presentation support structure. No physical privilege is assigned to the resulting cover.

### N5 — empirical anchor firewall

```text
RECORD_LABEL_DOMAIN = FORMALLY_AVAILABLE
ALLOWED_RESPONSE_TUPLES_FROM_ANCHOR = FORBIDDEN
```

The law-free anchor may name record labels. It does not specify which local tuples are possible, impossible, or probable.

## Acceptance criteria

```text
A1_COVER_CAN_BE_MECHANICALLY_EXTRACTED_WITHOUT_TARGET_RESULT = PASS_CONDITIONAL_ON_PRESENTATION_SUPPORT
A2_CANONICAL_OVERLAP_RESTRICTION_IS_AVAILABLE = PASS
A3_FREE_ASSIGNMENT_GLUING_THEOREM = PASS
A4_NONTRIVIAL_OBSTRUCTION_REQUIRES_PROPER_LOCAL_SUPPORT_OR_EQUIVALENT_STRUCTURE = PASS_WITHIN_LOCKED_ASSIGNMENT_SCHEMA
A5_RESPONSE_DERIVED_SUPPORT_IS_REJECTED = PASS
A6_ARBITRARY_SUPPORT_TABLE_UNIVERSAL_ENCODING_IS_EXPOSED = PASS
A7_CURRENT_GRAMMAR_TABLE_FAILURE_IS_NOT_RELABELED_SUCCESS = PASS
A8_REPRESENTATION_LIMITATION_OF_COVER_EXTRACTION_IS_EXPLICIT = PASS
```

## Scientific interpretation

This gate improves the PGH-1 architecture by locating the actual explanatory burden.

The problem is no longer simply to generate contexts or define overlap consistency. Under unrestricted local assignments those structures are automatically globally glueable.

The live R2 problem is now:

\[
\boxed{\text{What non-result-directed grammar principle generates proper local admissibility supports?}}
\]

A successful successor grammar would need to generate the local support restriction from compact structure not equivalent to a lookup table and not derived from the physical responses it is meant to explain.

No such grammar has yet been found.

## Hard-stop verification

```text
TARGET_CONTEXTUALITY_SUPPORT_IMPORTED = NO
LOCAL_SUPPORT_DEFINED_FROM_OBSERVED_RESPONSE = NO
ARBITRARY_F_RELABELED_AS_EXPLANATORY_LAW = NO
PRESENTATION_SUPPORT_CALLED_REPRESENTATION_INDEPENDENT = NO
SUCCESSOR_GRAMMAR_CREATED = NO
FCP_CHANGED = NO
```
