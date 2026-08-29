# PGH-FAIL-0015 — Local Admissibility Support Origin 0.1.0

## Status

```text
FAILURE_ID = PGH-FAIL-0015
DERIVATION_STATUS = FAILED_PRESERVED
FAILURE_CLASS = PHYSICS_SMUGGLED_OR_UNEXPLAINED_SELECTOR
```

## Failed claim

> Once a cover, value domain, and overlap rule are generated, proper local admissibility supports can be treated as an innocuous formal detail and the resulting global exclusions credited to grammar.

This claim fails.

## Why it fails

The family

\[
\{R_C\subseteq D^C\}
\]

contains selective information. It determines which local tuples are admitted before global compatibility is tested.

If `R_C=D^C` everywhere, `PGH-DER-0013` proves every overlap-compatible family glues uniquely. Therefore the nontrivial exclusion power comes from proper local support, or from some mathematically equivalent restriction on local sections.

At current scope PGH has no independently justified origin for that restriction.

## Failure modes

### 1. Response-derived supports

If the supports are learned from known response tables, measured probabilities, quantum supports, Bell/contextuality scenarios, or a desired empirical partition, the physical selection has been inserted before grammar acts.

```text
CLASS = PHYSICS_SMUGGLED
```

### 2. Arbitrary support tables

Arbitrary supports can encode arbitrary exclusions.

For example, using a single context `C=V` and setting

\[
R_V=S
\]

for any desired `S subseteq D^V` directly defines the allowed global models to be exactly `S`.

```text
CLASS = UNIVERSAL_ENCODING
```

### 3. Reusing arbitrary extensional formation

If the supports are read directly from freely chosen entries of `PGH-GRAM-0002`, the old universal-table failure remains. The table has only moved from `F` to `{R_C}`.

```text
CLASS = REPACKAGED_PGH_FAIL_0001
```

### 4. Result-directed support optimization

Choosing a compact support rule because it reproduces a desired no-go theorem or known physical law does not establish independent motivation.

```text
CLASS = DESIRED_RESULT_DEPENDENCE
```

## What survives

The local-to-global obstruction mechanism itself survives.

A compact, independently justified rule for generating local supports could in principle create genuine global impossibility without listing forbidden global configurations.

The failed claim is only that the present project has already earned such a rule.

## Scientific consequence

The next grammar-discovery burden is no longer:

> find any formal mechanism that excludes global structures.

That burden was met by `PGH-DER-0012`.

It is now:

\[
\boxed{\text{derive nontrivial local admissibility from compact, non-result-directed grammar structure.}}
\]

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = [PGH-OBJ-0010]
RULE_DEPENDENCIES = [PGH-DER-0013; PGH-DER-0012]
LEMMA_DEPENDENCIES = []
SEMANTIC_ASSUMPTIONS = [law-free record labels only]
PHYSICAL_ASSUMPTIONS = NONE_ACCEPTED
SOURCE_DEPENDENCIES = [frozen PGH-1 local/global corpus]
```

## Preserved boundary

```text
LOCAL_TO_GLOBAL_MECHANISM_REJECTED = NO
PROPER_SUPPORT_AS_CURRENTLY_EXPLAINED = NO
SUCCESSOR_GRAMMAR_QUALIFIED = NO
R2_SATISFIED = NO
PHYSICAL_LAW_DERIVED = NO
```
