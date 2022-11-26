#!/usr/bin/env python

import json
from gendiff.modules.stylish import walk, sort_dict


def get_json(text1, text2):
    json_tree = json.dumps(sort_dict(walk(text1, text2)))
    return json_tree
