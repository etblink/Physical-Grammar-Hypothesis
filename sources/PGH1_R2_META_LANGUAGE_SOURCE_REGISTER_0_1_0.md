# PGH-1 R2 Meta-Language and Logical-Framework Source Register 0.1.0

## Scope

```text
SOURCE_GAP_ID = SG3_META_LANGUAGE_AND_LOGICAL_FRAMEWORK_ORIGIN
ACCEPTED_SOURCE_RECORDS = 19
NEW_DISTINCT_AT_REPOSITORY_SEARCH_SCOPE = 19
PREEXISTING_FROZEN_ACCEPTED_SOURCES = 51
TOTAL_DISTINCT_IF_DEDUP_SCOPE_HOLDS = 70
PHYSICAL_CLAIM = NONE
SUCCESSOR_GRAMMAR_SELECTION = NONE
```

The records below are frozen for the bounded SG3 landscape. `META_LANGUAGE_FIXED_STRUCTURE` and `META_LANGUAGE_VARIABLE_STRUCTURE` are PGH extraction fields, not claims that the cited authors use PGH terminology.

---

## SG3-001 — Goguen & Burstall 1992

```text
SOURCE_ID = SG3-001
LANE = SG3-L1 / SG3-L5
AUTHOR = Joseph A. Goguen; Rod M. Burstall
TITLE = Institutions: Abstract Model Theory for Specification and Programming
YEAR = 1992
SOURCE_CLASS = PRIMARY_FOUNDATIONAL_PAPER
LOCATOR = doi:10.1145/147508.147524
DISPOSITION = ACCEPT
```

**Authority note:** Foundational Journal of the ACM paper introducing institutions as an abstract notion of logical system.

**Direct relevance:** Institution theory abstracts syntax/model/satisfaction structure so different logics can be treated uniformly and translations can preserve truth via the satisfaction condition.

```text
META_LANGUAGE_FIXED_STRUCTURE = institution-level architecture and satisfaction invariance
META_LANGUAGE_VARIABLE_STRUCTURE = concrete signatures, sentences, models, individual logic
SELECTION_OR_NEUTRALITY_RESULT = strong organization/neutrality; no general physical or intrinsic selector of one object logic supplied
PGH_RELEVANCE = direct control showing representation-independent treatment of many logics need not select one logic
```

## SG3-002 — Meseguer 1989

```text
SOURCE_ID = SG3-002
LANE = SG3-L1 / SG3-L5
AUTHOR = José Meseguer
TITLE = General Logics
YEAR = 1989
SOURCE_CLASS = PRIMARY_FOUNDATIONAL_PAPER
LOCATOR = doi:10.1016/S0049-237X(08)70132-0
DISPOSITION = ACCEPT
```

**Authority note:** Foundational general-logic paper in *Studies in Logic and the Foundations of Mathematics*.

**Direct relevance:** Develops an abstract framework in which different logical systems and relationships among them can be studied at a common level.

```text
META_LANGUAGE_FIXED_STRUCTURE = abstract architecture for logical entailment/system comparison
META_LANGUAGE_VARIABLE_STRUCTURE = concrete logic and its syntax/semantics/proof details
SELECTION_OR_NEUTRALITY_RESULT = generalizes across logics rather than selecting one
PGH_RELEVANCE = demonstrates that generality at the meta-level does not by itself determine a privileged object logic
```

## SG3-003 — Diaconescu 2008

```text
SOURCE_ID = SG3-003
LANE = SG3-L1
AUTHOR = Răzvan Diaconescu
TITLE = Institution-independent Model Theory
YEAR = 2008
SOURCE_CLASS = STANDARD_RESEARCH_MONOGRAPH
LOCATOR = doi:10.1007/978-3-7643-8708-2
DISPOSITION = ACCEPT
```

**Authority note:** First monograph devoted to institution-independent model theory.

**Direct relevance:** Explicitly develops model theory without commitment to one concrete logic, using institutions as the abstraction boundary.

