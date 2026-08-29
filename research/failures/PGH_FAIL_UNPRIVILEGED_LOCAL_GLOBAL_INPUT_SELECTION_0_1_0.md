# PGH-FAIL-0014 — Unprivileged Local-to-Global Input Selection 0.1.0

## Identity

```text
FAILURE_ID = PGH-FAIL-0014
OPERATION_ID = PGH1_R2_LOCAL_TO_GLOBAL_MECHANISM_GATE
STATUS = FAILED_PRESERVED_CANDIDATE_PENDING_PROJECT_LEAD_REVIEW
FAILURE_CLASS = PHYSICS_SMUGGLED_OR_TARGET_STRUCTURE_RELOCATED
PHYSICAL_CLAIM = NONE
```

## Failed promotion

The following inference is not justified:

> Because a compact local-to-global consistency system can derive a global impossibility without listing forbidden global assignments, the chosen local contexts, value domain, and compatibility rule therefore constitute a physically privileged grammar.

The formal mechanism is real. The physical promotion fails.

## 1. Arbitrary local tables remain universal target encoders

Let `V` be a finite global variable set, `D` a finite domain, and let any desired global admissible set be

\[
S\subseteq D^V.
\]

If arbitrary contexts and arbitrary local relations are permitted, simply include the global context `V` itself and define

\[
R_V=S.
\]

Then the global realization set is exactly

\[
\operatorname{Glob}(\mathcal L)=S.
\]

Thus unrestricted local-constraint presentations can encode any target possibility set extensionally.

Even if only proper subcontexts are allowed, sufficiently tailored local relations can still encode large amounts of target structure. Therefore:

```text
LOCAL_CONSTRAINT_LANGUAGE_ALONE = NOT_A_NONARBITRARY_GRAMMAR
```

## 2. Why the uniform odd-cycle witness is better

The odd-cycle witness avoids that simplest failure mode.

It uses:

```text
ONE_VALUE_DOMAIN = {0,1}
ONE_LOCAL_RULE = endpoints differ
ONE_UNIFORM_CONTEXT_TYPE = graph edge
```

and applies exactly the same rule on every edge.

No global bit string is named forbidden. The impossibility follows only after the local rule is composed around an odd cycle.

Therefore the witness earns:

```text
NON_TABLE_DRIVEN_EXCLUSION = YES
UNIFORM_LOCAL_RULE = YES
GLOBAL_OBSTRUCTION_DERIVED = YES
```

This is a genuine improvement over bare formation-table exclusion.

## 3. Cover/topology privilege remains external

However, the same local rule behaves differently on different incidence structures:

```text
ODD_CYCLE -> NO_GLOBAL_ASSIGNMENT
EVEN_CYCLE -> TWO_GLOBAL_ASSIGNMENTS
PATH -> GLOBAL_ASSIGNMENTS_EXIST
```

Hence the global exclusion depends essentially on the chosen cover/topology.

Nothing in currently accepted PGH commitments selects odd-cycle incidence, graph incidence generally, or any particular local-context cover as physically privileged.

Choosing the cover because it yields the desired impossibility would be result-directed.

```text
PHYSICAL_PRIVILEGE_OF_COVER = UNESTABLISHED
```

## 4. Domain privilege remains external

The binary domain `{0,1}` is part of the theorem's input.

The theorem does not derive:

```text
PHYSICAL_OUTCOMES_ARE_BINARY
PHYSICAL_PROPERTIES_HAVE_TWO_VALUES
BINARY_DOMAIN_IS_FUNDAMENTAL
```

A different domain can change the satisfiability problem. Therefore:

```text
PHYSICAL_PRIVILEGE_OF_VALUE_DOMAIN = UNESTABLISHED
```

## 5. Local-rule privilege remains external

The inequality relation

\[
x_u\neq x_v
\]

is compact and uniform, but it remains an input.

Current PGH does not derive why physical adjacency or contextual overlap, if any, should obey inequality rather than equality, parity, order, compatibility, probabilistic consistency, or another rule.

If the rule is chosen because its closure reproduces a known physical no-go theorem, the target law has been imported indirectly.

```text
PHYSICAL_PRIVILEGE_OF_LOCAL_RULE = UNESTABLISHED
```

## 6. Representation invariance does not repair input privilege

The same obstruction can be presented as:

```text
ODD_CYCLE_NOT_2_COLORABLE
INCONSISTENT_XOR_PARITY_SYSTEM
NO_GLOBAL_EXTENSION_OF_LOCAL_SUPPORTS
```

This is useful representation robustness.

But agreement across representations does not explain why the represented structure is the physically correct one. The PGH-0 distinction survives:

```text
REPRESENTATION_ROBUSTNESS != PHYSICAL_PRIVILEGE
```

## 7. Contextuality is a comparison case, not a shortcut

The frozen source corpus shows mature physical situations in which compatible local empirical models lack a global noncontextual realization.

PGH may use this as evidence that local-to-global obstruction is a physically meaningful **kind of mechanism**.

It may not infer:

```text
QUANTUM_CONTEXTUALITY = FUNDAMENTAL_PGH_GRAMMAR
EMPIRICAL_MODEL_COVER = PRIMITIVE_GRAMMAR_COVER
KNOWN_CONTEXTUALITY_SUPPORTS = GRAMMAR_DERIVED
```

Doing so would use the already known physical scenario to select the grammar inputs.

## 8. Failure verdict

```text
PGH-FAIL-0014 = UNPRIVILEGED_LOCAL_GLOBAL_INPUT_SELECTION
STATUS = FAILED_PRESERVED_CANDIDATE_PENDING_REVIEW

LOCAL_TO_GLOBAL_MECHANISM = FORMALLY_DISTINCT_AND_USEFUL
LOCAL_TO_GLOBAL_INPUTS = NOT_YET_PHYSICALLY_JUSTIFIED
SUCCESSOR_GRAMMAR_QUALIFIED = NO
R2_SATISFIED = NO
```

## Assumption ancestry

```text
PRIMITIVE_DEPENDENCIES = LOCAL_CONSTRAINT_SCHEMA
RULE_DEPENDENCIES = NONE_BEYOND_FAILURE_CONTROLS
SEMANTIC_ASSUMPTIONS = NONE
PHYSICAL_ASSUMPTIONS = NONE
SOURCE_DEPENDENCIES = PGH-R2-SRC-001; PGH-R2-SRC-002; PGH-R2-SRC-003; PGH-R2-SRC-004; PGH-R2-SRC-008; PGH-R2-SRC-009
```

## Next burden exposed

The next scientifically legitimate question is not whether another local-to-global obstruction can be found. It is:

> Can the local-context cover and compatibility rule themselves arise from a deeper, compact, independently motivated grammar construction tied only to the law-free empirical anchor, rather than being selected because they reproduce a target physical impossibility?
