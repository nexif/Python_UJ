from integer_list_generator import *
from collections import deque


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def partition(arr, start, end):
    pivot = arr[end]
    pIndex = start
    for i in range(start, end):
        if arr[i] <= pivot:
            swap(arr, i, pIndex)
            pIndex = pIndex + 1
    swap(arr, pIndex, end)
    return pIndex


def quicksort_iterative(a):
    stack = deque()
    start, end = 0, len(a) - 1
    stack.append((start, end))
    while stack:
        start, end = stack.pop()
        pivot = partition(a, start, end)
        if pivot - 1 > start:
            stack.append((start, pivot - 1))
        if pivot + 1 < end:
            stack.append((pivot + 1, end))


if __name__ == '__main__':
    arr1 = generate_random_numbers(30)
    arr2 = generate_almost_sorted_numbers(30)
    arr3 = generate_almost_sorted_numbers_reversed(30)
    arr4 = generate_gaussian_distribution_numbers(30)
    arr5 = generate_numbers_with_repetition(30)

    print('Różne liczby int od 0 do N-1 w kolejności losowej: \n', arr1, '\n')
    print('Różne liczby int od 0 do N-1 prawie posortowane (liczby są blisko swojej prawidłowej pozycji): \n', arr2, '\n')
    print('Różne liczby int od 0 do N-1 prawie posortowane w odwrotnej kolejności: \n', arr3, '\n')
    print('N liczb float w kolejności losowej o rozkładzie gaussowskim: \n', arr4, '\n')
    print('N liczb int w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego (k < N, np. k*k = N): \n', arr5, '\n')

    quicksort_iterative(arr1)
    quicksort_iterative(arr2)
    quicksort_iterative(arr3)
    quicksort_iterative(arr4)
    quicksort_iterative(arr5)

    print('Te same listy, ale po sortowaniu iteracyjną wersją algorytmu quick sort:', '\n', arr1, '\n', arr2, '\n',
          arr3, '\n', arr4, '\n', arr5)
