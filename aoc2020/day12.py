def parse(line):
    return (line[0], int(line[1:]))


cardinals = ("N", "E", "S", "W")
turns = ("L", "R")
forward = "F"


def turn(orient, order, dist):
    """
    >>> turn("N", "L", 90)
    'W'
    >>> turn("N", "L", 180)
    'S'
    >>> turn("E", "R", 270)
    'N'
    >>> turn("S", "R", 180)
    'N'
    """
    offset = dist//90
    if order == "L":
        offset = -offset
    return cardinals[(cardinals.index(orient) + offset) %
                     len(cardinals)]


def move(x, y, orient, order, dist):
    if order == "N":
        return (x, y + dist, orient)
    elif order == "E":
        return (x + dist, y, orient)
    elif order == "S":
        return (x, y - dist, orient)
    elif order == "W":
        return (x - dist, y, orient)
    elif order in turns:
        return (x, y, turn(orient, order, dist))
    elif order == "F":
        return move(x, y, orient, orient, dist)


def part1(lines):
    orders = [parse(line) for line in lines]
    x, y = 0, 0
    orient = "E"
    for order, dist in orders:
        x, y, orient = move(x, y, orient, order, dist)
    return [x, y, orient, abs(x)+abs(y)]


def rot(wx, wy, order, dist):
    """
    >>> rot(10, 4, "R", 90)
    (4, -10)
    """
    for _ in range(dist//90):
        if order == "R":
            wx, wy = wy, -wx
        elif order == "L":
            wx, wy = -wy, wx
    return wx, wy


def move2(x, y, wx, wy, order, dist):
    if order == "N":
        return (x, y, wx, wy+dist)
    elif order == "E":
        return (x, y, wx+dist, wy)
    elif order == "S":
        return (x, y, wx, wy-dist)
    elif order == "W":
        return (x, y, wx-dist, wy)
    elif order in turns:
        return (x, y, *rot(wx, wy, order, dist))
    elif order == "F":
        return (x + dist * wx, y+dist*wy, wx, wy)


def part2(lines):
    orders = [parse(line) for line in lines]
    x, y = 0, 0
    wx, wy = 10, 1
    for order, dist in orders:
        x, y, wx, wy = move2(x, y, wx, wy, order, dist)
    return [x, y, wx, wy, abs(x)+abs(y)]


def main(f):
    lines = [line.strip() for line in f]
    print(part1(lines))
    print(part2(lines))
