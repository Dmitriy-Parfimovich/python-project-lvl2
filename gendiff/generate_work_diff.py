#!/usr/bin/env python

import json
import yaml


# constants
ADDED = 'added'
REMOVED = 'removed'
CONSTANT = 'constant'
CHANGED = 'changed'
NESTED = 'nested'


# -------------------------------------------------------------------------
def get_work_diff(a, b): # noqa
    res = []
    keysA = list(a.keys())
    keysB = list(b.keys())
    keys = list(set(keysA + keysB))
    for elem in keys:
        # -------------------------------------------------------
        if elem in a and elem in b and a[elem] != b[elem]:
            if type(a[elem]) is dict and type(b[elem]) is dict:
                dict_type = {'type': NESTED, 'key': elem, 'value':
                             get_work_diff(a[elem], b[elem])}
                res.append(dict_type)
            else:
                dict_type = {'type': CHANGED, 'key': elem, 'old_value':
                             a[elem], 'new_value': b[elem]}
                res.append(dict_type)
    # -------------------------------------------------------
        if elem in a and elem in b and a[elem] == b[elem]:
            dict_type = {'type': CONSTANT, 'key': elem, 'value': a[elem]}
            res.append(dict_type)
    # -------------------------------------------------------
        if elem not in b:
            dict_type = {'type': REMOVED, 'key': elem, 'value': a[elem]}
            res.append(dict_type)
    # -------------------------------------------------------
        if elem not in a:
            dict_type = {'type': ADDED, 'key': elem, 'value': b[elem]}
            res.append(dict_type)
    return res


def read_file(file_path):
    extension = file_path.split('.')[-1]
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
        return text, extension


def get_dict_from_text(text, extension):
    if extension == 'json':
        text_dict = json.loads(text)
    if extension == 'yaml' or extension == 'yml':
        text_dict = yaml.load(text, Loader=yaml.FullLoader)
    return text_dict


def generate_work_diff(file_path1, file_path2):
    text1, extension1 = read_file(file_path1)
    text2, extension2 = read_file(file_path2)
    text_dict1 = get_dict_from_text(text1, extension1)
    text_dict2 = get_dict_from_text(text2, extension2)
    work_diff = get_work_diff(text_dict1, text_dict2)
    return work_diff
