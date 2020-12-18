import random


class RandomQueue:
    def __init__(self):
        self.items = []
        rand = random.getstate()

    def __str__(self):
        return str(self.items)

    def put(self, value):
        if self.is_full():
            raise ValueError("Kolejka jest pełna")
        self.items.append(value)

    def get(self):  # zwraca losowy element
        if self.is_empty():
            raise ValueError("Kolejka jest pusta")
        index = random.randint(0, len(self.items) - 1)
        # Zamieniamy wylosowany element z ostatnim elementem kolejki i go usuwamy uzyskując O(1)
        self.items[index], self.items[-1] = self.items[-1], self.items[index]
        return self.items.pop()

    def is_empty(self):
        return not self.items

    def is_full(self):  # nigdy nie jest pusta
        return False

    def clear(self):  # czyszczenie listy
        self.items = []
