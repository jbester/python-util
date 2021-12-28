import os
import unittest
from .. import *
import time
import logging


class UtilTests(unittest.TestCase):
    def test_timed(self):
        with timed() as timer:
            time.sleep(.25)
            self.assertGreaterEqual(timer.elapsed, .25)

    def test_trace(self):
        logging.basicConfig(filename='unittest.trace', level=logging.DEBUG)

        @trace
        def do_something(*args, **kw):
            return 1, 2, 3, 4
        do_something()
        with open('unittest.trace') as inf:
            txt = inf.read()
            self.assertIn('do_something() => (1, 2, 3, 4)', txt)
        os.unlink('unittest.trace')
        logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    unittest.main()
