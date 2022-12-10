#!/usr/bin/env python


from gendiff.generate_work_diff import generate_work_diff
from gendiff.stylish import stylish
from gendiff.plain import plain
from gendiff.json_output import get_json


# constants
FORMAT_ONE = 'stylish'
FORMAT_TWO = 'plain'
FORMAT_THREE = 'json'


def generate_diff(file_path1, file_path2, format='stylish'):
    work_diff = generate_work_diff(file_path1, file_path2)
    if format == FORMAT_ONE:
        return stylish(work_diff)
    if format == FORMAT_TWO:
        return plain(work_diff)
    if format == FORMAT_THREE:
        return get_json(work_diff)
    else:
        raise ValueError('Please, enter the correct format.')
