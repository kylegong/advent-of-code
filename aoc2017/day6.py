def next(nums):
    max_n = max(nums)
    for i, n in enumerate(nums):
        if n == max_n:
            dist = n
            nums[i] = 0
            c = i
            while dist > 0:
                c = (c + 1) % len(nums)
                nums[c] += 1
                dist -= 1
            return


def cycle(nums):
    hist = {}
    i = 0
    while True:
        hist[tuple(nums)] = i
        next(nums)
        i += 1
        if tuple(nums) in hist:
            return (i, hist[tuple(nums)])


def part1(nums):
    return cycle(nums)[0]


def part2(nums):
    second, first = cycle(nums)
    return second - first


def main(f):
    line = f.readline()
    nums = [int(n) for n in line.split('\t')]
    print(part1(nums))
    print(part2(nums))
