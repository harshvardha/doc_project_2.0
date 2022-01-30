// SPDX-License-Identifier: MIT

pragma solidity >=0.8.0 <0.9.0;

contract Auth {
    struct userDetails {
        address addr;
        string name;
        bytes32 password;
        bool isUserLoggedIn;
    }

    mapping(address => userDetails) user;

    // user registration function
    function registerUser(
        address _address,
        string memory _name,
        bytes memory _password
    ) public returns (bool) {
        require(user[_address].addr != msg.sender);
        user[_address].addr = _address;
        user[_address].name = _name;
        user[_address].password = keccak256(_password);
        user[_address].isUserLoggedIn = false;
        return true;
    }

    // user login function
    function logInUser(address _address, bytes memory _password)
        public
        returns (bool)
    {
        if (user[_address].password == keccak256(_password)) {
            user[_address].isUserLoggedIn = true;
            return user[_address].isUserLoggedIn;
        } else {
            return false;
        }
    }

    // user can reset account password through this function
    function resetPassword(address _address, bytes memory newPassword) public {
        require(user[_address].addr == msg.sender);
        user[_address].password = keccak256(newPassword);
    }

    // check if the user is already logged in or not
    function checkUserLoggedInOrNot(address _address)
        public
        view
        returns (bool)
    {
        return user[_address].isUserLoggedIn;
    }

    // logout user
    function logOutUser(address _address) public returns (bool) {
        user[_address].isUserLoggedIn = false;
        return true;
    }
}
