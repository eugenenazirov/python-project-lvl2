from gendiff.parse_files import parse_files


def generate_diff(file_path1, file_path2):
    """GENDIFF func generates the difference between two files, like git diff.
    The func gives two arguments: file_path1 and file_path2
    Supports .json, .yml, .yaml files"""

    file1 = parse_files(file_path1)
    file2 = parse_files(file_path2)
    merged_files = file1 | file2
    sorted_list = sorted(merged_files.items(), key=lambda x: x[0])
    sorted_files = dict(sorted_list)
    result = '{' + '\n'
    for i in sorted_files:
        if i in file1.keys() & file2.keys():
            if file1[i] == file2[i]:
                result = result + '    ' + i + ': ' + str(file1[i]) + '\n'
            else:
                result = result + '  - ' + i + ': ' + str(file1[i]) + '\n'
                result = result + '  + ' + i + ': ' + str(file2[i]) + '\n'
        elif i in file1.keys() - file2.keys():
            result = result + '  - ' + i + ': ' + str(file1[i]) + '\n'
        elif i in file2.keys() - file1.keys():
            result = result + '  + ' + i + ': ' + str(file2[i]) + '\n'
    result = result + '}'
    return result.lower()


# print(generate_diff(r'gendiff/files/file1.json', r'gendiff/files/file2.json'))
