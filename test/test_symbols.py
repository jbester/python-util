import unittest
from .. import symbols


class SymbolsTest(unittest.TestCase):
    def test_symbol(self):
        hello = symbols.Symbol('hello')
        bye = symbols.Symbol('bye')
        hello2 = symbols.Symbol('hello')
        self.assertEqual(hello, hello2)
        self.assertNotEqual(bye, hello)
        self.assertNotEqual(bye, hello2)


if __name__ == '__main__':
    unittest.main()
