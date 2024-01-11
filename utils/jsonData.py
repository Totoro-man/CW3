import requests, json


def get_list_from_url(url: str):
    """Получение данных с удаленного хранилища
    возвращает данные в понятном для питона виде"""
    result = requests.get(url)
    return result.json()


def get_list_from_file(path: str):
    """Получение данных с локального хранилища (файла)
    возвращает данные в понятном для питона виде"""
    with open(path, encoding="utf8") as f:
        return json.load(f)