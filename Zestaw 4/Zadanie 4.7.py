def flatten(sequence):
    result = []
    return flatten_helper(sequence, result)


def flatten_helper(sequence, result):
    for element in sequence:
        if isinstance(element, (list, tuple)):
            flatten_helper(element, result)
        else:
            result.append(element)
    return result


test_sequence = [5, (1, 4), [], 8, (1,5,2), [9]] #lista pusta zostanie zignorowana
print("Spłaszczona lista elementów: ", flatten(test_sequence))