```text
META_LANGUAGE_FIXED_STRUCTURE = institution-theoretic model-theory machinery
META_LANGUAGE_VARIABLE_STRUCTURE = underlying concrete logical system
SELECTION_OR_NEUTRALITY_RESULT = deliberate logic-independence; no unique logic selected by the framework
PGH_RELEVANCE = strong evidence that meta-level structural cleanliness is compatible with plural object logics
```

## SG3-004 — Mossakowski, Diaconescu & Tarlecki 2009

```text
SOURCE_ID = SG3-004
LANE = SG3-L5 / SG3-L1
AUTHOR = Till Mossakowski; Răzvan Diaconescu; Andrzej Tarlecki
TITLE = What Is a Logic Translation?
YEAR = 2009
SOURCE_CLASS = PRIMARY_RESEARCH_PAPER
LOCATOR = doi:10.1007/s11787-009-0005-2
DISPOSITION = ACCEPT
```

**Authority note:** Direct study of logic translations at an abstract level.

**Direct relevance:** Treats translations without commitment to the concrete structure of sentences or whether entailment is proof- or model-theoretic; studies expressiveness, consistency strength, and sublogic relations.

```text
META_LANGUAGE_FIXED_STRUCTURE = abstract translation conditions and preservation/reflection properties
META_LANGUAGE_VARIABLE_STRUCTURE = source and target logics
SELECTION_OR_NEUTRALITY_RESULT = comparison/translation machinery, not a unique-logic selector
PGH_RELEVANCE = directly addresses faithful-change-of-language machinery while preserving logical plurality
```

## SG3-005 — Ţuţu 2013

```text
SOURCE_ID = SG3-005
LANE = SG3-L5 / SG3-L1
AUTHOR = Ionuţ Ţuţu
TITLE = Comorphisms of Structured Institutions
YEAR = 2013
SOURCE_CLASS = PRIMARY_RESEARCH_PAPER
LOCATOR = doi:10.1016/j.ipl.2013.09.003
DISPOSITION = ACCEPT
```

**Authority note:** Peer-reviewed extension of institution comorphisms to structured institutions.

**Direct relevance:** Formalizes translations between structured specification logics and supports heterogeneous specification where both logical systems and structuring mechanisms may vary.

```text
META_LANGUAGE_FIXED_STRUCTURE = comorphism/translation architecture
META_LANGUAGE_VARIABLE_STRUCTURE = base logic and specification-structuring mechanism
SELECTION_OR_NEUTRALITY_RESULT = heterogeneity supported rather than collapsed to one privileged logic
PGH_RELEVANCE = shows robust translation machinery can coexist with variability even at the meta-language level
```

## SG3-006 — Harper, Honsell & Plotkin 1993

```text
SOURCE_ID = SG3-006
LANE = SG3-L2
AUTHOR = Robert Harper; Furio Honsell; Gordon Plotkin
TITLE = A Framework for Defining Logics
YEAR = 1993
SOURCE_CLASS = PRIMARY_FOUNDATIONAL_PAPER
LOCATOR = doi:10.1145/138027.138060
DISPOSITION = ACCEPT
```

**Authority note:** Foundational JACM paper defining the Edinburgh Logical Framework (LF).

**Direct relevance:** LF supplies a typed dependent-lambda metalanguage in which syntax, judgments, rules, and proofs of many object logics can be represented; proof checking becomes type checking in the framework.

```text
META_LANGUAGE_FIXED_STRUCTURE = LF dependent-type metalanguage and judgments-as-types representation principle
META_LANGUAGE_VARIABLE_STRUCTURE = object-logic constants, judgments, rules, axioms
SELECTION_OR_NEUTRALITY_RESULT = object logics are encoded/presented; LF does not by itself select one as uniquely correct
PGH_RELEVANCE = precise example of a strong meta-language whose fixed architecture still requires object-logic content as input
```

