# PGH-1 Post-Kp Common-Target Multi-Candidate Multiplicity Protocol Gate 0.1.0

## Identity

```text
OPERATION_ID = PGH1_POST_KP_COMMON_TARGET_MULTI_CANDIDATE_MULTIPLICITY_PROTOCOL_GATE
REGISTRY_ID = PGH-OP-0084
CANONICAL_BASE = 39aab2317246fe64eae1e57f86d1b9f72a34dfa3
PREREGISTRATION_COMMIT = 3517dcfd9aef3eaec78b82020d07a9654c40853a
NEW_OBJECT = PGH-OBJ-0047
```

## Outcome

```text
OUTCOME = A__COMMON_TARGET_FIVE_CANDIDATE_MULTIPLICITY_PROTOCOL_QUALIFIES__TARGET_DISCOVERY_MAY_BE_SEPARATELY_OPENED
TARGET = NONE
TARGET_DISCOVERY_EXECUTED = NO
FAMILY_SIZE = 5
FAMILY_ALPHA = 0.01
MULTIPLICITY = HOLM_STEP_DOWN_SEPARATELY_FOR_TWO_CALIBRATIONS
FCP_EFFECT = NONE
```

## Why the protocol qualifies

The five candidates share one empirical interface, so candidate-specific targets are unnecessary. One common target is both more efficient and less vulnerable to target shopping.

Holm's procedure controls familywise false refutation across the five candidate nulls without requiring their p-values to be independent. Applying it separately to two preregistered calibration architectures preserves the project's existing calibration-disagreement firewall.

## Why two calibrations remain necessary

The Kp test showed that null-model implementation choices can move finite-sample reference distributions even when the qualitative verdict is robust. The new standard therefore requires not only two conceptually distinct calibrations but exact stochastic semantics before data materialization.

## Why pre-Kp discovered targets are quarantined

The post-Kp successor packages did not exist before the old target-discovery program. Even an old target whose dependence values were never inspected was identified before the successor freeze.

Using such a target as the first positive successor result would violate the newly qualified ordering:

```text
CANDIDATE_FREEZE -> TARGET_DISCOVERY
```

Therefore all targets in the old discovery ledger are excluded from first positive successor credit.

This does not claim those targets are scientifically contaminated forever; it limits their evidential role for this successor family's first prospective test.

## Why nonrejection is not confirmation

The primary tests have candidate-predicted independence as their null. Failure to reject can reflect exact independence, small effect, limited power or calibration breadth. The family protocol therefore uses `SURVIVES_COMMON_TARGET_TEST`, never `CONFIRMED`.

A unique survivor would be a relative discriminator only and would require a later new target before stronger credit.

## Why no target-specific null is frozen yet

Autocorrelation, segmentation, phase structure, repeated-measure architecture and missingness are properties of the future target's metadata. Choosing their preservation rules before a target exists would either be meaningless or covertly constrain target selection.

The protocol instead freezes the two-calibration architecture and requires the exact target-specific nulls to be preregistered after target freeze but before data access.

## Next operation

```text
NEXT_RECOMMENDED_OPERATION = PGH1_POST_KP_COMMON_TARGET_MULTI_CANDIDATE_TARGET_DISCOVERY_AND_FREEZE
NEXT_OPERATION_AUTHORIZED = NO
```

That operation must search metadata only, bind and exclude the entire old target-discovery ledger, select exactly one new target for all five candidates, freeze the target/role mapping, and stop before inspecting dependence values or constructing target-specific statistical nulls.

## Stop verification

```text
TARGET_SEARCH = NO
TARGET_METADATA = NONE
TARGET = NONE
EMPIRICAL_DATA = NONE
NEW_SOURCE_SEARCH = NO
FCP_CHANGED = NO
```
