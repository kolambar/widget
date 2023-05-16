from utils.cl_oper import Operation
from utils.function import time_metamorphosis, from_json_to_data
import os
import datetime

test_data = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
]


def test_born_from_json():
    test_element = Operation.born_from_json(test_data)
    assert type(test_element[0]) is Operation
    assert test_element[0].id == 441945886


def test_born_from_json_without_from(data_without_from):
    test_element = Operation.born_from_json(data_without_from)
    assert type(test_element[0]) is Operation
    assert test_element[0].sender == 'Счета отправителя нет. Это операция по открытию вклада.'


def test_born_from_devastated_json(empty_data):
    test_element = Operation.born_from_json(empty_data)
    assert test_element == []

'''
1. получить список классов +
2. отфильтровать функцией класса от непринятых и давних 
3. получить время последовательно всех 5 оставшихся операций
4. реализовать работу с датой и временем +
5. сравнить время всех операций и убедиться, что они идут по порядку
6. проверить что все операции прошли
'''
def test_filter(full_list_of_class):
    sorted_executed_list = Operation.filter(full_list_of_class)
    assert sorted_executed_list[0].date > sorted_executed_list[1].date
    assert sorted_executed_list[2].date > sorted_executed_list[5].date
    assert sorted_executed_list[4].date > sorted_executed_list[12].date
    assert sorted_executed_list[7].date > sorted_executed_list[11].date
    assert sorted_executed_list[20].date > sorted_executed_list[35].date
    assert sorted_executed_list[0].date_to_print == '08.12.2019'