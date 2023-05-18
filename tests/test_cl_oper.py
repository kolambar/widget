from utils.cl_oper import Operation
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


def test_born_from_devastated_json(empty_data):
    test_element = Operation.born_from_json(empty_data)
    assert test_element == []


def test_bagger(full_list_of_class):
    sorted_executed_list = Operation.bagger(full_list_of_class)
    assert sorted_executed_list[0].date > sorted_executed_list[1].date
    assert sorted_executed_list[2].date > sorted_executed_list[5].date
    assert sorted_executed_list[4].date > sorted_executed_list[12].date
    assert sorted_executed_list[7].date > sorted_executed_list[11].date
    assert sorted_executed_list[20].date > sorted_executed_list[35].date
    assert sorted_executed_list[0].date_to_print == '08.12.2019'


def test_blur_sender(full_list_of_class):
    assert Operation.blur_num(full_list_of_class[0].sender) == 'Maestro 1596 83** **** 5199'
    assert Operation.blur_num(full_list_of_class[1].sender) == 'MasterCard 7158 30** **** 6758'
    assert Operation.blur_num(full_list_of_class[2].sender) == 'Счет **6952'
    assert Operation.blur_num(full_list_of_class[3].sender) == None


def test_time_metamorphosis(element_of_class):
    element_of_class.time_metamorphosis(element_of_class.date)
    assert element_of_class.date_to_compare == datetime.datetime(2018, 6, 30, 2, 8, 58, 425572)

