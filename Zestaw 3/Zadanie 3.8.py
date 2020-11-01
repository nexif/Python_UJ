import random

s = random.getstate()
sekwencja1 = [random.randint(1, 10) for i in range(10)]
sekwencja2 = [random.randint(1, 10) for j in range(10)]

print('Sekwencja nr 1:', sekwencja1)
print('Sekwencja nr 2:', sekwencja2)

sameElements = set()

for i in sekwencja1:
    for j in sekwencja2:
        if i == j:
            sameElements.add(i)

print('Elementy należące do obu sekwencji:', sameElements)

elementsWithoutRepetition = set(sekwencja1).union(sekwencja2)
print('Wszystkie elementy bez powtórzeń: ', elementsWithoutRepetition)
