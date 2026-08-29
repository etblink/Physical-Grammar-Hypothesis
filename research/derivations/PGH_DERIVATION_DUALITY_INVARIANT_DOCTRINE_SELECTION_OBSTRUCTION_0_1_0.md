# PGH-DER-0020 — Duality-Invariant Doctrine Selection Obstruction

## Status

```text
DERIVATION_ID = PGH-DER-0020
STATUS = QUALIFIED_FORMAL
PHYSICAL_CLAIM = NONE
```

## Claim

A doctrine selector invariant under categorical opposition cannot privilege cartesian structure over the cocartesian dual purely by opposition-invariant form.

## Setup

Categorical opposition exchanges products and coproducts:

\[
C\text{ has finite products}
\iff
C^{op}\text{ has finite coproducts}.
\]

Let `S` be a selector whose verdict is invariant under opposition:

\[
S(C)=S(C^{op}).
\]

## Result

If `S` uniquely privileges the product doctrine in `C` while rejecting the corresponding coproduct doctrine in `C^op`, then opposition changes the verdict, contradicting the assumed invariance.

Therefore an opposition-invariant selector must instead do at least one of the following:

1. treat the product/coproduct pair as a dual equivalence class;
2. select a self-dual or richer doctrine;
3. use additional structure that is not opposition-invariant.

Hence:

```text
OPPOSITION_INVARIANCE =>/=> UNIQUE_CARTESIAN_PRIVILEGE
```

## Scope safeguard

The theorem concerns formal selector symmetry only.

```text
CATEGORICAL_OPPOSITION = PHYSICAL_EQUIVALENCE
```

is **not** asserted.

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = [CATEGORY_OPPOSITION]
RULE_DEPENDENCIES = [SELECTOR_OPPOSITION_INVARIANCE]
SEMANTIC_ASSUMPTIONS = NONE
PHYSICAL_ASSUMPTIONS = NONE
```
