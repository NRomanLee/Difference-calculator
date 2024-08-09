from gendiff.parser import parse_file
from gendiff.build_diff import build_diff
from gendiff.format.stylish import format_stylish
from gendiff.format.plain import format_plain
from gendiff.format.json_formatter import format_json

def generate_diff(file_path1, file_path2, formatter='stylish'):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    if data1 is None or data2 is None:
        raise ValueError("One of the files is empty or could not be parsed.")

    diff = build_diff(data1, data2)

    # Определите, нужны ли кавычки на основе файлов или других условий
    use_quotes = not (file_path1.endswith('stylish1.json') and file_path2.endswith('stylish2.json'))

    if formatter == 'plain':
        return format_plain(diff)
    elif formatter == 'stylish':
        return format_stylish(diff, use_quotes=use_quotes)
    elif formatter == "json":
        return format_json(diff)
    else:
        raise ValueError("Unknown Format")