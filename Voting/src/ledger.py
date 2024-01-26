from web3 import Web3,HTTPProvider
import json

blockchain="http://127.0.0.1:7545"


def connect_with_voting(wallet):

    web3=Web3(HTTPProvider(blockchain))

    print("Connected")

    with open('../build/contracts/voting.json') as f:
        artifact_json=json.load(f)
        contract_abi=artifact_json['abi']
        contract_address=artifact_json['networks']['5777']['address']
    web3.eth.defaultAccount=wallet
    contract=web3.eth.contract(
        abi=contract_abi,
        address=contract_address
    )
    return(web3,contract)
def castvote(wallet,id):
    try:
        web3,contract=connect_with_voting(wallet)
        try:
            tx_hash=contract.functions.castvote(id).transact()
            web3.eth.wait_for_transaction_receipt(tx_hash)
            return "Vote Casted"
        except Exception as e:
            print(f"Error: {e}")
            return "Can't cast"

                # tx_hash=contract.functions.castvote(id).transact()
                # web3.eth.wait_for_transaction_receipt(tx_hash)
                # return "Vote Casted"
    except:
        return "Can't cast"


def result(wallet):
    try:
        web3,contract=connect_with_voting(wallet)
        data=contract.functions.result().call()
        return data
    except:
        return "Can't cast"