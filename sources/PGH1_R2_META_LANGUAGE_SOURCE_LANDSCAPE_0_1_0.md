# PGH-1 R2 Meta-Language and Logical-Framework Source Landscape 0.1.0

## Identity

```text
SOURCE_GAP_ID = SG3_META_LANGUAGE_AND_LOGICAL_FRAMEWORK_ORIGIN
ACCEPTED_SOURCE_RECORDS = 19
SEARCH_LANES = 5
LANDSCAPE_RESULT = B__MATURE_LANGUAGE_ORGANIZATION_AND_TRANSLATION_MACHINERY_WITHOUT_GENERAL_SELECTION_OF_ONE_PRIVILEGED_LOGIC
SCIENTIFIC_ADJUDICATION = NOT_PERFORMED
SUCCESSOR_GRAMMAR = NONE
PHYSICAL_CLAIM = NONE
```

## Executive result

The SG3 literature is mature and directly relevant to the PGH meta-language-origin problem.

It supplies at least four powerful kinds of machinery:

1. **logic-independent abstraction** — institutions and general logics provide common structures in which many concrete logics can be studied;
2. **metalanguage representation** — logical frameworks provide fixed meta-level syntax/judgment/proof infrastructure in which object logics are presented;
3. **structure-relative logic generation/semantics** — categorical logic and type theory derive or organize logical operations relative to categorical, fibred, or contextual structure;
4. **structural-rule variation** — Gentzen-style and substructural proof theory show that exchange, weakening, contraction, context order, and related structural principles materially alter derivability while leaving substantial logical vocabulary comparable.

The corpus does **not** reveal a general theorem or accepted principle that starts from neutral meta-structure and uniquely selects one object logic, one structural-rule package, or one physically privileged rule language.

That absence is a landscape finding, not proof that no such principle can exist.

## L1 — Institutions, general logics, and logic independence

### Core sources

```text
SG3-001 Goguen & Burstall 1992
SG3-002 Meseguer 1989
SG3-003 Diaconescu 2008
SG3-004 Mossakowski, Diaconescu & Tarlecki 2009
SG3-005 Tutu 2013
```

Institution theory is especially important for PGH because it explicitly separates what is invariant across a logical system from the internal details of one concrete logic.

The satisfaction condition is designed to make truth invariant under change of notation/signature in the appropriate sense. Institution-independent model theory then develops substantial model theory without commitment to one concrete logic. Abstract logic translations and institution comorphisms further formalize relationships between different logical systems.

For PGH this establishes a strong distinction:

```text
LANGUAGE_INVARIANCE / TRANSLATION_DISCIPLINE = MATURE
UNIQUE_LOGIC_SELECTION = NOT_SUPPLIED_BY_THAT_DISCIPLINE
```

The fact that one can state model-theoretic results independently of a concrete logic is evidence that meta-level invariance can be scientifically useful without collapsing the family of possible logics to one member.

### PGH consequence at source-landscape scope

A future PGH meta-grammar cannot claim uniqueness merely because it supports faithful translations or satisfaction invariance. Institution theory shows that such invariance is compatible with deliberate pluralism over object logics.

## L2 — Logical frameworks as metalanguages

### Core sources

```text
SG3-006 Harper, Honsell & Plotkin 1993
SG3-007 Pfenning 2001
SG3-008 Harper 2021
```

LF is explicitly a framework for **defining or presenting logics**. It fixes a dependently typed metalanguage and a judgments-as-types representation principle while object-logical judgments, constants, and inference rules are supplied as encodings/signatures.

Pfenning's survey makes the design-choice issue explicit: logical frameworks themselves come in different styles, including deductive and equational/rewrite-oriented frameworks. Harper's equational framework likewise presents many type theories by supplying signatures of constants inside a common framework.

The source-supported separation is therefore:

```text
META_FRAMEWORK = CAN_BE_FIXED
OBJECT_LOGIC = STILL_PARAMETERIZED
FRAMEWORK_DESIGN = ITSELF_NONUNIQUE
```

### PGH consequence at source-landscape scope

A successful PGH cannot point to the mere existence of a logical framework as a solution to rule-language origin. Logical frameworks demonstrate precisely how much reusable structure can be centralized while still leaving theory-specific rules and signatures as input.

## L3 — Categorical logic, hyperdoctrines, and contextual/type structure

### Core sources

```text
SG3-009 Lawvere 1969
SG3-010 Makkai & Reyes 1977
SG3-011 Jacobs 1999
SG3-012 Cartmell 1986
```

This lane is the strongest positive neighbor to the PGH idea that logical or grammatical structure might follow from more abstract relational/compositional organization.

Lawvere shows logical operations arising through adjoint/categorical structure. Makkai and Reyes develop inference, models, theories, and completeness categorically. Jacobs systematizes logic and type theory through fibred categories, while Cartmell develops generalized algebraic theories and contextual categories.

These works show that:

```text
LOGICAL_STRUCTURE_CAN_BE_GENERATED_OR_CHARACTERIZED_RELATIVE_TO_ABSTRACT_STRUCTURE = YES
```

