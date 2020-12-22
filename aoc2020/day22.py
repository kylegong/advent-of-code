from shared import utils


def part1(d1, d2):
    while len(d1) > 0 and len(d2) > 0:
        d1, d2 = spoils(d1, d2, d1[0] > d2[0])
    return score(d1 + d2)


def score(deck):
    score = 0
    for i, c in enumerate(reversed(deck)):
        score += (i+1)*c
    return score


def spoils(d1, d2, did_p1_win):
    if did_p1_win:
        return d1[1:] + [d1[0], d2[0]], d2[1:]
    return d1[1:], d2[1:] + [d2[0], d1[0]]


def part2(d1, d2):
    d1, d2, did_p1_win = game(d1, d2)
    if did_p1_win:
        return score(d1)
    return score(d2)


def game(d1, d2):
    history = set()
    while True:
        if len(d1) == 0 or len(d2) == 0:
            return d1, d2, len(d2) == 0
        if (tuple(d1), tuple(d2)) in history:
            return d1, d2, True
        history.add((tuple(d1), tuple(d2)))
        if len(d1) > d1[0] and len(d2) > d2[0]:
            _, _, did_p1_win = game(d1[1:d1[0]+1], d2[1:d2[0]+1])
            d1, d2 = spoils(d1, d2, did_p1_win)
            continue
        d1, d2 = spoils(d1, d2, d1[0] > d2[0])


def play2(d1, d2):
    if d1[0] > d2[0]:
        return d1[1:] + [d1[0], d2[0]], d2[1:]
    else:
        return d1[1:], d2[1:] + [d2[0], d1[0]]


def parseDecks(groups):
    return [[int(n) for n in group[1:]] for group in groups]


def main(f):
    d1, d2 = parseDecks(utils.group([line.strip() for line in f]))
    print(part1(d1, d2))
    print(part2(d1, d2))
