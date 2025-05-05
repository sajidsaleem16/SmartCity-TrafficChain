# 🚦 TrafficJamChain: A Blockchain-Based Traffic Reporting System

This project showcases a decentralized traffic congestion reporting system using **Blockchain** and **Flask**. It simulates how smart cities can leverage blockchain to maintain **Confidentiality, Integrity, and Availability (CIA)** of real-time traffic data. Built for educational and demonstrative purposes.

---

## 🌍 Use Case

In smart cities, congestion data must remain tamper-proof, verifiable, and accessible. TrafficJamChain lets users report congestion from any location and stores it immutably on a blockchain. This supports urban planners, emergency responders, and navigation systems with reliable data.

---

## 📦 Tech Stack

- **Frontend:** CLI-based API interface (extendable to mobile/web UI)
- **Backend:** Python (Flask + Web3.py)
- **Blockchain:** Solidity smart contract deployed via Truffle on Ganache (Ethereum testnet)
- **OS Support:** macOS (M1) and Windows
- **Proposed Extension (Report Only):** Federated Learning to predict traffic hotspots without compromising local data privacy

---

## 🧑‍💻 Setup Guide

### 🔁 Clone Repository

```bash
https://github.com/sajidsaleem16/SmartCity-TrafficChain.git
cd TrafficJamChain
```

## 🍎 macOS Setup

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install node
npm install -g ganache-cli
npm install -g truffle
pip install web3 flask python-dotenv
```
## Windows Setup

1. Install Node.js and Python 3.10+
2. Install Truffle & Ganache CLI:
```
npm install -g ganache-cli
npm install -g truffle
pip install web3 flask python-dotenv
```

## ⚙️ Deploy Smart Contract

```
truffle compile
ganache-cli  # Run in a separate terminal
truffle migrate --network development
```

## 🔧 Configure Flask Backend
Create a .env file:
```
GANACHE_URL=http://127.0.0.1:7545
CONTRACT_ADDRESS=0xYourDeployedContractAddress # Replace with actual address
```

## 🚀 Run Flask Server
```
cd backend
python app.py
```

## 🔗 API Endpoints

### 1. Submit Traffic Report
```
POST /submit
{
  "location": "Highway X",
  "congestionLevel": "Heavy"
}
```
### 2. Get Report
```
GET /get_report/1
```
### 3. Verify Report (Admin)
```
POST /verify/1
```

