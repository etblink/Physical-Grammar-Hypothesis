# PGH-DER-0029 — Sparse DAG Conditional Independence

## Status

```text
DERIVATION_ID = PGH-DER-0029
STATUS = QUALIFIED_FORMAL
PHYSICAL_CLAIM = NONE
```

## Setup

Let finite random variables `A,B,C` have a joint distribution factorizing over the directed chain

\[
A\to B\to C
\]

as

\[
p(a,b,c)=p(a)p(b\mid a)p(c\mid b).
\]

No physical causal interpretation is assumed.

## Claim

For every `b` with `p(b)>0`,

\[
p(a,c\mid b)=p(a\mid b)p(c\mid b).
\]

Therefore

\[
\boxed{A\perp C\mid B}.
\]

## Proof

For `p(b)>0`,

\[
\begin{aligned}
p(a,c\mid b)
&=\frac{p(a,b,c)}{p(b)}\\
&=\frac{p(a)p(b\mid a)p(c\mid b)}{p(b)}\\
&=\left(\frac{p(a)p(b\mid a)}{p(b)}\right)p(c\mid b)\\
&=p(a\mid b)p(c\mid b).
\end{aligned}
\]

This is exactly conditional independence.

## Locked counterdistribution

Let `A` and `B` be independent fair bits and let `C=A` deterministically.

Then for either `b`,

\[
P(A=0,C=0\mid B=b)=1/2
\]

while

\[
P(A=0\mid B=b)P(C=0\mid B=b)=1/4.
\]

Hence the distribution violates the derived conditional independence and cannot factorize over the sparse chain.

## Scope

The theorem shows that fixed sparse wiring can impose a proper restriction on a finite joint-distribution class while the local conditional kernels remain otherwise free.

It does not establish that the graph is physical causation or that the variables correspond to empirical quantities.
