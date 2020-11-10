def factorial(number):
    product = 1
    for i in range(1, number + 1):
        product *= i
    return product

number = int(input("Dla jakiej liczby chcesz policzyć silnię?"))
print(factorial(number))