import pytest
from utils.function import from_json_to_data
import os
from utils.cl_oper import Operation


@pytest.fixture
def data_without_from():
    dict_without_from = [
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
        }
        }
    ]
    return dict_without_from.copy()


@pytest.fixture
def empty_data():
    return [].copy()


@pytest.fixture
def full_list_of_class():
    data = from_json_to_data(os.path.join("..", 'operations.json'))
    return Operation.born_from_json(data)