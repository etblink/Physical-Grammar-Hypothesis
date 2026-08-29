# PGH-1 R2 Local-to-Global / Global-Constraint Source Register 0.1.0

## Status

```text
OPERATION_ID = PGH1_R2_LOCAL_TO_GLOBAL_AND_GLOBAL_CONSTRAINT_SOURCE_INTAKE
REGISTRY_ID = PGH-OP-0033
SOURCE_REGISTER_STATUS = FROZEN_CANDIDATE
TOTAL_ACCEPTED_SOURCE_COUNT = 15
NEW_EXTERNAL_ACCEPTED = 14
REUSED_CANONICAL_ACCEPTED = 1
SG1_ACCEPTED = 9
SG2_ACCEPTED = 6
PHYSICAL_GRAMMAR_SELECTION = NONE
FCP_EFFECT = NONE
```

Inclusion means relevance to the bounded R2 mechanism audit. It does not endorse a source's ontology or make its formalism part of PGH.

## Accepted sources

| ID | Authors | Title | Year | Type | Lane | Stable locator | Intake relevance |
|---|---|---|---:|---|---|---|---|
| PGH-R2-SRC-001 | Saunders Mac Lane; Ieke Moerdijk | *Sheaves in Geometry and Logic: A First Introduction to Topos Theory* | 1992 | Standard monograph | SG1 | DOI `10.1007/978-1-4612-0927-0` | Authoritative sheaf/gluing background; separates generic local-to-global machinery from quantum-specific interpretation. |
| PGH-R2-SRC-002 | N. N. Vorob'ev | *Consistent Families of Measures and Their Extensions* | 1962 | Primary mathematics article | SG1 | DOI `10.1137/1107014` | Direct extension problem: pairwise-consistent local measures need not admit a global extension; regularity condition controls universal extendability. |
| PGH-R2-SRC-003 | Arthur Fine | *Hidden Variables, Joint Probability, and the Bell Inequalities* | 1982 | Primary physics/foundations article | SG1 | DOI `10.1103/PhysRevLett.48.291` | Physical comparison: existence of one global joint distribution is equivalent to Bell-type conditions in the stated scenario. |
| PGH-R2-SRC-004 | Samson Abramsky; Adam Brandenburger | *The Sheaf-Theoretic Structure of Non-Locality and Contextuality* | 2011 | Primary interdisciplinary article | SG1 | DOI `10.1088/1367-2630/13/11/113036`; arXiv `1102.0264` | Central source: nonlocality/contextuality characterized as obstruction to global sections over compatible local measurement data. |
| PGH-R2-SRC-005 | Samson Abramsky; Shane Mansfield; Rui Soares Barbosa | *The Cohomology of Non-Locality and Contextuality* | 2011/2012 | Peer-reviewed conference article | SG1 | DOI `10.4204/EPTCS.95.1`; arXiv `1111.3620` | Cohomological obstruction witnesses for failure of global sections; useful control on sufficient versus necessary obstructions. |
| PGH-R2-SRC-006 | Samson Abramsky; Lucien Hardy | *Logical Bell Inequalities* | 2012 | Primary physics article | SG1 | DOI `10.1103/PhysRevA.85.062114`; arXiv `1203.1352` | Derives broad Bell inequalities from logical consistency; comparison case for compact consistency principles yielding testable exclusions. |
| PGH-R2-SRC-007 | Adán Cabello; Simone Severini; Andreas Winter | *Graph-Theoretic Approach to Quantum Correlations* | 2014 | Primary physics article | SG1 | DOI `10.1103/PhysRevLett.112.040401`; arXiv `1401.7081` | Alternative combinatorial contextuality framework; maps exclusivity structure to classical/quantum/general correlation bounds. |
| PGH-R2-SRC-008 | Antonio Acín; Tobias Fritz; Anthony Leverrier; Ana Belén Sainz | *A Combinatorial Approach to Nonlocality and Contextuality* | 2015 | Primary mathematical-physics article | SG1 | DOI `10.1007/s00220-014-2260-1`; arXiv `1212.4084` | Hypergraph contextuality scenarios with normalized probabilistic models; important alternative to sheaf language and representation-dependence control. |
| PGH-R2-SRC-009 | Costantino Budroni; Adán Cabello; Otfried Gühne; Matthias Kleinmann; Jan-Åke Larsson | *Kochen-Specker Contextuality* | 2022 | Authoritative review | SG1 | DOI `10.1103/RevModPhys.94.045007`; arXiv `2102.13036` | Modern map of contextuality definitions, proofs, experiments, and graph/nonlocality relations; saturation/control source. |
| PGH-R2-SRC-010 | R. P. Feynman | *Space-Time Approach to Non-Relativistic Quantum Mechanics* | 1948 | Primary physics article | SG2 | DOI `10.1103/RevModPhys.20.367` | Essential negative control: global path/action formulation is powerful, but the action phase is postulated and contains the physical dynamics. |
| PGH-R2-SRC-011 | Yakir Aharonov; Peter G. Bergmann; Joel L. Lebowitz | *Time Symmetry in the Quantum Process of Measurement* | 1964 | Primary physics article | SG2 | DOI `10.1103/PhysRev.134.B1410` | Demonstrates two-boundary/pre- and post-selected formulation; comparison case for global boundary data without ordinary one-way temporal specification. |
| PGH-R2-SRC-012 | Robert Oeckl | *A “General Boundary” Formulation for Quantum Mechanics and Quantum Gravity* | 2003 | Primary physics article | SG2 | DOI `10.1016/j.physletb.2003.08.043`; arXiv `hep-th/0306025` | Associates state spaces with arbitrary spacetime boundaries; reports structures emerging from consistency conditions in general-boundary formulation. |
| PGH-R2-SRC-013 | Robert Oeckl | *General Boundary Quantum Field Theory: Foundations and Probability Interpretation* | 2008 | Primary/foundational physics article | SG2 | DOI `10.4310/ATMP.2008.v12.n2.a3`; arXiv `hep-th/0509122` | Detailed axiomatic global-boundary framework; useful for distinguishing structural consistency axioms from theory-specific amplitudes/dynamics. |
| PGH-R2-SRC-014 | K. B. Wharton; N. Argaman | *Colloquium: Bell's Theorem and Locally Mediated Reformulations of Quantum Mechanics* | 2020 | Authoritative review | SG2 | DOI `10.1103/RevModPhys.92.021002` | Reviews models solved partly “all at once,” including future-boundary dependence; high-authority map of all-at-once physics and its open difficulties. |
| PGH-R2-SRC-015 | Emily Adlam | *Laws of Nature as Constraints* | 2022 | Peer-reviewed foundations article; reused canonical source | SG2 | DOI `10.1007/s10701-022-00546-0`; prior ID `PGH-LS-SRC-035` | Conceptual law-as-global/modal-constraint anchor; reused to bind new technical lane to prior landscape. |

## Lane coverage

```text
SG1_LOCAL_TO_GLOBAL_OBSTRUCTION = 9
SG2_GLOBAL_CONSTRAINT_FORMALISM = 6
MINIMUM_SG1 = PASS
MINIMUM_SG2 = PASS
```

## Freeze rule

This corpus is frozen for the subsequent PGH-1 mechanism adjudication. Later expansion requires a new concrete gap. A future operation may reinterpret scientific relevance but may not silently change this source set.
