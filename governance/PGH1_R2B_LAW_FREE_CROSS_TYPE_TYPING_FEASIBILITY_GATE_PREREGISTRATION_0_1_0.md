# PGH-1 R2B Law-Free Cross-Type Typing Feasibility Gate — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_R2B_LAW_FREE_CROSS_TYPE_TYPING_FEASIBILITY_GATE
REGISTRY_ID = PGH-OP-0051
CANONICAL_BASE = ad31f99599a0420800caf1d6904f402847b4c0aa
ANCHOR_SCHEMA = PGH-OBJ-0010
CORRECTED_CROSS_TYPE_SCHEMA = PGH-OBJ-0024
CANDIDATE_FAMILY = PGH-GRAM-0003..PGH-GRAM-0007
R2_TARGET = PGH-OBJ-0021
NEW_SOURCE_SEARCH = FORBIDDEN
EMPIRICAL_RESPONSE_DATA = FORBIDDEN
PHYSICAL_RESPONSE_INTERPRETATION = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

Test whether a covariant context-specific record typing/alphabet can be admitted as law-free semantic interface structure without already specifying the response law.

This gate follows the outcome-D correction of `PGH1_R2B_OUTCOME_NEUTRAL_CROSS_TYPE_GENERATIVITY_GATE`: representation neutrality is covariance, not full permutation automorphy.

## Candidate typing structure

Let `C` be a finite nonempty context set and `R` a finite record-label set.

A typing relation is

\[
T\subseteq C\times R.
\]

Define the fiber

\[
R_c=\{r\in R:(c,r)\in T\}.
\]

The intended semantic reading is only:

> `r` is a well-typed record label in the output alphabet/interface associated with context `c`.

The gate must not interpret `T(c,r)` as:

```text
r_IS_A_PHYSICALLY_POSSIBLE_RESPONSE_TO_c
r_HAS_NONZERO_PROBABILITY_GIVEN_c
r_IS_OBSERVED_GIVEN_c
```

## Law-free criterion L1 — response underdetermination

A typing structure passes the minimum law-free test only if it is compatible with at least two distinct response laws while held fixed.

For deterministic controls, require two different sections

\[
f_1,f_2:C\to R
\]

with

\[
(c,f_i(c))\in T
\]

for every `c`.

For probabilistic controls, the same `T` must permit at least two different distributions over at least one fiber.

A singleton-fiber typing that uniquely fixes every deterministic response fails this minimum test unless a richer response model still remains underdetermined for an independently stated reason.

## Locked finite witness T1

Use

```text
C = {a,b}
R = {a0,a1,b0,b1}
T = {(a,a0),(a,a1),(b,b0),(b,b1)}
```

Test the distinct deterministic response maps

```text
f0(a)=a0 ; f0(b)=b0
f1(a)=a1 ; f1(b)=b1
```

and at least two different probability assignments on the same fibers.

The typing relation must remain unchanged.

## Locked theorem T2 — finite fiber multiplicity

For finite nonempty `C`, if every fiber `R_c` is nonempty and at least one fiber has cardinality at least two, prove that there are at least two distinct deterministic sections of `T`.

This theorem establishes formal response underdetermination. It does not establish empirical adequacy or physical meaning.

## Representation test T3 — covariance

Under bijections

\[
\sigma:C\to C',\qquad\tau:R\to R',
\]

the typed interface must transform as

\[
T'=(\sigma\times\tau)[T].
\]

The property “same typing admits multiple response laws” must be preserved under this transport.

No requirement of full automorphy on one fixed carrier is allowed.

## No-smuggling controls

### C1 — allowed-response reinterpretation

If membership in `T` is interpreted as physical possibility/nonzero support, then `T` is already an allowed-response relation and fails the semantic firewall.

### C2 — empirical reconstruction

If `T` is chosen by taking the union of responses observed or predicted to be possible for each context, then its content is response-derived and cannot be counted as primitive law-free typing.

