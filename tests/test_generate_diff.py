
import os
import pytest
from gendiff.generate_diff import generate_diff

@pytest.fixture
def read_file():
    def _read_file(file_path):
        with open(file_path, "r") as file:
            return file.read().strip()
    return _read_file

def test_generate_diff(read_file):
    file1_path = os.path.join("tests", "fixtures", "file1.json")
    file2_path = os.path.join("tests", "fixtures", "file2.json")
    expected_diff_path = os.path.join("tests", "fixtures", "expected_diff.json")
    
    expected_diff = read_file(expected_diff_path).strip()
    actual_diff = generate_diff(file1_path, file2_path).strip()
    assert actual_diff == expected_diff
