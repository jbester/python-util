import unittest
from .. import *
from array import array


class IterToolsCase(unittest.TestCase):
    def test_unzip(self):
        args = [(1, 2, 3, 4), (3, 4, 5, 6), (10, 11, 12, 19)]
        self.assertEqual([(1, 3, 10), (2, 4, 11), (3, 5, 12), (4, 6, 19)],  list(unzip(args)))

    def test_count_if(self):
        count = count_if(lambda x: (x % 2) == 0, range(10), range(10))
        self.assertEqual(10, count)
        count = count_if(lambda x: (x % 2) == 1, range(10), range(10))
        self.assertEqual(10, count)

    def test_map_into_arrays(self):
        # create an array 0 .. 9
        b = array('b', range(10))
        # create an array 1 .. 11
        c = array('b', range(1, 11))
        # do the map
        map_into(lambda x: x + 1, b)
        # verify array
        self.assertEqual(b, c)

    def test_partition(self):
        # create an array 0 .. 9
        b = array('b', range(10))
        # split into even and odd partitions
        passed, fail = partition(lambda x: x % 2 == 0, b)
        self.assertTrue(all(map(lambda x: x % 2 == 0, passed)))
        self.assertFalse(any(map(lambda x: x % 2 == 0, fail)))

    def test_nth(self):
        # verify nth pulls the nth element out
        self.assertEqual(5, nth(5, range(10)))
        self.assertEqual(1, second(range(10)))
        self.assertEqual(6, second(range(5, 10)))

    def test_unique(self):
        # test unique only returns unique values
        a = [1, 2, 3, 4, 5]
        self.assertEqual(a, list(unique(a)))
        b = [2, 2, 2, 1, 1]
        self.assertEqual([2, 1], list(unique(b)))

    def test_remove_if(self):
        # test remove_if destructively removes elements that match the predicate
        a = [1, 2, 3, 4, 5]
        remove_if(lambda x: x % 2 == 0, a)
        self.assertEqual([1, 3, 5], a)


if __name__ == '__main__':
    unittest.main()
