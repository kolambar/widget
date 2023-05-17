from utils.cl_oper import Operation


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


def test_filter(full_list_of_class):
    sorted_executed_list = Operation.filter(full_list_of_class)
    assert sorted_executed_list[0].date > sorted_executed_list[1].date
    assert sorted_executed_list[2].date > sorted_executed_list[5].date
    assert sorted_executed_list[4].date > sorted_executed_list[12].date
    assert sorted_executed_list[7].date > sorted_executed_list[11].date
    assert sorted_executed_list[20].date > sorted_executed_list[35].date
    assert sorted_executed_list[0].date_to_print == '08.12.2019'


def test_blur_sender(full_list_of_class):
    assert Operation.blur_num(full_list_of_class[0].sender) == '1596 83** **** 5199'
    assert Operation.blur_num(full_list_of_class[1].sender) == '7158 30** **** 6758'
    assert Operation.blur_num(full_list_of_class[2].sender) == '**6952'
    assert Operation.blur_num(full_list_of_class[3].sender) == '   '
    assert Operation.blur_num(full_list_of_class[8].sender) == '6831 98** **** 7658'


def test_user_platform(full_list_of_class):
    assert Operation.user_platform(full_list_of_class[0].sender) == 'Maestro'
    assert Operation.user_platform(full_list_of_class[1].sender) == 'MasterCard'
    assert Operation.user_platform(full_list_of_class[2].sender) == 'Счет'
    assert Operation.user_platform(full_list_of_class[3].sender) == ''
    assert Operation.user_platform(full_list_of_class[8].to) == 'Visa Platinum'
    assert Operation.user_platform(full_list_of_class[15].to) == 'Visa Gold'
    assert Operation.user_platform(full_list_of_class[34].to) == 'МИР'
