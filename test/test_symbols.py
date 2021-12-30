import unittest
from .. import Symbol


class SymbolsTest(unittest.TestCase):
    def test_symbol(self):
        hello = Symbol('hello')
        bye = Symbol('bye')
        hello2 = Symbol('hello')
        self.assertEqual(hello, hello2)
        self.assertNotEqual(bye, hello)
        self.assertNotEqual(bye, hello2)


if __name__ == '__main__':
    unittest.main()
