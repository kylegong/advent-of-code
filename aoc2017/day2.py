
def checksums(values):
    """
    >>> checksums([[5, 1, 9, 5],[7,5,3],[2,4,6,8]])
    [8, 4, 6]
    """
    return [checksum(x) for x in values]


def checksum(values):
    """
    >>> checksum([5, 1, 9, 5])
    8
    >>> checksum([7,5,3])
    4
    >>> checksum([2,4,6,8])
    6
    """
    min_d = None
    max_d = 0
    for d in values:
        if min_d is None or int(d) < min_d:
            min_d = int(d)
        if int(d) > max_d:
            max_d = int(d)
    return max_d - min_d


def row_even_divide(row):
    """
    >>> row_even_divide([5, 9, 2, 8])
    4
    >>> row_even_divide([9, 4, 7, 3])
    3
    >>> row_even_divide([3, 8, 6, 5])
    2
    """
    for m in row:
        for n in row:
            if m == n:
                continue
            if m % n == 0:
                return m // n
    raise Exception("none divide evenly: %s", row)


def solve_p1(values):
    """
    >>> solve_p1([[5, 1, 9, 5],[7,5,3],[2,4,6,8]])
    18
    """
    return sum(checksums(values))


def solve_p2(values):
    """
    >>> solve_p2([[5, 9, 2, 8],[9, 4, 7, 3],[3, 8, 6, 5]])
    9
    """
    return sum(row_even_divide(row) for row in values)


def parse(text):
    lines = text.split("\n")
    return [[int(v) for v in line.strip().split()] for line in lines if line]


def main(f):
    values = parse(f.read())
    print(solve_p1(values))
    print(solve_p2(values))