## SG3-007 — Pfenning 2001

```text
SOURCE_ID = SG3-007
LANE = SG3-L2
AUTHOR = Frank Pfenning
TITLE = Logical Frameworks
YEAR = 2001
SOURCE_CLASS = AUTHORITATIVE_SURVEY_CHAPTER
LOCATOR = Handbook of Automated Reasoning, Chapter 17, pp. 1063-1147
DISPOSITION = ACCEPT
```

**Authority note:** Standard survey by a principal contributor to logical-framework research.

**Direct relevance:** Explicitly characterizes a logical framework as a meta-language for specifying deductive systems and reviews design choices among frameworks.

```text
META_LANGUAGE_FIXED_STRUCTURE = chosen framework's representation/proof infrastructure
META_LANGUAGE_VARIABLE_STRUCTURE = represented deductive systems/object logics
SELECTION_OR_NEUTRALITY_RESULT = multiple framework designs and multiple encoded logics remain possible
PGH_RELEVANCE = source-supported evidence that meta-framework design itself contains substantive choices
```

## SG3-008 — Harper 2021

```text
SOURCE_ID = SG3-008
LANE = SG3-L2 / SG3-L3
AUTHOR = Robert Harper
TITLE = An Equational Logical Framework for Type Theories
YEAR = 2021
SOURCE_CLASS = PRIMARY_RESEARCH_PAPER
LOCATOR = arXiv:2106.01484
DISPOSITION = ACCEPT
```

**Authority note:** Primary work by a principal logical-framework author on presenting type theories as equational theories in a framework.

**Direct relevance:** Shows a broad class of type theories can be presented through a framework while the particular type theory is supplied by a signature of constants.

```text
META_LANGUAGE_FIXED_STRUCTURE = equational logical-framework architecture
META_LANGUAGE_VARIABLE_STRUCTURE = signature/constants specifying individual type theory
SELECTION_OR_NEUTRALITY_RESULT = framework supports a class of type theories; signature remains input
PGH_RELEVANCE = sharp control on the distinction between framework-level organization and theory-level selective content
```

## SG3-009 — Lawvere 1969

```text
SOURCE_ID = SG3-009
LANE = SG3-L3
AUTHOR = F. William Lawvere
TITLE = Adjointness in Foundations
YEAR = 1969
SOURCE_CLASS = PRIMARY_FOUNDATIONAL_PAPER
LOCATOR = doi:10.1111/j.1746-8361.1969.tb01194.x
DISPOSITION = ACCEPT
```

**Authority note:** Seminal categorical-foundations paper connecting adjointness with logic and hyperdoctrines.

**Direct relevance:** Exhibits categorical structure capable of organizing propositional and predicate-logical operations through adjunctions.

```text
META_LANGUAGE_FIXED_STRUCTURE = chosen categorical/hyperdoctrine structure and adjunction architecture
META_LANGUAGE_VARIABLE_STRUCTURE = concrete category/model and additional categorical properties
SELECTION_OR_NEUTRALITY_RESULT = derives logical structure relative to categorical structure; does not supply a PGH-style physical selector for the categorical base
PGH_RELEVANCE = important positive example of logical operations arising from structural organization, with the origin of the organizing structure still a separate question
```

## SG3-010 — Makkai & Reyes 1977

```text
SOURCE_ID = SG3-010
LANE = SG3-L3
AUTHOR = Michael Makkai; Gonzalo E. Reyes
TITLE = First Order Categorical Logic
YEAR = 1977
SOURCE_CLASS = STANDARD_RESEARCH_MONOGRAPH
LOCATOR = doi:10.1007/BFb0066201
DISPOSITION = ACCEPT
```

**Authority note:** Foundational monograph in categorical logic.

**Direct relevance:** Develops interpretation of logic in categories, categorical inference principles, theories as categories, and classifying structures.

