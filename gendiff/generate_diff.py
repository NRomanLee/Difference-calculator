import json

def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

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