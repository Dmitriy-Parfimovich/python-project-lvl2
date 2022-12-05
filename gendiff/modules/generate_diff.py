#!/usr/bin/env python

import json
import yaml
from gendiff.modules.stylish import stylish
from gendiff.modules.plain import plain
from gendiff.modules.json_output import get_json


# constants
FORMAT_ONE = 'stylish'
FORMAT_TWO = 'plain'
FORMAT_THREE = 'json'


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
                dict_type = {'type': '=', 'key': elem, 'value':
                             get_work_diff(a[elem], b[elem])}
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


def generate_diff(file_path1, file_path2, format='stylish'):
    text1, extension1 = read_file(file_path1)
    text2, extension2 = read_file(file_path2)
    text_dict1 = get_dict_from_text(text1, extension1)
    text_dict2 = get_dict_from_text(text2, extension2)
    work_diff = get_work_diff(text_dict1, text_dict2)
    if format == FORMAT_ONE:
        return stylish(work_diff)
    if format == FORMAT_TWO:
        return plain(work_diff)
    if format == FORMAT_THREE:
        return get_json(work_diff)
    else:
        raise ValueError('Please, enter the correct format.')
