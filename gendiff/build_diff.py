def build_diff(data1, data2):
    diff = []
    all_keys = sorted(set(data1.keys()).union(set(data2.keys())))

    for key in all_keys:
        if key not in data1:
            diff.append({
                'type': 'added',
                'key': key,
                'value': data2[key]
            })
        elif key not in data2:
            diff.append({
                'type': 'removed',
                'key': key,
                'value': data1[key]
            })
        elif data1[key] == data2[key]:
            diff.append({
                'type': 'unchanged',
                'key': key,
                'value': data1[key]
            })
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff.append({
                'type': 'nested',
                'key': key,
                'children': build_diff(data1[key], data2[key])
            })
        else:
            diff.append({
                'type': 'changed', 
                'key': key,
                'old_value': data1[key],
                'new_value': data2[key]
            })

    return diff