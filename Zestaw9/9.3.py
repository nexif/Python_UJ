class Node:
    """Klasa reprezentująca węzeł listy dwukierunkowej."""

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        return self.data == other.data

    def __lt__(self, other):
        return self.data < other.data

    def __gt__(self, other):
        return self.data > other.data


class DoubleList:
    """Klasa reprezentująca całą listę dwukierunkową."""

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def __str__(self):
        result = ''
        current = self.head
        while current is not None:
            result += (',' + str(current))
            current = current.next
        result = '[' + result[1:] + ']'
        return result

    def is_empty(self):
        # return self.length == 0
        return self.head is None

    def count(self):
        return self.length

    def insert_head(self, node):
        if self.head:
            node.next = self.head
            self.head.prev = node  # stary head
            self.head = node  # nowy head
        else:  # pusta lista
            self.head = node
            self.tail = node
        self.length += 1

    def insert_tail(self, node):
        if self.tail:
            node.prev = self.tail
            self.tail.next = node  # stary tail
            self.tail = node  # nowy tail
        else:  # pusta lista
            self.head = node
            self.tail = node
        self.length += 1

    def remove_head(self):  # zwraca node
        if self.head is None:
            raise ValueError("Nie można usuwać z pustej listy")
        elif self.head is self.tail:
            node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return node
        else:
            node = self.head
            self.head = self.head.next
            self.head.prev = None  # czyszczenie
            self.length -= 1
            return node

    def remove_tail(self):  # zwraca node
        if self.head is None:
            raise ValueError("Nie można usuwać z pustej listy")
        elif self.head is self.tail:
            node = self.tail
            self.head = None
            self.tail = None
            self.length = 0
            return node
        else:
            node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None  # czyszczenie
            self.length -= 1
            return node

    def find_max(self):
        current = self.head
        max = current
        while current.next is not None:
            current = current.next
            if current > max:
                max = current
        return max

    def find_min(self):
        current = self.head
        min = current
        while current.next is not None:
            current = current.next
            if current < min:
                min = current
        return min

    def remove(self, node):
        if self.is_empty():
            raise ValueError("Nie można usuwać z pustej listy")
        elif node == self.head:
            self.remove_head()
        elif node == self.tail:
            self.remove_tail()
        else:
            current = self.head
            while current.next is not None and current != node:
                current = current.next
            previous_node = current.prev
            next_node = current.next
            previous_node.next = current.next
            next_node.prev = previous_node

    """czyszczenie listy"""
    def clear(self):
        current = self.tail
        self.tail = None
        while current.prev is not None:
            current = current.prev

            current.next.data = None
            current.next.prev = None
            current.next = None

        self.head.data = None
        self.head = None


if __name__ == '__main__':
    double_list = DoubleList()

    print('Lista pusta: ', double_list)
    double_list.insert_tail(Node(30))
    double_list.insert_tail(Node(2))
    double_list.insert_tail(Node(-5))
    double_list.insert_tail(Node(12))
    double_list.insert_tail(Node(1))
    double_list.insert_tail(Node(18))
    double_list.insert_tail(Node(4))
    double_list.insert_tail(Node(9))

    print('Lista po wstawieniu do niej kilku elementów: ', double_list)
    print('Najmniejszy element listy: ', double_list.find_min())
    print('Największy element listy: ', double_list.find_max())
    double_list.remove(Node(2))
    print('Lista po usunięciu węzła 2', double_list)
    double_list.remove(Node(4))
    print('Lista po usunięciu węzła 4', double_list)
    double_list.clear()
    print('Lista po usunięciu wszystkich elementów', double_list)

