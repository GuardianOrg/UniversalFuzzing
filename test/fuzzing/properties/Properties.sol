pragma solidity ^0.8.0;

import "./Properties_ERR.sol";

contract Properties is Properties_ERR {
    // ==============================================================
    // Global Properties (GLOB)
    // ==============================================================

    function invariant_GLOB_01() internal view returns (bool) {
        return true;
    }

    // ==============================================================
    // Invariant Properties (INV)
    // ==============================================================

    function invariant_INV_01() internal view returns (bool) {
        return true;
    }
}
