"""https://adventofcode.com/2017/day/3"""


def coords(n):
    """
    Bottom right corner is odd square: 1, 9, 25, 49...
    If bottom right corner = r^2
    bottom left corner = r^2 - (r-1)
    top left corner = r^2 - 2(r-1)
    top right corner = r^2 - 3(r-1)

    >>> coords(1)
    [0, 0]
    >>> coords(2)
    [1, 0]
    >>> coords(3)
    [1, 1]
    >>> coords(11)
    [2, 0]
    >>> coords(12)
    [2, 1]
    >>> coords(20)
    [-2, -1]
    >>> coords(23)
    [0, -2]
    >>> coords(24)
    [1, -2]
    >>> coords(49)
    [3, -3]
    """
    if n == 1:
        return [0, 0]
    x = 0
    y = 0
    r = 1
    # Bottom right corner is odd square: 1, 9, 25, 49...
    # Find smallest odd r s.t. n <= r^2
    r = 1
    while n > r**2:
        r += 2
    # Width from origin is (r-1)/2
    w = (r-1)//2
    diff = r**2 - n
    offset = diff % (2*w)
    if diff < 2*w:
        x = w - offset
        y = -w
    elif diff < 4*w:
        x = -w
        y = -w + offset
    elif diff < 6*w:
        x = -w + offset
        y = w
    else:
        x = w
        y = w - offset
    return [x, y]


def neighbors(coords):
    """
    >>> neighbors([5, -3])
    [[4, -2], [5, -2], [6, -2], [4, -3], [6, -3], [4, -4], [5, -4], [6, -4]]
    """
    x, y = coords
    return [
        [x-1, y+1], [x, y+1], [x+1, y+1],
        [x-1, y],             [x+1, y],
        [x-1, y-1], [x, y-1], [x+1, y-1],
    ]


def solve_p1(n):
    return sum(abs(x) for x in coords(n))


def solve_p2(val_limit):
    last_val = 0
    square_mem = {"[0, 0]": 1}
    m = 2
    while last_val < val_limit:
        c = coords(m)
        total = 0
        for neighbor in neighbors(c):
            total += square_mem.get(str(neighbor), 0)
        last_val = total
        square_mem[str(c)] = total
        m += 1
    return last_val


def main(f):
    n = int(f.read().strip())
    print(solve_p1(n))
    print(solve_p2(n))
