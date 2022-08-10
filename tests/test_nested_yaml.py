from pathlib import Path
import pytest
from gendiff import generate_diff


cwd = Path.cwd()


@pytest.fixture
def yaml1():
    path = Path(cwd, 'tests', 'fixtures', 'nested_yaml', 'file1.yaml')
    return path


@pytest.fixture
def yaml2():
    path = Path(cwd, 'tests', 'fixtures', 'nested_yaml', 'file2.yml')
    return path


def test_gendiff_yaml(yaml1, yaml2):
    assertion_path = Path(cwd, 'tests', 'fixtures', 'assertion_string_nested.txt')
    with open(assertion_path, 'r') as assertion_string:
        assertion_result = assertion_string.read()
    assert generate_diff(yaml1, yaml2) == assertion_result


def test_gendiff_json_formatter_plain(yaml1, yaml2):
    assertion_path = Path(cwd, 'tests', 'fixtures', 'assertion_string_formatter_plain.txt')
    with open(assertion_path, 'r') as assertion_string:
        assertion_result = assertion_string.read()
    assert generate_diff(yaml1, yaml2, formatter='plain') == assertion_result


def test_gendiff_with_empty(yaml1):
    assert generate_diff(yaml1, "tests/fixtures/empty.yml") is None
