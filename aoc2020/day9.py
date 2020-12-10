
def part1(nums):
    for i, n in enumerate(nums):
        if i < 25:
            continue
        if not n in sums(nums[i-25:i]):
            return n


def sums(nums):
    sums = set()
    for n in nums:
        for m in nums:
            if n != m:
                sums.add(n + m)
    return sums


def part2(nums, p1):
    contig = []
    for n in nums:
        contig.append(n)
        while sum(contig) >= p1:
            if len(contig) > 1 and sum(contig) == p1:
                return max(contig) + min(contig)
            contig = contig[1:]


def main(f):
    nums = [int(line.strip()) for line in f]
    p1 = part1(nums)
    print(p1)
    print(part2(nums, p1))
