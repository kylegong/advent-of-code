def part1(lines):
    return [parse(line) for line in lines]


def part2(lines):
    return


THETA = {
    'e': 0,
    'ne': 60,
    'nw': 120,
    'w': 180,
    'sw': 240,
    'se': 300,
}


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
    lines = [line.strip() for line in EXAMPLE.split("\n")]
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
