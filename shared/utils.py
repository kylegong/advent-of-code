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
