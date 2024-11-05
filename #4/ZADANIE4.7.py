def flatten(sequence):
    result = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

flatten_result = flatten([[9, 8, [7]], 4, [6, [5, 3], 2]])
expected_flatten_result = [9, 8, 7, 4, 6, 5, 3, 2]
assert flatten_result == expected_flatten_result