```text
META_LANGUAGE_FIXED_STRUCTURE = categorical semantic/structural conditions
META_LANGUAGE_VARIABLE_STRUCTURE = theories, models, categories satisfying differing properties
SELECTION_OR_NEUTRALITY_RESULT = categorical environment determines available logical behavior conditionally, not one universal object logic without further structure
PGH_RELEVANCE = establishes mature formal machinery for structural generation/interpretation of logical laws while leaving structure choice explicit
```

## SG3-011 — Jacobs 1999

```text
SOURCE_ID = SG3-011
LANE = SG3-L3
AUTHOR = Bart Jacobs
TITLE = Categorical Logic and Type Theory
YEAR = 1999
SOURCE_CLASS = STANDARD_RESEARCH_MONOGRAPH
LOCATOR = ISBN 978-0-444-50170-7
DISPOSITION = ACCEPT
```

**Authority note:** Standard systematic reference unifying logic and type theory through fibred category theory.

**Direct relevance:** Organizes multiple logics and type theories categorically, including signatures, dependent types, predicate logic, and higher-order structure.

```text
META_LANGUAGE_FIXED_STRUCTURE = fibration/comprehension/category-theoretic architecture
META_LANGUAGE_VARIABLE_STRUCTURE = signatures, categorical models, logical/type-theoretic strength
SELECTION_OR_NEUTRALITY_RESULT = systematic organization of families rather than intrinsic selection of one physical logic
PGH_RELEVANCE = strong map of how type/logical structure depends on categorical assumptions
```

## SG3-012 — Cartmell 1986

```text
SOURCE_ID = SG3-012
LANE = SG3-L3 / SG3-L2
AUTHOR = John Cartmell
TITLE = Generalised Algebraic Theories and Contextual Categories
YEAR = 1986
SOURCE_CLASS = PRIMARY_RESEARCH_PAPER
LOCATOR = doi:10.1016/0168-0072(86)90053-9
DISPOSITION = ACCEPT
```

**Authority note:** Foundational paper on generalized algebraic theories/contextual categories.

**Direct relevance:** Provides a structured theory of dependent/context-sensitive algebraic signatures and their categorical organization.

```text
META_LANGUAGE_FIXED_STRUCTURE = generalized algebraic/contextual-category doctrine
META_LANGUAGE_VARIABLE_STRUCTURE = particular generalized algebraic theory/signature
SELECTION_OR_NEUTRALITY_RESULT = formal framework organizes theory formation; specific selective signature remains theory data
PGH_RELEVANCE = relevant to whether typing/interface structure can be generated structurally without becoming an arbitrary target-specific signature
```

## SG3-013 — Gentzen 1935

```text
SOURCE_ID = SG3-013
LANE = SG3-L4
AUTHOR = Gerhard Gentzen
TITLE = Untersuchungen über das logische Schließen I & II
YEAR = 1935
SOURCE_CLASS = PRIMARY_FOUNDATIONAL_PAPER
LOCATOR = doi:10.1007/BF01201353 ; doi:10.1007/BF01201363
DISPOSITION = ACCEPT
```

**Authority note:** Foundational source for natural deduction and sequent calculus.

**Direct relevance:** Separates logical inference rules from structural manipulation of contexts and establishes the proof-theoretic setting in which structural rules can be studied explicitly.

```text
META_LANGUAGE_FIXED_STRUCTURE = sequent/natural-deduction proof architecture in the chosen calculus
META_LANGUAGE_VARIABLE_STRUCTURE = logical rules and structural rule package across calculi
SELECTION_OR_NEUTRALITY_RESULT = foundational formulation exposes structural assumptions rather than deriving one uniquely necessary package
PGH_RELEVANCE = baseline for treating structural rules as genuine meta-level contributors to derivability
```

## SG3-014 — Lambek 1958

