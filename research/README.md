# Research artifacts

This directory is reserved for versioned bounded research artifacts.

Planned subdirectories are created only when first needed:

```text
research/derivations/
research/failures/
research/formalizations/
research/models/
research/representation_tests/
```

The directory structure does not imply that any corresponding scientific result currently exists.

## Derivation ancestry

Substantive derivation artifacts should record:

```text
PRIMITIVE_DEPENDENCIES
RULE_DEPENDENCIES
LEMMA_DEPENDENCIES
SEMANTIC_ASSUMPTIONS
PHYSICAL_ASSUMPTIONS
SOURCE_DEPENDENCIES
```

## Failure preservation

Failed derivations belong under `research/failures/` or remain linked there through an explicit superseding/failure artifact.

Failure is a research result, not repository clutter.

## Versioning

Accepted bounded artifacts should be versioned, for example:

```text
PGH_MINIMAL_GRAMMAR_FORMALIZATION_0_1_0.md
PGH_CONTEXTUAL_EQUIVALENCE_DERIVATION_0_1_0.md
PGH_BOUNDARY_CONSERVATION_ANALOGY_FAILURE_0_1_0.md
```

Do not infer scientific status from the existence of a file or directory.
