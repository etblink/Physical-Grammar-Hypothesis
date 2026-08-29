# PGH-1 R2 Local-to-Global Mechanism Gate 0.1.0

## Identity

```text
OPERATION_ID = PGH1_R2_LOCAL_TO_GLOBAL_MECHANISM_GATE
REGISTRY_ID = PGH-OP-0034
CANONICAL_BASE = c60254f82bf2cca3628e2191e3968e622741197e
PREREGISTRATION_COMMIT = 630269b15ce39afe0332d5296311c88b5189271f
WORKING_TARGET = PGH-OBJ-0012
FORMAL_REFERENCE_BASELINE = PGH-GRAM-0002
FROZEN_NEW_SOURCE_COUNT = 15
NEW_SOURCE_SEARCH = NONE
FCP_EFFECT = NONE
```

## Outcome

```text
OUTCOME = B__LOCAL_TO_GLOBAL_OBSTRUCTION_IS_A_QUALIFIED_NON_TABLE_DRIVEN_FORMAL_MECHANISM_BUT_COVER_DOMAIN_AND_LOCAL_RULE_PRIVILEGE_REMAIN_UNEARNED

PGH-DER-0012 = ODD_CYCLE_LOCAL_TO_GLOBAL_OBSTRUCTION
PGH-FAIL-0014 = UNPRIVILEGED_LOCAL_GLOBAL_INPUT_SELECTION
SUCCESSOR_GRAMMAR_QUALIFIED = NO
R2_SATISFIED = NO
PHYSICAL_LAW_DERIVED = NO
```

The gate identifies a genuinely stronger formal exclusion mechanism than bare formation-table omission: one compact local rule can be satisfiable everywhere locally yet have no global realization because of the incidence/compatibility structure.

The gate does not identify the physically privileged cover, value domain, or local rule. Therefore no successor physical grammar is authorized.

---

## 1. Abstract local-to-global structure

Use the schema

\[
\mathcal L=(V,D,\mathcal C,\{R_C\}_{C\in\mathcal C}).
\]

A global realization is

\[
\operatorname{Glob}(\mathcal L)
=
\{g\in D^V:\forall C\in\mathcal C,\ g|_C\in R_C\}.
\]

The relevant obstruction is:

```text
EVERY_LOCAL_RELATION_NONEMPTY = YES
OVERLAP_SUPPORTS_COMPATIBLE = YES
GLOBAL_REALIZATION_SET = EMPTY
```

This is an extension/existence problem. It is not merely equality of alternative formal derivations.

That distinction is why the new mechanism is not reducible to the earlier parse-coherence result.

---

## 2. Locked M1 witness — odd cycle with one uniform rule

For odd `n=2k+1`, let:

```text
V = vertices of C_n
D = {0,1}
LOCAL_CONTEXTS = edges
RULE_ON_EVERY_EDGE = endpoint values differ
```

Equivalently:

\[
x_i\oplus x_{i+1}=1.
\]

### Local satisfiability

Each edge independently permits `(0,1)` and `(1,0)`.

```text
EVERY_EDGE_SATISFIABLE = PASS
```

### Overlap-support compatibility

Every edge relation projects to `{0,1}` on either endpoint. Adjacent edge supports therefore agree on their shared vertex.

```text
OVERLAP_SUPPORT_COMPATIBILITY = PASS
```

### Proper-subgraph control

Deleting any one edge produces a path. Fix one endpoint arbitrarily and alternate values along the path.

```text
EVERY_PROPER_PATH_CONTROL = SATISFIABLE
```

### Full-cycle obstruction

Summing all XOR equations modulo 2 makes every variable occur twice on the left, hence gives `0`. The odd number of right-hand ones sums to `1`.

Thus a global assignment would imply:

\[
0=1\pmod 2.
\]

Contradiction.

```text
ODD_CYCLE_GLOBAL_REALIZATION = NONE
```

This qualifies `PGH-DER-0012`.

---

## 3. Even-cycle control

For even cycle length, the same local rule closes consistently.

Exactly two alternating assignments exist.

