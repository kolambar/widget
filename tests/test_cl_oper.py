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

'''
1. получить список классов +
2. отфильтровать функцией класса от непринятых и давних 
3. получить время последовательно всех 5 оставшихся операций
4. реализовать работу с датой и временем !!!
5. сравнить время всех операций и убедиться, что они идут по порядку
6. проверить что все операции прошли
'''
def test_filter(full_list_of_class):
    last_five_executed = full_list_of_class.filter()
    first = last_five_executed[0]
    second = last_five_executed[1]
    third = last_five_executed[2]
    fourth = last_five_executed[3]
    fifth = last_five_executed[4]
    # first
    # second
    # third
    # fourth
    # fifth