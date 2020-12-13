def product(lst):
    import functools
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

def neighbors(x, y):
    """
    Generate all points adjacent and diagonal to (x, y).
    (x-1, y+1) (x, y+1) (x+1, y+1)
    (x-1,   y)          (x+1,   y)
    (x-1, y-1) (x, y-1) (x+1, y-1)

    >>> list(neighbors(3, 4))
    [(2, 5), (3, 5), (4, 5), (2, 4), (4, 4), (2, 3), (3, 3), (4, 3)]
    >>> list(neighbors(-2, 0))
    [(-3, 1), (-2, 1), (-1, 1), (-3, 0), (-1, 0), (-3, -1), (-2, -1), (-1, -1)]
    """
    for dx, dy in NEIGHBOR_DELTAS:
        yield (x+dx, y+dy)