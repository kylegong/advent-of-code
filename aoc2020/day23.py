def part1(nums, moves):
    for _ in range(moves):
        nums = turn(nums)
    return label(nums)


def label(nums):
    one = nums.index(1)
    return ''.join(str(n) for n in nums[one+1:] + nums[:one])


def turn(nums):
    cur = nums[0]
    pickup = nums[1:4]
    rest = nums[4:]
    dest = cur - 1
    while not dest in rest:
        dest -= 1
        if dest < min(rest):
            dest = max(rest)
    dest_i = rest.index(dest)
    return rest[:dest_i] + [dest] + pickup + rest[dest_i+1:] + [cur]


def add_cups(nums, total):
    return nums + list(range(max(nums)+1, total+1))


def part2(nums):
    nums = add_cups(nums, 1_000_000_000)
    for n in range(10_000_000_000):
        if n % 10000:
            print(n)
        nums = turn(nums)
    one = nums.index(1)
    return nums[one+1] * nums[one+2]


def main(f):
    line = f.readline().strip()
    #line = "389125467"
    nums = [int(n) for n in line]
    print(part1(nums, 100))
    print(part2(nums))
