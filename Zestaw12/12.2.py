# Napisać wersję rekurencyjną wyszukiwania binarnego. 

import random


def generate(quantity, max_value):
    arr = []
    for i in range(quantity):
        arr.append(random.randint(0, max_value - 1))
    arr.sort()
    return arr


def binary_search_recursive(array, left, right, key):
    if right >= left:
        mid = left + (right - left) // 2
        if array[mid] == key:
            return mid
        if array[mid] > key:
            return binary_search_recursive(arr, left, mid - 1, key)
        return binary_search_recursive(arr, mid + 1, right, key)
    return -1


if __name__ == '__main__':
    arr = generate(20, 50)
    searched_key = arr[random.randint(0, len(arr) - 1)]
    print('Wygenerowana tablica: ', arr)
    print('Szukana wartość', searched_key)
    print('Występuje pod indeksem:', binary_search_recursive(arr, 0, len(arr), searched_key))
