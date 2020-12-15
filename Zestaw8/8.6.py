class Solver:
    def __init__(self):
        self.values = {(0, 0): 0.5, (0, 1): 1, (1, 0): 0}

    def p_dynamicznie(self, i, j):
        if (i, j) in self.values.keys():
            return self.values.get((i, j))
        if i == 0:
            return self.values.get((0, 1))
        if j == 0:
            return self.values.get((1, 0))
        if i > 0 and j > 0:
            self.values[(i, j)] = 0.5 * (self.p_dynamicznie(i - 1, j) + self.p_dynamicznie(i, j - 1))
            return self.values.get((i, j))

def p_rekurencyjnie(i, j):
    if i == 0 and j == 0:
        return 0.5
    elif i > 0 and j == 0:
        return 0.0
    elif i == 0 and j > 0:
        return 1.0
    else:
        return 0.5 * (p_rekurencyjnie(i - 1, j) + p_rekurencyjnie(i, j - 1))


print("Rekurencyjnie: ", p_rekurencyjnie(10, 9))
print("Za pomocą programowania dynamicznego: ", Solver().p_dynamicznie(10, 9))
