def count(nums, turn):
    history = {n:i for i, n in enumerate(nums)}
    cur = 0
    for n in range(len(nums), turn-1):
        last = history.get(cur, -1)
        next_n = 0
        if last != -1:
            next_n = n-last
        history[cur] = n
        cur = next_n
    return cur

def part1(nums):
    return count(nums, 2020)

def part2(nums):
    return count(nums, 30000000)


def main(f):
    nums = [int(n) for n in f.read().split(",")]
    print(part1(nums))
    print(part2(nums))
