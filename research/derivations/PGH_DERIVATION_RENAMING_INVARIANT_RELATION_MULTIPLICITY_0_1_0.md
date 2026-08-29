# PGH-DER-0016 — Renaming-Invariant Relation Multiplicity 0.1.0

## Status

```text
DERIVATION_ID = PGH-DER-0016
DERIVATION_STATUS = QUALIFIED_FORMAL
PHYSICAL_CLAIM = NONE
NOVELTY_CLAIM = NONE
```

## Statement

Let `D` be a finite set carrying no structure beyond identity, and let the full symmetric group `S_D` act diagonally on `D^n`.

Every `S_D`-invariant `n`-ary relation is a union of action orbits.

For `|D| >= n`, those orbits are exactly the equality patterns among the `n` argument positions, equivalently the set partitions of `{1,...,n}`.

Thus if `B_n` is the `n`th Bell number, the number of invariant `n`-ary supports is

\[
2^{B_n}.
\]

In particular:

```text
n = 2 -> B_2 = 2 -> 4 invariant supports
n = 3 -> B_3 = 5 -> 32 invariant supports
```

## Proof sketch

Two tuples in `D^n` lie in the same orbit under simultaneous renaming iff they have the same equality pattern:

\[
x_i=x_j \iff y_i=y_j
\]

for all positions `i,j`.

When `|D| >= n`, every set partition of the argument positions can be realized by a tuple, so the orbits are in bijection with all set partitions.

An invariant relation must contain either all or none of each orbit, and any union of orbits is invariant. Therefore the number of invariant relations is the number of subsets of the orbit set.

## Binary control

For `|D| >= 2`, the two orbits are:

\[
\Delta=\{(x,x):x\in D\}
\]

and

\[
\nabla=\{(x,y):x\neq y\}.
\]

The invariant supports are exactly:

```text
EMPTY
DELTA (equality)
NABLA (inequality)
D^2 (full)
```

So two distinct nontrivial proper supports survive maximal label neutrality.

## Ternary control

For `|D| >= 3`, the five equality-pattern orbits are represented by:

```text
AAA
AAB
ABA
ABB
ABC
```

and every union of those five orbits is invariant, yielding 32 invariant ternary supports.

## PGH interpretation

Renaming invariance genuinely removes label-sensitive arbitrariness.

It does not select one local law.

```text
REPRESENTATION_DISCIPLINE = STRONG
RELATION_SPACE_REDUCTION = YES
UNIQUE_NONTRIVIAL_RELATION = NO
SYMMETRY_GROUP_ORIGIN = UNESTABLISHED
R2_PHYSICAL_CREDIT = NONE
```

Even equality, despite being structurally canonical, does not become a unique admissibility law merely from invariance because inequality is equally invariant in the binary control.

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = []
RULE_DEPENDENCIES = [FULL_SYMMETRIC_GROUP_ACTION_ON_BARE_SET]
LEMMA_DEPENDENCIES = []
SEMANTIC_ASSUMPTIONS = NONE
PHYSICAL_ASSUMPTIONS = NONE
SOURCE_DEPENDENCIES = NONE_FOR_FINITE_ORBIT_COUNT
```

## Claim ceiling

```text
FORMAL_THEOREM = YES
INVARIANCE_AS_UNIQUE_LAW_SELECTOR = FAIL
META_LANGUAGE_SELECTED = NO
PHYSICAL_LAW_DERIVED = NO
```