```text
SOURCE_ID = SG3-014
LANE = SG3-L4
AUTHOR = Joachim Lambek
TITLE = The Mathematics of Sentence Structure
YEAR = 1958
SOURCE_CLASS = PRIMARY_FOUNDATIONAL_PAPER
LOCATOR = doi:10.2307/2310058
DISPOSITION = ACCEPT
```

**Authority note:** Foundational source for the Lambek calculus and substructural/categorial grammar tradition.

**Direct relevance:** Demonstrates a proof/grammar system in which order and compositional structure matter and standard structural freedoms are not simply assumed.

```text
META_LANGUAGE_FIXED_STRUCTURE = ordered compositional calculus
META_LANGUAGE_VARIABLE_STRUCTURE = lexical/category assignments and derivable structures
SELECTION_OR_NEUTRALITY_RESULT = a distinct structural regime, not a derivation that all logics must share it
PGH_RELEVANCE = direct evidence that structural rule choice changes what counts as well-formed/derivable
```

## SG3-015 — Girard 1987

```text
SOURCE_ID = SG3-015
LANE = SG3-L4
AUTHOR = Jean-Yves Girard
TITLE = Linear Logic
YEAR = 1987
SOURCE_CLASS = PRIMARY_FOUNDATIONAL_PAPER
LOCATOR = doi:10.1016/0304-3975(87)90045-4
DISPOSITION = ACCEPT
```

**Authority note:** Foundational linear-logic paper.

**Direct relevance:** Restricts ordinary unrestricted weakening/contraction and makes resource-sensitive structure explicit, with modalities controlling where those structural behaviors are recovered.

```text
META_LANGUAGE_FIXED_STRUCTURE = linear proof-theoretic architecture and controlled structural behavior
META_LANGUAGE_VARIABLE_STRUCTURE = formulas/theories modeled within the logic
SELECTION_OR_NEUTRALITY_RESULT = supplies a powerful alternative structural regime, not an intrinsic selector proving linear logic uniquely mandatory
PGH_RELEVANCE = decisive control that modifying meta-level structural permissions changes admissibility and proof theory
```

## SG3-016 — Belnap 1982

```text
SOURCE_ID = SG3-016
LANE = SG3-L4 / SG3-L5
AUTHOR = Nuel D. Belnap Jr.
TITLE = Display Logic
YEAR = 1982
SOURCE_CLASS = PRIMARY_FOUNDATIONAL_PAPER
LOCATOR = doi:10.1007/BF00284976
DISPOSITION = ACCEPT
```

**Authority note:** Foundational display-logic paper.

**Direct relevance:** Constructs a general proof-theoretic architecture capable of treating multiple logics, with structural machinery controlling how formula occurrences can be displayed and related.

```text
META_LANGUAGE_FIXED_STRUCTURE = display-calculus structural architecture
META_LANGUAGE_VARIABLE_STRUCTURE = indexed connective/logical families and their rules
SELECTION_OR_NEUTRALITY_RESULT = explicitly supports multiple logics rather than selecting one
PGH_RELEVANCE = another strong example of unifying structural meta-language without unique object-logic selection
```

## SG3-017 — Restall 2000

```text
SOURCE_ID = SG3-017
LANE = SG3-L4
AUTHOR = Greg Restall
TITLE = An Introduction to Substructural Logics
YEAR = 2000
SOURCE_CLASS = STANDARD_RESEARCH_MONOGRAPH
LOCATOR = Routledge, ISBN 9780415215343
DISPOSITION = ACCEPT
```

**Authority note:** Standard monograph surveying the family of substructural logics.

**Direct relevance:** Systematically studies logics obtained by altering structural assumptions and their proof-theoretic/semantic consequences.

```text
META_LANGUAGE_FIXED_STRUCTURE = chosen proof-theoretic framework for structural comparison
META_LANGUAGE_VARIABLE_STRUCTURE = exchange/weakening/contraction/related structural principles
SELECTION_OR_NEUTRALITY_RESULT = plural family generated by structural choices; no unique structural package selected by the family concept itself
PGH_RELEVANCE = direct support for treating structural-rule origin as a substantive unresolved selector problem
```

