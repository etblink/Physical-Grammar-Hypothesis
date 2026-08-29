# PGH-1 Post-Kp Physical Scope / Domain-Selection Gate 0.1.0

## Identity

```text
OPERATION_ID = PGH1_POST_KP_PHYSICAL_SCOPE_DOMAIN_SELECTION_GATE
REGISTRY_ID = PGH-OP-0068
CANONICAL_BASE = d3b4a7e0d98e94e60fbff72cbb3a8c95e31fbde8
PREREGISTRATION_COMMIT = d1ae222f6df6ab541800f9b572e5abaf4e3037db
FIRST_EMPIRICAL_TARGET = PGH-OBJ-0037
FIRST_EMPIRICAL_FAILURE = PGH-FAIL-0035
TESTED_GRAMMAR = PGH-GRAM-0008
SEMANTIC_BRIDGE = PGH-OBJ-0035
SCOPE_SCHEMA = PGH-OBJ-0038
NEW_FAILURE = PGH-FAIL-0036
NEW_EMPIRICAL_DATA = NONE
NEW_TARGET_SEARCH = NONE
NEW_SOURCE_SEARCH = NONE
FCP_EFFECT = NONE
```

## Outcome

```text
OUTCOME = C__NO_PRE_KP_PHYSICAL_SCOPE_SELECTOR_QUALIFIES__THE_EXISTING_CANDIDATE_IS_PHYSICALLY_SCOPE_UNDERDETERMINED__THE_KP_FAILURE_REMAINS_FOR_THE_FROZEN_INSTANTIATION__ANY_NEW_SCOPE_RULE_IS_A_POST_KP_HYPOTHESIS_REVISION

PRE_KP_SCOPE_SELECTOR = NONE_QUALIFIED
KP_INSTANTIATION = REFUTED_AT_KP_TARGET
KP_TARGET_VALIDITY = RETAINED
PGH_GRAM_0008_FORMAL_STATUS = RETAINED
PGH_GRAM_0008_PHYSICAL_VALIDATION = NONE
UNCHANGED_CANDIDATE_SECOND_TARGET_PREDICTIVE_CREDIT = BLOCKED_PENDING_NON_RESULT_DIRECTED_SCOPE_OR_NEW_CANDIDATE_IDENTITY
R2B = UNSATISFIED
STRONG_PGH_CONFIRMED = NO
EVERY_POSSIBLE_PGH_REFUTED = NO
FCP_EFFECT = NONE
```

## Executive result

The pre-result PGH record contains a formally selective grammar, a conditional empirical realization schema, and a nonleaking procedure for choosing the first empirical test opportunity.

It does **not** contain a physical domain predicate stating which real systems are governed by `PGH-GRAM-0008` and which are not.

That distinction becomes controlling only because the first valid prospectively selected target failed. The project may not now manufacture a domain restriction from that failure and treat the restriction as if it had always belonged to the candidate.

The Kp target remains a valid frozen instantiation and remains refuted.

## Q1 — what was actually fixed before Kp?

Before Kp values were analyzed, the following were fixed:

```text
FORMAL_GRAMMAR = PGH-GRAM-0008
FORMAL_WIRING = A_TO_B_TO_C
FORMAL_RESTRICTION = A_INDEPENDENT_OF_C_GIVEN_B
SEMANTIC_BRIDGE = FULL_MODEL_CLASS_REALIZATION
TARGET_SELECTION_PROTOCOL = PGH-OBJ-0036
FIRST_TARGET = PGH-OBJ-0037
STATISTICAL_TEST = PREREGISTERED
```

What was **not** fixed was a physical-domain predicate of the form

```text
SYSTEM_X_IS_IN_SCOPE_IFF_PHYSICAL_PROPERTY_S(X)
```

for `PGH-GRAM-0008`.

The grammar artifact itself carried `PHYSICAL_STATUS = NONE`, and its variables/arrows had no physical assignment.

## Q2 — what classified Kp as a valid test opportunity?

`PGH-OBJ-0036` supplied a prospective metadata/architecture protocol for the **first empirical target**.

Its criteria concern:

- physical record status;
- objective ordered three-role architecture;
- finite alphabet or precommitted discretization;
- event-level access;
- support;
- missingness/selection documentation;
- reproducibility and archival properties;
- contamination control.

Kp passed those criteria and was frozen before the target dependence was inspected.

Therefore:

```text
KP_TEST_OPPORTUNITY = VALID
KP_SELECTION_WAS_RESULT_DIRECTED = NO
```

## Q3 — was the target-selection protocol a physical scope rule?

```text
NO
```

The protocol was explicitly designed to choose a nonleaking **first test target**. It did not state that all systems passing the metadata rubric are governed by the grammar, nor did it define a physical property that makes a system an instance of the grammar.

