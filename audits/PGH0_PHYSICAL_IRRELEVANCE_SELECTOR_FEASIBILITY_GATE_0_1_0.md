# PGH-0 Physical Irrelevance Selector Feasibility Gate 0.1.0

## Identity

```text
OPERATION_ID = PGH0_PHYSICAL_IRRELEVANCE_SELECTOR_FEASIBILITY_GATE
REGISTRY_ID = PGH-OP-0013
CANONICAL_BASE = a3b80ffab9f2d6a07ba11f1107e65f926104b893
PREREGISTRATION_COMMIT = 79c5c114039e749a0ff3c26668e5b0d8a3b11aa9
FROZEN_SOURCE_COUNT = 37
NEW_SOURCE_SEARCH = NONE
PHYSICAL_GRAMMAR_SELECTION = NONE
EMPIRICAL_ADJUDICATION = NONE
FCP_EFFECT = NONE
```

## Outcome

```text
OUTCOME = C__NO_FROZEN_FORMAL_SELECTOR_PASSES_AND_R1_REQUIRES_A_MINIMAL_PHYSICAL_SEMANTIC_ANCHOR
R1_SOLVED = NO
R1_PURELY_FORMAL_ROUTE = FAIL_AT_CURRENT_SCOPE
SPECIFIC_SOURCE_GAP = NONE
SOURCE_EXPANSION_JUSTIFIED = NO
PHYSICAL_GRAMMAR_FOUND = NO
```

None of the seven frozen equivalence/translation families satisfies all six R1 acceptance criteria.

The gate does **not** establish that R1 is impossible. It establishes a narrower result:

> Formal equivalence alone does not determine physical equivalence. Some physically meaningful semantic anchor is required to connect a mathematical presentation equivalence to physical irrelevance.

That anchor remains unidentified and must itself satisfy PGH's no-smuggling discipline.

---

## 1. Generic formal result

Let `P` be a presentation space and let `E` be any nontrivial formal equivalence relation on `P`.

Suppose `p E p'` with `p != p'`.

Let physical significance be represented abstractly by a map

\[
\sigma:P\to S.
\]

If no independent restriction on admissible `sigma` has been supplied, formal facts about `E` do not entail

\[
p E p' \Longrightarrow \sigma(p)=\sigma(p').
\]

For example choose `S={0,1}`.

One admissible map at purely formal scope is

\[
\sigma_{same}(x)=0
\]

for every `x`.

Another is a map with

