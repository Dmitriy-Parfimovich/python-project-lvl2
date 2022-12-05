#!/usr/bin/env python

import json
from gendiff.modules.stylish import sort_dict


def get_json(work_diff):
    json_tree = json.dumps(sort_dict(work_diff))
    return json_tree
