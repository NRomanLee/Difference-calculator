def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, bool):
        return "true" if value else "false"
    elif value is None:
        return "null"
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)

def format_plain(diff, parent=''):
    lines = []

    for node in diff:
        key = node['key']
        full_path = f"{parent}.{key}" if parent else key

        if node['type'] == 'added':
            lines.append(f"Property '{full_path}' was added with value: {format_value(node['value'])}")
        elif node['type'] == 'removed':
            lines.append(f"Property '{full_path}' was removed")
        elif node['type'] == 'changed':  
            old_value = format_value(node['old_value'])
            new_value = format_value(node['new_value'])
            lines.append(f"Property '{full_path}' was updated. From {old_value} to {new_value}")
        elif node['type'] == 'nested':
            lines.append(format_plain(node['children'], full_path))

    return '\n'.join(lines)