// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@perimetersec/fuzzlib/src/FuzzBase.sol";
import "../helpers/FuzzStorageVariables.sol";

contract FunctionCalls is FuzzBase, FuzzStorageVariables {
    event SampleFunctionCall(uint256 sampleInput);

    function _sampleFunctionCall(uint256 sampleInput) internal returns (bool success, bytes memory returnData) {
        emit SampleFunctionCall(sampleInput);

        vm.prank(currentActor);
        (success, returnData) =
            address(sampleContract).call(abi.encodeWithSelector(SampleContract.sampleFunction.selector, sampleInput));
    }

    function _sampleFailWithRequireCall(bool sampleInput) internal returns (bool success, bytes memory returnData) {
        vm.prank(currentActor);
        (success, returnData) = address(sampleContract).call(
            abi.encodeWithSelector(SampleContract.sampleFailWithRequire.selector, sampleInput)
        );
    }

    function _sampleFailWithCustomErrorCall(uint8 sampleInput)
        internal
        returns (bool success, bytes memory returnData)
    {
        vm.prank(currentActor);
        (success, returnData) = address(sampleContract).call(
            abi.encodeWithSelector(SampleContract.sampleFailWithCustomError.selector, sampleInput)
        );
    }

    function _sampleFailWithPanicCall(uint256 sampleInput) internal returns (bool success, bytes memory returnData) {
        vm.prank(currentActor);
        (success, returnData) = address(sampleContract).call(
            abi.encodeWithSelector(SampleContract.sampleFailWithPanic.selector, sampleInput)
        );
    }

    function _sampleFailWithAssertCall(uint256 sampleInput) internal returns (bool success, bytes memory returnData) {
        vm.prank(currentActor);
        (success, returnData) = address(sampleContract).call(
            abi.encodeWithSelector(SampleContract.sampleFailWithAssert.selector, sampleInput)
        );
    }

    function _sampleFailReturnEmptyDataCall(bool sampleInput)
        internal
        returns (bool success, bytes memory returnData)
    {
        vm.prank(currentActor);
        (success, returnData) = address(sampleContract).call(
            abi.encodeWithSelector(SampleContract.sampleFailReturnEmptyData.selector, sampleInput)
        );
    }
}
