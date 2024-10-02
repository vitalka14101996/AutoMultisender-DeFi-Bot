def check_transaction(tx_hash):
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    if tx_receipt is not None:
        print(f'Статус транзакции: {tx_receipt.status}')
    else:
        print('Транзакция не найдена или еще не завершена.')

tx_hash = 'YOUR_TRANSACTION_HASH'
check_transaction(tx_hash)
