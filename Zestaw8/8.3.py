import random


def calc_pi(n=100): #Obliczanie liczby pi metodą Monte Carlo. n oznacza liczbę losowanych punktów.
    random.getstate()
    circle_points = 0
    square_points = 0
    pi = 0

    for i in range(n):
        rand_x = random.random()
        rand_y = random.random()

        origin_dist = rand_x**2 + rand_y**2

        if origin_dist <= 1:
            circle_points += 1

        square_points += 1
        pi = 4.0 * circle_points / square_points

    return pi


print("Wartość pi dla n=10: ", calc_pi(10))
print("Wartość pi dla n=100: ", calc_pi(100))
print("Wartość pi dla n=1000: ", calc_pi(1000))
print("Wartość pi dla n=100000: ", calc_pi(100000))