## SG3-018 — Došen 1989

```text
SOURCE_ID = SG3-018
LANE = SG3-L4
AUTHOR = Kosta Došen
TITLE = Logical Constants as Punctuation Marks
YEAR = 1989
SOURCE_CLASS = PRIMARY_RESEARCH_PAPER
LOCATOR = doi:10.1305/ndjfl/1093635154
DISPOSITION = ACCEPT
```

**Authority note:** Direct proof-theoretic analysis of the relation between structural deductions and logical constants.

**Direct relevance:** Treats basic structural deductions as prior to logical constants and notes that alternative logical systems arise by changing structural deductions while retaining analogous constants.

```text
META_LANGUAGE_FIXED_STRUCTURE = structural-deduction perspective
META_LANGUAGE_VARIABLE_STRUCTURE = structural deduction package and resulting logical system
SELECTION_OR_NEUTRALITY_RESULT = explicitly highlights alternative systems from different structural deductions
PGH_RELEVANCE = unusually direct prior art for the idea that meta-level structural rules determine much of a logic's grammar, while leaving their ultimate selection open
```

## SG3-019 — SEP Substructural Logics

```text
SOURCE_ID = SG3-019
LANE = SG3-L4
AUTHOR = Greg Restall et al. / Stanford Encyclopedia of Philosophy entry
TITLE = Substructural Logics
YEAR = current authoritative revision consulted 2026
SOURCE_CLASS = AUTHORITATIVE_FIELD_SURVEY
LOCATOR = Stanford Encyclopedia of Philosophy, entry: logic-substructural
DISPOSITION = ACCEPT
```

**Authority note:** Authoritative survey used to cross-check field structure and terminology, not as a substitute for the primary sources above.

**Direct relevance:** Maps how classical, intuitionistic, relevance, linear, and related logics depend on structural settings of sequents and structural rules.

```text
META_LANGUAGE_FIXED_STRUCTURE = comparative proof-theoretic vocabulary
META_LANGUAGE_VARIABLE_STRUCTURE = ambient structural rules/context behavior
SELECTION_OR_NEUTRALITY_RESULT = field-level plurality, not unique selection
PGH_RELEVANCE = saturation and terminology control for SG3-L4
```

---

## Rejected / deferred candidates

```text
R-SG3-001 = Diaconescu 2025/2026 second edition of Institution-independent Model Theory
DISPOSITION = REJECT_REDUNDANT
REASON = newer edition of accepted SG3-003; no need to double-count one monograph lineage

R-SG3-002 = MathWorld/Wikipedia structural-rule pages
DISPOSITION = REJECT_WEAK_AUTHORITY
REASON = discovery aids only; primary/standard sources available

R-SG3-003 = ResearchGate copies of Belnap / logic-translation papers
DISPOSITION = REJECT_REDUNDANT
REASON = metadata/full-text mirrors of accepted primary publications

R-SG3-004 = PLS Lab bibliography pages
DISPOSITION = REJECT_WEAK_AUTHORITY
REASON = useful bibliographic discovery but superseded by primary publisher/author records

R-SG3-005 = modern application-specific substructural quantum-logic papers
DISPOSITION = REJECT_REMOTE_RELEVANCE
REASON = SG3 concerns origin/organization of meta-language, not physical applications of an already selected substructural logic

R-SG3-006 = recent complexity studies of substructural logics
DISPOSITION = REJECT_REMOTE_RELEVANCE
REASON = consequences of fixed structural systems rather than origin of structural rule package

R-SG3-007 = assorted theorem-prover implementation papers
DISPOSITION = REJECT_REMOTE_RELEVANCE
REASON = implementations do not materially address the rule-language selection burden

R-SG3-008 = secondary historical pages for Gentzen/Lambek
DISPOSITION = REJECT_REDUNDANT
REASON = primary bibliographic locators recovered
```
