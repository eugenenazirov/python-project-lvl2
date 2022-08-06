from gendiff.parse_files import parse_files
from gendiff.stylish import stylish
from gendiff.sort_files import sort_files


def generate_diff(file_path1, file_path2, formatter=stylish):
    """GENDIFF func generates the difference between two files, like git diff.
    The func gives two arguments: file_path1 and file_path2
    Supports .json, .yml, .yaml files"""

    file1 = parse_files(file_path1)
    file2 = parse_files(file_path2)
    sorted_files = sort_files(file1, file2)

    # def make_diff(file1: dict, file2: dict, sorted_files: dict):
    #     def walk(node1, node2, depth):
    #         result = []
    #         for i in sorted_files:
    #             if i in file1.keys() & file2.keys():
    #                 if file1[i] == file2[i]:
    #                     yield {'key': i, 'value': file1[i], 'diff': 'both_no_changes'})
    #                 else:
    #                     yield {
    #                         'key': i, 
    #                         'diff': 'both_have_changes', 
    #                         'changes': {
    #                             '-': file1[i],
    #                             '+': file2[i]
    #                         }})
    #             elif i in file1.keys() - file2.keys():
    #                 yield {'key': i, 'value': file1[i], 'diff': 'first_only'})
    #             elif i in file2.keys() - file1.keys():
    #                 yield {'key': i, 'value': file2[i], 'diff': 'second_only'})
    #         return result
    #     return walk(file1, file2, 0)
    # diff = make_diff(file1, file2, sorted_files)
    # result_str = formatter(diff)
    # return result_str

    def make_diff(file1: dict, file2: dict, sorted_files: dict):
        def walk(node1, node2, depth):
            for i in sorted_files:
                if i in file1.keys() & file2.keys():
                    if file1[i] == file2[i]:
                        yield {'key': i, 'value': file1[i], 'diff': 'both_no_changes'}
                    else:
                        yield{
                            'key': i, 
                            'diff': 'both_have_changes', 
                            'changes': {
                                '-': file1[i],
                                '+': file2[i]
                            }}
                elif i in file1.keys() - file2.keys():
                    yield {'key': i, 'value': file1[i], 'diff': 'first_only'}
                elif i in file2.keys() - file1.keys():
                    yield {'key': i, 'value': file2[i], 'diff': 'second_only'}
        return walk(file1, file2, 0)
    diff = make_diff(file1, file2, sorted_files)
    result_str = formatter(diff)
    return result_str
# generate_diff(r'gendiff/files/plain/json/file1.json', r'gendiff/files/plain/json/file2.json')
