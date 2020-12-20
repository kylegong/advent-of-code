
def main(f):
    digits = f.read().strip()
    solve(digits)


def solve(digits):
    print(sum_consecutive(digits))
    print(sum_halfway(digits))


def sum_consecutive(digits):
    """ Sum consecutive digits.
    >>> sum_consecutive("1122")
    3
    >>> sum_consecutive("1111")
    4
    >>> sum_consecutive("1234")
    0
    >>> sum_consecutive("91212129")
    9
    """
    total = 0
    for i, d in enumerate(digits):
        if d == digits[(i+1) % len(digits)]:
            total += int(d)
    return total


def sum_halfway(digits):
    """
    >>> sum_halfway("1212")
    6
    >>> sum_halfway("1221")
    0
    >>> sum_halfway("123425")
    4
    >>> sum_halfway("123123")
    12
    >>> sum_halfway("12131415")
    4
    """
    total = 0
    for i, d in enumerate(digits):
        if d == digits[(i+len(digits)//2) % len(digits)]:
            total += int(d)
    return total
