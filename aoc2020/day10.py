
import functools


def part1(nums):
    j = 0
    threes = []
    ones = []
    for n in nums:
        if n - j > 3:
            raise ValueError
        if n - j == 3:
            threes.append(n)
        if n - j == 1:
            ones.append(n)
        j = n
    threes.append(j+3)
    return [len(threes), len(ones), len(threes) * len(ones)]


@functools.lru_cache
def count_ways(j, nums):
    if len(nums) <= 1:
        return 1
    if nums[1] <= j + 3:
        return count_ways(j, nums[1:]) + count_ways(nums[0], nums[1:])
    return count_ways(nums[0], nums[1:])


def part2(nums):
    return count_ways(0, nums)


def main(f):
    nums = [int(line.strip()) for line in f]
    nums.sort()
    print(part1(nums))
    print(part2(tuple(nums)))
