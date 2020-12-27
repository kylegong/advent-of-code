def part1(nums):
    c, d = nums
    cloop = loop_size(7, c)
    return transform(d, cloop)


def part2(nums):
    return


def loop_size(sn, pk):
    """
    >>> loop_size(7, 5764801)
    8
    >>> loop_size(7, 17807724)
    11
    """
    v = 1
    loop_size = 0
    while v != pk:
        v = (v * sn) % 20201227
        loop_size += 1
    return loop_size


def transform(sn, loop_size):
    """
    >>> transform(7, 8)
    5764801
    >>> transform(7, 11)
    17807724
    """
    v = 1
    for _ in range(loop_size):
        v = (v * sn) % 20201227
    return v


def main(f):
    nums = [int(line.strip()) for line in f]
    # nums = [5764801, 17807724]
    print(part1(nums))
    print(part2(nums))
