# PGH-1 Compositional Doctrine Selection Map 0.1.0

## Status

```text
OBJECT_ID = PGH-OBJ-0019
OBJECT_CLASS = DOCTRINE_SELECTION_MAP
PHYSICAL_STATUS = NONE
SUCCESSOR_GRAMMAR = NONE
```

## Candidate selectors

| Selector | Result | Reason |
|---|---|---|
| Bare compositional entailment | Fail | weaker monoidal axioms have models with different stronger doctrines |
| Opposition/duality-invariant form | Fail as unique cartesian-vs-cocartesian selector | duality exchanges product and coproduct doctrines |
| Common core / minimality | Too weak | removes doctrine-specific maps needed for nontrivial `Theta` |
| Maximal structural closure | Unfixed / overpermissive | no non-result-directed maximality ordering is supplied |
| Universal-property status | Nonunique | multiple and dual doctrines are universal-property based |
| Representation invariance | Nonselective | several competing doctrines are invariantly formulable |
| Empirical fit | Deferred | legitimate later testing, not grammar-internal origin |

## Current architecture

\[
M+D\longrightarrow\Theta_D\longrightarrow L(\Theta_D)\longrightarrow P.
\]

The arrow `D -> Theta_D` has conditional formal support.

The origin of `D` is underdetermined at current scope.

## Crucial methodological distinction

```text
DOCTRINE_NOT_DERIVED = TRUE_AT_CURRENT_SCOPE
DOCTRINE_THEREFORE_ILLEGITIMATE_AS_PRIMITIVE_HYPOTHESIS = NOT_ESTABLISHED
```

The project must now decide its stopping rule for primitive grammatical postulates before introducing another meta-layer.

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = [COMPOSITIONAL_STRUCTURE]
RULE_DEPENDENCIES = [CANDIDATE_DOCTRINE_SELECTOR]
SEMANTIC_ASSUMPTIONS = NONE
PHYSICAL_ASSUMPTIONS = NONE
```
