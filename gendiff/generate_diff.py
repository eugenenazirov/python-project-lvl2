from gendiff.parse_files import parse_files
from gendiff.stylish import stylish
from gendiff.make_diff import make_diff


def generate_diff(file_path1, file_path2, formatter=stylish):
    """GENDIFF func generates the difference between two files, like git diff.
    The func gives two arguments: file_path1 and file_path2
    Supports .json, .yml, .yaml files"""

    file1 = parse_files(file_path1)
    file2 = parse_files(file_path2)

    diff = make_diff(file1, file2)
    result_str = formatter(diff)
    return result_str
