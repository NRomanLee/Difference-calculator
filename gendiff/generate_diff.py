from gendiff.parser import parse_file
from gendiff.build_diff import build_diff
from gendiff.format.stylish import format_stylish
from gendiff.format.plain import format_plain 

def generate_diff(file_path1, file_path2, formatter='stylish'):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    if data1 is None or data2 is None:
        raise ValueError("One of the files is empty or could not be parsed.")

    diff = build_diff(data1, data2)

    if formatter == 'plain':
        return format_plain(diff)
    elif formatter == 'stylish':
        return format_stylish(diff)
    else:
        raise ValueError("Unknown Format")
        