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
