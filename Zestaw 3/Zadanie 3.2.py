#  a)
# L = [3, 5, 4] ; L = L.sort()
# Funkcję sort() wywołuje się na liście, którą ma posortować. Funkcja ta niczego nie zwraca.
# Poprawnie:
L = [3,5,4]
L.sort()
print(L)

#x, y = 1, 2, 3
# Liczba zmiennych i ilości elementów należących do tuple musi się zgadzać:
x, y, z = 1, 2, 3
print(x,y,z)

# X = 1, 2, 3 ; X[1] = 4
# Kod jest niepoprawny ze względu na próbę modyfikacji tuple, która jest obiektem niemodyfikowalnym. Można jedynie utworzyc ją na nowo
X = 1, 2, 3
X = X[0], 4, X[2]
print(X)

#X = [1, 2, 3] ; X[3] = 4
#Ten przykład jest niepoprawny ze względu na próbę przypisania wartości spoza zakresu listy (dostępne indeksy to 0,1,2)
X = [1, 2, 3]
X[2] = 4
print(X)


# X = "abc" ; X.append("d")
# Metoda append nie jest zdefiniowana w Pythonie dla napisów. Poprawnie:
X = "abc"
X += "d"
print(X)

# L = list(map(pow, range(8)))
# Funkcja pow jest funkcją przyjmującą dwa argumenty: liczbę, którą podnosimy do potęgi i wartość potęgi. Funkcja map jako pierwszy argument przyjmuje funkcję, którą w tym przypadku możemy napisac sami:

def power(a, b=2):
    return a ** b

print(list(map(power, range(8))))