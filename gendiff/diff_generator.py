from gendiff.read_file import read_file
from collections import OrderedDict
from gendiff.format.stylish_formated import format_stylish
from gendiff.format.plain_formated import format_plain
from gendiff.format.json_formated import format_json


def gen_diff(data1, data2) -> dict:
    diff = {}
    keys = set(data1.keys() | set(data2.keys()))

    for key in keys:
        if isinstance(data1.get(key), dict) and isinstance(data2.get(key), dict):
            diff[key] = {'type': 'nested',
                         'value': gen_diff(data1[key], data2[key])}
        elif key not in data1.keys():
            diff[key] = {'type': 'added', 'value': data2[key]}
        elif key not in data2.keys():
            diff[key] = {'type': 'removed', 'value': data1[key]}
        elif data1[key] == data2[key]:
            diff[key] = {'type': 'unchanged', 'value': data1[key]}
        else:
            diff[key] = {'type': 'changed', 'old': data1[key], 'new': data2[key]}

    return OrderedDict(sorted(diff.items(), key=lambda k: k))


def generate_diff(data1: str, data2: str, format='stylish'):
    old_file = read_file(data1)
    new_file = read_file(data2)
    diff = gen_diff(old_file, new_file)

    match format:
        case None:
            return format_stylish(diff)
        case 'stylish':
            return format_stylish(diff)
        case 'plain':
            return format_plain(diff)
        case 'json':
            return format_json(diff)
