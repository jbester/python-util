import unittest
from .. import symbol


class SymbolsTest(unittest.TestCase):
    def test_symbol(self):
        hello = symbol('hello')
        bye = symbol('bye')
        hello2 = symbol('hello')
        self.assertEqual(hello, hello2)
        self.assertNotEqual(bye, hello)
        self.assertNotEqual(bye, hello2)


if __name__ == '__main__':
    unittest.main()
