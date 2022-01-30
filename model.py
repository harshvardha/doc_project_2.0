from deploy import Deploy
from Schemas import Patient, PatientData, LogInUser, RegisterUser


class Model:
    def __init__(self):
        self._deploy = Deploy()

    def loginUser(self, user: LogInUser) -> bool:
        if(self._deploy.logInUser(user.address, user.password, user.privateKey)):
            return True
        return False

    def registerUser(self, user: RegisterUser, privateKey: str) -> bool:
        if(self._deploy.registerUser(user.address, user.name, user.password, privateKey)):
            return True
        return False

    def resetPassword(self, address: str, newPassword, privateKey: str) -> bool:
        if(self._deploy.resetPassword(address, newPassword, privateKey)):
            return True
        return False

    def addNewPatient(self, user: Patient, privateKey: str) -> bool:
        if(self._deploy.addNewPatient(user, privateKey)):
            return True
        return False

    def getPatientData(self, address: str):
        data = self._deploy.getPatientMedicalRecord(address)
        if(data):
            return PatientData(
                address=data[0],
                name=data[1],
                age=data[2],
                gender=data[3],
                symptoms=data[4],
                disease=data[5],
                pathologicalInformation=data[6],
                medicine=data[7]
            )
        return False
