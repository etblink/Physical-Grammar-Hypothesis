# PGH-FAIL-0017 — Meta-Language Origin Relocation 0.1.0

## Status

```text
FAILURE_ID = PGH-FAIL-0017
DERIVATION_STATUS = FAILED_PRESERVED
FAILURE_CLASS = UNDERDETERMINED
PHYSICAL_CLAIM = NONE
```

## Failed claim

> Replacing arbitrary local support tables by a canonical/free/invariant rule-language construction is sufficient to explain the origin of the local admissibility law.

This claim fails at current scope.

## Failure pattern

The explanatory burden can move upstream without disappearing:

\[
R_C
\to
\text{formula/rule defining }R_C
\to
\text{restricted language admitting that rule}
\to
\text{meta-language construction generating the restricted language}.
\]

A move is explanatory only if the upstream layer is fixed by less target-specific and independently motivated structure.

## Control 1 — primitive adjunction

For any target support `R`, introduce a primitive predicate `P_R` interpreted as exactly `R`.

Then the target has a one-symbol description.

Nothing has been derived.

```text
SHORT_DESCRIPTION = YES
EXPLANATORY_COMPRESSION = NO
```

## Control 2 — free construction

A free/initial language is canonical relative to its signature, but the signature remains input.

If the signature is unselective, the free language is unselective.

If the signature contains typed/partial operations that generate exclusions, the selectivity is already in those declarations.

## Control 3 — invariance

Automorphism invariance restricts admissible relations to unions of orbits.

It does not choose one orbit union.

In the bare binary case both equality and inequality are nontrivial full-renaming-invariant supports.

Therefore invariance reduces arbitrariness without eliminating rule selection.

## Control 4 — type extraction

Types extracted from arbitrary extensional formation profiles inherit the arbitrary formation table.

Types extracted from presentation positions inherit presentation dependence.

Neither route currently supplies an independently grounded physical rule language.

## Control 5 — projection-kernel equations

A fixed presentation projection generates a canonical kernel equivalence and therefore a canonical equation/coherence language relative to that projection.

But `PGH-FAIL-0004` already establishes that the privileged projection is underdetermined.

The language-origin problem is therefore relocated into `q`.

## Control 6 — common core

Taking only distinctions invariant under every accepted representation can yield a sparse common language.

But a common language does not itself specify which formula/relation in that language becomes admissibility law.

If the common core is narrowed until only trivial relations remain, selectivity is lost; if broadened to regain useful distinctions, multiple candidate relations reappear.

## What the failure does not establish

```text
META_GRAMMAR_IMPOSSIBLE = NO
INFINITE_REGRESS_PROVED = NO
EQUATIONAL_LANGUAGE_USELESS = NO
TYPE_THEORY_USELESS = NO
COHERENCE_USELESS = NO
SYMMETRY_USELESS = NO
```

The failure is narrower:

```text
CURRENT_PGH_DOES_NOT_YET_FIX_THE_SELECTIVE_META_LANGUAGE = YES
```

## Source consequence

The frozen 51-source corpus lacks a dedicated lane for theories whose explicit subject is organization/translation of logical languages and their structural rules.

This justifies a targeted future source intake on:

```text
INSTITUTION_THEORY_AND_LOGICAL_FRAMEWORKS
CATEGORICAL_LOGIC
STRUCTURAL_PROOF_THEORY
RELATED_META_LOGICAL_INVARIANCE_FRAMEWORKS
```

That source gap is not evidence that those fields solve PGH.

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = [PGH-OBJ-0015]
RULE_DEPENDENCIES = [PGH-DER-0014, PGH-DER-0015, PGH-DER-0016]
LEMMA_DEPENDENCIES = []
SEMANTIC_ASSUMPTIONS = NONE
PHYSICAL_ASSUMPTIONS = NONE
SOURCE_DEPENDENCIES = FROZEN_51_SOURCE_CORPUS_FOR_GAP_AUDIT_ONLY
```

## Preservation reason

This failure prevents future PGH work from treating words such as `free`, `initial`, `canonical`, `invariant`, `typed`, or `coherent` as automatic explanations of why a physical rule language has its particular selective content.
