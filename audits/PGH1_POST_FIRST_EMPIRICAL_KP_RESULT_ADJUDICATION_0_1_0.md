# PGH-1 Post-First-Empirical Kp Result Adjudication 0.1.0

## Identity

```text
OPERATION_ID = PGH1_POST_FIRST_EMPIRICAL_KP_RESULT_ADJUDICATION
REGISTRY_ID = PGH-OP-0066
CANONICAL_BASE = aa520a94fbd2817d020e4c1de8480ab2397a014f
EMPIRICAL_EXECUTION_COMMIT = fcaaa3202155a9f3af8f891f0b8389a1e10bfcfe
EXECUTION_QUALIFICATION_FINALIZATION = aa520a94fbd2817d020e4c1de8480ab2397a014f
TARGET = PGH-OBJ-0037
TARGET_ID = TGT-001
GRAMMAR = PGH-GRAM-0008
SEMANTIC_BRIDGE = PGH-OBJ-0035
FAILURE_RECORD = PGH-FAIL-0034
NEW_EMPIRICAL_DATA = NONE
NEW_SOURCE_SEARCH = NONE
NEW_TARGET_SELECTION = NONE
GRAMMAR_MODIFICATION = NONE
FCP_EFFECT = NONE
```

## Purpose

Adjudicate the exact scientific meaning of the first preregistered empirical failure only after that result is canonical.

This operation does not explain the geomagnetic mechanism behind the observed dependence, select a second target, refine the grammar, alter the semantic bridge, or grant convergence/confirmation credit.

## Canonical empirical fact

The frozen Kp instantiation tested

\[
\mathcal A\perp\mathcal C\mid\mathcal B
\]

on 91,557 preregistered non-overlapping triples of the native 28-state definitive GFZ Kp record.

The canonical execution records:

```text
G2_OBS = 8716.1945352372713
I_BITS_A_C_GIVEN_B = 0.068672032894318807
M = 0.020796039825599761
P_PERM = 0.0002__0_OF_4999
P_MARKOV = 0.0005__0_OF_1999
PRIMARY_VERDICT = REFUTED_AT_KP_TARGET
```

The first and second chronological halves both retain nonzero conditional mutual information in the mandatory descriptive diagnostic. The phase-aware first-order Markov bootstrap is the stronger preregistered adversarial control because its null distribution lies substantially closer to the observed statistic than the conditional-permutation null, yet both the predecessor first execution and the successor independent reconstruction report zero bootstrap exceedances.

The effect-size ratio `M` is descriptive only. Statistical rejection is not promoted to a claim that the residual dependence is large in physical importance.

## Adjudication question A — did the formal theorem fail?

```text
FORMAL_THEOREM_PGH_DER_0029 = SURVIVES
```

No.

`PGH-DER-0029` is a theorem about the model class defined by the factorization

\[
p(a,b,c)=p(a)p(b\mid a)p(c\mid b).
\]

Every distribution in that model class still satisfies `A independent of C given B`.

The Kp empirical distribution being incompatible with the transferred restriction does not provide a counterexample to the theorem; it provides evidence that the frozen empirical target is not adequately represented by that grammar model class under the frozen instantiation.

## Adjudication question B — did formal primitive-grammar candidacy fail?

```text
PGH_GRAM_0008_FORMAL_PRIMITIVE_GRAMMAR_CANDIDACY = SURVIVES
PHYSICAL_STATUS_FROM_FORMAL_CANDIDACY = NONE
```

No.

The formal candidacy gate admitted `PGH-GRAM-0008` because its fixed sparse wiring is non-extensional, compressive, representation-disciplined, and genuinely excludes finite joint distributions while leaving local kernels free.

Those formal properties are unchanged by the Kp result.

This does **not** preserve or create a claim that `PGH-GRAM-0008` is a physical grammar.

## Adjudication question C — what exactly failed physically?