Treating the rubric retrospectively as a universal scope rule would add a stronger scientific claim that was not frozen before Kp.

Conversely, treating it as a rule that can be revised after each failed target would turn target selection into hidden hypothesis flexibility.

## Q4 — was any named physical domain fixed before Kp?

```text
NO
```

No pre-result artifact restricts `PGH-GRAM-0008` to a named sector such as geomagnetism, equilibrium systems, microscopic systems, causal chains of a particular physical type, or any other physical field/scale/process class.

The first-target discovery protocol deliberately searched across heterogeneous physical-record architectures. That procedure is inconsistent with claiming that a narrow named physical sector had already been part of the candidate identity.

## Q5 — could physical causal-chain membership supply the scope?

Not as a pre-existing qualified rule.

The physical-semantic firewall explicitly classified the stronger reading

```text
ARROWS_AS_PHYSICAL_CAUSES
```

as `NOT_REQUIRED_AND_NOT_QUALIFIED`.

The qualified bridge intentionally obtained falsifiability without causal ontology.

Therefore a post-Kp rule saying

> apply `PGH-GRAM-0008` only to systems independently known to realize the physical causal chain `A -> B -> C`

would add stronger semantic content than the candidate possessed before Kp.

Such a future hypothesis is not forbidden, but it is a **new candidate specification**, not a retrospective interpretation of the failed one.

## Q6 — can conditional-independence or Markov fit define the scope?

```text
NO__CIRCULAR
```

Rules such as

```text
IN_SCOPE_IFF_A_INDEPENDENT_OF_C_GIVEN_B
IN_SCOPE_IFF_FIRST_ORDER_MARKOV
IN_SCOPE_IFF_SPARSE_CHAIN_FIT_IS_GOOD
```

fail the preregistered S4/S5 controls. They use the predicted behavior, or a near-equivalent property, to decide whether the system is allowed to count as an instance.

This relocates empirical selectivity from the grammar into scope membership.

The failure is frozen as `PGH-FAIL-0036`.

## Q7 — does strong PGH force a universal reading of PGH-GRAM-0008?

```text
NO
```

`HYPOTHESIS.md` formulates strong PGH as the existence of some compact grammar `G` corresponding to physical possibility broadly.

But the project never identified `PGH-GRAM-0008` with that complete universal `G`.

Canonical artifacts consistently label `PGH-GRAM-0008` a **formal primitive grammar candidate** and deny it physical status.

Therefore the Kp failure cannot be promoted to a global refutation of strong PGH merely by identifying this small candidate with the final universal grammar after the fact.

The converse is equally important: strong PGH cannot supply a narrow domain exemption for `PGH-GRAM-0008` after Kp.

## Route adjudication

### R0 — no physical scope beyond formal model class

```text
RESULT = ACCURATE_DESCRIPTION_OF_PRE_KP_STATE
SCIENTIFIC_LIMITATION = PHYSICAL_INSTANCE_MEMBERSHIP_UNDERDETERMINED
```

The grammar and bridge define what follows **if** a physical system is instantiated as the grammar model class, but they do not classify physical systems into that scope.

### R1 — empirical-architecture eligibility as scope

```text
RESULT = REJECT_AS_RETROACTIVE_SCOPE_PROMOTION
```

`PGH-OBJ-0036` remains a valid target-selection protocol. It is not promoted into a universal physical-domain law.

Kp passed it, so this route cannot remove Kp from the historical test without contradicting the frozen selection record.

### R2 — graph as physical causal/dependency scope

```text
RESULT = NOT_PRE_KP_QUALIFIED
```

Physical causal semantics were explicitly withheld. Adding them now would be hypothesis revision.

### R3 — named domain-specific physical sector

```text
RESULT = NONE_PRE_KP
```

No such sector was frozen.

### R4 — result-defined / Markov-fit scope

```text
RESULT = REJECT_CIRCULAR
```

This is direct post-result selector relocation.

### R5 — strong-PGH universal reading

```text
RESULT = DOES_NOT_IDENTIFY_PGH_GRAM_0008_WITH_FINAL_UNIVERSAL_GRAMMAR
```

The umbrella strong hypothesis remains open/unestablished; `PGH-GRAM-0008` was a bounded candidate, not the established universal grammar.

## Scope qualification table

| Criterion | Best pre-Kp candidate | Result |
|---|---|---|
| S1 pre-result provenance | metadata target-selection protocol | PASS as protocol, not scope |
| S2 no Kp dependence input | metadata target-selection protocol | PASS |
| S3 non-extensional physical scope | no candidate | FAIL |
| S4 not equivalent to predicted CI | metadata protocol | PASS |
| S5 not selected because it excludes Kp | metadata protocol | PASS |
| S6 physical/semantic scope interpretation without fit | no qualified domain predicate | FAIL |
| S7 classifies targets before analysis | metadata protocol | PASS as target selection |
| S8 does not import independent physical law | causal-scope proposal | FAIL / not previously qualified |

