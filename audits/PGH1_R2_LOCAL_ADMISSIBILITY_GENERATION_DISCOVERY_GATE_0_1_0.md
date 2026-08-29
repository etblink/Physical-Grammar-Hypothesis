# PGH-1 R2 Local Admissibility Generation Discovery Gate — Adjudication 0.1.0

## Identity

```text
OPERATION_ID = PGH1_R2_LOCAL_ADMISSIBILITY_GENERATION_DISCOVERY_GATE
REGISTRY_ID = PGH-OP-0038
CANONICAL_BASE = fd928b754f15affbb461d9e4a8a9d78ba12bc5cd
PREREGISTRATION_COMMIT = f2731689e1643219abe817159302236048d81eff
WORKING_TARGET = PGH-OBJ-0012
FROZEN_ACCEPTED_SOURCE_COUNT = 51
NEW_SOURCE_SEARCH = NONE
FCP_EFFECT = NONE
```

## Outcome

```text
OUTCOME = B__FORMAL_SUPPORT_GENERATORS_EXIST_BUT_EVERY_TESTED_FAMILY_STILL_DEPENDS_ON_AN_UNEARNED_RULE_LANGUAGE_SIGNATURE_TYPE_SYSTEM_SYMMETRY_OR_COHERENCE_PREMISE
SUCCESSOR_GRAMMAR_SELECTED = NO
R2_SATISFIED = NO
PHYSICAL_LAW_DERIVED = NO
```

## Executive result

The prior gate located the local-to-global selective burden in proper local supports

\[
R_C\subsetneq D^C.
\]

This gate asks whether replacing explicit support tables by compact rule descriptions solves that burden.

It does not, by itself.

On finite domains every arbitrary support has an exact finite logical description using equality atoms. Therefore unrestricted local predicates/formulas are universal encoders of the same support information as tables.

Several restricted formal families can nevertheless generate proper supports non-enumeratively inside a fixed formal environment:

- equations in a fixed algebraic signature;
- grammar-derived typing/interface constraints;
- derivational coherence or rewrite consistency;
- invariance under a fixed symmetry action.

But the present project has not independently justified the signature, type system, rewrite/coherence structure, or symmetry action. Those inputs can still carry the selective content.

Empirical/operational supports are physically meaningful but fail the PGH R2 firewall when used as explanatory grammar because the local physical possibility structure has already been imported.

## U1 — finite local predicate universal encoding

Let `C` and `D` be finite and let arbitrary

\[
R\subseteq D^C.
\]

For each tuple `r in R`, define the conjunction

\[
\chi_r(x)=\bigwedge_{i\in C}(x_i=r_i).
\]

Then define

\[
\Phi_R(x)=\bigvee_{r\in R}\chi_r(x).
\]

For any `x in D^C`,

\[
\Phi_R(x)\text{ is true}\iff x=r\text{ for some }r\in R\iff x\in R.
\]

Thus every finite support is exactly the model set of some formula.

```text
UNRESTRICTED_LOCAL_FORMULA_LANGUAGE = UNIVERSAL_SUPPORT_ENCODER
FORMULA_DESCRIPTION_ALONE = NO_EXPLANATORY_CREDIT
```

This is recorded as `PGH-DER-0014`.

## U2 — compact-description control

Description length alone does not solve the problem unless the language in which length is measured is itself fixed independently.

A formal language may add one primitive symbol `P_R` interpreted as exactly the target support `R`. Then the support has a one-symbol description while remaining a lookup table semantically.

Therefore:

```text
SHORT_DESCRIPTION != GENERATED_NECESSITY
```

The relevant question is why the allowed rule language, primitives, and construction rules have the form they do.

## Family classification

### S0 — arbitrary support table

```text
PROPER_SUPPORT_POWER = YES
NON_TABLE_DRIVEN = NO
R2_PRIORITY = REJECT
```

Direct encoding control.

### S1 — unrestricted local predicate/formula

```text
PROPER_SUPPORT_POWER = YES
NON_TABLE_DRIVEN_IN_UNRESTRICTED_LANGUAGE = NO
UNIVERSAL_ENCODING = YES
R2_PRIORITY = REJECT_AS_EXPLANATORY_ENDPOINT
```

The representation changes; the support information need not.

### S2 — grammar-internal equational support

For a fixed independently supplied algebraic signature, equations can define proper subsets of local tuples without enumerating them. This has genuine compact generative potential.

But current PGH has no independently qualified successor signature/equational theory. Freely selecting equations because they produce desired restrictions is result-directed.

```text
PROPER_SUPPORT_POWER = YES
NON_TABLE_DRIVEN_IN_FIXED_LANGUAGE = YES
INDEPENDENT_LANGUAGE_ORIGIN = UNESTABLISHED
R2_EVALUATION_PRIORITY = B__PROMISING_CONDITIONAL
SOURCE_COVERAGE = STRONG__UNIVERSAL_ALGEBRA_AND_ALGEBRAIC_THEORIES
```

### S3 — typing/interface matching support

A fixed type system can forbid locally malformed tuples and can do so compositionally.

But deriving types from arbitrary entries of `PGH-GRAM-0002` inherits the baseline table failure; freely declaring a type system simply moves local admissibility into type declarations.

