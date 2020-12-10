def parseLine(line):
    rules, password = line.split(": ")
    nums, letter = rules.split(" ")
    a, b = [int(n) for n in nums.split("-")]
    return [a, b, letter, password]


def isValid1(parsed):
    [minCount, maxCount, letter, password] = parsed
    count = len([n for n in password if n == letter])
    return minCount <= count <= maxCount


def isValid2(parsed):
    [p1, p2, letter, password] = parsed
    matches = [p for p in [p1, p2] if password[p - 1] == letter]
    return len(matches) == 1


def part1(lines):
    return len([l for l in lines if isValid1(parseLine(l))])


def part2(lines):
    return len([l for l in lines if isValid2(parseLine(l))])


def main(f):
    lines = [line.strip() for line in f]
    print(part1(lines))
    print(part2(lines))
