# PGH Branch and Ref Lifecycle Policy 0.1.0

## Status

```text
POLICY_ID = PGH_BRANCH_AND_REF_LIFECYCLE_POLICY
VERSION = 0.1.0
STATUS = ACTIVE
```

## Purpose

This policy keeps repository history intelligible as PGH grows without accumulating permanent working branches.

## Canonical branch

```text
CANONICAL_BRANCH = main
```

`main` represents the accepted canonical PGH repository state.

## Working branches

Preferred namespaces:

```text
research/<bounded-operation>
maintenance/<bounded-operation>
audit/<bounded-operation>
```

A branch name records workflow purpose, not scientific status.

## Branch lifecycle

A typical bounded operation should:

1. verify fresh remote `main`;
2. create one working branch from the exact authorized baseline;
3. perform only the authorized changes;
4. qualify the candidate;
5. integrate non-force after independent review when required;
6. verify canonical integration;
7. remove the now-integrated redundant working branch when no unique provenance depends on it.

Integrated working branches do not need to accumulate indefinitely.

## Direct-main exception

For very small repository-opening or infrastructure bootstrapping operations, a separately authorized bounded fast-forward commit may be created directly on `main` when the exact pre-write baseline is independently verified and no review boundary requires a staging branch.

This exception should not become the default for substantive scientific work.

## Force policy

Default:

```text
FORCE_PUSH = FORBIDDEN
NON_FORCE_FAST_FORWARD = REQUIRED
```

History rewriting requires a separately explicit exceptional authorization.

## Tags

Tags should be rare.

Appropriate uses include genuinely durable milestones such as:

```text
milestone/pgh-0-complete
milestone/first-qualified-nontrivial-derivation
milestone/first-qualified-formal-grammar
```

Do not tag routine commits.

Do not use tags as a substitute for canonical artifacts.

## Archival preservation

If a branch carries historically unique provenance that would otherwise become difficult to recover, preservation by an explicit archival or milestone tag may be appropriate.

Do not create archival refs merely for symmetry.

## Remote race gate

Before every remote ref mutation:

```text
FRESHLY_VERIFY_REMOTE_MAIN
COMPARE_WITH_AUTHORIZED_BASELINE
STOP_ON_UNEXPECTED_DRIFT
```

Do not silently rebase an authorization onto a newer state.

## Publication identity

Git commit identities are provenance facts.

If future tooling uses content-equivalent publication mechanisms, the repository must preserve a clear mapping between qualified candidate identity and canonical publication identity.

No such relaxed publication policy is assumed merely by this document.

## Repository hygiene

Prefer:

```text
ONE_CANONICAL_MAIN
FEW_TEMPORARY_WORKING_BRANCHES
RARE_MEANINGFUL_TAGS
```

over permanent accumulation of integrated branches.
