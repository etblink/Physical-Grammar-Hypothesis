# PGH-1 Local Rule Language Origin Map 0.1.0

## Status

```text
OBJECT_ID = PGH-OBJ-0016
OBJECT_CLASS = META_LANGUAGE_CANDIDATE_MAP
PHYSICAL_STATUS = NONE
SUCCESSOR_GRAMMAR = NONE
```

## Purpose

Map candidate ways of fixing a local admissibility rule language before its physical consequences are known.

The map is not a ranking of mathematical formalisms and does not declare any formal language fundamental.

## Layer decomposition

A local support generator can hide choices at several distinct layers:

\[
\text{primitive vocabulary}
\to
\text{formation / typing rules}
\to
\text{equations / rewrites / invariances}
\to
\text{local support}
\to
\text{global obstruction}.
\]

A successful R2 grammar must prevent target physical information from being inserted at any earlier layer.

## Candidate family table

| Candidate | Canonical conditional on | Selective power | Current blocker | R2 status |
|---|---|---|---|---|
| Unrestricted primitive adjunction | nothing substantive | arbitrary | primitive interpretation can be target table | reject |
| Free/initial term language | fixed signature / types | formation only unless signature selective | signature/type origin | conditional, insufficient |
| Automorphism-invariant relation language | fixed base structure/group action | reduces relations to orbit unions | multiple invariant supports; group origin | conditional, insufficient |
| Compositional-role/type language | fixed incidence/formation structure | can forbid type mismatch | inherits arbitrary/presentation-dependent incidence | conditional, insufficient |
| Projection-kernel coherence language | fixed presentation projection `q` | generates equations/coherence | `q` underdetermined | conditional, insufficient |
| Common structural core | fixed representation class | representation discipline | tends to be too weak or leaves multiple admissible relations | control |

## Free / initial construction

For a fixed signature `Sigma`, the free term language `T(Sigma)` is distinguished by a universal property.

That universal property does real mathematical work: it makes the generated syntax canonical relative to `Sigma`.

But it does not explain `Sigma`.

In the absence of additional equations, distinct terms remain distinct in the free term algebra. Therefore nontrivial equational selection must be supplied through:

```text
SIGNATURE / TYPE RESTRICTION
ADDED EQUATIONS
ADDED REWRITES
SEMANTIC INTERPRETATION
```

Free construction is therefore a **canonical amplifier of given structure**, not a source of selective physical law by itself.

## Automorphism-invariant construction

For fixed base structure `B`, the action of `Aut(B)` gives a canonical orbit decomposition.

Relations invariant under that action are unions of orbits.

This can sharply reduce the relation space.

For a bare finite set under the full symmetric group:

```text
BINARY_ORBITS = 2
BINARY_INVARIANT_SUPPORTS = 4
TERNARY_ORBITS_FOR_|D|>=3 = 5
TERNARY_INVARIANT_SUPPORTS = 32
```

So invariance is a genuine compression of arbitrary relation choice but not a unique selector.

## Role / type extraction

Types can be defined extensionally from where expressions may occur and how they compose.

This is conceptually attractive for PGH because it could make type structure emerge from grammatical role.

Current limitation:

```text
ROLE_PROFILE_SOURCE = CURRENT_FORMATION_OR_PRESENTATION_INCIDENCE
CURRENT_FORMATION = ARBITRARY_AT_PHYSICAL_SCOPE
PRESENTATION_INCIDENCE = NOT_REPRESENTATION_INDEPENDENT
```

Therefore role-derived typing is not yet an independently grounded meta-language.

## Projection-kernel coherence

A presentation projection `q:P->I` canonically determines which presentations are identified.

Its kernel generates equations/coherence constraints without listing them individually.

This is real generative compression, but it is conditional on `q`.

Prior PGH work already established:

```text
PRIVILEGED_PRESENTATION_PROJECTION = UNDERDETERMINED
```

Thus coherence generation relocates the origin problem into the projection unless `q` is independently fixed.

## Common structural core

A language containing only distinctions preserved under every admissible representation change is an attractive representation-independent candidate.

But two failure modes remain:

1. the common core is too weak to generate proper supports;
2. it contains several equally structural relations and still needs a law selector.

Equality on a bare set illustrates the point. Equality is canonical, yet inequality is equally invariant under full renaming, and the language containing both does not say which relation should govern a given local context.

## Meta-language test standard

A future candidate meta-language receives positive R2 priority only if it satisfies all of:

```text
PRE_TARGET_FIXATION = YES
REPRESENTATION_ROBUST = YES_OR_EXPLICITLY_TESTABLE
PRIMITIVE_SEMANTIC_LOADING = NO
UNIVERSAL_SUPPORT_ENCODING = NO
NONTRIVIAL_SELECTIVE_POWER = YES
LOCAL_SUPPORT_GENERATED = YES
PHYSICAL_BRIDGE = INDEPENDENTLY_JUSTIFIED_OR_OPENLY_SEPARATE
```

## Current conclusion

```text
IMMEDIATE_META_LANGUAGE_WINNER = NONE
FREE_LANGUAGE = CANONICAL_BUT_NONSELECTIVE
INVARIANT_LANGUAGE = RESTRICTIVE_BUT_NONUNIQUE
ROLE_TYPE_LANGUAGE = INHERITS_UNEARNED_BASE_STRUCTURE
COHERENCE_LANGUAGE = INHERITS_UNEARNED_PROJECTION
META_LANGUAGE_SOURCE_GAP = SG3_META_LANGUAGE_AND_LOGICAL_FRAMEWORK_ORIGIN
```

The next source operation should study formal frameworks whose explicit subject is the organization and translation of logics/languages themselves, without treating their existence as evidence that any such framework is physically fundamental.
