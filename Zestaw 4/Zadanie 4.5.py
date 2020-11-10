def odwracanie_iteracyjnie(lista, left, right):
    counter = 0
    for i in range(left, right + 1):
        if counter >= (right - left + 1) / 2:
            break

        lista[i], lista[right - counter] = lista[right - counter], lista[i]
        counter = counter + 1

def odwracanie_rekurencyjnie(lista, left, right):
    if left == right:
        return
    lista[left], lista[right] = lista[right], lista[left]
    return odwracanie_rekurencyjnie(lista, left + 1, right - 1)


lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

odwracanie_iteracyjnie(lista, 2, 5)
print(lista)

odwracanie_rekurencyjnie(lista, 2, 5)
print(lista)