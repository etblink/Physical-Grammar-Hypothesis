# PGH-1 Primitive Bridge Internalization Admissibility Standard 0.1.0

## Status

```text
OBJECT_ID = PGH-OBJ-0027
OBJECT_CLASS = BRIDGE_CANDIDATE_ADMISSIBILITY_STANDARD
STATUS = QUALIFIED_FORMAL_STANDARD
PHYSICAL_STATUS = NONE
R2B = UNSATISFIED
```

## Purpose

Define when an anchor-to-grammar internalization may enter **formal bridge candidacy** without either demanding an infinite meta-derivation or allowing a response law to be hidden in the bridge signature.

This standard is analogous in role to the primitive grammar admissibility standard `PGH-OBJ-0020`.

It does not make any admitted bridge physically correct.

## Required criteria

A primitive bridge/internalization `I` may enter formal candidacy only if:

```text
P0_EXPLICIT_PREREGISTRATION = PASS
P1_PRE_TARGET_FIXATION = PASS
P2_RESPONSE_UNDERDETERMINATION = PASS
P3_COMPONENT_EDGE_EQUIVALENT_ENCODING = PASS_ONLY_IF_NO
P4_NONTRIVIAL_CROSS_TYPE_FORMAL_STRUCTURE = PASS
P5_REPRESENTATION_COVARIANCE = PASS_OR_TESTABLE
P6_GRAMMAR_DOCTRINE_DEPENDENCE = DECLARED
P7_COUNTEREXAMPLE_EXPOSURE = PASS
P8_MORPHISM_AS_PHYSICAL_RESPONSE = NOT_ASSUMED
P9_EMPIRICAL_FIT_USED_TO_CHOOSE_I = NO
```

Hard failures of P1, P2, P3, P8, or P9 block candidacy.

## Meaning of response underdetermination

The same bridge/internalization and typed anchor must remain compatible with at least two incompatible response laws while held fixed.

A bridge that determines the response support/function by its formal content fails this criterion.

## Edge-equivalent encoding test

Surface compactness receives no credit.

If an internalization is naturally information-equivalent to the component context-record edge family it later appears to generate, it fails P3.

The product control is canonical:

\[
Hom(X,\prod_iY_i)\cong\prod_iHom(X,Y_i).
\]

Thus one arrow into a product is not less response-edge information than the corresponding tuple of component arrows.

## Aggregate-process possibility

A generic process into an aggregate output object may pass P3 if its universal property does not identify it with component response arrows and if explicit models demonstrate that component arrows remain unforced.

Passing P3 does not establish that the process is physically meaningful.

## Primitive stopping rule

A bridge candidate need not be derived from a deeper bridge principle merely because it is primitive.

Its explanatory burden is instead exposed through:

- preregistration;
- non-encoding controls;
- response underdetermination;
- representation transport;
- declared doctrine dependence;
- downstream independent consequences;
- countermodels and empirical failure exposure at later stages.

## Candidate versus physical bridge

```text
FORMAL_BRIDGE_CANDIDATE = MAY_BE_ADMITTED_BY_THIS_STANDARD
PHYSICAL_BRIDGE = REQUIRES_SEPARATE_SEMANTIC_AND_EMPIRICAL_ADJUDICATION
R2B_SUCCESS = REQUIRES_SUBSTANTIVE_PHYSICAL_LAW_EXHAUSTION
```

No candidate passes R2B merely by satisfying this standard.