def solve1(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                print("Nieskończenie wiele rozwiązań - równanie tożsamościowe")
            else:
                print("Równanie jest sprzeczne")
        else:
            if c == 0:
                print("Rozwiązanie: y = 0")
            else:
                print("Rozwiązanie: y =", -c/b)
    else:
        if b == 0:
            if c == 0:
                print("Rozwiązanie: x = 0")
            else:
                print("Rozwiązanie: x =", -c/a)
        else:
            if c == 0:
                print("Rozwiązanie: y =", -a/b, "x")
            else:
                print("Rozwiązanie: y =", -a/b, "x +", -c/b)

# Przykładowe równania:
print("Równanie: x + y + 3 = 0")
solve1(0, 0, 3)
print("Równanie: 3x + 6y + 1 = 0")
solve1(3, 6, 1)
print("Równanie: -2x + 5y - 3 = 0")
solve1(-2, 5, -3)
