def part1(lines):
    return sum(evalLR(parse(line)) for line in lines)


def part2(lines):
    return sum(evalAM(parse(line)) for line in lines)


def evalAM(exp):
    '''
    >>> evalLR([1, '+', 2])
    3
    >>> evalLR([2, '*', 3])
    6
    >>> evalAM([2, '*', 3, '+', 1])
    8
    >>> evalAM([1, '+', 2, '*', 3, '+', 4, '*', 5, '+', 6])
    231
    '''
    if isinstance(exp, int):
        return exp
    if len(exp) > 3:
        for i, t in enumerate(exp):
            if t == '+':
                return evalAM(exp[:i-1] + [evalAM(exp[i-1:i+2])] + exp[i+2:])
        return evalAM([evalAM(exp[:3])] + exp[3:])
    if len(exp) == 3:
        a, op, b = exp
        if op == '+':
            return evalAM(a) + evalAM(b)
        if op == '*':
            return evalAM(a) * evalAM(b)
    raise ValueError([exp])


def evalLR(exp):
    '''
    >>> evalLR([1, '+', 2])
    3
    >>> evalLR([2, '*', 3])
    6
    >>> evalLR([[1, '+', 2], '*', 3])
    9
    >>> evalLR([[1, '+', [2, '*', 3]], '+', [4, '*', [5, '+', 6]]])
    51
    >>> evalLR([2, '*', 3, '+', 1])
    7
    >>> evalLR([1, '+', 2, '*', 3, '+', 4, '*', 5, '+', 6])
    71
    '''
    if isinstance(exp, int):
        return exp
    if len(exp) == 3:
        a, op, b = exp
        if op == '+':
            return evalLR(a) + evalLR(b)
        if op == '*':
            return evalLR(a) * evalLR(b)
    if len(exp) > 3:
        return evalLR([evalLR(exp[:3])] + exp[3:])
    raise ValueError(exp)


def parse(exp):
    '''
    >>> parse('1 + 2')
    [1, '+', 2]
    >>> parse('2 * 3')
    [2, '*', 3]
    >>> parse('1 + 2 * 3')
    [1, '+', 2, '*', 3]
    >>> parse('1 + (2 * 3) + (4 * (5 + 6))')
    [1, '+', [2, '*', 3], '+', [4, '*', [5, '+', 6]]]
    '''
    stack = (None, [])
    for token in tokenize(exp):
        if token.isdigit():
            stack[1].append(int(token))
            continue
        if token in ('+', '*'):
            stack[1].append(token)
        if token == '(':
            stack = (stack, [])
        if token == ')':
            stack[0][1].append(stack[1])
            stack = stack[0]
    return stack[1]


def tokenize(exp):
    '''
    >>> tokenize('1 + 2')
    ['1', '+', '2']
    >>> tokenize('2 * 3')
    ['2', '*', '3']
    >>> tokenize('1 + 2 * 3')
    ['1', '+', '2', '*', '3']
    >>> tokenize('1 + (2 * 3) + (4 * (5 + 6))')
    ['1', '+', '(', '2', '*', '3', ')', '+', '(', '4', '*', '(', '5', '+', '6', ')', ')']
    '''
    tokens = []
    splits = exp.split(" ")
    for s in splits:
        if s in ('+', '*'):
            tokens.append(s)
            continue
        left = []
        right = []
        while not s.isdigit():
            if s.startswith('('):
                left.append('(')
                s = s[1:]
            if s.endswith(')'):
                right.append(')')
                s = s[:-1]
        tokens.extend(left + [s] + right)
    return tokens


def main(f):
    lines = [line.strip() for line in f]
    print(part1(lines))
    print(part2(lines))
