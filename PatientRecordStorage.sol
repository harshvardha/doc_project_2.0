// SPDX-License-Identifier: MIT

pragma solidity >=0.8.0 <0.9.0;

contract PatientRecordStorage {
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
    mapping(address => Patient) medicalCases;

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
        medicalCases[_address] = Patient({
            addr: _address,
            patientName: _patientName,
            age: _age,
            gender: _gender,
            symptoms: _symptoms,
            disease: _disease,
            pathologicalInformation: _pathologicalInformation,
            medicine: _medicine
        });
    }

    function getPatientMedicalRecord(address _address)
        public
        view
        returns (Patient memory)
    {
        return medicalCases[_address];
    }
}
