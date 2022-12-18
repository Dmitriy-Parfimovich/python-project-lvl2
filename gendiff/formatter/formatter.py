#!/usr/bin/env python

from gendiff.formatter.stylish import stylish
from gendiff.formatter.plain import plain
from gendiff.formatter.json_output import get_json


# constants
FORMAT_ONE = 'stylish'
FORMAT_TWO = 'plain'
FORMAT_THREE = 'json'


def formatter(diff, format):
    if format == FORMAT_ONE:
        return stylish(diff)
    if format == FORMAT_TWO:
        return plain(diff)
    if format == FORMAT_THREE:
        return get_json(diff)
    else:
        raise ValueError('Please, enter the correct format.')
