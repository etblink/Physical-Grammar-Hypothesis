# PGH-DER-0023 — Typed Interface Response Underdetermination

## Status

```text
DERIVATION_ID = PGH-DER-0023
STATUS = QUALIFIED_FORMAL
PHYSICAL_CLAIM = NONE
```

## Theorem

Let `C` be a finite nonempty set, `R` a finite set, and

\[
T\subseteq C\times R
\]

with every fiber

\[
R_c=\{r:(c,r)\in T\}
\]

nonempty.

If at least one fiber has at least two elements, then `T` admits at least two distinct deterministic sections

\[
f_1,f_2:C\to R
\]

such that

\[
(c,f_i(c))\in T
\]

for all `c`.

## Proof

Choose a context `c_*` with distinct

\[
r_0,r_1\in R_{c_*}.
\]

For every other context `c`, choose one element `r_c in R_c`; this requires only finitely many choices.

Define

\[
f_1(c_*)=r_0,\qquad f_2(c_*)=r_1,
\]

and for `c != c_*` define

\[
f_1(c)=f_2(c)=r_c.
\]

Both maps are sections of `T`, and they differ at `c_*`. QED.

## Locked witness

Take

```text
C = {a,b}
R = {a0,a1,b0,b1}
T = {(a,a0),(a,a1),(b,b0),(b,b1)}
```

Then

```text
f0(a)=a0 ; f0(b)=b0
f1(a)=a1 ; f1(b)=b1
```

are distinct deterministic response maps on the exact same typing relation.

The same fibers also support multiple probability distributions, for example uniform versus biased distributions.

Therefore:

\[
T\not\Rightarrow \text{one response law}.
\]

## Covariance

Under bijections `sigma:C->C'` and `tau:R->R'`, set

\[
T'=(\sigma\times\tau)[T].
\]

If `f` is a section of `T`, then

\[
f'=\tau\circ f\circ\sigma^{-1}
\]

is a section of `T'`.

Distinct sections remain distinct under bijective transport.

Thus response underdetermination is invariant under faithful relabeling of the typed interface.

## Scope

The theorem proves only that a typed interface can fail to determine the response law.

It does not prove:

```text
T_IS_PHYSICALLY_PRIVILEGED
T_IS_COMPLETE
T_MEMBERSHIP_IS_PHYSICAL_POSSIBILITY
ANY_CURRENT_GRAMMAR_GENERATES_A_RESPONSE
```

Those remain separate burdens.