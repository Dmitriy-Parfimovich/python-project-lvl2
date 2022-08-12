import json
from collections import OrderedDict


def get_correct_output(ordered_result):
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
    print('{')
    for key, value in ordered_result_right.items():
        print(f'  {key}: {str(value).lower()}')
    print('}')


def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r', encoding='utf-8') as f1:
        text1 = json.load(f1)
    with open(file_path2, 'r', encoding='utf-8') as f2:
        text2 = json.load(f2)
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
    get_correct_output(ordered_result)