### C3 — singleton-response encoding

If each context fiber is a singleton chosen to match a target deterministic response, the typing relation is simply the response function written as a type declaration.

### C4 — arbitrary partition encoding

A freely chosen family of fibers can encode selective information. Passing L1 shows only that `T` does not uniquely determine a response law; it does not by itself justify why that typing is physically or semantically privileged.

## Outcome space

```text
A = A_COVARIANT_CONTEXT_SPECIFIC_RECORD_TYPING_CAN_FORMALLY_REMAIN_LAW_FREE_BECAUSE_THE_SAME_TYPED_INTERFACE_SUPPORTS_MULTIPLE_INCOMPATIBLE_RESPONSE_LAWS__TYPING_DOES_NOT_ITSELF_SUPPLY_R2B_RESPONSE_SELECTION
B = EVERY_NONTRIVIAL_CROSS_TYPE_TYPING_THAT_COULD_CONNECT_THE_ANCHOR_IS_EQUIVALENT_TO_AN_ALLOWED_RESPONSE_RELATION_OR_OTHER_SUBSTANTIVE_LAW__LAW_FREE_TYPED_INTERFACE_FAILS
C = ONLY_DEGENERATE_OR_PURE_REINDEXING_TYPED_INTERFACES_PASS_THE_LAW_FREE_TEST_AND_THEY_ADD_NO_USEFUL_CROSS_TYPE_STRUCTURE_FOR_A_LATER_GRAMMAR_BRIDGE
D = THE_CURRENT_ANCHOR_AND_CANDIDATE_FORMALISM_ARE_INSUFFICIENT_TO_STATE_THE_TYPING_RESPONSE_DISTINCTION_COHERENTLY
```

No outcome satisfies R2B or identifies a physical bridge.

## Required outputs

Commit 2 may add only:

```text
audits/PGH1_R2B_LAW_FREE_CROSS_TYPE_TYPING_FEASIBILITY_GATE_0_1_0.md
research/formalizations/PGH1_LAW_FREE_CROSS_TYPE_TYPING_SCHEMA_0_1_0.md
research/derivations/PGH_DERIVATION_TYPED_INTERFACE_RESPONSE_UNDERDETERMINATION_0_1_0.md
research/failures/PGH_FAIL_CROSS_TYPE_TYPING_AS_ALLOWED_RESPONSE_SUPPORT_0_1_0.md
handoffs/PGH1_R2B_LAW_FREE_CROSS_TYPE_TYPING_FEASIBILITY_GATE_HANDOFF_0_1_0.md
```

Expected identities if earned:

```text
PGH-OBJ-0025 = LAW_FREE_CROSS_TYPE_TYPING_SCHEMA
PGH-DER-0023 = TYPED_INTERFACE_RESPONSE_UNDERDETERMINATION
PGH-FAIL-0025 = CROSS_TYPE_TYPING_AS_ALLOWED_RESPONSE_SUPPORT
```

## Commit topology

```text
COMMIT_1_MESSAGE = Preregister PGH-1 R2B law-free cross-type typing feasibility gate
COMMIT_2_MESSAGE = Adjudicate PGH-1 R2B law-free cross-type typing feasibility gate
EXACT_COMMITS = 2
```

## Hard stops

```text
DO_NOT_SEARCH_NEW_SOURCES
DO_NOT_USE_EMPIRICAL_RESPONSE_DATA
DO_NOT_DEFINE_T_FROM_TARGET_RESPONSE_SUPPORT
DO_NOT_INTERPRET_TYPING_AS_PHYSICAL_POSSIBILITY
DO_NOT_SELECT_A_GRAMMAR_BY_EMPIRICAL_FIT
DO_NOT_DECLARE_R2B_SATISFIED
DO_NOT_MAKE_EMPIRICAL_PREDICTIONS
DO_NOT_CHANGE_FCP
```