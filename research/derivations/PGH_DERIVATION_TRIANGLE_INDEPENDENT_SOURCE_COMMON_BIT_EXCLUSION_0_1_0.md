# PGH-DER-0033 — Triangle Independent-Source Common-Bit Exclusion 0.1.0

## Statement

For arbitrary finite source supports and arbitrary normalized stochastic local kernels, the independent-source triangle model `T_ind` cannot realize the nondegenerate perfect common-bit distribution

\[
p_*(000)=p_*(111)=\tfrac12.
\]

The same pairwise-access topology can realize `p_*` if the three sources are allowed to be correlated, and a one-common-source model can realize every finite joint distribution.

## Model

Let positive-support source values be `u in U+`, `v in V+`, `w in W+`, with

\[
p(u,v,w)=p_U(u)p_V(v)p_W(w),
\]

and local kernels

\[
A_{u,w}(a),\quad B_{u,v}(b),\quad C_{v,w}(c).
\]

For every positive-support source triple, the conditional observed law is the product

\[
A_{u,w}\otimes B_{u,v}\otimes C_{v,w}.
\]

## Lemma 1 — perfect agreement forces local determinism at every source triple

Assume the induced observed distribution has support only on `{000,111}`.

All terms in the mixture are nonnegative. Therefore for every positive-support `(u,v,w)`, the product conditional law itself must assign zero mass to every disagreement outcome.

Let

```text
S_A(u,w) = support of A_{u,w}
S_B(u,v) = support of B_{u,v}
S_C(v,w) = support of C_{v,w}
```

Each support is a nonempty subset of `{0,1}`. Their Cartesian product must satisfy

\[
S_A(u,w)\times S_B(u,v)\times S_C(v,w)
\subseteq\{000,111\}.
\]

The only nonempty Cartesian-product subsets of `{000,111}` are `{000}` and `{111}`. Hence every local kernel is deterministic at that source input and the three deterministic outputs agree.

There exist bits

\[
f(u,w),\quad g(u,v),\quad h(v,w)
\]

such that for all positive-support source triples

\[
f(u,w)=g(u,v)=h(v,w).
\]

## Lemma 2 — the common deterministic output is constant

Fix any positive-support `u` and any positive-support `v_0`. For arbitrary positive-support `w_1,w_2`,

\[
f(u,w_1)=g(u,v_0)=f(u,w_2).
\]

Therefore `f(u,w)` is independent of `w`; write it as `F(u)`.

Similarly, for fixed `u` and arbitrary positive-support `v`, equality with `f` gives

\[
g(u,v)=F(u).
\]

Now fix any positive-support `v,w`. For any positive-support `u_1,u_2`,

\[
F(u_1)=h(v,w)=F(u_2).
\]

Thus `F` is constant on positive-support `U`. The common observed output is therefore almost surely a single constant bit.

## Contradiction

`p_*` is nondegenerate: it assigns probability `1/2` to common output 0 and `1/2` to common output 1.

The preceding lemmas show that any perfect-agreement distribution in `T_ind` must be degenerate. Therefore

\[
\boxed{p_*\notin T_{\mathrm{ind}}}.
\]

## Same-topology correlated-source control

Drop source independence while retaining the pairwise access diagram. Let a fair bit `L` satisfy

\[
U=V=W=L
\]

with probability one, and let every local output return the source bit it sees.

Then

\[
p(000)=p(111)=\tfrac12.
\]

Hence

\[
\boxed{p_*\in T_{\mathrm{corr}}}.
\]

This proves that independence of the sources is an essential selective assumption; the pairwise-access topology alone does not exclude `p_*`.

## Common-source universality control

For any finite joint distribution `q(a,b,c)`, take a shared latent variable

\[
\Lambda=(a,b,c)
\]

with `p(lambda)=q(a,b,c)`. Let the three local kernels deterministically output the corresponding coordinate.

Then the induced observed distribution is exactly `q`.

Therefore

\[
\boxed{T_{\mathrm{common}}=\Delta(A\times B\times C)}
\]

at finite scope: the common-source control represents every finite joint distribution.

## Interpretation ceiling

The theorem establishes a real structural model-class exclusion with local kernels unrestricted.

It does not establish that mutually independent pairwise sources or the triangle topology are physically privileged. The exclusion must be charged to the explicit source/resource architecture.

```text
FORMAL_RESULT = QUALIFIED
PHYSICAL_LAW = NONE
STRONG_PGH_CANDIDATE = NONE
R2B = UNSATISFIED
```
