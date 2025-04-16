// SPDX-License-Identifier: UNTITLED
pragma solidity ^0.8.0;

import "./utils/FunctionCalls.sol";

contract FuzzSetup is FunctionCalls {
    function fuzzSetup() internal {
        deploySampleContract();
        labelAll();
    }

    function deploySampleContract() internal {
        sampleContract = new SampleContract();
    }

    //DO LABELING
    function labelAll() internal {
        //CONTRACTS
        vm.label(address(sampleContract), "SampleContract");

        //USERS
        vm.label(USER1, "USER1");
        vm.label(USER2, "USER2");
        vm.label(USER3, "USER3");
    }
}
