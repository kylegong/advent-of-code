class Rules:
    def __init__(self, rules):
        self.ruleMap = {}
        for color, contents in rules:
            self.ruleMap[color] = contents

    def countContents(self, color):
        contents = self.ruleMap[color]
        return sum([v + v*self.countContents(c) for c, v in contents.items()])

    def colors(self):
        return self.ruleMap.keys()

    def canContain(self, color, contColor):
        """
        >>> rules = Rules([['a': {'b': 3, 'c': 2}], ['d': {'a': 1}], ['e': {'d': 5}]])
        >>> rules.canContain('a', 'b')
        True
        >>> rules = Rules([['a': {'b': 3, 'c': 2}], ['d': {'a': 1}], ['e': {'d': 5}]])
        >>> rules.canContain('d', 'a')
        True
        >>> rules = Rules([['a': {'b': 3, 'c': 2}], ['d': {'a': 1}], ['e': {'d': 5}]])
        >>> rules.canContain('d', 'b')
        True
        >>> rules = Rules([['a': {'b': 3, 'c': 2}], ['d': {'a': 1}], ['e': {'d': 5}]])
        >>> rules.canContain('e', 'a')
        True
        >>> rules = Rules([['a': {'b': 3, 'c': 2}], ['d': {'a': 1}], ['e': {'d': 5}]])
        >>> rules.canContain('b', 'd')
        False
        >>> rules = Rules([['a': {'b': 3, 'c': 2}], ['d': {'a': 1}], ['e': {'d': 5}]])
        >>> rules.canContain('c', 'a')
        False
        """
        if not color in self.ruleMap:
            return False
        for allowColor in self.ruleMap[color]:
            if contColor == allowColor:
                return True
            if self.canContain(allowColor, contColor):
                return True
        return False


def part1(rules):
    colors = []
    for color in rules.colors():
        if rules.canContain(color, 'shiny gold'):
            colors.append(color)
    return len(colors)


def part2(rules):
    return rules.countContents('shiny gold')


def parse(line):
    """
    >>> parse("light red bags contain 1 bright white bag, 2 muted yellow bags.")
    ['light red', {'bright white': 1, 'muted yellow': 2}]
    """
    line = line.replace("bags", "bag")
    color, contentDesc = line.split(" bag contain ")
    contents = {}
    if contentDesc != "no other bag.":
        for desc in contentDesc.split(", "):
            count = int(desc.split(" ")[0])
            ccolor = desc[len(str(count))+1:]
            ccolor = ccolor.replace(" bag.", "").replace(" bag", "")
            contents[ccolor] = count
    return [color, contents]


def main(f):
    rules = Rules([parse(line.strip()) for line in f])
    print(part1(rules))
    print(part2(rules))
