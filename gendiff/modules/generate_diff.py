#!/usr/bin/env python

import json
import yaml
from gendiff.modules.stylish import stylish
from gendiff.modules.plain import plain
from gendiff.modules.json_output import get_json
from collections import OrderedDict


# constants
FORMAT_ONE = 'stylish'
FORMAT_TWO = 'plain'
FORMAT_THREE = 'json'


# flake8: noqa
def get_diff_dict(text1, text2):
    key_list, value_list, result = [], [], []
    for key1 in text1.keys():
        for key2 in text2.keys():
            if key1 == key2 and text1[key1] == text2[key2]:
                key_list.append(key1)
                value_list.append(text1[key1])
            if key1 == key2 and text1[key1] != text2[key2]:
                key_list.append(f'{key1}-X_*')
                key_list.append(f'{key2}-Y_*')
                value_list.append(text1[key1])
                value_list.append(text2[key2])
            if key1 not in text2.keys():
                key_list.append(f'{key1}-X_*')
                value_list.append(text1[key1])
            if key2 not in text1.keys():
                key_list.append(f'{key2}-Y_*')
                value_list.append(text2[key2])
    result = dict(zip(key_list, value_list)).items()
    result = dict(sorted(result))
    ordered_result = OrderedDict(result.items())
    return ordered_result


def get_correct_output(ordered_result):
    total_output = ''
    ordered_result_right = OrderedDict()
    for key in ordered_result:
        key_list = list(key)
        if key_list[-4::] != ['-', 'X', '_', '*'] and\
           key_list[-4::] != ['-', 'Y', '_', '*']:
            ordered_result_right['  ' + key] = ordered_result[key]
        if key_list[-4::] == ['-', 'X', '_', '*']:
            key_list = key_list[0:-4]
            new_key = ['- ' + ''.join(key_list)]
            ordered_result_right[new_key[0]] = ordered_result[key]
        if key_list[-4::] == ['-', 'Y', '_', '*']:
            key_list = key_list[0:-4]
            new_key = ['+ ' + ''.join(key_list)]
            ordered_result_right[new_key[0]] = ordered_result[key]
    for key, value in ordered_result_right.items():
        one_output_line = str(f'  {key}: {str(value).lower()}')
        total_output += '\n' + one_output_line
    return '{' + f'{total_output}' + '\n}'


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
    if format == FORMAT_ONE:
        return stylish(text_dict1, text_dict2)
    if format == FORMAT_TWO:
        return plain(text_dict1, text_dict2)
    if format == FORMAT_THREE:
        return get_json(text_dict1, text_dict2)
    else:
        ordered_result = get_diff_dict(text_dict1, text_dict2)
        return get_correct_output(ordered_result)
