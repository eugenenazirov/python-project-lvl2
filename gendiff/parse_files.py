import json
import yaml


def parse_json(file_path):
    '''Returns parsed json file in dict representation.
    Takes path to json file.'''
    file = json.load(open(file_path))
    return file


def parse_yaml(file_path):
    '''Returns parsed yaml file in dict representation.
    Takes path to yaml file.'''
    file = yaml.load(open(file_path), Loader=yaml.Loader)
    return file


def parse_files(file_path):
    '''Detect file type (json or yaml)
    and returns the result of calling the corresponding functions'''
    path_to_str = str(file_path)
    if path_to_str.endswith('.json'):
        return parse_json(file_path)
    elif path_to_str.endswith('.yml') or path_to_str.endswith('.yaml'):
        return parse_yaml(file_path)
