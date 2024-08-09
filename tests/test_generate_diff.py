import os
import pytest
from gendiff.diff_generator import generate_diff

@pytest.fixture
def read_file():
    def _read_file(file_path):
        with open(file_path, "r") as file:
            return file.read().strip()
    return _read_file

def test_generate_diff_json(read_file):
    file1_path = os.path.join("tests", "fixtures", "file1.json")
    file2_path = os.path.join("tests", "fixtures", "file2.json")
    expected_diff_path = os.path.join("tests", "fixtures", "expected_diff.txt")

    expected_diff = read_file(expected_diff_path)
    actual_diff = generate_diff(file1_path, file2_path).strip()
    assert actual_diff == expected_diff

def test_generate_diff_yaml(read_file):
    file1_path = os.path.join("tests", "fixtures", "file1.yml")
    file2_path = os.path.join("tests", "fixtures", "file2.yml")
    expected_diff_path = os.path.join("tests", "fixtures", "expected_diffyml.txt")

    expected_diff = read_file(expected_diff_path)
    actual_diff = generate_diff(file1_path, file2_path).strip()
    assert actual_diff == expected_diff

def test_generate_diff_stylish(read_file):
    file1_path = os.path.join("tests", "fixtures", "stylish1.json")
    file2_path = os.path.join("tests", "fixtures", "stylish2.json")
    expected_diff_path = os.path.join("tests", "fixtures", "expected_stylish.txt")

    expected_diff = read_file(expected_diff_path)
    actual_diff = generate_diff(file1_path, file2_path, formatter='stylish').strip()
    assert actual_diff == expected_diff

def test_generate_diff_plain(read_file):
    file1_path = os.path.join("tests", "fixtures", "plain1.json")
    file2_path = os.path.join("tests", "fixtures", "plain2.json")
    expected_diff_file_path = os.path.join("tests", "fixtures", "expected_plain.txt")

    expected_diff = read_file(expected_diff_file_path)
    actual_diff = generate_diff(file1_path, file2_path, formatter='plain').strip()
    assert actual_diff == expected_diff

def test_generate_diff_json_format(read_file):
    file1_path = os.path.join("tests", "fixtures", "file1.json")
    file2_path = os.path.join("tests", "fixtures", "file2.json")
    expected_diff_path = os.path.join("tests", "fixtures", "expected_diff_json.txt")

    expected_diff = read_file(expected_diff_path)
    actual_diff = generate_diff(file1_path, file2_path, 'json').strip()
    assert actual_diff == expected_diff

