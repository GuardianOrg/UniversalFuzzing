pragma solidity ^0.8.0;

import "../FuzzSetup.sol";

contract BeforeAfter is FuzzSetup {
    struct SampleFunctionParams {
        uint256 sampleUint;
    }

    struct SampleFailWithRequireParams {
        bool sampleUint;
    }

    struct SampleFailWithCustomErrorParams {
        uint8 sampleUint;
    }

    struct SampleFailWithPanicParams {
        uint256 sampleUint;
    }

    struct SampleFailWithAssertParams {
        uint256 sampleUint;
    }

    struct SampleFailReturnEmptyDataParams {
        bool sampleUint;
    }

    mapping(uint8 => State) states;

    struct State {
        mapping(address => ActorStates) actorStates;
        uint256 contractEthBalance;
    }

    struct ActorStates {
        uint256 userEthBalance;
    }

    function _before(address[] memory actors) internal {
        // Reset full state mapping
        // delete states[0]; //use only if needed
        // delete states[1]; //use only if needed
        _setStates(0, actors);
    }

    function _after(address[] memory actors) internal {
        _setStates(1, actors);
    }

    function _setStates(uint8 callNum, address[] memory actors) internal {
        _processActors(callNum, actors);
        _updateCommonState(callNum);
    }

    function _processActors(uint8 callNum, address[] memory actors) private {
        for (uint256 i = 0; i < actors.length; i++) {
            _setActorState(callNum, actors[i]);
        }
    }

    function _updateCommonState(uint8 callNum) private {
        checkContractEthBalance(callNum);
        _logicalCoverage(callNum);
    }

    function _logicalCoverage(uint8 callNum) private {
        // Implement logical coverage here.
    }

    function _setActorState(uint8 callNum, address actor) internal virtual {
        checkUserEthBalance(callNum, actor);
    }

    function checkUserEthBalance(uint8 callNum, address user) internal {
        console.log("Before/After userEthBalance", callNum, user.balance);
        states[callNum].actorStates[user].userEthBalance = user.balance;
    }

    function checkContractEthBalance(uint8 callNum) internal {
        console.log("Before/After contractEthBalance", callNum, address(sampleContract).balance);
        states[callNum].contractEthBalance = address(sampleContract).balance;
    }

    function min(uint256 a, uint256 b) internal pure returns (uint256) {
        return a < b ? a : b;
    }
}
