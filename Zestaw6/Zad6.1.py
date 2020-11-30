from times import Time
import unittest

class TestTime(unittest.TestCase):

    def setUp(self): pass

    def test_print(self):
        self.assertEqual(str(Time(5)), "00:00:05")
        self.assertEqual(repr(Time(5)), "Time(5)")

    def test_cmp(self):
        # Sprawdzenie ==, !=, >, >=, <, <=.
        self.assertTrue(Time(2) == Time(2))
        self.assertFalse(Time(2) == Time(3))
        self.assertTrue(Time(2) != Time(3))
        self.assertFalse(Time(2) != Time(2))
        self.assertTrue(Time(2) < Time(3))
        self.assertFalse(Time(4) < Time(3))
        self.assertTrue(Time(2) <= Time(3))
        self.assertFalse(Time(4) <= Time(3))
        self.assertTrue(Time(4) > Time(3))
        self.assertFalse(Time(2) > Time(3))
        self.assertTrue(Time(4) >= Time(3))
        self.assertFalse(Time(2) >= Time(3))

    def test_add(self):
        self.assertEqual(Time(1) + Time(2), Time(3))

if __name__ == "__main__":
    unittest.main() #uruchomienie testów
