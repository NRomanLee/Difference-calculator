def format_value(value, depth, use_quotes=True):
    if isinstance(value, dict):
        indent = "    " * depth
        lines = ["{"]
        for key, sub_value in value.items():
            lines.append(
                f"{indent}    {key}: {format_value(sub_value, depth + 1, use_quotes)}")
        lines.append(f"{indent}}}")
        return "\n".join(lines)
    elif isinstance(value, bool):
        return "true" if value else "false"
    elif value is None:
        return "null"
    elif isinstance(value, str):
        # Используем кавычки, если use_quotes равно True
        return f'"{value}"' if use_quotes else value
    else:
        return str(value)


def format_node(node, indent, depth, use_quotes):
    key = node['key']
    if node['type'] == 'added':
        return f"{indent}  + {key}: {format_value(node['value'], depth, use_quotes)}"
    elif node['type'] == 'removed':
        return f"{indent}  - {key}: {format_value(node['value'], depth, use_quotes)}"
    elif node['type'] == 'unchanged':
        return f"{indent}    {key}: {format_value(node['value'], depth, use_quotes)}"
    elif node['type'] == 'changed':
        old_value = f"{indent}  - {key}: {format_value(node['old_value'], depth, use_quotes)}"
        new_value = f"{indent}  + {key}: {format_value(node['new_value'], depth, use_quotes)}"
        return f"{old_value}\n{new_value}"
    elif node['type'] == 'nested':
        return f"{indent}    {key}: {format_stylish(node['children'], depth + 1, use_quotes)}"


def format_stylish(diff, depth=1, use_quotes=True):
    lines = ['{']
    indent = '    ' * (depth - 1)

    for node in diff:
        lines.append(format_node(node, indent, depth, use_quotes))

    lines.append(f"{indent}}}")
    return '\n'.join(lines)
