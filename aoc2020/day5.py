def parse(line):
    """
    >>> parse("BFFFBBFRRR")
    (70, 7, 567)
    >>> parse("FFFBBBFRRR")
    (14, 7, 119)
    >>> parse("BBFFBBFRLL")
    (102, 4, 820)
    """

    row = int("0b" + line[:7].replace("F", "0").replace("B", "1"), 2)
    col = int("0b" + line[7:].replace("L", "0").replace("R", "1"), 2)
    return (row, col, row*8 + col)


def part1(lines):
    seats = [parse(line) for line in lines]
    seats.sort(key=lambda s: -s[2])
    return seats[0][2]


def part2(lines):
    seats = [parse(line) for line in lines]
    seats.sort(key=lambda s: s[2])
    last = seats[0]
    for seat in seats:
        if seat[2] > last[2] + 1:
            return last[2] + 1
        last = seat


def main(f):
    lines = [line.strip() for line in f]
    print(part1(lines))
    print(part2(lines))
