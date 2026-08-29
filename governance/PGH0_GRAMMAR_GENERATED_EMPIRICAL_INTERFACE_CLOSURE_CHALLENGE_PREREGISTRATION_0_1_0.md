# PGH-0 Grammar-Generated Empirical Interface Closure Challenge — Preregistration 0.1.0

## Status

```text
OPERATION_ID = PGH0_GRAMMAR_GENERATED_EMPIRICAL_INTERFACE_CLOSURE_CHALLENGE
REGISTRY_ID = PGH-OP-0022
OPERATION_CLASS = SOURCE_BOUND_FOUNDATIONAL_FORMALIZATION
STATUS = PREREGISTERED_IN_PROGRESS
CANONICAL_BASE = e6467fa370591b6e8e322a886530dd1d5a496688
WORKING_BRANCH = research/pgh0-grammar-generated-empirical-interface-closure
FROZEN_SOURCE_COUNT = 37
NEW_SOURCE_SEARCH = FORBIDDEN_UNLESS_A_SPECIFIC_BLOCKING_GAP_IS_DEMONSTRATED
R2_LAW_EXHAUSTION = FORBIDDEN
PHYSICAL_GRAMMAR_SELECTION = FORBIDDEN
EMPIRICAL_PREDICTION = FORBIDDEN
FCP_EFFECT = NONE
```

## Purpose

The empirical-interface primitive gate established a formally admissible law-free contact signature

\[
\Sigma_E=(C,R,\iota_C,\rho)
\]

that can designate probe/interface and record tokens without supplying a response relation, probability kernel, or complete physical possibility set.

The remaining problem is interface completeness. A complete physical probe universe cannot simply be listed as primitive without risking hidden physical-law import.

This challenge asks whether a **small law-free empirical seed** can be expanded by grammar-generated formation into a larger empirical context closure without introducing an independent closure oracle or making the closure depend on desired responses.

## Core question

> Can the grammar itself generate the admissible empirical-interface closure from a small seed, so that the full probe/context family is not independently listed, while the closure construction remains response-law independent?

## Fixed notation

Let:

```text
P = ambient formal context/presentation space
C0 subset P = law-free empirical contact seed
Gamma = family of context constructors
Cl_Gamma(C0) = least Gamma-closed superset of C0, when defined
e = response/evaluation map
rho = terminal-to-record interpretation
```

No candidate closure may inspect `e`, `rho(e(...))`, target record profiles, desired distinguishability, probabilities, or a predeclared physically possible response set.

## Locked candidate families

Test in the following order.

### K0 — Identity/trivial closure

\[
Cl(C_0)=C_0.
\]

Control question: does this avoid smuggling but fail to generate any new empirical accessibility?

### K1 — Arbitrary closure operator

Permit an arbitrary extensive, monotone, idempotent map

\[
Cl:\mathcal P(P)\to\mathcal P(P).
\]

Universal-encoding control: for an arbitrary target `T` with `C0 subseteq T`, can one choose `Cl` so that `Cl(C0)=T` by fiat?

If yes, arbitrary closure has no explanatory selection value.

### K2 — Least closure under a freely chosen constructor family

Let `Gamma` be an independently chosen family of nullary/finitary context constructors. Define the least `Gamma`-closed superset of `C0`.

Test separately:

1. existence/uniqueness of the least closure;
2. nontrivial finite-seed expansion;
3. response-law independence;
4. whether freely choosing `Gamma` merely relocates arbitrary target encoding into the constructor family.

### K3 — Least closure under constructors mechanically inherited from the grammar

Let `Gamma_G` be extracted from the candidate grammar's **formation skeleton only** by a fixed rule declared independently of any empirical response result.

Examples include one-hole context extension by grammar constructors/formation rules.

The extraction may use:

```text
formal constructor arity
formal typing/interface compatibility
grammar formation incidence
syntactic/context insertion structure
```

It may not use:

```text
which records occur
which states are distinguished
which responses are physically wanted
response probabilities
empirical success/failure labels
```

Question: does `Cl_{Gamma_G}(C0)` remove the need for a *separate* empirical closure law, even if the physical privilege of `G` and `C0` remains unresolved?

### K4 — Response-sensitive closure

Controls such as:

```text
add c iff c distinguishes x from y
add c iff e(c,x) produces record r
add c iff response r is physically allowed
add c with weight determined by p(r|c,x)
```

must be classified as response-law or empirical-selection smuggling rather than law-free interface generation.

## Theorem targets

### T1 — Least-constructor-closure theorem

For a context universe `P`, seed `C0`, and finitary constructor family `Gamma`, define a subset `S subseteq P` to be `Gamma`-closed if it contains the result of every `Gamma` constructor whenever all of that constructor's arguments lie in `S`.

Test whether:

\[
Cl_\Gamma(C_0)
=
\bigcap\{S\subseteq P:C_0\subseteq S\text{ and }S\text{ is }\Gamma\text{-closed}\}
\]