```text
PROPER_SUPPORT_POWER = YES
NON_TABLE_DRIVEN_IN_FIXED_TYPE_SYSTEM = YES
TYPE_SYSTEM_ORIGIN = UNESTABLISHED
R2_EVALUATION_PRIORITY = B__PROMISING_CONDITIONAL
```

### S4 — derivational coherence / rewrite consistency

A fixed rewrite/coherence architecture can exclude tuples or diagrams that fail confluence, normalization, or required commutation.

This is compact and non-table-driven once the rewrite system and equivalence structure are fixed. But PGH-0 already established that the relevant coherence premise is additional, and the frozen literature establishes mature prior art rather than physical privilege.

```text
PROPER_SUPPORT_POWER = YES
NON_TABLE_DRIVEN_IN_FIXED_REWRITE_SYSTEM = YES
COHERENCE_PREMISE_ORIGIN = UNESTABLISHED
PHYSICAL_BRIDGE = NONE
R2_EVALUATION_PRIORITY = B__PROMISING_CONDITIONAL
SOURCE_COVERAGE = STRONG
```

### S5 — symmetry/invariance-generated support

A fixed symmetry action can force admissible sets to be invariant and can rule out noninvariant local structures.

But a symmetry group/action chosen after the target support is known can encode the desired result, and invariance generally leaves many invariant subsets.

```text
PROPER_SUPPORT_POWER = CONDITIONAL
SYMMETRY_ACTION_ORIGIN = UNESTABLISHED
UNIQUE_SUPPORT_SELECTION = NO_GENERAL_RESULT
R2_EVALUATION_PRIORITY = C__CONTROL_OR_SECONDARY
```

### S6 — empirical/operational support

Observed response supports, probability-zero events, possible/impossible tasks, and reconstructed operational state spaces can be physically substantive and scientifically legitimate inputs to ordinary physics.

They cannot receive PGH R2 explanatory credit as grammar-generated local admissibility unless independently derived, because the physical possibility structure is already present.

```text
PHYSICAL_RELEVANCE = HIGH
PGH_NO_SMUGGLING = FAIL_IF_USED_AS_EXPLANATORY_ORIGIN
R2_EVALUATION_PRIORITY = REJECT_AS_GRAMMAR_ORIGIN
```

## Source-gap audit

The frozen corpus already covers the relevant comparison families at representative scope:

```text
UNIVERSAL_ALGEBRA_AND_EQUATIONAL_LOGIC = COVERED
REWRITING_AND_CONFLUENCE = COVERED
CATEGORICAL_COHERENCE = COVERED
OPERADS_AND_ALGEBRAIC_THEORIES = COVERED
SYMMETRY_AND_THEORETICAL_EQUIVALENCE = COVERED_AT_COMPARISON_SCOPE
OPERATIONAL_INFORMATIONAL_RECONSTRUCTION = COVERED
CONSTRUCTOR_TASK_POSSIBILITY = COVERED
LOCAL_TO_GLOBAL_OBSTRUCTION = COVERED
```

The finite formula encoding theorem is elementary and does not require new source intake for the present adjudication.

```text
SPECIFIC_BLOCKING_SOURCE_GAP = NONE
SOURCE_EXPANSION_JUSTIFIED = NO
```

## Acceptance criteria

```text
A1_FORMULA_UNIVERSAL_ENCODING_CONTROL = PASS
A2_COMPACT_DESCRIPTION_LANGUAGE_CONTROL = PASS
A3_EQUATIONAL_SUPPORT_FAMILY = CLASSIFIED
A4_TYPING_INTERFACE_SUPPORT_FAMILY = CLASSIFIED
A5_COHERENCE_SUPPORT_FAMILY = CLASSIFIED
A6_SYMMETRY_SUPPORT_FAMILY = CLASSIFIED
A7_EMPIRICAL_OPERATIONAL_SUPPORT_SMUGGLING_CONTROL = PASS
A8_FROZEN_CORPUS_USED_FIRST = PASS
A9_SPECIFIC_SOURCE_GAP_IF_ANY = NONE
A10_NO_SUCCESSOR_GRAMMAR_SELECTED = PASS
```

## Scientific consequence

PGH-1 has now moved the R2 bottleneck one meta-level deeper.

It is not enough to say:

```text
LOCAL_SUPPORTS_ARE_GENERATED_BY_RULES
```

because an unrestricted rule language can encode arbitrary supports.

The next burden is:

\[
\boxed{\text{What independently fixes or restricts the local rule language itself?}}
\]

A successful route must constrain the signature, primitive predicates/operations, and rule-construction machinery before target physical supports are consulted.

This does not refute anchored PGH. It prevents support-generation syntax from being counted as explanatory merely because it is compact.

## Hard-stop verification

```text
OBSERVED_SUPPORT_IMPORTED_AS_GRAMMAR = NO
SHORT_TABLE_CALLED_DERIVATION = NO
TARGET_FITTED_LOGIC_OR_TYPE_SYSTEM_SELECTED = NO
COHERENCE_PROMOTED_TO_PHYSICAL_LAW = NO
SUCCESSOR_GRAMMAR_SELECTED = NO
NEW_SOURCE_SEARCH = NO
FCP_CHANGED = NO
```
