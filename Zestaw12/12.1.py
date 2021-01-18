# Napisać program, który na listę L wstawi n liczb wylosowanych z zakresu od 0 do k-1.
# Następnie program wylosuje liczbę y z tego samego zakresu i znajdzie wszystkie jej wystąpienia
# na liście L przy pomocy wyszukiwania liniowego. [n=100, k=10]

import random


def generate(quantity, max_value):
    arr = []
    for i in range(quantity):
        arr.append(random.randint(0, max_value - 1))
    return arr


def linear_search(arr, key):
    index = []
    for i in range(len(arr)):
        if arr[i] == key:
            index.append(i)
    return index


if __name__ == '__main__':
    array = generate(100, 10)
    searched_key = array[random.randint(0, len(array) - 1)]
    print('Wygenerowana tablica: ', array)
    print('Szukana wartość: ', searched_key)
    print('Występuje na pozycjach, których indeks to:', linear_search(array, searched_key))