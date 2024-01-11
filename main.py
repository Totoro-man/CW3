from utils import *

JSON_URL = "https://www.jsonkeeper.com/b/PLZ0"
JSON_PATH = "data/operations"

# получение списка операций из локального хранилища
operation_list = jsonData.get_list_from_file(JSON_PATH)

print(operation_list[0])
