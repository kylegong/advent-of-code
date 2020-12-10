from shared import utils


def part1(groups):
    count = 0
    for group in groups:
        answers = set([q for ans in group for q in ans])
        count += len(answers)
    return count


def part2(groups):
    count = 0
    for group in groups:
        answers = [set([a for a in ans]) for ans in group]
        all_ans = answers[0].intersection(*answers[1:])
        count += len(all_ans)
    return count


def main(f):
    groups = utils.group([line.strip() for line in f])
    print(part1(groups))
    print(part2(groups))
