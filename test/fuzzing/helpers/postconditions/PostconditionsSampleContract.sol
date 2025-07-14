// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./PostconditionsBase.sol";

contract PostconditionsSampleContract is PostconditionsBase {
    function sampleFunctionPostconditions(bool success, bytes memory returnData, address[] memory actorsToUpdate)
        internal
    {
        if (success) {
            _after(actorsToUpdate);

            invariant_INV_01();

            onSuccessInvariantsGeneral(returnData);
        } else {
            onFailInvariantsGeneral(returnData);
        }
    }

    function sampleFailWithRequirePostconditions(bool success, bytes memory returnData, address[] memory actorsToUpdate)
        internal
    {
        if (success) {
            onSuccessInvariantsGeneral(returnData);
        } else {
            onFailInvariantsGeneral(returnData);
        }
    }

    function sampleFailWithCustomErrorPostconditions(
        bool success,
        bytes memory returnData,
        address[] memory actorsToUpdate
    ) internal {
        if (success) {
            onSuccessInvariantsGeneral(returnData);
        } else {
            onFailInvariantsGeneral(returnData);
        }
    }

    function sampleFailWithPanicPostconditions(bool success, bytes memory returnData, address[] memory actorsToUpdate)
        internal
    {
        if (success) {
            onSuccessInvariantsGeneral(returnData);
        } else {
            onFailInvariantsGeneral(returnData);
        }
    }

    function sampleFailWithAssertPostconditions(bool success, bytes memory returnData, address[] memory actorsToUpdate)
        internal
    {
        if (success) {
            onSuccessInvariantsGeneral(returnData);
        } else {
            onFailInvariantsGeneral(returnData);
        }
    }

    function sampleFailReturnEmptyDataPostconditions(
        bool success,
        bytes memory returnData,
        address[] memory actorsToUpdate
    ) internal {
        if (success) {
            onSuccessInvariantsGeneral(returnData);
        } else {
            onFailInvariantsGeneral(returnData);
        }
    }
}