```text
PGH_OBJ_0037_KP_EMPIRICAL_INSTANTIATION = REFUTED
FROZEN_KP_REALIZATION_OF_PGH_GRAM_0008 = FAILED
TARGET_DATASET_IDENTITY = STILL_VALID
TARGET_SELECTION_PROTOCOL_COMPLIANCE = UNAFFECTED
```

The prospectively selected Kp assignment was a valid empirical test opportunity under `PGH-OBJ-0036`. It then failed the grammar-derived restriction.

The failure is therefore not dismissed as an invalid target merely because the target disagreed with the candidate.

The frozen Kp instantiation receives no further PGH physical-success credit and may not be repaired by changing lag, phase, alphabet, subperiod, graph wiring, or calibration after the result.

## Adjudication question D — did the semantic bridge fail?

```text
PGH_OBJ_0035_AS_CONDITIONAL_TRANSFER_SCHEMA = SURVIVES
PGH_OBJ_0035_AS_EVIDENCE_THAT_KP_INSTANTIATES_THE_GRAMMAR = FAILS_FOR_KP
```

The bridge schema remains logically sound as a conditional full-model-class realization rule: if an empirical system is modeled by the grammar class under the declared role/alphabet realization, the grammar theorem transfers without semantic model selection.

The Kp result shows that the frozen Kp target does not satisfy that candidate restriction. It does not show that the transfer theorem itself is false.

This is precisely the falsification exposure the bridge was designed to create.

## Adjudication question E — is PGH-GRAM-0008 globally refuted as a physical grammar?

```text
GLOBAL_PHYSICAL_REFUTATION_OF_PGH_GRAM_0008 = NOT_ESTABLISHED
PHYSICAL_VALIDATION_OF_PGH_GRAM_0008 = NONE
```

No global refutation is licensed because no canonical artifact had established that every physical system, or every eligible three-record physical target, must instantiate this specific sparse chain grammar.

However, the first prospectively chosen empirical opportunity failed. That is adverse evidence against promoting this grammar from formal candidacy to physical status, and it may not be neutralized by immediately searching for a friendlier target.

A second target would require a new prospective scientific justification for domain/scope selection that does not use the Kp failure to choose where the grammar is allowed to apply.

## Adjudication question F — does strong PGH fail?

```text
STRONG_PGH_CONFIRMED = NO
STRONG_PGH_GLOBALLY_REFUTED_BY_THIS_RESULT = NO
R2B_SATISFIED = NO
PHYSICAL_GRAMMAR_CONFIRMED = NO
```

The failure concerns one formal grammar candidate under one prospectively selected empirical instantiation.

It does not logically exhaust the space of possible non-extensional, non-universal, representation-disciplined primitive grammars or semantic bridges.

Conversely, preserving that logical possibility earns no confirmation credit for strong PGH.

## Adjudication question G — may the graph be repaired from Kp?

```text
ADD_A_TO_C_EDGE_AFTER_KP = FORBIDDEN_AS_RESULT_DIRECTED_REPAIR
COMPLETE_DAG_PROMOTION = REJECT_AS_EMPIRICALLY_NONSELECTIVE_CONTROL
Kp_DRIVEN_GRAPH_SEARCH = FORBIDDEN
```

No.

The complete ordered DAG was already frozen as the universality control: it represents every finite joint distribution. Promoting it after the failure would remove the candidate's finite-joint exclusion power rather than explain the Kp result.

Any future graph or grammar candidate must be justified independently of the observed Kp dependence and separately preregistered before empirical confrontation.

## Adjudication question H — what does the Monte Carlo implementation defect mean?

```text
PRNG_AND_EXACT_SAMPLING_MAPPING_NOT_FROZEN = CONFIRMED_PREREGISTRATION_LIMITATION
NULL_DEFINITIONS = FROZEN
SEED_DERIVATION = FROZEN
PREDECESSOR_AND_SUCCESSOR_VERDICT = AGREES
RETROACTIVE_METHOD_REWRITE = FORBIDDEN
```

