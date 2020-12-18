class Queue:

    def __init__(self):
        self.items = []

    def __str__(self):  # podglądanie kolejki
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):  # nigdy nie jest pusta
        return False

    def put(self, data):  # wstawia element
        if self.is_full():
            raise ValueError("Kolejka jest pełna")
        self.items.append(data)

    def get(self):  # pobiera element
        if self.is_empty():
            raise ValueError("Kolejka jest pusta")
        return self.items.pop(0)  # mało wydajne!
