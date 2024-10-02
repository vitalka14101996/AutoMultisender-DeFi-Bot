from web3 import Web3

# Connect to Ethereum host
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

# Setting up an account
account = w3.eth.account.privateKeyToAccount('YOUR_PRIVATE_KEY')

# Token address and number of tokens
token_address = 'TOKEN_CONTRACT_ADDRESS'
amount = w3.toWei(1, 'ether') # Example of sending 1 token

# Creating a transaction
nonce = w3.eth.getTransactionCount(account.address)
transaction = {
    'to': token_address,
    'value': amount,
    'gas': 2000000,
    'gasPrice': w3.toWei('50', 'gwei'),
    'nonce': nonce,
}

# Signing and sending the transaction
signed_txn = w3.eth.account.signTransaction(transaction, private_key='YOUR_PRIVATE_KEY')
txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

print(f'Transaction sent with hash: {txn_hash.hex()}')