Independent finite enumeration for cycle lengths `3` through `8` gives:

```text
C3 = 0 solutions
C4 = 2 solutions
C5 = 0 solutions
C6 = 2 solutions
C7 = 0 solutions
C8 = 2 solutions
```

Therefore the local inequality rule does not merely declare all cycles impossible. Global incidence matters.

```text
NONVACUOUS_MODEL_VARIATION = PASS
```

---

## 4. Non-table-driven exclusion test

The odd-cycle family is specified by:

```text
BINARY_DOMAIN
CYCLE_INCIDENCE
ONE_UNIFORM_EDGE_RULE
```

There is no table of forbidden global strings.

One parity theorem rules out every global assignment on every odd cycle in the family.

Compared with bare formation `F=S`, this yields a genuine compression of the exclusion mechanism.

```text
M2_NON_TABLE_DRIVEN_GLOBAL_EXCLUSION = PASS
M3_UNIFORM_LOCAL_RULE = PASS
```

This is the strongest new formal R2 mechanism obtained so far.

---

## 5. Representation controls

The same obstruction appears as:

### Graph coloring

An odd cycle is not 2-colorable.

### XOR constraint system

The equations

\[
x_i\oplus x_{i+1}=1
\]

have inconsistent total parity for odd `n`.

### Local/global extension

Each edge support is nonempty and has compatible endpoint projections, but no global assignment belongs to every edge support simultaneously.

The scientific content of the theorem is not tied to sheaf terminology.

```text
M4_MULTIPLE_REPRESENTATION_CONTROL = PASS
```

The source corpus further supplies sheaf, logical, graph, and hypergraph formalisms for physically important local/global obstruction phenomena, strengthening this representation-control result without selecting any one notation as fundamental.

---

## 6. Arbitrary-local-table control

If arbitrary local relations are allowed with arbitrary contexts, any target global admissible set `S subseteq D^V` can be encoded immediately by including context `V` and setting

\[
R_V=S.
\]

Thus:

```text
ARBITRARY_LOCAL_CONSTRAINT_SYSTEM = UNIVERSAL_TARGET_ENCODER
M5_ARBITRARY_LOCAL_TABLE_FAILURE_EXPOSED = PASS
```

A local-to-global vocabulary is not sufficient by itself. The anti-smuggling value comes only from compact, independently justified restrictions on the local-rule family and context-generation architecture.

---

## 7. Cover/topology selection control

The global result changes when the incidence structure changes while the local rule remains fixed:

```text
PATH = SATISFIABLE
EVEN_CYCLE = SATISFIABLE
ODD_CYCLE = UNSATISFIABLE
```

Therefore the cover/topology carries indispensable information.

Current PGH commitments do not derive which context incidence structures are physically admissible or privileged.

```text
PHYSICAL_PRIVILEGE_OF_COVER = UNESTABLISHED
```

Selecting a cover because it yields a desired known physical impossibility would be result-directed.

---

## 8. Domain and local-rule selection controls

The value domain `{0,1}` and the inequality relation are also inputs.

Nothing in accepted PGH science currently derives either.

```text
PHYSICAL_PRIVILEGE_OF_DOMAIN = UNESTABLISHED
PHYSICAL_PRIVILEGE_OF_LOCAL_RULE = UNESTABLISHED
```

The compactness of the rule does not by itself make it physically fundamental.

---

## 9. Physical-anchor firewall

The witness uses no empirical response table, probability kernel, known quantum prediction, or target measurement distribution.

The proof is purely formal.

```text
M7_PHYSICAL_BRIDGE_NOT_SMUGGLED = PASS
```

But that pass is deliberately limited: because no physical bridge is used, no physical exclusion credit can yet be assigned.

The law-free empirical anchor remains untouched.

---

## 10. Why the new source corpus matters

The frozen 15-source corpus establishes three points relevant to this gate:

1. extension/gluing obstruction is generic mathematics and is not intrinsically quantum;
2. mature physical contextuality/nonlocality work exhibits physically meaningful global-extension failures;
3. related obstruction structure has sheaf, logical, graph, and hypergraph presentations.

