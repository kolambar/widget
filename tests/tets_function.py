import os
import pytest
from utils.function import from_json_to_data, time_metamorphosis
import datetime


def test_from_json_to_data():
    assert from_json_to_data(os.path.join("test_data", "good.json")) == []


def test_time_metamorphosis():
    date = "2018-06-30T02:08:58.425572"
    data_to_compare, data_to_print = time_metamorphosis(date)
    assert data_to_compare == datetime.datetime(2018, 6, 30, 2, 8, 58, 425572)
    assert data_to_print == "30.06.2018"


def test_from_json_to_data_with_mistake():
    with pytest.raises(FileNotFoundError):
        from_json_to_data(os.path.join("incorrect_path_to_json.json"))
    # with pytest.raises(NameError):
    #     from_json_to_data(os.path.join("test_data", "incorrect_json.json"))
