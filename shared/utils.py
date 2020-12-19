import functools
import itertools

def product(lst):
    return functools.reduce(lambda x, y: x*y, lst)


def group(strings):
    """
    >>> group(["a", "", "b", "c", "", "d", "e", "f"])
    [['a'], ['b', 'c'], ['d', 'e', 'f']]
    """
    group = []
    groups = []
    for string in strings:
        if string == "":
            groups.append(group)
            group = []
            continue
        group.append(string)
    if group:
        groups.append(group)
    return groups

NEIGHBOR_DELTAS = (
    (-1,  1), (0,  1), (1,  1),
    (-1,  0),          (1,  0),
    (-1, -1), (0, -1), (1, -1),
)

def neighbors(*coords):
    """
    Generate all points adjacent and diagonal to coords of arbitrary dimension.

    >>> all(p in neighbors(3, 4) for p in [(2, 5), (3, 5), (4, 5), (2, 4), (4, 4), (2, 3), (3, 3), (4, 3)])
    True
    >>> all(p in neighbors(-2, 0) for p in [(-3, 1), (-2, 1), (-1, 1), (-3, 0), (-1, 0), (-3, -1), (-2, -1), (-1, -1)])
    True
    >>> all(p in neighbors(1, 2 ,3) for p in [(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 2, 2), (0, 2, 3), (0, 2, 4), (0, 3, 2), (0, 3, 3), (0, 3, 4), (1, 1, 2), (1, 1, 3), (1, 1, 4), (1, 2, 2), (1, 2, 4), (1, 3, 2), (1, 3, 3), (1, 3, 4), (2, 1, 2), (2, 1, 3), (2, 1, 4), (2, 2, 2), (2, 2, 3), (2, 2, 4), (2, 3, 2), (2, 3, 3), (2, 3, 4)])
    True
    >>> (-1, 2, 1, 4) in neighbors(0, 1, 2, 3)
    True
    >>> len(list(neighbors(0, 1, 2, 3)))
    80
    """
    n_arrays = []
    for c in coords:
        n_arrays.append((-1, 0, 1))
    for diff in itertools.product(*n_arrays):
        # Skip itself, e.g. (0, 0, 0, ...)
        if all(d == 0 for d in diff):
            continue
        yield array_add(coords, diff)

def array_add(a, b):
    """
    Add the respective values two tuples of equal length.
    
    >>> array_add((1, 2, 3), (7, 11, 13))
    (8, 13, 16)
    """
    return tuple(sum(n) for n in zip(a, b))