This supports local-to-global obstruction as a legitimate mechanism family to investigate.

It does not supply the missing physical privilege of the context cover or compatibility rules.

---

## 11. Acceptance-criteria result

```text
M1_FORMAL_LOCAL_TO_GLOBAL_OBSTRUCTION = PASS
M2_NON_TABLE_DRIVEN_GLOBAL_EXCLUSION = PASS
M3_UNIFORM_LOCAL_RULE = PASS
M4_MULTIPLE_REPRESENTATION_CONTROL = PASS
M5_ARBITRARY_LOCAL_TABLE_FAILURE_EXPOSED = PASS
M6_COVER_AND_RULE_PRIVILEGE_EXPLICITLY_UNRESOLVED = PASS
M7_PHYSICAL_BRIDGE_NOT_SMUGGLED = PASS
```

All gate criteria pass.

However, outcome C additionally requires that the cover/domain/local rule be independently justified from already accepted PGH inputs.

They are not.

Therefore outcome C is forbidden by the preregistration.

---

## 12. Outcome adjudication

```text
OUTCOME_A = REJECTED__MECHANISM_FORMALLY_WORKS
OUTCOME_B = SELECTED
OUTCOME_C = REJECTED__INPUT_PRIVILEGE_NOT_JUSTIFIED
OUTCOME_D = REJECTED__FROZEN_SOURCE_AND_FORMAL_SCOPE_ARE_SUFFICIENT
```

Final outcome:

```text
B__LOCAL_TO_GLOBAL_OBSTRUCTION_IS_A_QUALIFIED_NON_TABLE_DRIVEN_FORMAL_MECHANISM_BUT_COVER_DOMAIN_AND_LOCAL_RULE_PRIVILEGE_REMAIN_UNEARNED
```

---

## 13. R2 consequence

The project now has something it did not have at the end of PGH-0:

```text
QUALIFIED_NON_TABLE_DRIVEN_GLOBAL_EXCLUSION_MECHANISM = YES
```

But it still lacks:

```text
INDEPENDENT_ORIGIN_OF_LOCAL_CONTEXT_COVER
INDEPENDENT_ORIGIN_OF_LOCAL_VALUE_DOMAIN
INDEPENDENT_ORIGIN_OF_COMPATIBILITY_RULE
PHYSICAL_BRIDGE_FROM_FORMAL_OBSTRUCTION_TO_PHYSICAL_IMPOSSIBILITY
```

Thus:

```text
PGH-OBJ-0012 = REMAINS_PROVISIONAL
R2 = UNSATISFIED
SUCCESSOR_GRAMMAR = NONE
PHYSICAL_GRAMMAR_FOUND = NO
```

---

## 14. Next scientific burden

The next operation should not search for another obstruction theorem.

It should ask whether the **inputs to the obstruction mechanism** can themselves be generated from deeper, independently motivated PGH structure:

> Can a context cover and local compatibility relation be generated from the law-free empirical anchor plus a compact formation/extension principle, without choosing them because they reproduce a target global impossibility?

Recommended next operation:

```text
NEXT_RECOMMENDED_OPERATION = PGH1_R2_GENERATED_COVER_AND_COMPATIBILITY_ORIGIN_GATE
NEXT_OPERATION_AUTHORIZED = NO
```

---

## Final boundary

```text
PGH-DER-0012 = QUALIFIED_FORMAL_CANDIDATE_PENDING_PROJECT_LEAD_REVIEW
PGH-FAIL-0014 = FAILED_PRESERVED_CANDIDATE_PENDING_PROJECT_LEAD_REVIEW
LOCAL_TO_GLOBAL_MECHANISM = FORMALLY_QUALIFIED
NON_TABLE_DRIVEN_EXCLUSION = YES
SUCCESSOR_GRAMMAR = NONE
R2_SATISFIED = NO
PHYSICAL_LAW_DERIVED = NO
EMPIRICAL_PREDICTION = NONE
FCP_EFFECT = NONE
```
