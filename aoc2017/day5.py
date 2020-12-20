def part1(lines):
    prog = [int(n) for n in lines]
    steps = 0
    cur = 0
    while True:
        if cur >= len(prog):
            return steps
        nxt = cur + prog[cur]
        prog[cur] += 1
        steps += 1
        cur = nxt


def part2(lines):
    prog = [int(n) for n in lines]
    steps = 0
    cur = 0
    while True:
        if cur >= len(prog):
            return steps
        nxt = cur + prog[cur]
        if prog[cur] >= 3:
            prog[cur] -= 1
        else:
            prog[cur] += 1
        steps += 1
        cur = nxt


def main(f):
    lines = [line.strip() for line in f]
    print(part1(lines))
    print(part2(lines))
