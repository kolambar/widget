import json
import os


# PATH_TO_JSON = os.path.join("..", 'operations.json')
def from_json_to_data(path_to_json):
    with open(path_to_json, 'r', encoding="UTF-8") as file:
        data = json.load(file)
    return data
