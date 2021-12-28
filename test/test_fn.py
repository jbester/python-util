import unittest
from .. import *


class FnTests(unittest.TestCase):
    def test_identity(self):
        self.assertEqual(1, identity(1))
        self.assertEqual(('a', 'b'), identity('a', 'b'))

    def test_compose(self):
        f = compose(lambda x: x - 7, lambda x: x * x)
        self.assertEqual(42, f(7))


if __name__ == '__main__':
    unittest.main()
