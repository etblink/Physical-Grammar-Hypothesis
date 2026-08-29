# PGH-1 Coproduct Bridge Physical Meaning Firewall Schema 0.1.0

## Identity

```text
OBJECT_ID = PGH-OBJ-0029
OBJECT_CLASS = SEMANTIC_BRIDGE_FIREWALL_SCHEMA
STATUS = PROVISIONAL_LAW_FREE_SEMANTIC_BRIDGE_ROLE
PARENT_BRIDGE = PGH-OBJ-0028
TYPED_ANCHOR = PGH-OBJ-0025
PHYSICAL_LAW_STATUS = NONE
```

## Formal candidate

For a context `c` with typed record fiber `R_c`, let

\[
O_c=\coprod_{r\in R_c}Y_r
\]

and

\[
n_c:X_c\to O_c.
\]

No component arrow `X_c -> Y_r` is assumed or forced.

## Four semantic readings

### S0 — syntactic only

`n_c` is only a formal generator.

```text
EMPIRICAL_ROLE = NONE
RESPONSE_LAW = NONE
```

### S1 — law-free process role

`n_c` is designated as a generic empirical process/interface from context `c` into the typed record carrier `O_c`.

The designation fixes only:

```text
SOURCE_ROLE = EMPIRICAL_CONTEXT
TARGET_ROLE = TYPED_RECORD_CARRIER
CROSS_TYPE_PROCESS_ROLE_EXISTS = YES
```

It does not fix:

```text
RESPONSE_MAP
ALLOWED_RESPONSE_SUPPORT
RESPONSE_PROBABILITIES
SUMMAND_AS_ACTUAL_OUTCOME
```

S1 is admissible only while compatible with at least two incompatible response realizations.

### S2 — concrete response reading

A chosen interpretation of `n_c` is read as the actual deterministic, relational, or stochastic response process.

At this level the interpretation can be pushed forward along the coproduct tags to extract response data.

Those data are model/semantic inputs unless constrained by the abstract grammar.

### S3 — empirical fit

A concrete interpretation is selected because it matches observations.

```text
S3 = FORBIDDEN_FOR_GRAMMAR_DERIVED_EXPLANATORY_CREDIT
```

## Law-free criterion

S1 is law-free at this scope only if the exact same semantic role and typed anchor admit at least two incompatible response models.

The gate witness supplies two deterministic Set interpretations of one abstract bridge generator that yield different record-label maps.

Therefore:

```text
S1_UNDERDETERMINES_RESPONSE = YES
S1_IS_COMPLETE_PHYSICAL_BRIDGE = NO
```

## Explanatory-credit rule

If a response map, support, or distribution is obtained only after choosing a concrete interpretation of `n_c`, then that response structure cannot be credited to the abstract grammar unless a later theorem shows that every admissible interpretation satisfies the same nontrivial restriction.

## Next burden

The live R2B test is model-class invariance/constraint:

\[
\text{bridge-enriched grammar}\quad\stackrel{?}{\Longrightarrow}\quad\text{nontrivial response restriction across admissible models}.
\]

## Nonclaims

```text
COPRODUCT_IS_PHYSICAL_ALTERNATIVE = NO
MORPHISM_IS_PHYSICAL_RESPONSE = NO
SUMMAND_TAG_IS_ACTUAL_OUTCOME = NO
MINIMAL_PROCESS_ROLE_IS_FULL_RESPONSE_LAW = NO
R2B = UNSATISFIED
EMPIRICAL_PREDICTION = NONE
```
