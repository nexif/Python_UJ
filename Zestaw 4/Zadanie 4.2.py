def draw_ruler(length):
    segmentLength = 10
    ruler = '| '

    for i in range(length):
        ruler += '. . . . | '

    ruler += '\n0'

    for i in range(length):
        next_number = str(i + 1)
        next_number = ''.ljust(segmentLength - len(next_number), ' ') + next_number
        ruler += next_number

    return ruler


def draw_rectangle(height, length):
    result = ''
    for i in range(height * 2 + 1):
        if i % 2 == 0:
            result += '+'
            for j in range(length):
                result += '---+'
            result += '\n'
        else:
            result += '|'
            for j in range(length):
                result += '   |'
            result += '\n'

    return result


print("Miarka:")
length = int(input("Wprowadź długość segmentu: "))
print(draw_ruler(length))

height = int(input("Wprowadź wysokość: "))
length = int(input("Wprowadź szerokość: "))
print(draw_rectangle(height, length))