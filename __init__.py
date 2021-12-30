import time
from typing import AnyStr
import logging
from .shellutils import die, warn, in_directory, directory_removed_after, file_removed_after, chomp
from .iterutil import count_if, first, nth, map_into, remove_if, unique, unzip, reduce, \
    second, third, fourth, fifth, skip, take
from .fnutil import identity, compose, PARAM, cut
from .symbols import Symbol
from typing import Optional, Callable
import contextlib


class StopWatch:
    def __init__(self):
        self.start = time.time()

    @property
    def elapsed(self):
        return time.time() - self.start

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


@contextlib.contextmanager
def timed():
    """Decorator that clocks a function each time it is called.

    :returns: a started stopwatch
    """
    watch = StopWatch()
    try:
        yield watch
    finally:
        pass


def trace(fun: Optional[Callable] = None):
    """Decorator for a function that in effect generates a log event
every time a function is called. The log message contains the function name, parameters, return value and timestamp.
    :param fun: function to trace
    """
    def call(*args, **kw):
        """
        Call the function
        """
        nonlocal fun
        # generate the message
        msg = fun.__qualname__
        parameters = list(map(str, args))
        for keyword in kw:
            parameters.append(f'{keyword}={kw[keyword]}')
        msg += '(' + ','.join(parameters) + ')'
        result = fun(*args, **kw)
        msg += " => " + str(result)
        logging.debug(msg)
        return result

    return call

