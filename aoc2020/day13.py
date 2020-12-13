import math

def part1(lines):
    time = int(lines[0])
    buses = parse(lines[1])
    next_bus = None
    bus = None
    for b in buses:
        n = math.ceil(time/b)
        print(b, n, b*n, next_bus)
        if next_bus is None or n*b < next_bus:
            next_bus = n*b
            bus = b
    return [b, next_bus, next_bus - time, (next_bus - time) * bus]

def part2(lines):
    offsets = parse2(lines[1])
    time = 0
    jump = 1
    for b, i in offsets:
        print("(t + %d) %% %d == 0" % (i, b))
        while (time + i) % b != 0:
            print("(%d + %d) %% %d == %d" % (time, i, b, (time + i) % b))
            print ("time %d jump %d" % (time, jump))
            time += jump
        jump *= b
        print ("time %d jump %d" % (time, jump))
    return time

def parse(line):
    return [int(b) for b in line.split(",") if b != 'x']

def parse2(lines):
    offsets = []
    for i, b in enumerate(lines.split(',')):
        if b != 'x':
            offsets.append((int(b), i))
    return offsets

def main(f):
    lines = [line.strip() for line in f]
    print(part1(lines))
    print(part2(lines))
