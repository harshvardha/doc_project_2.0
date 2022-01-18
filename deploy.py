from solcx import compile_standard
import json
from web3 import Web3

with open("./PatientRecordStorage.sol", "r") as file:
    patientRecordStorage = file.read()

compiledSol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"PatientRecordStorage.sol": {"content": patientRecordStorage}},
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
contractBytecode = compiledSol["contracts"]["PatientRecordStorage.sol"]["PatientRecordStorage"]["evm"]["bytecode"]["object"]

# getting abi to deploy the contract
contractABI = compiledSol["contracts"]["PatientRecordStorage.sol"]["PatientRecordStorage"]["abi"]

# for connecting to ganache
web3Provider = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chainId = 1337
myAddress = "0x3db72a2e0c28482658F0f56853631802D41Ed07e"
privateKey = "d9af4811fc2c4d9dd49e180f0a1e1f8a94ca87d890ef9afda359f17e7258a41d"

# deploying the contract
PatientRecordStorage = web3Provider.eth.contract(abi = contractABI, bytecode = contractBytecode)

# getting the latest transaction
nonce = web3Provider.eth.getTransactionCount(myAddress)

# now creating a transaction
# build transaction
# sign transaction
# send transaction
transaction = PatientRecordStorage.constructor().buildTransaction(
    {
        "chainId": chainId,
        "from": myAddress,
        "nonce": nonce
    }
)
signedTransaction = web3Provider.eth.account.sign_transaction(transaction, private_key = privateKey)
transactionHash = web3Provider.eth.send_raw_transaction(signedTransaction.rawTransaction)
transactionReciept = web3Provider.eth.wait_for_transaction_receipt(transactionHash)
print("deployed!!!")

# now interacting with contract
patient_record_storage = web3Provider.eth.contract(address = transactionReciept.contractAddress, abi = contractABI)
#print(patient_record_storage.functions.getPatientMedicalRecord(1).call())

def addNewPatient(patientObject = None):
    global nonce
    nonce += 1
    storePatientData = patient_record_storage.functions.addNewPatient("Harsh", 22, "male", "high temperature", "fever", "None", "paracetamol").buildTransaction(
    {"chainId": chainId, "from": myAddress, "nonce": nonce})
    signed_store_transaction = web3Provider.eth.account.sign_transaction(storePatientData, privateKey)
    sendTransaction = web3Provider.eth.send_raw_transaction(signed_store_transaction.rawTransaction)
    transactionReciept = web3Provider.eth.wait_for_transaction_receipt(sendTransaction)
    print("updated!!!\n", transactionReciept)

def getPatientMedicalRecord(caseNo: int):
    print(patient_record_storage.functions.getPatientMedicalRecord(caseNo).call())

addNewPatient()
getPatientMedicalRecord(1)