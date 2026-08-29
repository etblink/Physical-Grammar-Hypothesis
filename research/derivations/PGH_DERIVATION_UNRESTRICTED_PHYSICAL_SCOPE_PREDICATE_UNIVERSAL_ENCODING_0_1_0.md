# PGH-DER-0032 — Unrestricted Physical-Scope Predicate Universal Encoding 0.1.0

## Status

```text
DERIVATION_ID = PGH-DER-0032
STATUS = QUALIFIED_FORMAL_CONTROL
MATHEMATICAL_NOVELTY_CLAIM = NONE
```

## Statement

Let `E` be a set of candidate empirical systems or empirical instantiations.

For every subset

\[
T\subseteq E,
\]

there exists a scope predicate

\[
S_T:E\to\{0,1\}
\]

such that

\[
S_T(e)=1 \iff e\in T.
\]

Hence an unrestricted scope-predicate language can represent every desired subset of empirical systems exactly.

## Proof

Define `S_T` to be the characteristic function of `T`.

Then for each `e in E`, `S_T(e)=1` exactly when `e` belongs to `T`. Therefore the selected scope is exactly `T`.

QED.

## PGH consequence

A declaration of restricted physical scope does not earn explanatory credit merely because it can be written as a predicate or given a short name.

If the permitted scope language can encode arbitrary target subsets, then after seeing empirical outcomes one can always define the candidate's domain to contain the favorable cases and exclude the unfavorable ones.

Therefore a restricted physical scope requires an independent origin constraint analogous to the project's earlier controls on unrestricted response tables, support predicates, and rule languages.

```text
SCOPE_FORM != SCOPE_EXPLANATION
SCOPE_PREDICATE_EXISTENCE != PHYSICAL_APPLICABILITY_DERIVATION
UNRESTRICTED_SCOPE_LANGUAGE = UNIVERSAL_TARGET_SUBSET_ENCODER
```

## Boundary

This result does not prove that every compact or structurally generated scope rule is arbitrary. It establishes only the universal-encoding control that any proposed restricted-scope language must beat.
