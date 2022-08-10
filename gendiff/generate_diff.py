from .parse_files import parse_files
from .make_diff import make_diff


def generate_diff(file_path1, file_path2, formatter="stylish"):
    """GENDIFF func generates the difference between two files, like git diff.
    The func gives two arguments: file_path1 and file_path2
    Supports .json, .yml, .yaml files"""
    print(f'{formatter=}')
    with open(file_path1) as f1_open:
        with open(file_path2) as f2_open:
            if len(f1_open.read()) == 0 or len(f2_open.read()) == 0:
                return

    file1 = parse_files(file_path1)
    file2 = parse_files(file_path2)

    keys1 = list(file1.keys())
    keys2 = list(file2.keys())

    if len(keys1) == 0 and len(keys2) == 0:
        return

    result = make_diff(file1, file2, formatter)
    return result
