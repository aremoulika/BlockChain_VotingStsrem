from web3 import Web3, HTTPProvider
import json

blockchain="http://127.0.0.1:7545"
web3 = Web3(HTTPProvider(blockchain))
print("COnnected")

artifact = "./build/contracts/voting.json"

with open(artifact, 'r') as f:
    artifact_json = json.load(f)
    contract_abi = artifact_json['abi']
    contract_address = artifact_json['networks']['5777']['address']

contract = web3.eth.contract(
    abi=contract_abi,
    address=contract_address
)

print('Smart Contract Selected')

from_address = web3.eth.accounts[3]

tx_hash = contract.functions.castvote(id).transact({'from': from_address})

receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

m = contract.functions.result().call()
print(m)