The preregistration fixed seed formulas but did not specify a PRNG and exact mapping from pseudorandom words to permutations/categorical draws. Therefore it did not uniquely determine bit-identical Monte Carlo arrays across implementations.

This limits exact computational reproducibility and must be repaired prospectively in future Monte Carlo preregistrations.

It does not authorize choosing among realizations by result. The predecessor first execution and a separately implemented successor reconstruction both produced the minimum attainable Monte Carlo p-values under both frozen null definitions and the same mechanical verdict.

The present result is therefore retained, with the limitation visible.

## Adjudication question I — what has actually been learned?

The first empirical confrontation demonstrated three things at distinct levels:

1. **Formal selectivity was real:** the grammar supplied a proper finite-joint restriction before the target was known.
2. **Semantic exposure was real:** the bridge transferred that restriction without fitting kernels or adding a response table.
3. **Empirical failure was real:** the first prospectively selected physical record did not satisfy the transferred restriction under either preregistered calibration.

The scientific value of the operation is therefore not that PGH survived. It did not survive this instantiation. The value is that the project reached a point where its grammar could lose and then preserved the loss.

## Domain-selection consequence

A new issue is now unavoidable:

```text
IF_PGH_GRAM_0008_IS_NOT_UNIVERSAL_OVER_ELIGIBLE_TARGETS
THEN_A_NON_RESULT_DIRECTED_PHYSICAL_SCOPE_SELECTOR_IS_REQUIRED
BEFORE_SECOND_TARGET_CREDIT_CAN_BE_INTERPRETED
```

Without such a scope rule, moving from a failed target to another physical domain risks relocating the law into post-result target choice.

This is not yet a new failure theorem and is not resolved in this adjudication. It is a sequencing constraint for whatever operation follows.

## Forbidden post-result moves inside this operation

```text
NO_SECOND_TARGET_SEARCH
NO_C9_SUBSTITUTION
NO_GOES_SUBSTITUTION
NO_KP_LAG_OR_PHASE_SEARCH
NO_KP_STATE_MERGING
NO_KP_SUBPERIOD_SELECTION
NO_GRAPH_EDGE_ADDITION
NO_MODEL_FAMILY_FIT_TO_KP
NO_PHYSICAL_CAUSAL_STORY_FROM_KP
NO_LITERATURE_SEARCH_FOR_A_POSTHOC_EXPLANATION
NO_STRONG_PGH_CONFIRMATION_OR_GLOBAL_REFUTATION
NO_FCP_EFFECT
```

## Outcome

```text
OUTCOME = K1__FROZEN_KP_INSTANTIATION_REFUTED__FORMAL_GRAMMAR_AND_TRANSFER_THEOREMS_REMAIN_VALID_AT_THEIR_DECLARED_LEVELS__NO_PHYSICAL_VALIDATION__NO_GLOBAL_PGH_REFUTATION__POST_RESULT_TARGET_OR_GRAPH_REPAIR_FORBIDDEN__DOMAIN_SCOPE_SELECTION_BURDEN_EXPOSED

KP_INSTANTIATION = REFUTED
PGH_GRAM_0008_FORMAL_STATUS = RETAINED
PGH_GRAM_0008_PHYSICAL_STATUS = NONE
PGH_OBJ_0035_CONDITIONAL_SCHEMA = RETAINED
R2B = UNSATISFIED
STRONG_PGH_CONFIRMED = NO
EVERY_POSSIBLE_PGH_REFUTED = NO
FCP_EFFECT = NONE
```

## Sequencing boundary

This adjudication intentionally does not choose the next substantive research operation.

Only after this adjudication is independently reviewed and canonically integrated should the Project Lead select among post-failure directions. Any such choice must account for the newly exposed domain/scope-selection burden and the need to fully specify future Monte Carlo RNG semantics prospectively.
