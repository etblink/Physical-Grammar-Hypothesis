# PGH-1 Generated Cover / Compatibility Schema 0.1.0

## Status

```text
OBJECT_ID = PGH-OBJ-0014
OBJECT_CLASS = PROVISIONAL_FORMAL_SCHEMA
PHYSICAL_STATUS = UNESTABLISHED
SUCCESSOR_GRAMMAR = NO
```

## Purpose

Factor the local-to-global mechanism into four independently auditable ingredients:

\[
(\mathcal C,D,\rho,\{R_C\}).
\]

Here:

- `mathcal C` is a family of local contexts covering a formal carrier `V`;
- `D` is a local value/record-label domain;
- `rho` denotes canonical restriction maps between assignment spaces;
- `R_C subseteq D^C` is the local admissibility support on context `C`.

This schema is not a physical grammar. It exists to expose where selective information enters.

## Conditional cover extraction

Given a grammar-generated empirical context family and a presentation in which each context `c` exposes finite formal constituent incidence, define

```text
SUPPORT(c) = finite set of formal positions/subcomponents occurring in c
GENERATED_COVER = { SUPPORT(c) }
```

The extraction is result-independent if it inspects syntax/incidence only.

```text
COVER_EXTRACTION = MECHANICAL_AT_PRESENTATION_SCOPE
REPRESENTATION_INDEPENDENCE = NOT_ESTABLISHED
PHYSICAL_PRIVILEGE = NONE
```

## Domain inheritance

The law-free empirical contact signature may provide a set or typed family of record labels `R`.

A finite local value domain `D` may be chosen from such labels for formal testing provided this introduces no response relation, probability distribution, allowed tuple set, or complete possibility partition.

```text
DOMAIN_LABEL_AVAILABILITY = PERMITTED
DOMAIN_AS_COMPLETE_PHYSICAL_STATE_SPACE = NOT_ESTABLISHED
```

## Canonical overlap compatibility

For `C' subseteq C`, local assignments are ordinary functions and restrict canonically:

\[
\rho_{C,C'}:D^C\to D^{C'},\qquad s\mapsto s|_{C'}.
\]

A family is overlap-compatible when

\[
s_C|_{C\cap C'}=s_{C'}|_{C\cap C'}.
\]

No additional target-dependent compatibility predicate is part of this schema.

## Free local assignment case

If

\[
R_C=D^C
\]

for every context, then every overlap-compatible family glues uniquely to a global assignment on `V`.

Thus:

```text
UNRESTRICTED_LOCAL_SUPPORT = NO_LOCAL_TO_GLOBAL_OBSTRUCTION
```

See `PGH-DER-0013`.

## Proper-support case

A nontrivial support family satisfies, for at least one context,

\[
R_C\subsetneq D^C.
\]

Such a family can generate global obstruction when combined with incidence/overlap structure. The odd-cycle inequality witness is one formal example.

However, the schema does not explain the origin of `R_C`.

```text
PROPER_LOCAL_SUPPORT = SELECTIVE_INFORMATION
ORIGIN_OF_SELECTIVE_INFORMATION = UNRESOLVED
```

## No-smuggling boundary

The following do not count as explanatory support generation:

```text
OBSERVED_RESPONSE_TABLE -> R_C
TARGET_BELL_OR_CONTEXTUALITY_SUPPORT -> R_C
DESIRED_GLOBAL_FORBIDDEN_SET -> R_C
ARBITRARY_LOOKUP_TABLE -> R_C
ARBITRARY_PGH_GRAM_0002_FORMATION_ENTRIES -> R_C
```

Any future successor grammar must explain why its local supports have the form they do without deriving them from the physical exclusions used to evaluate the grammar.

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = [PGH-OBJ-0010]
RULE_DEPENDENCIES = [ordinary functional restriction; presentation support extraction]
LEMMA_DEPENDENCIES = [PGH-DER-0013]
SEMANTIC_ASSUMPTIONS = [record labels may serve as formal value labels]
PHYSICAL_ASSUMPTIONS = NONE_CLAIMED
SOURCE_DEPENDENCIES = [frozen PGH-1 local/global corpus]
```

## Scientific ceiling

```text
LOCAL_TO_GLOBAL_FORMAL_ARCHITECTURE = AVAILABLE
PROPER_SUPPORT_GENERATION = NOT_AVAILABLE
PHYSICAL_LOCAL_SUPPORT = NOT_ESTABLISHED
PHYSICAL_LAW_DERIVED = NO
```
