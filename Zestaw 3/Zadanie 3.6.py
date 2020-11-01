length = int(input("Wprowadź wysokość: "))
height = int(input("Wprowadź szerokość: "))

result = ''

for i in range(length * 2 + 1):
    if i % 2 == 0:
        result += '+'
        for j in range(height):
            result += '---+'
        result += '\n'
    else:
        result += '|'
        for j in range(height):
            result += '   |'
        result += '\n'

print(result)