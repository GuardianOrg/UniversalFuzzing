// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./helpers/preconditions/PreconditionsSampleContract.sol";
import "./helpers/postconditions/PostconditionsSampleContract.sol";

contract FuzzSampleContract is PreconditionsSampleContract, PostconditionsSampleContract {
    function fuzz_sampleFunction(uint256 sampleInput) public setCurrentActor {
        SampleFunctionParams memory params = sampleFunctionPreconditions(sampleInput);

        address[] memory actorsToUpdate = new address[](1);
        actorsToUpdate[0] = currentActor;
        _before(actorsToUpdate);

        (bool success, bytes memory returnData) = _sampleFunctionCall(params.sampleUint);

        sampleFunctionPostconditions(success, returnData, actorsToUpdate);
    }

    function fuzz_sampleFailWithRequire(bool sampleInput) public setCurrentActor {
        SampleFailWithRequireParams memory params = sampleFailWithRequirePreconditions(sampleInput);

        address[] memory actorsToUpdate = new address[](1);
        actorsToUpdate[0] = currentActor;
        _before(actorsToUpdate);

        (bool success, bytes memory returnData) = _sampleFailWithRequireCall(params.sampleUint);

        sampleFailWithRequirePostconditions(success, returnData, actorsToUpdate);
    }

    function fuzz_sampleFailWithCustomError(uint8 sampleNum) public setCurrentActor {
        SampleFailWithCustomErrorParams memory params = sampleFailWithCustomErrorPreconditions(sampleNum);

        address[] memory actorsToUpdate = new address[](1);
        actorsToUpdate[0] = currentActor;
        _before(actorsToUpdate);

        (bool success, bytes memory returnData) = _sampleFailWithCustomErrorCall(params.sampleUint);

        sampleFailWithCustomErrorPostconditions(success, returnData, actorsToUpdate);
    }

    function fuzz_sampleFailWithPanic(uint256 sampleInput) public setCurrentActor {
        SampleFailWithPanicParams memory params = sampleFailWithPanicPreconditions(sampleInput);

        address[] memory actorsToUpdate = new address[](1);
        actorsToUpdate[0] = currentActor;
        _before(actorsToUpdate);

        (bool success, bytes memory returnData) = _sampleFailWithPanicCall(params.sampleUint);

        sampleFailWithPanicPostconditions(success, returnData, actorsToUpdate);
    }

    function fuzz_sampleFailWithAssert(uint256 sampleInput) public setCurrentActor {
        SampleFailWithAssertParams memory params = sampleFailWithAssertPreconditions(sampleInput);

        address[] memory actorsToUpdate = new address[](1);
        actorsToUpdate[0] = currentActor;
        _before(actorsToUpdate);

        (bool success, bytes memory returnData) = _sampleFailWithAssertCall(params.sampleUint);

        sampleFailWithAssertPostconditions(success, returnData, actorsToUpdate);
    }

    function fuzz_sampleFailReturnEmptyData(bool sampleInput) public setCurrentActor {
        SampleFailReturnEmptyDataParams memory params = sampleFailReturnEmptyDataPreconditions(sampleInput);

        address[] memory actorsToUpdate = new address[](1);
        actorsToUpdate[0] = currentActor;
        _before(actorsToUpdate);

        (bool success, bytes memory returnData) = _sampleFailReturnEmptyDataCall(params.sampleUint);

        sampleFailReturnEmptyDataPostconditions(success, returnData, actorsToUpdate);
    }
}