exists uniquely and is the least closed superset.

For finitary constructors, test the iterative form by finite depth.

### T2 — Response-law separation

If `C0` and `Gamma` are specified without `e` or `rho`, test whether two incompatible response maps can share the same generated closure.

### T3 — Constructor-family universal encoding

For an arbitrary target `T superset C0`, test whether a freely chosen constructor family can be manufactured so that its least closure is exactly `T`.

If yes, `least closure` is not by itself a non-arbitrariness principle.

### T4 — Grammar-extraction separation

If `Gamma_G` is obtained mechanically from the already-declared formation skeleton of `G`, test whether the generated interface introduces **no additional independent closure selector beyond `G`, the extraction rule, and `C0`**.

This is a bookkeeping/nonduplication result only; it does not establish that `G`, the extraction rule, or `C0` is physically privileged.

## Required finite witness

Construct at least one small seed and response-independent constructor family that yields a strictly larger closure.

Preferred witness:

```text
C0 = {c}
Gamma = {w}
w:P->P
```

with distinct formal contexts

```text
c, w(c), w(w(c)), ...
```

so that a one-element empirical seed generates an unbounded formal context family while two incompatible response evaluators can be defined on the same closure.

Also provide a finite target-encoding counterexample for K1/K2.

## Acceptance criteria

A grammar-generated closure architecture qualifies formally only if:

```text
B1_LEAST_CLOSURE_EXISTS_AND_IS_UNIQUE
B2_FINITE_SEED_CAN_EXPAND_NONTRIVIALLY
B3_CLOSURE_RULE_DOES_NOT_INSPECT_RESPONSES
B4_SAME_CLOSURE_CAN_SUPPORT_INCOMPATIBLE_RESPONSE_LAWS
B5_ARBITRARY_CLOSURE_UNIVERSAL_ENCODING_IS_EXPOSED
B6_FREE_CONSTRUCTOR_FAMILY_UNIVERSAL_ENCODING_IS_EXPOSED
B7_GRAMMAR_DERIVED_CONSTRUCTORS_ADD_NO_SEPARATE_CLOSURE_ORACLE
B8_PHYSICAL_COMPLETENESS_IS_NOT_INFERRED_FROM_FORMAL_CLOSURE
B9_PHYSICAL_PRIVILEGE_OF_G_OR_C0_IS_NOT_ASSUMED
```

## Outcome space

```text
A = NO_NONTRIVIAL_LAW_FREE_INTERFACE_CLOSURE_IS_FORMALLY_AVAILABLE
B = LEAST_CONSTRUCTOR_CLOSURE_IS_FORMALLY_AVAILABLE_BUT_FREE_CONSTRUCTOR_SELECTION_RETAINS_FULL_ARBITRARINESS
C = GRAMMAR_EXTRACTED_LEAST_CLOSURE_REMOVES_AN_INDEPENDENT_INTERFACE_ORACLE_BUT_PHYSICAL_GRAMMAR_SEED_AND_COMPLETENESS_REMAIN_UNESTABLISHED
D = ANY_NONTRIVIAL_CLOSURE_REQUIRES_RESPONSE_LAW_OR_EMPIRICAL_SELECTION_IMPORT
E = FROZEN_CORPUS_IS_INSUFFICIENT_AND_A_SPECIFIC_SOURCE_GAP_IS_IDENTIFIED
F = UNRESOLVED
```

No outcome is a ranking.

## Required outputs

Commit 2 may add only:

```text
audits/PGH0_GRAMMAR_GENERATED_EMPIRICAL_INTERFACE_CLOSURE_CHALLENGE_0_1_0.md
research/formalizations/PGH0_GRAMMAR_GENERATED_EMPIRICAL_INTERFACE_CLOSURE_0_1_0.md      # if a formal schema qualifies
research/derivations/PGH_DERIVATION_LEAST_GRAMMAR_INTERFACE_CLOSURE_0_1_0.md          # if established
research/failures/PGH_FAIL_ARBITRARY_OR_RESPONSE_SENSITIVE_INTERFACE_CLOSURE_0_1_0.md  # if warranted
handoffs/PGH0_GRAMMAR_GENERATED_EMPIRICAL_INTERFACE_CLOSURE_CHALLENGE_HANDOFF_0_1_0.md
```

Do not mutate current-state/navigation files on the scientific branch.

## Commit boundary

```text
COMMIT_1_MESSAGE = Preregister PGH-0 grammar-generated empirical interface closure
COMMIT_2_MESSAGE = Adjudicate PGH-0 grammar-generated empirical interface closure
```

Exactly two commits are permitted.

## Hard stops

Stop before:

- claiming the generated context closure is the complete physical probe universe;
- claiming `PGH-GRAM-0002` is physically privileged;
- treating the empirical seed as unique or fundamental;
- deriving a physical response law;
- beginning R2 law exhaustion;
- unbounded source expansion;
- changing FCP;
- mutating canonical `main` before independent review.
