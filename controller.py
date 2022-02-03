from AuthenticationUserInterface import LoginForm, RegisterForm, ForgetPassword
from newPatientWindow import AddNewPatient
from patientMedicalRecordWindow import MedicalRecord
from optionsWindow import OptionsWindow
from Schemas import RegisterUser, LogInUser, PatientData
from model import Model
from baseWindow import BaseWindow


class Controller:
    def __init__(self):
        print("hello")
        self._model = Model()
        self._activeWindow: BaseWindow = None
        self._buttons: dict
        self._entryBoxes: dict
        self._privateKey: str
        self._whichWindow: str
        self._dialogBoxInstance = None
        self._bindLoginFormEvents()

    def _bindLoginFormEvents(self):
        if(self._activeWindow):
            self._activeWindow.destroy()
        self._activeWindow = LoginForm()
        self._buttons = self._activeWindow.getButtons()
        self._entryBoxes = self._activeWindow.getEntryBoxes()
        self._buttons["login"].bind("<Button-1>", self._loginUser)
        self._buttons["register"].bind(
            "<Button-1>", self._bindRegisterFormEvents)
        self._buttons["forgetPassword"].bind(
            "<Button-1>", self._bindForgetPasswordEvents)
        self._activeWindow.mainloop()

    def _loginUser(self, event=None):
        user = LogInUser(
            address=self._entryBoxes["address"].get(),
            password=self._entryBoxes["password"].get(),
            privateKey=self._entryBoxes["privateKey"].get()
        )
        self._privateKey = "0x"+user.privateKey
        if(self._model.loginUser(user)):
            self._bindOptionsWindowEvents()
        else:
            self._activeWindow.displayMessageDialog()

    def _bindRegisterFormEvents(self, event=None):
        self._activeWindow.destroy()
        self._activeWindow = RegisterForm()
        self._buttons = self._activeWindow.getButtons()
        self._entryBoxes = self._activeWindow.getEntryBoxes()
        self._buttons["register"].bind("<Button-1>", self._registerUser)
        self._activeWindow.mainloop()

    def _registerUser(self, event=None):
        user = RegisterUser(
            address=self._entryBoxes["address"].get(),
            name=self._entryBoxes["name"].get(),
            password=self._entryBoxes["password"].get()
        )
        if(self._model.registerUser(user, self._entryBoxes["privateKey"].get())):
            self._activeWindow.displaySuccessMessage()
            self._bindLoginFormEvents()
        else:
            self._activeWindow.displayErrorMessage()

    def _bindForgetPasswordEvents(self, event=None):
        self._activeWindow.destroy()
        self._activeWindow = ForgetPassword()
        self._buttons = self._activeWindow.getButtons()
        self._entryBoxes = self._activeWindow.getEntryBoxes()
        self._buttons["reset"].bind("<Button-1>", self._resetPassword)
        self._activeWindow.mainloop()

    def _resetPassword(self, event=None):
        address = self._entryBoxes["address"].get()
        newPassword = self._entryBoxes["newPassword"].get()
        privateKey = self._entryBoxes["privateKey"].get()
        if(self._model.resetPassword(address, newPassword, privateKey)):
            self._activeWindow.displaySuccessMessage()
            self._bindLoginFormEvents()
        else:
            self._activeWindow.displayErrorMessage()

    def _bindOptionsWindowEvents(self, event=None):
        self._activeWindow.destroy()
        self._activeWindow = OptionsWindow()
        self._buttons = self._activeWindow.getButtons()
        self._whichWindow = "OptionsWindow"
        self._buttons["addNewPatient"].bind(
            "<Button-1>", self._bindAddNewPatientEvents)
        self._buttons["searchPatient"].bind("<Button-1>", self._searchPatient)
        self._activeWindow.mainloop()

    def _searchPatient(self, event=None):
        self._dialogBoxInstance = self._activeWindow.displaySearchDialog()
        self._dialogBoxInstance.searchButton.bind(
            "<Button-1>", self._executeQuery)

    def _executeQuery(self, event=None):
        self._dialogBoxInstance._search()
        address = self._dialogBoxInstance.getAddress()
        self._dialogBoxInstance._cancel()
        user = self._model.getPatientData(address)
        if(type(user) == PatientData):
            self._bindMedicalRecordEvents(user)
        else:
            if(self._whichWindow == "AddNewPatient"):
                self._activeWindow.displayErrorMessage("Patient Not Found")
            else:
                self._activeWindow.displayErrorMessage()

    def _bindAddNewPatientEvents(self, event=None):
        self._activeWindow.destroy()
        self._activeWindow = AddNewPatient()
        self._buttons = self._activeWindow.getButtons()
        self._entryBoxes = self._activeWindow.getInformationWidgets()
        self._whichWindow = "AddNewPatient"
        self._buttons["save"].bind("<Button-1>", self._save)
        self._buttons["search"].bind("<Button-1>", self._searchPatient)
        self._activeWindow.mainloop()

    def _save(self, event=None):
        basicInformation = self._entryBoxes["basicInfo"]
        medicalInformation = self._entryBoxes["medicalInfo"]
        patientData = PatientData(
            address=basicInformation["address"].get(),
            name=basicInformation["name"].get(),
            age=basicInformation["age"].get(),
            gender=self._activeWindow.getPatientGender(),
            symptoms=medicalInformation["symptoms"].get("1.0", "end"),
            disease=medicalInformation["disease"].get("1.0", "end"),
            pathologicalInformation=medicalInformation["pathologicalInformation"].get(
                "1.0", "end"),
            medicine=medicalInformation["medicine"].get("1.0", "end")
        )
        if(self._model.addNewPatient(patientData, self._privateKey)):
            self._activeWindow.displaySuccessMessage()
        else:
            self._activeWindow.displayErrorMessage("Error Saving Data")

    def _bindMedicalRecordEvents(self, patientInformation: PatientData, event=None):
        self._activeWindow.destroy()
        self._activeWindow = MedicalRecord(patientInformation)
        self._buttons = self._activeWindow.getButtons()
        if(self._whichWindow == "AddNewPatient"):
            self._buttons["back"].bind(
                "<Button-1>", self._bindAddNewPatientEvents)
        elif(self._whichWindow == "OptionsWindow"):
            self._buttons["back"].bind(
                "<Button-1>", self._bindOptionsWindowEvents)
        self._activeWindow.mainloop()
