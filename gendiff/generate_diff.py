from gendiff.parser import parse_file


def generate_diff(file_path1, file_path2):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    if data1 is None or data2 is None:
        raise ValueError("One of the files is empty or could not be parsed.")

    all_keys = sorted(set(data1.keys()).union(set(data2.keys())))
    diff_lines = []

    def format_value(value):
        if isinstance(value, bool):
            return 'true' if value else 'false'
        if isinstance(value, str):
            return f'"{value}"'
        return str(value)

    for key in all_keys:
        if key in data1 and key not in data2:
            diff_lines.append(f'  - {key}: {format_value(data1[key])}')
        elif key not in data1 and key in data2:
            diff_lines.append(f'  + {key}: {format_value(data2[key])}')
        elif data1[key] != data2[key]:
            diff_lines.append(f'  - {key}: {format_value(data1[key])}')
            diff_lines.append(f'  + {key}: {format_value(data2[key])}')
        else:
            diff_lines.append(f'    {key}: {format_value(data1[key])}')

    return "{\n" + "\n".join(diff_lines) + "\n}"