\[
\sigma_{split}(p)=0,\qquad \sigma_{split}(p')=1.
\]

Both are functions on the same formal presentation space. Therefore `E` alone cannot determine whether the pair is physically identical or physically distinct.

The result is elementary and carries no novelty claim.

It exposes the exact missing premise:

```text
A_RESTRICTION_ON_PHYSICAL_SIGNIFICANCE_MAPS_IS_REQUIRED
```

The scientific problem becomes whether such a restriction can be weak and independent enough not to contain the substantive physical laws PGH aims to explain.

---

## 2. Selector-family audit

Pass requires all of:

```text
R1A = NON_RESULT_DIRECTED
R1B = REPRESENTATION_ROBUST
R1C = DISCRIMINATES_COMPETING_EQUIVALENCES
R1D = NOT_DEFINED_AS_WHATEVER_PRESERVES_TARGET_PHYSICS
R1E = NO_HIDDEN_PHYSICAL_LAW
R1F = APPLICABLE_BEFORE_A_FULL_PHYSICAL_THEORY_IS_ALREADY_FIXED
```

### S1 — Definitional / syntactic equivalence

Frozen neighborhood: Barrett–Halvorson and Weatherall theory-equivalence sources.

```text
R1A = PASS_AT_FORMAL_SCOPE
R1B = FAIL
R1C = PARTIAL
R1D = PASS_AT_FORMAL_SCOPE
R1E = PASS_AT_FORMAL_SCOPE
R1F = PASS_AT_FORMAL_SCOPE
OVERALL = FAIL
```

Definitional or syntactic equivalence can be precisely stated without consulting target predictions, but it remains tied to chosen languages/signatures and is too formal-language-specific to establish physical irrelevance across genuinely different formulations.

It can certify one kind of formal sameness; it cannot by itself explain why that sameness is physical sameness.

### S2 — Categorical equivalence

Frozen neighborhood: Weatherall plus categorical/structural sources.

```text
R1A = PARTIAL
R1B = PARTIAL_PASS
R1C = PARTIAL
R1D = PARTIAL
R1E = FAIL
R1F = FAIL
OVERALL = FAIL
```

Categorical equivalence can ignore substantial presentation detail and compare structures via objects and morphisms. But the choice of category—especially which morphisms count as structure-preserving—is itself substantive.

If physically relevant structure is encoded in the category construction, categorical equivalence does not independently select that structure; it presupposes it.

### S3 — Morita equivalence

Frozen neighborhood: Barrett–Halvorson.

```text
R1A = PASS_AT_FORMAL_SCOPE
R1B = PARTIAL_PASS
R1C = PASS_WITHIN_LOGICAL_SCOPE
R1D = PASS_AT_FORMAL_SCOPE
R1E = PASS_AT_FORMAL_SCOPE
R1F = PASS_AT_FORMAL_SCOPE
OVERALL = FAIL_FOR_PHYSICAL_SELECTOR
```

Morita equivalence improves on strict definitional equivalence by allowing richer sorts/extensions while preserving appropriate theoretical content.

But the gate's target is not merely a robust formal criterion. Nothing in Morita equivalence alone entails that the preserved content is exactly the physically relevant content.

The generic formal-under\-determination result still applies.

### S4 — Duality / common-core equivalence

Frozen neighborhood: De Haro–Butterfield plus theory-equivalence sources.

```text
R1A = PARTIAL
R1B = PASS_WITHIN_DECLARED_DUALITY
R1C = PASS_WITHIN_CASE
R1D = PARTIAL
R1E = FAIL
R1F = FAIL
OVERALL = FAIL
```

A common-core strategy is highly relevant to PGH's aspiration that different surface formulations share invariant content.

But identifying the correct common core already requires a judgment about which structures are representational surplus and which are physical content.

Thus common-core machinery organizes a selector once supplied; it does not generically derive the selector.

### S5 — Structural / isomorphic / univalent equivalence

Frozen neighborhood: structural realism, mathematical structuralism, invariance, univalence.

```text
R1A = PASS_ONCE_STRUCTURE_IS_FIXED
R1B = PASS_ONCE_STRUCTURE_IS_FIXED
R1C = FAIL_GENERICALLY
R1D = PASS_AT_FORMAL_SCOPE
R1E = FAIL
R1F = FAIL
OVERALL = FAIL
```

Identity up to isomorphism/equivalence is powerful once the relevant structure is specified.

But the physical question is precisely **which structure** must be preserved. Choosing that structure is not supplied by the abstract injunction to respect isomorphism.

The selector problem therefore moves one level up rather than disappearing.

### S6 — Operational / empirical equivalence

Frozen neighborhood: process/CQM, operational reconstructions, Weatherall surveys.

```text
R1A = PARTIAL
R1B = PASS_OR_PARTIAL
R1C = PARTIAL
R1D = FAIL
R1E = FAIL
R1F = FAIL
OVERALL = FAIL
```

Operational/empirical equivalence is physically motivated, but the relevant observables, interventions, outcomes, or operational procedures must already be identified.

If the selector is simply “presentations are physically equivalent when all physically meaningful observations agree,” then “physically meaningful” carries the unresolved semantics.

Moreover empirical equivalence can be weaker than theoretical/ontological equivalence.

So operational equivalence is a promising **semantic anchor family**, not a completed R1 selector.

### S7 — Task / possibility equivalence

Frozen neighborhood: constructor theory.

```text
R1A = PARTIAL
R1B = PASS_WITHIN_TASK_FORMULATION
R1C = PARTIAL_PASS
R1D = FAIL
R1E = FAIL
R1F = FAIL
OVERALL = FAIL
```

Defining equivalence by agreement on possible/impossible transformations has direct physical meaning.

But for PGH this risks importing exactly the target possibility structure that the grammar is supposed to explain. If the task-possibility set is already fixed, the selector may inherit the substantive physical law rather than derive it.

Constructor-theoretic possibility structure is therefore a nearby control, not an automatic PGH solution.

---

## 3. Cross-family conclusion

The seven families fail for two different reasons.

### Purely formal families

```text
S1_DEFINITIONAL
S3_MORITA
S5_STRUCTURAL_FORMAL_SIDE
```

can often satisfy non-result-directedness and mathematical precision, but they do not establish that their preserved structure is **physical** structure.

### Physically interpreted families

```text
S2_CATEGORY_AS_PHYSICAL_MODELS
S4_COMMON_CORE
S6_OPERATIONAL_EMPIRICAL
S7_TASK_POSSIBILITY
```

can track physically meaningful content, but only after substantive choices about physical models, morphisms, observables, interpretation, common core, or possibility structure have entered.

Thus the project faces a genuine middle-layer problem:

\[
\text{formal equivalence}
\quad\not\Rightarrow\quad
\text{physical irrelevance}
\]

without some physical semantic constraint.

---

## 4. Why no hybrid selector is accepted

The preregistration forbids post hoc rescue by combining criteria until the desired result appears.

A natural hybrid might require both structural intertranslatability and operational equivalence. But that still presupposes:

1. which structural features belong in the translation;
2. which operations/observables count as physically meaningful.

No frozen, independently justified rule fixes both.

Therefore:

```text
AD_HOC_HYBRID_SELECTOR = NOT_ACCEPTED
```

This does not preclude a future principled conjunction if it is preregistered and independently motivated.

---

## 5. R1 consequence

R1 is not solved by the frozen formal-equivalence families.

However:

```text
R1_IMPOSSIBLE = NOT_ESTABLISHED
R1_REQUIRES_MINIMAL_PHYSICAL_SEMANTIC_ANCHOR = YES
```

The necessary next object is **not** another equivalence formalism. It is a minimal physical semantic anchor that can constrain admissible physical-significance maps `sigma` without already encoding the target physical law set.

This returns the project to an older live burden in sharpened form:

```text
PGH-Q-0007 = WHAT_SEMANTICS_MAP_IS_WEAK_ENOUGH_NOT_TO_CARRY_THE_PHYSICS_ITSELF
```

The question is now no longer generic. It is the immediate continuation of R1.

---

## 6. Minimal semantic-anchor requirements exposed by the gate

A candidate anchor `A_phys` must be weaker than a full physical theory yet strong enough to make some formal differences physically meaningful or meaningless.

Minimum requirements:

```text
A1_NOT_FULL_LAW_SET
A2_NOT_DEFINED_BY_TARGET_EQUIVALENCE
A3_SUPPORTS_PHYSICAL_DISTINGUISHABILITY_JUDGMENTS
A4_SURVIVES_MULTIPLE_MATHEMATICAL_PRESENTATIONS
A5_DOES_NOT_ENCODE_DESIRED_DYNAMICS_OR_SELECTION_RULES
A6_EXPOSES_FAILURE_CONDITIONS
```

Examples worth testing later include observational records, intervention interfaces, event correlations, or task interfaces, but none is selected here.

---

## 7. Source-gap decision

The gate failure is not caused by an identified missing theorem or absent source lane.

It is caused by a conceptual distinction shared across the frozen landscape: formal equivalence criteria and physical interpretation are not the same thing.

Therefore:

```text
SPECIFIC_SOURCE_GAP = NONE
SOURCE_EXPANSION_JUSTIFIED = NO
```

A later semantic-anchor challenge may expose a more targeted source need.

---

## 8. Effect on residual strong PGH

`PGH-OBJ-0008` remains live but is narrowed operationally.

```text
R1_PURELY_FORMAL_SELECTOR_ROUTE = FAILED_AT_CURRENT_SCOPE
R1_SEMANTIC_ANCHOR_ROUTE = OPEN
R2_LAW_EXHAUSTION = DEFERRED
```

Strong PGH is not helped by simply choosing the strongest available formal equivalence. Doing so would confuse mathematical invariance with physical irrelevance.

---

## 9. Next sequencing

Recommended next operation:

```text
NEXT_RECOMMENDED_OPERATION = PGH0_MINIMAL_PHYSICAL_SEMANTIC_ANCHOR_CHALLENGE
NEXT_OPERATION_AUTHORIZED = NO
```

The challenge should test whether any deliberately weak physical anchor can constrain `sigma` enough to make R1 nonvacuous while remaining too weak to contain the substantive laws or possibility structure that R2 eventually asks the grammar to explain.

It should begin with the frozen operational, theory-equivalence, process, constructor, and laws-as-constraints sources. No new source search should occur unless a specific semantic-anchor gap is demonstrated.

---

## 10. Final boundary

```text
R1_SOLVED = NO
R1_PURE_FORMAL_ROUTE = FAIL
MINIMAL_PHYSICAL_SEMANTIC_ANCHOR_REQUIRED = YES
SEMANTIC_ANCHOR_FOUND = NO
R2_STARTED = NO
PHYSICAL_GRAMMAR_FOUND = NO
PHYSICAL_LAW_DERIVED = NO
EMPIRICAL_WORK = NONE
FCP_EFFECT = NONE
```
