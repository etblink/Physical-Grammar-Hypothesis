# PGH-0 Context/Record Semantic Anchor 0.1.0

## Identity

```text
OBJECT = CONTEXT_RECORD_SEMANTIC_ANCHOR_SCHEMA
OPERATION_ID = PGH0_MINIMAL_PHYSICAL_SEMANTIC_ANCHOR_CHALLENGE
STATUS = PROVISIONAL_FORMALLY_FEASIBLE
PHYSICAL_REALIZATION = UNESTABLISHED
NOVELTY_CLAIM = NONE
```

## Schema

Let a candidate grammar expose:

- a set or class `X` of candidate structures;
- a set or class `T` of terminal/output labels;
- an evaluator/response rule `e` defined on suitable context-structure pairs.

A context/record semantic anchor is:

\[
A=(C,R,\rho),
\]

where:

- `C` is a selected family of formal one-hole contexts interpreted as physical probe/interface types;
- `R` is a record-label space;
- `rho:T_R→R` is a partial interpretation of designated terminal labels `T_R subseteq T` as records.

The anchor excludes the evaluator `e` itself.

## Record profile

For `x in X`, define where all required maps are defined:

\[
O_{A,e}(x):C\to R,
\]

\[
O_{A,e}(x)(c)=\rho(e(c,x)).
\]

The induced anchor-relative equivalence is:

\[
x\sim_{A,e}y
\iff
\forall c\in C:\ O_{A,e}(x)(c)=O_{A,e}(y)(c).
\]

Partial-response variants may restrict the comparison to jointly defined contexts, but no such convention is physically selected in this artifact.

## Semantic/formal separation

The anchor contains:

```text
INTERFACE_TYPES
RECORD_TYPES
TERMINAL_TO_RECORD_INTERPRETATION
```

It does not contain:

```text
CONTEXT_STATE_RESPONSE_TABLE
DYNAMICAL_EQUATIONS
TRANSITION_PROBABILITIES
COMPLETE_POSSIBILITY_SET
TARGET_EQUIVALENCE_CLASSES
```

Therefore the architecture separates **what counts as a probe/record interface** from **what response the candidate grammar produces**.

## Reusability condition

The same anchor can be shared by multiple candidate grammars/evaluators provided each exposes compatible interface and terminal maps into the declared `C` and `R` structure.

This is an interface compatibility requirement, not a claim that arbitrary theories naturally share such an interface.

## Physical interpretation burden

A later physical realization must independently justify:

1. why the chosen contexts correspond to physically meaningful probes/interfaces;
2. why the selected outputs correspond to records;
3. why the record map is stable across faithful mathematical reformulation;
4. whether equality of complete record profiles is sufficient for the intended notion of physical equivalence;
5. whether inaccessible/internal physical structure can matter despite record equivalence.

None of these is settled here.

## No-smuggling boundary

A candidate implementation fails this schema's intended role if the anchor is enlarged to include the response map itself or a complete table of possible/impossible outcomes.

The schema is designed so that:

\[
A\quad\text{fixed},\qquad e_1\neq e_2
\]

can yield different record profiles.

That separation is demonstrated in `PGH-DER-0007`.

## Current status

```text
FORMAL_FEASIBILITY = PASS
PHYSICAL_PRIVILEGE = UNESTABLISHED
REPRESENTATION_ROBUSTNESS = UNTESTED
EMPIRICAL_REALIZATION = NONE
R1_COMPLETE = NO
R2_RELEVANCE = DEFERRED
```
