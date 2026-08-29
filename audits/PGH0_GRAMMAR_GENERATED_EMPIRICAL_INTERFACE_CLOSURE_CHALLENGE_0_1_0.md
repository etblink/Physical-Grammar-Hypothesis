# PGH-0 Grammar-Generated Empirical Interface Closure Challenge 0.1.0

## Identity

```text
OPERATION_ID = PGH0_GRAMMAR_GENERATED_EMPIRICAL_INTERFACE_CLOSURE_CHALLENGE
REGISTRY_ID = PGH-OP-0022
CANONICAL_BASE = e6467fa370591b6e8e322a886530dd1d5a496688
PREREGISTRATION_COMMIT = d4e923e05c3c320726f851008b090b652296b564
FROZEN_SOURCE_COUNT = 37
NEW_SOURCE_SEARCH = NONE
R2_LAW_EXHAUSTION = NOT_STARTED
PHYSICAL_GRAMMAR_SELECTION = NONE
EMPIRICAL_PREDICTION = NONE
FCP_EFFECT = NONE
```

## Outcome

```text
OUTCOME = C__GRAMMAR_EXTRACTED_LEAST_CLOSURE_REMOVES_AN_INDEPENDENT_INTERFACE_ORACLE_BUT_PHYSICAL_GRAMMAR_SEED_AND_COMPLETENESS_REMAIN_UNESTABLISHED
LEAST_CONSTRUCTOR_CLOSURE = QUALIFIED_FORMAL
FINITE_SEED_NONTRIVIAL_EXPANSION = PASS
RESPONSE_LAW_SEPARATION = PASS
ARBITRARY_CLOSURE_UNIVERSAL_ENCODING = FAIL_CONTROL_CONFIRMED
FREE_CONSTRUCTOR_SELECTION_UNIVERSAL_ENCODING = FAIL_CONTROL_CONFIRMED
GRAMMAR_EXTRACTED_CLOSURE_ADDS_SEPARATE_ORACLE = NO_AT_DECLARED_FORMAL_SCOPE
PHYSICAL_INTERFACE_COMPLETENESS = UNESTABLISHED
R1_SOLVED = NO
R2_STARTED = NO
```

The challenge establishes a useful but deliberately limited result.

A law-free empirical seed can be expanded into a larger, even unbounded, family of formal empirical contexts by taking the least closure under response-independent constructors. If those constructors are mechanically inherited from the grammar's formation skeleton, the closure does not require a separately listed empirical probe universe or an independent extensional closure table.

However, least closure does not itself create non-arbitrariness. An arbitrary closure operator or freely chosen constructor family can encode any desired target interface. The physical privilege of the grammar, extraction convention, empirical seed, and resulting closure therefore remains unresolved.

---

## 1. K0 — Identity closure

The identity control

\[
Cl(C_0)=C_0
\]

is response-law free but generates nothing new.

```text
NO_SMUGGLING = PASS
NONTRIVIAL_INTERFACE_EXPANSION = FAIL
```

So simply refusing to add contexts cannot solve the completeness problem.

---

## 2. K1 — Arbitrary closure operator

Let `P` be an ambient context space and let `T` be any target satisfying

\[
C_0\subseteq T\subseteq P.
\]

Define

\[
Cl_T(S)=S\cup T.
\]

Then `Cl_T` is extensive, monotone, and idempotent:

- `S subseteq S union T`;
- `S subseteq S'` implies `S union T subseteq S' union T`;
- `(S union T) union T = S union T`.

And because `C0 subseteq T`:

\[
Cl_T(C_0)=T.
\]

Therefore every desired target interface can be encoded directly into an otherwise respectable closure operator.

```text
ARBITRARY_CLOSURE_HAS_SELECTION_VALUE = NO
UNIVERSAL_ENCODING = YES
```

This is one part of `PGH-FAIL-0009`.

---

## 3. K2 — Least closure under constructors

Let `Gamma` be a family of partial finitary constructors on `P`.

A subset `S subseteq P` is `Gamma`-closed if whenever a constructor is defined on arguments in `S`, its result also lies in `S`.

Let

\[
\mathcal F=\{S\subseteq P:C_0\subseteq S\text{ and }S\text{ is }\Gamma\text{-closed}\}.
\]

Because `P` is itself closed under constructors valued in `P`, `F` is nonempty.

Define

\[
Cl_\Gamma(C_0)=\bigcap_{S\in\mathcal F}S.
\]

The intersection contains `C0` and is `Gamma`-closed because each member of `F` is closed. It is contained in every closed superset of `C0` by construction.

Therefore it is the unique least `Gamma`-closed superset of `C0`.

This is qualified as part of `PGH-DER-0009`.

### Finitary iterative form

For finitary constructors define:

\[
C_{n+1}=C_n\cup\{\gamma(\vec c):\gamma\in\Gamma,\ \vec c\in C_n^{k_\gamma},\ \gamma(\vec c)\text{ defined}\}.
\]

