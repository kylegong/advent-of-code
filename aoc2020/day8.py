def execute(cmds):
    executed = set()
    acc = 0
    i = 0
    while i < len(cmds):
        print(i, acc, cmds[i])
        if i in executed:
            return (acc, False)
        executed.add(i)
        op, val = cmds[i]
        if op == "acc":
            acc += val
        if op == "jmp":
            i += val
        else:
            i += 1
    return (acc, True)


def mutate(cmds):
    for i, cmd in enumerate(cmds):
        op, val = cmd
        if op == "jmp":
            yield cmds[:i] + [["nop", val]] + cmds[i+1:]
        elif op == "nop":
            yield cmds[:i] + [["jmp", val]] + cmds[i+1:]


def part1(cmds):
    return execute(cmds)


def part2(cmds):
    for mutated_cmds in mutate(cmds):
        acc, terminated = execute(mutated_cmds)
        if terminated:
            return acc


def parse(line):
    """
    >>> parse("acc -14")
    ['acc', -14]
    >>> parse("jmp +362")
    ['jmp', 362]
    >>> parse("nop +236")
    ['nop', 236]
    """
    op, val = line.split(" ")
    return [op, int(val)]


def main(f):
    cmds = [parse(line.strip()) for line in f]
    print(part1(cmds))
    print(part2(cmds))
