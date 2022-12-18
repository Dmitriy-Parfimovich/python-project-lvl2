#!/usr/bin/env python

import copy
import itertools
from gendiff.formatter.stylish import convert_to_str
from gendiff.generate_work_diff import ADDED, REMOVED, CHANGED, NESTED


# constants
COMPLEX = '[complex value]'


def get_plain_format(tree): # noqa
    tree = copy.deepcopy(tree)

    def walk(tree, node='', res_lines=[]):
        lines = []
        if type(tree) is list:
            tree = sorted(tree, key=lambda d: d['key'])
        for item in tree:
            for item1 in item:
                children = item[item1]
                if children == NESTED and type(item['value']) is list:
                    node += '.' + item['key']
                    walk(item['value'], node)
                    node = node[::-1]
                    node = node[node.find('.') + 1:]
                    node = node[::-1]
                if children == ADDED:
                    lines.append(f"{node}.{item['key']}")
                    if type(item['value']) is dict:
                        lines.append(COMPLEX)
                    else:
                        lines.append(item['value'])
                    lines.append(ADDED)
                    lines[1] = convert_to_str(lines[1])
                    if lines[1] == COMPLEX or\
                       lines[1] == 'true' or\
                       lines[1] == 'false' or\
                       lines[1] == 'null' or\
                       type(lines[1]) is int:
                        res_lines.append(f"Property '{lines[0][1:]}' was added with value: {lines[1]}") # noqa
                    else:
                        res_lines.append(f"Property '{lines[0][1:]}' was added with value: '{lines[1]}'") # noqa
                    lines = []
                if children == REMOVED:
                    lines.append(f"{node}.{item['key']}")
                    lines.append(REMOVED)
                    res_lines.append(f"Property '{lines[0][1:]}' was removed")
                    lines = []
                if children == CHANGED:
                    lines.append(f"{node}.{item['key']}")
                    if type(item['old_value']) is dict:
                        lines.append(COMPLEX)
                        lines.append(item['new_value'])
                    elif type(item['new_value']) is dict:
                        lines.append(item['old_value'])
                        lines.append(COMPLEX)
                    else:
                        lines.append(item['old_value'])
                        lines.append(item['new_value'])
                    lines.append(CHANGED)
                    lines[1] = convert_to_str(lines[1])
                    lines[2] = convert_to_str(lines[2])
                    if (lines[1] == 'true' or lines[1] == 'false'
                        or lines[1] == 'null'
                        or lines[1] == COMPLEX or type(lines[1]) is int)\
                        and (lines[2] == 'true' or lines[2] == 'false'
                             or lines[2] == 'null' or lines[2] == COMPLEX
                             or type(lines[2]) is int):
                        res_lines.append(f"Property '{lines[0][1:]}' was updated. From {lines[1]} to {lines[2]}") # noqa
                    elif (lines[1] == 'true' or lines[1] == 'false'
                          or lines[1] == 'null'
                          or lines[1] == COMPLEX or type(lines[1]) is int):
                        res_lines.append(f"Property '{lines[0][1:]}' was updated. From {lines[1]} to '{lines[2]}'") # noqa
                    elif (lines[2] == 'true' or lines[2] == 'false'
                          or lines[2] == 'null' or lines[2] == COMPLEX
                          or type(lines[2]) is int):
                        res_lines.append(f"Property '{lines[0][1:]}' was updated. From '{lines[1]}' to {lines[2]}") # noqa
                    else:
                        res_lines.append(f"Property '{lines[0][1:]}' was updated. From '{lines[1]}' to '{lines[2]}'") # noqa
                    lines = []
        result = itertools.chain(res_lines)
        return '\n'.join(result)
    return walk(tree)


# ---------------------------------------------------------------------------
def plain(work_diff):
    return get_plain_format(work_diff)