Then

\[
C_\omega=\bigcup_{n\ge0}C_n
\]

is `Gamma`-closed. Any finite tuple of arguments lies together in some common finite stage, so its constructor result enters the next stage. Every closed superset of `C0` contains each stage by induction, hence contains `C_omega`.

Thus:

\[
C_\omega=Cl_\Gamma(C_0).
\]

---

## 4. Nontrivial finite-seed witness

Take one seed context:

```text
C0 = {c}
```

and two response-independent unary constructors:

```text
L(c')
R(c')
```

whose formal images remain distinct.

At exact depth `n`, there are `2^n` constructor words applied to `c`:

```text
c
L(c), R(c)
L(L(c)), L(R(c)), R(L(c)), R(R(c))
...
```

The closure through depth `n` therefore contains

\[
1+2+\cdots+2^n=2^{n+1}-1
\]

contexts, and the full finite-depth union is countably infinite.

So:

```text
FINITE_EMPIRICAL_SEED = YES
STRICTLY_LARGER_GENERATED_INTERFACE = YES
UNBOUNDED_FINITE_DEPTH_CONTEXT_FAMILY = YES
```

No response relation or record distribution was used to generate the contexts.

---

## 5. Response-law separation

Let terminal labels be `u,v` and let the record map satisfy:

```text
rho(u)=0
rho(v)=1
```

On the same generated closure define two incompatible evaluators for a fixed candidate state `x`:

```text
e_const(c',x) = u for every generated context c'

e_parity(c',x) =
    u if constructor depth(c') is even
    v if constructor depth(c') is odd
```

Both evaluators use exactly the same:

```text
C0
Gamma
Cl_Gamma(C0)
rho
```

but they produce different record profiles.

Therefore the generated interface does not determine the response law.

```text
CLOSURE_RESPONSE_LAW_SEPARATION = PASS
```

---

## 6. K2 failure — freely chosen constructor families can encode any target

Least closure is not a non-arbitrariness principle when `Gamma` is free.

Take any nonempty seed `C0 subseteq T subseteq P` and choose one seed element `c* in C0`.

For every `t in T minus C0`, introduce a partial unary constructor

\[
\gamma_t(c^*)=t
\]

undefined elsewhere, and introduce no constructors whose values lie outside `T`.

Then the least generated closure is exactly `T`.

If nullary constructors are admitted, the encoding is even more direct: include a constant constructor returning each desired `t`.

Thus:

```text
LEAST_CLOSURE = MATHEMATICALLY_CANONICAL_RELATIVE_TO_GAMMA
FREE_GAMMA_SELECTION = UNIVERSALLY_EXPRESSIVE
TARGET_INTERFACE_CAN_BE_ENCODED_BY_CONSTRUCTOR_CHOICE = YES
```

So K2 alone does not solve `PGH-Q-0020`.

---

## 7. K3 — grammar-extracted constructor family

The stronger candidate does not introduce `Gamma` as a separately selected empirical law.

Let a grammar presentation `G` already contain a response-independent formation skeleton. Fix an extraction convention `E` that maps the formation skeleton to its admissible one-hole context constructors:

\[
\Gamma_G=E(G).
\]

For a simple binary grammar constructor `m(-,-)` and a grammar ground term `a`, the extracted context extensions include:

\[
L_a(C)=m(C,a),
\qquad
R_a(C)=m(a,C).
\]

Starting from the seed hole/context `square`, least closure gives:

```text
square
m(square,a)
m(a,square)
m(m(square,a),a)
m(a,m(square,a))
...
```

No list of those contexts is supplied independently. They are generated from the already-declared formation machinery.

### Separation statement

Once the triple

\[
(G,E,C_0)
\]

is fixed, the resulting

\[
Cl_{E(G)}(C_0)
\]

is fixed. There is no fourth independent extensional object specifying which generated contexts belong to the interface.

Therefore:

```text
SEPARATE_EXTENSIONAL_PROBE_UNIVERSE = NOT_REQUIRED
SEPARATE_ARBITRARY_CLOSURE_TABLE = NOT_REQUIRED
RESPONSE_LAW_INSPECTED_BY_EXTRACTION = NO
```

This is the positive content of the result.

### Exact limitation

It does **not** follow that:

```text
G_IS_PHYSICALLY_PRIVILEGED = NO
E_IS_THE_UNIQUE_PHYSICAL_EXTRACTION = NO
C0_IS_THE_UNIQUE_OR_FUNDAMENTAL_EMPIRICAL_SEED = NO
GENERATED_CLOSURE_IS_THE_COMPLETE_PHYSICAL_PROBE_UNIVERSE = NO
```

Moreover, because a sufficiently unconstrained grammar formation skeleton can itself encode arbitrary structure, moving the interface closure into `G` does not by itself solve the deeper PGH non-arbitrariness problem.

It removes an additional oracle; it does not justify the remaining one.

---

