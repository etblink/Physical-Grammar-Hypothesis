# PGH-DER-0022 — Independent Relabeling Cross-Type Dichotomy

## Status

```text
DERIVATION_ID = PGH-DER-0022
STATUS = QUALIFIED_FORMAL_CONDITIONAL
PHYSICAL_CLAIM = NONE
```

## Scope warning

This theorem assumes **full independent permutation automorphy** of one fixed cross-type relation. It must not be confused with ordinary covariance of a structure under relabeling.

Canonical `PGH-FAIL-0002` already establishes that this distinction matters.

## Setup

Let `C` and `R` be nonempty sets. Let

\[
G=S_C\times S_R
\]

act on `C x R` by

\[
(\sigma,\tau)\cdot(c,r)=(\sigma(c),\tau(r)).
\]

Let `S subset C x R` satisfy the strong automorphy condition

\[
gS=S\quad\forall g\in G.
\]

## Theorem 1 — empty/complete dichotomy

Then

\[
S=\varnothing
\]

or

\[
S=C\times R.
\]

### Proof

For arbitrary pairs `(c,r)` and `(c',r')`, choose permutations `sigma` and `tau` with

\[
\sigma(c)=c',\qquad \tau(r)=r'.
\]

Thus `G` acts transitively on `C x R`, so there is exactly one orbit.

An invariant subset under a group action is a union of whole orbits. With one orbit, the only invariant subsets are the empty union and the whole orbit. QED.

## Theorem 2 — deterministic control

Assume `C` is nonempty and `|R|>1`. There is no function

\[
f:C\to R
\]

satisfying

\[
f(\sigma c)=\tau f(c)
\]

for every `c` and every independently chosen `sigma in S_C`, `tau in S_R`.

### Proof

Set `sigma=id`. Then

\[
f(c)=\tau f(c)
\]

for every permutation `tau` of `R`.

For `|R|>1`, no element of `R` is fixed by every permutation. Contradiction. QED.

If `|R|=1`, the unique map is trivially invariant and carries no nontrivial outcome selectivity.

## Coupled-action countercontrol

If an additional bijection

\[
\phi:C\to R
\]

is supplied and relabelings are restricted to

\[
(\sigma,\phi\sigma\phi^{-1}),
\]

the graph

\[
\Gamma_\phi=\{(c,\phi(c)):c\in C\}
\]

is invariant and can be proper and nonempty.

This demonstrates that the dichotomy is caused by the strong independent-automorphy premise, not by covariance under change of notation.

## Correct interpretation

```text
FULL_INDEPENDENT_PERMUTATION_AUTOMORPHY => EMPTY_OR_COMPLETE_RELATION
RELABELING_COVARIANCE => DOES_NOT_IMPLY_EMPTY_OR_COMPLETE_RELATION
```

The theorem supplies a useful homogeneity control. It does not establish that outcome neutrality or representation neutrality requires the automorphy premise.