No single pre-result rule passes the scope standard as a physical-domain selector.

## Why outcome A does not pass

No pre-Kp physical scope rule exists that can be shown both to qualify and to include Kp.

Kp remains in the historical test because it was prospectively selected as a valid empirical instantiation, not because a broader physical scope rule has now been reconstructed.

## Why outcome B does not pass

No qualified pre-Kp scope rule exists to conflict with the Kp freeze.

The target-selection protocol and Kp freeze are internally consistent.

## Why outcome D does not pass

The umbrella strong hypothesis is broad, but no canonical artifact identifies `PGH-GRAM-0008` as the exhaustive universal grammar of physical possibility.

That identification cannot be added after the failure merely to increase the severity of the result.

## New preserved failure

```text
PGH-FAIL-0036 = POST_RESULT_PHYSICAL_SCOPE_SELECTION_RELOCATION
```

The failed move is to choose or narrow the physical domain of a candidate after an empirical failure and then treat the new domain predicate as though it had been part of the original candidate.

This is a scope-level version of the project's general selector-relocation problem.

## New schema

```text
PGH-OBJ-0038 = POST_KP_PHYSICAL_SCOPE_DOMAIN_SELECTION_SCHEMA
```

It separates:

```text
G = FORMAL_GRAMMAR_MODEL_CLASS
J = SEMANTIC_REALIZATION_SCHEMA
T = EMPIRICAL_TARGET_SELECTION_PROTOCOL
S = PHYSICAL_SCOPE_PREDICATE
```

`T` and `S` are not interchangeable.

For future cross-target predictive credit, a nontrivial `S` must either be part of the candidate identity before target outcomes are known or be explicitly introduced as a new post-failure hypothesis revision.

## Scientific consequence

The first Kp experiment did more than reject one instantiation. It exposed an auxiliary-freedom question that had not mattered while the candidate remained pre-empirical:

> What makes a physical system an intended instance of this grammar?

For the existing identity of `PGH-GRAM-0008`, that question was not answered before Kp.

Therefore immediately moving to C9, GOES, or another target under the unchanged candidate would not earn clean continuation credit. A successful second target could always be challenged as post-failure scope migration unless the scope problem is resolved prospectively.

## What this result does not say

```text
PGH_GRAM_0008_FORMAL_MATHEMATICS_IS_FALSE = NO
EVERY_PHYSICAL_INSTANTIATION_OF_PGH_GRAM_0008_IS_REFUTED = NO
STRONG_PGH_IS_GLOBALLY_REFUTED = NO
A_FUTURE_SCOPE_BEARING_CANDIDATE_IS_FORBIDDEN = NO
A_NAMED_DOMAIN_CAN_NEVER_BE_JUSTIFIED = NO
```

A future scope-bearing hypothesis may be scientifically legitimate. It must simply carry honest post-Kp provenance and receive a new/revised candidate identity before any new target is selected.

## Mandatory method consequence

Any future empirical Monte Carlo preregistration must also freeze:

```text
PRNG_ALGORITHM
WORD_TO_BOUNDED_INTEGER_MAPPING
UNIT_UNIFORM_MAPPING
SHUFFLE_ALGORITHM
CATEGORICAL_SAMPLER
QUANTILE_CONVENTION
SOFTWARE_OR_REFERENCE_IMPLEMENTATION_BINDING_AS_NEEDED
```

This requirement comes from the already canonical reproducibility limitation and is not a reinterpretation of the Kp result.

## Recommended next operation

```text
NEXT_RECOMMENDED_OPERATION = PGH1_POST_KP_CANDIDATE_DISPOSITION_AND_SUCCESSOR_ARCHITECTURE_SEQUENCING_GATE
NEXT_OPERATION_AUTHORIZED = NO
```

That gate should decide, without new empirical data or source search, whether the scientifically appropriate response is to:

1. retire unchanged `PGH-GRAM-0008` from further physical-target testing while retaining it as a formal control;
2. formulate a new explicitly scope-bearing successor candidate with post-Kp provenance; or
3. return to grammar/bridge architecture rather than continuing empirical target search.

It must stop before constructing or testing the successor itself.

## Hard-stop verification

```text
SECOND_TARGET_SEARCH = NO
NEW_EMPIRICAL_DATA = NONE
EXTERNAL_SOURCE_SEARCH = NONE
KP_TARGET_RECLASSIFIED_AS_INVALID = NO
KP_RESULT_REINTERPRETED = NO
GRAPH_REPAIRED = NO
NEW_PHYSICAL_SCOPE_ENGINEERED = NO
NEW_SCOPE_BACKDATED = NO
STRONG_PGH_GLOBAL_REFUTATION = NO
R2B_SATISFIED = NO
FCP_CHANGED = NO
```
