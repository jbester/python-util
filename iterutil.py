import functools
from typing import List, Iterable, Callable, Any, Union, Tuple, Optional
from array import array
from functools import reduce
import collections
import itertools

Predicate = Callable[[Any], bool]


def unzip(iterables: Iterable) -> Iterable[Tuple]:
    """Undo what zip does; Split a list of tuples into a tuple of lists where
the first list is a list of all the first elements, second list is a
list of all second elements, etc.

e.g. unzip a list of four-tuples into four lists

    >>>  list(unzip([(1, 2, 3, 4), (3, 4, 5, 6), (10, 11, 12, 19)]))
    [(1, 3, 10), (2, 4, 11), (3, 5, 12), (4, 6, 19)]

    :param iterables: iterable to unzip
    :return: tuple of lists
    """
    return zip(*iterables)


def count_if(pred: Predicate, *iterables) -> int:
    """count_if( pred, *iterables )

    Apply predicate to iterables and count times when predicate is true.
    Would be equivalent to count( map( pred, *iterables ) ) if map
    took multiple list parameters

    >>> count_if(lambda x: x % 2 == 0, range(1, 5))
    2

    :param pred: predicate to call on each item
    :returns: count of items that when result of pred( item ) is true

    """
    counter = 0
    for iterable in iterables:
        for i in iterable:
            if pred(i):
                counter += 1
    return counter


def take(count: int, it: Union[Iterable, range]) -> Iterable:
    """Take count of elements and skip the rest"""
    try:
        if isinstance(it, range):
            it = iter(it)
        yield from (next(it) for _ in range(count))
    except StopIteration:
        pass


def skip(count: int, it: Union[Iterable, range]) -> Iterable:
    """Skip count # of elements and yield the rest"""
    try:
        if isinstance(it, range):
            it = iter(it)
        for _ in range(count):
            _ = next(it)
        yield from it
    except StopIteration:
        pass


def map_into(fun: Callable, lst: Union[Tuple, array]):
    """map_into(fun,lst).   Same as map except modifies list in place

    >>> a = list(range(0, 5))
    >>> a
    [0, 1, 2, 3, 4]
    >>> map_into(lambda x: x + 1, a)
    [1, 2, 3, 4, 5]
    >>> a
    [1, 2, 3, 4, 5]

    :param fun: function to call on each item in lst
    :param lst: list to map in place in
    :return: original list (note: not a copy)

    """
    if not lst:
        return None
    for idx, val in enumerate(lst):
        lst[idx] = fun(val)
    return lst


def remove_if(pred: Predicate, lst: List):
    """remove_if(pred, lst).  Modify the list to remove all items where pred returns a true value

    :param pred: predicate to test each item
    :param lst: list to analyze
    :returns: None
    """
    for i in reversed([i for i, item in enumerate(lst) if pred(item)]):
        del lst[i]


def unique(it: Iterable, hash_fn: Optional[Callable[[Any], Any]] = None) -> Iterable:
    """Iterates over an iterable and only yields unique items

    :param it: iterable
    :param hash_fn: Hash function to use,

    :returns: generator that returns unique items for an iterable
    """
    visited = set()

    def do_hash(element):
        # use ident if no hash function provided
        if hash_fn is None:
            return element, element
        return hash_fn(element), element

    # iterate and hash each value and add each to set
    for hash_value, item in map(do_hash, it):
        if hash_value not in visited:
            visited.add(hash_value)
            yield item


def nth(n: int, it: Optional[Iterable] = None) -> Tuple[Callable, Any]:
    """Nth function (as in lisp, Occasionally useful, when supplied as a first class function

    :param n: index get an element for
    :param it: iterable - if not supplied return the partial application
    :return: Element or partial application
    """
    if it is None:
        return functools.partial(nth, n)
    if isinstance(it, range):
        it = iter(it)
    for _ in range(n):
        _ = next(it)
    return next(it)


first, second, third, fourth, fifth = map(nth, range(5))
