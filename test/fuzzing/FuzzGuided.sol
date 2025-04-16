// SPDX-License-Identifier: UNTITLED
pragma solidity ^0.8.0;

import "./FuzzSampleContract.sol";

contract FuzzGuided is FuzzSampleContract {
    function fuzz_guided_sampleFunctionCallTwice(uint256 sampleInput, uint256 sampleInput2) public setCurrentActor {
        fuzz_sampleFunction(sampleInput);
        fuzz_sampleFunction(sampleInput2);
    }
}
