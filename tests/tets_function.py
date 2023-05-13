from utils.function import from_json_to_data
import os
import pytest

def test_from_json_to_data():
    assert from_json_to_data(os.path.join("test_data", "good.json")) == []


def test_with_mistake_from_json_to_data():
    with pytest.raises(NameError):
        from_json_to_data(incorrect_path_to_json)
    with pytest.raises(FileNotFoundError):
        from_json_to_data("incorrect_path_to_json")