## 8. K4 — response-sensitive closure

Rules such as

```text
add c iff c distinguishes x from y
add c iff e(c,x) yields record r
add c iff record r is physically allowed
weight/add c according to p(r|c,x)
```

are not law-free interface generation.

They inspect the response behavior or physical possibility relation that the grammar is supposed to generate.

Therefore:

```text
RESPONSE_SENSITIVE_CLOSURE = PHYSICAL_LAW_SMUGGLING
```

This is the second part of `PGH-FAIL-0009`.

---

## 9. Acceptance-criteria result

```text
B1_LEAST_CLOSURE_EXISTS_AND_IS_UNIQUE = PASS
B2_FINITE_SEED_CAN_EXPAND_NONTRIVIALLY = PASS
B3_CLOSURE_RULE_DOES_NOT_INSPECT_RESPONSES = PASS_FOR_K2_K3
B4_SAME_CLOSURE_CAN_SUPPORT_INCOMPATIBLE_RESPONSE_LAWS = PASS
B5_ARBITRARY_CLOSURE_UNIVERSAL_ENCODING_IS_EXPOSED = PASS
B6_FREE_CONSTRUCTOR_FAMILY_UNIVERSAL_ENCODING_IS_EXPOSED = PASS
B7_GRAMMAR_DERIVED_CONSTRUCTORS_ADD_NO_SEPARATE_CLOSURE_ORACLE = PASS_AT_FORMAL_SCOPE
B8_PHYSICAL_COMPLETENESS_IS_NOT_INFERRED_FROM_FORMAL_CLOSURE = PASS
B9_PHYSICAL_PRIVILEGE_OF_G_OR_C0_IS_NOT_ASSUMED = PASS
```

The preregistered outcome is therefore C.

---

## 10. Scientific interpretation

The result changes the architecture of the live R1 problem.

Before this operation, a complete empirical interface appeared to require one of two unattractive options:

1. list the complete physical probe set as primitive; or
2. leave empirical accessibility incomplete.

The present result establishes a third formal option:

\[
\boxed{
\text{law-free empirical seed}
+
\text{grammar formation skeleton}
\longrightarrow
\text{generated interface closure}
}
\]

without putting the response map into the closure rule.

But the physical claim remains unearned. Strong PGH still needs a principled account of why the chosen grammar-generated substructure is the physically relevant empirical interface.

---

## 11. R1 consequence

```text
R1_LAW_FREE_EMPIRICAL_CONTACT = FORMALLY_ADMISSIBLE
R1_RESPONSE_LAW_SEPARATION = PASS
R1_REPRESENTATION_ROBUSTNESS = PASS_CONDITIONALLY
R1_GRAMMAR_GENERATED_INTERFACE_CLOSURE = FORMALLY_FEASIBLE
R1_SEPARATE_INTERFACE_ORACLE = NOT_REQUIRED_AT_FORMAL_SCOPE
R1_GRAMMAR_PRIVILEGE = UNESTABLISHED
R1_EMPIRICAL_SEED_PRIVILEGE = UNESTABLISHED
R1_PHYSICAL_COMPLETENESS = UNESTABLISHED
R1_SOLVED = NO
```

The immediate residual question is whether seed choice is itself merely a presentation choice inside a generated interface or whether it carries irreducible physical content.

---

## 12. Source-gap decision

No specific source deficiency blocks this formal adjudication.

```text
SPECIFIC_SOURCE_GAP = NONE
SOURCE_EXPANSION_JUSTIFIED = NO
```

---

## 13. Next sequencing

Recommended next operation:

```text
NEXT_RECOMMENDED_OPERATION = PGH0_EMPIRICAL_GENERATOR_INVARIANCE_AND_SEED_MINIMALITY_GATE
NEXT_OPERATION_AUTHORIZED = NO
```

That gate should test whether two different law-free empirical seeds that generate the same grammar-closed interface are equivalent as presentations of that interface, whether minimal generating seeds exist or are unique, and whether physical privilege can be shifted from a particular seed to the generated substructure without smuggling the target interface back in.

R2 remains deferred.

---

## 14. Final boundary

```text
GRAMMAR_GENERATED_INTERFACE_CLOSURE_FORMAL_FEASIBILITY = PASS
INDEPENDENT_CLOSURE_ORACLE_REQUIRED = NO_AT_DECLARED_SCOPE
FREE_CLOSURE_NONARBITRARINESS = FAIL
FREE_CONSTRUCTOR_NONARBITRARINESS = FAIL
RESPONSE_LAW_IN_CLOSURE = NO_FOR_QUALIFIED_SCHEMA
PHYSICAL_INTERFACE_COMPLETENESS = UNESTABLISHED
PHYSICAL_GRAMMAR_FOUND = NO
PHYSICAL_LAW_DERIVED = NO
EMPIRICAL_PREDICTION = NONE
R1_SOLVED = NO
R2_STARTED = NO
FCP_EFFECT = NONE
```
