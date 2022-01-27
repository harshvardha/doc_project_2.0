from pydantic import BaseModel


class Patient(BaseModel):
    address: str
    name: str


class LogInUser(BaseModel):
    address: str
    password: str


class PatientData(Patient):
    age: int
    gender: str
    symptoms: str
    disease: str
    pathologicalInformation: str = None
    medicine: str


class RegisterUser(Patient):
    password: str
