def start_comparison(dict1, dict2):  # noqa: C901
    '''Function compares two dict-type files.
    Walks through both dicts, detects difference and adds extra-keys.
    Returns diff dict with extra-keys.'''
    result = {}

    def first_dict_walk(dict1, dict2, result_cur):
        for key1 in dict1:
            key2 = key1 in dict2
            is_key1_dict = isinstance(dict1[key1], dict)
            is_key2_dict = isinstance(dict2[key1], dict) if key2 else None

            if not key2:
                result_cur[key1 + "__minus"] = dict1[key1]

            elif is_key1_dict and is_key2_dict:
                result_cur[key1] = {}
                first_dict_walk(dict1[key1], dict2[key1], result_cur[key1])

            elif not is_key1_dict and not is_key2_dict:
                if dict1[key1] != dict2[key1]:
                    result_cur[key1 + "__minus"] = dict1[key1]
                    result_cur[key1 + "__plus"] = dict2[key1]
                else:
                    result_cur[key1 + "__same"] = dict1[key1]

            elif is_key1_dict and not is_key2_dict:
                result_cur[key1 + "__minus"] = {}
                result_cur[key1 + "__minus"] = dict1[key1]
                result_cur[key1 + "__plus"] = dict2[key1]

            elif not is_key1_dict and is_key2_dict:
                result_cur[key1 + "__minus"] = dict1[key1]
                result_cur[key1 + "__plus"] = {}
                result_cur[key1 + "__plus"] = dict2[key1]

    first_dict_walk(dict1, dict2, result)
    return compare_with_second_dict(dict1, dict2, result)


def compare_with_second_dict(dict1, dict2, result):
    '''The second part of comparison process.
    See the start_comparison func to more info.'''
    total_result = result

    def second_dict_walk(dict1, dict2, result_cur):
        for key2 in dict2:
            key1 = key2 in dict1
            is_key1_dict = isinstance(dict1[key2], dict) if key1 else None
            is_key2_dict = isinstance(dict2[key2], dict)

            if not key1:
                if is_key2_dict:
                    result_cur[key2 + "__plus"] = {}
                    result_cur[key2 + "__plus"] = dict2[key2]
                else:
                    result_cur[key2 + "__plus"] = dict2[key2]
            elif is_key1_dict and is_key2_dict:
                second_dict_walk(dict1[key2], dict2[key2], result_cur[key2])

    second_dict_walk(dict1, dict2, total_result)
    return total_result


def compare_dicts(dict1, dict2):
    '''Makes diff dict and returns sorted diff.'''
    diff = start_comparison(dict1, dict2)
    return sort_result(diff)


def sort_result(tree):
    '''Returns sorted dict.'''
    result = {}

    def start(tree, result_cur):
        keys = sorted(tree.keys())
        for key in keys:
            is_key_dict = isinstance(tree[key], dict)
            if is_key_dict:
                result_cur[key] = {}
                start(tree[key], result_cur[key])
            else:
                result_cur[key] = tree[key]

    start(tree, result)
    return result
