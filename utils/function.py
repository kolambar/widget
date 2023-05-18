import json


def from_json_to_data(path_to_json):
    '''
    достает содержимое из файла json
    :param path_to_json:
    :return:
    '''
    with open(path_to_json, 'r', encoding="UTF-8") as file:
        data = json.load(file)
    return data


