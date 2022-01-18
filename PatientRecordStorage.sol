// SPDX-License-Identifier: MIT

pragma solidity >=0.8.0 <0.9.0;

struct Patient {
    string patientName;
    uint256 age;
    string gender;
    string symptoms;
    string disease;
    string pathologicalInformation;
    string medicine;
}

contract PatientRecordStorage {
    mapping(uint256 => Patient) public medicalCases;
    uint256 caseNumber = 1;

    function addNewPatient(
        string memory _patientName,
        uint256 _age,
        string memory _gender,
        string memory _symptoms,
        string memory _disease,
        string memory _pathologicalInformation,
        string memory _medicine
    ) public {
        Patient memory newPatient = Patient({
            patientName: _patientName,
            age: _age,
            gender: _gender,
            symptoms: _symptoms,
            disease: _disease,
            pathologicalInformation: _pathologicalInformation,
            medicine: _medicine
        });
        medicalCases[caseNumber] = newPatient;
    }

    function getPatientMedicalRecord(uint256 caseNo)
        public
        view
        returns (Patient memory)
    {
        require(
            caseNo <= caseNumber,
            "There is no patient with this caseNumber"
        );
        return medicalCases[caseNo];
    }
}
