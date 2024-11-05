def sum_seq(sequence):
    total = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            total += sum_seq(item)
        else:
            total += item
    return total

sum_seq_result = sum_seq([5, [4, [3, [2]]], 1])
expected_sum_seq_result = 15
assert sum_seq_result == expected_sum_seq_result