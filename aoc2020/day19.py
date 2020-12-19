from shared import utils

def part1(rules, messages):
    all_matches = []
    for message in messages:
        matches = match(rules, rules[0], message)
        for m in matches:
            if m == message:
                all_matches.append(message)
    return len(all_matches)


def part2(rules, messages):
    rules[8] = "42 | 42 8"
    rules[11] = "42 31 | 42 11 31"
    all_matches = []
    for message in messages:
        matches = match(rules, rules[0], message)
        for m in matches:
            if m == message:
                all_matches.append(message)
    return len(all_matches)

def parseRules(lines):
    rules = {}
    for line in lines:
        i, rule = line.split(": ")
        rules[int(i)] = rule
    return rules

def match(rules, rule, message):
    if rule == '"a"':
        if message.startswith("a"):
            return ["a"]
        return ""
    elif rule == '"b"':
        if message.startswith("b"):
            return ["b"]
        return []
    if "|" in rule:
        matches = []
        for opt in rule.split(" | "):
            m = match(rules, opt, message)
            if m:
                matches.extend(m)
        return matches
    progress = [("", message)]
    for rule_no in rule.split(" "):
        new_progress = []
        for prev_m, remainder in progress:
            matches = match(rules, rules[int(rule_no)], remainder)
            new_progress.extend([(prev_m + m, remainder[len(m):]) for m in matches])
        progress = new_progress
    return [m for m, rest in progress if m]


def main(f):
    lines = [line.strip() for line in f]
    rules, messages = utils.group(lines)
    rules = parseRules(rules)
    print(part1(rules, messages))
    print(part2(rules, messages))
