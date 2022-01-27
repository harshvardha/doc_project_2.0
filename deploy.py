from solcx import compile_standard
import json
from web3 import Web3

# compiling PatientRecordStorage contract
with open("./PatientRecordStorage.sol", "r") as file:
    patientRecordStorage = file.read()

with open("./Auth.sol", "r") as file:
    authentication = file.read()

compiledSol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"PatientRecordStorage.sol": {"content": patientRecordStorage}, "Auth.sol": {"content": authentication}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.8.0",
)

with open("compiledCode.json", "w") as file:
    json.dump(compiledSol, file)

# getting bytecode to deploy the contract
contractBytecodePatient = compiledSol["contracts"]["PatientRecordStorage.sol"][
    "PatientRecordStorage"]["evm"]["bytecode"]["object"]
contractBytecodeAuth = compiledSol["contracts"]["Auth.sol"]["Auth"]["evm"]["bytecode"]["object"]

# getting abi to deploy the contract
contractABIPatient = compiledSol["contracts"]["PatientRecordStorage.sol"]["PatientRecordStorage"]["abi"]
contractABIAuth = compiledSol["contracts"]["Auth.sol"]["Auth"]["abi"]

# for connecting to ganache
web3Provider = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chainId = 1337
myAddress = "0xfC324C1AEd15cD99eefFeEb796F426b65284174c"
privateKey = "63b0c2c7577bb787f279ce55bc19fbc3b105ab9d3390c2b8913f900f51431e0e"


def _performTransaction(transaction, privateKey):
    signedTransaction = web3Provider.eth.account.sign_transaction(
        transaction, privateKey)
    sendTransaction = web3Provider.eth.send_raw_transaction(
        signedTransaction.rawTransaction)
    transactionReciept = web3Provider.eth.wait_for_transaction_receipt(
        sendTransaction)
    return transactionReciept


# getting the latest transaction
nonce = web3Provider.eth.getTransactionCount(myAddress)

# deploying the contracts
patientRecordStorage = web3Provider.eth.contract(
    abi=contractABIPatient, bytecode=contractBytecodePatient)
storageTransaction = patientRecordStorage.constructor().buildTransaction(
    {"chainId": chainId, "from": myAddress, "nonce": nonce})
storageTransactionReciept = _performTransaction(storageTransaction, privateKey)
print("PatientRecordStorage Contract Deployed: ", storageTransactionReciept)
nonce += 1

authentication = web3Provider.eth.contract(
    abi=contractABIAuth, bytecode=contractBytecodeAuth)
authenticationTransaction = authentication.constructor().buildTransaction(
    {"chainId": chainId, "from": myAddress, "nonce": nonce}
)
authenticationTransactionReciept = _performTransaction(
    authenticationTransaction, privateKey)
print("Authentication Contract Deployed: ", authenticationTransactionReciept)

# now interacting with contract
patientRecordStorage = web3Provider.eth.contract(
    address=storageTransactionReciept.contractAddress, abi=contractABIPatient)
authentication = web3Provider.eth.contract(
    address=authenticationTransactionReciept.contractAddress, abi=contractABIAuth)


def registerUser(address: str, name: str, password: str, privateKey: str):
    global nonce
    nonce += 1
    register = authentication.functions.registerUser(address, name, password).buildTransaction(
        {"chainId": chainId, "from": address, "nonce": nonce})
    print("registered : ", _performTransaction(register, privateKey))


def logInUser(address: str, password: str, privateKey: str):
    global nonce
    nonce += 1
    logIn = authentication.functions.logInUser(address, password).buildTransaction(
        {"chainId": chainId, "from": address, "nonce": nonce})
    print("log in successful : ", _performTransaction(logIn, privateKey))


def checkUserLoggedInOrNot(address: str):
    print("Status: ", authentication.functions.chechUserLoggedInOrNot(address).call())


def addNewPatient(patientObject, privateKey: str):
    global nonce
    nonce += 1
    storePatientData = patientRecordStorage.functions.addNewPatient(
        patientObject.name, patientObject.age, patientObject.gender, patientObject.symptoms,
        patientObject.disease, patientObject.pathalogicalInformation, patientObject.medicine
    ).buildTransaction(
        {"chainId": chainId, "from": myAddress, "nonce": nonce})
    print("updated: ", _performTransaction(storePatientData, privateKey))


def getPatientMedicalRecord(address: str):
    print(patientRecordStorage.functions.getPatientMedicalRecord(address).call())

# addNewPatient()
# getPatientMedicalRecord(1)
