contract_address = 'YOUR_CONTRACT_ADDRESS'
abi = [...] # ABI of your contract

contract = w3.eth.contract(address=contract_address, abi=abi)

# Example of calling the contract function
def call_contract_function():
    result = contract.functions.yourFunctionName().call()
    print(f'Result from contract: {result}')

call_contract_function()
