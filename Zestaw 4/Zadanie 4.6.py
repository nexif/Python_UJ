def sum_seq(sequence):
    suma = 0
    for element in sequence:
        if isinstance(element, (list, tuple)):
            suma += sum_seq(element)
        else:
            suma += element
    return suma


test_sequence = [5, (1, 4), [], 8, (1,5,2), [9]]
print("Suma elementów: ", sum_seq(test_sequence))