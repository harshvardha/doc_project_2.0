// SPDX-License-Identifier: MIT

pragma solidity >=0.8.0 <0.9.0;

struct Patient {
    address addr;
    string patientName;
    uint256 age;
    string gender;
    string symptoms;
    string disease;
    string pathologicalInformation;
    string medicine;
}

contract PatientRecordStorage {
    mapping(address => Patient) public medicalCases;

    function addNewPatient(
        address _address,
        string memory _patientName,
        uint256 _age,
        string memory _gender,
        string memory _symptoms,
        string memory _disease,
        string memory _pathologicalInformation,
        string memory _medicine
    ) public {
        require(medicalCases[_address].addr != msg.sender);
        Patient memory newPatient = Patient({
            addr: _address,
            patientName: _patientName,
            age: _age,
            gender: _gender,
            symptoms: _symptoms,
            disease: _disease,
            pathologicalInformation: _pathologicalInformation,
            medicine: _medicine
        });
        medicalCases[_address] = newPatient;
    }

    function getPatientMedicalRecord(address _address)
        public
        view
        returns (Patient memory)
    {
        return medicalCases[_address];
    }
}
