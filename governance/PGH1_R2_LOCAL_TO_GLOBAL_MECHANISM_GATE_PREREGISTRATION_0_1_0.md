# PGH-1 R2 Local-to-Global Mechanism Gate — Preregistration 0.1.0

## Identity

```text
OPERATION_ID = PGH1_R2_LOCAL_TO_GLOBAL_MECHANISM_GATE
REGISTRY_ID = PGH-OP-0034
CANONICAL_BASE = c60254f82bf2cca3628e2191e3968e622741197e
WORKING_TARGET = PGH-OBJ-0012
FORMAL_REFERENCE_BASELINE = PGH-GRAM-0002
FROZEN_NEW_SOURCE_CORPUS = sources/PGH1_R2_LOCAL_GLOBAL_SOURCE_REGISTER_0_1_0.md
FROZEN_NEW_SOURCE_COUNT = 15
NEW_SOURCE_SEARCH = FORBIDDEN
SUCCESSOR_GRAMMAR_SELECTION = FORBIDDEN_UNLESS_OUTCOME_C
FCP_EFFECT = NONE
```

## Purpose

Test whether local-to-global compatibility obstruction is a genuinely different non-table-driven exclusion mechanism for anchored R2, while exposing exactly which inputs remain freely chosen and therefore cannot yet receive physical-law credit.

The gate tests the **mechanism**, not sheaf theory as a preferred representation.

## Abstract structure

Use a finite variable set `V`, a finite value set `D`, a family of local contexts `C_i subseteq V`, and one or more compact local admissibility rules.

A global assignment is admissible only when its restriction to every local context satisfies the corresponding local rule.

The key question is whether:

```text
EVERY_LOCAL_CONTEXT_HAS_ADMISSIBLE_ASSIGNMENTS
AND
OVERLAP_PROJECTIONS_ARE_LOCALLY_COMPATIBLE
BUT
NO_GLOBAL_ASSIGNMENT_EXISTS
```

can arise from a compact uniform rule rather than an extensional forbidden-global table.

## Locked witness family M1 — odd-cycle binary inequality

For each odd cycle `C_(2k+1)`:

```text
V = cycle vertices
D = {0,1}
LOCAL_CONTEXTS = graph edges
UNIFORM_LOCAL_RULE = endpoint values must differ
```

Required checks:

1. every edge constraint is individually satisfiable;
2. every proper path subgraph is globally satisfiable;
3. the full odd cycle has no global satisfying assignment;
4. the impossibility is derived by parity/alternation around the cycle rather than by enumerating forbidden global strings.

## Representation controls

The same obstruction must be expressible without scientific dependence on one notation:

```text
R1_GRAPH_COLORING = 2-colorability of an odd cycle
R2_XOR_CONSTRAINTS = x_u XOR x_v = 1 on each edge
R3_LOCAL_GLOBAL_EXTENSION = local edge assignments have no global binary assignment satisfying all supports
```

No claim of full categorical/sheaf equivalence is required. The gate tests that the core obstruction survives obvious faithful reformulation.

## No-smuggling controls

### C1 — arbitrary local tables

If arbitrary local relations may be chosen independently, a target global exclusion can still be encoded. Such systems receive no special PGH credit.

### C2 — uniform-rule control

The odd-cycle witness uses the **same** local inequality rule on every edge. The global failure must arise from topology/cover structure plus the uniform rule.

### C3 — cover-selection control

The graph/cover itself remains input. The gate must explicitly test whether a freely chosen cover can encode the target impossibility.

### C4 — domain/rule-selection control

The binary value domain and inequality relation remain input. Their physical status may not be inferred from the formal theorem.

### C5 — anchor firewall

No response values, probabilities, known quantum predictions, or empirical target partition may be used to choose the witness or prove the obstruction.

## R2 acceptance criteria

```text
M1_FORMAL_LOCAL_TO_GLOBAL_OBSTRUCTION = required
M2_NON_TABLE_DRIVEN_GLOBAL_EXCLUSION = required
M3_UNIFORM_LOCAL_RULE = required
M4_MULTIPLE_REPRESENTATION_CONTROL = required
M5_ARBITRARY_LOCAL_TABLE_FAILURE_EXPOSED = required
M6_COVER_AND_RULE_PRIVILEGE_EXPLICITLY_UNRESOLVED = required
M7_PHYSICAL_BRIDGE_NOT_SMUGGLED = required
```

## Outcome space

```text
A = LOCAL_TO_GLOBAL_MECHANISM_FAILS_EVEN_AS_A_DISTINCT_FORMAL_EXCLUSION
B = MECHANISM_IS_QUALIFIED_FORMALLY_AND_NON_TABLE_DRIVEN_BUT_COVER_RULE_DOMAIN_PRIVILEGE_REMAINS_UNEARNED
C = MECHANISM_PLUS_ALREADY_JUSTIFIED_PGH_INPUTS_QUALIFIES_A_PROVISIONAL_SUCCESSOR_GRAMMAR_FOR_R2_TESTING
D = FROZEN_SOURCE_OR_FORMAL_SCOPE_IS_INSUFFICIENT
```

Outcome C requires more than the odd-cycle theorem. It requires that the candidate grammar inputs themselves be independently justified from already accepted PGH commitments. No such justification may be invented during the gate.

## Required outputs

Commit 2 may add only:

```text
audits/PGH1_R2_LOCAL_TO_GLOBAL_MECHANISM_GATE_0_1_0.md
research/formalizations/PGH1_LOCAL_TO_GLOBAL_CONSTRAINT_SCHEMA_0_1_0.md
research/derivations/PGH_DERIVATION_ODD_CYCLE_LOCAL_GLOBAL_OBSTRUCTION_0_1_0.md
research/failures/PGH_FAIL_UNPRIVILEGED_LOCAL_GLOBAL_INPUT_SELECTION_0_1_0.md
handoffs/PGH1_R2_LOCAL_TO_GLOBAL_MECHANISM_GATE_HANDOFF_0_1_0.md
```

## Commit topology

```text
COMMIT_1_MESSAGE = Preregister PGH-1 R2 local-to-global mechanism gate
COMMIT_2_MESSAGE = Adjudicate PGH-1 R2 local-to-global mechanism gate
EXACT_COMMITS = 2
```

## Hard stops

```text
DO_NOT_CALL_CONTEXTUALITY_THE_PGH_GRAMMAR
DO_NOT_SELECT_SHEAF_THEORY_AS_FUNDAMENTAL
DO_NOT_IMPORT_QUANTUM_PROBABILITIES
DO_NOT_TREAT_GRAPH_CHOICE_AS_PHYSICALLY_PRIVILEGED
DO_NOT_CREATE_A_PHYSICAL_BRIDGE_BY_ASSERTION
DO_NOT_CHANGE_FCP
```
