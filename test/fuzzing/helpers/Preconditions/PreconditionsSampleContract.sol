// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./PreconditionsBase.sol";

contract PreconditionsSampleContract is PreconditionsBase {
    function sampleFunctionPreconditions(uint256 sampleInput) internal returns (SampleFunctionParams memory params) {
        params.sampleUint = fl.clamp(sampleInput, 0, 100);
    }

    function sampleFailWithRequirePreconditions(bool sampleInput)
        internal
        returns (SampleFailWithRequireParams memory params)
    {
        params.sampleUint = sampleInput;
    }

    function sampleFailWithCustomErrorPreconditions(uint8 sampleNum)
        internal
        returns (SampleFailWithCustomErrorParams memory params)
    {
        params.sampleUint = sampleNum;
    }

    function sampleFailWithPanicPreconditions(uint256 sampleInput)
        internal
        returns (SampleFailWithPanicParams memory params)
    {
        params.sampleUint = fl.clamp(sampleInput, 0, 8);
    }

    function sampleFailWithAssertPreconditions(uint256 sampleInput)
        internal
        returns (SampleFailWithAssertParams memory params)
    {
        params.sampleUint = sampleInput;
    }

    function sampleFailReturnEmptyDataPreconditions(bool sampleInput)
        internal
        returns (SampleFailReturnEmptyDataParams memory params)
    {
        params.sampleUint = sampleInput;
    }
}
