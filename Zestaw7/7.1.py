from frac import *
import unittest


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = Frac()

    def test_print(self):
        self.assertEqual(str(Frac(1, 3)), "1/3")
        self.assertEqual(repr(Frac(1, 3)), "Frac(1, 3)")

    def test_cmp_frac(self):
        self.assertTrue(Frac(1, 3) < Frac(4, 5))
        self.assertTrue(Frac(1, 3) <= Frac(4, 12))
        self.assertTrue(Frac(4, 5) > Frac(1, 3))
        self.assertTrue(Frac(4, 12) >= Frac(1, 3))
        self.assertTrue(Frac(3, 9) == Frac(1, 3))
        self.assertTrue(Frac(1, 3) == Frac(1, 3))
        self.assertTrue(Frac(1, 3) != Frac(1, 4))

    def test_add_frac_frac(self):
        self.assertEqual(Frac(1, 2) + Frac(1, 3), Frac(5, 6))

    def test_add_frac_int(self):
        self.assertEqual(Frac(1, 2) + 1, Frac(3, 2))

    def test_add_int_frac(self):
        self.assertEqual(1 + Frac(1, 2), Frac(3, 2))

    def test_add_frac_float(self):
        self.assertEqual(Frac(1, 3) + 1.5, Frac(11, 6))

    def test_sub_frac_frac(self):
        self.assertEqual(Frac(1, 2) - Frac(1, 3), Frac(1, 6))

    def test_sub_frac_int(self):
        self.assertEqual(Frac(1, 2) - 1, Frac(-1, 2))

    def test_sub_int_frac(self):
        self.assertEqual(1 - Frac(1, 2), Frac(1, 2))

    def test_sub_frac_float(self):
        self.assertEqual(Frac(2, 3) - 0.5, Frac(1, 6))

    def test_mul_frac_frac(self):
        self.assertEqual(Frac(2, 3) * Frac(3, 4), Frac(1, 2))

    def test_mul_frac_int(self):
        self.assertEqual(Frac(2, 3) * 2, Frac(4, 3))

    def test_mul_int_frac(self):
        self.assertEqual(2 * Frac(2, 3), Frac(4, 3))

    def test_mul_frac_float(self):
        self.assertEqual(Frac(2, 5) * 1.5, Frac(3, 5))

    def test_div_frac_frac(self):
        self.assertEqual(Frac(2, 3) / Frac(3, 4), Frac(8, 9))

    def test_div_frac_int(self):
        self.assertEqual(Frac(2, 3) / 2, Frac(1, 3))

    def test_div_int_frac(self):
        self.assertEqual(2 / Frac(3, 4), Frac(8, 3))

    def test_div_frac_float(self):
        self.assertEqual(Frac(2, 3) / 0.5, Frac(4, 3))

    def test_one_argument_operators(self):
        self.assertEqual(+Frac(2, 3), Frac(2, 3))
        self.assertEqual(+Frac(2, 3), Frac(-2, -3))
        self.assertEqual(-Frac(2, 3), Frac(-2, 3))
        self.assertEqual(-Frac(2, 3), Frac(2, -3))
        self.assertEqual(~Frac(2, 3), Frac(3, 2))

    def test_float_frac(self):
        self.assertEqual(float(Frac(2, 3)), 2/3)

    def test_create_frac(self):
        self.assertRaises(ValueError, Frac, 3, 0)


if __name__ == '__main__':
    unittest.main()
