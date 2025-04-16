// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./FuzzGuided.sol";

contract FoundryPlayground is FuzzGuided {
    function setUp() public {
        vm.warp(1524785992); //echidna starting time
        fuzzSetup();
    }

    function test_coverage_SampleFunction() public {
        fuzz_sampleFunction(1);
    }

    function test_repro_INV_01() public {
        fuzz_sampleFunction(1);
        fuzz_sampleFunction(2);
    }

    function test_repro_ERR_01_01() public {
        //fail with require
        fuzz_sampleFailWithRequire(true);
    }

    function test_repro_ERR_01_02() public {
        //fail with custom error
        fuzz_sampleFailWithCustomError(1);
    }

    function test_repro_ERR_01_03() public {
        //fail with panic
        fuzz_sampleFailWithPanic(1);
    }

    function test_repro_ERR_01_04() public {
        //fail with assert
        fuzz_sampleFailWithAssert(1);
    }

    function test_repro_ERR_01_05() public {
        //fail with empty revert
        fuzz_sampleFailReturnEmptyData(true);
    }
}
