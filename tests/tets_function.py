import os
import pytest
import datetime
from utils.function import from_json_to_data, time_metamorphosis


def test_from_json_to_data():
    assert from_json_to_data(os.path.join("test_data", "good.json")) == []


def test_from_json_to_data_with_mistake():
    with pytest.raises(FileNotFoundError):
        from_json_to_data(os.path.join("incorrect_path_to_json.json"))


def test_time_metamorphosis():
    date = "2018-06-30T02:08:58.425572"
    data_to_compare, data_to_print = time_metamorphosis(date)
    assert data_to_compare == datetime.datetime(2018, 6, 30, 2, 8, 58, 425572)
    assert data_to_print == "30.06.2018"


# def test_blur_sender():
#     assert blur_sender('Maestro 1596837868705199') == '1596 83** **** 5199'
#     assert blur_sender('MasterCard 7158300734726758') == '7158 30** **** 6758'
#     assert blur_senderm('Счет 75106830613657916952') == '7510 68** **** 6952'
#     assert blur_sender('Счета отправителя нет. Это операция по открытию вклада.') == 'Счета отправителя нет. Это операция по открытию вклада.'
#     assert blur_sender('Visa Classic 6831982476737658') == '6831 98** **** 7658'