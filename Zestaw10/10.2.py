from stack import *
import unittest


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_str(self):
        self.assertEqual(str(self.stack), '[]')

    def test_is_empty(self):
        self.assertEqual(self.stack.is_empty(), True)

    def test_is_full(self):
        self.assertEqual(self.stack.is_full(), False)

    def test_pop(self):
        with self.assertRaises(ValueError):
            Stack().pop()
        self.stack.push(1)
        self.assertEqual(self.stack.pop(), 1)

    def test_push(self):
        self.stack.push(3)
        self.stack.push(5)
        self.stack.push(7)
        self.assertAlmostEqual(self.stack.pop(), 7)
        self.assertAlmostEqual(self.stack.pop(), 5)
        self.assertAlmostEqual(self.stack.pop(), 3)


    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
