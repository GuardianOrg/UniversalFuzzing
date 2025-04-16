pragma solidity ^0.8.0;

contract PropertiesDescriptions {
    // ==============================================================
    // Global Properties (GLOB)
    // These properties define invariants that must hold true across all market states and operations
    // ==============================================================

    string constant GLOB_01 = "GLOB_01: Sample Global Invariant";

    // ==============================================================
    // Invariant Properties (INV)
    // These properties define invariants that must hold true as a sample
    // ==============================================================

    string constant INV_01 = "INV_01: Sample Invariant";

    string constant ERR_01 = "ERR_01: Unexpected Error";
}
