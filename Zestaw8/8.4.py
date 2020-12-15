import math

def heron(a, b, c):

    if not is_correct_triangle(a, b, c):
        raise ValueError("Z podanych boków nie można zbudować trójkąta")

    s = (a + b + c) / 2
    formula = s * (s - a) * (s - b) * (s - c)
    return math.sqrt(formula)


def is_correct_triangle(a, b, c):
# Aby z trzech odcinków zbudować trójkąt, najdłuższy z nich musi być krótszy niż suma długość dwóch pozostałych.
    lengths = [a, b, c]
    lengths.sort()
    return lengths[0] + lengths[1] > lengths[2]


print("Pole trójkąta złożonego z długości (3,4,5) to: ", heron(3, 4, 5))
print(heron(1, 2, 3)) #Spowoduje ValueError

