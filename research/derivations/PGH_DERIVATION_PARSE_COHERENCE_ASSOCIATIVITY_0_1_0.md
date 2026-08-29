# PGH-DER-0003 — Parse Coherence Implies Associativity 0.1.0

## Identity

```text
DERIVATION_ID = PGH-DER-0003
OPERATION_ID = PGH0_NONARBITRARY_FORMATION_CONSTRAINT_CHALLENGE
STATUS = QUALIFIED_CONDITIONAL_FORMAL
CLAIM_SCOPE = TOTAL_DETERMINISTIC_BINARY_FORMATION_REPRESENTATION
PHYSICAL_CLAIM = NONE
```

## Conditional claim

Let a formation representation use a total binary operation

\[
\star:A\times A\to A.
\]

If the two binary parse trees for every three-term composite are declared grammar-internally equivalent in the sense that they must produce the same result label,

\[
((a\star b)\star c)
\sim
(a\star(b\star c)),
\]

then `star` must be associative:

\[
(a\star b)\star c=a\star(b\star c)
\]

for all `a,b,c`.

This is a theorem **conditional on parenthesization-independence**. The theorem does not establish that the premise is a fundamental law.

## Proof

Under the declared representation, the grammar-internal result of the left parse tree is `(a star b) star c` and the result of the right parse tree is `a star (b star c)`.

The coherence premise requires equality of those results for every triple. That equation is exactly associativity. QED.

## Finite exclusion witness

For a two-element carrier there are

\[
2^{2\cdot2}=16
\]

total binary operations.

Exhaustive enumeration gives:

```text
ASSOCIATIVE_OPERATIONS = 8
NONASSOCIATIVE_OPERATIONS = 8
```

Thus the conditional coherence rule has real nonuniversal exclusion power.

## Explicit nonassociative operation

```text
* | 0 1
--+----
0 | 0 0
1 | 1 0
```

For `a=1`, `b=0`, `c=1`:

```text
(1*0)*1 = 1*1 = 0
1*(0*1) = 1*0 = 1
```

so the two parses disagree.

## Explicit associative operation

XOR on `{0,1}`:

```text
* | 0 1
--+----
0 | 0 1
1 | 1 0
```

satisfies associativity and therefore the stated three-term parse-coherence condition.

## Why the theorem does not solve PGH-Q-0011

The logical implication is exact, but the premise remains unearned.

A parse tree can carry genuine grammatical structure. Declaring parenthesization irrelevant is an additional equivalence principle.

At current PGH scope, representation independence establishes only that arbitrary *labels* should not matter. It does not yet establish that arbitrary *decompositions* or *bracketings* are semantically irrelevant.

Therefore:

```text
FORMAL_EXCLUSION = YES
CONDITIONAL_INDEPENDENT_CONSEQUENCE = YES
COHERENCE_PREMISE_JUSTIFIED_FROM_EXISTING_PGH_COMMITMENTS = NO
NONARBITRARY_FORMATION_LAW_FOUND = NO
```

## General lesson

This derivation identifies a possible mechanism:

\[
\text{representation equivalence}
\Longrightarrow
\text{coherence equation}
\Longrightarrow
\text{excluded formation tables}.
\]

The unresolved scientific burden moves to the first arrow: which representation differences may be identified without encoding the desired equation by hand?

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = TOTAL_DETERMINISTIC_BINARY_OPERATION
RULE_DEPENDENCIES = PARENTHESIZATION_INDEPENDENCE
LEMMA_DEPENDENCIES = NONE
SEMANTIC_ASSUMPTIONS = EQUALITY_OF_BINARY_RESULTS_IS_THE_DECLARED_PARSE_EQUIVALENCE_TEST
PHYSICAL_ASSUMPTIONS = NONE
SOURCE_DEPENDENCIES = NONE
METALANGUAGE_DEPENDENCIES = FUNCTIONS; EQUALITY; FINITE_ENUMERATION_FOR_WITNESS
```

## Result

```text
PGH-DER-0003 = QUALIFIED_CONDITIONAL_FORMAL
PARSE_COHERENCE_IMPLIES_ASSOCIATIVITY = YES
ASSOCIATIVITY_IS_FUNDAMENTAL = NOT_ESTABLISHED
ASSOCIATIVITY_IS_PHYSICAL = NO
```
