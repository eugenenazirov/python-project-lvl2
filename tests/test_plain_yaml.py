from pathlib import Path
import pytest
from gendiff import generate_diff


cwd = Path.cwd()


@pytest.fixture
def yaml1():
    path = Path(cwd, 'tests', 'fixtures', 'plain_yaml', 'file1.yml')
    return path


@pytest.fixture
def yaml2():
    path = Path(cwd, 'tests', 'fixtures', 'plain_json', 'file2.yaml')
    return path


def test_gendiff_yaml(yaml1, yaml2):
    assertion_path = Path(cwd, 'tests', 'fixtures', 'assertion_string.txt')
    with open(assertion_path, 'r') as assertion_string:
        assertion_result = assertion_string.read()
    assert generate_diff(yaml1, yaml2) == assertion_result
