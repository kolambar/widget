import os
import pytest
from utils.function import from_json_to_data
import json

def test_from_json_to_data():
    assert from_json_to_data(os.path.join("test_data", "good.json")) == []


def test_time_metamorphosis():
    date = "2018-06-30T02:08:58.425572"
    assert time_metamorphosis(date) == "2018-06-30 02:08:58"
    date = "2018-06-30T02:08:58.585572"
    assert time_metamorphosis(date) == "2018-06-30 02:08:59"


def test_from_json_to_data_with_mistake():
    # with pytest.raises(NameError):
    #     from_json_to_data(os.path.join("test_data", "incorrect_json.json"))
    with pytest.raises(FileNotFoundError):
        from_json_to_data(os.path.join("incorrect_path_to_json.json"))