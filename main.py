from utils import *

JSON_URL = "https://www.jsonkeeper.com/b/PLZ0"
JSON_PATH = "data/operations"

# получение списка операций из локального хранилища
operation_list = jsonData.get_list_from_file(JSON_PATH)
# получение списка выполненных операций
operation_list = receiptEdit.get_executed_receipts(operation_list)
# получение списка последние COUNT операций
operation_list = receiptEdit.get_latest_receipts(5, operation_list)
for i in operation_list:
    # предварительное форматирование данных операции
    operation = receiptEdit.get_preformatted_receipt(i)
    # приведение данных об операции в вид чека
    receipt = receiptEdit.get_formatted_receipt(operation)
    #печать чека
    print(receipt)
