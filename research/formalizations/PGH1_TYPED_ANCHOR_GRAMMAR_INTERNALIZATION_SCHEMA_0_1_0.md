# PGH-1 Typed Anchor Grammar Internalization Schema 0.1.0

## Status

```text
OBJECT_ID = PGH-OBJ-0026
OBJECT_CLASS = BRIDGE_INTERNALIZATION_SCHEMA
STATUS = PROVISIONAL_FORMAL_SCHEMA
PHYSICAL_STATUS = UNESTABLISHED
R2B = UNSATISFIED
```

## Purpose

Separate law-free typed semantic metadata from the additional formal choices required to make that metadata participate in a candidate grammar.

## Four layers

A typed anchor/grammar bridge must distinguish:

```text
L1 = TYPED_SEMANTIC_METADATA
L2 = ANCHOR_TO_GRAMMAR_INTERNALIZATION
L3 = GRAMMAR_GENERATED_CONSEQUENCES
L4 = PHYSICAL_RESPONSE_INTERPRETATION
```

No explanatory credit may be moved silently from one layer to another.

## External metadata

Let

\[
T\subseteq C\times R
\]

be a response-underdetermining typed interface satisfying `PGH-OBJ-0025`.

If `T` is not represented in the signature, generators, equations, objects, typing judgments, or other syntax of a candidate grammar `G`, then the free grammar construction is unchanged.

External metadata can guide an analyst's reading of the formalism, but it cannot alter grammar derivability by itself.

## Internalization maps

An internalization map `I` specifies how typed semantic structure enters the grammar presentation.

The locked controls include:

1. **edge internalization**
   \[
   (c,r)\in T\mapsto e_{c,r}:X_c\to Y_r;
   \]
2. **product-output packaging**
   \[
   R_c=\{r_0,r_1\},\quad m_c:X_c\to Y_{r_0}\times Y_{r_1};
   \]
3. **coproduct-output generic process**
   \[
   R_c=\{r_0,r_1\},\quad n_c:X_c\to Y_{r_0}+Y_{r_1}.
   \]

These are distinct presentations, but their information content must be audited rather than inferred from surface compactness.

## Product packaging warning

In a category with products,

\[
\operatorname{Hom}(X,Y_0\times Y_1)
\cong
\operatorname{Hom}(X,Y_0)\times\operatorname{Hom}(X,Y_1).
\]

Therefore one primitive morphism

\[
m:X\to Y_0\times Y_1
\]

is equivalent formal data to a pair of component morphisms

\[
X\to Y_0,\qquad X\to Y_1.
\]

It does not earn compression or derivational credit merely because the pair is packaged through a product object.

## Coproduct contrast

A primitive morphism

\[
n:X\to Y_0+Y_1
\]

is not, in general, equivalent to choosing either component morphism `X->Y_i`. A coproduct supplies injections from its summands, not canonical projections to them.

Thus it can represent a generic process with a typed aggregate codomain while leaving component-level arrows underdetermined.

This remains additional primitive bridge structure, not a grammar consequence of `T` alone.

## Internalization is not automatically response law

A generic process with typed aggregate codomain can remain weaker than specifying which record response occurs.

However, the internalization is substantive formal structure. It must be preregistered and audited independently of downstream consequences.

```text
GENERIC_TYPED_PROCESS = NOT_AUTOMATICALLY_RESPONSE_LAW
GENERIC_TYPED_PROCESS = NOT_AUTOMATICALLY_EXPLANATORILY_FREE
PRODUCT_PACKAGING = NOT_COMPRESSION_OF_COMPONENT_EDGE_DATA
```

## Canonicality burden

A candidate internalization receives explanatory credit only if its choice is fixed before target response evaluation and passes an anti-encoding audit.

A convenient embedding cannot be promoted because it produces desired morphisms.

## Representation-role burden

Treating a context as any of the following is itself part of `I`:

```text
ATOMIC_OBJECT
PROCESS_SOURCE
PROCESS_WITH_TYPED_CODOMAIN
INDEX_FOR_A_FAMILY_OF_OBJECTS_OR_PROCESSES
OTHER_INTERFACE_STRUCTURE
```

No one role is currently fundamental by canonical PGH result.

## Physical ceiling

```text
LAW_FREE_TYPED_METADATA = AVAILABLE
CANONICAL_INTERNALIZATION = NOT_FOUND
GRAMMAR_GENERATED_CROSS_TYPE_STRUCTURE = INTERNALIZATION_DEPENDENT
MORPHISM_AS_RESPONSE = UNESTABLISHED
R2B = UNSATISFIED
PHYSICAL_LAW_DERIVED = NO
```