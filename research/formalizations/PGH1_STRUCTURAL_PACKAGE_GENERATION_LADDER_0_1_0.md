# PGH-1 Structural Package Generation Ladder 0.1.0

## Status

```text
OBJECT_ID = PGH-OBJ-0018
OBJECT_CLASS = STRUCTURAL_PACKAGE_GENERATION_MAP
PHYSICAL_STATUS = NONE
SUCCESSOR_GRAMMAR = NONE
```

## Purpose

Record how structural permissions change as compositional doctrine is strengthened, without treating any doctrine as physically privileged.

## Ladder

| Compositional doctrine | Exchange-like map | Copy-like map | Discard-like map | Selective input still required |
|---|---|---|---|---|
| Bare strict monoidal, no morphism generators | No | No | No | Tensor/composition only |
| Symmetric monoidal | Yes | No | No | Symmetry structure |
| Finite-product/cartesian | Yes | Yes, diagonal | Yes, terminal map | Finite-product doctrine |
| Finite-coproduct/cocartesian | Yes | Dual package: codiagonal is merge-like | Dual package: initial map is create-like | Finite-coproduct doctrine |
| Bicartesian | Both product and coproduct packages | Yes | Yes | Both doctrines |

## Structural lesson

A structural permission can be **generated rather than enumerated** once the doctrine contains a suitable universal property.

This is genuine explanatory compression relative to an object-by-object permission table.

But the hierarchy does not terminate automatically:

\[
D\longrightarrow\Theta_D.
\]

The doctrine `D` carries selective information about which canonical maps exist.

Therefore a future PGH successor architecture must explain doctrine origin as well as rule generation.

## Representation discipline

The current gate uses doctrine-level properties rather than a preferred coordinate or syntactic presentation. This improves representation robustness.

It does not establish physical privilege.

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = [COMPOSITIONAL_STRUCTURE]
RULE_DEPENDENCIES = [CHOSEN_COMPOSITIONAL_DOCTRINE]
SEMANTIC_ASSUMPTIONS = NONE
PHYSICAL_ASSUMPTIONS = NONE
```

## Nonclaims

```text
CARTESIAN = FUNDAMENTAL_PHYSICS        [NO]
COCARTESIAN = FUNDAMENTAL_PHYSICS      [NO]
SYMMETRY = PHYSICAL_SYMMETRY           [NO]
DIAGONAL = PHYSICAL_CLONING             [NO]
TERMINAL_MAP = PHYSICAL_DELETION        [NO]
STRUCTURAL_PACKAGE = PHYSICAL_LAW       [NO]
```
