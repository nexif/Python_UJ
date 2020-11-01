sequence = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
result = []

for element in sequence:
    result.append(sum(element))

print(result)