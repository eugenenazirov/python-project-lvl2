from pathlib import Path
import pytest
from gendiff import generate_diff


cwd = Path.cwd()


@pytest.fixture
def json1():
    path = Path(cwd, 'tests', 'fixtures', 'plain_json', 'file1.json')
    return path


@pytest.fixture
def json2():
    path = Path(cwd, 'tests', 'fixtures', 'plain_json', 'file2.json')
    return path


def test_gendiff_json(json1, json2):
    assertion_path = Path(cwd, 'tests', 'fixtures', 'assertion_string_plain.txt')
    with open(assertion_path, 'r') as assertion_string:
        assertion_result = assertion_string.read()
    assert generate_diff(json1, json2) == assertion_result


def test_gendiff_with_empty(json1):
    assert generate_diff(json1, "tests/fixtures/empty.json") is None
