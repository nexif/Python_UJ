DLUGOSC_SEGMENTU = 10
length = int(input("Wprowadź długość miarki: "))
ruler = '| '

for i in range(length):
    ruler += '. . . . | '

ruler += '\n0'

for i in range(length):
    next_number = str(i + 1)
    next_number = ''.ljust(DLUGOSC_SEGMENTU - len(next_number), ' ') + next_number
    ruler += next_number

print(ruler)