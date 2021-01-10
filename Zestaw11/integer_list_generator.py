# Moduł Pythona z funkcjami tworzącymi listy liczb całkowitych do sortowania
from random import randint
from random import gauss
from random import shuffle


def generate_random_numbers(quantity):
    arr = []
    for i in range(quantity):
        arr.append(i)
    shuffle(arr)
    return arr


def generate_almost_sorted_numbers(quantity):
    arr = []
    for i in range(quantity):
        arr.append(i)
    for i in range(quantity-1):
        var = randint(i, i+1)
        arr[i], arr[var] = arr[var], arr[i]
    return arr


def generate_almost_sorted_numbers_reversed(quantity):
    arr = generate_almost_sorted_numbers(quantity)
    arr.reverse()
    return arr


def generate_gaussian_distribution_numbers(quantity):
    arr = []
    for i in range(quantity):
        arr.append(gauss(0, 1))
    return arr


def generate_numbers_with_repetition(quantity):
    arr = []
    for i in range(quantity):
        arr.append(randint(0, quantity // 2))
    shuffle(arr)
    return arr
