import pytest


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
