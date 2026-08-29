# PGH-OBJ-0046 — Post-Kp Successor Plurality Equivalence Map 0.1.0

```text
OBJECT_ID = PGH-OBJ-0046
STATUS = QUALIFIED_FORMALIZATION
DECLARING_OPERATION = PGH-OP-0082
TARGET_INPUT = NONE
```

## Two levels of equivalence

### Formal grammar level `G`

The five admitted packages contain two abstract three-node path grammar classes up to variable relabeling:

```text
G_NC = NONCOLLIDER_PATH_CLASS
  represented historically by PGH-GRAM-0008
  admitted post-Kp embeddings = PGH-OBJ-0042, PGH-OBJ-0044

G_COL = COLLIDER_PATH_CLASS
  PGH-GRAM-0009
  admitted embeddings = PGH-OBJ-0041, PGH-OBJ-0043, PGH-OBJ-0045
```

Thus:

```text
FORMAL_G_COUNT = 2
```

The historical separator-at-B noncollider embedding is not part of the admitted plurality because its frozen Kp instantiation failed.

## Candidate package level `C=(G,J,S,I)`

The common instantiation protocol assigns noninterchangeable empirical role predicates:

```text
A = EARLIEST_OR_UPSTREAM
B = INTERMEDIATE
C = LATEST_OR_DOWNSTREAM
```

A candidate-level representation equivalence must preserve those role predicates as well as the bridge and empirical restriction.

The five restrictions are:

```text
PGH-OBJ-0041: A ⟂ C
PGH-OBJ-0042: A ⟂ B | C
PGH-OBJ-0043: A ⟂ B
PGH-OBJ-0044: B ⟂ C | A
PGH-OBJ-0045: B ⟂ C
```

No nonidentity permutation of `A,B,C` preserves all three ordered empirical role predicates.

Therefore a formal relabeling that maps one graph picture into another does not by itself map the complete physical candidate package into the other.

```text
PHYSICAL_CANDIDATE_PACKAGE_COUNT = 5
```

This count means five distinct frozen empirical hypotheses under the current `J/I`; it does not mean five fundamentally distinct ontological grammars.

## Internal automorphisms

Some packages have formal automorphisms, such as exchange of the two outer parents of a collider. Such automorphisms do not create additional package identities and do not reduce distinct packages whose center/separator occupies a different empirical role.

## Selection-map result

| Selector | Result | Reason |
|---|---|---|
| formal primitive count | tie | all admitted DAG packages have three roles and two edges |
| representation-disciplined description length | no unique winner | no pre-qualified invariant complexity measure distinguishes the five |
| graph symmetry | no unique physical selector | collider/noncollider classes each possess role-independent structural symmetries; elegance is not physical evidence |
| ordered role architecture | no selector | temporal/upstream order does not itself imply which role must be collider or separator |
| causal-arrow alignment | prohibited | arrows are causal-ontology neutral in the qualified bridge |
| prior use of PGH-GRAM-0008 | no positive privilege | historical use does not confer post-failure priority |
| known Kp negative | elimination only | it kills the historical separator-at-B package but gives no positive ranking among the five survivors |
| lexicographic package ID | administrative only | deterministic and outcome-neutral but scientifically arbitrary |

## Operational consequence

A deterministic administrative tie-break could schedule one candidate first without target leakage, but it would discard information and would not justify treating the scheduled package as uniquely preferred.

Because all five share the same target-interface class, the scientifically cleaner next architecture is a **common-target multi-candidate empirical program** in which one prospectively selected target confronts all five frozen restrictions under explicit multiplicity and decision rules.

That later program must be frozen before target discovery.

## Nonclaims

```text
UNIQUE_SUCCESSOR_SELECTED = NO
FIVE_FUNDAMENTAL_GRAMMARS_ESTABLISHED = NO
TWO_FORMAL_GRAMMAR_CLASSES_MEANS_TWO_PHYSICAL_THEORIES = NO
TARGET_DISCOVERY_AUTHORIZED = NO
EMPIRICAL_SUPPORT = NONE
```
