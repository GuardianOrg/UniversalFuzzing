## Echidna fuzzing template

### Use Echidna

    echidna test/fuzzing/Fuzz.sol --contract Fuzz --config echidna.yaml

### Use Foundry

    forge test --mp FoundryFuzz.sol

### Use Foundry for repros

    forge test --mp FoundryPlayground.sol -vvvv

## Initial Cursor prompt with reference

```
@referenceContracts @fuzzing Using reference contracts, create handlers for SampleContract.complexFunction usage in FuzzSampleContract, appropriately filling in pre and post conditions.
```
