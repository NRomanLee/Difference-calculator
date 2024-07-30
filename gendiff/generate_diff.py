import json

def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

    all_keys = sorted(set(data1.keys()).union(set(data2.keys())))
    diff_lines = []

    for key in all_keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff_lines.append(f"  {key}: {data1[key]}")
            else:
                diff_lines.append(f"- {key}: {data1[key]}")
                diff_lines.append(f"+ {key}: {data2[key]}")
        elif key in data1:
            diff_lines.append(f"- {key}: {data1[key]}")
        elif key in data2:
            diff_lines.append(f"+ {key}: {data2[key]}")

    return "{\n" + "\n".join(diff_lines) + "\n}"