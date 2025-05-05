from flask import Flask, request, jsonify
from web3 import Web3
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables
load_dotenv()
GANACHE_URL = os.getenv("GANACHE_URL", "http://127.0.0.1:7545")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")
CONTRACT_ABI = [
    {
      "inputs": [],
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "reportId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "reporter",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "string",
          "name": "location",
          "type": "string"
        },
        {
          "indexed": False,
          "internalType": "string",
          "name": "congestionLevel",
          "type": "string"
        }
      ],
      "name": "NewReport",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "reportId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "bool",
          "name": "verified",
          "type": "bool"
        }
      ],
      "name": "ReportVerified",
      "type": "event"
    },
    {
      "inputs": [],
      "name": "admin",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function",
      "constant": True
    },
    {
      "inputs": [],
      "name": "reportCount",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function",
      "constant": True
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "name": "reports",
      "outputs": [
        {
          "internalType": "address",
          "name": "reporter",
          "type": "address"
        },
        {
          "internalType": "string",
          "name": "location",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "congestionLevel",
          "type": "string"
        },
        {
          "internalType": "uint256",
          "name": "timestamp",
          "type": "uint256"
        },
        {
          "internalType": "bool",
          "name": "verified",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function",
      "constant": True
    },
    {
      "inputs": [
        {
          "internalType": "string",
          "name": "_location",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_congestionLevel",
          "type": "string"
        }
      ],
      "name": "submitReport",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_reportId",
          "type": "uint256"
        }
      ],
      "name": "verifyReport",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_reportId",
          "type": "uint256"
        }
      ],
      "name": "getReport",
      "outputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        },
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function",
      "constant": True
    }
  ]

# Connect to blockchain
web3 = Web3(Web3.HTTPProvider(GANACHE_URL))
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)
admin_account = web3.eth.accounts[0]

@app.route('/submit', methods=['POST'])
def submit_report():
    data = request.json
    location = data.get("location")
    congestion = data.get("congestionLevel")

    tx_hash = contract.functions.submitReport(location, congestion).transact({"from": web3.eth.accounts[1]})
    web3.eth.wait_for_transaction_receipt(tx_hash)

    return jsonify({"message": "Report submitted", "tx_hash": tx_hash.hex()}), 200

@app.route('/verify/<int:report_id>', methods=['POST'])
def verify_report(report_id):
    tx_hash = contract.functions.verifyReport(report_id).transact({"from": admin_account})
    web3.eth.wait_for_transaction_receipt(tx_hash)
    return jsonify({"message": "Report verified", "tx_hash": tx_hash.hex()}), 200

@app.route('/get_report/<int:report_id>', methods=['GET'])
def get_report(report_id):
    report = contract.functions.getReport(report_id).call()
    return jsonify({"location": report[0], "congestionLevel": report[1], "verified": report[2]})

if __name__ == '__main__':
    app.run(debug=True)
