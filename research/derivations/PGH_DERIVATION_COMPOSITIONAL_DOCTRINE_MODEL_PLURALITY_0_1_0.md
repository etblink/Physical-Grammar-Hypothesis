# PGH-DER-0019 — Compositional Doctrine Model Plurality

## Status

```text
DERIVATION_ID = PGH-DER-0019
STATUS = QUALIFIED_FORMAL
PHYSICAL_CLAIM = NONE
```

## Claim

Bare monoidal composition does not entail a unique stronger doctrine such as symmetry or cartesianness.

## Proof by models

If a stronger property were derivable from the monoidal axioms, every model of those axioms would possess it.

But:

1. the free strict monoidal category on two object-generators and no nonidentity morphism generators is monoidal and nonsymmetric;
2. the free symmetric monoidal category on the same generators is symmetric monoidal but has no arity-changing morphisms `A -> A tensor A` or `A -> I`, hence is not cartesian in the required sense;
3. categories with finite products provide cartesian monoidal examples with diagonal and terminal maps.

Thus the weaker axioms admit models that disagree on the structural permissions under test.

Therefore:

```text
MONOIDAL =>/=> SYMMETRIC
SYMMETRIC_MONOIDAL =>/=> CARTESIAN
BARE_COMPOSITION =>/=> UNIQUE_DOCTRINE
```

## Scope

This is a formal non-entailment result. It does not rank the doctrines physically or mathematically.

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = [MONOIDAL_AXIOMS]
RULE_DEPENDENCIES = NONE
SEMANTIC_ASSUMPTIONS = NONE
PHYSICAL_ASSUMPTIONS = NONE
```
