# PGH-OBJ-0035 — Causal Wiring Model-Class Physical Bridge Schema 0.1.0

## Status

```text
OBJECT_ID = PGH-OBJ-0035
STATUS = QUALIFIED_CONDITIONAL_SEMANTIC_BRIDGE_SCHEMA
PHYSICAL_STATUS = TESTABLE_IN_PRINCIPLE_ONLY
EMPIRICAL_TARGET = NONE
```

## Purpose

Provide the weakest response-relevant semantic realization of `PGH-GRAM-0008` that gives the grammar empirical testability without selecting local kernels or adding response restrictions through interpretation.

## Formal source

The source model class is

\[
W(PGH\text{-}GRAM\text{-}0008)
\]

consisting of finite normalized joint distributions satisfying the sparse Markov-chain factorization.

## Prospective empirical roles

Introduce three record-valued empirical variable roles

\[
\mathcal A,\mathcal B,\mathcal C
\]

with finite alphabets bijectively matched to the formal alphabets.

No actual physical variables are selected in this schema.

## Realization map

For each formal model `p`, `J(p)` is the corresponding candidate empirical joint-response distribution under the fixed variable/alphabet relabeling.

Admissibility requires:

```text
FULL_CLASS_REALIZATION = YES
PROPER_SUBSET_SELECTION = NO
LOCAL_KERNEL_SELECTION = NO
NEW_RESPONSE_EQUATIONS = NO
EMPIRICAL_FIT = NO
```

The bridge may change representation/meaning but not the model class's selective content.

## Transferred restriction

By `PGH-DER-0031`,

\[
A\perp C\mid B
\]

transports to

\[
\mathcal A\perp\mathcal C\mid\mathcal B.
\]

This restriction is conditional on a later valid empirical instantiation of the roles.

## Causal-ontology neutrality

The schema does not require interpreting graph arrows as physical causes.

Its empirical content is only model-class admissibility of joint response distributions.

Thus a causal ontology is neither endorsed nor needed for the first falsifiability test.

## Target-selection firewall

A concrete mapping from the roles to real observables must be separately preregistered before examining whether the target satisfies the predicted conditional independence.

Post-hoc role assignment receives no PGH credit.

## Claim ceiling

```text
PHYSICALLY_TESTABLE_IN_PRINCIPLE = YES
CANDIDATE_PHYSICAL_RESTRICTION = YES_CONDITIONAL
ACTUAL_PHYSICAL_INSTANTIATION = NONE
EMPIRICAL_VALIDATION = NONE
R2B = UNSATISFIED
```
