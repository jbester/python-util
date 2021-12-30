from typing import Any, Callable
from .symbols import symbol


def compose(outer_fun: Callable, inner_fun: Callable):
    """Compose two functinos

    :param outer_fun: function takes result of innerfunction as parameter
    and provides return value of the composed function
    :param inner_fun: function takes paramter of composed function and
    provides parameter for outerfunction
    :returns: composed function

    >>> f = compose( lambda y: y - 7, lambda x: x ** 2 )
    >>> f(7)
    42
    """

    def composite_function(*args, **kw):
        """
        Composition of two functions
        """
        return outer_fun(inner_fun(*args, **kw))

    return composite_function


def identity(*args):
    """return argument unmodified.  Occasionally, useful when passed as a first class function.

    :param args: any object
    :return: returns object without any modification

    >>> identity(3)
    3
    >>> identity(3, 4)
    (3, 4)

    """
    if len(args) == 1:
        return args[0]
    return args


PARAM = symbol('PARAM')


def cut(func, *args, **keywords):
    """Partially apply a function without keyword arguments

    >>> fn = cut(lambda a,b,c: (a, b, c), 1, PARAM, 3)
    >>> fn(2)
    (1, 2, 3)
    >>> fn('a')
    (1, 'a', 3)
    """
    num_args = 0
    for arg in args:
        if arg == PARAM:
            num_args += 1

    def new_func(*fargs, **fkeywords):
        nonlocal args, keywords
        new_keywords = {**keywords, **fkeywords}
        new_args = []
        if len(fargs) != num_args:
            raise Exception(f"Expected number of arguments {num_args} actual={len(fargs)}")
        fargs = iter(fargs)
        for arg in args:
            if arg == PARAM:
                new_args.append(next(fargs))
            else:
                new_args.append(arg)
        return func(*new_args, **new_keywords)
    new_func.func = func
    new_func.args = args
    new_func.keywords = keywords
    return new_func


