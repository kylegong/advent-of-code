def part1(nums):
    for a in nums:
        for b in nums:
            if a+b == 2020:
                return (a, b, a*b)


def part2(nums):
    for a in nums:
        for b in nums:
            for c in nums:
                if a+b+c == 2020:
                    return (a, b, c, a*b*c)


def main(f):
    nums = [int(line) for line in f]
    print("%d * %d = %d" % part1(nums))
    print("%d * %d * %d = %d" % part2(nums))
