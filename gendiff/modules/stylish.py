import copy
import itertools

# -------------------------------------------------------------------------
def walk(a, b): # noqa
    res = []
    keysA = list(a.keys())
    keysB = list(b.keys())
    keys = list(set(keysA + keysB))
    for elem in keys:
        # -------------------------------------------------------
        if elem in a and elem in b and a[elem] != b[elem]:
            if type(a[elem]) is dict and type(b[elem]) is dict:
                dict_type = {'type': '=', 'key': elem, 'value':
                             walk(a[elem], b[elem])}
                res.append(dict_type)
            else:
                dict_type = {'type': '-+', 'key': elem, 'old_value':
                             a[elem], 'new_value': b[elem]}
                res.append(dict_type)
    # -------------------------------------------------------
        if elem in a and elem in b and a[elem] == b[elem]:
            dict_type = {'type': '=', 'key': elem, 'value': a[elem]}
            res.append(dict_type)
# -------------------------------------------------------
        if elem not in b:
            dict_type = {'type': '-', 'key': elem, 'value': a[elem]}
            res.append(dict_type)
# -------------------------------------------------------
        if elem not in a:
            dict_type = {'type': '+', 'key': elem, 'value': b[elem]}
            res.append(dict_type)
    return res


# -------------------------------------------------------------------------
def sort_dict(a):
    for item in a:
        if 'value' in item and type(item['value']) is list and\
           type(item['value'][0]) is dict:
            item['value'] = sorted(sort_dict(item['value']),
                                   key=lambda d: d['key'])
        if 'old_value' in item and type(item['old_value']) is list and\
           type(item['old_value'][0]) is dict:
            item['old_value'] = sorted(sort_dict(item['old_value']),
                                       key=lambda d: d['key'])
        if 'new_value' in item and type(item['new_value']) is list and\
           type(item['new_value'][0]) is dict:
            item['new_value'] = sorted(sort_dict(item['new_value']),
                                       key=lambda d: d['key'])
    for item in a:
        a = sorted(a, key=lambda d: d['key'])
    return a

# -------------------------------------------------------------------------
def get_decoded_dict(value): # noqa
    tree = copy.deepcopy(value)
    for item in tree:
        if type(item) is dict:
            for item1 in item:
                if type(item[item1]) is list and type(item[item1][0]) is dict:
                    item[item1] = get_decoded_dict(item[item1])
                if type(item[item1]) is dict:
                    item[item1] = get_decoded_dict(item[item1])
                if item[item1] == '=':
                    item['  ' + item['key']] = item.pop('value')
                if item[item1] == '-':
                    item['- ' + item['key']] = item.pop('value')
                if item[item1] == '+':
                    item['+ ' + item['key']] = item.pop('value')
                if item[item1] == '-+':
                    item['- ' + item['key']] = item.pop('old_value')
                    item['+ ' + item['key']] = item.pop('new_value')
                if item[item1] is True:
                    item[item1] = 'true'
                if item[item1] is False:
                    item[item1] = 'false'
                if item[item1] is None:
                    item[item1] = 'null'
            del item['type']
            del item['key']
        if type(item) is not dict:
            if tree[item] == '=':
                tree[tree['  ' + 'key']] = tree.pop('value')
            if tree[item] == '-':
                tree['- ' + tree['key']] = tree.pop('value')
            if tree[item] == '+':
                tree['+ ' + tree['key']] = tree.pop('value')
            if tree[item] == '-+':
                tree['- ' + tree['key']] = tree.pop('old_value')
                tree['+ ' + tree['key']] = tree.pop('new_value')
            if tree[item] is True:
                tree[item] = 'true'
            if tree[item] is False:
                tree[item] = 'false'
            if tree[item] is None:
                tree[item] = 'null'
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


# -------------------------------------------------------------------------
def stylish(text1, text2):
    return stringify(get_decoded_dict(sort_dict(walk(text1, text2))), ' ', 2)
