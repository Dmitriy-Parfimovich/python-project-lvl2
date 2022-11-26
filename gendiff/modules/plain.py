#!/usr/bin/env python

import copy
import itertools
from gendiff.modules.stylish import walk, sort_dict


def get_plain_list(tree): # noqa
    tree = copy.deepcopy(tree)

    def walk(tree, node='', lines=[]):
        for item in tree:
            for item1 in item:
                children = item[item1]
                if children == '=' and type(item['value']) is list:
                    node += '.' + item['key']
                    walk(item['value'], node)
                    node = node[::-1]
                    node = node[node.find('.') + 1:]
                    node = node[::-1]
                if children == '+':
                    lines.append(f"{node}.{item['key']}")
                    if type(item['value']) is dict:
                        lines.append('[complex value]')
                    else:
                        lines.append(item['value'])
                    lines.append('added')
                if children == '-':
                    lines.append(f"{node}.{item['key']}")
                    lines.append('removed')
                if children == '-+':
                    lines.append(f"{node}.{item['key']}")
                    if type(item['old_value']) is dict:
                        lines.append('[complex value]')
                        lines.append(item['new_value'])
                    elif type(item['new_value']) is dict:
                        lines.append(item['old_value'])
                        lines.append('[complex value]')
                    else:
                        lines.append(item['old_value'])
                        lines.append(item['new_value'])
                    lines.append('updated')
        return lines
    return walk(tree)


def get_plain_format(lines): # noqa
    res_lines = []
    for elem in lines:
        if elem == 'added':
            if lines[1] is True:
                lines[1] = 'true'
            if lines[1] is False:
                lines[1] = 'false'
            if lines[1] is None:
                lines[1] = 'null'
            if lines[1] == '[complex value]' or\
               lines[1] == 'true' or\
               lines[1] == 'false' or\
               lines[1] == 'null' or\
               type(lines[1]) is int:
                res_lines.append(f"Property '{lines[0][1:]}' was added with value: {lines[1]}") # noqa
            else:
                res_lines.append(f"Property '{lines[0][1:]}' was added with value: '{lines[1]}'") # noqa
            lines = lines[3:]
        if elem == 'removed':
            res_lines.append(f"Property '{lines[0][1:]}' was removed")
            lines = lines[2:]
        if elem == 'updated':
            if lines[1] is True:
                lines[1] = 'true'
            if lines[1] is False:
                lines[1] = 'false'
            if lines[1] is None:
                lines[1] = 'null'
            if lines[2] is True:
                lines[2] = 'true'
            if lines[2] is False:
                lines[2] = 'false'
            if lines[2] is None:
                lines[2] = 'null'
            if (lines[1] == 'true' or lines[1] == 'false' or lines[1] == 'null'
                or lines[1] == '[complex value]' or type(lines[1]) is int)\
                and (lines[2] == 'true' or lines[2] == 'false'
                     or lines[2] == 'null' or lines[2] == '[complex value]'
                     or type(lines[2]) is int):
                res_lines.append(f"Property '{lines[0][1:]}' was updated. From {lines[1]} to {lines[2]}") # noqa
            elif (lines[1] == 'true' or lines[1] == 'false'
                  or lines[1] == 'null'
                  or lines[1] == '[complex value]' or type(lines[1]) is int):
                res_lines.append(f"Property '{lines[0][1:]}' was updated. From {lines[1]} to '{lines[2]}'") # noqa
            elif (lines[2] == 'true' or lines[2] == 'false'
                  or lines[2] == 'null' or lines[2] == '[complex value]'
                  or type(lines[2]) is int):
                res_lines.append(f"Property '{lines[0][1:]}' was updated. From '{lines[1]}' to {lines[2]}") # noqa
            else:
                res_lines.append(f"Property '{lines[0][1:]}' was updated. From '{lines[1]}' to '{lines[2]}'") # noqa
            lines = lines[4:]
    result = itertools.chain(res_lines)
    return '\n'.join(result)


# ---------------------------------------------------------------------------
def plain(text1, text2):
    return get_plain_format(get_plain_list(sort_dict(walk(text1, text2))))
