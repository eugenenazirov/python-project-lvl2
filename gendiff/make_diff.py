from .stylish_formatter import stylish, change_keys
from .plain_formatter import plain
from .json_formatter import true_false_none_for_tree


def compare(dict1, dict2):  # noqa: C901
    result = {}

    def start(dict1, dict2, result_cur):
        for key1 in dict1:
            key2 = key1 in dict2
            is_key1_dict = isinstance(dict1[key1], dict)
            is_key2_dict = isinstance(dict2[key1], dict) if key2 else None

            if not key2:
                result_cur[key1 + "__minus"] = dict1[key1]

            elif is_key1_dict and is_key2_dict:
                result_cur[key1] = {}
                start(dict1[key1], dict2[key1], result_cur[key1])

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

    start(dict1, dict2, result)
    return compare_second(dict1, dict2, result)


def compare_second(dict1, dict2, result):
    total_result = result

    def start(dict1, dict2, result_cur):
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
                start(dict1[key2], dict2[key2], result_cur[key2])

    start(dict1, dict2, total_result)
    return total_result


def sort_dict(tree):
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


def make_diff(file1, file2, formatter="stylish"):
    compare_ = compare(file1, file2)
    sort_dict_ = sort_dict(compare_)

    if formatter == "stylish":
        return stylish(change_keys(sort_dict_))

    if formatter == "plain":
        return plain(sort_dict_)

    if formatter == "json":
        return true_false_none_for_tree(change_keys(sort_dict_))
