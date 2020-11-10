def fibonacci(number):
    if number == 0:
        return 0

    previous_number = 0
    current_number = 1

    for i in range(1, number):
        previous_previous_number = previous_number
        previous_number = current_number
        current_number = previous_previous_number + previous_number
    return current_number


number = int(input("Który wyraz ciągu Fibonacciego chcesz policzyć? "))
print(fibonacci(number))