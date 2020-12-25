import collections


def part1(lines):
    locs = [location(parse(line)) for line in lines]
    return len(visit(locs))


def part2(lines):
    locs = [location(parse(line)) for line in lines]
    b = visit(locs)
    for n in range(100):
        b = turn(b)
    return len(b)


def turn(b):
    w = collections.defaultdict(int)
    b_flip = set()
    w_flip = set()
    for t in b:
        num_b = 0
        for n in neighbors(t):
            if n in b:
                num_b += 1
            else:
                w[n] += 1
        if num_b == 0 or num_b > 2:
            b_flip.add(t)
    for t, c in w.items():
        if c == 2:
            w_flip.add(t)
    return b.difference(b_flip).union(w_flip)


COORDS = {
    'e': (2, 0),
    'ne': (1, 1),
    'se': (1, -1),
    'w': (-2, 0),
    'sw': (-1, -1),
    'nw': (-1, 1),
}


def visit(locs):
    b = set()
    for l in locs:
        if l in b:
            b.remove(l)
        else:
            b.add(l)
    return b


def neighbors(loc):
    for dx, dy in COORDS.values():
        x, y = loc
        yield x+dx, y+dy


def location(directions):
    """Translate directions into a canonical location vector

    >>> location(["ne", "se", "e", "e"])
    (6, 0)
    >>> location(["ne", "se", "se", "w"])
    (1, -1)
    >>> location(["nw", "nw", "se"])
    (-1, 1)
    >>> location(["nw", "nw", "ne"])
    (-1, 3)
    >>> location(["e", "w", "w", "e", "w"])
    (-2, 0)
    """
    x, y = 0, 0
    for d in directions:
        dx, dy = COORDS[d]
        x += dx
        y += dy
    return x, y


def parse(line):
    directions = []
    for d in line:
        if (len(directions) > 0
            and d in ('e', 'w')
                and directions[-1] in ('n', 's')):
            directions[-1] += d
            continue
        directions.append(d)
    return directions


def main(f):
    # f = EXAMPLE.split("\n")
    lines = [line.strip() for line in f]
    print(part1(lines))
    print(part2(lines))


EXAMPLE = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""
