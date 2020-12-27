def part1(nums, min_n, max_n):
    for _ in range(100):
        nums = turn(nums, min_n, max_n)
    return label(nums)


def label(nums):
    passed = []
    for n in nums:
        if n != 1:
            passed.append(n)
            continue
        break
    return ''.join(str(n) for n in list(nums) + passed)


def turn(nums, min_n, max_n):
    cur = next(nums)
    pickup = [next(nums) for n in range(3)]
    dest = cur - 1
    if dest < min_n:
        dest = max_n
    while dest in pickup:
        dest -= 1
        if dest < min_n:
            dest = max_n
    passed = []
    for n in nums:
        if dest != n:
            passed.append(n)
            continue
        break
    for n in passed + [dest] + pickup:
        yield n
    yield from nums
    yield cur


def add_cups(nums, total):
    yield from nums
    yield from range(max(nums)+1, total+1)


def part2(nums):
    nums = add_cups(nums, 1_000_000)
    for n in range(1_000_000):
        if n % 10000 == 0:
            print(n)
        nums = turn(nums, 1, 1_000_000)
    for n in nums:
        if n == 1:
            break
    return next(nums) * next(nums)


def main(f):
    line = f.readline().strip()
    #line = "389125467"
    nums = [int(n) for n in line]
    print(part1((n for n in nums), min(nums), max(nums)))
    print(part2(nums))
