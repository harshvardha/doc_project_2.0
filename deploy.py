from solcx import compile_standard
import json
from web3 import Web3
from Schemas import PatientData


class Deploy:
    def __init__(self):
        self._patientRecordStorage: str
        self._authentication: str
        self._compiledContracts: dict
        self._chainId = 1337
        self._web3Provider = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
        self._myAddress = "0x0e80eA8A79bcb58F12bF835c991d71CE31E95d6f"
        self._privateKey = "0xf2677b22f58272e2740e0388a535829856c304cda71962454ced6ef4d4370455"
        self._nonce = self._web3Provider.eth.getTransactionCount(
            self._myAddress)
        with open("./PatientRecordStorage.sol", "r") as file:
            self._patientRecordStorage = file.read()
        with open("./Auth.sol", "r") as file:
            self._authentication = file.read()
        self._compileContracts()
        self._contractBytecodePatient = self._compiledContracts["contracts"]["PatientRecordStorage.sol"][
            "PatientRecordStorage"]["evm"]["bytecode"]["object"]
        self._contractBytecodeAuth = self._compiledContracts[
            "contracts"]["Auth.sol"]["Auth"]["evm"]["bytecode"]["object"]
        self._contractABIPatient = self._compiledContracts["contracts"][
            "PatientRecordStorage.sol"]["PatientRecordStorage"]["abi"]
        self._contractABIAuth = self._compiledContracts["contracts"]["Auth.sol"]["Auth"]["abi"]
        self._deployContracts()

    def _compileContracts(self):
        self._compiledContracts = compile_standard(
            {
                "language": "Solidity",
                "sources": {"PatientRecordStorage.sol": {"content": self._patientRecordStorage}, "Auth.sol": {"content": self._authentication}},
                "settings": {
                    "outputSelection": {
                        "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
                    }
                },
            },
            solc_version="0.8.0",
        )
        with open("compiledCode.json", "w") as file:
            json.dump(self._compiledContracts, file)

    def _performTransaction(self, transaction, privateKey: str):
        signedTransaction = self._web3Provider.eth.account.sign_transaction(
            transaction, privateKey)
        sendTransaction = self._web3Provider.eth.send_raw_transaction(
            signedTransaction.rawTransaction)
        transactionReciept = self._web3Provider.eth.wait_for_transaction_receipt(
            sendTransaction)
        return transactionReciept

    def _deployContracts(self):
        # deploying PatientRecordStorage.sol contract
        self._patientRecordStorage = self._web3Provider.eth.contract(
            abi=self._contractABIPatient, bytecode=self._contractBytecodePatient
        )
        transaction = self._patientRecordStorage.constructor().buildTransaction(
            {"chainId": self._chainId, "from": self._myAddress, "nonce": self._nonce}
        )
        transactionReciept = self._performTransaction(
            transaction, self._privateKey)
        print("PatientRecordStorage.sol Contract Deployed : ", transactionReciept)
        self._updateNonce()
        self._patientRecordStorage = self._web3Provider.eth.contract(
            address=transactionReciept.contractAddress, abi=self._contractABIPatient
        )
        print(self._patientRecordStorage.address)

        # deploying Auth.sol contract
        self._authentication = self._web3Provider.eth.contract(
            abi=self._contractABIAuth, bytecode=self._contractBytecodeAuth
        )
        transaction = self._authentication.constructor().buildTransaction(
            {"chainId": self._chainId, "from": self._myAddress, "nonce": self._nonce}
        )
        transactionReciept = self._performTransaction(
            transaction, self._privateKey)
        print("Auth.sol Contract Deployed : ", transactionReciept)
        self._updateNonce()
        self._authentication = self._web3Provider.eth.contract(
            address=transactionReciept.contractAddress, abi=self._contractABIAuth
        )
        print(self._authentication.address)

    def _updateNonce(self):
        self._nonce += 1

    def _getNonce(self, address: str):
        return self._web3Provider.eth.getTransactionCount(address)

    def registerUser(self, address: str, name: str, password: str, privateKey: str):
        register = self._authentication.functions.registerUser(address, name, bytes(password)).buildTransaction(
            {"chainId": self._chainId, "from": address, "nonce": self._getNonce(address)})
        return self._performTransaction(register, privateKey)["status"]

    def logInUser(self, address: str, password: str, privateKey: str):
        logIn = self._authentication.functions.logInUser(address, bytes(password)).buildTransaction(
            {"chainId": self._chainId, "from": address, "nonce": self._getNonce(address)})
        return self._performTransaction(logIn, privateKey)["status"]

    def resetPassword(self, address: str, password: str, privateKey: str):
        reset = self._authentication.functions.resetPassword(address, bytes(password)).buildTransaction(
            {"chainId": self._chainId, "from": address,
                "nonce": self._getNonce(address)}
        )
        return self._performTransaction(reset, privateKey)["status"]

    def addNewPatient(self, patientObject: PatientData, privateKey: str):
        storePatientData = self._patientRecordStorage.functions.addNewPatient(
            patientObject.address, patientObject.name, patientObject.age, patientObject.gender, patientObject.symptoms,
            patientObject.disease, patientObject.pathologicalInformation, patientObject.medicine
        ).buildTransaction(
            {"chainId": self._chainId, "from": patientObject.address, "nonce": self._getNonce(patientObject.address)})
        return self._performTransaction(storePatientData, privateKey)["status"]

    def checkUserLoggedInOrNot(self, address: str):
        return self._authentication.functions.chechUserLoggedInOrNot(address).call()

    def getPatientMedicalRecord(self, address: str):
        return self._patientRecordStorage.functions.getPatientMedicalRecord(address).call()
