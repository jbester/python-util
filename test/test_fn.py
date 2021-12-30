import unittest
from .. import *


class FnTests(unittest.TestCase):
    def test_identity(self):
        self.assertEqual(1, identity(1))
        self.assertEqual(('a', 'b'), identity('a', 'b'))

    def test_compose(self):
        f = compose(lambda x: x - 7, lambda x: x * x)
        self.assertEqual(42, f(7))

    def test_cut(self):
        def poly(x1, x2, x3):
            return x1**2 + x2 + x3
        fn = cut(poly, 10, PARAM, 3)
        self.assertEqual(123, fn(20))


if __name__ == '__main__':
    unittest.main()
