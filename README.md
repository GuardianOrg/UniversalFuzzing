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

#NOTES:

- RevertHandler has separate check for a 4 bytest returnData and detirects it to solady errors check, while the check for the protocol errors is in the end of the function. Not all protcol behaves like this, eg. `Ethereal` has a special sol file with listed errors, that outputs 4 bytes returnData. For this cases redirect 4 bytes errors check.
