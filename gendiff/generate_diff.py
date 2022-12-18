#!/usr/bin/env python


from gendiff.generate_work_diff import read_file
from gendiff.generate_work_diff import get_dict_from_text, get_work_diff
from gendiff.formatter.formatter import formatter


def generate_diff(file_path1, file_path2, format='stylish'):
    text1, extension1 = read_file(file_path1)
    text2, extension2 = read_file(file_path2)
    text_dict1 = get_dict_from_text(text1, extension1)
    text_dict2 = get_dict_from_text(text2, extension2)
    work_diff = get_work_diff(text_dict1, text_dict2)
    return formatter(work_diff, format)
