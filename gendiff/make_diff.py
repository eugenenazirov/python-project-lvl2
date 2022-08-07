def get_children(value):
        return list(value.items()) if isinstance(value, dict) else None

def get_description(key: str, value, diff_type: str, changes=None):
    return {
        'key': key,
        'value': value,
        'diff': diff_type,
        'changes': changes,
        'children': get_children(value)
        }

def make_diff(file1: dict, file2: dict):
    
    def sort_files(file1, file2):
        merged_files = file1 | file2
        sorted_list = sorted(merged_files.items(), key=lambda x: x[0])
        sorted_files = dict(sorted_list)
        return sorted_files

    sorted_files = sort_files(file1, file2)
    result = []
    for i in sorted_files:
        if i in file1.keys() & file2.keys():
            value1, value2 = file1[i], file2[i]
            if value1 == value2:
                result.append(get_description(key=i, value=value1, diff_type='both_no_changes'))
            elif value1 != value2 and all((isinstance(value1, dict), isinstance(value2, dict))):
                result.append(get_description(key=i, value=None, diff_type='both_dicts', changes={
                    '-': value1,
                    '+': value2
                }))
                # make_diff(value1, value2, sort_files(value1, value2))
            else:
                result.append(get_description(key=i, value=None, diff_type='both_have_changes', changes={
                    '-': value1,
                    '+': value2}))
        elif i in file1.keys() - file2.keys():
            result.append(get_description(key=i, value=file1[i], diff_type='first_only'))
        elif i in file2.keys() - file1.keys():
            result.append(get_description(key=i, value=file2[i], diff_type='second_only'))
        else:
            raise Exception('Incorrect data!')
    return result
