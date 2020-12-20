def part1(lines):
    count = 0
    for line in lines:
        words = line.split(' ')
        if len(words) == len(set(words)):
            count += 1
    return count


def part2(lines):
    count = 0
    for line in lines:
        words = [str(sorted(w)) for w in line.split(' ')]
        if len(words) == len(set(words)):
            count += 1
    return count


def main(f):
    lines = [line.strip() for line in f]
    print(part1(lines))
    print(part2(lines))
