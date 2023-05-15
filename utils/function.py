import json
import datetime


def from_json_to_data(path_to_json):
    with open(path_to_json, 'r', encoding="UTF-8") as file:
        data = json.load(file)
    return data


def time_metamorphosis(date):
    data_to_compare = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    data_to_print = data_to_compare.strftime('%d-%m-%Y')
    return data_to_compare, data_to_print
