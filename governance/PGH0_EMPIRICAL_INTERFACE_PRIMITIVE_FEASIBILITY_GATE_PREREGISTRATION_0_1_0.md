# PGH-0 Empirical Interface Primitive Feasibility Gate — Preregistration 0.1.0

## Status

```text
OPERATION_ID = PGH0_EMPIRICAL_INTERFACE_PRIMITIVE_FEASIBILITY_GATE
REGISTRY_ID = PGH-OP-0019
OPERATION_CLASS = SOURCE_BOUND_FOUNDATIONAL_FEASIBILITY_GATE
STATUS = PREREGISTERED_IN_PROGRESS
CANONICAL_BASE = 46ffa0a5acb1dfcb2ba56eb012677f09d60e4253
WORKING_BRANCH = research/pgh0-empirical-interface-primitive-feasibility
FROZEN_SOURCE_COUNT = 37
NEW_SOURCE_SEARCH = FORBIDDEN_UNLESS_SPECIFIC_GAP_IS_DEMONSTRATED
R2_LAW_EXHAUSTION = FORBIDDEN
PHYSICAL_GRAMMAR_SELECTION = FORBIDDEN
EMPIRICAL_DATA_ANALYSIS = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Prior PGH-0 work established three points:

1. formal equivalence alone does not select physical equivalence;
2. a minimal context/record semantic anchor can be held fixed while response laws vary;
3. such an anchor can commute across explicit faithful translations, but representation robustness still does not select the physically correct anchor.

This gate asks whether a minimal **empirical-contact primitive** can be admitted as semantic reference without importing substantive physical law or physical possibility selection.

The target distinction is:

```text
EMPIRICAL_CONTACT_PRIMITIVE
!=
EMPIRICAL_RESPONSE_LAW
```

## Candidate empirical interfaces

Test the following separately and in the locked order below.

### E0 — Vocabulary-only naming

Provide names for candidate probes and records with no reference to empirical contact.

Expected risk: too weak to connect the formalism to physical records.

### E1 — Contact signature

Use a signature

\[
\Sigma_E=(C,R,\iota_C,\rho)
\]

where:

- `C` is a family of formal context tokens designated as empirical probe/interface tokens;
- `R` is a family of empirical record labels;
- `iota_C` records the semantic designation of context tokens as probe/interface types;
- `rho` maps designated terminal/output tokens to record labels.

E1 may specify **reference/type membership only**.

It may not contain any relation or function that states which record occurs, may occur, or with what weight/probability for a given probe/state.

### E2 — Primitive intervention/record pairing

Add a relation such as

\[
K\subseteq C\times R
\]

or

\[
K\subseteq C\times X\times R
\]

stating which probe-record pairs/triples are admissible.

Test whether this already constitutes a possibility/response law.

### E3 — Primitive correlation/probability structure

Add probabilities, amplitudes, frequencies, expectation values, or a response kernel to the empirical interface.

Test whether this directly imports response law.

### E4 — Primitive full possibility set

Take the complete set of possible/impossible empirical tasks or histories as primitive.

Test whether this simply relocates substantive physical selection into semantics.

## Locked admissibility criteria

A candidate primitive empirical interface passes only if all of the following hold.

```text
A1_REFERENCE_CONTACT = it gives the formal theory some empirical referential/contact content
A2_RESPONSE_LAW_SEPARATION = distinct incompatible response laws can share the same interface
A3_NO_POSSIBILITY_TABLE = it does not primitive-list allowed/forbidden probe-state-record combinations
A4_NO_PROBABILITY_LAW = it does not primitive-supply probabilities/amplitudes/weights
A5_NO_TARGET_EQUIVALENCE = it does not define full physical identity/equivalence by assumption
A6_NO_COMPLETENESS_SMUGGLING = it does not claim its probe family is the complete physically possible probe universe without independent justification
A7_REPRESENTATION_COMPATIBILITY = it can in principle be transported using the previously qualified commuting-interface conditions
A8_R2_PRESERVATION = no independent law set is admitted during this gate
```

## Formal separation test

For every candidate interface that survives A1–A8, hold the interface fixed and construct at least two incompatible evaluators/grammars inducing different empirical response profiles.

If this cannot be done because the interface already fixes the responses, the candidate fails `A2_RESPONSE_LAW_SEPARATION`.

## Negative-control principle

Any primitive object containing a nontrivial relation of the form

\[
L(c,x,r)
\]

interpreted as “record `r` is physically allowed/required for probe `c` applied to `x`” must be treated as a candidate physical law or possibility-selection rule, not mere semantic contact.

Likewise, any primitive response distribution

\[
p(r\mid c,x)
\]

is substantive response law.

## Physical-contact interpretation discipline

The phrase “empirical primitive” is not permission to insert experimental facts, existing dynamical laws, calibration tables, or a complete operational theory.

At this gate, primitive empirical contact means only a semantic bridge sufficient to identify:

```text
THIS_KIND_OF_FORMAL_CONTEXT_COUNTS_AS_A_PROBE_OR_INTERFACE_TOKEN
THIS_KIND_OF_FORMAL_TERMINAL_COUNTS_AS_A_RECORD_TOKEN
```

without specifying the law relating them.

## Completeness firewall

A finite or declared context family `C` is treated only as the interface under test.

```text
C = DECLARED_EMPIRICAL_INTERFACE
```

must not be promoted to

```text
C = ALL_PHYSICALLY_POSSIBLE_PROBES
```

unless a later, separately justified result establishes completeness.

This firewall is mandatory because a complete probe universe could itself encode substantial physical possibility constraints.

## Outcome space

```text
A = NO_EMPIRICALLY_MEANINGFUL_PRIMITIVE_AVOIDS_RESPONSE_LAW_SMUGGLING
B = LAW_FREE_EMPIRICAL_CONTACT_SIGNATURE_IS_FORMALLY_ADMISSIBLE_BUT_DOES_NOT_SOLVE_PHYSICAL_PRIVILEGE_OR_COMPLETENESS
C = MINIMAL_EMPIRICAL_CONTACT_PLUS_EXISTING_PGH_CRITERIA_RESOLVES_R1_WITHOUT_LAW_SMUGGLING
D = ANY_NONTRIVIAL_EMPIRICAL_CONTACT_ALREADY_REQUIRES_A_SUBSTANTIVE_PHYSICAL_LAW
E = FROZEN_CORPUS_IS_INSUFFICIENT_AND_A_SPECIFIC_SOURCE_GAP_IS_IDENTIFIED
F = UNRESOLVED
```

No outcome is a score or ranking.

## Expected output discipline

If E1 qualifies only as a formal admissible schema, record that narrow result and do not promote it to a physical ontology.

If E2–E4 fail because they encode response/possibility law, preserve those failures explicitly.

## Required outputs

Commit 2 may add only:

```text
audits/PGH0_EMPIRICAL_INTERFACE_PRIMITIVE_FEASIBILITY_GATE_0_1_0.md
research/formalizations/PGH0_LAW_FREE_EMPIRICAL_CONTACT_SIGNATURE_0_1_0.md      # if warranted
research/derivations/PGH_DERIVATION_EMPIRICAL_CONTACT_RESPONSE_SEPARATION_0_1_0.md # if established
research/failures/PGH_FAIL_EMPIRICAL_INTERFACE_AS_RESPONSE_LAW_0_1_0.md        # if warranted
handoffs/PGH0_EMPIRICAL_INTERFACE_PRIMITIVE_FEASIBILITY_GATE_HANDOFF_0_1_0.md
```

Do not mutate current-state/navigation files on the scientific branch.

## Commit boundary

```text
COMMIT_1_MESSAGE = Preregister PGH-0 empirical interface primitive feasibility
COMMIT_2_MESSAGE = Adjudicate PGH-0 empirical interface primitive feasibility
```

Exactly two commits are permitted.

## Hard stops

Stop before:

- claiming the empirical contact signature is physically fundamental;
- claiming the declared interface is complete;
- treating record equivalence as full physical identity;
- beginning R2 law exhaustion;
- choosing a physical grammar;
- importing empirical response data;
- expanding sources without a demonstrated gap;
- changing FCP;
- mutating canonical `main` before independent review.
