import os
import pytest
from utils.function import from_json_to_data


def test_from_json_to_data():
    assert from_json_to_data(os.path.join("test_data", "good.json")) == []


def test_from_json_to_data_with_mistake():
    with pytest.raises(FileNotFoundError):
        from_json_to_data(os.path.join("incorrect_path_to_json.json"))
