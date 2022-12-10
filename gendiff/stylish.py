#!/usr/bin/env python

import copy
import itertools


# constants
ADDED = 'added'
REMOVED = 'removed'
CONSTANT = 'constant'
CHANGED = 'changed'
NESTED = 'nested'


# -------------------------------------------------------------------------
def convert_to_str(value):
    if value is True:
        value = 'true'
    if value is False:
        value = 'false'
    if value is None:
        value = 'null'
    return value


# -------------------------------------------------------------------------
def get_decoded_dict(value): # noqa
    tree = copy.deepcopy(value)
    if type(tree) is list:
        tree = sorted(tree, key=lambda d: d['key'])
    for item in tree:
        if type(item) is dict:
            for item1 in item:
                if type(item[item1]) is list and type(item[item1][0]) is dict:
                    item[item1] = get_decoded_dict(item[item1])
                if type(item[item1]) is dict:
                    item[item1] = get_decoded_dict(item[item1])
                if item[item1] == CONSTANT or item[item1] == NESTED:
                    item['  ' + item['key']] = item.pop('value')
                if item[item1] == REMOVED:
                    item['- ' + item['key']] = item.pop('value')
                if item[item1] == ADDED:
                    item['+ ' + item['key']] = item.pop('value')
                if item[item1] == CHANGED:
                    item['- ' + item['key']] = item.pop('old_value')
                    item['+ ' + item['key']] = item.pop('new_value')
                item[item1] = convert_to_str(item[item1])
            del item['type']
            del item['key']
        if type(item) is not dict:
            if tree[item] == CONSTANT or tree[item] == NESTED:
                tree[tree['  ' + 'key']] = tree.pop('value')
            if tree[item] == REMOVED:
                tree['- ' + tree['key']] = tree.pop('value')
            if tree[item] == ADDED:
                tree['+ ' + tree['key']] = tree.pop('value')
            if tree[item] == CHANGED:
                tree['- ' + tree['key']] = tree.pop('old_value')
                tree['+ ' + tree['key']] = tree.pop('new_value')
            tree[item] = convert_to_str(tree[item])
    return tree

# -------------------------------------------------------------------------
def stringify(value, replacer=' ', spaces_count=1): # noqa

    def iter_(current_value, depth):
        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for item in current_value:
            if type(item) is dict:
                for key, val in item.items():
                    if (type(val) is list and type((val)[0]) is dict) or type(val) is dict: # noqa
                        lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size+2)}') # noqa
                    else:
                        lines.append(f'{deep_indent}{key}: {val}')
            else:
                if type(current_value[item]) is dict:
                    lines.append(f'{replacer * (deep_indent_size+2)}{item}: {iter_(current_value[item], deep_indent_size+2)}') # noqa
                else:
                    lines.append(f'{replacer * (deep_indent_size+2)}{item}: {current_value[item]}') # noqa
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    return iter_(value, 0)


# ---------------------------------------------------------------------------
def stylish(work_diff):
    return stringify(get_decoded_dict(work_diff), ' ', 2)
