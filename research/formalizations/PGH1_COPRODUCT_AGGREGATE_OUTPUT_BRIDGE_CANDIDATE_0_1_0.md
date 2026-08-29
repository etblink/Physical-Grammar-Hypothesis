# PGH-1 Coproduct Aggregate-Output Bridge Candidate 0.1.0

## Status

```text
OBJECT_ID = PGH-OBJ-0028
OBJECT_CLASS = PRIMITIVE_BRIDGE_CANDIDATE
STATUS = FORMALLY_ADMITTED_BRIDGE_CANDIDATE
PHYSICAL_STATUS = NONE
R2B = UNSATISFIED
```

## Candidate definition

Let `T` be a response-underdetermining typed interface satisfying `PGH-OBJ-0025`.

For each context `c` with finite nonempty typed fiber

\[
R_c=\{r_1,\dots,r_n\},
\]

and for a candidate grammar supporting finite coproducts (`PGH-GRAM-0006` or `PGH-GRAM-0007`), define the aggregate typed output object

\[
O_c=\coprod_{r\in R_c}Y_r.
\]

Add exactly one primitive generic process

\[
n_c:X_c\to O_c.
\]

No component morphism

\[
X_c\to Y_r
\]

is primitive solely by this candidate definition.

## Candidate boundary

The candidate includes:

```text
TYPED_FIBER = FROM_PGH_OBJ_0025
COPRODUCT_AGGREGATE_OBJECT = YES
ONE_GENERIC_PROCESS_PER_CONTEXT = YES
COMPONENT_RESPONSE_EDGES = NO
PROBABILITY_OR_AMPLITUDE = NO
ALLOWED_RESPONSE_SUPPORT = NO
PHYSICAL_RESPONSE_MEANING = NO
```

## Why it is not a new grammar ID

The underlying compositional doctrine remains `PGH-GRAM-0006` or `PGH-GRAM-0007`.

This object records an explicit **bridge-enriched configuration** between the law-free typed anchor and those grammar candidates.

If later work adds substantive equations, response rules, or physical dynamics, a new scientific identity may be required.

## Response underdetermination

For a fiber containing at least two record labels, `PGH-DER-0023` guarantees multiple deterministic response sections of the same `T`.

`PGH-DER-0026` shows that the generic coproduct process does not force any one component arrow.

Therefore the bridge candidate does not itself determine which record response occurs.

## Representation covariance

Under a faithful relabeling of contexts and record labels, the typed fibers transport covariantly.

The finite coproduct of the transported record objects is canonically isomorphic to the transported aggregate object, up to the usual coproduct coherence/isomorphism.

The bridge presentation transports the generic process accordingly.

No fixed labeled ordering of the summands is treated as physical.

## Admissibility result

Under `PGH-OBJ-0027`:

```text
P0_EXPLICIT_PREREGISTRATION = PASS
P1_PRE_TARGET_FIXATION = PASS_AT_CURRENT_EXPERIMENTAL_SCOPE
P2_RESPONSE_UNDERDETERMINATION = PASS
P3_COMPONENT_EDGE_EQUIVALENT_ENCODING = PASS_NOT_EQUIVALENT
P4_NONTRIVIAL_CROSS_TYPE_FORMAL_STRUCTURE = PASS
P5_REPRESENTATION_COVARIANCE = PASS_CONDITIONALLY
P6_GRAMMAR_DOCTRINE_DEPENDENCE = DECLARED_COPRODUCT_REQUIRED
P7_COUNTEREXAMPLE_EXPOSURE = PASS
P8_MORPHISM_AS_PHYSICAL_RESPONSE = NOT_ASSUMED
P9_EMPIRICAL_FIT_USED_TO_CHOOSE_I = NO
```

## Counterexample exposure

The candidate fails as a bridge to component-level response structure if later science requires the grammar alone to select one component record but no additional principled structure produces such a selection.

It also fails law-free status if `n_c` or membership in `T` is later reinterpreted as already encoding physical response possibility.

## Physical ceiling

```text
FORMAL_BRIDGE_CANDIDATE = YES
PHYSICAL_BRIDGE = NO
PHYSICAL_RESPONSE_LAW = NO
R2B = UNSATISFIED
EMPIRICAL_PREDICTION = NONE
```