# PGH-DER-0013 — Free Local Assignment Gluing 0.1.0

## Status

```text
DERIVATION_ID = PGH-DER-0013
DERIVATION_STATUS = QUALIFIED_FORMAL
PHYSICAL_CLAIM = NONE
```

## Statement

Let `mathcal C` be a cover of a set `V`, let `D` be nonempty, and for each `C in mathcal C` let

\[
s_C\in D^C.
\]

Assume pairwise overlap agreement:

\[
s_C|_{C\cap C'}=s_{C'}|_{C\cap C'}
\]

for all contexts `C,C'`.

Then there exists a unique global assignment

\[
s\in D^V
\]

such that

\[
s|_C=s_C
\]

for every context.

## Proof

Because `mathcal C` covers `V`, for every `v in V` there is at least one `C` containing `v`.

Define

\[
s(v):=s_C(v).
\]

If both `C` and `C'` contain `v`, then `v in C cap C'`; overlap agreement gives

\[
s_C(v)=s_{C'}(v),
\]

so the definition is well defined.

For each `C`, the constructed `s` agrees pointwise with `s_C`, hence `s|_C=s_C`.

If another global assignment `t` has the same restrictions, then for every `v`, choosing any `C` containing `v` gives

\[
t(v)=t|_C(v)=s_C(v)=s(v).
\]

Thus `t=s`.

## Consequence

For the assignment schema with unrestricted local sections

\[
A(C)=D^C,
\]

ordinary cover structure plus equality-on-overlap cannot by itself generate a global obstruction.

Any nonextendability in this schema requires additional selective structure, such as proper local supports

\[
R_C\subsetneq D^C,
\]

or an equivalent restriction on admissible local sections.

This is an explanatory-location theorem, not a physical-law theorem.

## Finite control

For the triangle cover

\[
\{\{0,1\},\{1,2\},\{2,0\}\}
\]

with `D={0,1}`, all eight global assignments induce overlap-compatible local families, and every overlap-compatible family is one of those eight.

For inequality supports on cycle edges, the locked control instead yields:

```text
C3 = 0
C4 = 2
C5 = 0
C6 = 2
C7 = 0
C8 = 2
```

showing that the obstruction appears only after local admissibility is restricted.

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = []
RULE_DEPENDENCIES = [set cover; ordinary functions; equality on overlaps]
LEMMA_DEPENDENCIES = []
SEMANTIC_ASSUMPTIONS = NONE
PHYSICAL_ASSUMPTIONS = NONE
SOURCE_DEPENDENCIES = [frozen PGH-1 local/global corpus as prior-art context only]
```

## Limitations

The theorem does not establish:

```text
A_PHYSICALLY_PRIVILEGED_COVER
A_PHYSICALLY_COMPLETE_DOMAIN
A_PHYSICALLY_JUSTIFIED_LOCAL_SUPPORT_FAMILY
A_SUCCESSOR_GRAMMAR
A_PHYSICAL_LAW
```
