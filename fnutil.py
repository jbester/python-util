from typing import Any, Callable


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

