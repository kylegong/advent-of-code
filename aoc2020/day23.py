def label(nums):
    """
    >>> label([5, 8, 3, 7, 4, 1, 9, 2, 6])
    '92658374'
    """
    ind = nums.index(1)
    return ''.join(str(n) for n in nums[ind+1:] + nums[:ind])


def turns(nums, numTurns):
    min_n, max_n = min(nums), max(nums)
    after = {}
    for i, n in enumerate(nums[:-1]):
        after[n] = nums[i+1]
    after[nums[-1]] = nums[0]
    cur = nums[0]
    for _ in range(numTurns):
        turn(after, cur, min_n, max_n)
        cur = after[cur]
    last = 1
    out = []
    for _ in nums:
        out.append(after[last])
        last = after[last]
    return out


def turn(after, cur, min_n, max_n):
    pickup = {}
    last = cur
    for _ in range(3):
        last = after[last]
        pickup[last] = after[last]
    dest = cur - 1
    if dest < min_n:
        dest = max_n
    while dest in pickup:
        dest -= 1
        if dest < min_n:
            dest = max_n
    afterCur = after[last]
    after[last] = after[dest]
    after[dest] = after[cur]
    after[cur] = afterCur


def add_cups(nums, total):
    """
    >>> add_cups([4, 3, 1, 2], 6)
    [4, 3, 1, 2, 5, 6]
    """
    return nums + list(range(max(nums)+1, total+1))


def part1(nums):
    out = turns(nums, 100)
    return label(out)


def part2(nums):
    nums = add_cups(nums, 1_000_000)
    out = turns(nums, 10_000_000)
    return out[0] * out[1]


def main(f):
    line = f.readline().strip()
    # line = "389125467"
    nums = [int(n) for n in line]
    print(part1(nums))
    print(part2(nums))
