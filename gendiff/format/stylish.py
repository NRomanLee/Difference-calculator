def format_value(value, depth):
    if isinstance(value, dict):
        indent = "    " * depth
        lines = ["{"]
        for key, sub_value in value.items():
            lines.append(f"{indent}    {key}: {format_value(sub_value, depth + 1)}")
        lines.append(f"{indent}}}")
        return "\n".join(lines)
    elif isinstance(value, bool):
        return "true" if value else "false"
    elif value is None:
        return "null"
    elif isinstance(value, str):
        return f'"{value}"'
    else:
        return str(value)

def format_stylish(diff, depth=1):
    lines = ['{']
    indent = '    ' * (depth - 1)

    for node in diff:
        key = node['key']
        if node['type'] == 'added':
            lines.append(f"{indent}  + {key}: {format_value(node['value'], depth)}")
        elif node['type'] == 'removed':
            lines.append(f"{indent}  - {key}: {format_value(node['value'], depth)}")
        elif node['type'] == 'unchanged':
            lines.append(f"{indent}    {key}: {format_value(node['value'], depth)}")
        elif node['type'] == 'changed':  
            lines.append(f"{indent}  - {key}: {format_value(node['old_value'], depth)}")
            lines.append(f"{indent}  + {key}: {format_value(node['new_value'], depth)}")
        elif node['type'] == 'nested':
            lines.append(f"{indent}    {key}: {format_stylish(node['children'], depth + 1)}")

    lines.append(f"{indent}}}")
    return '\n'.join(lines)