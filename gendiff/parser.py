import json
import yaml
import argparse


def parse(data: str, format: str):
    if format == 'json':
        return json.loads(data)
    elif format == 'yaml':
        return yaml.load(data, Loader=yaml.FullLoader) or {}
    raise ValueError("Неподдерживаемый формат файла")


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('file_path_1')
    parser.add_argument('file_path_2')
    parser.add_argument(
        "-f",
        "--format",
        choices=['json', 'plain', 'stylish'],
        default='stylish',
        help="set format of output (default: 'stylish')")
    return parser.parse_args()
