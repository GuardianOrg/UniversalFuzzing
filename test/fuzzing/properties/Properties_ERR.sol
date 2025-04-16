//SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

import "./RevertHandler.sol";

abstract contract Properties_ERR is RevertHandler {
    /*
    *
    * FUZZ NOTE: CHECK REVERTS CONFIGURATION IN FUZZ STORAGE VARIABLES
    *
    */

    function _getAllowedPanicCodes() internal pure virtual override returns (uint256[] memory) {
        uint256[] memory panicCodes = new uint256[](4);
        panicCodes[0] = PANIC_ENUM_OUT_OF_BOUNDS;
        panicCodes[1] = PANIC_POP_EMPTY_ARRAY;
        panicCodes[2] = PANIC_ARRAY_OUT_OF_BOUNDS;
        panicCodes[3] = PANIC_ARITHMETIC;

        // Add additional codes
        return panicCodes;
    }

    // Add additional errors here
    // Example:
    // Deposit errors [0-5]
    // allowedErrors[0] = IUsdnProtocolErrors.UsdnProtocolEmptyVault.selector;
    // allowedErrors[1] = IUsdnProtocolErrors
    //     .UsdnProtocolDepositTooSmall
    //     .selector;

    function _getAllowedCustomErrors() internal pure virtual override returns (bytes4[] memory) {
        bytes4[] memory allowedErrors = new bytes4[](1);
        // allowedErrors[0] = bytes4(abi.encode(""));
        return allowedErrors;
    }

    function _isAllowedERC20Error(bytes memory returnData) internal pure virtual override returns (bool) {
        bytes[] memory allowedErrors = new bytes[](9);
        allowedErrors[0] = INSUFFICIENT_ALLOWANCE;
        allowedErrors[1] = TRANSFER_FROM_ZERO;
        allowedErrors[2] = TRANSFER_TO_ZERO;
        allowedErrors[3] = APPROVE_TO_ZERO;
        allowedErrors[4] = MINT_TO_ZERO;
        allowedErrors[5] = BURN_FROM_ZERO;
        allowedErrors[6] = DECREASED_ALLOWANCE;
        allowedErrors[7] = BURN_EXCEEDS_BALANCE;
        allowedErrors[8] = EXCEEDS_BALANCE_ERROR;

        for (uint256 i = 0; i < allowedErrors.length; i++) {
            if (keccak256(returnData) == keccak256(allowedErrors[i])) {
                return true;
            }
        }
        return false;
    }

    function _getAllowedSoladyERC20Error() internal pure virtual override returns (bytes4[] memory) {
        bytes4[] memory allowedErrors = new bytes4[](7);
        allowedErrors[0] = SafeTransferLib.ETHTransferFailed.selector;
        allowedErrors[1] = SafeTransferLib.TransferFromFailed.selector;
        allowedErrors[2] = SafeTransferLib.TransferFailed.selector;
        allowedErrors[3] = SafeTransferLib.ApproveFailed.selector;
        allowedErrors[4] = SafeTransferLib.Permit2Failed.selector;
        allowedErrors[5] = SafeTransferLib.Permit2AmountOverflow.selector;
        allowedErrors[6] = bytes4(0x82b42900); //unauthorized selector

        return allowedErrors;
    }
}
