# PGH-1 Post-Kp HURDAT2 Five-Candidate Analysis and Custody Preregistration Gate — Audit 0.1.0

```text
OPERATION_ID = PGH1_POST_KP_HURDAT2_FIVE_CANDIDATE_ANALYSIS_AND_CUSTODY_PREREGISTRATION_GATE
REGISTRY_ID = PGH-OP-0088
PREREGISTRATION_COMMIT = 2580fe334a7239f1833167708d8914b43cb07857
OUTCOME = A__COMPLETE_TARGET_SPECIFIC_PROTOCOL_AND_REFERENCE_IMPLEMENTATION_QUALIFY_PRE_DATA
NEW_OBJECT = PGH-OBJ-0049
REAL_DATA_ACCESSED = NO
FCP_EFFECT = NONE
```

## Qualification finding

The target-specific five-candidate protocol can be made fully executable without inspecting Atlantic HURDAT2 event values and without introducing a new unfrozen scientific choice.

The result binds:

- exact target parser and support semantics;
- five frozen `G2` statistics;
- CAL1 with 4999 candidate-specific fixed-margin randomizations;
- CAL2 with 1999 candidate-null storm/run-preserving block-process bootstraps;
- separate Holm familywise correction at alpha 0.01;
- exact candidate/family verdict mappings;
- complete stochastic implementation semantics;
- synthetic-only executable qualification.

## Reference implementation qualification

Reconstruction from the frozen preregistration was performed after the previous uncommitted working copy did not persist across a chat-turn boundary. This did not alter the scientific method; the preregistration explicitly permits implementation-bug repair/reconstruction before data access provided the frozen statistic/calibration/verdict method is unchanged.

Local qualification environment:

```text
COMPILER = g++ (Debian 14.2.0-19) 14.2.0
BUILD = -std=c++20 -O2 -Wall -Wextra -pedantic -Werror
PLATFORM = Linux x86_64
SOURCE_SHA256 = 1b7fcd8e1958d5614a73cdb2226465bb41f355fbc2d7c3e6769b1f8f488682d4
SELF_TEST = PASS
STD_RANDOM_DISTRIBUTION_USE = NONE_FOUND
REAL_HURDAT2_BYTES = NOT_ACCESSED
```

A separate unintegrated GitHub validation branch must compile the exact committed source and run `--self-test` before canonical integration. That validation history is transport/qualification history only and must not enter the two-commit scientific candidate.

## Scientific limitations retained

CAL1 does not claim exact validity under arbitrary serial/storm clustering. CAL2 is a deliberately model-dependent process calibration and does not claim to span all possible cyclone dynamics. Requiring both corrected calibrations to reject preserves this limitation rather than hiding it.

A one-target survival is not confirmation of strong PGH, a unique fundamental grammar, or R2B.

## Boundary

```text
RAW_DOWNLOAD = NOT_PERFORMED
RAW_HASH = NONE
MASTER_SEED = NONE
REAL_PARSE = NOT_PERFORMED
REAL_G2 = NONE
MONTE_CARLO = NOT_PERFORMED
CANDIDATE_VERDICT = NONE
```

The next operation may perform bounded raw-data custody and parser/support qualification only after canonical integration and navigation reconciliation.
