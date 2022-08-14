from .stylish_formatter import stylish, change_keys
from .plain_formatter import plain
from .json_formatter import true_false_none_for_tree
from .dict_comparison import compare_dicts


def make_diff(file1, file2, formatter="stylish"):
    '''Function makes sorted diff
     and send it to one of the formatter. 
     The default formatter is stylish. Plain and json formatters available'''
    diff = compare_dicts(file1, file2)

    if formatter == "stylish":
        return stylish(change_keys(diff))

    if formatter == "plain":
        return plain(diff)

    if formatter == "json":
        return true_false_none_for_tree(change_keys(diff))
