// SPDX-License-Identifier: UNTITLED
pragma solidity ^0.8.0;

import "test/fuzzing/SampleContract.sol";

import "../utils/FuzzActors.sol";

contract FuzzStorageVariables is FuzzActors {
    // ==============================================================
    // FUZZING SUITE SETUP
    // ==============================================================

    address currentActor;
    bool _setActor = true;

    uint256 internal constant PRIME = 2147483647;
    uint256 internal constant SEED = 22;
    uint256 iteration = 1; // fuzzing iteration
    uint256 lastTimestamp;

    //==============================================================
    // REVERTS CONFIGURATION
    //==============================================================

    bool internal constant CATCH_REQUIRE_REVERT = true; // Set to false to ignore require()/revert()
    bool internal constant CATCH_EMPTY_REVERTS = true; // Set to true to allow empty return data

    // ==============================================================
    // CONTRACTS
    // ==============================================================

    SampleContract internal sampleContract;
}