But the qualifier **relative to** matters. Different categorical assumptions support different internal logics/type theories. The categorical framework does not erase the need to say what categorical/fibrational/contextual structure is present.

### PGH consequence at source-landscape scope

Categorical logic is a serious candidate resource for explaining how a restricted rule language can arise from deeper structure. It is not, from this corpus alone, a selector of the deeper structure itself.

Thus it potentially moves PGH's explanatory burden upward rather than eliminating it—the same pattern already found internally in `PGH-FAIL-0017`.

## L4 — Structural and substructural proof theory

### Core sources

```text
SG3-013 Gentzen 1935
SG3-014 Lambek 1958
SG3-015 Girard 1987
SG3-016 Belnap 1982
SG3-017 Restall 2000
SG3-018 Dosen 1989
SG3-019 SEP Substructural Logics
```

This lane provides the clearest source-based reason PGH must treat structural-rule origin as substantive rather than cosmetic.

Gentzen's sequent calculus makes structural manipulations explicit. Lambek's calculus removes structural freedoms appropriate to unordered/reusable contexts. Linear logic controls weakening and contraction through its resource-sensitive architecture. Display logic supplies a common structural setting for multiple logical systems. Restall surveys the broader substructural family. Došen explicitly analyzes structural deduction as prior to the punctuation supplied by logical constants and notes that alternative logical systems can arise by changing structural deductions.

The source-supported conclusion is:

```text
CHANGE_STRUCTURAL_RULES => CHANGE_DERIVABILITY / LOGICAL_SYSTEM
STRUCTURAL_RULE_PACKAGE = SCIENTIFICALLY_MATERIAL_FORMAL_INPUT
```

The literature supplies many disciplined alternatives; it does not supply a general neutral theorem selecting exchange vs nonexchange, contraction vs noncontraction, weakening vs nonweakening, or one related package as universally privileged.

### PGH consequence at source-landscape scope

This lane strengthens the meta-language-origin burden rather than resolving it. A PGH rule language must explain why its structural permissions have their particular form instead of treating them as invisible background syntax.

## L5 — Translation and heterogeneous-control lane

The institution/translation and display-logic sources show that a framework can remain highly systematic while accommodating multiple logics.

```text
REPRESENTATION_OR_TRANSLATION_ROBUSTNESS = COMPATIBLE_WITH_LOGICAL_PLURALITY
```

That is an important negative control against a recurrent PGH temptation:

> If a meta-language is sufficiently invariant under representation change, perhaps it must be the uniquely fundamental logic.

The source landscape does not support that inference.

Translation frameworks can preserve satisfaction, entailment-related structure, expressiveness relationships, or proof-theoretic behavior while leaving source and target logics genuinely distinct.

## Cross-lane synthesis

The corpus separates three questions that PGH must not collapse:

### 1. Can many logics be represented in one meta-framework?

```text
YES
```

Institution theory, general logics, and logical frameworks answer this strongly.

### 2. Can logical operations/rules arise from abstract structure?

```text
YES_CONDITIONALLY
```

Categorical logic, type-theoretic/contextual structures, and structural proof theory provide many examples.

### 3. Does the meta-framework or abstract structure generally select one privileged logic/rule package?

```text
NO_GENERAL_SELECTION_PRINCIPLE_FOUND_IN_REPRESENTATIVE_SG3_CORPUS
```

This is the key SG3 result.

## Strongest PGH-relevant source lesson

The literature repeatedly has the form

\[
M + \Theta \longrightarrow L,
\]

where:

- `M` is reusable meta-level architecture;
- `Theta` is a signature, category, type discipline, structural-rule package, theory presentation, or translation input;
- `L` is the resulting logic/theory/proof system.

PGH's R2 problem is not merely to find `M`.

It is to explain why the selective information in `Theta` is not an arbitrary or physical-law-loaded input.

The SG3 corpus therefore sharpens the target to:

\[
\boxed{\text{Can the variable structural package itself be generated from a smaller invariant principle?}}
\]

without simply adding another unearned meta-layer.

## Outcome

```text
OUTCOME = B
MATURE_META_LANGUAGE_ORGANIZATION = YES
MATURE_LOGIC_TRANSLATION = YES
STRUCTURE_RELATIVE_LOGIC_GENERATION = YES
STRUCTURAL_RULE_VARIABILITY = YES
GENERAL_PRIVILEGED_LOGIC_SELECTOR = NOT_FOUND_AT_REPRESENTATIVE_SCOPE
SUCCESSOR_GRAMMAR = NONE
PHYSICAL_LAW_DERIVED = NO
R2_SATISFIED = NO
```

## Next scientific use

The corpus is sufficient for a separate source-bound adjudication comparing the canonical PGH meta-language-origin failure against:

1. institutions/logical frameworks as **neutral metalanguages**;
2. categorical/type-theoretic formalisms as **structure-relative logic generators**;
3. substructural proof theory as **evidence that structural rules carry selective content**.

That later adjudication—not this intake—should decide whether PGH now has:

- only a reformulation of known meta-logical underdetermination;
- a narrowed residual burden about generation of structural rules;
- or a genuinely promising route through structure-to-logic generation.
