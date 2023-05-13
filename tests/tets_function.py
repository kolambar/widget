from utils.function import from_json_to_data
import os

def test_from_json_to_data():
    assert from_json_to_data(os.path.join("test_data", "good.json")) == []